# Weekly Competitor Watch Prompt

Copy and paste the prompt below into Claude every week (Monday or Tuesday recommended). Attach any screenshots, files, or data exports you have from the week. The prompt will run the standard weekly competitive scan and produce a prioritized action list.

Adjust the [FILL] fields before pasting.

---

## How to Use This Prompt

1. Open a new Claude session
2. Attach any of the following if you have them this week:
   - HomeDepot.com search screenshots for key categories
   - Competitor listing screenshots
   - Calwood listing screenshots
   - Rithum / CommerceHub sales data
   - Any new RTV or deduction notices
   - QuoteCenter activity
3. Copy the prompt below and paste it into Claude
4. Fill in the [FILL] fields
5. Send — Claude will run the scan and output the weekly report

The scan should take 20–30 minutes. If it takes longer, the scope has drifted. Stay focused on the top competitors and the highest-revenue Calwood categories.

---

## Weekly Prompt (Copy-Paste)

```
You are running Calwood Flooring Supply's weekly Home Depot competitive intelligence scan.

Today's date: [FILL — e.g., May 27, 2026]

Calwood's current monthly revenue baseline: [FILL — e.g., $28,000/month or "unknown"]

Calwood's revenue target: $300,000/month

---

ATTACHED DATA (if any):
[DESCRIBE WHAT YOU ATTACHED — e.g., "HomeDepot.com stair tread search screenshot from today", "Calwood May sales report from Rithum", "Stairtek listing screenshot" — or write "No attachments this week"]

---

Run the weekly competitive scan covering the following areas. Be direct and skeptical. Do not hype weak data. Label all data as Confirmed, Estimated, or Unknown.

---

SECTION 1: PRICE MONITORING

Check or estimate current pricing for Calwood's key competitors in the following categories:
- Stair treads (red oak, maple, white oak — unfinished and prefinished)
- Engineered hardwood flooring (white oak, red oak, maple — 5 in.+ width)
- Reducers and T-moldings
- Stair noses

For each category, answer:
1. What is the current competitor price range (lowest to highest)?
2. Where does Calwood's current price sit within that range?
3. Has any Tier 1 competitor changed price since last week? (Stairtek, Bruce, Malibu Wide Plank, Blue Ridge, Roppe, Lifeproof, Home Decorators Collection)
4. Is Calwood's price defensible given current competitor pricing and Calwood's review count?

Flag any category where Calwood is priced above a competitor with significantly more reviews and equivalent specs. That is a conversion problem — name it clearly.

---

SECTION 2: NEW LISTINGS MONITOR

Check or identify any new competitor listings in Calwood's core categories that were not present (or were significantly weaker) in prior scans.

For each new or changed listing found:
1. Brand and product name
2. Category
3. Price per unit or sq. ft.
4. Initial review count
5. Listing quality assessment (title, images, specs — quick pass/fail)
6. Is this a threat to a Calwood product? If so, which one?
7. Is this an opportunity (weak listing in a category where Calwood can compete)?

---

SECTION 3: WEAK COMPETITOR LISTINGS

Identify competitor listings in Calwood's categories that are ranking visibly but have weaknesses Calwood can exploit:
- Low review count (fewer than 25)
- Poor images (no lifestyle scene, no texture close-up)
- Incomplete specs
- Missing accessory / matching trim message
- Price that appears misaligned with specs or review count
- No sample listing linked

For each weak listing found:
1. Brand and product
2. What the weakness is
3. Whether Calwood has a current or potential listing that could capture this opportunity
4. Estimated monthly revenue Calwood could gain by executing well here

---

SECTION 4: SKU GAP CHECK

Identify any category or product type where multiple competitors have Home Depot listings but Calwood does not, or where Calwood's coverage is significantly weaker.

Priority gaps to check this week:
- White oak stair treads (any width / finish)
- White oak stair noses
- Matching wood floor vents / registers for Calwood flooring SKUs
- Any wide plank white oak flooring (7 in.+ width) Calwood is not covering
- Any stair riser listings competitors have that Calwood does not

For each gap confirmed:
1. How many competitors have listings in this gap?
2. What is the price range?
3. What is Calwood's capability to fill it?
4. Estimated monthly revenue if filled
5. Priority: Launch this quarter / Add to backlog / Monitor

---

SECTION 5: CALWOOD LISTING HEALTH CHECK

Review [FILL — list 1–3 specific Calwood SKUs to check this week, e.g., "Calwood red oak stair tread 48 in., Calwood white oak engineered hardwood 5 in., Calwood reducer"].

For each Calwood listing:
1. Is it ranking for its primary search term? (estimated)
2. Any change in review count or rating since last week?
3. Any competitor now outranking it?
4. Top 1–2 listing issues that may be hurting conversion

---

SECTION 6: QUOTECENTER AND SPECIAL ORDER SIGNAL CHECK

Answer the following based on any data available:
1. Any new stores requesting quotes or product information this week?
2. Any QuoteCenter bids submitted or won/lost?
3. Any Special Order activity worth noting?
4. Are there any stores where Pro Desk follow-up is overdue?

If no data is available, say so. Do not fabricate activity.

---

OUTPUT FORMAT

Produce the weekly report in this exact format:

## Calwood Weekly Competitive Intel — [DATE]

### Key Findings
(3–5 bullet points — most important things learned this week)

### Price Monitoring Summary
(Table: Category | Competitor Price Range | Calwood Price | Position | Flag?)

### New Listings Found
(Table or list — brand, product, price, threat/opportunity)

### Weak Competitor Listings
(List — brand, product, weakness, Calwood opportunity)

### SKU Gaps
(List — gap, competitor count, revenue estimate, priority)

### Calwood Listing Health
(List — SKU, status, top issue)

### QuoteCenter / Special Order Signal
(Summary — activity or "no data this week")

### Top 3 Actions This Week
(Numbered list — specific, actionable, include dollar impact estimate where possible)

1.
2.
3.

### What to Ignore This Week
(1–2 things that look interesting but are not worth acting on right now — and why)

### Confidence Summary
(Overall confidence in this week's findings: High / Medium / Low — and what data would improve it)

---

DATA INTEGRITY REMINDER

Label every data point in your output as:
- Confirmed = directly from a live source or attached file
- Estimated = calculated or inferred from partial data
- Unknown = cannot determine from available information

Do not present estimated competitor pricing as confirmed. Do not invent review counts or rankings.

If a section cannot be completed due to missing data, say: "Insufficient data this week — [what would be needed]."
```

