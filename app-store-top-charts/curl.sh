#!/usr/bin/env sh
# App Store Charts & Keyword Rank Tracker - Top Charts, ASO: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/app-store-top-charts (public from 2026-10-14)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~app-store-top-charts/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "mode": "charts",
  "countries": [
    "us",
    "gb"
  ],
  "chartTypes": [
    "topfree"
  ],
  "genres": [
    "all",
    "Productivity"
  ],
  "maxRank": 10,
  "keywords": [
    "habit tracker"
  ],
  "trackApps": [
    "https://apps.apple.com/us/app/habitkit/id6443918070"
  ],
  "resultsPerKeyword": 5
}
JSON
