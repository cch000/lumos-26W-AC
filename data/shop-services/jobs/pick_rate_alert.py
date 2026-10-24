"""Monthly warehouse picking-error alert -> #warehouse-ops (Slack).

Reads the WMS monthly export (data/wms_monthly.csv, dropped there by the WMS on the 1st)
and posts to Slack if last month's picking error rate is above the threshold.
Cron: 07:00 on the 1st of every month.

    python jobs/pick_rate_alert.py [YYYY-MM]
"""
import csv
import logging
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

logging.basicConfig(filename=ROOT / "logs" / "pick_rate_alert.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("pick_rate_alert")

WMS_EXPORT = ROOT / "data" / "wms_monthly.csv"
THRESHOLD = 5  # alert if more than 5% of orders have a picking error
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def load_months(path=WMS_EXPORT):
    with open(path, newline="") as f:
        return {r["Month"]: r for r in csv.DictReader(f)}


def error_rate(row):
    return int(row["PickingErrors"]) / int(row["OrdersPicked"])


def post_alert(text):
    if not WEBHOOK_URL:
        log.warning("no SLACK_WEBHOOK_URL set, alert not sent: %s", text)
        return
    requests.post(WEBHOOK_URL, json={"text": text}, timeout=10)


def check(month=None):
    months = load_months()
    month = month or max(months)
    rate = error_rate(months[month])
    status = "ALERT" if rate > THRESHOLD else "OK"
    log.info("%s error_rate=%.3f threshold=%s -> %s", month, rate, THRESHOLD, status)
    if status == "ALERT":
        post_alert(f":rotating_light: Picking error rate {month}: {rate:.1%} (threshold {THRESHOLD}%)")
    return rate, status


if __name__ == "__main__":
    check(sys.argv[1] if len(sys.argv) > 1 else None)
