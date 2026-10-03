# Website Traffic Rank Checker - Similarweb Alternative, Bulk (available from 2026-10-13)

Bulk website traffic rank from Chrome's real-user data: global Top 1K-1M rank, rank in each of 238 countries, top country and 12-month trend for any list of domains. No Similarweb login or proxies. $2 per 1,000 domains.

- Apify Store: `apify.com/tidytools/website-traffic-rank` (public from 2026-10-13)
- Actor ID: `tidytools/website-traffic-rank` (`QTlig3gBQedJW1HV4`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-traffic-rank`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-13**. Until then the recipes below return an error.

## Use case

Give it a list of domains (or URLs, or e-mail addresses). For each one it returns, in bulk and in seconds:

- its **global traffic rank**: Top 1K, 5K, 10K, 50K, 100K, 500K or 1M websites worldwide, measured by real Chrome users,
- its **rank in every country** where it is popular (238 countries), with the **top country** first,
- a **12-month history** of the global rank and a **6-month trend**: rising, falling, stable, new or dropped out,
- optional **rank in the countries you choose** (`rankIn.us`, `rankIn.de`...) for filtering a lead list by market.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Domain checked | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "apify.com",
    "notion.so",
    "shopify.com",
    "bbc.co.uk",
    "tools.yukai.uk"
  ],
  "countries": [
    "us",
    "gb"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "apify.com",
    "domain": "apify.com",
    "found": true,
    "globalRank": 100000,
    "globalRankLabel": "Top 100K websites worldwide",
    "trend": "up",
    "globalRankSixMonthsAgo": 500000,
    "monthsInGlobalTop1M": 12,
    "topCountry": "de",
    "topCountryName": "Germany",
    "topCountryRank": 50000,
    "topCountryRankLabel": "Top 50K in Germany",
    "countryCount": 135,
    "rankIn": { "us": 100000, "tw": 100000, "de": 50000 },
    "countryRanks": [
        { "country": "de", "countryName": "Germany", "rank": 50000, "rankLabel": "Top 50K" }
    ],
    "globalHistory": [
        { "month": "2025-09", "rank": 500000 },
        { "month": "2026-08", "rank": 100000 }
    ],
    "summary": "Top 100K worldwide; Top 50K in Germany; listed in 135 countries; 6-month trend: rising",
    "origin": "https://apify.com",
    "dataMonth": "2026-08",
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
