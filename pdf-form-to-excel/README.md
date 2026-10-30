# PDF to Excel - PDF Form & Scanned Document Data to Rows

PDF to Excel for filled PDF forms, scanned receipts and printed reports: one aligned row per document or page with your column names, XLSX and CSV downloads. $0.01 per readable page; failed pages are free.

- Apify Store: [https://apify.com/tidytools/pdf-form-to-excel](https://apify.com/tidytools/pdf-form-to-excel)
- Actor ID: `tidytools/pdf-form-to-excel` (`r45HGEw0iesTsoLiv`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/pdf-form-to-excel`

## Use case

- `sources`: up to 500 direct public PDF, JPG, or PNG URLs. A repeated or invalid URL yields a free error row.
- `datasetId` and optional `datasetField`: read source URLs from an Apify Dataset. You can combine these with `sources`.
- `fields`: optional array of 1–50 exact column names. Every row uses these columns, with `null` for a missing value. Leave empty to let AI infer **one shared set** of columns from the first readable document. Output metadata names such as `pageNumber` and `chargedPages` are reserved.
- `oneRowPer`: `document` (default) or `page`.
- `maxPdfPages`: first 1–50 pages per PDF (default 20). Only readable pages are sent to extraction.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Extracted page | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "sources": [
    "https://filedone.ai/sample-files/sample-invoice.pdf"
  ],
  "fields": [
    "invoice_number",
    "total"
  ]
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/pdf-form-to-excel).

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
