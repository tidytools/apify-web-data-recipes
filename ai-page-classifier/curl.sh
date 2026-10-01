#!/usr/bin/env sh
# Website Classifier & Text Classifier - Industry & Sentiment: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/ai-page-classifier (public from 2026-10-07)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-page-classifier/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "domains": [
    "https://stripe.com/pricing",
    "https://docs.python.org/3/tutorial/index.html",
    "https://www.bbc.com/news",
    "https://www.allbirds.com/products/mens-tree-runners"
  ]
}
JSON
