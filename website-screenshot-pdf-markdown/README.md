# Website Screenshot API - Full Page, URL to PDF & Markdown

Bulk website screenshots (full page, element, mobile, tablet), URL to PDF and clean Markdown in one run. PNG, JPEG or WebP, ad and cookie banner hiding. Pay only for successful outputs.

- Apify Store: [https://apify.com/tidytools/website-screenshot-pdf-markdown](https://apify.com/tidytools/website-screenshot-pdf-markdown)
- Actor ID: `tidytools/website-screenshot-pdf-markdown` (`aHKoTOLGnFnzHgHPI`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-screenshot-pdf-markdown`

## Use case

Give it a list of URLs and get back, for every page:

- 📸 **Screenshot**: viewport, full-page or **one element only** (e.g. a pricing table or chart), PNG / JPEG / WebP, desktop, laptop, tablet or mobile, retina (2x/3x) and dark mode
- 📄 **PDF**: print-ready A4 / Letter / Legal, portrait or landscape, with backgrounds
- 📝 **Markdown**: clean, LLM-ready text of the page, without navigation, headers and footers by default, optionally limited to one part of it (e.g. `article`)

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

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://stripe.com",
    "finalUrl": "https://stripe.com/",
    "httpStatus": 200,
    "title": "Stripe | Financial Infrastructure to Grow Your Revenue",
    "success": true,
    "inputIndex": 0,
    "inputUrl": "stripe.com",
    "variant": "mobile",
    "device": "mobile",
    "viewportWidth": 390,
    "viewportHeight": 844,
    "pixelDensity": 3,
    "screenshotUrl": "https://api.apify.com/v2/key-value-stores/…/records/00000-stripe-com-screenshot-mobile.jpg",
    "screenshotBytes": 1255663,
    "screenshotTruncated": true,
    "format": "jpeg",
    "fullPage": true,
    "pdfUrl": null,
    "markdown": null,
    "scrolledPx": 16880,
    "hiddenElements": 5,
    "waitForSelectorTimedOut": true,
    "errors": {},
    "loadTimedOut": false,
    "cookieBannersHidden": 0,
    "capturedAt": "2026-09-29T02:01:42.003Z",
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
