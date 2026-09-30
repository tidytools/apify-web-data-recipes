# AI Website & Text Classifier - Industry, Category, Sentiment (available from 2026-10-07)

Classify URLs, domains or texts with AI: company industry with B2B/B2C, page type, topic, IAB category, sentiment, content moderation or your own labels, with confidence and reason. $4/1,000.

- Apify Store: [https://apify.com/tidytools/ai-page-classifier](https://apify.com/tidytools/ai-page-classifier)
- Actor ID: `tidytools/ai-page-classifier` (`6XEMjr8sYaAARYqyi`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-page-classifier`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-07**. Until then the recipes below return an error.

## Use case

Give it a list of URLs, bare domains or texts and it **reads each one and labels it with AI**: by page type, by topic, by **industry and business model**, by IAB category, by **sentiment**, for **content moderation**, or by **your own labels**. Every result comes with a confidence level, a one-sentence reason and the language, ready to filter in a spreadsheet.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Classified page | $4.00 |
| Classified page (quick) | $3.00 |
| Classified page (deep) | $8.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "https://stripe.com/pricing",
    "https://docs.python.org/3/tutorial/index.html",
    "https://www.bbc.com/news",
    "https://www.allbirds.com/products/mens-tree-runners"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real results)"):

```json
[
    { "url": "https://stripe.com", "label": "financial-services", "businessModel": "B2B", "confidence": "high",
      "companySummary": "Stripe is a financial services platform that helps businesses accept payments, build flexible billing models, and manage money movement." },
    { "url": "https://allbirds.com", "label": "consumer-products", "businessModel": "B2C", "confidence": "high",
      "companySummary": "Allbirds is a company that designs and sells comfortable and sustainable shoes made from natural materials." },
    { "url": "https://redcross.org", "label": "nonprofit", "businessModel": "nonprofit", "confidence": "high" },
    { "url": "https://www.gov.uk", "label": "government-public-sector", "businessModel": "government", "confidence": "high" },
    { "url": "https://hubspot.com", "label": "software-saas", "businessModel": "B2B", "confidence": "high",
      "companySummary": "HubSpot provides software and tools for businesses to manage marketing, sales, customer service, and CRM" }
]
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
