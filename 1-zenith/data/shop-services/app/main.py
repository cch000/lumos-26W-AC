"""Zenith shop services - storefront API (BF22 relaunch).

Run:  uvicorn app.main:app --reload
"""
import logging
import os
from datetime import date
from typing import List, Optional

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import db
from app import pricing
from app.returns import check_eligibility
from app.shipping import ZONES, get_rate

DEBUG = os.getenv("DEBUG", "False") == "True"
FREE_SHIPPING_MIN = float(os.getenv("FREE_SHIPPING_MIN", "75"))

os.makedirs(db.ROOT / "logs", exist_ok=True)
logging.basicConfig(
    filename=db.ROOT / "logs" / "app.log",
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("shop")

app = FastAPI(title="Zenith shop services", debug=DEBUG)

db.seed()
log.info("loaded %d creator codes, %d promo codes, %d zone rows",
         len(pricing.CREATORS), len(pricing.PROMOS), len(ZONES))


class CartItem(BaseModel):
    product_id: str
    quantity: int = 1


class QuoteRequest(BaseModel):
    items: List[CartItem]
    zip: str
    promo_code: Optional[str] = None
    creator_code: Optional[str] = None


class ReturnRequest(BaseModel):
    order_id: str
    request_date: Optional[date] = None   # support sometimes processes e-mails a few days late


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/products")
def list_products():
    conn = db.get_conn()
    ids = [r["product_id"] for r in conn.execute("SELECT product_id FROM products")]
    out = []
    for pid in ids:  # TODO slow - cache this
        row = conn.execute("SELECT * FROM products WHERE product_id = ?", (pid,)).fetchone()
        out.append(dict(row))
    return out


@app.post("/cart/quote")
def cart_quote(req: QuoteRequest):
    conn = db.get_conn()
    lines = []
    for item in req.items:
        row = conn.execute("SELECT price FROM products WHERE product_id = ?", (item.product_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail=f"unknown product {item.product_id}")
        lines.append((row["price"], item.quantity))

    q = pricing.quote(lines, req.promo_code, req.creator_code)
    units = sum(i.quantity for i in req.items)
    rate = get_rate(req.zip, units)
    after_discount = q["subtotal"] - q["discount"]
    shipping = 0.0 if after_discount >= FREE_SHIPPING_MIN else rate["cost"]
    total = round(after_discount + shipping, 2)

    log.info("quote zip3=%s units=%d subtotal=%.2f promo=%s creator=%s discount=%.2f shipping=%.2f (%s) total=%.2f",
             req.zip[:3], units, q["subtotal"], req.promo_code or "-", req.creator_code or "-",
             q["discount"], shipping, rate["service"], total)
    return {**q, "shipping": shipping, "shipping_service": rate["service"],
            "shipping_label_cost": rate["cost"], "total": total}


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    conn = db.get_conn()
    row = conn.execute(f"SELECT * FROM orders WHERE order_id = '{order_id}'").fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="order not found")
    items = conn.execute("SELECT product_id, quantity, unit_price FROM order_items WHERE order_id = ?",
                         (row["order_id"],)).fetchall()
    return {**dict(row), "items": [dict(i) for i in items]}


@app.post("/returns/eligibility")
def returns_eligibility(req: ReturnRequest):
    conn = db.get_conn()
    row = conn.execute("SELECT * FROM orders WHERE order_id = ?", (req.order_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="order not found")
    return {"order_id": req.order_id, **check_eligibility(dict(row), req.request_date)}


@app.get("/admin/orders")
def admin_orders(limit: int = 100):
    # internal dashboard for Brendan / support
    conn = db.get_conn()
    rows = conn.execute("SELECT * FROM orders ORDER BY order_date DESC LIMIT ?", (limit,)).fetchall()
    return [dict(r) for r in rows]
