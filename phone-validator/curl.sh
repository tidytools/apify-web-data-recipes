#!/usr/bin/env sh
# Bulk Phone Number Validator - Format, Type & Country: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/phone-validator (public from 2026-10-06)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~phone-validator/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "phones": [
    "+1 650-253-0000",
    "+44 20 7946 0958 ext. 12",
    "+49 30 901820",
    "0912 345 678",
    "(02) 2345-6789",
    "+1 800 555 0199",
    "+1 123 456 7890",
    "+44 20 7946"
  ],
  "defaultCountry": "TW"
}
JSON
