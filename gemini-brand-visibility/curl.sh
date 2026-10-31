#!/usr/bin/env sh
# Gemini Brand Visibility Tracker - Share of Voice & Citations: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/gemini-brand-visibility
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~gemini-brand-visibility/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "brand": "Linear",
  "domain": "linear.app",
  "competitors": [
    "Jira",
    "Asana",
    "ClickUp"
  ],
  "queries": [
    "What is the best issue tracker for a startup engineering team?",
    "Which project management tool do software teams switch to from Jira?",
    "What is a good bug tracking tool for a small SaaS company?"
  ]
}
JSON
