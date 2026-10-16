#!/usr/bin/env sh
# Answer Engine Optimization & GEO Audit - ChatGPT Fix Plan: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/geo-readiness-audit
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~geo-readiness-audit/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "websites": [
    "https://plausible.io"
  ],
  "targetQuestions": [
    "how much does plausible analytics cost",
    "is plausible analytics gdpr compliant"
  ],
  "competitorPages": [
    "how much does plausible analytics cost | https://usefathom.com/pricing"
  ]
}
JSON
