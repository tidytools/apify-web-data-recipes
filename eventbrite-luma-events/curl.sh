#!/usr/bin/env sh
# Eventbrite Scraper & Luma Scraper - Events, Venues, Organizers: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: apify.com/tidytools/eventbrite-luma-events (public from 2026-10-16)
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~eventbrite-luma-events/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "searches": [
    "AI"
  ],
  "locations": [
    "San Francisco, CA"
  ],
  "dateTo": "+30 days",
  "maxEventsPerSearch": 20,
  "maxEvents": 100
}
JSON
