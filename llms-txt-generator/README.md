# llms.txt Generator & Checker - llms-full.txt, AI SEO (GEO) (available from 2026-10-10)

Generate llms.txt and llms-full.txt for any website from its sitemap or a crawl, with sections and AI descriptions, or validate existing llms.txt files in bulk. $2 per 1,000 pages or sites.

- Apify Store: `apify.com/tidytools/llms-txt-generator` (public from 2026-10-10)
- Actor ID: `tidytools/llms-txt-generator` (`egcg4cyQFYEB7CfPM`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/llms-txt-generator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-10**. Until then the recipes below return an error.

## Use case

It creates an **llms.txt** file for any website, plus an optional **llms-full.txt**, so AI assistants and AI search engines can understand the site quickly. It can also **validate the llms.txt files that websites already publish**, in bulk. This is part of **GEO (Generative Engine Optimization)**: making your content easy for ChatGPT, Claude, Perplexity and other AI tools to find and cite.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Indexed page | $2.00 |
| Validated llms.txt | $2.00 |
| AI page description | $5.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "website": "https://docs.apify.com",
  "maxPages": 30
}
```

## Sample output

From the Actor's documentation (section "Generate an llms.txt"):

```json
{
    "type": "files",
    "title": "llms.txt (download)",
    "llmsTxtUrl": "https://api.apify.com/v2/key-value-stores/<store>/records/llms.txt",
    "llmsFullTxtUrl": "https://api.apify.com/v2/key-value-stores/<store>/records/llms-full.txt",
    "siteName": "Python",
    "summarySource": "input",
    "pageCount": 11,
    "source": "crawl"
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
