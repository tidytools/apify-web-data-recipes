# Google Maps Email Extractor - Website Emails, Phones & Socials

Google Maps email extractor: add emails to Google Maps results. Reads each business's own website (from a Maps scraper dataset or a domain list) for emails, best email with MX check, phones, socials. Does not scrape Maps itself. $2/1,000 sites; nothing found = free.

- Apify Store: [https://apify.com/tidytools/website-contact-extractor](https://apify.com/tidytools/website-contact-extractor)
- Actor ID: `tidytools/website-contact-extractor` (`kFhBWk7SCYTakF6Fn`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-contact-extractor`

## Use case

**Google Maps email extractor for $2 per 1,000 websites: give it the results of your Google Maps scraper (or a plain list of domains) and get each business's emails, the best email to use, phone numbers and social profiles, read from the business's own website. Websites with nothing found and unreachable websites are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Processed website | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "katzsdelicatessen.com",
    "hofbraeuhaus.de"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output: one row per place (shortened)"):

```json
{
    "businessName": "Stumptown Coffee Roasters",
    "placeName": "Stumptown Coffee Roasters",
    "placeAddress": "128 SW 3rd Ave, Portland, OR 97204",
    "placePhone": "+15032241000",
    "placeId": "ChIJ...",
    "mapsUrl": "https://www.google.com/maps/search/?api=1&query=...&query_place_id=ChIJ...",
    "domain": "stumptowncoffee.com",
    "bestEmail": "info@stumptowncoffee.com",
    "bestEmailType": "role_company",
    "bestEmailHasMx": true,
    "emailsText": "info@stumptowncoffee.com, legal@stumptown.com, customerservice@stumptown.com",
    "primaryPhone": "+18777113385",
    "socialProfiles": { "instagram": "https://www.instagram.com/stumptowncoffee", "facebook": "https://www.facebook.com/stumptowncoffee" },
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
