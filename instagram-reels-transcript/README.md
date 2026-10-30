# Instagram Reels Transcript - Video to Text and SRT/VTT

Public Instagram Reel speech to text. Private, login-only and speech-free reels are free. $0.006/min.

- Apify Store: [https://apify.com/tidytools/instagram-reels-transcript](https://apify.com/tidytools/instagram-reels-transcript)
- Actor ID: `tidytools/instagram-reels-transcript` (`ya3mYYl7XCfd93VZZ`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/instagram-reels-transcript`

## Use case

Paste an individual **public Instagram Reel URL** with speech. Each video yields one row with `text`, timed `segments`, `language` and `billedMinutes`. Optional subtitle links are `srtUrl` and `vttUrl`. Private or login-only videos return free failure rows. A Reel with Instagram library music and no speech returns a free `no_text` row. Successful transcription is **$0.006 per started audio minute** on Free/Bronze; the deployed engine price applies on other tiers.

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
  "urls": [
    "https://www.instagram.com/reel/C-YpOOwvJME/"
  ],
  "subtitleLanguages": []
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
  "url": "https://www.instagram.com/reel/C-YpOOwvJME/",
  "success": true,
  "charged": true,
  "language": "en",
  "durationSeconds": 25,
  "billedMinutes": 1,
  "text": "Example spoken words.",
  "segments": [
    {
      "start": 0,
      "end": 2.5,
      "text": "Example spoken words."
    }
  ]
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
