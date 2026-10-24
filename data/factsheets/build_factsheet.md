# Track E · Software & Infrastructure factsheet: Zenith's in-house services
*Compiled by IT (Brendan Ohs). Code and config: `shop-services/`.*

## System inventory
| Service | What it does | Built by / when | Owner today |
|---|---|---|---|
| Storefront | Shopify theme + `web/cart.js` | Alex Thompson, BF22 relaunch (14 Nov 2022) | Marketing (Shopify admin) |
| Pricing service | Applies promo and creator codes at checkout | Alex Thompson, Nov 2022 | — |
| Shipping-rate service | ZIP → carrier zone → label service and rate | Alex Thompson, Nov 2022 | — |
| Return eligibility | Approves return requests (30 days; 60 for creator orders) | Alex Thompson, Nov 2022 | — |
| Shipping notifications | Cron job: "your order has shipped" e-mail with tracking link | Alex Thompson, Nov 2022; server moved 14 Feb 2023 | — |
| Pick-rate alert bot | Posts to Slack when the picking error rate is too high | Alex Thompson, Nov 2022 | IT (Slack → Teams cutover 2 Jan 2024) |
| Server | One VPS, nginx + the app | Brendan Ohs | IT |

## Symptoms the business has reported (unexplained)
| Since | Symptom | Reported by |
|---|---|---|
| Nov 2022 | Creator-code orders get up to 60% off (avg 39% in 2023) | CX, Finance |
| Nov 2022 | 75% of West Coast parcels ship Express Air (avg $15.01/order) | Logistics |
| Nov 2022 | Items per order fell from ~2.0 to ~1.6 | E-commerce |
| Mar 2023 | "Where is my order?" tickets per 100 orders jumped from ~3 to ~12 | CX |
| 2023 | Creator-order returns approved after day 60 | CX, Legal |
| 2023 | Picking errors up to 6%, but the Slack alert bot never posted | Ops |
| Oct 2023 | Intermittent 502 errors after a deploy | IT |

## Scale
~3,158 orders/month in 2023 (peak 4,249 in December), i.e. a few orders per hour.


---
*Source: board-pack extract of 5 Jan 2024 (`analysis_ready/`). December 2023 is preliminary (returns arrive up to 30 days after purchase, longer for creator orders).*
