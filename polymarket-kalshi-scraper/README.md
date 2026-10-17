# Polymarket & Kalshi Scraper - Prediction Market Odds API

Live odds from Kalshi and Polymarket in one clean format: YES probability, bid/ask, volume, liquidity, close date, rules. Search, categories (politics, weather, crypto...), links, order books, price history, odds-change alerts. $1 per 1,000 markets.

- Apify Store: [https://apify.com/tidytools/polymarket-kalshi-scraper](https://apify.com/tidytools/polymarket-kalshi-scraper)
- Actor ID: `tidytools/polymarket-kalshi-scraper` (`g6ydibLLuhffYJI2G`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/polymarket-kalshi-scraper`

## Use case

**Search keywords or categories, or paste market links, and get one row per Kalshi or Polymarket market in the same format (YES probability, bid/ask, volume, close time, rules, link), at $1 per 1,000 markets.** Optional price history is $1 per 1,000 and order books $0.50 per 1,000, charged only when the venue returned data. Markets your filters drop, unchanged markets in odds-alert mode, failed links and input mistakes are free. No start fee, no login.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Market | $1.00 |
| Price history | $1.00 |
| Order book | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "platforms": [
    "kalshi",
    "polymarket"
  ],
  "search": [
    "election"
  ],
  "maxMarkets": 20
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "platform": "kalshi",
    "marketId": "KXNCAAFGAME-26OCT03ALAMSST-MSST",
    "eventId": "KXNCAAFGAME-26OCT03ALAMSST",
    "seriesId": "KXNCAAFGAME",
    "eventTitle": "Alabama vs Mississippi St.",
    "question": "Mississippi St. wins",
    "outcome": "Yes — Mississippi St.",
    "yesProbability": 0.135,
    "yesProbabilityPercent": 13.5,
    "yesBid": 0.13, "yesAsk": 0.14, "noBid": 0.86, "noAsk": 0.87,
    "lastPrice": 0.14,
    "spread": 0.01,
    "oneDayPriceChange": -0.2,
    "volume": 4444545.9,
    "volume24h": 4191872.56,
    "volumeUnit": "contracts ($1 payout each)",
    "openInterest": 3000256.44,
    "closeTime": "2026-10-05T17:00:00.000Z",
    "status": "open",
    "category": "Sports",
    "tags": ["Football"],
    "resolutionSource": "Kalshi using information originating from the NCAA; ESPN",
    "url": "https://kalshi.com/markets/kxncaafgame/alabama-vs-mississippi-st/kxncaafgame-26oct03alamsst",
    "orderBook": { "yesBids": [{ "price": 0.13, "size": 314889.91 }], "yesAsks": [{ "price": 0.14, "size": 632293.76 }], "sizeUnit": "contracts" },
    "priceHistory": [{ "time": "2026-10-03T04:00:00.000Z", "probability": 0.34, "volume": 128564.05 }],
    "rank": 1,
    "success": true,
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
