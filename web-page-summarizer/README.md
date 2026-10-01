# Article Summarizer & Text Summarizer - Summarize Web Pages (available from 2026-10-07)

AI summarizer for URLs, articles or your own text: TL;DR, bullets or executive summary, plus key points, topics, sentiment and keywords. Any language, JavaScript sites. No API key. $6/1,000.

- Apify Store: `apify.com/tidytools/web-page-summarizer` (public from 2026-10-07)
- Actor ID: `tidytools/web-page-summarizer` (`UK839QHsFspWRaI7d`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/web-page-summarizer`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-07**. Until then the recipes below return an error.

## Use case

Give it URLs or your own texts and get a **clear, factual summary of each one**: one line, a paragraph, bullet points, a TL;DR or an executive summary, in the language you choose. Optionally get **key points, topic tags, sentiment and keywords** in the same call, at no extra cost. Works on articles, blogs, documentation, product and company pages, and JavaScript-heavy sites. No API key needed.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Summarized page | $6.00 |
| Summarized long page (deep) | $12.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urlsText": "https://en.wikipedia.org/wiki/Cloudflare"
}
```

## Sample output

From the Actor's documentation (section "Output example (real result for the text above)"):

```json
{
    "source": "text-0",
    "success": true,
    "summary": "The X200 headphones have both positive and negative aspects.\n- The noise cancelling is excellent.\n- The battery lasts 30 hours.\n- The ear cushions get hot after an hour.\n- The app had connectivity issues on Android phones, but support provided a fix.",
    "keyPoints": ["The X200 headphones have excellent noise cancelling.", "The battery lasts 30 hours.", "The ear cushions get hot after an hour.", "The app keeps disconnecting on Android phones.", "Support replied within a day with a firmware fix."],
    "topics": ["headphones", "noise cancelling", "battery life"],
    "sentiment": "mixed",
    "keywords": ["X200 headphones", "noise cancelling", "battery", "ear cushions", "app", "Android", "firmware fix", "support"],
    "style": "executive",
    "sourceCharacters": 302,
    "analysisDepth": "standard"
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
