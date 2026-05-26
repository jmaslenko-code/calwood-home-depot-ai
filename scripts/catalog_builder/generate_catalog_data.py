#!/usr/bin/env python3
"""
generate_catalog_data.py
Calwood Flooring Supply — Catalog Data Generator

Generates catalog/data/products.json and catalog/data/categories.json
from Python dictionaries. Run from the repo root:

    python3 scripts/catalog_builder/generate_catalog_data.py

Use --dry-run to preview output without writing files.
"""

import argparse
import json
import os
import sys
from pathlib import Path

# ── Output paths ────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CATALOG_DATA_DIR = REPO_ROOT / "catalog" / "data"
PRODUCTS_FILE = CATALOG_DATA_DIR / "products.json"
CATEGORIES_FILE = CATALOG_DATA_DIR / "categories.json"

# ── Categories ──────────────────────────────────────────────────────────
CATEGORIES = [
    {
        "id": "engineered-hardwood",
        "name": "Engineered Hardwood Flooring",
        "slug": "engineered-hardwood",
        "short_description": "Wire brushed European White Oak engineered hardwood with a 3.5mm veneer and 50-year finish warranty. Available in multiple collections, widths, and colors.",
        "use_case": "Installs as the primary floor surface in living rooms, bedrooms, hallways, and open-plan spaces.",
        "badge_quotecenter": True,
        "badge_matching": True,
    },
    {
        "id": "stair-treads",
        "name": "Stair Treads",
        "slug": "stair-treads",
        "short_description": "Unfinished European White Oak stair treads in multiple lengths, ready to finish on-site to match any Calwood flooring product.",
        "use_case": "Forms the horizontal walking surface on each stair step, matching the flooring species and finish.",
        "badge_quotecenter": True,
        "badge_matching": True,
    },
    {
        "id": "risers",
        "name": "Stair Risers",
        "slug": "risers",
        "short_description": "Unfinished European White Oak risers, 0.75\" thick, available in multiple lengths for a clean finished staircase.",
        "use_case": "Covers the vertical face between stair steps.",
        "badge_quotecenter": True,
        "badge_matching": True,
    },
    {
        "id": "stair-nose",
        "name": "Stair Nose",
        "slug": "stair-nose",
        "short_description": "Matching stair nose profiles that cap the exposed leading edge of flooring at the top or intermediate stair step.",
        "use_case": "Caps the exposed edge of flooring at the top of a stair step.",
        "badge_quotecenter": True,
        "badge_matching": True,
    },
    {
        "id": "reducer",
        "name": "Reducer",
        "slug": "reducer",
        "short_description": "Matching wood reducer moldings that step down from hardwood to a lower adjacent surface such as tile or carpet.",
        "use_case": "Transitions flooring down to a lower surface like tile or carpet.",
        "badge_quotecenter": False,
        "badge_matching": True,
    },
    {
        "id": "t-molding",
        "name": "T-Molding",
        "slug": "t-molding",
        "short_description": "Matching T-molding profiles that bridge two equal-height floors at doorways or open room transitions.",
        "use_case": "Bridges two equal-height flooring surfaces at doorways or room transitions.",
        "badge_quotecenter": False,
        "badge_matching": True,
    },
    {
        "id": "end-cap",
        "name": "End Cap",
        "slug": "end-cap",
        "short_description": "Matching end cap moldings that provide a finished termination where hardwood flooring meets a wall or vertical surface.",
        "use_case": "Finishes a flooring edge against a wall or vertical surface.",
        "badge_quotecenter": False,
        "badge_matching": True,
    },
    {
        "id": "baby-threshold",
        "name": "Baby Threshold",
        "slug": "baby-threshold",
        "short_description": "Low-profile matching wood thresholds for doorway transitions where minimal height change is required.",
        "use_case": "Creates a smooth low-profile transition at doorways.",
        "badge_quotecenter": False,
        "badge_matching": True,
    },
    {
        "id": "wood-vent",
        "name": "Wood Vents / Registers",
        "slug": "wood-vent",
        "short_description": "Matching wood floor vents and registers milled from the same species as the flooring.",
        "use_case": "Replaces standard metal floor vents with matching wood for a seamless look.",
        "badge_quotecenter": False,
        "badge_matching": True,
    },
    {
        "id": "custom-profile",
        "name": "Custom Profiles",
        "slug": "custom-profile",
        "short_description": "Made-to-order custom milled trim profiles to match any Calwood flooring product — any species, finish, and profile shape.",
        "use_case": "Made-to-order trim profiles to match any Calwood flooring product.",
        "badge_quotecenter": True,
        "badge_matching": True,
    },
]

