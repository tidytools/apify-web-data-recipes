# Text to Speech - Bulk TTS to MP3, Subtitles, Articles & Texts

Turn texts and article URLs into natural speech: one MP3 (or Opus, WAV) file per text with optional SRT/VTT subtitles, in English, Spanish, French, Chinese, Japanese or Korean. $0.008 per 1,000 characters; empty and failed items are free; no start fee.

- Apify Store: [https://apify.com/tidytools/text-to-speech](https://apify.com/tidytools/text-to-speech)
- Actor ID: `tidytools/text-to-speech` (`7z3qAZcuvDMYZN34E`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/text-to-speech`

## Use case

One text (the "Text" field), as MP3 with subtitles:

A list of texts, each with an optional `id` (names the file and the row) and `language`:

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| 1,000 characters spoken | $8.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "text": "Hello from TidyTools. This text was turned into speech in a few seconds. Paste an article, a script or a list of texts, and get one audio file for each."
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{"index":0,"input":"text","source":"text","success":true,"language":"en","chars":72,"durationSec":4.25,
 "audioUrl":"https://api.apify.com/v2/key-value-stores/<store>/records/audio-001-Hello-from-TidyTools-This-text-was-turn.mp3",
 "fileKey":"audio-001-Hello-from-TidyTools-This-text-was-turn.mp3","format":"mp3","sampleRate":44100,"bitrateKbps":64,"bytes":34272,
 "srtUrl":"https://api.apify.com/v2/key-value-stores/<store>/records/audio-001-Hello-from-TidyTools-This-text-was-turn.srt",
 "vttUrl":"https://api.apify.com/v2/key-value-stores/<store>/records/audio-001-Hello-from-TidyTools-This-text-was-turn.vtt","cueCount":2,
 "truncated":false,"textPreview":"Hello from TidyTools. This text was turned into speech in a few seconds.","synthesisSec":2,"charged":true,"chargedUnits":1}
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
