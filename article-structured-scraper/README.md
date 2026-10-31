# Article Scraper - Structured Article Fields from URLs

Extract headline, byline, publication date and article text from public article URLs into one structured JSON row per page. Missing fields are null; failed pages are free.

- Apify Store: [https://apify.com/tidytools/article-structured-scraper](https://apify.com/tidytools/article-structured-scraper)
- Actor ID: `tidytools/article-structured-scraper` (`1qVnNsxc2JI2ZL3WN`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/article-structured-scraper`

## Use case

Paste publicly readable article URLs and get one JSON Dataset row per page. The default `data` object asks for `headline`, `byline`, `datePublished`, and `articleText`. Article editors and data teams can export the rows or use the Dataset API. This Actor uses the AI Web Data Extractor engine; it is a URL list to article fields, not news search or a whole-site Markdown crawler.

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
    "https://en.wikipedia.org/wiki/Cloudflare"
  ],
  "fields": {
    "headline": "string",
    "byline": "string",
    "datePublished": "string",
    "articleText": "string"
  }
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
  "url": "https://example.org/public-article",
  "title": "Example article",
  "data": {
    "headline": "Example article",
    "byline": null,
    "datePublished": null,
    "articleText": "The article body found on the page."
  },
  "success": true,
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
