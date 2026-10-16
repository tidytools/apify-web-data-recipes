# SEC Form D Scraper - Recently Funded Companies & Startups

Every new SEC Form D filing from EDGAR: companies that just raised money, amount sold, offering size, industry, state, phone and executives. Filter by industry, state, amount; only-new alerts for daily schedules; CSV. $5 per 1,000 filings, filtered and failed free.

- Apify Store: [https://apify.com/tidytools/sec-form-d-scraper](https://apify.com/tidytools/sec-form-d-scraper)
- Actor ID: `tidytools/sec-form-d-scraper` (`FrOgWmwyr08jC2fyH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/sec-form-d-scraper`

## Use case

**Input:** a date range (or "last N days") plus optional filters for industry, state, amount raised and company name. **Output:** one row per SEC Form D filing with the company, amount sold, offering size, industry, address, phone and executives, plus a CSV file. **Price:** $5 per 1,000 filings; filings your filters drop, unreadable filings and invalid inputs are free; no start fee.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Form D filing | $5.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "daysBack": 5,
  "maxResults": 100
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "filing",
    "filingDate": "2026-10-02",
    "formType": "D",
    "isAmendment": false,
    "accessionNumber": "0002028034-26-000002",
    "cik": "2028034",
    "companyName": "Alethios Inc.",
    "entityType": "Corporation",
    "jurisdictionOfIncorporation": "Delaware",
    "yearOfIncorporation": 2023,
    "incorporatedWithinFiveYears": true,
    "street": "235 Montgomery St., Suite 948",
    "city": "San Francisco",
    "stateOrCountry": "CA",
    "zipCode": "94104",
    "phone": "(650) 334-8239",
    "industryGroup": "Other",
    "isPooledInvestmentFund": false,
    "revenueRange": "Decline to Disclose",
    "federalExemptionNames": ["Rule 506(b)"],
    "dateOfFirstSale": "2026-09-29",
    "securitiesOffered": ["Equity"],
    "totalOfferingAmountUsd": 2191763,
    "totalAmountSoldUsd": 2169962,
    "totalRemainingUsd": 21801,
    "percentSold": 99,
    "totalInvestors": 17,
    "salesCommissionsUsd": 0,
    "relatedPersons": [
        { "name": "Zeenia Framroze", "relationships": ["Executive Officer", "Director", "Promoter"], "clarification": null },
        { "name": "Stephen M. McLean, Jr.", "relationships": ["Director"], "clarification": null }
    ],
    "executives": "Zeenia Framroze (Executive Officer, Director, Promoter); Stephen M. McLean, Jr. (Director)",
    "signerTitle": "Chief Executive Officer",
    "formUrl": "https://www.sec.gov/Archives/edgar/data/2028034/000202803426000002/xslFormDX01/primary_doc.xml",
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
