# Smart Fetch - URL to Markdown from US, Singapore, EU or Taiwan (available from 2026-10-11)

Fetch any public URL as clean Markdown, HTML and JSON metadata. Pick the region it is fetched from (US, Singapore, EU, Taiwan residential) or let Auto switch region when a site blocks. JavaScript rendering, robots.txt respected, failed pages free. From $1/1,000 pages.

- Apify Store: `apify.com/tidytools/smart-fetch` (public from 2026-10-11)
- Actor ID: `tidytools/smart-fetch` (`ZwrMww9WkNBFqS9gl`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/smart-fetch`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-11**. Until then the recipes below return an error.

## Use case

Give it URLs and get each page back as **clean Markdown**, optionally the **HTML**, and **JSON metadata** (title, description, language, canonical URL, content type, size, Last-Modified, ETag, X-Robots-Tag, links). PDF, Word and Excel files are converted to Markdown too.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Page (HTTP) | $1.00 |
| Page (browser) | $3.00 |
| Region fee | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.python.org/about/",
    "https://en.wikipedia.org/wiki/Web_scraping"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "https://www.python.org/about/",
    "url": "https://www.python.org/about/",
    "finalUrl": "https://www.python.org/about/",
    "success": true,
    "httpStatus": 200,
    "title": "About Python™ | Python.org",
    "description": "The official home of the Python Programming Language",
    "lang": "en",
    "markdown": "---\ndescription: The official home of the Python Programming Language\ntitle: Welcome to Python.org\n...",
    "markdownChars": 4815,
    "region": "cf",
    "regionLocation": "Cloudflare edge (nearest data center)",
    "mode": "browser",
    "metadata": { "title": "About Python™ | Python.org", "contentType": "text/html; charset=utf-8", "bytes": 51593, "lastModified": null, "etag": null, "xRobotsTag": null },
    "robots": "unavailable",
    "attempts": ["cf/http: blocked (HTTP 403)", "cf/browser: ok (HTTP 200)"],
    "chargedEvents": ["page-browser"],
    "priceUsd": 0.003,
    "charged": true,
    "userAgent": "Mozilla/5.0 (compatible; TidyToolsSmartFetch/1.0; +https://apify.com/tidytools/smart-fetch)"
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
