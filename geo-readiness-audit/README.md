# Answer Engine Optimization & GEO Audit - ChatGPT Fix Plan

AEO with a fix plan, not just a score: for each buyer question, see which page ChatGPT, Perplexity or Google AI Overviews would quote, why competitors win, and what to add. Plus a GEO audit of AI crawler access and firewalls. $0.01/question, $0.03/site.

- Apify Store: [https://apify.com/tidytools/geo-readiness-audit](https://apify.com/tidytools/geo-readiness-audit)
- Actor ID: `tidytools/geo-readiness-audit` (`mcmwUZfsZ9rTlgMqr`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/geo-readiness-audit`

## Use case

**It tells you why ChatGPT, Perplexity and Google AI Overviews quote your competitors instead of you, and what to change.** Give it your website and the questions your buyers ask. For each question it finds the page and the passage on your site that an answer engine would most likely quote, scores it 0-100, compares it with the pages that do get cited, and writes a **fix plan**: which page, which section, a rewrite draft built only from facts already on your pages, and what is missing. It also runs a full **GEO audit** (Generative Engine Optimization, also called AEO, answer engine optimization): can AI crawlers reach and read the site at all, with a live firewall test, a 0-100 GEO score and a shareable HTML report.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Audited website | $30.00 |
| Sampled page | $4.00 |
| Target question analyzed | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "websites": [
    "https://plausible.io"
  ],
  "targetQuestions": [
    "how much does plausible analytics cost",
    "is plausible analytics gdpr compliant"
  ],
  "competitorPages": [
    "how much does plausible analytics cost | https://usefathom.com/pricing"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "site",
    "site": "https://python.org",
    "score": 82,
    "grade": "B",
    "uncappedScore": 82,
    "gated": false,
    "gateReason": null,
    "partial": false,
    "reportUrl": "https://api.apify.com/v2/key-value-stores/<store>/records/REPORT-python.org.html",
    "categories": {
        "access": { "points": 40, "max": 40 },
        "discovery": { "points": 0, "max": 15 },
        "content": { "points": 29, "max": 30 },
        "entity": { "points": 11, "max": 12 }
    },
    "recommendations": [
        { "priority": "high", "check": "sitemap", "fix": "Publish an XML sitemap and list it in robots.txt with a \"Sitemap:\" line.", "pointsLost": 8 },
        { "priority": "medium", "check": "llms-txt", "fix": "Add /llms.txt: a Markdown file with your site name, a one-line summary and links to your key pages.", "pointsLost": 4 },
        { "priority": "medium", "check": "robots-sitemap-line", "fix": "Add \"Sitemap: https://your-site/sitemap.xml\" to robots.txt.", "pointsLost": 3 },
        { "priority": "low", "check": "extractable-structure", "fix": "Wrap the main content in <main> or <article>, and present key facts as lists or tables and common questions as H2/H3 headings; AI systems quote well-structured passages more easily.", "pointsLost": 1 }
    ],
    "aiCrawlers": {
        "allowed": ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "..."],
        "blocked": [],
        "unknown": [],
        "blockedAtFirewall": [],
        "userAgentTest": { "baseline": 200, "baselineBytes": 53213, "results": [{ "bot": "GPTBot", "status": 200, "blocked": false, "blockedReason": null, "bytes": 53213 }, "..."] }
    },
    "robotsTxt": { "status": 200, "found": true, "state": "found", "reason": null, "sitemaps": [] },
    "performance": { "ttfbMs": 335, "https": true, "hsts": true },
    "pages": [
        { "url": "https://python.org/", "title": "Welcome to Python.org", "readVia": "http", "via": "direct", "wordCount": 1182, "hasDescription": true, "h1Count": 5, "h2Count": 9, "lang": "en", "listCount": 28, "tableCount": 1 }
    ]
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
