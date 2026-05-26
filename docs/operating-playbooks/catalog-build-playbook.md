# Catalog Build Playbook
## Calwood Flooring Supply — Home Depot Online Catalog

This playbook covers how to build, maintain, and use the Calwood product catalog. Follow this guide when adding new SKUs, updating product data, generating QR codes, or using the catalog during store visits.

---

## What Product Data Is Needed Before Adding a New SKU

Before adding a new product to `catalog/data/products.json`, collect the following:

**Required:**
- `product_name` — Display name as it appears on HomeDepot.com (e.g., "Cotton", "Sandy")
- `collection` — Collection name (Supreme, Woodline, Icon, or TBD)
- `species` — Species as listed on the product page
- `thickness` and `width` — Exact dimensions from the spec sheet
- `vendor_sku` — The Home Depot SKU or model number on the product listing
- `home_depot_url` — Direct URL to the product on HomeDepot.com
- `price_per_sqft` and `case_price` — From the active HomeDepot.com listing
- `sq_ft_per_case` — From the product listing or packaging
- `color_family` — One of: white, beige, gray, brown, natural (used for CSS color placeholder)

**Recommended:**
- `finish` — Full finish description (e.g., "UV Oil Matte, 50-Year Finish Warranty")
- `construction` — Construction type (e.g., "Wire Brushed Engineered, Tongue & Groove")
- `veneer` — Veneer thickness if available
- `installation` — Installation methods accepted
- `warranty` — Warranty description

**If not yet confirmed:**
- Set `data_source` to `"TBD — not yet listed on HomeDepot.com"`
- Set `vendor_sku` to `"SKU TBD"`
- Set `home_depot_url` to `"Home Depot URL TBD"`
- Set `omsid` to `"OMSID TBD"` — never invent a fake OMSID

---

## How to Map Internal Supplier / Palazzo Names to Display Names

Calwood receives products from suppliers who may use internal or Italian naming conventions (Palazzo names). The HomeDepot.com listing uses different consumer-facing color names.

**Mapping process:**
1. Find the active product listing on HomeDepot.com
2. Use the consumer-facing name from the listing as `product_name`
3. The internal/supplier/Palazzo name can be stored in the `notes` field if needed for internal reference — do NOT expose it in the catalog UI
4. When the HD name and supplier name differ, always use the HD name in the catalog

**Example mapping format in notes field (internal only):**
```
"notes": "Supreme Collection, White Oak. Internal ref: [internal-code]"
```

Do not include actual supplier names, Palazzo catalog names, or internal order codes in any public-facing field.

---

## How to Find and Organize Product Images

**Finding images:**
1. Navigate to the product page on HomeDepot.com
2. Right-click the primary product image and select "Open image in new tab"
3. Download the full-resolution image (typically 1000×1000px or larger)
4. Also check the brand page: https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u

**Organizing images:**
1. Save all images to `catalog/assets/images/`
2. Use lowercase, hyphenated filenames matching the `image` field in `products.json`
   - Example: `supreme-cotton.jpg`, `woodline-spirit.jpg`, `icon-sandy.jpg`
3. Recommended minimum size: 800×600px (4:3 ratio for product cards)
4. Format: JPEG, quality 80–90% to balance file size and quality
5. The catalog will automatically use the image file if it exists at the path in the `image` field

**For stair and trim products:**
- Use lifestyle or closeup photos that clearly show grain and finish
- If no photo is available, the catalog displays a CSS gradient color placeholder automatically

---

## How to Find Home Depot OMSIDs and Product URLs

**Finding an OMSID:**
The OMSID (Order Management System ID) is an internal Home Depot identifier.
- It appears in the product URL: `homedepot.com/p/.../[OMSID]`
- Example: `homedepot.com/p/Cotton-5-8-in-T.../312345678` — the number at the end is the OMSID
- It may also appear in the Special Order or QuoteCenter system

