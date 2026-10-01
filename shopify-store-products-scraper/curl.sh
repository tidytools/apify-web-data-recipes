#!/usr/bin/env sh
# Shopify Scraper - Shopify Products, Prices & Stock Monitor: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/shopify-store-products-scraper (public from 2026-10-11)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~shopify-store-products-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "stores": [
    "https://www.allbirds.com",
    "https://www.tentree.com"
  ],
  "maxProductsPerStore": 20
}
JSON