# ── Flooring helper ─────────────────────────────────────────────────────
_SUPREME_BASE = dict(
    collection="Supreme",
    category="flooring",
    species="White Oak",
    construction="Wire Brushed Engineered, Tongue & Groove",
    finish="UV Oil Matte, 50-Year Finish Warranty",
    thickness='5/8"',
    width='7.5"',
    veneer="3.5mm",
    sq_ft_per_case=30.35,
    case_price=212.15,
    price_per_sqft=6.99,
    installation="Nail, Staple, or Glue",
    warranty="50-Year Finish Warranty",
    omsid="OMSID TBD",
    home_depot_url="https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u",
    matching_accessories=True,
    quote_available=True,
    data_source="Confirmed — HomeDepot.com listing",
    notes="Supreme Collection, White Oak, wire brushed, prefinished.",
)

_WOODLINE_BASE = dict(
    collection="Woodline",
    category="flooring",
    species="Western European Oak",
    construction="Wire Brushed Engineered, Tongue & Groove, 3-Ply Core",
    finish="UV Oil, Wire Brushed",
    thickness='7/8"',
    width='7.5"',
    veneer="TBD",
    sq_ft_per_case=20.55,
    case_price=184.74,
    installation="Nail, Staple, or Glue",
    warranty="Manufacturer Warranty",
    omsid="OMSID TBD",
    home_depot_url="https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u",
    matching_accessories=True,
    quote_available=True,
)


def _make_flooring(id_, name, sku, color_family, extra_notes="", **overrides):
    base = {**_SUPREME_BASE}
    base.update(overrides)
    base.update(
        id=id_,
        product_name=name,
        vendor_sku=sku,
        color_family=color_family,
        image=f"assets/images/{id_}.jpg",
        notes=extra_notes or base.get("notes", ""),
    )
    return base


