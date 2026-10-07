# Sitemap URL Extractor & Sitemap Scraper - All Website URLs

Get every URL of a website from its sitemaps: finds them via robots.txt, follows indexes and .gz files, returns lastmod, images and hreflang, optional status codes and changes. $0.50/1k URLs.

- Apify Store: [https://apify.com/tidytools/sitemap-url-extractor](https://apify.com/tidytools/sitemap-url-extractor)
- Actor ID: `tidytools/sitemap-url-extractor` (`FHYQa0BejmepV5Bwb`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/sitemap-url-extractor`

## Use case

Sitemap URL extractor and sitemap scraper: get all URLs of a website (lastmod, images, videos, hreflang) from robots.txt, sitemap indexes and .gz files, with optional HTTP status checks and change detection. $0.50 per 1,000 URLs on the Free plan, from $0.15 on Business and higher.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| URL | $0.50 |
| URL status check | $0.30 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://docs.apify.com"
  ],
  "maxUrls": 1000
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://docs.apify.com/api",
    "lastmod": null,
    "lastmodIso": null,
    "changefreq": "weekly",
    "priority": 0.5,
    "images": [],
    "imageDetails": [],
    "videos": [],
    "alternates": [],
    "sitemap": "https://docs.apify.com/sitemap_base.xml",
    "site": "https://docs.apify.com",
    "startUrl": "https://docs.apify.com",
    "input": "docs.apify.com",
    "lastmodSource": null,
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
