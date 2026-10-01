#!/usr/bin/env sh
# llms.txt Generator & Checker - llms-full.txt, AI SEO (GEO): run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/llms-txt-generator (public from 2026-10-09)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~llms-txt-generator/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "website": "https://docs.apify.com",
  "maxPages": 30
}
JSON
