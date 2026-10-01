# SEO Audit Tool - SEO Checker, Site Audit & Core Web Vitals

SEO crawler for technical SEO audits, JS sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional Core Web Vitals. $5/1k pages.

- Apify Store: [https://apify.com/tidytools/seo-audit-crawler](https://apify.com/tidytools/seo-audit-crawler)
- Actor ID: `tidytools/seo-audit-crawler` (`V1FNXB9GeyVft8LTH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/seo-audit-crawler`

## Use case

SEO audit tool that crawls your website and checks **every page for on-page and technical SEO problems**, including **sites built with JavaScript or protected against bots**: when a site blocks plain requests, the page is fetched from a second network or audited in a real browser automatically, and a page that loads almost empty until JavaScript runs (a client-rendered app shell) is rendered in a real browser too. Each page gets a **score from 0 to 100**, **category scores** and a list of issues with **a fix hint for every issue**. The whole site gets a **report**: score distribution, most common problems, crawl coverage (indexable / noindex / canonicalized / 4xx / 5xx), sitemap checks, canonical and redirect problems, duplicate titles, H1s and content, and broken internal pages.

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

From the Actor's documentation (section "Output: one item per page"):

```json
{
    "url": "https://www.python.org/",
    "site": "python.org",
    "startUrl": "https://www.python.org/",
    "input": "https://www.python.org/",
    "success": true,
    "mode": "fast",
    "via": "direct",
    "score": 93,
    "issueCount": 2,
    "issueCodes": "h1-multiple, canonical-missing",
    "issues": [
        { "id": "h1-multiple", "severity": "warning", "message": "Page has 5 H1 headings.", "category": "headings",
          "fixHint": "Keep a single main H1 and turn the others into H2 headings.", "impact": "medium" },
        { "id": "canonical-missing", "severity": "notice", "message": "Canonical link is missing.", "category": "indexing",
          "fixHint": "Add <link rel=\"canonical\"> pointing to the preferred URL of this page (usually itself).", "impact": "low" }
    ],
    "categoryScores": { "technical": 100, "indexing": 94, "meta": 100, "headings": 85, "images": 100, "social": 100, "...": 100 },
    "httpStatus": 200,
    "title": "Welcome to Python.org",
    "titleLength": 21,
    "metaDescriptionLength": 52,
    "h1": ["Intuitive Interpretation", "Compound Data Types", "..."],
    "headings": [{ "level": 1, "text": "Intuitive Interpretation" }, "..."],
    "canonical": null,
    "xRobotsTag": null,
    "blockedByRobotsTxt": false,
    "viewport": true,
    "wordCount": 1182,
    "contentHash": "9f824c550ac6dbe88bd0688e",
    "bytes": 53229,
    "imagesMissingAlt": 0,
    "nofollowLinks": 0,
    "hreflangLinks": [],
    "twitterCard": null,
    "structuredDataTypes": ["WebSite"]
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
