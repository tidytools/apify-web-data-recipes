# YouTube Channel Scraper - Videos, Shorts, Views & Likes (available from 2026-10-15)

Scrape YouTube channels, playlists and videos: subscribers, total views, join date, country, links, plus each video's views, likes, publish date, duration, tags and description. Videos, Shorts and live tabs. No login, no proxy needed. From $1 per 1,000 videos; failed items are free.

- Apify Store: `apify.com/tidytools/youtube-channel-scraper` (public from 2026-10-15)
- Actor ID: `tidytools/youtube-channel-scraper` (`tYsrX7KkSKgUHIemE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/youtube-channel-scraper`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-15**. Until then the recipes below return an error.

## Use case

It turns **YouTube channels, playlists and video links into clean rows**: channel statistics and the newest videos, Shorts and live streams of each channel, with views, likes, publish dates, durations, tags and descriptions.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Video | $1.00 |
| Video with full details | $2.00 |
| Channel info | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.youtube.com/@mkbhd"
  ],
  "maxVideos": 10
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "channel",
    "channelId": "UCBJycsmduvYEL83R_U4JriQ",
    "channelName": "Marques Brownlee",
    "handle": "@mkbhd",
    "handleUrl": "https://www.youtube.com/@mkbhd",
    "subscriberCount": 21300000,
    "subscriberCountText": "21.3M subscribers",
    "videoCount": 1856,
    "viewCount": 5730204755,
    "joinedDate": "2008-03-21",
    "country": "United States",
    "links": [{ "title": "Twitter", "url": "http://twitter.com/MKBHD" }, { "title": "Instagram", "url": "http://instagram.com/MKBHD" }],
    "isVerified": true,
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
