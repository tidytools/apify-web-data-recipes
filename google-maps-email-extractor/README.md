# Google Maps Email Extractor - Place Contacts for CRM

Add website emails, phones and social profiles to Google Maps scraper results. One CRM-ready row per place; places without a website or contact are free. $2 per 1,000 charged websites.

- Apify Store: [https://apify.com/tidytools/google-maps-email-extractor](https://apify.com/tidytools/google-maps-email-extractor)
- Actor ID: `tidytools/google-maps-email-extractor` (`n0cIUvFJpqAT7K0dg`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/google-maps-email-extractor`

## Use case

Search businesses with a Google Maps Scraper, then give its dataset to this Actor: it returns one contact row per business for a CRM, including places without a listed website. The website's emails, phones and social profiles appear alongside the place name, address, category and Maps ID. This Actor reads an existing Google Maps Scraper dataset or a pasted export; it does not scrape Google Maps.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Processed website | $2.00 |
| Validated email | $1.00 |
| Additional page | $3.00 |
| Decision maker | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "mapsData": "[{\"title\":\"Hofbräuhaus München\",\"address\":\"Platzl 9, 80331 München\",\"website\":\"https://www.hofbraeuhaus.de/\"},{\"title\":\"Daunt Books Marylebone\",\"address\":\"83-84 Marylebone High Street, London W1U 4QW\",\"website\":\"https://dauntbooks.co.uk/\"}]"
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"placeName":"Hofbräuhaus München","placeAddress":"Platzl 9, 80331 München","website":"https://www.hofbraeuhaus.de/","emails":["willkommen@hofbraeuhaus.de"],"phones":["+49 89 290136100"],"socials":{},"checkedAt":"2026-10-21T08:00:00.000Z","charged":true}
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
