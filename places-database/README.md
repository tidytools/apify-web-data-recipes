# Google Maps Scraper Alternative - Local Business Leads by City (available from 2026-10-04)

Business lead lists for any city, box or country from the open Overture Maps places data: name, category, address, coordinates, website, phone, role emails (info@) and socials. No proxies, no blocking. $1/1,000 places.

- Apify Store: `apify.com/tidytools/places-database` (public from 2026-10-04)
- Actor ID: `tidytools/places-database` (`jSovfkbjeiDdEMz7f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/places-database`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-04**. Until then the recipes below return an error.

## Use case

It returns **business lead lists for any city, area or country**, straight from the open **Overture Maps places dataset**: name, category, address, coordinates, website, phone, role e-mail addresses (info@, contact@) and social links. You give it `Berlin, DE` and `dental_clinic`; it gives you a clean table.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Place | $1.00 |
| Place enriched (contacts) | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "locations": [
    "Lisbon, PT"
  ],
  "categories": [
    "dental_clinic"
  ]
}
```

## Sample output

See the output examples on the Store page.

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
