# Website Change Monitor - Page Change Detection & Alerts

Website change tracker and content monitor: text and price changes, CSS selector per URL, keyword triggers, noise filters, screenshots, email, Slack, Discord, webhook alerts, AI summary. $2/1k checks.

- Apify Store: [https://apify.com/tidytools/website-change-monitor](https://apify.com/tidytools/website-change-monitor)
- Actor ID: `tidytools/website-change-monitor` (`rhX83ewDzbmT6Fq94`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-change-monitor`

## Use case

It watches web pages and tells you **what changed since the last check**: which text was added and which was removed. Run it on a schedule (hourly, daily, weekly) and get the changes in the dataset, by **e-mail**, in **Slack or Discord**, or pushed to a **webhook** (Zapier, Make, n8n, your own app). It accepts **Content Checker inputs** (`url`, `contentSelector`, `sendNotificationTo` and more) and the input fields of other change monitors (`startUrls`, `kvStoreName`, `slackWebhookUrl`...), takes **before and after screenshots**, and can watch thousands of pages in one run.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Page check | $2.00 |
| AI change summary | $5.00 |
| Change screenshot | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urlList": [
    "https://www.python.org/downloads/",
    "https://news.ycombinator.com"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{
    "url": "https://httpbin.org/uuid",
    "status": "changed",
    "checkedAt": "2026-09-29T02:38:51.571Z",
    "addedCount": 1,
    "removedCount": 1,
    "changeRatio": 0.333,
    "added": ["\"uuid\": \"03c057ca-3989-4dd3-9bbe-076de0a0eb27\""],
    "removed": ["\"uuid\": \"3f613ece-f6a4-4943-bfa1-d6a33a3ce95a\""],
    "significant": true,
    "aiSummary": "The UUID value changed from 3f613ece-f6a4-4943-bfa1-d6a33a3ce95a to 03c057ca-3989-4dd3-9bbe-076de0a0eb27",
    "significance": 1,
    "mode": "browser",
    "via": "browser"
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
