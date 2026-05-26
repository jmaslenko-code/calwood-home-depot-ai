# Operating Playbook: Competitive Intelligence Agent

## Purpose

This playbook defines how Calwood runs its Home Depot competitive intelligence system — what to track, how often, which templates to use, and how to turn intelligence into revenue actions.

Competitive intelligence is not research for its own sake. Every session should end with one of three outputs:

1. A listing change to make
2. A SKU to add or price to adjust
3. A store or QuoteCenter action to take

If a session produces none of those, the scope was too broad or the data was too thin.

---

## What This System Covers

| Area | What We Track |
|---|---|
| Competitor pricing | Price per sq. ft., price per unit, case price, price trends |
| Competitor listings | Title, images, specs, reviews, variation setup, accessory messaging |
| SKU gaps | Categories where competitors have listings and Calwood does not |
| Listing quality | How Calwood's listings compare to competitors across 20+ dimensions |
| New competitor activity | New listings, price drops, new SKUs, new review velocity |
| Calwood opportunity | Where Calwood can win on price, quality, matching accessories, or Pro Desk support |

---

## Competitors to Track

### Tier 1 — Track weekly

These brands directly compete with Calwood's core products on Home Depot and have enough presence to move the category.

| Brand | Primary categories | Why tier 1 |
|---|---|---|
| Stairtek | Stair treads, risers, stair noses | Dominant in the stair category; the benchmark Calwood is measured against |
| Bruce | Solid/engineered hardwood, strip flooring | Major HD brand with high review counts; sets pricing expectations |
| Malibu Wide Plank | Wide plank engineered hardwood, white oak | Premium white oak competitor; prices high but converts well |
| Blue Ridge | Engineered hardwood | Mid-market; frequently in the same search results as Calwood |
| Roppe | Reducers, T-moldings, transitions, base | Dominant in molding/accessory category |
| Lifeproof | Flooring, LVP | Strong HD brand trust; may divert flooring budget from hardwood |
| Home Decorators Collection | HD private label flooring and accessories | HD-favored placement; aggressively priced |

### Tier 2 — Track monthly or when a gap is identified

| Brand | Watch for |
|---|---|
| Shaw | Any new white oak or wide plank SKUs on HD |
| Pergo | Pricing and spec changes in engineered hardwood |
| Armstrong | Stair nose and transition product coverage |
| TrafficMaster | Budget flooring and molding — sets the price floor |
| MSI | Hard surface flooring and tile; monitors any hardwood expansion |
| Unbranded / white-label | Stair tread and molding listings with no clear brand — often rank well on price |

### Search terms to monitor

Track these search terms on HomeDepot.com regularly. What ranks here is what customers see instead of — or before — Calwood.

**Stair category:**
- unfinished red oak stair tread
- unfinished maple stair tread
- unfinished white oak stair tread
- prefinished stair tread
- stair nose hardwood
- stair riser 48 in.
- landing tread hardwood

**Flooring:**
- white oak engineered hardwood
- engineered hardwood flooring white oak
- wide plank white oak flooring
- red oak engineered hardwood
- maple engineered hardwood
- rustic white oak hardwood

**Accessories/moldings:**
- hardwood reducer
- hardwood T-molding
- hardwood stair nose
- wood floor vent register
- hardwood floor transition
- baby threshold hardwood

---

## Product Categories to Track

| Category | Key metrics to compare |
|---|---|
| Engineered hardwood | Price/sq. ft., species, width, veneer thickness, finish, warranty |
| Stair treads | Price/unit, species, dimensions, finish, review count |
| Stair noses | Price/unit, species, profile dimensions, finish compatibility |
| Risers | Price/unit, species, dimensions, finish |
| Reducers | Price/unit, profile, species, finish, compatibility messaging |
| T-moldings | Price/unit, species, width, finish |
| End caps | Price/unit, species, finish |
| Baby thresholds | Price/unit, species, finish |
| Wood vents/registers | Price/unit, size options, species, finish compatibility |
| Flooring samples | Whether offered, price, shipping, link to parent SKU |
| Custom molding listings | Whether competitors have Special Order or custom-size pages |

---

## Templates and When to Use Each

### 1. Weekly Competitor Watch Prompt
**File:** `templates/competitive-intel/weekly-competitor-watch-prompt.md`
**When:** Every week — run on Monday or Tuesday
**Time investment:** 20–30 minutes with attachments; 10–15 minutes without
**Output:** Top 3 actions for the week, price changes, new listings, SKU gaps

### 2. Competitor Comparison Template
**File:** `templates/competitive-intel/competitor-comparison-template.md`
**When:** Quarterly per Tier 1 brand, or any time a competitor launches something new or changes pricing significantly
**Time investment:** 45–60 minutes per competitor
**Output:** Full head-to-head comparison — pricing, specs, listing quality, weaknesses, Calwood opportunity

### 3. SKU Gap Analysis Template
**File:** `templates/competitive-intel/sku-gap-analysis-template.md`
**When:** Any time a gap is identified in the weekly scan, or when evaluating what to launch next
**Time investment:** 30–45 minutes per gap
**Output:** Go/no-go recommendation with revenue estimate, confidence level, and launch requirements

### 4. Pricing Benchmark Template
**File:** `templates/competitive-intel/pricing-benchmark-template.md`
**When:** Monthly, or any time Calwood is considering a price change
**Time investment:** 30–45 minutes per category
**Output:** Full category price map — where Calwood sits, whether current pricing is defensible

### 5. Listing Quality Scorecard
**File:** `templates/competitive-intel/listing-quality-scorecard.md`
**When:** Monthly for top Calwood SKUs; any time a listing is underperforming; when launching a new SKU
**Time investment:** 15–20 minutes per listing
**Output:** Pass/fail score across 20+ dimensions, ranked fix list, competitor comparison

