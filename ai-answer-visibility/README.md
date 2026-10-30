# AI Visibility Tracker - Gemini Brand Mentions & Citations

Ask live AI engines your buyer questions: brand mentions, mention order vs competitors and cited URLs, with a GEO fix plan link. Gemini is available; Perplexity needs its API key. $0.12 per successful query; failed queries free.

- Apify Store: [https://apify.com/tidytools/ai-answer-visibility](https://apify.com/tidytools/ai-answer-visibility)
- Actor ID: `tidytools/ai-answer-visibility` (`BedxKIqujmhiwJ4vg`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-answer-visibility`

## Use case

**Weekly tracking:** Reuse a monitor name in an Apify Schedule to compare AI answer mentions and mention order week by week. Monitoring uses the existing $0.12 per successful answer event; no extra event or price change.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Successful AI engine query | $120.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "brand": "Cloudflare",
  "domain": "cloudflare.com",
  "competitors": [
    "Akamai",
    "Fastly"
  ]
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/ai-answer-visibility).

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
