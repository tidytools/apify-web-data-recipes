#!/usr/bin/env sh
# AI Image Upscaler - Bulk Photos and TSV to 2x or 4x: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/ai-image-upscaler
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-image-upscaler/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "imageUrls": [
    "https://images.unsplash.com/photo-1500534623283-312aade485b7?w=250&fm=webp"
  ],
  "scale": 4,
  "format": "webp"
}
JSON
