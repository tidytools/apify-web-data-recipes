#!/usr/bin/env sh
# Text to Speech - Bulk TTS to MP3, Subtitles, Articles & Texts: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/text-to-speech
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~text-to-speech/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "text": "Hello from TidyTools. This text was turned into speech in a few seconds. Paste an article, a script or a list of texts, and get one audio file for each."
}
JSON
