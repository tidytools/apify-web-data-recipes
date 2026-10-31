# AI Image Upscaler - Bulk Photos and TSV to 2x or 4x

Upscale public photo and product image URLs by 2x or 4x. Paste a list or spreadsheet TSV; get downloadable JPEG/WebP per source row. Failed rows are free.

- Apify Store: [https://apify.com/tidytools/ai-image-upscaler](https://apify.com/tidytools/ai-image-upscaler)
- Actor ID: `tidytools/ai-image-upscaler` (`KVe7e6f1rYK3S2uB4`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-image-upscaler`

## Use case

Upscale public photos and product images 2× or 4×, one result or free error per source row.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Upscaled image | $10.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "imageUrls": [
    "https://images.unsplash.com/photo-1500534623283-312aade485b7?w=250&fm=webp"
  ],
  "scale": 4,
  "format": "webp"
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
[
  {"sourceId":"tsv:2","input":"https://www.gstatic.com/webp/gallery/1.jpg","sourceLine":2,"sourceRow":{"sku":"A-01","imageUrl":"https://www.gstatic.com/webp/gallery/1.jpg","note":"front"},"outputUrl":"<run-kv-url>","outputKey":"<output-key>","width":1280,"height":960,"bytes":123456,"success":true,"resultStored":true,"chargeEligible":true,"durationMs":1500},
  {"sourceId":"tsv:3","input":"not-a-url","sourceLine":3,"sourceRow":{"sku":"A-02","imageUrl":"not-a-url","note":"bad cell"},"success":false,"errorType":"invalid_url","error":"invalid_url","resultStored":false,"chargeEligible":false,"durationMs":0}
]
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
