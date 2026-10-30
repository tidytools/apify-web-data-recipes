# Subtitle Generator — Audio & Video to SRT/VTT in Any Language

Generate original and translated SRT/VTT subtitles from audio or video files in one run. Downloadable files and timed transcript; $0.006/audio minute plus $0.002/min per successful translation language. Failures free.

- Apify Store: [https://apify.com/tidytools/subtitle-generator](https://apify.com/tidytools/subtitle-generator)
- Actor ID: `tidytools/subtitle-generator` (`0aaZAeIHNM7VUJfvN`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/subtitle-generator`

## Use case

This Actor delivers original and requested translated subtitle files for each successful spoken recording. It uses the audio-transcriber engine; translations are separate per language.

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
    "https://upload.wikimedia.org/wikipedia/commons/d/d0/Fetesgalantes_06_verlaine.mp3"
  ],
  "subtitleLanguages": []
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/subtitle-generator).

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
