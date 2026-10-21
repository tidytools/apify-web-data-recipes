# Video Transcript - Direct Video Files to SRT

Transcribe spoken audio in direct MP4/MOV video files to text and timed SRT/VTT subtitles. Upload video or paste public file URLs. Free failed and silent files. Same engine and prices as Audio Transcription.

- Apify Store: [https://apify.com/tidytools/video-transcript-files](https://apify.com/tidytools/video-transcript-files)
- Actor ID: `tidytools/video-transcript-files` (`jH39RULgdW1imNiDZ`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/video-transcript-files`

## Use case

Turn spoken audio in a video file into a timestamped transcript and downloadable SRT/VTT subtitles. Paste direct MP4/MOV file links or upload video files in Apify Console. This Actor uses the same transcription engine and prices as [Audio Transcription](https://apify.com/tidytools/audio-transcriber); this form starts with video files instead of a podcast feed. It listens to the audio track; it does not read words displayed in video frames.

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
    "https://archive.org/download/gerald-ford-inaugural-address-august-9-1974-720p/Gerald%20Ford%20inaugural%20address_%20August%209%2C%201974%20%28720p%29.mp4"
  ],
  "podcastFeeds": []
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/video-transcript-files).

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
