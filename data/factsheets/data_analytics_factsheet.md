# Track A · Data & Analytics factsheet
*Everything in `analysis_ready/` is clean, joined-ready and documented in `analysis_ready/README.md`. `raw_systems/` holds the original system exports if you want to rebuild it yourself (optional).*

## What you have
| File | Rows | Grain |
|---|---|---|
| `orders.csv` | 50,507 | one row per order, Jan 2022 – Dec 2023 (channel, codes, discount, shipping, return, profit) |
| `order_lines.csv` | 83,343 | one row per order × SKU |
| `customers.csv` | 19,212 | one row per customer (acquisition channel, region, ZIP3, signup date) |
| `skus.csv` | 200 | one row per SKU (price, cost, sales, margin, stock, overflow storage) |
| `pnl_monthly.csv` | 24 | monthly P&L incl. marketing, support, G&A (Dec 2023 = PRELIMINARY) |
| `marketing_monthly.csv` | 96 | spend by channel and month |
| `ops_monthly.csv` | 24 | warehouse staff, overtime, errors, incidents, delivery and refund times |
| `support_monthly.csv` | 24 | tickets by category and month |
| `overflow_storage_rate_card.csv` | 8 | StoreSafe fee per unit per month |

## Official KPIs circulating in the company (verify before you use them)
| Claim | Source |
|---|---|
| "Creator program ROAS 2.3x, our best channel for new customers" | CMO / Pulse |
| "Returns hit a record low in December (4.8%)" | Ops weekly |
| "Klarna customers return 9.5% of orders vs 6.5%; we should drop BNPL" | Finance analyst |
| "Eco products average 31% margin vs 39%; the Terra line is a drag" | Product meeting |
| "Supplements need climate-controlled storage; cut the category" | Ops |
| "West Coast shipping costs ~$15/order because it's far; we need a West Coast warehouse" | Logistics |

## Questions your partner track may ask you
- What does a creator customer actually earn us after discounts, returns and costs, and do they come back?
- How big is each leak in $ per year?
- Did something change on a specific date? (Look at weekly or monthly trends, not only yearly totals.)


---
*Source: board-pack extract of 5 Jan 2024 (`analysis_ready/`). December 2023 is preliminary (returns arrive up to 30 days after purchase, longer for creator orders).*
