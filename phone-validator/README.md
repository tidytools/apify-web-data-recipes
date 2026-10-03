# Bulk Phone Number Validator - Format, Type & Country (available from 2026-10-06)

Validate and format phone numbers in bulk, offline: valid or not, E.164 / international / national format, country, line type (mobile, fixed line, toll free, VoIP) and time zones. CSV upload or another Actor's dataset. Invalid numbers are free. $0.30 per 1,000.

- Apify Store: `apify.com/tidytools/phone-validator` (public from 2026-10-06)
- Actor ID: `tidytools/phone-validator` (`lIC2MOymH7l4MlpCH`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/phone-validator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-06**. Until then the recipes below return an error.

## Use case

**Phone number validator and formatter** for lists you are about to import into a CRM, a dialer or an SMS tool: give it a list, a CSV or the dataset of a lead scraper and get, for every number, **valid or not**, the **E.164, international, national and RFC 3966 formats**, the **country**, the **line type** (mobile, fixed line, toll free, VoIP…) and the **reason** when it is invalid. **$0.30 per 1,000 valid numbers, no start fee, invalid numbers free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Phone number validated | $0.30 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "phones": [
    "+1 650-253-0000",
    "+44 20 7946 0958 ext. 12",
    "+49 30 901820",
    "0912 345 678",
    "(02) 2345-6789",
    "+1 800 555 0199",
    "+1 123 456 7890",
    "+44 20 7946"
  ],
  "defaultCountry": "TW"
}
```

## Sample output

From the Actor's documentation (section "Output example (local test run, 2 October 2026)"):

```json
{
    "input": "0912 345 678",
    "valid": true,
    "possible": true,
    "phone": "+886912345678",
    "e164": "+886912345678",
    "international": "+886 912 345 678",
    "national": "0912 345 678",
    "rfc3966": "tel:+886912345678",
    "countryCode": "TW",
    "country": "Taiwan",
    "callingCode": "+886",
    "nationalNumber": "912345678",
    "type": "MOBILE",
    "extension": null,
    "timezones": ["Asia/Taipei"],
    "defaultCountryUsed": "TW",
    "reasonCode": null,
    "liveCheck": false,
    "charged": true,
    "source": "list",
    "duplicates": 2
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
