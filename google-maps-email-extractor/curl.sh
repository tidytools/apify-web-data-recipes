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
  "mapsData": "[{\"title\":\"Hofbräuhaus München\",\"address\":\"Platzl 9, 80331 München\",\"website\":\"https://www.hofbraeuhaus.de/\"},{\"title\":\"Daunt Books Marylebone\",\"address\":\"83-84 Marylebone High Street, London W1U 4QW\",\"website\":\"https://dauntbooks.co.uk/\"}]"
}
JSON
