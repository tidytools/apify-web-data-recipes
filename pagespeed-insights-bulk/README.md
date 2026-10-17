# Bulk PageSpeed Insights & Core Web Vitals Checker

Google PageSpeed Insights (Lighthouse) for many URLs: performance, accessibility, SEO scores, LCP, CLS, TBT, real-user Core Web Vitals (CrUX), top fixes, budgets and regression alerts. No API key needed. $2 per 1,000 measurements, failed free.

- Apify Store: [https://apify.com/tidytools/pagespeed-insights-bulk](https://apify.com/tidytools/pagespeed-insights-bulk)
- Actor ID: `tidytools/pagespeed-insights-bulk` (`IQqhSJHrbNWc7KAzh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/pagespeed-insights-bulk`

## Use case

**Paste a list of URLs, get one row per page and device with Lighthouse scores, lab metrics, real-user Core Web Vitals and the biggest fix, at $2 per 1,000 measurements ($0.002 each).** Failed or timed-out measurements, pages that cannot be loaded, invalid URLs and measurements skipped after a quota stop are free. No start fee, no API key needed.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| PageSpeed measurement | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.python.org/",
    "https://example.com/"
  ],
  "strategy": "both"
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "measurement",
    "input": "https://www.python.org/",
    "url": "https://www.python.org/",
    "finalUrl": "https://www.python.org/",
    "strategy": "mobile",
    "performanceScore": 72,
    "performanceRating": "needs-improvement",
    "accessibilityScore": 75,
    "bestPracticesScore": 96,
    "seoScore": 92,
    "fcpMs": 2859,
    "lcpMs": 5318,
    "tbtMs": 0,
    "cls": 0,
    "speedIndexMs": 4890,
    "ttiMs": 5318,
    "coreWebVitals": "PASSED",
    "fieldDataScope": "url",
    "fieldLcpMs": 1236,
    "fieldInpMs": 88,
    "fieldCls": 0,
    "fieldFcpMs": 1168,
    "fieldTtfbMs": 531,
    "fieldData": {
        "url": { "lcpMs": 1236, "lcpCategory": "FAST", "inpMs": 88, "inpCategory": "FAST", "cls": 0, "clsCategory": "FAST", "fcpMs": 1168, "fcpCategory": "FAST", "ttfbMs": 531, "ttfbCategory": "FAST", "coreWebVitals": "PASSED", "overallCategory": "FAST" },
        "origin": null
    },
    "topOpportunity": "Reduce unused JavaScript (~750 ms)",
    "opportunities": [
        { "id": "unused-javascript", "title": "Reduce unused JavaScript", "savingsMs": 750, "savingsBytes": 60458 },
        { "id": "unused-css-rules", "title": "Reduce unused CSS", "savingsMs": 560, "savingsBytes": 131404 }
    ],
    "passed": false,
    "failedChecks": ["lcpMs 5318 > 4000"],
    "source": "google",
    "lighthouseVersion": "13.5.0",
    "durationSecs": 15.1,
    "measuredAt": "2026-10-03T17:51:16.672Z",
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
