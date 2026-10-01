# Audio & Video to Text - Speech to Text Transcription, SRT

Whisper transcription: audio to text and video to text from files, Drive/Dropbox links and podcast RSS feeds, with timestamps and SRT/VTT subtitles. 90+ languages, optional speaker labels. $0.006/min.

- Apify Store: [https://apify.com/tidytools/audio-transcriber](https://apify.com/tidytools/audio-transcriber)
- Actor ID: `tidytools/audio-transcriber` (`3W2KtIbvHitDH8GCc`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/audio-transcriber`

## Use case

It turns **audio files, videos and podcast episodes** into **text with timestamps**, readable **paragraphs**, and ready-to-use **SRT and VTT subtitle files**. It uses OpenAI's open **Whisper large-v3-turbo** model, detects the language automatically and supports 90+ languages.

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
  "subtitleLanguages": []
}
```

## Sample output

From the Actor's documentation (section "Output example (real result, shortened)"):

```json
{
    "url": "https://archive.org/download/gerald-ford-inaugural-address-august-9-1974-720p/Gerald%20Ford%20inaugural%20address_%20August%209%2C%201974%20%28720p%29.mp4",
    "success": true,
    "format": "mp4",
    "fileSizeBytes": 48964530,
    "durationSeconds": 500.1,
    "billedMinutes": 9,
    "language": "en",
    "wordCount": 876,
    "text": "Mr. Chief Justice, my dear friends, my fellow Americans, the oath that I have taken is the same oath that was taken by George Washington...",
    "segments": [
        { "start": 1.36, "end": 20.4, "text": "Mr. Chief Justice, my dear friends, my fellow Americans, the oath that I have taken is the same oath that was taken by George Washington and by every president under the Constitution." },
        { "start": 20.4, "end": 31.32, "text": "But I assume the presidency under extraordinary circumstances never before experienced by Americans." }
    ],
    "paragraphs": [
        { "start": 1.36, "end": 39.68, "text": "Mr. Chief Justice, my dear friends, ... This is an hour of history that troubles our minds and hurts our hearts." },
        { "start": 41.44, "end": 73.64, "text": "Therefore, I feel it is my first duty to make an unprecedented compact with my countrymen. ..." }
    ],
    "summary": "The president assumes office under extraordinary circumstances ... and asks for prayers for Richard Nixon and his family.",
    "chapters": [
        { "startSeconds": 0, "start": "0:00", "title": "Introduction and Compact with the Nation" },
        { "startSeconds": 304, "start": "5:04", "title": "Message of Hope and Unity" }
    ],
    "srtUrl": "https://api.apify.com/v2/key-value-stores/.../records/0000-Gerald-20Ford-...mp4.srt",
    "vttUrl": "https://api.apify.com/v2/key-value-stores/.../records/0000-Gerald-20Ford-...mp4.vtt",
    "processingSeconds": 33
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
