# AI Web Scraper - Extract Structured Data & URL to JSON

AI scraper and AI extractor: list the fields or describe what you want, and an LLM reads each page and returns JSON. No selectors or code. One row per list item, follows detail links. $0.01/page.

- Apify Store: [https://apify.com/tidytools/ai-web-data-extractor](https://apify.com/tidytools/ai-web-data-extractor)
- Actor ID: `tidytools/ai-web-data-extractor` (`zuXZ7jgllbXStKb3f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-web-data-extractor`

## Use case

Set `followPagination: true` to extract the starting list page and follow its same-domain **Next** or next page-number links. It is off by default. `maxPages` includes the starting page: default **5**, maximum **50**, per starting URL. **Each successful page creates one `page-extracted` event**, even when one page produces many item rows. Pagination stops when the page has no next link; it does not guess a URL from `?page=N` alone. Repeated URLs and identical page content also stop the chain; failed and empty pages are free. This follows list pages, whereas `followLinks` reads a start page for free and extracts its linked detail pages.

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
    "in_stock": "boolean"
  }
}
```

## Sample output

From the Actor's documentation (section "Input example: one row per page"):

```json
{
    "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "success": true,
    "data": { "title": "A Light in the Attic", "price": 51.77, "in_stock": true },
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
