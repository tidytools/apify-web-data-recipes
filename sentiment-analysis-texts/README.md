# Review Sentiment Analysis - Reviews, Posts & Support Texts

Review sentiment analysis for your own reviews, social posts and support messages: each text gets positive, neutral, negative or mixed, plus confidence and a one-line reason. Paste texts or pass a Dataset. $4 per 1,000 texts; blank rows free.

- Apify Store: [https://apify.com/tidytools/sentiment-analysis-texts](https://apify.com/tidytools/sentiment-analysis-texts)
- Actor ID: `tidytools/sentiment-analysis-texts` (`pMAh6tLHjjlwnCz8o`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/sentiment-analysis-texts`

## Use case

Paste your own product reviews, social posts or support messages. This variant uses the AI page classifier with **Sentiment** selected by default, returning one Dataset row per text with a `label` of `positive`, `neutral`, `negative` or `mixed`, plus a short `reason` and `confidence`. The three example reviews are ready to run without changing a field. You can also classify public page URLs or text from another Actor's dataset.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Classified page | $4.00 |
| Classified page (quick) | $3.00 |
| Classified page (deep) | $8.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "texts": [
    "Great product, arrived early.",
    "Terrible support, never again.",
    "Good price but the box was damaged."
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"source":"text-0","textPreview":"Great product, arrived early.","label":"positive","confidence":"high","reason":"Praises the product and early delivery.","language":"en","taxonomy":"sentiment","analysisDepth":"standard","charged":true}
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
