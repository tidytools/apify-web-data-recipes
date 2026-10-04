# Google Maps Scraper Alternative - Local Business Leads by City

Business lead lists for any city, box or country from the open Overture Maps places data: name, category, address, coordinates, website, phone, role emails (info@) and socials. No proxies, no blocking. $1/1,000 places.

- Apify Store: [https://apify.com/tidytools/places-database](https://apify.com/tidytools/places-database)
- Actor ID: `tidytools/places-database` (`jSovfkbjeiDdEMz7f`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/places-database`

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
  ],
  "maxResults": 20
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "id": "eb8be1be-fb13-4309-84af-f2578e753841",
    "name": "Gragger Brot",
    "category": "bakery",
    "categoryPath": ["food_and_drink", "casual_eatery", "bakery"],
    "website": "http://www.gragger.de/",
    "phone": "+493081866477",
    "emails": ["marketing@gragger.de"],
    "emailType": "role-only",
    "address": "Potsdamer Str. 107",
    "city": "Berlin",
    "postcode": "10785",
    "country": "DE",
    "latitude": 52.5,
    "longitude": 13.36,
    "confidence": 0.996,
    "release": "2026-09-23.1",
    "license": "CDLA-Permissive-2.0",
    "attribution": "© Overture Maps Foundation (places)"
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
