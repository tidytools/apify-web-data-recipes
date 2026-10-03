# Backlink Checker - Referring Domains & Link Gap, Open Data (available from 2026-10-14)

Referring domains of any website, strongest first, with authority score and Chrome traffic rank, plus a competitor link gap: sites linking to your competitors but not to you. Common Crawl web graph, no Ahrefs login. $1 per 1,000 referring domains.

- Apify Store: `apify.com/tidytools/backlink-gap` (public from 2026-10-14)
- Actor ID: `tidytools/backlink-gap` (`20WDEXIozaSOcbUFu`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/backlink-gap`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-14**. Until then the recipes below return an error.

## Use case

Two jobs, in bulk and in seconds, for **any website on the web**:

1. **Referring domains**: the websites that link to a domain, **strongest first**, each with a **0-100 authority score** and its **Chrome traffic rank** (Top 1K ... Top 1M websites by real visitors).
2. **Link gap** ("link intersect"): enter your website and up to 10 competitors and get the **websites that link to your competitors but not to you**, ranked by how many competitors they link to, then by authority. These are your link-building and PR prospects: directories, review sites, partner pages, blogs and news sites that already cover businesses like yours.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Referring domain | $1.00 |
| Link prospect | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "mode": "referringDomains",
  "domains": [
    "apify.com",
    "tools.yukai.uk"
  ],
  "maxReferringDomainsPerDomain": 25
}
```

## Sample output

From the Actor's documentation (section "Output examples"):

```json
{
    "mode": "referringDomains",
    "domain": "zapier.com",
    "input": "zapier.com",
    "referringDomain": "adobe.com",
    "position": 1,
    "authorityScore": 85,
    "chromeTrafficBucket": 1000,
    "trafficRank": "Top 1K websites (Chrome)",
    "targetReferringDomains": 48072,
    "targetListedReferringDomains": 14804,
    "targetListTruncated": true,
    "found": true,
    "dataRelease": "cc-main-2026-jul-aug-sep",
    "charged": true,
    "checkedAt": "2026-10-03T13:49:45.617Z"
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
