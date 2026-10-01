#!/usr/bin/env sh
# Trade Show Exhibitor List Scraper - Company, Booth, Website: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/trade-show-exhibitor-list-scraper (public from 2026-10-13)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~trade-show-exhibitor-list-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://slas2026.expofp.com/",
    "https://kbis.a2zinc.net/kbis2026/Public/Exhibitors.aspx?Index=All"
  ],
  "maxExhibitorsPerDirectory": 10
}
JSON
