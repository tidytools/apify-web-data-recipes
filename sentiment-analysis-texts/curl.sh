#!/usr/bin/env sh
# Review Sentiment Analysis - Reviews, Posts & Support Texts: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/sentiment-analysis-texts
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~sentiment-analysis-texts/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "texts": [
    "Great product, arrived early.",
    "Terrible support, never again.",
    "Good price but the box was damaged."
  ]
}
JSON
