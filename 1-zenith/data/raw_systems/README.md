# raw_systems/: original system exports (optional)

These are the raw exports `analysis_ready/` was built from. **You don't need them**: everything is already clean in `analysis_ready/`. They're here for anyone who wants to rebuild the pipeline (a Data or Build stretch goal), check how a number was derived, or enjoy a messy file.

| File | System | Notes |
|---|---|---|
| `zenith_core_db.sqlite` | Order database | Tables `transactions_master` (one row per order) and `order_items`. Payment method, promo code, creator code, discount, ZIP3 and status are packed into one text field `Transaction_Log`, e.g. `METHOD:Klarna (BNPL)\|\|PROMO:ZENITH30\|\|CREATOR:FITFAM30\|\|DISC:0.6\|\|ZIP3:941\|\|STATUS:REFUNDED`. Net revenue and profit are not stored. |
| `customer_profiles_v2.json` | CRM | Nested JSON per customer. The channel is at `acquisition_telemetry.source.utm_medium`. `projected_ltv_at_signup_usd` comes from a model last updated in June 2022. |
| `sys_ops_log_archive.sys` | Warehouse system | `~`-delimited, no header. Columns: Month, ShiftSupervisor, MonthlyLaborCost, WarehouseRent, OvertimeHours, SafetyIncidents, PickingErrorRate, AvgDeliveryTimeDays, RefundProcessingTimeHours. |
| `marketing_spend_history.xlsx` | Marketing | Spend by month (rows) and channel (columns) |
