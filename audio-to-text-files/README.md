# Audio to Text: Uploaded & Direct Audio Files

Convert audio files to text: paste direct MP3, WAV, M4A, OGG or FLAC links or upload recordings, and get each transcript as text plus TXT and Markdown files. Whisper, 90+ languages, $0.006 per audio minute. Failed or silent files are free.

- Apify Store: [https://apify.com/tidytools/audio-to-text-files](https://apify.com/tidytools/audio-to-text-files)
- Actor ID: `tidytools/audio-to-text-files` (`40YN2yrWrfachO2vE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/audio-to-text-files`

## Use case

**Paste links to your audio files or upload recordings, and get each one back as a text transcript with timestamps plus a TXT and a Markdown file, for $0.006 per audio minute (Whisper, 90+ languages). Failed or silent files are free.**

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
    "https://webcapture-api.yukailin.workers.dev/samples/speech-sample.wav"
  ],
  "subtitleLanguages": [],
  "podcastFeeds": [],
  "maxEpisodesPerFeed": 1
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/audio-to-text-files).

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
