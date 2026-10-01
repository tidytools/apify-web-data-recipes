# PDF Text Extractor & PDF to Markdown - OCR, Word, Excel

Document parser and PDF parser for LLMs: convert PDF, Word (DOCX/DOC), PowerPoint, Excel and CSV to clean Markdown text. PDF OCR for scanned files, RAG chunks. URLs, uploads, base64. $2/1,000 docs.

- Apify Store: [https://apify.com/tidytools/document-to-markdown](https://apify.com/tidytools/document-to-markdown)
- Actor ID: `tidytools/document-to-markdown` (`3O5uaRFA9cfTdEzNn`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/document-to-markdown`

## Use case

Give it documents (links, an uploaded file, or base64 from your code) and get back **clean Markdown text** for each one: ready for ChatGPT / Claude prompts, vector databases, RAG pipelines, search indexes or content migration.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Converted document | $2.00 |
| OCR page | $5.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://arxiv.org/pdf/1706.03762"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view",
    "resolvedUrl": "https://drive.google.com/uc?export=download&id=0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx&confirm=t",
    "source": "url",
    "finalUrl": "https://drive.usercontent.google.com/download?id=0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx&export=download",
    "fileName": "Sample.pdf",
    "contentType": "application/pdf",
    "bytes": 23567,
    "title": "Preface",
    "pageCount": 8,
    "author": "Loren",
    "createdAt": "2010-08-26T10:15:07-05:00",
    "producer": "Acrobat Distiller 9.3.3 (Windows)",
    "success": true,
    "status": "success",
    "needsOcr": false,
    "via": "direct",
    "characters": 13129,
    "wordCount": 2274,
    "markdown": "# Sample.pdf\n\n## Contents\n### Page 1\n…",
    "convertedAt": "2026-09-29T02:26:12.454Z"
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
