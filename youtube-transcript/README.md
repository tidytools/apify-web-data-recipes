# YouTube Transcript Scraper - Timestamps, No API Key or Login

YouTube transcript API without a YouTube API key: transcripts with timestamps from videos, channels or playlists, manual or auto captions in any language, plus title, channel, views and date. Optional speech-to-text. Failed videos free. $3/1,000.

- Apify Store: [https://apify.com/tidytools/youtube-transcript](https://apify.com/tidytools/youtube-transcript)
- Actor ID: `tidytools/youtube-transcript` (`HquiZorfA0G2SsVDc`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/youtube-transcript`

## Use case

**YouTube Transcript Scraper is a YouTube transcript API that needs no YouTube API key: paste video, channel or playlist links and get the full transcript, timestamped segments and video details, one row per video, for $3 per 1,000 transcripts. Videos without a transcript and failed videos are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Video transcript | $3.00 |
| Speech-to-text minute | $8.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "videos": [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "success": true,
    "videoId": "jNQXAC9IVRw",
    "title": "Me at the zoo",
    "channel": "jawed",
    "durationSec": 19,
    "language": "en",
    "source": "manual_captions",
    "transcript": "All right, so here we are, in front of the elephants the cool thing about these guys is that they have really... really really long trunks and that's cool (baaaaaaaaaaahhh!!) and that's pretty much all there is to say",
    "segments": [
        { "start": 1.2, "duration": 2.16, "text": "All right, so here we are, in front of the elephants" }
    ],
    "wordCount": 39,
    "failureReason": null
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
