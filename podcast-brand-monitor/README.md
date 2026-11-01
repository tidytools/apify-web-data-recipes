# Podcast Brand Mention Monitor - RSS Keyword Tracking

Find brand mentions in new public podcast episodes from RSS feeds. Export timestamped matches and a CSV. Publisher transcripts use no ASR minutes; failed files are free.

- Apify Store: [https://apify.com/tidytools/podcast-brand-monitor](https://apify.com/tidytools/podcast-brand-monitor)
- Actor ID: `tidytools/podcast-brand-monitor` (`zwM1vhc1aYqXpYQ4U`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/podcast-brand-monitor`

## Use case

Track names, brands and topics mentioned in public podcast RSS episodes. Enter feeds and search terms, then inspect the matching sentence and timestamp when the source has timing. The Actor uses the existing audio-transcriber engine and its pricing; this variant makes monitoring the first-run workflow. The form includes a public NASA RSS feed and `Apify` as examples. Replace them with your own feed and terms.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Audio minute | $6.00 |
| Audio minute with speaker labels | $15.00 |
| AI summary and chapters | $10.00 |
| Podcast content pack | $100.00 |
| Translated subtitles (per minute and language) | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "contentPackSubtitleLanguages": [],
  "podcastFeeds": [
    "https://www.nasa.gov/feeds/podcasts/small-steps-giant-leaps"
  ],
  "searchTerms": [
    "Apify"
  ],
  "monitorName": "my-brand-monitor",
  "urls": [],
  "maxEpisodesPerFeed": 1,
  "subtitleLanguages": []
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/podcast-brand-monitor).

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
