# Broken Link Checker - Find 404 & Dead Links on Any Website (available from 2026-10-05)

Crawl a website and find every broken link and image (404, 410, 5xx, dead domains, SSL errors) with the page and anchor text. Internal and external links. $1/1k pages + $0.30/1k links.

- Apify Store: [https://apify.com/tidytools/broken-link-checker](https://apify.com/tidytools/broken-link-checker)
- Actor ID: `tidytools/broken-link-checker` (`iU4sjuweSBNA1jq0f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/broken-link-checker`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-05**. Until then the recipes below return an error.

## Use case

It **crawls your website, collects every link and image on every page and checks each one**. You get a list of broken links (404, 410, server errors, dead domains, expired SSL certificates…) together with **the pages where each link appears and its anchor text**, plus a shareable **Markdown report** with a fix list per page.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Crawled page | $1.00 |
| Checked link | $0.30 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.python.org/"
  ],
  "maxPages": 10,
  "maxLinksToCheck": 2000
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "http://www.ironport.com/",
    "site": "python.org",
    "startUrl": "https://www.python.org/",
    "status": 503,
    "statusClass": "server-error",
    "statusText": "Service Unavailable",
    "error": null,
    "finalUrl": "http://www.ironport.com/",
    "redirects": 0,
    "internal": false,
    "linkType": "link",
    "nofollow": false,
    "responseMs": 1771,
    "slow": false,
    "foundOnPages": 1,
    "firstFoundOn": "https://www.python.org/about/quotes/",
    "firstAnchorText": "IronPort Systems",
    "sources": [{ "page": "https://www.python.org/about/quotes/", "text": "IronPort Systems" }],
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
