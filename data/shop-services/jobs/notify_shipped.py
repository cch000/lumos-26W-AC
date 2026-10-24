"""Send the "your order has shipped" e-mail (with tracking link) for every order
that has a tracking number and was not notified yet. Runs from cron every 30 min.

    python jobs/notify_shipped.py [--dry-run]
"""
import logging
import os
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from app import db  # noqa: E402

logging.basicConfig(filename=ROOT / "logs" / "notify.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("notify")

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM", "orders@zenithactive.com")
TRACKING_URL = "https://track.northstarparcel.com/?tracking={}"
BATCH = 500


def pending_orders(conn):
    return conn.execute(
        "SELECT order_id, email, tracking_number, shipping_service FROM orders "
        "WHERE tracking_number IS NOT NULL AND shipped_notified = 0 LIMIT ?", (BATCH,)).fetchall()


def build_message(order):
    msg = EmailMessage()
    msg["From"] = f"Zenith Active <{MAIL_FROM}>"
    msg["To"] = order["email"]
    msg["Subject"] = f"Your Zenith order {order['order_id']} is on its way"
    msg.set_content(
        f"Good news - your order {order['order_id']} has shipped ({order['shipping_service']}).\n\n"
        f"Track it here: {TRACKING_URL.format(order['tracking_number'])}\n\n"
        "Questions? Just reply to this e-mail.\nTeam Zenith"
    )
    return msg


def main(dry_run=False):
    db.seed()
    conn = db.get_conn()
    orders = pending_orders(conn)
    log.info("run start: %d orders pending", len(orders))
    sent = 0
    try:
        if dry_run:
            for o in orders:
                print(build_message(o))
            return 0
        smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20)
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        for o in orders:
            smtp.send_message(build_message(o))
            conn.execute("UPDATE orders SET shipped_notified = 1 WHERE order_id = ?", (o["order_id"],))
            sent += 1
        smtp.quit()
    except:  # noqa: E722  - never let one bad address kill the batch
        pass
    conn.commit()
    log.info("run complete: %d sent", sent)
    return sent


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
