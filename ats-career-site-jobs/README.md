# ATS & Career Site Jobs Scraper - Greenhouse, Lever, Workday (available from 2026-10-01)

Live jobs from company career sites: paste career pages, domains or board URLs. Auto-detects 17 ATSs incl. Greenhouse, Lever, Ashby, Workday, SmartRecruiters; only-new-jobs alerts. $1/1,000 jobs.

- Apify Store: [https://apify.com/tidytools/ats-career-site-jobs](https://apify.com/tidytools/ats-career-site-jobs)
- Actor ID: `tidytools/ats-career-site-jobs` (`k95BFAjcwk9AX61BE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ats-career-site-jobs`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-01**. Until then the recipes below return an error.

## Use case

It returns the **open jobs of any list of companies, live from their own career sites**. Paste career pages, company websites or job board URLs, in any mix: the Actor finds which applicant tracking system (ATS) each company uses and reads that ATS's **public job board feed** — the JSON, XML and RSS feeds these vendors serve so companies can show their jobs on their own websites. Every job comes back in **one normalised format**, whatever the ATS.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Job | $1.00 |
| Company ATS detected | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "companies": [
    "https://job-boards.greenhouse.io/airbnb",
    "jobs.lever.co/leverdemo",
    "https://apply.workable.com/huggingface/"
  ],
  "maxJobsPerCompany": 10
}
```

## Sample output

From the Actor's documentation (section "Output example (jobs mode)"):

```json
{
    "input": "greenhouse:reddit",
    "inputIndex": 5,
    "success": true,
    "jobKey": "greenhouse:reddit:8147559",
    "jobId": "8147559",
    "title": "Front End Software Engineer, Consumer Engineering",
    "company": "Reddit",
    "department": "Consumer",
    "team": null,
    "location": "Remote - United States",
    "locations": ["Remote - United States"],
    "country": "US",
    "workplaceType": "remote",
    "remote": true,
    "employmentType": null,
    "employmentTypeText": null,
    "salaryMin": 164200,
    "salaryMax": 229900,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "salaryText": "$164,200—$229,900 USD",
    "salarySource": "description",
    "postedAt": "2026-09-17T17:07:34.000Z",
    "postedAtApproximate": false,
    "updatedAt": "2026-09-17T17:07:34.000Z",
    "jobUrl": "https://job-boards.greenhouse.io/reddit/jobs/8147559",
    "applyUrl": "https://job-boards.greenhouse.io/reddit/jobs/8147559",
    "requisitionId": "Pooled",
    "descriptionText": "Reddit is a community of communities. It’s built on shared interests, passion, and trust, and is home to the most open and authentic conversations on …",
    "source": "ats",
    "ats": "greenhouse",
    "atsSlug": "reddit",
    "boardUrl": "https://job-boards.greenhouse.io/reddit",
    "detectionMethod": "input",
    "charged": true,
    "scrapedAt": "2026-09-30T04:52:29.128Z"
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
