# B2B Leads by City - Dentist, Lawyer & HVAC Contact Lists

Prebuilt public business contacts by US or Canadian city. Search a niche and city, receive source links and refresh dates; optional live contact extraction. Charged per contact row.

- Apify Store: [https://apify.com/tidytools/b2b-lead-lists](https://apify.com/tidytools/b2b-lead-lists)
- Actor ID: `tidytools/b2b-lead-lists` (`v3wb5CY0PgzZPWKWE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/b2b-lead-lists`

## Use case

Search for businesses with one to five free-form keywords and a location. The Actor finds matching Overture Maps places, checks each company's own website for a public phone or role email, and returns contact rows with source pages. Different searches that find the same website can reuse its recent contact result.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Business contact row | $2.00 |
| Live website with contacts | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "searchTerms": [
    "dentist"
  ],
  "location": "Austin, TX",
  "maxResults": 2,
  "maxAgeDays": 30
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/b2b-lead-lists).

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
