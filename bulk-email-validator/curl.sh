#!/usr/bin/env sh
# Bulk Email Validator & Email List Cleaner - Disposable Check: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/bulk-email-validator
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~bulk-email-validator/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "emails": [
    "jane.doe@gmail.com",
    "info@stripe.com",
    "sales@apify.com",
    "someone@gmial.com",
    "test@mailinator.com",
    "noreply@github.com",
    "user@example.com",
    "bad..address@gmail.com"
  ]
}
JSON
