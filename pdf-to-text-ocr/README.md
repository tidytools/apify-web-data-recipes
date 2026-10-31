# PDF to Text OCR — Scanned PDFs to Text & Markdown

Convert public scanned PDF links to text or Markdown, one row per page by default. Text-bearing pages cost $0.003 each; blank and failed pages are free. Select page ranges or combine a PDF into one result row.

- Apify Store: [https://apify.com/tidytools/pdf-to-text-ocr](https://apify.com/tidytools/pdf-to-text-ocr)
- Actor ID: `tidytools/pdf-to-text-ocr` (`nictrJI3c872MHvUn`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/pdf-to-text-ocr`

## Use case

Paste a public scanned PDF URL (or a Google Drive, Dropbox or OneDrive share link) and get **one Dataset row per page** with its text or Markdown. This edition targets scanned PDFs and image-only pages for page-by-page OCR through the existing `image-ocr` engine and `image-ocr` billing event. `document-to-markdown` primarily converts text-based documents to Markdown. Each page with text uses one existing `image-ocr` event: **$0.003 per page on the Free plan**. Blank pages and failures are free. The default limit is **50 selected pages per PDF**; you can change it up to 500. PDFs must be **15 MB or less**. Password-protected or oversized PDFs return a free error row. Searchable PDFs also work: their text layer is read directly when available, while scanned pages use OCR. Markdown may keep simple tables, but original page layout is not preserved.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Image transcribed | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://filedone.ai/sample-files/sample-scanned-report-3-pages.pdf"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{"pdfUrl":"https://filedone.ai/sample-files/sample-scanned-report-3-pages.pdf","pageNumber":1,"pdfPageCount":3,"text":"# Larkfield Community Library\nAnnual report ...","charCount":47,"success":true,"charged":true,"route":"pdf-ocr"}
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
