#!/usr/bin/env sh
# Bulk URL Status Checker - HTTP Status Codes & Redirects: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/bulk-url-status-checker
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~bulk-url-status-checker/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "urls": [
    "http://python.org",
    "https://github.com/apify/crawlee",
    "https://example.com/this-page-does-not-exist",
    "https://expired.badssl.com/"
  ],
  "includeHtmlSignals": true
}
JSON
