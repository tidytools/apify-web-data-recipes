#!/usr/bin/env sh
# Decision Maker Finder - CEOs, Founders & VPs from Websites: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/decision-maker-finder
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~decision-maker-finder/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "companies": [
    "apify.com",
    "buffer.com"
  ],
  "titleContains": [
    "CEO",
    "CTO",
    "CFO",
    "COO",
    "CMO",
    "Chief",
    "Founder",
    "Owner",
    "President",
    "VP",
    "Head",
    "Director",
    "General Manager",
    "Managing"
  ]
}
JSON
