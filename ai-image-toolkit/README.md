# Background Remover - Image Converter, Compressor & Resizer

Remove image backgrounds in bulk with AI (hair and fur kept): transparent PNG/WebP or any color, crop to subject. Plus resize, convert to WebP/AVIF/JPEG and compress.

- Apify Store: [https://apify.com/tidytools/ai-image-toolkit](https://apify.com/tidytools/ai-image-toolkit)
- Actor ID: `tidytools/ai-image-toolkit` (`w3p8rtI51QdMqjtKr`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-image-toolkit`

## Use case

**Paste image URLs, get back a download link for every result: background removed (transparent PNG/WebP or any color), resized, converted to WebP/AVIF/JPEG, or compressed. Background removal costs $0.005 per image, resize/convert/compress $0.002 per image (Free plan, no start fee). Failed images are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Background removed | $5.00 |
| Image resized, converted or compressed | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "imageUrls": [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Canon_EOS_5D_Mark_II_with_50mm_1.4_edit1.jpg/960px-Canon_EOS_5D_Mark_II_with_50mm_1.4_edit1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/960px-Cat03.jpg"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real run, 1 October 2026)"):

```json
{
    "index": 1,
    "input": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/960px-Cat03.jpg",
    "operation": "removeBackground",
    "success": true,
    "outputUrl": "https://api.apify.com/v2/key-value-stores/RHb9MvsFd3ZZkxU7c/records/0002-960px-Cat03-nobg.png?signature=…",
    "outputKey": "0002-960px-Cat03-nobg.png",
    "format": "png",
    "width": 960,
    "height": 959,
    "bytes": 983802,
    "transparent": true,
    "savedPercent": -554.6,
    "inputFormat": "jpeg",
    "inputWidth": 960,
    "inputHeight": 959,
    "inputBytes": 150302,
    "warnings": [],
    "via": "backend",
    "charged": true,
    "durationMs": 2834
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
