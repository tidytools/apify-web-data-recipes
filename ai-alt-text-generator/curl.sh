#!/usr/bin/env sh
# AI Alt Text Generator - Image Alt Text & Image Captions: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/ai-alt-text-generator (public from 2026-10-06)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-alt-text-generator/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urlsText": "https://www.apple.com",
  "maxImagesPerPage": 10,
  "maxImages": 20
}
JSON
