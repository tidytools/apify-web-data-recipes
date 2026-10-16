#!/usr/bin/env sh
# Google Trends Scraper - Interest, Regions, Trending Now: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/google-trends-scraper
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~google-trends-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "searchTerms": [
    "chatgpt, claude, gemini",
    "sourdough"
  ],
  "geo": "US",
  "trendingGeos": [
    "US"
  ],
  "maxTrendingPerGeo": 25
}
JSON
