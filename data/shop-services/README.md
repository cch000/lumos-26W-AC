# zenith-shop-services

Small services around the Zenith Active Shopify store, built for the **BF22 relaunch**
(went live 14 Nov 2022). Shopify does the storefront and checkout; this repo does the parts
Shopify couldn't do the way we wanted:

| What | Where |
|---|---|
| Discount engine (promo codes + creator codes) | `app/pricing.py`, `config/promos.yaml` |
| Shipping rates (ZIP -> NorthStar Parcel zone -> rate) | `app/shipping.py`, `config/shipping_zones.csv` |
| Return eligibility for the support return form | `app/returns.py` |
| Storefront API used by the theme (`/cart/quote`, ...) | `app/main.py` |
| Cart drawer / "added to cart" modal for the theme | `web/cart.js` |
| "Your order has shipped" e-mails | `jobs/notify_shipped.py` (cron) |
| Warehouse picking-error alert to Slack | `jobs/pick_rate_alert.py` (cron) |

Built by Alex Thompson (freelance, thompson-dev.io). Server: Brendan Ohs (IT).

## Setup (local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/seed_db.py          # optional, the app builds data/zenith.db on first start
uvicorn app.main:app --reload --port 5000
```

Then open http://localhost:5000/docs.

Tests: `python -m pytest`

To try the cart script: `python -m http.server -d web 8080` and open http://localhost:8080/product.html

## API

| Method | Path | Used by |
|---|---|---|
| POST | `/cart/quote` | theme checkout step: `{items:[{product_id, quantity}], zip, promo_code, creator_code}` -> subtotal, discount, shipping, total |
| GET | `/orders/{order_id}` | support |
| POST | `/returns/eligibility` | support return form: `{order_id}` |
| GET | `/products` | theme (prices) |
| GET | `/admin/orders` | internal dashboard |

## Production

- One VM, repo checked out at `/opt/zenith`, `docker compose up -d` (app + nginx).
- nginx serves `api.zenithactive.com` and `/static/cart.js` for the theme.
- Cron jobs from `crontab` (install with `crontab crontab`).
- Secrets in `.env` (see `.env.example`).

## Discounts

- Promo codes: one per order (WELCOME10, NEWS5, LOYAL15, flash sale codes).
- Creator codes: entered in the separate creator-code field. Marketing sends new codes,
  add them to `config/promos.yaml` and restart the app.
- Flash sale code (ZENITH30): set `active: true` on Friday, back to `false` on Monday.

## Handover notes (Alex, 2 Dec 2022)

- BF22 went fine. Peak was ~140 orders/hour on Black Friday, SQLite didn't blink.
- `cart.js` still has the BF22 checkout test in `addToCart()` - revert after Cyber Monday,
  I'll do it if you want, just ping me.
- Zone table is from the NorthStar Parcel zone chart for origin 088.
- The shipped e-mails go out through PostLoft (transactional mail relay) (`SMTP_*` in `.env`), cron every 30 min.
- I'm on another project from January, available for small paid changes.

## Server move (Brendan, 14 Feb 2023)

- Moved everything to the new VM (Ubuntu 22.04). Repo now in `/opt/zenith`.
- App runs with uvicorn in Docker now (was gunicorn).
- Cleaned up the job names (`notify.py` -> `notify_shipped.py`).
- Mail goes through Microsoft 365 now, new SMTP settings in `.env`.
- Creator codes updated to 30% for the agency contract (Alex did the code change, 3 Feb).

## Roadmap

- [ ] Migrate SQLite -> Postgres, run on Kubernetes so we can scale for next BF
- [ ] Split into microservices (pricing, shipping, notifications)
- [ ] Move storefront to headless Next.js
- [ ] Fix rounding in pricing (see FIXME)
- [ ] Cache `/products`
- [ ] Bump dependencies, add linting
- [ ] Order status page ("where is my order")
