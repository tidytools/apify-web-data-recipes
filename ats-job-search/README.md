# Job Search API - Greenhouse, Lever, Ashby & Workday Jobs Index (available from 2026-10-10)

Search 1.4M+ live jobs from 54,000+ company career boards (Greenhouse, Lever, Ashby, Workday, Workable, Personio and 10 more ATSs) in one query, refreshed daily. Posted vs first-seen dates, reposts, duplicates, hiring companies. $1.50/1,000 jobs.

- Apify Store: `apify.com/tidytools/ats-job-search` (public from 2026-10-10)
- Actor ID: `tidytools/ats-job-search` (`AdBiuPJ3lCiwM0a8M`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ats-job-search`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-10**. Until then the recipes below return an error.

## Use case

It searches **one index of live job postings from company career boards** — Greenhouse, Lever, Ashby, Workday, Workable, Recruitee, Personio, Teamtailor, BambooHR and 7 more applicant tracking systems — and returns the matching jobs in seconds. No company list needed: ask for "data engineer, remote, posted in the last 7 days" and get every matching job across all indexed employers.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Actor Start | $0.50 |
| Job | $1.50 |
| Hiring company | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "keywords": [
    "data engineer",
    "machine learning"
  ],
  "maxResults": 100
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{
    "title": "Data Engineer, Data Quality & Provenance",
    "company": "Wayve",
    "companyDomain": "wayve.ai",
    "companyWebsite": "https://wayve.ai/",
    "location": "Leonberg, Germany",
    "country": "DE",
    "remote": false,
    "workplaceType": null,
    "employmentType": "full-time",
    "department": "Simulation, Evaluation, Validation / Simulation, Evaluation, Validation",
    "salaryMin": null,
    "salaryMax": null,
    "salaryCurrency": null,
    "salaryPeriod": null,
    "url": "https://jobs.ashbyhq.com/wayve/102a31c7-44a5-48bc-8c6e-1f4434e83974",
    "applyUrl": "https://jobs.ashbyhq.com/wayve/102a31c7-44a5-48bc-8c6e-1f4434e83974/application",
    "sourcePostedAt": "2026-10-02T15:25:57.680Z",
    "sourcePostedAtApproximate": false,
    "originalPostedAt": "2026-10-02T15:25:57.680Z",
    "firstSeenAt": "2026-10-02T16:21:23.777Z",
    "firstSeenIsBaseline": false,
    "indexLagHours": 0.9,
    "lastSeenAt": "2026-10-02T16:21:23.777Z",
    "removedAt": null,
    "postedAt": "2026-10-02T15:25:57.680Z",
    "postedAtApproximate": false,
    "updatedAt": null,
    "repostOf": null,
    "repostKind": null,
    "repostCount": 0,
    "reopenedCount": 0,
    "duplicateGroup": null,
    "duplicateKind": null,
    "isDuplicate": false,
    "companyDomainSource": "ats_profile",
    "companyDomainConfidence": "high",
    "snippet": "Before the detail, here's the challenge you'd help us solve. We build the embodied intelligence that moves real vehicles safely, and the ecosystem a billion machines will run on in the future. Very few people in AI can say this. Every role here, whatever the team, plugs into…",
    "ats": "ashby",
    "board": "ashby:wayve",
    "jobKey": "ashby:wayve:102a31c7-44a5-48bc-8c6e-1f4434e83974"
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
