# Google Trends Scraper - Interest, Regions, Trending Now

Google Trends data with retries for 429 errors: interest over time, interest by region, top and rising related queries for up to 5 compared terms, and Trending Now by country with search volume. CSV export, new-trend alerts. $2 per 1,000 term reports, no start fee.

- Apify Store: [https://apify.com/tidytools/google-trends-scraper](https://apify.com/tidytools/google-trends-scraper)
- Actor ID: `tidytools/google-trends-scraper` (`VFeRdMvjUYJ1Vubtj`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/google-trends-scraper`

## Use case

**Enter search terms (up to 5 per line to compare them), countries and a time range, and get Google's interest over time, interest by region and rising related queries as clean rows; or enter a country and get its Trending Now list. $2 per 1,000 term reports and $0.50 per 1,000 trending searches, with no start fee.** Searches without enough Google data and failed requests are free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Term report | $2.00 |
| Trending search | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "searchTerms": [
    "chatgpt, claude, gemini",
    "sourdough"
  ],
  "geo": "US",
  "trendingGeos": [
    "US"
  ],
  "maxTrendingPerGeo": 25
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "interest",
    "search": "sourdough",
    "terms": ["sourdough"],
    "keyword": "sourdough",
    "geo": "US",
    "timeRange": "today 12-m",
    "success": true,
    "interestOverTime": [
        { "date": "2026-09-20T00:00:00.000Z", "time": 1789862400, "formattedTime": "Sep 20 – 26, 2026", "values": { "sourdough": 60 } },
        { "date": "2026-09-27T00:00:00.000Z", "time": 1790467200, "formattedTime": "Sep 27 – Oct 3, 2026", "values": { "sourdough": 59 }, "partial": true }
    ],
    "averages": { "sourdough": 69 },
    "peak": { "sourdough": { "date": "2026-01-18T00:00:00.000Z", "value": 100 } },
    "latest": { "date": "2026-09-20T00:00:00.000Z", "values": { "sourdough": 60 } },
    "interestByRegion": [
        { "geoCode": "US-AK", "geoName": "Alaska", "values": { "sourdough": 100 } },
        { "geoCode": "US-WY", "geoName": "Wyoming", "values": { "sourdough": 90 } }
    ],
    "regionValues": "index (0-100, 100 = the region where the term is most popular)",
    "regionResolution": "REGION",
    "relatedQueries": {
        "sourdough": {
            "top": [ { "query": "sourdough bread", "value": 100 }, { "query": "sourdough starter", "value": 74 } ],
            "rising": [
                { "query": "costco authentic sourdough bread debate", "increasePercent": null, "breakout": true, "formattedValue": "Breakout" },
                { "query": "costco sourdough bread bowls", "increasePercent": 3950, "breakout": false, "formattedValue": "+3,950%" }
            ]
        }
    },
    "trendsUrl": "https://trends.google.com/trends/explore?q=sourdough&geo=US&date=today+12-m",
    "via": "direct",
    "charged": true
}
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
