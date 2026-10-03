# Domain Authority Checker - Backlinks & Traffic Rank, Bulk (available from 2026-10-12)

Bulk domain authority from open web data: 0-100 authority score, referring domains, web graph rank, Majestic referring subnets and Chrome traffic rank for any domain. No Ahrefs or Moz login. $3 per 1,000 domains.

- Apify Store: `apify.com/tidytools/domain-authority` (public from 2026-10-12)
- Actor ID: `tidytools/domain-authority` (`d2qqhs32rIPvhdnbh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/domain-authority`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-12**. Until then the recipes below return an error.

## Use case

Give it a list of domains (or URLs, or e-mail addresses). For each one it returns, in bulk and in seconds:

- an **authority score from 0 to 100**,
- **referring domains**: how many other websites link to it,
- its **web graph rank** (harmonic centrality) and **PageRank position** among 133 million domains,
- **Majestic Million** rank, referring subnets and referring IPs (for the top 1 million sites),
- a **traffic rank** from Chrome's real-user data: "Top 1K / 5K / 10K / 50K / 100K / 500K / 1M websites",
- the number of subdomains seen.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Domain checked | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "apify.com",
    "wikipedia.org",
    "tools.yukai.uk",
    "github.com",
    "bbc.co.uk"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "apify.com",
    "inputs": ["apify.com", "https://apify.com/store"],
    "domain": "apify.com",
    "found": true,
    "authorityScore": 60,
    "authorityPercentile": 99.99,
    "referringDomains": 3556,
    "webGraphRank": 5287,
    "pageRankPosition": 19402,
    "subdomains": 29,
    "majesticRank": 16288,
    "majesticReferringSubnets": 2586,
    "majesticReferringIPs": 5911,
    "chromeTrafficBucket": 100000,
    "trafficRank": "Top 100K websites (Chrome)",
    "dataRelease": "cc-main-2026-jul-aug-sep",
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
