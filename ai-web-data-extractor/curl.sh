#!/usr/bin/env sh
# AI Web Scraper - Extract Structured Data & URL to JSON: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/ai-web-data-extractor
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-web-data-extractor/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  ],
  "fields": {
    "title": "string",
    "price": "number",
    "in_stock": "boolean",
    "stock_count": "integer",
    "upc": "string"
  }
}
JSON
