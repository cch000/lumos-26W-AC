"""SQLite storage. Orders come from the Shopify order export (data/*.csv, see scripts/seed_db.py)."""
import csv
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = Path(os.getenv("DATABASE_PATH", DATA_DIR / "zenith.db"))
if not DB_PATH.is_absolute():
    DB_PATH = ROOT / DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    order_date TEXT,
    customer_id TEXT,
    email TEXT,
    zip3 TEXT,
    items INTEGER,
    units INTEGER,
    subtotal REAL,
    promo_code TEXT,
    creator_code TEXT,
    discount_pct REAL,
    discount REAL,
    total REAL,
    shipping_service TEXT,
    shipping_cost REAL,
    status TEXT,
    tracking_number TEXT,
    shipped_notified INTEGER DEFAULT 0,
    return_date TEXT
);
CREATE TABLE IF NOT EXISTS order_items (
    order_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    unit_price REAL
);
"""


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _rows(name):
    with open(DATA_DIR / name, newline="") as f:
        return list(csv.DictReader(f))


def seed(force=False):
    if DB_PATH.exists():
        if not force:
            return
        DB_PATH.unlink()
    conn = get_conn()
    conn.executescript(SCHEMA)
    conn.executemany("INSERT INTO products VALUES (?,?,?,?)",
                     [(p["ProductID"], p["ProductName"], p["Category"], float(p["Price"]))
                      for p in _rows("products.csv")])
    conn.executemany(
        "INSERT INTO orders VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        [(o["OrderID"], o["OrderDate"], o["CustomerID"], o["Email"], o["Zip3"], int(o["Items"]),
          int(o["Units"]), float(o["Subtotal"]), o["PromoCode"] or None, o["CreatorCode"] or None,
          float(o["DiscountPct"]), float(o["Discount"]), float(o["Total"]), o["ShippingService"],
          float(o["ShippingCost"]), o["Status"], o["TrackingNumber"], int(o["ShippedNotified"]),
          o["ReturnDate"] or None)
         for o in _rows("orders_sample.csv")])
    conn.executemany("INSERT INTO order_items VALUES (?,?,?,?)",
                     [(i["OrderID"], i["ProductID"], int(i["Quantity"]), float(i["UnitPrice"]))
                      for i in _rows("order_items.csv")])
    conn.commit()
    conn.close()
