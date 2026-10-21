# Career Page Jobs Scraper - Greenhouse, Lever, Workday & ATS

Career page jobs scraper and ATS jobs scraper: scrape job postings from Greenhouse, Lever, Ashby, Workday + 13 more ATSs, live from company domains or career-page URLs, auto-detected. Salary, remote, new-job alerts. $1/1,000 jobs.

- Apify Store: [https://apify.com/tidytools/ats-career-site-jobs](https://apify.com/tidytools/ats-career-site-jobs)
- Actor ID: `tidytools/ats-career-site-jobs` (`k95BFAjcwk9AX61BE`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ats-career-site-jobs`

## Use case

**Career Page Jobs Scraper (an ATS jobs scraper) scrapes job postings from Greenhouse, Lever and 16 more applicant tracking systems: give it company domains, career pages or board URLs, and get their live open jobs from Greenhouse, Lever, Ashby, Workday and the rest (auto-detected) in one normalised format, for $1 per 1,000 jobs. Companies without a readable job board and filtered-out jobs are free.**

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
