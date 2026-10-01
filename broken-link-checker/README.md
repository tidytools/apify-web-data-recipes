# Broken Link Checker - Find 404 & Dead Links on Any Website (available from 2026-10-05)

Crawl a website and find every broken link and image (404, 410, 5xx, dead domains, SSL errors) with the page and anchor text. Alerts on new broken links. $1/1k pages + $0.30/1k links.

- Apify Store: `apify.com/tidytools/broken-link-checker` (public from 2026-10-05)
- Actor ID: `tidytools/broken-link-checker` (`iU4sjuweSBNA1jq0f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/broken-link-checker`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-05**. Until then the recipes below return an error.

## Use case

**Broken link checker for any website**: it crawls your site, collects every link and image on every page and checks each one, so you get **every broken (404) and dead link with the pages where it appears and its anchor text**. Reasons include 404, 410, server errors, dead domains and expired SSL certificates, and a shareable **Markdown report** lists the fixes per page. **Monitoring mode** reports only links that broke since the last run.

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
