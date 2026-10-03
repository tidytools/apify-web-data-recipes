# Regional Price Checker - Geo Pricing from US, SG, UK, TW (available from 2026-10-11)

See the price, currency, country site and language a page shows in the US, Singapore, London and Taiwan, side by side. Extracts prices (text, JSON-LD, meta tags), flags geo blocks and cookie walls, monitors changes. Failed regions free.

- Apify Store: `apify.com/tidytools/regional-price-check` (public from 2026-10-11)
- Actor ID: `tidytools/regional-price-check` (`NQ3LNyHkvKKUAjQCt`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/regional-price-check`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-11**. Until then the recipes below return an error.

## Use case

Give it pricing, product or store pages. It opens each page **from four fixed places at the same time** and shows you, side by side, what a visitor there gets:

- the **price and currency** (from the page text, JSON-LD offers and price meta tags),
- the **country site** it was redirected to (`spotify.com/uk`, `kayak.sg`, `zendesk.tw`) and the HTTP status,
- the **language** of the page,
- **blocks and walls**: "not available in your region", cookie-consent walls, "choose your country" pickers, 404s,
- a **comparison**: does the page differ by region (`differs: true`), what differs (currency, price, redirect, language, availability, consent wall, page text), a price table converted to one currency, and a text-similarity score.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Region checked | $4.00 |
| Region checked (browser) | $6.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.spotify.com/premium/",
    "https://www.zendesk.com/pricing/"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://www.spotify.com/premium/",
    "differs": true,
    "differences": ["currency", "price", "redirect", "language", "content"],
    "summary": "Currency differs (US USD, Singapore SGD, London GBP, Taiwan TWD); prices differ (first price: US $12.99, Singapore $11.98, London £12.99, Taiwan $168); different country site (US www.spotify.com/us, Singapore www.spotify.com/sg-en, London www.spotify.com/uk, Taiwan www.spotify.com/tw); language differs (US en-us, Singapore en-sg, London en-gb, Taiwan zh-hant); text differs (lowest similarity 0 between US and Taiwan).",
    "pricesSummary": "US: $12.99 | Singapore: $11.98 | London: £12.99 | Taiwan: $168",
    "currencies": "USD, SGD, GBP, TWD",
    "regionsDelivered": 4,
    "priceTable": [
        {
            "position": 1,
            "us": { "amount": 12.99, "currency": "USD", "display": "$12.99", "period": "month", "inUSD": 12.99 },
            "sg": { "amount": 11.98, "currency": "SGD", "display": "$11.98", "period": "month", "inUSD": 9.36 },
            "eu": { "amount": 12.99, "currency": "GBP", "display": "£12.99", "period": "month", "inUSD": 17.16 },
            "tw": { "amount": 168, "currency": "TWD", "display": "$168", "period": "month", "inUSD": 5.25 }
        }
    ],
    "regions": {
        "tw": {
            "region": "tw",
            "location": "Taiwan (residential line)",
            "success": true,
            "status": "ok",
            "httpStatus": 200,
            "finalUrl": "https://www.spotify.com/tw/premium/",
            "locale": "www.spotify.com/tw",
            "title": "Spotify Premium - Spotify (台灣)",
            "language": "zh-hant",
            "currency": "TWD",
            "currencySource": "text",
            "mainPrice": { "amount": 168, "currency": "TWD", "display": "$168", "period": "month", "source": "text" },
            "renderedWith": "http",
            "elapsedMs": 2140,
            "charged": true
        }
    },
    "fx": { "base": "USD", "date": "Fri, 02 Oct 2026 00:02:31 +0000", "source": "ExchangeRate-API open access (open.er-api.com), daily rates" },
    "chargedEvents": { "region-checked": 4 },
    "priceUsd": 0.016
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
