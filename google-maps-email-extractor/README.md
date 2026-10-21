# Google Maps Email Extractor - Place Contacts for CRM

Add website emails, phones and social profiles to Google Maps scraper results. One CRM-ready row per place; places without a website or contact are free. $2 per 1,000 charged websites.

- Apify Store: [https://apify.com/tidytools/google-maps-email-extractor](https://apify.com/tidytools/google-maps-email-extractor)
- Actor ID: `tidytools/google-maps-email-extractor` (`n0cIUvFJpqAT7K0dg`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/google-maps-email-extractor`

## Use case

Turn Google Maps place results into one contact row per business for a CRM. Every source place gets a row, including places without a listed website. This Actor reads an existing Google Maps Scraper dataset or a pasted export; it does not scrape Google Maps.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Processed website | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "mapsData": "[{\"title\":\"Sample Shop A\",\"address\":\"Example Street 1\",\"categoryName\":\"Shop\",\"website\":\"https://example.com\"},{\"title\":\"Sample Shop B\",\"address\":\"Example Street 2\",\"website\":\"https://example.org\"},{\"title\":\"Sample Shop C\",\"address\":\"Example Street 3\",\"website\":null}]"
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"placeName":"Sample Cafe","address":"1 Example Street","category":"Cafe","website":"https://sample.example/","emails":["hello@sample.example"],"phones":["+1 555 0100"],"socials":{"instagram":"https://instagram.com/sample"},"placeId":"ChIJsample","charged":true}
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
