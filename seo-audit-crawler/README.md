# SEO Audit Tool - SEO Checker, Site Audit & Core Web Vitals

SEO crawler for technical SEO audits, JS sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional Core Web Vitals. $5/1k pages.

- Apify Store: [https://apify.com/tidytools/seo-audit-crawler](https://apify.com/tidytools/seo-audit-crawler)
- Actor ID: `tidytools/seo-audit-crawler` (`V1FNXB9GeyVft8LTH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/seo-audit-crawler`

## Use case

**For SEO agencies, consultants and site owners:** use this SEO Audit Tool, SEO Checker and Site Audit to crawl whole sites, compare your site with competitors side by side, and see what changed since the previous run.
**From $0.005 per audited page on Free/Bronze; failed pages are free.** Download the printable `REPORT_HTML` client report after the run (or save it as a PDF). Optional PageSpeed measurements have a separate charge.
**AI search readiness is included at the same page price:** each site's report now checks AI crawler rules in robots.txt, `/llms.txt`, JSON-LD coverage and answer-style headings, with a 0–100 signal score and up to five fixes. It does not promise that ChatGPT, Perplexity or Google AI will cite your site.
**Weekly monitoring, only regressions:** run a saved input from a weekly Apify Schedule with `compareWithPrevious: true`, `weeklyChangesDigest: true` and a fixed `monitorName`. Each run's `WEEKLY_CHANGES` record then lists only new issues, score drops and pages no longer found ([setup steps](#weekly-schedule-setup)). Audited pages are still billed at the page price; the comparison and digest add no charge.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Audited page | $5.00 |
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
