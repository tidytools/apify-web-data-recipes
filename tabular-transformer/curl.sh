#!/usr/bin/env sh
# CSV to JSON & JSON to CSV Converter - Batch, JSON Lines: run the Actor, wait for it (up to 300 s) and print the dataset items as JSON.
# Store page: https://apify.com/tidytools/tabular-transformer
# Usage: export APIFY_TOKEN=your_token && sh curl.sh
# maxTotalChargeUsd is a cost cap: the run stops charging at this amount.
: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"

curl -sS -X POST "https://api.apify.com/v2/acts/tidytools~tabular-transformer/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "files": [
    {
      "name": "example.csv",
      "dataText": "color,shape,flag,k,index,quantity,rate\nyellow,triangle,true,1,11,43.6498,9.8870\nred,square,true,2,15,79.2778,0.0130\n"
    }
  ]
}
JSON
