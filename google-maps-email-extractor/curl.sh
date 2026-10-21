#!/usr/bin/env sh
# Google Maps Email Extractor - Place Contacts for CRM: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/google-maps-email-extractor
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~google-maps-email-extractor/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "mapsData": "[{\"title\":\"Sample Shop A\",\"address\":\"Example Street 1\",\"categoryName\":\"Shop\",\"website\":\"https://example.com\"},{\"title\":\"Sample Shop B\",\"address\":\"Example Street 2\",\"website\":\"https://example.org\"},{\"title\":\"Sample Shop C\",\"address\":\"Example Street 3\",\"website\":null}]"
}
JSON
