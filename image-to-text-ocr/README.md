# OCR API - Image to Text, Photo to Text & Receipt OCR

Bulk image OCR and photo to text for receipts, screenshots and document photos. Extract text from image URLs, datasets or base64 as plain text or Markdown; optional receipt fields and table rows. $0.003 per image with text on Free and Bronze; no-text and failed results are free.

- Apify Store: [https://apify.com/tidytools/image-to-text-ocr](https://apify.com/tidytools/image-to-text-ocr)
- Actor ID: `tidytools/image-to-text-ocr` (`DuFFQzZueyf7cBjft`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/image-to-text-ocr`

## Use case

Choose **Receipt / invoice fields** (`"mode":"receipt_fields"`) for an image of a receipt or invoice. The dataset row keeps the full OCR `text` and adds `receipt: {vendor, date, total, currency, review}`. For example, an image transcribed as `Vendor: ACME SUPPLIES\nInvoice Date: 2026-10-18\nTotal: USD 105.00` yields `{"vendor":"ACME SUPPLIES","date":"2026-10-18","total":105,"currency":"USD","review":false}`. Only explicit labels are used; an unlabeled shop name is not guessed, and `Subtotal`, `Tax` and `Invoice No` are not extracted as the total or vendor. Taiwan invoices: `發票日期`/`日期` (Gregorian dates such as `2024-07-16`, `2024/7/16` or `2024年7月16日`) and `總計`/`應付總額` are read, with `新臺幣`, `NT$` or `TWD` as currency `TWD`; for example `發票日期：2024-07-16\n總計：NT$945` yields `"date":"2024-07-16","total":945,"currency":"TWD"`. `小計`, `營業稅`/`稅額` and `發票號碼` are never the total; ROC-year dates (`113/07/16`), a bare `$` or `元` and two different totals give `null` or `review:true`. Brazilian receipts (NFC-e, nota fiscal): `Data de emissão`/`Emissão` and `Valor a Pagar`/`Valor total` are read, with `R$` or `BRL` as currency `BRL`; when both totals are printed, `Valor a Pagar` (after discounts) is the total, so `Data de emissão: 28/10/2026\nValor total R$ 138,74\nValor a Pagar R$ 130,74` yields `"date":"2026-10-28","total":130.74,"currency":"BRL"`. Spanish receipts and facturas: `Fecha`/`Fecha de emisión` and `Total`/`Importe total`, with `€` or `EUR`; `Fecha: 28/10/2026\nTotal: 24,50 €` yields `"date":"2026-10-28","total":24.5,"currency":"EUR"`. Day-first dates (`28/10/2026`) and decimal commas (`130,74`, `1.234,56`) are read only next to these Brazilian and Spanish labels. `Valor total dos tributos`, `Desconto`, `IVA`, `Subtotal`, due dates and a bare `$` (never taken as reais) are not used; two different amounts with the same label rank give `review:true`. Missing or ambiguous values are `null`, with `review:true` when the date, total or currency needs checking. Even `review:false` is not an accuracy guarantee: check fields against the source image before accounting use.

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
