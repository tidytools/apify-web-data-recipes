# Domain Overview - Semrush & Ahrefs Alternative, Tech & Hiring (available from 2026-10-13)

One row per domain: traffic rank (global and by country, 12-month trend), authority and referring domains, tech stack, open jobs, domain age and AI crawler policy. Bulk lists, no logins. $10 per 1,000 domains; unreadable websites free.

- Apify Store: `apify.com/tidytools/domain-overview` (public from 2026-10-13)
- Actor ID: `tidytools/domain-overview` (`qUmyFGvHNegwY3URy`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/domain-overview`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-13**. Until then the recipes below return an error.

## Use case

Give it a list of domains (or URLs, or e-mail addresses, or another run's dataset). For each domain you get **one row** that answers "how big is this company's website, what is it built with, and is the company growing?":

- 📈 **Traffic rank** from real Chrome users: global Top 1K ... 1M, the top country, the rank in up to 238 countries and the 6-month trend
- 🔗 **Authority**: a 0-100 score and the number of referring domains (who links to the site), from the Common Crawl web graph
- 🧰 **Tech stack**: CMS, e-commerce platform, frameworks, analytics, CDN and hosting, plus the **e-mail provider** and the SaaS tools verified in its DNS
- 💼 **Hiring**: open jobs, remote jobs, hiring countries, sample job titles and the careers page, from our index of 1.4 million openings on 54,000 company career sites (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Personio and 10 more)
- 🗓️ **Domain age** and registrar (from the registry's RDAP record)
- 🤖 **AI crawler policy**: whether robots.txt lets GPTBot, ClaudeBot, PerplexityBot and 26 other AI crawlers in, and whether the site has an `llms.txt`
- 📝 the site's **title and description**, and a one-line **summary**

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