**If you cannot find the OMSID:**
- Set `"omsid": "OMSID TBD"` in `products.json`
- Contact the Home Depot Special Order desk with the vendor SKU to look it up
- Do NOT invent or guess an OMSID

**Finding and adding Home Depot listing links:**
1. Go to https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u (Calwood brand page)
2. Click into each product
3. Copy the full product URL
4. Paste it into the `home_depot_url` field in `products.json`

For products not yet listed, use `"Home Depot URL TBD"` — the catalog will still work and will link to the brand page instead.

---

## How to Generate a QR Code for Store Visits

**Target URL:** Your deployed GitHub Pages catalog URL, e.g.:
`https://[username].github.io/calwood-home-depot-ai/`

**Recommended tool:** https://www.qr-code-monkey.com

**Steps:**
1. Go to https://www.qr-code-monkey.com
2. Paste your GitHub Pages catalog URL into the URL field
3. Choose a size: 500×500px minimum for print; 1000×1000px for large format
4. Add your brand color (dark green: #1d3d28) as the QR foreground color
5. Add the CW logo or "Scan for Catalog" label text if the tool supports it
6. Download as PNG (for digital) or SVG (for print)
7. Test the QR code with your phone before printing

**Where to use the QR code:**
- Business cards
- Shelf talkers / hang tags near flooring samples
- Counter displays at the flooring department
- Printed project quote sheets
- Email signatures

---

## How to Use the Catalog During Store Visits

**What to say when opening the catalog:**

> "Here's our full product line — you can browse it on your phone too. Let me show you the collections we have available through Home Depot Special Order."

**What to show:**

1. **Hero / brand intro** — Establish that Calwood is a Home Depot vendor, SF Bay Area company
2. **Flooring Collections** — Filter by collection or species to narrow to what the customer is interested in. Click "View Details" to open the product modal with full specs.
3. **Matching Accessories section** — This is the key differentiator. Emphasize: "If you choose a Calwood floor, we can match the stair treads, risers, T-moldings, reducers, and vents to the same species and finish. Most vendors can't do this."
4. **Stair section** — Show confirmed SKUs and pricing for White Oak treads and risers
5. **Project Packages** — Use these to help scope the project: Package 1 (flooring only), Package 2 (flooring + trims), Package 3 (full stair + accessories)

**How to take order details:**

Use the Quote Request form on the catalog page, OR collect:
- Customer name, phone, and email
- Flooring color/species selected
- Square footage per room
- Stair count (treads and risers needed)
- Trim/accessory needs
- Project city and delivery location
- Timeline
- Home Depot store number

**Send collected details to:**
- Email: jmaslenko@gmail.com
- Phone: 650-645-0306

---

## What NOT to Include Publicly

The catalog is deployed to GitHub Pages and is publicly accessible. Do not add any of the following to any file in this repository:

- Internal cost of goods or landed cost per unit
- Margin or markup targets
- DP (dealer/distributor) pricing
- Supplier names that are not on the public HD listing
- Palazzo or internal collection names
- Any terms from the Calwood–Home Depot vendor agreement
- Volume discount schedules
- Wholesale or contract pricing for contractors
- Any internal Home Depot system IDs beyond what is publicly visible in product URLs

If project notes or internal references are needed, keep them in a private document outside this repository.

---

## Maintenance Schedule

| Task | Frequency |
|------|-----------|
| Verify all confirmed HD product URLs are still live | Monthly |
| Update prices if HD listing prices change | As needed (check HD listing) |
| Add new SKUs when products go live on HD | As available |
| Replace placeholder products with confirmed data | As products launch |
| Check for broken images | Before any store visit |
| Regenerate QR codes if the GitHub Pages URL changes | When URL changes |

---

## Contact

**Jacob Maslenko — Calwood Flooring Supply**
- Email: jmaslenko@gmail.com
- Phone: 650-645-0306
- Address: 340 Barneveld Ave, San Francisco, CA 94124
- Home Depot brand page: https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u
