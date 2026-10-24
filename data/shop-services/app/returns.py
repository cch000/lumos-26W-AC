"""Return eligibility, used by the support team's return form."""
from datetime import date

STANDARD_WINDOW_DAYS = 30
# Creator promo orders: extended window, required by the creator agency contract (from Feb 2023)
CREATOR_WINDOW_DAYS = 60


def _parse(d):
    return d if isinstance(d, date) else date.fromisoformat(str(d)[:10])


def days_since_order(order_date, today):
    return (today - order_date).days


def check_eligibility(order, today=None):
    today = _parse(today) if today else date.today()
    order_date = _parse(order["order_date"])

    if order.get("status") == "returned":
        return {"eligible": False, "reason": "already returned"}

    if order.get("creator_code"):
        window = CREATOR_WINDOW_DAYS
        age = (order_date - today).days
    else:
        window = STANDARD_WINDOW_DAYS
        age = days_since_order(order_date, today)

    if age <= window:
        return {"eligible": True, "days_since_order": age, "window_days": window}
    return {"eligible": False, "days_since_order": age, "window_days": window,
            "reason": f"outside {window}-day return window"}
