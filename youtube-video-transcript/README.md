# YouTube Video Transcript - Bulk Captions with Timestamps

Paste public YouTube video URLs to get ready-made captions with text and start/end timestamps. Multiple videos per run; unavailable captions and blocked requests are free. $2 per 1,000 caption transcripts.

- Apify Store: [https://apify.com/tidytools/youtube-video-transcript](https://apify.com/tidytools/youtube-video-transcript)
- Actor ID: `tidytools/youtube-video-transcript` (`Y6rIqGsvIQFiWowKQ`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/youtube-video-transcript`

## Use case

**Paste public YouTube video URLs → get one transcript per video with `start` and `end` timestamps.** The default uses existing manual or auto-generated captions. Paste one link or a list; no YouTube API key is needed.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Video transcript | $2.00 |
| Speech-to-text minute | $6.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "videos": [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
    "https://www.youtube.com/watch?v=6CXgPVw_-0g",
    "https://www.youtube.com/watch?v=gpdHe3QZiiY"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
  "success": true,
  "videoUrl": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
  "title": "Me at the zoo",
  "language": "en",
  "text": "All right, so here we are ...",
  "segments": [{"start": 1.2, "end": 3.36, "text": "All right, so here we are, in front of the elephants"}],
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
