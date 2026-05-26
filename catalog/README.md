# Calwood Flooring Supply — Online Catalog

A premium product catalog for Calwood Flooring Supply, a Home Depot vendor. Used during store visits and shared via QR code — a Home Depot associate or customer scans the code and sees the full Calwood product line.

**Audience:** Home Depot flooring associates, Pro Desk teams, contractors, and end customers.

---

## What This Catalog Contains

- **Flooring Collections** — Supreme, Woodline, and Icon collections with European White Oak engineered hardwood
- **Stair Treads & Risers** — Unfinished European White Oak in multiple lengths
- **Custom Matching Accessories** — Stair nose, reducers, T-moldings, end caps, baby thresholds, wood vents, custom profiles
- **Project Packages** — Flooring Only, Flooring + Trims, Full Project
- **Quote Request Form** — Front-end form for capturing project details
- **How to Order** — Step-by-step ordering process through Home Depot

---

## How to Preview Locally

Run a local HTTP server from the `catalog/` directory:

```bash
cd catalog
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

**Note:** The catalog must be served over HTTP (not opened as a `file://` URL) because it loads `data/products.json` and `data/categories.json` via `fetch()`.

---

## How to Edit Products

Edit `catalog/data/products.json` directly.

### Adding a confirmed product

1. Open `catalog/data/products.json`
2. Find the correct array (`flooring`, `stair_treads`, `risers`, or `trim_accessories`)
3. Add a new object following the same structure as existing entries
4. Set `"data_source": "Confirmed — HomeDepot.com listing"` for live HD products
5. Set `"home_depot_url"` to the actual product URL from HomeDepot.com
6. Run `python3 scripts/catalog_builder/validate_catalog_data.py` to check for missing fields

### Updating a placeholder

Find the product by `id` (e.g., `"tbd-natural-white-oak"`) and fill in the real values for `vendor_sku`, `price_per_sqft`, `thickness`, `width`, `home_depot_url`, and `data_source`.

---

## How to Replace Placeholder Images

Product images are referenced in `products.json` using the `image` field (e.g., `"assets/images/supreme-cotton.jpg"`).

To add a real product image:

1. Save the image to `catalog/assets/images/` using the exact filename from the `image` field
2. Recommended format: JPEG, minimum 800×600px, 4:3 aspect ratio for flooring cards, 16:9 for modal view
3. The catalog will automatically use the image instead of the CSS gradient placeholder

Image files are not tracked in this repo by default — add them separately.

---

## How to Deploy to GitHub Pages

GitHub Pages requires the catalog to be in either the `/docs` folder (repo root level) or the root of the `main` branch. The current `/catalog` subdirectory layout requires one of two approaches:

**Option A — Move to `/docs`:**
1. Rename `catalog/` to `docs/`
2. Update internal paths if needed
3. Go to GitHub repository Settings → Pages
4. Set Source: `main` branch, folder: `/docs`

**Option B — GitHub Actions (recommended for subdirectory):**
1. Create `.github/workflows/deploy.yml`
2. Use `actions/upload-pages-artifact` pointing to `./catalog`
3. Set Pages source to GitHub Actions in repository settings

After deployment, the catalog URL will be:
`https://[username].github.io/[repo-name]/`

---

## How to Use During Home Depot Store Visits

1. **Generate a QR code** pointing to the deployed GitHub Pages URL (see playbook in `docs/operating-playbooks/catalog-build-playbook.md`)
2. **Print the QR code** on a business card, shelf talker, or display
3. When a customer or associate scans the code, they land on the catalog homepage
4. **Walk through the catalog** — show flooring collections, explain the matching accessories differentiator, and use the quote form to capture project details
5. **Send project details** to jmaslenko@gmail.com or call 650-645-0306

---

## What NOT to Include

Do not add any of the following to the catalog data files, HTML, JavaScript, or any file in this repository:

- Internal cost prices or cost of goods
- Supplier or manufacturer pricing
- Dealer/distributor pricing (DP pricing)
- Margin or markup percentages
- Internal Home Depot terms, agreements, or vendor contracts
- Wholesale pricing or volume discount schedules
- Any supplier names that are not public-facing

The catalog is a public-facing sales tool. It should only contain information that is appropriate to share with customers and Home Depot store associates.

---

## Files

| File | Purpose |
|------|---------|
| `index.html` | Main catalog page |
| `styles.css` | Complete CSS (premium design, ~700+ lines) |
| `app.js` | All JavaScript — data loading, rendering, filters, modal |
| `data/products.json` | All product data (flooring, stairs, trims) |
| `data/categories.json` | Category definitions and metadata |
| `assets/images/` | Product images (add manually) |
| `assets/logos/` | Brand logos (add manually) |

---

## Contact

**Jacob Maslenko — Calwood Flooring Supply**
- Email: jmaslenko@gmail.com
- Phone: 650-645-0306
- Address: 340 Barneveld Ave, San Francisco, CA 94124
- Home Depot: https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u
