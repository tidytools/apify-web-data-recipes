#!/usr/bin/env sh
# Bulk WHOIS & DNS Lookup - Domain Age, Expiry, Availability: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/bulk-domain-whois-dns-lookup (public from 2026-10-06)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~bulk-domain-whois-dns-lookup/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "domains": [
    "github.com",
    "https://www.bbc.co.uk/news",
    "spiegel.de",
    "sony.jp"
  ]
}
JSON
