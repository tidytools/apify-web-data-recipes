#!/usr/bin/env sh
# Website Email Finder - Fill Missing Company Emails: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/website-email-finder-crm
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~website-email-finder-crm/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "rows": [
    {
      "row_number": 1,
      "Website": "hofbraeuhaus.de",
      "Email": ""
    }
  ],
  "domains": []
}
JSON
