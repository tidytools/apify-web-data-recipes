# Bulk URL Status Checker - HTTP Status & Redirect Checker (available from 2026-10-03)

Check thousands of URLs, a sitemap or a CSV for HTTP status codes, redirect chains, 404s, DNS and SSL errors. Verify a redirect map for site migrations, track changes. $1 per 1,000 URLs.

- Apify Store: `apify.com/tidytools/bulk-url-status-checker` (public from 2026-10-03)
- Actor ID: `tidytools/bulk-url-status-checker` (`ZOWuVMgMJNRNJnmyb`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/bulk-url-status-checker`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-03**. Until then the recipes below return an error.

## Use case

Paste a list of URLs (or upload a file, or give a sitemap) and get, for each one, the **HTTP status code, the full redirect chain, the final URL** and the reason when a link fails (404, server error, DNS error, expired SSL certificate, timeout, and so on). For site migrations, give a **redirect map** of old → expected new URLs and see which redirects are wrong.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Checked URL | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "http://python.org",
    "https://github.com/apify/crawlee",
    "https://example.com/this-page-does-not-exist",
    "https://expired.badssl.com/"
  ],
  "includeHtmlSignals": true
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "http://python.org",
    "finalUrl": "https://www.python.org/",
    "status": 200,
    "statusClass": "ok",
    "redirects": 1,
    "statusText": "OK",
    "redirectChain": [
        { "url": "http://python.org", "status": 301, "location": "https://www.python.org/" },
        { "url": "https://www.python.org/", "status": 200 }
    ],
    "httpsUpgrade": true,
    "contentType": "text/html; charset=utf-8",
    "contentLength": 11774,
    "server": "nginx",
    "xRobotsTag": null,
    "responseMs": 341,
    "error": null
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
