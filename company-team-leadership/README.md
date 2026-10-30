# Company Employees Scraper - Leadership Team Names & Titles

Find the people a company publishes on its own website and investor site: team, executives, founders and board, each with job title, role and source page. No LinkedIn login. $3 per 1,000 people; companies without people are free.

- Apify Store: [https://apify.com/tidytools/company-team-leadership](https://apify.com/tidytools/company-team-leadership)
- Actor ID: `tidytools/company-team-leadership` (`vW2U4JzEwUgDgFcxU`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/company-team-leadership`

## Use case

Give it company websites; it returns **the people each company publishes about itself**: the leadership team, executives, founders, board members and, if you want, advisors and the wider team. One row per person with **full name, job title, role (employee / founder / board / advisor) and the page it came from**.

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
    "apify.com"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (October 2026: a real row from apify.com, and the free row a company without a people list gets)"):

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
