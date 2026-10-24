# analysis_ready/: data dictionary

Clean, documented extracts from Zenith's systems, pulled on **5 January 2024** for the board pack. Everyone can use them from minute 0, with Excel, Google Sheets, Python, R or anything else. The original system exports are in `../raw_systems/` (optional).

**December 2023 is preliminary.** Returns are booked when the parcel comes back, which can be up to 30 days after purchase (60 for creator-code orders). Some December orders that will be returned are not yet flagged.

## orders.csv: one row per order (Jan 2022 – Dec 2023)
| Column | Meaning |
|---|---|
| OrderID, OrderDate, CustomerID | identifiers; date of purchase |
| AcquisitionChannel | channel that first acquired the customer (Organic, Search, Paid Social, Influencer) |
| Region, Zip3 | shipping region (East, North, South, West) and first 3 digits of the ZIP code |
| CarrierZone | NorthStar Parcel zone from Edison NJ (2 = near … 8 = farthest) |
| Items, Units | distinct SKUs in the order; total units |
| GrossSales | list price × units, before discounts |
| PromoCode | WELCOME10, NEWS5, LOYAL15, ZENITH30 (flash-sale weekends) or empty |
| CreatorCode | creator code used (e.g. FITFAM30) or empty |
| DiscountPct, DiscountAmount | total discount applied at checkout (share of gross; $) |
| ChargedAmount | what the customer paid (gross − discount) |
| PaymentMethod, PaymentFee | Credit Card, PayPal, Apple Pay, Klarna (BNPL); processor fee in $ |
| ShippingService, ShippingCost | label service printed (Ground / Express Air) and what Zenith paid the carrier |
| ReturnFlag, ReturnDays | 1 if the order was returned (booked by 5 Jan 2024); days after purchase |
| ReturnLabel | prepaid return label paid by Zenith ($6.50) |
| NetRevenue | ChargedAmount, or 0 if returned (full refund) |
| COGS | product cost; for returned orders 60% of the cost is written off (40% restocked) |
| Profit | NetRevenue − COGS − ShippingCost − ReturnLabel − PaymentFee (order contribution, before warehouse labor, marketing and overheads) |

## order_lines.csv: one row per order × SKU
OrderID, ProductID, Quantity, UnitPrice (list), UnitCost. Discounts and returns apply at order level (see orders.csv).

## customers.csv: one row per customer who ordered in 2022–2023
CustomerID, AcquisitionChannel, Region, Zip3, SignupDate (first account creation; customers from before 2022 have older dates).

## skus.csv: one row per SKU (FY2022–2023 totals)
ProductID, ProductName, Category, Color, EcoFriendly, ListPrice, UnitCost, UnitsSold, NetRevenue, COGS, ReturnRate, GrossMarginPct ((NetRevenue − COGS) / NetRevenue), OnHandUnits (31 Dec 2023), AvgDaysInInventory, InOverflowStorage (stored at StoreSafe since April 2023), OverflowStorageFeePerUnitMonth (from the rate card).

## pnl_monthly.csv: monthly P&L
Orders, GrossSales, Discounts, Refunds, NetRevenue, COGS, Shipping, ReturnLabels, PaymentFees, **ContributionMargin**, WarehouseLabor, WarehouseRent, ReshipmentCost (re-sending wrong items), OverflowStorage, SupportCost, Marketing, GeneralAdmin, **EBITDA**, Status (CLOSED / PRELIMINARY).

## marketing_monthly.csv
Month, Channel, Spend. "Influencer" = creator program (Pulse agency fee from Feb 2023; small direct creator deals before).

## ops_monthly.csv: warehouse (Edison NJ)
Month, ShiftSupervisor, WarehouseStaff, RegularHours, OvertimeHours, MonthlyLaborCost (regular $19/h, overtime $28.50/h, fully loaded), WarehouseRent, SafetyIncidents, PickingErrorRate, AvgDeliveryTimeDays (order to doorstep), RefundProcessingTimeHours, PickingErrors, ReshipmentCost.

## support_monthly.csv
Month, TicketsTotal, WISMO ("where is my order?"), WrongItem, ReturnsRefunds, Other, CostPerTicket, SupportCost.

## overflow_storage_rate_card.csv
StoreSafe Logistics monthly fee per unit by category and handling type (plus $1,400/month unit rent, not in the file).
