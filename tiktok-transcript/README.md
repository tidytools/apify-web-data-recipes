# TikTok Transcript - Video to Text with Timestamps

Transcribe public TikTok video speech to text with timestamped segments and optional SRT/VTT subtitles. One row per video; failed, private, silent and non-TikTok links are free. Audio billed by the minute.

- Apify Store: [https://apify.com/tidytools/tiktok-transcript](https://apify.com/tidytools/tiktok-transcript)
- Actor ID: `tidytools/tiktok-transcript` (`7zDKW9y46yJmstEJD`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/tiktok-transcript`

## Use case

Paste public TikTok video links and receive one dataset row per video with the spoken words, timed `segments`, detected `language`, and `billedMinutes`. SRT and VTT subtitles are saved when timing is available. The Actor transcribes the video's **original sound track**; it does not copy TikTok captions or use licensed music.

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
  "urls": [
    "https://www.tiktok.com/@nasa/video/7665075736742530317",
    "https://www.tiktok.com/@zachking/video/7652362186873916686"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
  "videoUrl": "https://www.tiktok.com/@nasa/video/7665075736742530317",
  "success": true,
  "charged": true,
  "language": "en",
  "billedMinutes": 1,
  "text": "Example spoken words.",
  "segments": [{ "start": 0, "end": 2.5, "text": "Example spoken words." }]
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
