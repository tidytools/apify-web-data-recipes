# Real Estate Listing Extractor - Price, Beds, Area & Agent

Extract price, beds, area, address and agent from public real estate listing URLs or agency list pages. One row per property; one event per successful page.

- Apify Store: [https://apify.com/tidytools/real-estate-listing-extractor](https://apify.com/tidytools/real-estate-listing-extractor)
- Actor ID: `tidytools/real-estate-listing-extractor` (`uSR9AlcdoTy5fHTkp`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/real-estate-listing-extractor`

## Use case

Extract public estate agency listings into **one Dataset row per property**. Paste a single property URL or an agency list page; no platform-specific search or login is needed. The prefilled [Churcher Estates listing page](https://churcherestates.co.uk/listings/) is a public independent-agent example, not a guarantee of future access.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Extracted page | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://churcherestates.co.uk/listings/"
  ],
  "fields": {}
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/real-estate-listing-extractor).

## Run it

Set your Apify API token first (Apify Console > Settings > API & Integrations):

```bash
export APIFY_TOKEN=your_token      # PowerShell: $env:APIFY_TOKEN="your_token"
```

| Language | File | Command |
|---|---|---|
| Python | [`python/run.py`](python/run.py) | `pip install apify-client && python python/run.py` |
| JavaScript (Node.js 18+) | [`js/run.mjs`](js/run.mjs) | `npm install apify-client && node js/run.mjs` |
| curl | [`curl.sh`](curl.sh) | `sh curl.sh` |

Python and JavaScript save all rows to `results.json`. The curl recipe uses `run-sync-get-dataset-items`, which waits up to 300 seconds; use the Python or JavaScript client for longer runs.
Every recipe sets a cost cap (`maxTotalChargeUsd`, $1.00): the run stops charging at that amount. Change it for bigger inputs.
