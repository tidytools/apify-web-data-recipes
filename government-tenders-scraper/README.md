# Government Tenders Scraper: SAM.gov, TED EU, UK & Canada

Public tenders and contract awards from 5 official sources in one format: SAM.gov, EU TED, UK Find a Tender, Contracts Finder, CanadaBuys. Keywords, CPV/NAICS, countries, value, open deadlines; only-new alerts; CSV. $3 per 1,000 notices.

- Apify Store: [https://apify.com/tidytools/government-tenders-scraper](https://apify.com/tidytools/government-tenders-scraper)
- Actor ID: `tidytools/government-tenders-scraper` (`MCtFa3ieS768GEaSh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/government-tenders-scraper`

## Use case

**Enter keywords, countries or CPV / NAICS codes (all optional), get one row per tender or contract award from SAM.gov, TED, UK Find a Tender, Contracts Finder and CanadaBuys, with title, buyer, deadline, value, codes, link and the buyer's published contact point, at $3 per 1,000 notices.** Notices dropped by your filters, closed tenders, notices seen in earlier runs and sources that cannot be read are free. No start fee.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Notice | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "keywords": [
    "software"
  ],
  "daysBack": 3,
  "maxResults": 100
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "notice",
    "source": "ted",
    "sourceName": "TED (EU and EEA)",
    "noticeId": "678030-2026",
    "noticeType": "cn-standard",
    "stage": "tender",
    "title": "Assistance technique sécurité",
    "category": "IT services: consulting, software development, Internet and support",
    "language": "fra",
    "description": "Le marché porte sur la réalisation de prestations d'assistance technique dans le domaine de la sécurité des systèmes d'information ...",
    "buyerName": "GIE SESAM-Vitale",
    "buyerCountry": "FR",
    "buyerCity": "Le mans cedex 2",
    "publishedDate": "2026-10-02",
    "deadline": "2026-11-02T12:00:00+02:00",
    "daysToDeadline": 29,
    "cpvCodes": ["72000000"],
    "contractType": "services",
    "procedure": "neg-w-call",
    "estimatedValue": 2700000,
    "currency": "EUR",
    "url": "https://ted.europa.eu/en/notice/-/detail/678030-2026",
    "submissionUrl": "http://www.achatpublic.com",
    "contactEmail": "(buyer's published contact)",
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
