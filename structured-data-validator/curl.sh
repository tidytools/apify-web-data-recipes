#!/usr/bin/env sh
# Schema Markup Validator - JSON-LD Structured Data Checker: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/structured-data-validator (public from 2026-10-05)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~structured-data-validator/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://www.allbirds.com/products/mens-tree-runners",
    "https://www.ikea.com/us/en/p/billy-bookcase-white-00263850/",
    "https://stripe.com/",
    "https://webscraper.io/test-sites/e-commerce/allinone/product/60"
  ]
}
JSON
