import pytest

from app.pricing import discount_pct, quote


def test_no_code():
    assert discount_pct() == 0


def test_promo_code():
    assert discount_pct("NEWS5") == pytest.approx(0.05)
    assert discount_pct("welcome10") == pytest.approx(0.10)


def test_unknown_code():
    assert discount_pct("FREESTUFF") == 0


def test_creator_code():
    assert discount_pct(None, "FITFAM30") == pytest.approx(0.30)


def test_creator_with_promo():
    assert discount_pct("WELCOME10", "FITFAM30") == pytest.approx(0.40)


def test_quote():
    q = quote([(85.0, 1), (28.0, 2)], "LOYAL15")
    assert q["subtotal"] == 141.0
    assert q["discount"] == 21.15
