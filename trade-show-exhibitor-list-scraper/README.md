# Trade Show Exhibitor List Scraper - Company, Booth, Website (available from 2026-10-06)

Exhibitor lists from trade show and expo directories: company, booth, hall, categories, country, website, description, logo. a2z (Personify) and ExpoFP natively; other sites via AI. Company data only.

- Apify Store: `apify.com/tidytools/trade-show-exhibitor-list-scraper` (public from 2026-10-06)
- Actor ID: `tidytools/trade-show-exhibitor-list-scraper` (`kF9CLDGcwUS4BehnG`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/trade-show-exhibitor-list-scraper`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-06**. Until then the recipes below return an error.

## Use case

It turns **trade show exhibitor directories into a clean company list**: one row per exhibiting company with **name, booth, hall, categories, country, city, website, description, logo and profile link**, plus the event name and dates. Paste the directory URL, or just the event's own website: the Actor finds the directory platform behind it and reads the **public data the directory page itself loads**. No login, no browser for the supported platforms, and **company-level data only**.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Exhibitor | $2.00 |
| Exhibitor (name and booth only) | $0.50 |
| Exhibitor (AI-extracted) | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://slas2026.expofp.com/",
    "https://kbis.a2zinc.net/kbis2026/Public/Exhibitors.aspx?Index=All"
  ],
  "maxExhibitorsPerDirectory": 10
}
```

## Sample output

From the Actor's documentation (section "Output example (a2z, profile read)"):

```json
{
    "input": "https://s36.a2zinc.net/clients/SME/FABTECH2026/Public/Exhibitors.aspx?Index=All",
    "success": true,
    "source": "platform",
    "platform": "a2z (Personify)",
    "eventName": "FABTECH 2026",
    "name": "1960 SERAVESI",
    "booth": "C8119",
    "categories": ["Bending/Forming", "Flanging Machines", "Plate & Structural Fabricating", "Angle Bending Rolls"],
    "website": "https://www.1960seravesi.com/",
    "country": "Italy",
    "city": "Calcinato",
    "postalCode": "25011",
    "address": "Via Statale 10T",
    "companyPhone": "+39030-6091301",
    "profileUrl": "https://s36.a2zinc.net/clients/SME/FABTECH2026/Public/eBooth.aspx?BoothID=539883&EventID=128",
    "detailLevel": "full",
    "charged": true,
    "chargedEvent": "exhibitor"
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
