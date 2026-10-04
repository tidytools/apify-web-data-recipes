# SEO Audit Tool - SEO Checker, Site Audit & Core Web Vitals

SEO crawler for technical SEO audits, JS sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional Core Web Vitals. $8/1k pages.

- Apify Store: [https://apify.com/tidytools/seo-audit-crawler](https://apify.com/tidytools/seo-audit-crawler)
- Actor ID: `tidytools/seo-audit-crawler` (`V1FNXB9GeyVft8LTH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/seo-audit-crawler`

## Use case

**SEO audit tool for $8 per 1,000 pages: it crawls your site, scores every page from 0 to 100 and lists each on-page and technical SEO issue with a fix hint, plus a site report (sitemap, canonicals, duplicates, broken pages). Broken, blocked and failed pages are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Audited page | $8.00 |
| PageSpeed measurement | $5.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.python.org/",
    "books.toscrape.com"
  ],
  "maxPages": 20
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "url": "https://www.python.org/",
    "success": true,
    "score": 93,
    "issueCount": 2,
    "issues": [
        { "id": "h1-multiple", "severity": "warning", "message": "Page has 5 H1 headings.", "category": "headings",
          "fixHint": "Keep a single main H1 and turn the others into H2 headings.", "impact": "medium" },
        { "id": "canonical-missing", "severity": "notice", "message": "Canonical link is missing.", "category": "indexing",
          "fixHint": "Add <link rel=\"canonical\"> pointing to the preferred URL of this page (usually itself).", "impact": "low" }
    ],
    "categoryScores": { "technical": 100, "indexing": 94, "meta": 100, "headings": 85, "images": 100, "social": 100, "...": 100 },
    "title": "Welcome to Python.org",
    "wordCount": 1182
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
