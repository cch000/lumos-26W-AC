**From:** Brendan Ohs, IT Manager
**To:** Priya Raman
**Date:** Wednesday, 3 January 2024
**Subject:** IT helpdesk export 2023 + Teams migration status (for board pack)

Priya, as requested: the 2023 helpdesk export from the IT Notion board. I left out about 200 routine tickets (password resets, toner, "Wi-Fi slow") apart from a few examples. Teams status at the bottom.

---

## Helpdesk export (Notion database "IT Requests", 1 Jan – 31 Dec 2023, filtered)

**#4392 · 17 Jan · Megan Thompson (Marketing) · Closed 3 Feb**
*Add 12 Pulse creator codes, retire MAXLIFTS20 / YOGAWITHJESS20 / COACHDRE20*
All new codes 30%. Alex made the change in promos.yaml (3 Feb), I restarted the app.

**#4404 · 6 Feb · Brendan Ohs · Closed 14 Feb**
*Move shop services off Alex's VPS before his contract ends*
Alex's box is on his personal hosting account. Plan: Docker on a new Zenith VPS, nginx in front.

**#4409 · 14 Feb · Brendan Ohs · Closed 14 Feb**
*Notifier alert e-mails flooding inbox during migration*
Once I stopped the services on the old box, the monitoring check for the shipping-notification job sent a failure e-mail every 30 min. Muted the alert rule for the migration window. Re-enable after cutover.

**#4410 · 14 Feb · Brendan Ohs · Done**
*Server move: shop services → new VPS*
Cutover 11:30–11:40, containers up 11:37, DNS switched. Order mail now goes through Microsoft 365 (orders@ mailbox); tidied the job file names. Smoke test: /cart/quote, /returns/eligibility, product list, checkout test order all OK. Old VPS shut down 21 Feb.

**#4411 · 20 Feb · Jordan Blake (CX) · Owner: — · OPEN**
*promo stacking?*
20 Feb JB: Customer used FITFAM30 + LOYAL15 and got 45% off. Is that right? Contract says one discount?
22 Feb BO: Asked Alex. Reply: "works as specced for BF22, check with marketing."
24 Feb MT: Intended. The cart banner literally says stack it. Please don't change.
6 Mar JB: Flash weekend: ZENITH30 + creator code = 60%. Agents getting questions all weekend. Still intended??
13 Nov BO: Vivienne asked about this again (something in Schedule B of the Pulse agreement). This is a business decision, not an IT one. Need marketing + legal to agree first.

**#4413 · 27 Feb · Brendan Ohs · Closed 28 Feb**
*Offboard Alex Thompson*
Removed Shopify account, server keys, drive access. Code repository transferred to Zenith. His README has a "roadmap" (Postgres, Kubernetes). Parked.

**#4421 · 6 Mar · Harold H. Montgomery · Closed 9 Mar**
*Time clock + badge access for 4 new warehouse staff*
Done.

**#4479 · 19 Jun · Brendan Ohs · Closed 19 Jun**
*Odd errors in shop service log Sunday night (500s on /orders/…)*
Looks like an internet scanner trying random URLs. Nothing to do.

**#4484 · 26 Jun · Priya Raman · Closed 28 Jun**
*Onboarding: CFO laptop, Shopify reports, finance shared drive*
Done.

**#4506 · 22 Aug · R. Gupta (Warehouse) · Closed 23 Aug**
*Green Station label printer keeps dropping off Wi-Fi*
Moved the access point. Station lighting is out (Facilities ticket); they're working by headlamp.

**#4521 · 12 Sep · R. Gupta (Warehouse) · Closed 15 Sep: works as designed**
*Slack pick-rate bot never posts anything?*
RG: Harold says a bot warns #warehouse-ops when picking errors go up. Nobody has ever seen a message, and errors feel way up this summer.
BO: Checked. Bot runs on the 1st of each month at 07:00 and is running fine. Last run: `2023-09-01 07:00:04,406 INFO 2023-08 error_rate=0.043 threshold=5 -> OK`. No alert because it's under the threshold. Works as designed.

**#4549 · 9 Oct · Jordan Blake (CX) · MONITORING**
*Customers seeing "502 Bad Gateway" when the cart updates*
Started after the promo deploy for the 6–8 Oct flash weekend. nginx error log: `connect() failed (111: Connection refused) while connecting to upstream … upstream: "http://172.18.0.2:5000/cart/quote"`. Restarted containers; cleared. Grepped the log: the same error shows up a few times a month since the February move, always clears on its own. Monitoring.

**#4570 · 1 Nov · Brendan Ohs · IN PROGRESS**
*Slack → Microsoft Teams migration*
Cutover target 2 Jan 2024. See status note.

**#4574 · 6 Nov · Brendan Ohs · OPEN (after cutover)**
*Inventory Slack integrations before cutover*
1. Shopify order notifications → #orders: replace with Shopify's Teams connector.
2. Pick-rate alert bot → #warehouse-ops: custom Slack webhook in Alex's code. Needs rewriting for a Teams incoming webhook. Nobody here knows that code well.
3. StoreSafe weekly inventory e-mail → #logistics forward: switch to a Teams channel e-mail address.

**#4588 · 27 Nov · Megan Thompson · Closed 4 Dec**
*Turn on ZENITH30 for 1–3 Dec flash weekend*
promos.yaml `active: true`, deployed 30 Nov 18:00. Set back to false Mon 4 Dec.

**#4601 · 4 Dec · Warehouse office · Closed**
*Pick-list printer jams on every third sheet*
Replaced pickup roller, ordered spares. They print a lot of pick lists.

**#4607 · 11 Dec · Jordan Blake (CX) · OPEN**
*Can we add a "track my order" page to the website?*
Needs Shopify theme work and someone who knows the order service. After Teams.

**#4612 · 18 Dec · Brendan Ohs · Done**
*Teams licences and accounts for all staff*

**#4619 · 28 Dec · various · Closed**
*Password resets after Teams single sign-on rollout (×6)*

---

## Teams migration: status 3 Jan 2024

- **Cutover done 2 Jan.** All staff on Teams. Slack is read-only until 31 Jan, then the workspace closes.
- Shop-services VPS rebooted 2 Jan 06:15 for a kernel patch. Containers came back on their own.
- **Open:** integrations in #4574. Shopify notifications already moved. The pick-rate alert bot is not migrated: it still posts to a Slack webhook that will stop working when Slack closes. Rewriting it needs a developer.

Honest note: I'm one person, and since February nobody has looked after the shop services except me when something breaks. Several tickets above are parked for that reason.

Brendan
