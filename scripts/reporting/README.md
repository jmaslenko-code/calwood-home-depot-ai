# Scripts: Reporting

Scripts for generating channel performance reports and summaries from cleaned data.

## What belongs here

- Sales velocity and trend reports (by SKU, category, store, or time period)
- Dispute and chargeback summary reports (open balance, recovery rate, aging)
- Freight billing reconciliation reports
- Rithum fill rate and order exception reports
- QuoteCenter win/loss rate reports
- Pro Desk outreach activity summaries

## Guidelines

- Scripts should read from cleaned data outputs (see `scripts/data-cleaning/`)
- Output formats should be consistent: CSV for data consumers, Markdown or HTML for human review
- Parameterize date ranges and filters at the top of each script for easy reuse
