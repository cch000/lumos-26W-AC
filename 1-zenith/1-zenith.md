# Zenith Active Solutions: Turnaround Audit
Candidate briefing & task directives

## Executive Summary & Context
Welcome. Your consulting team has been engaged by the board of **Zenith Active Solutions**, a US direct-to-consumer (D2C) fitness brand: apparel, equipment, supplements and accessories, about 200 products, one warehouse in Edison, New Jersey.

On paper, 2023 was a rocket year. **Orders tripled (12,600 → 37,900) and net revenue more than doubled ($1.7M → $3.7M).** But the preliminary FY2023 numbers just landed: **EBITDA margin fell from 12% to under 2%.** The lead investor, Northgate Ventures, wants **7% within two quarters**, or the next funding tranche is frozen.

Everyone has an explanation. Marketing says growth costs money. The warehouse says it's understaffed. IT says it's busy migrating to Teams. Finance can see *that* the profit disappears, but not *where* or *why*. The CFO has asked the board to approve **one turnaround plan, with up to $250,000 and two contract engineers for one quarter**. The board meets this afternoon, and you present to it.

**Your mission:** find the structural leaks that are destroying Zenith's margin, and present a turnaround plan that is backed by evidence and fits that budget.

## How You Should Work
**Your team picks 2 of the 5 tracks** and goes deep on them. Pick based on your team's strengths. Every track has its own starting numbers and documents, so neither track has to wait for the other. But your two tracks should end up telling **one connected story** to the board, not two separate presentations.

- 🟢 **Track A:** Data & Analytics
- 🔵 **Track B:** Business & Strategy
- 🟠 **Track C:** Marketing & Brand
- 🔴 **Track D:** UX/UI & Design
- 🟣 **Track E:** Software & Infrastructure *(new)*

**Pairs that work well** (any pair is fine; these are just examples):

| Pair | The story it can tell |
|---|---|
| A + B | Follow the money: where every dollar goes between revenue and EBITDA, and which leaks to fix first |
| B + C | Growth that pays: which customers and channels make money, and what happens to the creator contract |
| C + D | Fix the customer journey: what Zenith promises, what customers experience, and the redesign |
| B + E | Maybe it's the systems, not the strategy: which "business problems" are actually broken software, and what two engineers fix first |
| A + E | Prove it in the data: the bugs, the date they started, and what they cost |
| D + E | The cart and the after-order experience: design the fix and build it |

⚠️ A shallow attempt at more tracks is worse than a deep, connected solution across two.

---

## 🟢 Track A: Data & Analytics
> "Check the numbers everyone quotes, and find where the money really goes."

Zenith's leadership quotes KPIs that nobody has checked. The data exists in clean tables (`analysis_ready/`) and in the original messy exports (`raw_systems/`). Your job is to turn it into evidence the board can trust.

**Start with:** `factsheets/data_analytics_factsheet.md`, `analysis_ready/` and its README, then `docs/CFO_Memo_FY2023_Preliminary.md` and `docs/Q3_Marketing_Readout.md`.

>We suggest using: Python (pandas), SQL, R or Excel, plus a charting tool.

**What you should produce:**
1. **A leak table:** at least 3 places where Zenith loses money, each sized in **$ per year**, with the evidence and how sure you are.
2. **3–4 charts** a board member understands in 10 seconds: an anomaly, a cost driver, a customer-behavior issue.
3. **Two KPI checks:** take two "official" KPIs from your factsheet and confirm or debunk them. Watch out: some patterns change when you look *within* groups or at *when* something started.
4. **Key differentiator (pick one):**
   - a reproducible pipeline that rebuilds the clean tables from `raw_systems/` (raw → cleaned → final); or
   - a cohort view: what a customer from each channel is worth after 6–12 months.

## 🔵 Track B: Business & Strategy
> "Explain where the money goes, and what the board should do about it."

The board knows the margin collapsed but not which decisions caused it. Costs are rising faster than revenue. Your job is to follow every dollar from revenue to EBITDA, find the decisions and contracts behind the leaks, and give the board clear levers, backed by numbers rather than opinions.

