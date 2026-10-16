# Domain Authority Checker - Backlinks & Traffic Rank, Bulk

Bulk domain authority from open web data: 0-100 authority score, referring domains, web graph rank, Majestic referring subnets and Chrome traffic rank for any domain. No Ahrefs or Moz login. $3 per 1,000 domains.

- Apify Store: [https://apify.com/tidytools/domain-authority](https://apify.com/tidytools/domain-authority)
- Actor ID: `tidytools/domain-authority` (`d2qqhs32rIPvhdnbh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/domain-authority`

## Use case

**Paste a list of domains, get an authority score (0-100), referring domains and a traffic rank for each one, at $3 per 1,000 domains with data.** Domains that nothing links to, duplicates and invalid lines are free.

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
