#!/usr/bin/env sh
# Background Remover - Image Converter, Compressor & Resizer: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/ai-image-toolkit (public from 2026-10-08)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-image-toolkit/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "imageUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Canon_EOS_5D_Mark_II_with_50mm_1.4_edit1.jpg/960px-Canon_EOS_5D_Mark_II_with_50mm_1.4_edit1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/960px-Cat03.jpg"
  ]
}
JSON