**Start with:** `factsheets/business_operations_factsheet.md`, then `docs/CFO_Memo_FY2023_Preliminary.md`, `docs/Board_Minutes_2023-10-12.md`, `docs/Pulse_Creator_Agency_Agreement.md`, `docs/West_Coast_Fulfillment_Proposals.md` and `docs/Warehouse_Floor_Interviews.md`.

>We suggest using: Excel or Google Sheets, flowcharts, value-driver trees, unit economics.

**Expected deliverables:**
1. **Cost waterfall, 2022 vs 2023:** where each dollar of revenue goes before it reaches EBITDA. Name the **top 3 cost lines** that grew, size each one, and say which are structural and which you can fix.
2. **A small financial model** with at least one assumption you can change (e.g. discount rate, overtime hours or shipping mix) that updates the result.
3. **One process, current vs future:** for example warehouse picking, West Coast shipping or returns. Show at least 2 concrete inefficiencies and the improved process.
4. **The plan:** 2–3 moves that fit **$250K and two engineers for one quarter**, each with its expected 12-month impact, its cost and your assumptions. Say what you would *not* fund, and why.

## 🟠 Track C: Marketing & Brand
> "Fix growth so it actually creates value."

In 2023 marketing spend more than doubled and orders tripled, but profit fell. The biggest share of new customers came through creators, pushed by discount codes and flash sales. The creator agency (Pulse, about $400K a year) wants to renew, and **the notice deadline is 17 January**. Your job is to find which channels create value and which destroy it, and to show how Zenith grows without buying every order with a discount.

**Start with:** `factsheets/growth_marketing_factsheet.md` (no coding needed), then `docs/Q3_Marketing_Readout.md`, `docs/Pulse_Q4_Business_Review_Email.md`, `docs/Brand_Guidelines_and_Voice.md`, `docs/Customer_Reviews_Compilation.md` and `design/`.

>We suggest using: Google Docs or Notion, PowerPoint, Canva, Figma, your phone, whatever you'd use to build a real campaign.

**Expected deliverables:**
1. **Channel audit & pivot:** which channels make money *after* discounts and returns, and which lose it? Question the dashboard's headline numbers. Propose a **2024 channel mix** with the reasoning.
2. **The creator decision:** renew, renegotiate or exit Pulse? If you renegotiate, say on what terms. The contract is in `docs/`.
3. **A campaign with 2–3 real mockups** (posts, stories, an e-mail, an ad) for one of these:
   - a "Bundle & Save" launch that moves slow inventory without killing margin;
   - a retention or win-back campaign for the customers who actually come back;
   - a repositioning away from discount-first messaging.
4. **A 2-week content calendar** that supports the campaign: what gets posted where, and why it is different from what Zenith does now.

## 🔴 Track D: UX/UI & Design
> "Make the solution tangible: fix the touchpoints that quietly cost money."

Zenith's customer experience is suppressing revenue and creating work elsewhere. Since the November 2022 website relaunch, customers buy fewer items per order. Support is buried in "where is my order?" questions, and the packing process slows the warehouse. Your job is to redesign the customer touchpoints that bleed money, and to show how a design change turns into margin.

**Start with:** `factsheets/design_cx_factsheet.md`, `design/WebsiteLanding.png` and `design/WebsiteCart.png`, then `docs/Website_UX_Audit_Notes.md`, `docs/User_Test_Transcript_Cart.md`, `docs/Support_Ticket_Categorization_Report.md` and `docs/Packaging_Vendor_Specs.md`.

You are not designing from scratch: you are evolving an existing brand (see `docs/Brand_Guidelines_and_Voice.md`).

>We suggest using: Figma, Adobe CC, sketches.

**Expected deliverables:**
1. **Cart & bundle flow:** a before → after wireframe (low or high fidelity) that encourages multi-item orders. Base it on what real users did and said.
2. **One more touchpoint (pick one):**
   - the after-order experience (confirmation, tracking, "where is my order?"); or
   - a packaging concept that is simpler, consistent and faster to pack.
