# App Store Keyword Rank Tracker & App Store Top Charts - ASO

Apple App Store keyword rank tracker and top charts (free, paid, grossing, new) by country and category, plus Apple Podcasts charts and daily rank changes. Official Apple feeds, $0.50/1k rows.

- Apify Store: [https://apify.com/tidytools/app-store-top-charts](https://apify.com/tidytools/app-store-top-charts)
- Actor ID: `tidytools/app-store-top-charts` (`u2wdaOwzbQGmcNpXm`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/app-store-top-charts`

## Use case

**Input:** countries plus chart types and categories, or keywords plus the apps you track. **Output:** one row per chart entry, search result or tracked-app rank. **Price:** $0.50 per 1,000 chart entries or search results, $3 per 1,000 tracked-app ranks, no start fee; empty, failed and invalid items are free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Chart entry or search result | $0.50 |
| Tracked app keyword rank | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "mode": "charts",
  "countries": [
    "us",
    "gb"
  ],
  "chartTypes": [
    "topfree"
  ],
  "genres": [
    "all",
    "Productivity"
  ],
  "maxRank": 10,
  "keywords": [
    "habit tracker"
  ],
  "trackApps": [
    "https://apps.apple.com/us/app/habitkit/id6443918070"
  ],
  "resultsPerKeyword": 5
}
```

## Sample output

From the Actor's documentation (section "Output example: chart entry"):

```json
{
    "type": "chart-entry",
    "success": true,
    "input": "us Top Free",
    "media": "apps",
    "device": "iphone",
    "country": "us",
    "chart": "topfree",
    "chartTitle": "Top Free",
    "genreId": null,
    "genre": "All",
    "rank": 1,
    "appId": "6760173601",
    "bundleId": "com.facebook.hatch",
    "name": "Muse from Meta",
    "developer": "Meta Platforms, Inc.",
    "developerId": "284882218",
    "developerUrl": "https://apps.apple.com/us/developer/meta-platforms-inc/id284882218",
    "price": 0,
    "currency": "USD",
    "priceLabel": "Get",
    "category": "Productivity",
    "categoryId": "6007",
    "releaseDate": "2026-09-08T07:00:00.000Z",
    "url": "https://apps.apple.com/us/app/muse-from-meta/id6760173601",
    "iconUrl": "https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/73/72/9b/73729ba4-8f07-dabc-9e4c-07ee3d667630/HatchAppIconPublic-0-0-1x_U007ephone-0-1-0-sRGB-0-85-220.png/512x512bb.png",
    "averageRating": 4.87,
    "ratingCount": 107455,
    "version": "9.0",
    "currentVersionReleaseDate": "2026-09-26T18:41:05Z",
    "contentRating": "17+",
    "fileSizeMB": 130,
    "primaryGenre": "Productivity",
    "changeType": "new",
    "previousRank": null,
    "rankChange": null,
    "chartUpdatedAt": "2026-09-30T14:30:30.000Z",
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
