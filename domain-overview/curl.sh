#!/usr/bin/env sh
# Domain Overview - Semrush & Ahrefs Alternative, Tech & Hiring: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/domain-overview (public from 2026-10-13)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~domain-overview/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "domains": [
    "stripe.com",
    "figma.com",
    "apify.com",
    "bbc.co.uk",
    "tools.yukai.uk"
  ]
}
JSON