---

## How to Run the Weekly Scan

### Step 1 — Gather data before scanning (5 minutes)

Pull any of the following before opening Claude:
- Rithum / CommerceHub sales export for the week
- Any new RTV or deduction notices
- HomeDepot.com screenshots of key search terms (stair treads, white oak flooring, reducers)
- Screenshots of any competitor listings that look different from last week
- QuoteCenter activity summary if available

### Step 2 — Run the weekly prompt

Open a new Claude session. Paste the weekly prompt from `templates/competitive-intel/weekly-competitor-watch-prompt.md`. Attach your data files and screenshots. Fill in the date and baseline revenue fields.

### Step 3 — Evaluate the output

Read the report critically. Ask:
- Is the data confirmed or estimated? If mostly estimated, note that and plan to get better data next week.
- Are the top 3 actions actually executable this week?
- Is there anything in the "weak competitor listings" section Calwood should move on immediately?

### Step 4 — Act on at least one action immediately

Do not defer all three actions. Take the top one the same day. If it requires a listing change, queue it. If it requires a pricing decision, flag it for a decision this week.

### Step 5 — Archive the report

Save the output to: `docs/weekly-review/YYYY-MM-DD-competitor-watch.md`

---

## How to Evaluate Competitive Data Quality

Not all competitive data is equal. Use these labels throughout every template:

| Label | Meaning |
|---|---|
| **Confirmed** | Directly from a live source — HomeDepot.com screenshot, attached file, live search result |
| **Estimated** | Calculated or inferred from partial data — price trend, review velocity estimate |
| **Unknown** | Cannot determine from available data — internal competitor costs, conversion rates, wholesale pricing |

### Common data quality traps to avoid

- Do not treat a Claude estimate of competitor pricing as a confirmed current price. Prices change. Confirm from HomeDepot.com before making a pricing decision.
- Do not assume a competitor's high review count means they are winning the category. Check whether their reviews are recent or stale.
- Do not assume a weak listing means low sales. Some weak listings still rank well due to early review count or HD placement deals. Verify ranking before calling it a displacement opportunity.

---

## Competitive Advantage Framework

Calwood can win against competitors through four channels. Know which channel applies before deciding how to respond to a competitive threat.

### 1. Price advantage
Win when Calwood can match or undercut a competitor while maintaining acceptable margin.
Use when: Competitor is weak on reviews, Calwood is launching a new SKU, or a category is purely price-driven.

### 2. Quality advantage
Win when Calwood's product spec is genuinely superior — thicker veneer, better species, superior finish — and the listing communicates that clearly.
Use when: Calwood's product is demonstrably better but the listing isn't showing it.

### 3. Custom matching accessories advantage
Win when Calwood can offer matching stair treads, stair noses, reducers, T-moldings, end caps, vents, and custom moldings that competitors cannot match.
This is Calwood's strongest differentiator and most competitors cannot replicate it on short notice.
Use when: A flooring or stair tread sale is in play and the customer needs a complete package.

### 4. Pro Desk / QuoteCenter support advantage
Win when Calwood can respond faster, provide better project pricing, and support larger orders through QuoteCenter and Special Order channels that competitors handle poorly or not at all.
Use when: A store or contractor needs more than what HomeDepot.com online sales can provide.

---

## Metrics to Track Over Time

Build a simple tracker (spreadsheet or note file) with these metrics. Update monthly.

| Metric | What to track |
|---|---|
| Calwood price vs. category benchmark | Are we positioned where we intend to be? |
| Review count — top 5 Calwood SKUs | Growing, flat, or declining? |
| Review count — top Stairtek stair tread | Calwood's gap vs. the category leader |
| Competitor new SKU count | How fast is the competitive landscape expanding? |
| SKU gap count | How many confirmed gaps remain unfilled? |
| Listing quality score — average top 5 Calwood SKUs | Trending up or down? |
| Weekly scan action completion rate | Are we actually executing on findings? |

---

## What Not to Track

Focus protects the business. Do not spend time tracking:

- Competitors outside Home Depot (Lowe's, Amazon, Floor & Decor) unless a specific cross-channel signal warrants it
- LVP / luxury vinyl plank competitors unless Calwood is adding LVP SKUs
- Budget flooring below $2.50/sq. ft. — Calwood does not compete there
- Competitor social media, advertising, or brand activity — not actionable at this stage
- Individual customer reviews on competitor products unless investigating a specific listing weakness

---

## Escalation Triggers

Act immediately — do not wait for the weekly scan — when:

- A Tier 1 competitor drops price by more than 15% on a category where Calwood competes directly
- A new listing appears in a Calwood core category with 100+ reviews (suggests a brand pivot or aggressive launch)
- A Calwood listing drops significantly in search ranking (visible by checking manually on HomeDepot.com)
- A QuoteCenter opportunity above $20K is identified that involves a product a competitor also offers
- A store Pro Desk contact reports a competitor is offering something Calwood cannot currently match

---

## File Structure

All competitive intelligence files live here:

```
templates/competitive-intel/
  weekly-competitor-watch-prompt.md     ← Weekly scan prompt
  competitor-comparison-template.md     ← Head-to-head brand comparison
  sku-gap-analysis-template.md          ← Individual gap analysis
  pricing-benchmark-template.md         ← Category price map
  listing-quality-scorecard.md          ← Listing audit scorecard

docs/operating-playbooks/
  competitive-intelligence-agent.md    ← This file

docs/weekly-review/
  YYYY-MM-DD-competitor-watch.md        ← Weekly scan archives
```
