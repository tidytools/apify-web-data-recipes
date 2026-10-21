#!/usr/bin/env sh
# Video Transcript - Direct Video Files to SRT: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/video-transcript-files
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~video-transcript-files/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://archive.org/download/gerald-ford-inaugural-address-august-9-1974-720p/Gerald%20Ford%20inaugural%20address_%20August%209%2C%201974%20%28720p%29.mp4"
  ],
  "podcastFeeds": []
}
JSON
