# Audio Transcription - Speech to Text, Audio to Text, Whisper

Bulk audio transcription with Whisper: transcribe audio to text, video to text, speech to text, MP3 to text, YouTube video transcription, podcast RSS, Google Drive/Dropbox links. SRT/VTT subtitle generator, speaker diarization, TXT/Markdown, 90+ languages. $0.006/min.

- Apify Store: [https://apify.com/tidytools/audio-transcriber](https://apify.com/tidytools/audio-transcriber)
- Actor ID: `tidytools/audio-transcriber` (`3W2KtIbvHitDH8GCc`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/audio-transcriber`

## Use case

**Turn an audio file, video link or podcast RSS feed into searchable text with timestamps and downloadable SRT, VTT, TXT and Markdown files.**

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
  "maxEpisodesPerFeed": 1,
  "subtitleLanguages": []
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "success": true,
    "durationSeconds": 500.1,
    "billedMinutes": 9,
    "language": "en",
    "text": "Mr. Chief Justice, my dear friends, my fellow Americans, the oath that I have taken is the same oath that was taken by George Washington...",
    "segments": [
        { "start": 1.36, "end": 20.4, "text": "Mr. Chief Justice, my dear friends, my fellow Americans, the oath that I have taken ..." }
    ],
    "chapters": [{ "start": "0:00", "title": "Introduction and Compact with the Nation" }, { "start": "5:04", "title": "Message of Hope and Unity" }],
    "srtUrl": "https://api.apify.com/v2/key-value-stores/.../records/0000-Gerald-20Ford-...mp4.srt",
    "txtUrl": "https://api.apify.com/v2/key-value-stores/.../records/0000-Gerald-20Ford-...mp4.txt"
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