# ── Flooring products ────────────────────────────────────────────────────
FLOORING = [
    # Supreme Collection
    _make_flooring("supreme-cotton",         "Cotton",          "LM2U712COT",     "beige"),
    _make_flooring("supreme-andante",        "Andante",         "LM2U712AND",     "beige"),
    _make_flooring("supreme-beige",          "Beige",           "LM2U712BEIGE",   "beige"),
    _make_flooring("supreme-cream",          "Cream",           "LM2U712CREAM",   "white"),
    _make_flooring("supreme-jade-rustic",    "Jade Rustic",     "LM2U712REJADE",  "beige",
                   extra_notes="Supreme Collection, White Oak, rustic grade, wire brushed, prefinished."),
    _make_flooring("supreme-jubilee",        "Jubilee",         "LM2U712REJEW",   "white"),
    _make_flooring("supreme-kashmire-rustic","Kashmire Rustic", "LM2U712REKASH",  "beige",
                   extra_notes="Supreme Collection, White Oak, rustic grade, wire brushed, prefinished."),
    _make_flooring("supreme-opal-rustic",    "Opal Rustic",     "LM2U712REOPAL",  "white",
                   extra_notes="Supreme Collection, White Oak, rustic grade, wire brushed, prefinished."),
    _make_flooring("supreme-pearl-rustic",   "Pearl Rustic",    "LM2U712REPEARL", "white",
                   extra_notes="Supreme Collection, White Oak, rustic grade, wire brushed, prefinished."),
    _make_flooring("supreme-horizon",        "Horizon",         "LM2U712HOR",     "gray",
                   extra_notes="Supreme Collection, White Oak, gray tone, wire brushed, prefinished."),

    # Woodline Collection
    {
        **_WOODLINE_BASE,
        "id": "woodline-spirit",
        "product_name": "Spirit",
        "color_family": "white",
        "price_per_sqft": 8.99,
        "vendor_sku": "WL-SPIRIT",
        "image": "assets/images/woodline-spirit.jpg",
        "data_source": "Confirmed — HomeDepot.com listing",
        "notes": "Woodline Collection, Western European Oak, wire brushed, prefinished.",
    },
    {
        **_WOODLINE_BASE,
        "id": "woodline-strasbourg",
        "product_name": "Strasbourg",
        "color_family": "beige",
        "price_per_sqft": 8.74,
        "vendor_sku": "WL-STRASBOURG",
        "image": "assets/images/woodline-strasbourg.jpg",
        "data_source": "Estimated",
        "notes": "Woodline Collection, Western European Oak. Price estimated — verify on HomeDepot.com.",
    },
    {
        **_WOODLINE_BASE,
        "id": "woodline-aspen",
        "product_name": "Aspen",
        "color_family": "white",
        "price_per_sqft": 10.87,
        "vendor_sku": "WL-ASPEN",
        "image": "assets/images/woodline-aspen.jpg",
        "data_source": "Estimated",
        "notes": "Woodline Collection, Western European Oak. Price estimated — verify on HomeDepot.com.",
    },
    {
        **_WOODLINE_BASE,
        "id": "woodline-honey",
        "product_name": "Honey",
        "color_family": "beige",
        "price_per_sqft": 9.49,
        "vendor_sku": "WL-HONEY",
        "image": "assets/images/woodline-honey.jpg",
        "data_source": "Estimated",
        "notes": "Woodline Collection, Western European Oak. Price estimated — verify on HomeDepot.com.",
    },

    # Icon Collection
    {
        "id": "icon-sandy",
        "product_name": "Sandy",
        "collection": "Icon",
        "category": "flooring",
        "species": "White Oak",
        "construction": "Wire Brushed Engineered, 3-Ply Core",
        "finish": "Matte Aluminum Oxide",
        "color_family": "beige",
        "thickness": '5/8"',
        "width": '7.2"',
        "veneer": "TBD",
        "sq_ft_per_case": 39.92,
        "case_price": 279.04,
        "price_per_sqft": 6.99,
        "installation": "Nail, Staple, or Glue",
        "warranty": "Manufacturer Warranty",
        "vendor_sku": "LM6U5873T6CSAN",
        "omsid": "OMSID TBD",
        "home_depot_url": "https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u",
        "image": "assets/images/icon-sandy.jpg",
        "matching_accessories": True,
        "quote_available": True,
        "data_source": "Confirmed — HomeDepot.com listing",
        "notes": "Icon Collection, White Oak, matte aluminum oxide finish, 39.92 sq.ft. per case.",
    },

    # Placeholder products
    {
        "id": "tbd-natural-white-oak",
        "product_name": "Natural White Oak",
        "collection": "TBD",
        "category": "flooring",
        "species": "White Oak",
        "construction": "TBD",
        "finish": "TBD",
        "color_family": "white",
        "thickness": "TBD",
        "width": "TBD",
        "veneer": "TBD",
        "sq_ft_per_case": "TBD",
        "case_price": "TBD",
        "price_per_sqft": "TBD",
        "installation": "TBD",
        "warranty": "TBD",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "image": "assets/images/placeholder-white-oak.jpg",
        "matching_accessories": True,
        "quote_available": True,
        "data_source": "TBD — not yet listed on HomeDepot.com",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
    {
        "id": "tbd-rustic-white-oak",
        "product_name": "Rustic White Oak",
        "collection": "TBD",
        "category": "flooring",
        "species": "White Oak",
        "construction": "TBD",
        "finish": "TBD",
        "color_family": "beige",
        "thickness": "TBD",
        "width": "TBD",
        "veneer": "TBD",
        "sq_ft_per_case": "TBD",
        "case_price": "TBD",
        "price_per_sqft": "TBD",
        "installation": "TBD",
        "warranty": "TBD",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "image": "assets/images/placeholder-rustic-white-oak.jpg",
        "matching_accessories": True,
        "quote_available": True,
        "data_source": "TBD — not yet listed on HomeDepot.com",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
    {
        "id": "tbd-red-oak-flooring",
        "product_name": "Red Oak Flooring",
        "collection": "TBD",
        "category": "flooring",
        "species": "Red Oak",
        "construction": "TBD",
        "finish": "TBD",
        "color_family": "brown",
        "thickness": "TBD",
        "width": "TBD",
        "veneer": "TBD",
        "sq_ft_per_case": "TBD",
        "case_price": "TBD",
        "price_per_sqft": "TBD",
        "installation": "TBD",
        "warranty": "TBD",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "image": "assets/images/placeholder-red-oak.jpg",
        "matching_accessories": True,
        "quote_available": True,
        "data_source": "TBD — not yet listed on HomeDepot.com",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
    {
        "id": "tbd-maple-flooring",
        "product_name": "Maple Flooring",
        "collection": "TBD",
        "category": "flooring",
        "species": "Maple",
        "construction": "TBD",
        "finish": "TBD",
        "color_family": "white",
        "thickness": "TBD",
        "width": "TBD",
        "veneer": "TBD",
        "sq_ft_per_case": "TBD",
        "case_price": "TBD",
        "price_per_sqft": "TBD",
        "installation": "TBD",
        "warranty": "TBD",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "image": "assets/images/placeholder-maple.jpg",
        "matching_accessories": True,
        "quote_available": True,
        "data_source": "TBD — not yet listed on HomeDepot.com",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
]

# ── Stair treads ─────────────────────────────────────────────────────────
STAIR_TREADS = [
    {
        "id": "tread-euro-white-oak",
        "product_name": "Euro White Oak Stair Tread",
        "species": "European White Oak",
        "thickness": '1-1/16"',
        "width": '11.5"',
        "lengths_available": ["36 in.", "48 in.", "60 in.", "72 in."],
        "finish": "Unfinished",
        "vendor_sku": "TR085PTSWO",
        "omsid": "OMSID TBD",
        "home_depot_url": "https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u",
        "price_per_unit": 54.99,
        "quote_available": True,
        "data_source": "Confirmed",
        "notes": "Unfinished — finish on-site to match any Calwood flooring. Rating: 4.7 (9 reviews). Multiple lengths available.",
    },
    {
        "id": "tread-red-oak",
        "product_name": "Red Oak Stair Tread",
        "species": "Red Oak",
        "thickness": "TBD",
        "width": "TBD",
        "lengths_available": ["TBD"],
        "finish": "Unfinished",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "price_per_unit": "TBD",
        "quote_available": True,
        "data_source": "TBD",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
    {
        "id": "tread-maple",
        "product_name": "Maple Stair Tread",
        "species": "Maple",
        "thickness": "TBD",
        "width": "TBD",
        "lengths_available": ["TBD"],
        "finish": "Unfinished",
        "vendor_sku": "SKU TBD",
        "omsid": "OMSID TBD",
        "home_depot_url": "Home Depot URL TBD",
        "price_per_unit": "TBD",
        "quote_available": True,
        "data_source": "TBD",
        "notes": "Placeholder — contact Calwood for availability and pricing.",
    },
]

# ── Risers ───────────────────────────────────────────────────────────────
RISERS = [
    {
        "id": "riser-euro-white-oak",
        "product_name": "Euro White Oak Stair Riser",
        "species": "European White Oak",
        "thickness": '0.75"',
        "width": '7.5"',
        "lengths_available": ["36 in.", "48 in.", "60 in."],
        "finish": "Unfinished",
        "vendor_sku": "TRRBSP34WO36",
        "omsid": "OMSID TBD",
        "home_depot_url": "https://www.homedepot.com/b/CALWOOD/N-5yc1vZ119u",
        "price_per_unit": 39.99,
        "quote_available": True,
        "data_source": "Confirmed",
        "notes": "Unfinished — finish on-site to match any Calwood flooring or stair tread. Multiple lengths available.",
    },
]

# ── Trim accessories ─────────────────────────────────────────────────────
_TRIM_BASE = dict(
    vendor_sku="SKU TBD",
    omsid="OMSID TBD",
    home_depot_url="Home Depot URL TBD",
    species_available=["White Oak", "Red Oak", "Maple"],
    matching_available=True,
    quote_available=True,
    data_source="TBD — contact Calwood for availability",
)

TRIM_ACCESSORIES = [
    {**_TRIM_BASE, "id": "trim-stair-nose", "product_name": "Stair Nose", "trim_type": "stair_nose",
     "description": "Matching stair nose profiles that cap the exposed leading edge of flooring at the top of a stair step. Available in White Oak, Red Oak, and Maple to match any Calwood flooring product.",
     "use_case": "Caps the exposed edge of flooring at the top of a stair step for a safe, finished transition.",
     "image": "assets/images/trim-stair-nose.jpg"},
    {**_TRIM_BASE, "id": "trim-reducer", "product_name": "Reducer", "trim_type": "reducer",
     "description": "Matching wood reducer moldings that step down from hardwood flooring to a lower adjacent surface. Available in White Oak, Red Oak, and Maple.",
     "use_case": "Transitions flooring down to a lower surface like tile or carpet.",
     "image": "assets/images/trim-reducer.jpg"},
    {**_TRIM_BASE, "id": "trim-t-molding", "product_name": "T-Molding", "trim_type": "t_molding",
     "description": "Matching T-molding profiles that bridge two flooring surfaces of equal height at doorways or open room transitions. Machined to match Calwood flooring species and finish.",
     "use_case": "Bridges two equal-height flooring surfaces at doorways or room transitions.",
     "image": "assets/images/trim-t-molding.jpg"},
    {**_TRIM_BASE, "id": "trim-end-cap", "product_name": "End Cap", "trim_type": "end_cap",
     "description": "Matching end cap moldings that provide a finished termination where hardwood flooring meets a wall or vertical surface. Available in all Calwood species.",
     "use_case": "Finishes a flooring edge against a wall or vertical surface.",
     "image": "assets/images/trim-end-cap.jpg"},
    {**_TRIM_BASE, "id": "trim-baby-threshold", "product_name": "Baby Threshold", "trim_type": "baby_threshold",
     "description": "Low-profile matching wood thresholds for doorway transitions where minimal height change is required. A clean, refined solution for room-to-room transitions.",
     "use_case": "Creates a smooth low-profile transition at doorways.",
     "image": "assets/images/trim-baby-threshold.jpg"},
    {**_TRIM_BASE, "id": "trim-flush-vent", "product_name": "Flush Wood Vent", "trim_type": "flush_vent",
     "description": "Flush-mount wood floor vents milled from the same species as the Calwood flooring for a completely seamless integrated look.",
     "use_case": "Replaces standard metal floor vents with matching wood for a seamless look.",
     "image": "assets/images/trim-flush-vent.jpg"},
    {**_TRIM_BASE, "id": "trim-surface-mount-vent", "product_name": "Surface Mount Wood Register", "trim_type": "surface_mount_vent",
     "description": "Surface-mount wood floor registers in matching species and finish. A premium upgrade from standard metal registers that visually disappear into the floor.",
     "use_case": "Replaces standard metal floor vents with matching wood for a seamless look.",
     "image": "assets/images/trim-surface-mount-vent.jpg"},
    {**_TRIM_BASE, "id": "trim-custom-profile", "product_name": "Custom Profile", "trim_type": "custom_profile",
     "description": "Made-to-order custom milled trim profiles to match any Calwood flooring product. Any species, any finish, any profile shape — machined to exact project specifications.",
     "use_case": "Made-to-order trim profiles to match any Calwood flooring product.",
     "image": "assets/images/trim-custom-profile.jpg"},
]

# ── Main ─────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Generate Calwood catalog JSON data files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output to stdout without writing files.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(CATALOG_DATA_DIR),
        help=f"Output directory (default: {CATALOG_DATA_DIR})",
    )
    args = parser.parse_args()

    products_data = {
        "flooring": FLOORING,
        "stair_treads": STAIR_TREADS,
        "risers": RISERS,
        "trim_accessories": TRIM_ACCESSORIES,
    }

    products_json  = json.dumps(products_data, indent=2, ensure_ascii=False)
    categories_json = json.dumps(CATEGORIES, indent=2, ensure_ascii=False)

    if args.dry_run:
        print("=== products.json (dry run) ===")
        print(products_json[:400], "...\n")
        print("=== categories.json (dry run) ===")
        print(categories_json[:400], "...\n")
    else:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        products_path = out_dir / "products.json"
        categories_path = out_dir / "categories.json"

        products_path.write_text(products_json, encoding="utf-8")
        categories_path.write_text(categories_json, encoding="utf-8")

        print(f"Written: {products_path}")
        print(f"Written: {categories_path}")

    # Summary
    flooring_confirmed = sum(1 for p in FLOORING if "Confirmed" in str(p.get("data_source", "")))
    flooring_estimated = sum(1 for p in FLOORING if "Estimated" in str(p.get("data_source", "")))
    flooring_tbd       = sum(1 for p in FLOORING if "TBD" in str(p.get("data_source", "")))

    print("\n=== Generation Summary ===")
    print(f"  Categories:         {len(CATEGORIES)}")
    print(f"  Flooring products:  {len(FLOORING)}")
    print(f"    - Confirmed:      {flooring_confirmed}")
    print(f"    - Estimated:      {flooring_estimated}")
    print(f"    - Placeholder:    {flooring_tbd}")
    print(f"  Stair treads:       {len(STAIR_TREADS)}")
    print(f"  Risers:             {len(RISERS)}")
    print(f"  Trim accessories:   {len(TRIM_ACCESSORIES)}")
    print("Done.")


if __name__ == "__main__":
    main()
