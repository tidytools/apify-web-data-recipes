# Scanned PDF to Word - OCR PDF to DOCX, Photos & Handwriting

Scanned PDF to Word: convert public scanned PDF or handwriting photo URLs into one editable Word DOCX per file, with headings, paragraphs and simple tables, plus one Dataset row per page. $0.003 per page with text; blank and failed pages are free.

- Apify Store: [https://apify.com/tidytools/scanned-docs-to-word](https://apify.com/tidytools/scanned-docs-to-word)
- Actor ID: `tidytools/scanned-docs-to-word` (`Jg0vSEdo9uaUlWXfK`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/scanned-docs-to-word`

## Use case

Paste a public scanned PDF or document-photo URL. This Actor reads each page with the existing TidyTools OCR backend, builds **one editable Word file per source**, and returns one Dataset row per page. Headings, paragraphs, bullet lists and complete simple Markdown tables become Word elements. Each page is a Word section. The original visual layout, images and complex tables are not reconstructed.

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
{"sourceUrl":"https://filedone.ai/sample-files/sample-scanned-report-3-pages.pdf","pageNumber":1,"pageCount":3,"text":"# Report","success":true,"charged":true,"documentKey":"DOCUMENT_001.docx","documentUrl":"https://api.apify.com/v2/key-value-stores/<store-id>/records/DOCUMENT_001.docx"}
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
