# Image to Text OCR API - Extract Text from Images with AI (available from 2026-10-03)

Extract text from images with AI OCR: receipts, screenshots, signs, document photos and tables as Markdown, in English, Chinese, Japanese and more. URLs, a dataset or base64. $3/1,000 images.

- Apify Store: `apify.com/tidytools/image-to-text-ocr` (public from 2026-10-03)
- Actor ID: `tidytools/image-to-text-ocr` (`DuFFQzZueyf7cBjft`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/image-to-text-ocr`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-03**. Until then the recipes below return an error.

## Use case

Give it images and get their text back:

- 🧾 **Receipts, invoices and photos of documents**: line items and totals, in reading order
- 🖥️ **Screenshots**: terminal output, app screens, web pages
- 🪧 **Signs and labels** in photos
- 🌏 **Many languages and scripts**: English, German, Dutch..., Chinese, Japanese, Korean; the text stays in its original language (nothing is translated)
- 📊 **Tables**: kept as Markdown tables in *Markdown* mode, or as one line per row in *Plain text* mode

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
    "https://upload.wikimedia.org/wikipedia/commons/6/67/Japanese_Road_Sign_119_%28Street_name%29.jpg",
    "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b3/Sahan_Supermarket_receipt%2C_Hillegersberg%2C_Rotterdam_%282021%29_02.jpg/1280px-Sahan_Supermarket_receipt%2C_Hillegersberg%2C_Rotterdam_%282021%29_02.jpg"
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
