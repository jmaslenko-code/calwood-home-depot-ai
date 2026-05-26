#!/usr/bin/env python3
"""
validate_catalog_data.py
Calwood Flooring Supply — Catalog Data Validator

Loads catalog/data/products.json and validates required fields for
all flooring products. Prints a pass/warn report and exits with
code 1 if any required field is missing.

Run from the repo root:

    python3 scripts/catalog_builder/validate_catalog_data.py
"""

import argparse
import json
import sys
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PRODUCTS_FILE = REPO_ROOT / "catalog" / "data" / "products.json"

# ── Required fields for flooring products ───────────────────────────────
REQUIRED_FLOORING_FIELDS = [
    "product_name",
    "category",
    "species",
    "thickness",
    "width",
    "vendor_sku",
    "omsid",
    "home_depot_url",
    "image",
    "matching_accessories",
    "quote_available",
]

# ── ANSI color codes ─────────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
RESET  = "\033[0m"
BOLD   = "\033[1m"


def use_color(force_no_color=False):
    """Return True if color output is supported."""
    if force_no_color:
        return False
    return sys.stdout.isatty()


def check_flooring_product(product, colors=True):
    """
    Validate a single flooring product dict.
    Returns (passed: bool, warnings: list[str]).
    """
    warnings = []
    for field in REQUIRED_FLOORING_FIELDS:
        if field not in product or product[field] is None or product[field] == "":
            warnings.append(f"Missing required field: '{field}'")
    return (len(warnings) == 0), warnings


def validate_products(products_path, colors=True, strict=False):
    """
    Load products.json and validate all flooring entries.
    Returns (total, passed, failed) counts.
    """
    if not products_path.exists():
        msg = f"ERROR: products.json not found at: {products_path}"
        print(f"{RED}{msg}{RESET}" if colors else msg)
        sys.exit(1)

    with open(products_path, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            msg = f"ERROR: Invalid JSON in {products_path}: {e}"
            print(f"{RED}{msg}{RESET}" if colors else msg)
            sys.exit(1)

    flooring = data.get("flooring", [])
    if not flooring:
        print(f"{YELLOW}WARNING: No flooring products found in products.json{RESET}" if colors
              else "WARNING: No flooring products found in products.json")
        return 0, 0, 0

    total = len(flooring)
    passed = 0
    failed = 0

    print(f"\n{BOLD}Validating {total} flooring product(s)...{RESET}\n" if colors
          else f"\nValidating {total} flooring product(s)...\n")

    for product in flooring:
        name = product.get("product_name") or product.get("id") or "(unknown)"
        sku  = product.get("vendor_sku", "SKU TBD")
        ok, warnings = check_flooring_product(product, colors)

        if ok:
            passed += 1
            mark = f"{GREEN}  ✓{RESET}" if colors else "  OK"
            print(f"{mark}  {name}  [{sku}]")
        else:
            failed += 1
            mark = f"{YELLOW}  WARN{RESET}" if colors else "  WARN"
            print(f"{mark}  {name}  [{sku}]")
            for w in warnings:
                indent = f"{YELLOW}        {w}{RESET}" if colors else f"        {w}"
                print(indent)

    print()

    # Summary line
    summary_color = GREEN if failed == 0 else YELLOW
    summary = f"Results: {passed}/{total} passed"
    if failed:
        summary += f"  |  {failed} with warnings"
    print(f"{summary_color}{BOLD}{summary}{RESET}\n" if colors else f"{summary}\n")

    # Additional section counts
    stair_treads = data.get("stair_treads", [])
    risers       = data.get("risers", [])
    trims        = data.get("trim_accessories", [])
    print(f"  Stair treads:      {len(stair_treads)}")
    print(f"  Risers:            {len(risers)}")
    print(f"  Trim accessories:  {len(trims)}")
    print()

    return total, passed, failed


def main():
    parser = argparse.ArgumentParser(
        description="Validate Calwood catalog products.json for required fields."
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable color output.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 on any warning (not just errors).",
    )
    parser.add_argument(
        "--file",
        default=str(PRODUCTS_FILE),
        help=f"Path to products.json (default: {PRODUCTS_FILE})",
    )
    args = parser.parse_args()

    colors = use_color(force_no_color=args.no_color)
    products_path = Path(args.file)

    total, passed, failed = validate_products(products_path, colors=colors, strict=args.strict)

    if failed > 0 or (args.strict and passed < total):
        exit_msg = "Validation completed with warnings. Review missing fields above."
        print(f"{YELLOW}{exit_msg}{RESET}" if colors else exit_msg)
        sys.exit(1)
    else:
        exit_msg = "Validation passed. All required fields present."
        print(f"{GREEN}{exit_msg}{RESET}" if colors else exit_msg)
        sys.exit(0)


if __name__ == "__main__":
    main()
