# Facebook Ad Library Scraper - Competitor Ads by Keyword or Page

Find Facebook and Instagram ads by keyword or Facebook Page. Export Library ID, advertiser, start date, platforms, copy, CTA, creative links and landing URL. Failed searches are free.

- Apify Store: [https://apify.com/tidytools/facebook-ads-library-scraper](https://apify.com/tidytools/facebook-ads-library-scraper)
- Actor ID: `tidytools/facebook-ads-library-scraper` (`8kv78HtHXhbcyibyK`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/facebook-ads-library-scraper`

## Use case

Search Meta's public Ad Library by keyword, Facebook Page URL or numeric Page ID and export one row per ad. The browser is rendered through the TidyTools Chrome pool with WARP egress requested. No Meta login is used. This Actor is a draft and has not been published.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Ad | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "searchTerms": [
    "nike"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"input":"nike","searchType":"keyword","country":"US","libraryId":"100000000000000","advertiserName":"Nike","pageUrl":"https://www.facebook.com/Nike/","startedAt":"2026-10-01","active":true,"platforms":["Facebook","Instagram"],"adText":"Find your next run","linkUrl":"https://www.nike.com/running","cta":"Shop now","imageUrls":["https://cdn.example.com/ad.jpg"],"videoUrls":[],"variationCount":1,"adUrl":"https://www.facebook.com/ads/library/?id=100000000000000","success":true,"errorType":null,"charged":true,"chargedEvents":["ad"],"scrapedAt":"2026-10-20T00:00:00.000Z"}
```

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
