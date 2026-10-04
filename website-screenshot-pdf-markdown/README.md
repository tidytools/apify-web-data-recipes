# Website Screenshot API - Full Page Screenshot & URL to PDF

Bulk website screenshots: full page, one element, mobile or tablet. URL to PDF and HTML to PDF for any web page, plus clean Markdown, in one run. Hides ads, cookie banners and pop-ups. Failures free.

- Apify Store: [https://apify.com/tidytools/website-screenshot-pdf-markdown](https://apify.com/tidytools/website-screenshot-pdf-markdown)
- Actor ID: `tidytools/website-screenshot-pdf-markdown` (`aHKoTOLGnFnzHgHPI`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-screenshot-pdf-markdown`

## Use case

**Website screenshot API for bulk URLs: full-page, mobile or single-element screenshots for $1 per 1,000, plus URL to PDF ($2.50 per 1,000) and clean Markdown from the same page load. Failed and blocked pages are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Screenshot | $1.00 |
| PDF | $2.50 |
| Markdown | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://example.com"
  ],
  "outputs": [
    "screenshot",
    "markdown"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "url": "https://stripe.com",
    "httpStatus": 200,
    "title": "Stripe | Financial Infrastructure to Grow Your Revenue",
    "success": true,
    "device": "mobile",
    "viewportWidth": 390,
    "pixelDensity": 3,
    "screenshotUrl": "https://api.apify.com/v2/key-value-stores/…/records/00000-stripe-com-screenshot-mobile.jpg",
    "screenshotBytes": 1255663,
    "format": "jpeg",
    "fullPage": true,
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