---

## What to Do With the Output

After Claude produces the weekly report:

1. **Save the report** to `docs/weekly-review/YYYY-MM-DD-competitor-watch.md`
2. **Take the top action immediately** — do not defer all three
3. **Add any new SKU gaps** to the gap tracking backlog in `templates/competitive-intel/sku-gap-analysis-template.md`
4. **Flag any listing problems** for the IDM / listing update queue
5. **Note any price changes** in the pricing benchmark for the relevant category

If the weekly scan consistently produces nothing actionable, either the competitive landscape is stable (good) or the scan is not going deep enough (investigate).

---

## Attachments That Improve the Scan

The more you attach, the better the output. Priority attachments:

| Attachment | Why it helps |
|---|---|
| HomeDepot.com search screenshots | Confirms current rankings and competitor presence |
| Competitor listing screenshots (full page) | Confirms current price, review count, and listing quality |
| Calwood listing screenshots | Confirms Calwood's current state |
| Rithum / CommerceHub weekly sales report | Confirms what's selling and what's not |
| QuoteCenter activity summary | Shows pipeline health |
| Any new RTV or deduction notice | Triggers dispute workflow in addition to competitive scan |

Without attachments, Claude will work from prior knowledge and estimations. Label that output accordingly — it is a starting point, not a confirmed report.

---

## Cadence Reminder

| Frequency | Task |
|---|---|
| Weekly | Run this prompt — focus on Tier 1 competitors and top 5 Calwood SKUs |
| Monthly | Full pricing benchmark per category (`pricing-benchmark-template.md`) |
| Monthly | Full listing quality audit on top 10 Calwood SKUs (`listing-quality-scorecard.md`) |
| Quarterly | Full competitor comparison per Tier 1 brand (`competitor-comparison-template.md`) |
| As needed | SKU gap analysis when a new gap is identified (`sku-gap-analysis-template.md`) |
