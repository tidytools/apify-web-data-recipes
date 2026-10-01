#!/usr/bin/env sh
# Website to Vector Embeddings for RAG - Pinecone, Qdrant: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/website-to-embeddings (public from 2026-10-06)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~website-to-embeddings/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "https://docs.apify.com/academy/web-scraping-for-beginners"
  ],
  "maxPages": 5,
  "removeBoilerplate": true
}
JSON
