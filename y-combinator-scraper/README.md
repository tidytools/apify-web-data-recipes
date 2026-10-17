# Y Combinator Scraper - YC Companies, Jobs & Startup Directory

All 6,000+ Y Combinator companies by batch, industry, location, status and team size, with founders, social links, launches and open jobs (salary, equity, visa). New-company and new-job alerts. $2 per 1,000 companies, $1 per 1,000 jobs.

- Apify Store: [https://apify.com/tidytools/y-combinator-scraper](https://apify.com/tidytools/y-combinator-scraper)
- Actor ID: `tidytools/y-combinator-scraper` (`4OfDed53gMCNUTw8c`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/y-combinator-scraper`

## Use case

**Input:** YC batches, industries, locations, status or keywords (or a list of YC company links); choose companies or jobs. **Output:** one row per YC company (with founders' names, links and open jobs) or one row per open job (with salary, equity and visa). **Price:** $2 per 1,000 companies with profile details, $0.50 per 1,000 with directory fields only, $1 per 1,000 jobs; filtered-out and failed items are free; no start fee.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Company with profile | $2.00 |
| Company (directory fields) | $0.50 |
| Job | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "batches": [
    "Fall 2026",
    "Summer 2026"
  ],
  "maxResults": 20
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "company",
    "name": "Stripe",
    "slug": "stripe",
    "batch": "Summer 2009",
    "batchCode": "S09",
    "status": "Active",
    "oneLiner": "Economic infrastructure for the internet.",
    "website": "http://stripe.com",
    "domain": "stripe.com",
    "teamSize": 7000,
    "industry": "Fintech",
    "tags": ["Banking as a Service", "Fintech", "SaaS"],
    "locations": "San Francisco, CA, USA",
    "stage": "Growth",
    "isHiring": true,
    "topCompany": true,
    "yearFounded": 2009,
    "linkedinUrl": "https://www.linkedin.com/company/stripe/",
    "twitterUrl": "https://twitter.com/stripe",
    "githubUrl": "https://github.com/stripe",
    "founders": [
        { "name": "Patrick Collison", "title": "Founder/CEO", "isActive": true },
        { "name": "John Collison", "title": "Founder/President", "isActive": true }
    ],
    "founderNames": "Patrick Collison, John Collison",
    "openJobs": 3,
    "jobTitles": ["Frontend Engineer, Identity", "Machine Learning Engineer, Identity", "Head of Engineering, Identity Graph"],
    "news": [{ "title": "Stripe: 2023 CNBC Disruptor 50", "url": "https://www.cnbc.com/2023/05/09/stripe-disruptor-50.html", "date": "May 09, 2023" }],
    "ycUrl": "https://www.ycombinator.com/companies/stripe",
    "detailLevel": "profile",
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
