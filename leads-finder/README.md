# Leads Finder - B2B Emails by City (Apollo Alternative)

Find public company website emails by industry and US or Canadian city. Prebuilt lists or live lookup, source page and MX domain result. With requireEmail true (default), phone-only rows are skipped without charge; with false, phone-only contact rows can be charged.

- Apify Store: [https://apify.com/tidytools/leads-finder](https://apify.com/tidytools/leads-finder)
- Actor ID: `tidytools/leads-finder` (`x3mMatrbtvESUwdcL`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/leads-finder`

## Use case

Find companies in a supported industry and US or Canadian city. With the default `requireEmail: true`, each returned company has a public email found on its own website, a source page, and an MX result for the email domain. If you set `requireEmail: false`, phone-only contact rows can also be returned and charged. This is an Apollo alternative for public company contacts; it does not provide private profiles or mailbox verification.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Business contact row | $2.00 |
| Live website with contacts | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "industry": "dentist",
  "location": "Austin, TX",
  "maxResults": 2,
  "buildIfMissing": false,
  "requireEmail": true
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"id":"example-1","name":"Example Dental","website":"https://example.org/","phone":"+15125550100","emails":["info@example.org"],"emailMx":"valid","address":"Austin, TX","sourcePage":"https://example.org/contact","sourceDataset":"Overture Maps Places","sourceUpdated":null,"fetchedAt":"2026-10-23T00:00:00.000Z","fromIndex":true,"license":"CDLA-Permissive-2.0","attribution":"© Overture Maps Foundation (places)","niche":"dentist","city":"Austin, TX","success":true,"charged":true,"chargeEvent":"lead-row"}
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
