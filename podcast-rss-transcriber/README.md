# Podcast Transcription - RSS Episodes to Text

Turn public podcast RSS episodes into text, TXT and optional SRT. Use publisher transcripts when available or transcribe audio by the minute. One newest episode per feed by default; failed inputs are free.

- Apify Store: [https://apify.com/tidytools/podcast-rss-transcriber](https://apify.com/tidytools/podcast-rss-transcriber)
- Actor ID: `tidytools/podcast-rss-transcriber` (`0Roc7SavHR3S8766I`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/podcast-rss-transcriber`

## Use case

Turn public podcast RSS episodes into searchable text and optional SRT subtitles. Paste one or more public RSS feed URLs into **Podcast RSS feeds**. The first-run form contains one NASA feed and selects the newest episode from each feed (`maxEpisodesPerFeed: 1`). Remove the example before entering your own feed.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Audio minute | $6.00 |
| Audio minute with speaker labels | $15.00 |
| AI summary and chapters | $10.00 |
| Translated subtitles (per minute and language) | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "podcastFeeds": [
    "https://www.nasa.gov/feeds/podcasts/small-steps-giant-leaps"
  ],
  "maxEpisodesPerFeed": 1,
  "urls": [],
  "subtitleLanguages": []
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/podcast-rss-transcriber).

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
