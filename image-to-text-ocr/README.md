# Image to Text OCR API - Extract Text from Images with AI

Extract text from images in bulk with AI OCR: receipts, screenshots, signs, document photos and tables as Markdown, in English, Chinese, Japanese and more. Use URLs, datasets or base64. No-text and failed results are free; no start fee.

- Apify Store: [https://apify.com/tidytools/image-to-text-ocr](https://apify.com/tidytools/image-to-text-ocr)
- Actor ID: `tidytools/image-to-text-ocr` (`DuFFQzZueyf7cBjft`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/image-to-text-ocr`

## Use case

Choose **Receipt / invoice fields** (`"mode":"receipt_fields"`) for an image of a receipt or invoice. The dataset row keeps the full OCR `text` and adds `receipt: {vendor, date, total, currency, review}`. For example, an image transcribed as `Vendor: ACME SUPPLIES\nInvoice Date: 2026-10-18\nTotal: USD 105.00` yields `{"vendor":"ACME SUPPLIES","date":"2026-10-18","total":105,"currency":"USD","review":false}`. Only explicit labels are used; an unlabeled shop name is not guessed, and `Subtotal`, `Tax` and `Invoice No` are not extracted as the total or vendor. Missing or ambiguous values are `null`, with `review:true` when the date, total or currency needs checking. Even `review:false` is not an accuracy guarantee: check fields against the source image before accounting use.

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
    "https://upload.wikimedia.org/wikipedia/commons/6/67/Japanese_Road_Sign_119_%28Street_name%29.jpg"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output examples (real results, September 2026)"):

```json
{
    "imageUrl": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b3/Sahan_Supermarket_receipt%2C_Hillegersberg%2C_Rotterdam_%282021%29_02.jpg/1920px-...jpg",
    "success": true,
    "mode": "markdown",
    "text": "# SAHAN Supermarkt\nBergweg 170\n3036 BL Rotterdam\nTel: 010-265.33.99\n\n## KASSABON\n\nNummer 2-00005155\nDatum: 26/01/2021\nTime : 11.29\nCaissier Tuge\nKassa: 1\n\n| Omschrijving | Bedrag |\n|--------------|--------|\n| MIRAS OLijfoute (glas) 1L | 3,99 |\n| MERAY TRAKY A POMPOENPIT 200 | 1,99 |\n| PINAR POMPOENPITTEN 200G | 1,99 |\n| ULKER PETIBOR BISKUVI 1KG | 2,49 |\n| BROOD SIMIT * 5 x 0.75 | 3,75 |\n\nTOTAAL Incl: 14,21\nPIN Betaling 14,21\nTeruggave 0,00\nBTW Bedrag: 1,17\n\n6 Artikel / 9 Stuks\nD. uwel en tot ziens",
    "lineCount": 23,
    "charCount": 529,
    "language": "nl",
    "languageName": "Dutch",
    "imageFormat": "jpeg",
    "width": 1920,
    "height": 3413,
    "route": "image",
    "imageBytes": 2315283
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
