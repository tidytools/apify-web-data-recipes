# Backlink Checker - Referring Domains & Link Gap, Open Data

Referring domains of any website, strongest first, with authority score and Chrome traffic rank, plus a competitor link gap: sites linking to your competitors but not to you. Common Crawl web graph, no Ahrefs login. $1.50 per 1,000 referring domains.

- Apify Store: [https://apify.com/tidytools/backlink-gap](https://apify.com/tidytools/backlink-gap)
- Actor ID: `tidytools/backlink-gap` (`20WDEXIozaSOcbUFu`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/backlink-gap`

## Use case

**Give it domains, get the websites that link to them** (authority score and Chrome traffic rank for each): **$1.50 per 1,000 referring domains**. **Give it your site and 1-10 competitors, get the sites that link to them but not to you**: **$3.00 per 1,000 link prospects**. Domains the web graph does not know, duplicates, invalid lines and empty results are free; there is no start fee. Data: the open Common Crawl web graph (domain level, July-September 2026), not Ahrefs or Semrush. Jump to [How to use it](#how-to-use-it).

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Referring domain | $1.50 |
| Link prospect | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "mode": "referringDomains",
  "domains": [
    "apify.com",
    "scrapingbee.com"
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
