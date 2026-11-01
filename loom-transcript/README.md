# Loom Transcript - Video to Text and SRT/VTT

Public Loom video speech to text. Private and failed videos are free. $0.006/min.

- Apify Store: [https://apify.com/tidytools/loom-transcript](https://apify.com/tidytools/loom-transcript)
- Actor ID: `tidytools/loom-transcript` (`98F7akXlfKH04kr3F`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/loom-transcript`

## Use case

Paste an individual **public Loom video URL** with speech. Each video yields one row with `text`, timed `segments`, `language` and `billedMinutes`. Optional subtitle links are `srtUrl` and `vttUrl`. Private or login-only videos return free failure rows. A Loom video with no speech returns a free `no_text` row. Successful transcription is **$0.006 per started audio minute** on Free/Bronze; the deployed engine price applies on other tiers.

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
    "https://www.loom.com/share/9e09ad3f4ad2449f977af2cbf5d64acf"
  ],
  "subtitleLanguages": []
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
  "url": "https://www.loom.com/share/9e09ad3f4ad2449f977af2cbf5d64acf",
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
