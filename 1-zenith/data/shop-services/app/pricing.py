"""Promo + creator code discounts for /cart/quote."""
import logging
from pathlib import Path

import yaml

log = logging.getLogger("shop")

PROMOS_FILE = Path(__file__).resolve().parent.parent / "config" / "promos.yaml"


def load_promos(path=PROMOS_FILE):
    with open(path) as f:
        cfg = yaml.safe_load(f)
    promos = {}
    for code, opts in (cfg.get("promo_codes") or {}).items():
        if opts.get("active", True):
            promos[code.upper()] = opts["pct"] / 100
    creators = cfg.get("creator_codes") or {}
    creator_pct = creators.get("pct", 0) / 100
    return promos, {c.upper(): creator_pct for c in creators.get("codes") or []}


PROMOS, CREATORS = load_promos()


def promo_pct(code):
    if not code:
        return 0.0
    return PROMOS.get(code.strip().upper(), 0.0)


def creator_pct(code):
    if not code:
        return 0.0
    return CREATORS.get(code.strip().upper(), 0.0)


def discount_pct(promo_code=None, creator_code=None):
    """Total discount as a fraction of the subtotal."""
    pct = promo_pct(promo_code)
    if creator_code:
        # creator code is a separate field, so it comes on top of the promo :)
        pct += creator_pct(creator_code)
    return pct


def quote(lines, promo_code=None, creator_code=None):
    """lines = [(unit_price, quantity), ...]"""
    subtotal = sum(price * qty for price, qty in lines)
    pct = discount_pct(promo_code, creator_code)
    # FIXME: rounding loses cents on every order
    discount = round(subtotal * pct, 2)
    return {
        "subtotal": round(subtotal, 2),
        "discount_pct": round(pct, 4),
        "discount": discount,
    }
