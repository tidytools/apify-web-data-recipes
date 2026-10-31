# YouTube Shorts Channel Scraper - Public Channel Shorts

Get the newest Shorts from public YouTube channel URLs or handles. Set tabs to shorts in API input. No login; up to 100 per channel page. Successful list rows use the engine's Video event ($1 per 1,000).

- Apify Store: [https://apify.com/tidytools/youtube-shorts-channel](https://apify.com/tidytools/youtube-shorts-channel)
- Actor ID: `tidytools/youtube-shorts-channel` (`hWPtsxLv7IiMJ7TnH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/youtube-shorts-channel`

## Use case

For each public channel, this Actor reads the visible Shorts tab and returns recent video rows with a Shorts URL, title, channel, and any view count and thumbnail YouTube exposes. Optional channel information and full video details use the shared YouTube Channel Scraper engine.

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
    "https://www.youtube.com/@mkbhd",
    "https://www.youtube.com/@veritasium",
    "https://www.youtube.com/@NASA"
  ],
  "tabs": [
    "shorts"
  ],
  "maxVideos": 10
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{"type":"video","contentType":"short","detailLevel":"list","videoId":"R6yNUnRXZ64","url":"https://www.youtube.com/shorts/R6yNUnRXZ64","title":"iPhone Duo is here","charged":true}
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
