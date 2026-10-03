#!/usr/bin/env sh
# Google Ads Transparency Scraper - Competitor Ads by Domain: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/ads-transparency (public from 2026-10-12)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ads-transparency/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "advertisers": [
    "Nike, Inc."
  ],
  "domains": [
    "notion.so"
  ],
  "region": "US",
  "maxAdsPerSearch": 20
}
JSON
