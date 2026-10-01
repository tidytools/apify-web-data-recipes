# AI Web Scraper - Extract Structured Data & URL to JSON

AI scraper and AI extractor: list the fields or describe what you want, and an LLM reads each page and returns JSON. No selectors or code. One row per list item, follows detail links. $0.01/page.

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
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  ],
  "fields": {
    "title": "string",
    "price": "number",
    "in_stock": "boolean",
    "stock_count": "integer",
    "upc": "string"
  }
}
```

## Sample output

From the Actor's documentation (section "Input example: one row per page"):

```json
{
    "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "success": true,
    "data": { "title": "A Light in the Attic", "price": 51.77, "in_stock": true, "stock_count": 22, "upc": "a897fe39b1053632" },
    "completeness": 1,
    "charged": true
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
