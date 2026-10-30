# Invoice Parser & Receipt Parser - Invoice OCR to JSON/CSV

Invoice parser and receipt parser for public PDF, JPG and PNG URLs. Invoice OCR returns supplier, invoice number, date, currency, subtotal, tax, total and line items as JSON, one row per document; export CSV for Excel. $0.01 per readable page; unreadable documents are free.

- Apify Store: [https://apify.com/tidytools/invoice-receipt-parser](https://apify.com/tidytools/invoice-receipt-parser)
- Actor ID: `tidytools/invoice-receipt-parser` (`YDGmNa4fnOX8ZiCWG`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/invoice-receipt-parser`

## Use case

Read public invoice or receipt PDF, JPG and PNG URLs into structured header fields and an item array. Paste a document URL, choose **invoice** (default) or **receipt**, then export the Dataset as JSON or CSV; Excel can open the CSV.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Extracted page | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://filedone.ai/sample-files/sample-invoice.pdf"
  ],
  "fields": {}
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"url":"https://example.org/invoice.pdf","success":true,"charged":true,"supplier":"Example Ltd","invoice_number":"INV-1","date":"2026-10-01","currency":"USD","subtotal":100,"tax":10,"total":110,"line_items":"[{\"description\":\"Service\",\"quantity\":1,\"unit_price\":100,\"amount\":100}]","documentPagesRead":1}
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
