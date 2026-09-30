# AI Web Scraper - Extract Structured Data to JSON by Prompt

List the fields or just describe what you want: AI reads each page and returns clean JSON. No selectors or code. One row per item on list pages, follows detail links. $0.01 per page.

- Apify Store: [https://apify.com/tidytools/ai-web-data-extractor](https://apify.com/tidytools/ai-web-data-extractor)
- Actor ID: `tidytools/ai-web-data-extractor` (`zuXZ7jgllbXStKb3f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-web-data-extractor`

## Use case

Give it **a list of URLs** and **the fields you want**, or simply **describe what you want in one sentence**. AI reads each page and returns **clean, structured JSON**: no CSS selectors, no XPath, no code, and it keeps working when the site's layout changes.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Extracted page | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://github.com/apify/crawlee"
  ],
  "fields": {
    "name": "string",
    "description": "string",
    "license": "string",
    "primary_language": "string"
  }
}
```

## Sample output

From the Actor's documentation (section "Input example: one row per page"):

```json
{
    "url": "https://github.com/apify/crawlee",
    "title": "GitHub - apify/crawlee: Crawlee—A web scraping and browser automation library...",
    "success": true,
    "data": {
        "name": "crawlee",
        "description": "Crawlee—A web scraping and browser automation library for Node.js to build reliable crawlers...",
        "license": "Apache License 2.0",
        "primary_language": "JavaScript"
    },
    "mode": "fast",
    "via": "backend",
    "contentTruncated": false
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
