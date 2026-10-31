#!/usr/bin/env sh
# YouTube Shorts Channel Scraper - Public Channel Shorts: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/youtube-shorts-channel
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~youtube-shorts-channel/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://www.youtube.com/@mkbhd",
    "https://www.youtube.com/@veritasium",
    "https://www.youtube.com/@NASA"
  ],
  "tabs": [
    "shorts"
  ],
  "maxVideos": 10
}
JSON
