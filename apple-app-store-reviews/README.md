# Apple App Store Reviews Scraper - iOS App Reviews & Ratings

App Store scraper for iOS app reviews and app details from Apple's official public feeds, many countries. Star, date and keyword filters, new-review alerts, optional AI summary. $0.10/1,000 reviews.

- Apify Store: [https://apify.com/tidytools/apple-app-store-reviews](https://apify.com/tidytools/apple-app-store-reviews)
- Actor ID: `tidytools/apple-app-store-reviews` (`Z9MXLhY9FvkLVvdB2`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/apple-app-store-reviews`

## Use case

**App Store reviews scraper for $0.10 per 1,000 reviews: iPhone and iPad app reviews, ratings and app details from Apple's own public feeds, many countries in one run, no login or API key. Filtered-out reviews and apps that are not found are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Review | $0.10 |
| App details | $1.00 |
| AI insights | $20.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "apps": [
    "https://apps.apple.com/us/app/notion-notes-tasks-ai/id1232780281",
    "com.spotify.client"
  ],
  "countries": [
    "us",
    "gb"
  ],
  "maxReviewsPerCountry": 20
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "type": "review",
    "appId": "324684580",
    "appName": "Spotify: Music and Podcasts",
    "country": "us",
    "rating": 1,
    "title": "Hate the update",
    "text": "Hate it thanks.",
    "version": "9.1.86",
    "author": "Poleryeno",
    "date": "2026-09-28T13:07:21.000Z",
    "helpfulVotes": 0,
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
