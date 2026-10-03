# Websites by Technology - BuiltWith Alternative & Store Leads (available from 2026-10-14)

Lists of websites that use a technology, by country: Shopify stores in Germany, WordPress sites in Taiwan, HubSpot users in the UK. Candidates come from Chrome's top 1K-1M websites per country; each home page is checked live. $5 per 1,000 websites found; scanning is free.

- Apify Store: `apify.com/tidytools/website-lists` (public from 2026-10-14)
- Actor ID: `tidytools/website-lists` (`V2bdPhQNV5k4k0CnM`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-lists`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-14**. Until then the recipes below return an error.

## Use case

It builds **lead lists of websites that use a technology, in the countries you choose**: "Shopify stores popular in Germany", "WordPress sites in Taiwan's top 10,000", "companies in the US top 10,000 that use HubSpot".

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Website found | $5.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "technologies": [
    "Shopify"
  ],
  "countries": [
    "US"
  ],
  "maxRank": 100000,
  "skipTopRank": 10000,
  "maxResults": 10,
  "maxSitesToScan": 300
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "domain": "ortlieb.com",
    "website": "https://de.ortlieb.com/",
    "title": "ORTLIEB | Built to Endure. Waterproof. Made in Germany",
    "description": "Die legendären ORTLIEB Fahrradtaschen, Rucksäcke und Reisetaschen. Nachhaltigkeit durch Haltbarkeit. 100% wasserdicht. Hergestellt in Deutschland.",
    "language": "de",
    "country": "DE",
    "countryName": "Germany",
    "countryRankBucket": 10000,
    "countryRankLabel": "Top 10K in Germany (Chrome)",
    "matchedTechnologies": ["Shopify"],
    "matchEvidence": {
        "Shopify": ["header: powered-by: Shopify", "cookie: _shopify_essential", "meta: shopify-digital-wallet: /85001568588/digital_wallets/dialog"]
    },
    "technologyCount": 11,
    "technologies": [
        { "name": "Shopify", "category": "E-commerce", "confidence": "high" },
        { "name": "Tailwind CSS", "category": "UI library", "confidence": "medium" },
        { "name": "Microsoft Clarity", "category": "Analytics", "confidence": "high" },
        { "name": "Cloudflare", "category": "CDN", "confidence": "high" },
        { "name": "Shop Pay", "category": "Payment", "confidence": "high" },
        { "name": "CookieFirst", "category": "Cookie consent", "confidence": "high" },
        { "name": "Judge.me", "category": "Reviews", "confidence": "high" },
        { "name": "Microsoft 365", "category": "Email hosting", "confidence": "high", "source": "dns" },
        { "name": "Hornetsecurity", "category": "Email security", "confidence": "high", "source": "dns" }
    ],
    "ecommerce": "Shopify",
    "emailProvider": "Microsoft 365",
    "emailSecurity": "Hornetsecurity",
    "via": "direct",
    "dataRelease": "crux-202608",
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
