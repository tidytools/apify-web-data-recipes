#!/usr/bin/env sh
# Website Traffic Rank Checker - Similarweb Alternative, Bulk: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/website-traffic-rank (public from 2026-10-13)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~website-traffic-rank/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "domains": [
    "apify.com",
    "notion.so",
    "shopify.com",
    "bbc.co.uk",
    "tools.yukai.uk"
  ],
  "countries": [
    "us",
    "gb"
  ]
}
JSON
