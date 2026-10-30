#!/usr/bin/env sh
# B2B Leads by City - Dentist, Lawyer & HVAC Contact Lists: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/b2b-lead-lists
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~b2b-lead-lists/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "searchTerms": [
    "dentist"
  ],
  "location": "Austin, TX",
  "maxResults": 2,
  "maxAgeDays": 30
}
JSON
