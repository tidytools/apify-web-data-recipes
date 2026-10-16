# Google Ads Transparency Scraper - Competitor Ads by Domain

Competitor ads from Google's Ads Transparency Center by advertiser or domain: text, image and video ads, first and last shown, countries, ad text. Monitor new ads. $1.50 per 1,000 ads, failed searches free.

- Apify Store: [https://apify.com/tidytools/ads-transparency](https://apify.com/tidytools/ads-transparency)
- Actor ID: `tidytools/ads-transparency` (`h2sgUDYx9j6G4FmKM`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ads-transparency`

## Use case

**Enter competitors (name, advertiser ID or link) and/or domains, get one row per Google ad: advertiser, format, first and last shown, days shown, image and a link to the ad. $1.50 per 1,000 ads.** Searches that fail or find nothing are free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Ad | $1.50 |
| Ad details | $2.00 |
| Ad text | $4.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "advertisers": [
    "Nike, Inc."
  ],
  "domains": [
    "notion.so"
  ],
  "region": "US",
  "maxAdsPerSearch": 20
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "zapier.com",
    "searchType": "domain",
    "region": "US",
    "advertiserId": "AR07656268315995668481",
    "advertiserName": "Zapier, Inc",
    "creativeId": "CR05925856452345331713",
    "format": "text",
    "firstShown": "2025-04-25T01:23:10.000Z",
    "lastShown": "2026-10-03T04:56:29.000Z",
    "daysShown": 468,
    "targetDomain": "zapier.com",
    "imageUrl": "https://tpc.googlesyndication.com/archive/simgad/16983613173943704328",
    "adUrl": "https://adstransparency.google.com/advertiser/AR07656268315995668481/creative/CR05925856452345331713?region=US",
    "variationCount": 1,
    "regionsShown": [
        { "country": "DE", "geoId": 2276, "lastShownDate": "2026-10-02" },
        { "country": "US", "geoId": 2840, "lastShownDate": "2026-10-02" },
        { "country": "GB", "geoId": 2826, "lastShownDate": "2026-10-02" }
    ],
    "countriesShown": ["DE", "IL", "CA", "US", "AU", "IT", "MX", "GB"],
    "chargedEvents": ["ad", "ad-details"],
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