3. **The number:** for each design, what it changes (bigger baskets, fewer tickets, minutes saved per order), using your factsheet.
4. *Optional bonus:* 1–2 campaign visuals that match Track C, if your team has it.

## 🟣 Track E: Software & Infrastructure (new)
> "Some of Zenith's business problems might be broken software."

Zenith's in-house shop services (pricing, shipping rates, returns, order e-mails, the cart script) were written by a freelancer for the November 2022 relaunch. He left in February 2023, the server was moved, and nobody owns the code. Since then, odd things show up in the business: strange discounts, expensive shipping, angry customers. The board is getting two contract engineers for one quarter. Your job is to find what's broken, connect it to what it costs the business, and decide what those engineers fix first.

**Start with:** `factsheets/build_factsheet.md` (the system inventory and the symptoms the business reported), `shop-services/` and its README, and `docs/IT_Incident_Log_and_Helpdesk_Export.md`.

**Running it:** `cd shop-services && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload`. It probably won't start on the first try; that's part of the job. Docker is optional. If you can't run it at all, reading the code and configs still counts.

>We suggest using: Python, any editor, git, AI coding tools (but check what they tell you).

**Expected deliverables:**
1. **Get it running:** what stopped the service from starting, and what you changed.
2. **A defect register** with at least 3 defects: what is wrong, where (file:line), the evidence, **which business symptom it explains**, a rough $ impact (your own estimate is fine if you label it) and the fix effort (S/M/L).
3. **One fix with proof:** a test that fails before and passes after, or a clear before/after demo.
4. **The engineers' quarter:** what the two contract engineers should do first, second and third, and what you would leave alone. Include anything in the server setup or configuration that worries you.

---

## 🖼️ Final Presentation (10–12 slides)
At the end, your team presents **one** pitch to the Zenith board (your assessors). **Every team member presents a part.**

Your presentation must include:
- **The problem (1–2 slides):** what is broken at Zenith. Root causes, not symptoms.
- **Your evidence (2–3 slides):** data, documents, code, user research. Whatever your two tracks produced.
- **Your solution (3–4 slides):** concrete changes, not ideas: re-engineered processes, fixed systems, redesigned flows, a new channel plan.
- **Expected impact (1–2 slides):** a rough $ estimate and what it costs, against the $250K / two-engineer budget. State your assumptions.
- **Next steps (1 slide):** what happens in the first 30 / 60 / 90 days.

Optional but encouraged: a value-driver tree from operations to EBITDA, current vs future process maps, a live demo.

## 📁 The Data Room
Everything is in `data_room/`. Start with `00_INDEX.md`, which describes every file in one line.

- `factsheets/`: one page per track with ready-to-use numbers. They are the company's *official* numbers, so treat them like any internal report.
- `docs/`: 27 internal documents (e-mails, contracts, minutes, reports, chat logs, interviews). Some contain vital clues; others are corporate noise. **You don't have to read them all.** Your track's "start with" list is enough to begin.
- `analysis_ready/`: clean data (orders, customers, products, monthly P&L, operations, support, marketing). Excel is enough.
- `raw_systems/`: the original messy exports (SQLite, JSON, a log file, a spreadsheet). Optional.
- `shop-services/`: code and server configuration of Zenith's in-house services (Track E).
- `design/`: website screenshots and logo.

## Ground Rules
- Put a number on things where you can, and say how sure you are. Rough and honest beats precise and invented.
- AI tools are allowed. You are responsible for every number and claim, and we may ask how you checked it.

## What We're Looking For
Strong teams:
- focus on the problems with the biggest impact;
- connect their two tracks into one story;
- build practical, implementable solutions;
- use data as evidence, not decoration.

Weak teams:
- work in silos and merge slides at the end;
- over-focus on low-impact details;
- give vague recommendations;
- fail to connect operations to profit.

---

Good luck 😊
