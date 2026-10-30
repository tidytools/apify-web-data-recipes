# Decision Maker Finder - CEOs, Founders & VPs from Websites

Company domains in, decision makers out: CEO, founders, C-level, VPs, heads and directors from each company's own website and investor pages, with job title and source page. No LinkedIn, no emails. $3 per 1,000 people.

- Apify Store: [https://apify.com/tidytools/decision-maker-finder](https://apify.com/tidytools/decision-maker-finder)
- Actor ID: `tidytools/decision-maker-finder` (`u9WIZ570yxhEaQrJB`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/decision-maker-finder`

## Use case

**Paste company domains → get the decision makers each company publishes about itself**: CEO and other C-level executives, founders, owners, presidents, VPs, heads of department and directors. One row per person with **full name, job title, role and the page it came from**.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Person | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "companies": [
    "apify.com",
    "buffer.com"
  ],
  "titleContains": [
    "CEO",
    "CTO",
    "CFO",
    "COO",
    "CMO",
    "Chief",
    "Founder",
    "Owner",
    "President",
    "VP",
    "Head",
    "Director",
    "General Manager",
    "Managing"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
[
    {
        "input": "apify.com",
        "company": "Apify",
        "domain": "apify.com",
        "personName": "Jan Curn",
        "jobTitle": "Founder & CEO",
        "role": "founder",
        "sourceUrl": "https://apify.com/about",
        "sources": ["https://apify.com/about"],
        "via": "card",
        "confidence": "high",
        "investorSite": null,
        "observedAt": "2026-10-23T08:10:00.000Z"
    },
    {
        "input": "example-bakery.com",
        "company": "Example Bakery",
        "domain": "example-bakery.com",
        "personName": null,
        "jobTitle": null,
        "role": null,
        "sourceUrl": null,
        "errorType": "no_people",
        "error": "No people for example-bakery.com: no team, leadership or board list found on 3 page(s) read (not charged)",
        "charged": false,
        "observedAt": "2026-10-23T08:10:00.000Z"
    }
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
