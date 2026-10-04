# ATS Jobs Scraper - Career Sites, Greenhouse, Lever, Workday

Give company domains or career-page URLs, get their live open jobs: Greenhouse, Lever, Ashby, Workday + 13 more ATSs, auto-detected. Salary, remote, new-job alerts. $2/1,000 jobs.

- Apify Store: [https://apify.com/tidytools/ats-career-site-jobs](https://apify.com/tidytools/ats-career-site-jobs)
- Actor ID: `tidytools/ats-career-site-jobs` (`k95BFAjcwk9AX61BE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ats-career-site-jobs`

## Use case

**ATS and career site jobs scraper for $2 per 1,000 jobs: open jobs live from company career sites on Greenhouse, Lever, Ashby, Workday and 13 more applicant tracking systems, auto-detected from a website, in one normalised format. Companies without a readable job board and filtered-out jobs are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Job | $2.00 |
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
  "companyPreset": "ai-labs",
  "maxJobsPerCompany": 3
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "input": "greenhouse:reddit",
    "title": "Front End Software Engineer, Consumer Engineering",
    "company": "Reddit",
    "location": "Remote - United States",
    "country": "US",
    "workplaceType": "remote",
    "salaryMin": 164200,
    "salaryMax": 229900,
    "salaryCurrency": "USD",
    "salaryPeriod": "year",
    "postedAt": "2026-09-17T17:07:34.000Z",
    "jobUrl": "https://job-boards.greenhouse.io/reddit/jobs/8147559",
    "ats": "greenhouse",
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
