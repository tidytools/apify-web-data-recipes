#!/usr/bin/env sh
# ATS Jobs Scraper - Career Sites, Greenhouse, Lever, Workday: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/ats-career-site-jobs
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ats-career-site-jobs/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "companies": [
    "https://job-boards.greenhouse.io/airbnb",
    "jobs.lever.co/leverdemo",
    "https://apply.workable.com/huggingface/"
  ],
  "maxJobsPerCompany": 10
}
JSON
