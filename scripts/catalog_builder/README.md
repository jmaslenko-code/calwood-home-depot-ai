# Catalog Builder Scripts

Scripts for generating and validating the Calwood Flooring Supply catalog data files.

---

## Scripts

### `generate_catalog_data.py`

Generates `catalog/data/products.json` and `catalog/data/categories.json` from Python dictionaries embedded in the script. Use this to rebuild both data files from scratch, or to add new products by editing the Python source and re-running.

**When to use:**
- Initial setup of the catalog data files
- After adding new products or categories to the Python dictionaries
- After making bulk edits to product specs across a collection

**Usage:**

```bash
# Run from repo root
python3 scripts/catalog_builder/generate_catalog_data.py

# Preview output without writing files
python3 scripts/catalog_builder/generate_catalog_data.py --dry-run

# Write to a custom output directory
python3 scripts/catalog_builder/generate_catalog_data.py --output-dir /path/to/dir
```

---

### `validate_catalog_data.py`

Loads `catalog/data/products.json` and validates required fields for all flooring products. Prints a `✓` for each valid product and `WARN` for any product missing a required field. Exits with code `1` if any required field is missing.

**Required fields checked (flooring):**
- `product_name`, `category`, `species`, `thickness`, `width`
- `vendor_sku`, `omsid`, `home_depot_url`, `image`
- `matching_accessories`, `quote_available`

**When to use:**
- After editing `products.json` manually
- After running `generate_catalog_data.py`
- Before deploying an updated catalog to GitHub Pages
- As part of a CI/CD pipeline check

**Usage:**

```bash
# Run from repo root
python3 scripts/catalog_builder/validate_catalog_data.py

# Disable color output (for CI logs)
python3 scripts/catalog_builder/validate_catalog_data.py --no-color

# Strict mode: exit 1 on any warning, not just missing-field errors
python3 scripts/catalog_builder/validate_catalog_data.py --strict

# Validate a different products.json file
python3 scripts/catalog_builder/validate_catalog_data.py --file path/to/products.json
```

---

## Typical Workflow

1. Edit the product dictionaries in `generate_catalog_data.py`
2. Run `python3 scripts/catalog_builder/generate_catalog_data.py`
3. Run `python3 scripts/catalog_builder/validate_catalog_data.py`
4. Open `catalog/index.html` locally to verify the catalog renders correctly
5. Commit and push to GitHub Pages

---

## Notes

- Do **not** include internal cost, margin, DP pricing, or supplier pricing in any data file.
- Use `"data_source": "TBD — not yet listed on HomeDepot.com"` for placeholder products.
- Use `"omsid": "OMSID TBD"` — do not invent fake OMSIDs.
- Product images should be saved to `catalog/assets/images/` using the filename in the `image` field.
