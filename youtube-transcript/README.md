# YouTube Transcript Scraper - Timestamps, No API Key or Login

YouTube transcript API without a YouTube API key: transcripts with timestamps from videos, channels or playlists, manual or auto captions in any language, plus title, channel, views and date. Optional speech-to-text. Failed videos free. $2/1,000.

- Apify Store: [https://apify.com/tidytools/youtube-transcript](https://apify.com/tidytools/youtube-transcript)
- Actor ID: `tidytools/youtube-transcript` (`HquiZorfA0G2SsVDc`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/youtube-transcript`

## Use case

- **$2 per 1,000 caption transcripts** (FREE/BRONZE rate; speech-to-text for videos without captions is billed per audio minute), no start fee; failed and no-caption videos are free.
- **No YouTube API key, cookies or login**: paste video, channel or playlist links.
- **Every failure says why** (`failureReason`), and each result says which language and caption type (`source`) you got.
- Timestamps on by default (`segments`), Markdown video notes, RAG chunks that link to the second in the video and a channel digest, all at no extra charge.
- **Optional simple output:** set `compactTranscript: true` for `videoUrl` and caption segments with `start`, `end`, `text`; the default output still uses `url` and `start`, `duration`, `text`.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Video transcript | $2.00 |
| Speech-to-text minute | $6.00 |

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

From the Actor's documentation (section "Output example"):

```json
{
  "success": true,
  "status": "ok",
  "videoId": "jNQXAC9IVRw",
  "url": "https://www.youtube.com/watch?v=jNQXAC9IVRw",
  "title": "Me at the zoo",
  "channel": "jawed",
  "channelId": "UC4QobU6STFB0P71PMvOGN5A",
  "publishDate": "2005-04-23T20:31:52-07:00",
  "durationSec": 19,
  "viewCount": 439408167,
  "requestedLanguages": [],
  "language": "en",
  "languageMatch": null,
  "source": "manual_captions",
  "isGenerated": false,
  "availableLanguages": [{ "code": "en", "name": "English", "generated": false }, { "code": "de", "name": "German", "generated": false }],
  "transcript": "All right, so here we are, in front of the elephants the cool thing about these guys is that they have really... really really long trunks and that's cool (baaaaaaaaaaahhh!!) and that's pretty much all there is to say",
  "segments": [
    { "start": 1.2, "duration": 2.16, "text": "All right, so here we are, in front of the elephants" },
    { "start": 5.318, "duration": 2.656, "text": "the cool thing about these guys is that they have really..." }
  ],
  "wordCount": 39,
  "charCount": 217,
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
