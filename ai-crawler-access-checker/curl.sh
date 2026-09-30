#!/usr/bin/env sh
# AI Crawler Access Checker - robots.txt for GPTBot, ClaudeBot: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/ai-crawler-access-checker
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~ai-crawler-access-checker/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "websites": [
    "https://www.nytimes.com",
    "python.org",
    "docs.anthropic.com"
  ]
}
JSON
