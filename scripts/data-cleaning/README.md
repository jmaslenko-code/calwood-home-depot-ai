# Scripts: Data Cleaning

Scripts for normalizing, deduplicating, and preparing raw data exports before analysis or reporting.

## What belongs here

- SKU and product data normalization scripts (standardizing units, descriptions, category codes)
- Order and shipment data deduplication scripts
- Freight invoice parsing and field extraction scripts
- Rithum / CommerceHub export cleaning scripts
- QuoteCenter export parsers and field mappers
- Dispute log import and enrichment scripts

## Guidelines

- Scripts should be idempotent — safe to run multiple times on the same input
- Include a brief header comment describing input format, output format, and any dependencies
- Store sample input files in a `samples/` subfolder where useful for testing
