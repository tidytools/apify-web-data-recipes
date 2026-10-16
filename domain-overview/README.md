# Domain Overview - Semrush & Ahrefs Alternative, Tech & Hiring

One row per domain: traffic rank (global and by country, 12-month trend), authority and referring domains, tech stack, open jobs, domain age and AI crawler policy. Bulk lists, no logins. $10 per 1,000 domains; unreadable websites free.

- Apify Store: [https://apify.com/tidytools/domain-overview](https://apify.com/tidytools/domain-overview)
- Actor ID: `tidytools/domain-overview` (`qUmyFGvHNegwY3URy`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/domain-overview`

## Use case

**Input:** a list of domains (or URLs, e-mail addresses, or another run's dataset). **Output:** one row per domain with traffic rank, authority, tech stack, open jobs, domain age and AI crawler policy. **Price:** $10 per 1,000 domains ($0.01 each), only when the website could be read; unreadable websites, duplicates and invalid lines are free. No start fee.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Domain analyzed | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "stripe.com",
    "figma.com",
    "apify.com",
    "bbc.co.uk",
    "tools.yukai.uk"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "linear.app",
    "domain": "linear.app",
    "website": "https://linear.app/",
    "websiteStatus": "online",
    "title": "Linear – The system for product development",
    "globalTrafficRank": 50000,
    "globalTrafficRankLabel": "Top 50K websites worldwide",
    "trafficTrend": "stable",
    "topCountry": "us",
    "topCountryRankLabel": "Top 5K in United States",
    "countriesListed": 127,
    "authorityScore": 61,
    "referringDomains": 4288,
    "technologyCount": 24,
    "technologies": ["Next.js", "React", "Cloudflare", "Google Cloud", "Stripe", "HubSpot", "Google Workspace", "Slack", "Zoom"],
    "hosting": "Cloudflare, Google Cloud",
    "emailProvider": "Google Workspace",
    "aiCrawlerPolicy": "open",
    "aiBotsBlocked": [],
    "hasLlmsTxt": true,
    "domainCreatedAt": "2018-05-09T23:45:22.384Z",
    "domainAgeYears": 8.4,
    "registrar": "CloudFlare, Inc.",
    "hiringIndexed": true,
    "openJobs": 30,
    "remoteJobs": 29,
    "hiringCountries": ["US", "European Union", "GB"],
    "sampleJobTitles": ["Senior / Staff Fullstack Engineer", "Product Manager", "Developer Relations"],
    "careersUrl": "https://jobs.ashbyhq.com/linear",
    "atsPlatforms": ["ashby"],
    "summary": "Top 50K worldwide (stable); authority 61/100 (4,288 referring domains); Next.js, React, Cloudflare, Google Cloud; 30 open jobs; domain 8.4 years old; open to AI crawlers",
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
