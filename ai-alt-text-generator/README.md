# AI Alt Text Generator - Image Alt Text & Image Captions (available from 2026-10-06)

Find images missing alt text on pages, a sitemap or a whole site and write AI alt text in any language. Optional SEO title, caption and file name. WCAG accessibility, image SEO. $4/1,000.

- Apify Store: `apify.com/tidytools/ai-alt-text-generator` (public from 2026-10-06)
- Actor ID: `tidytools/ai-alt-text-generator` (`libCpYWq57jwvqqXR`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-alt-text-generator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-06**. Until then the recipes below return an error.

## Use case

It finds the **images on your web pages, or across your whole site, that have no alt text** and writes **concise, descriptive alt text with AI**, in the language you choose. Better accessibility (WCAG 1.1.1 "Non-text Content") for screen-reader users and better **image SEO**, without writing hundreds of descriptions by hand. Free extras: pixel size, format and file-size checks for every image, and a quality check of existing alt text.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Described image | $4.00 |
| Described image with SEO fields | $6.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urlsText": "https://www.apple.com",
  "maxImagesPerPage": 10,
  "maxImages": 20
}
```

## Sample output

From the Actor's documentation (section "Output example: existing alt audit (real results from books.toscrape.com)"):

```json
{
    "pageUrl": "https://books.toscrape.com/",
    "imageUrl": "https://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
    "existingAlt": "A Light in the Attic",
    "pageCount": 3,
    "success": true,
    "missingAlt": false,
    "suggestedAlt": "Black and white book cover with drawing of child's face and house on head, titled \"A Light in the Attic\" by Shel Silverstein.",
    "altQuality": "good",
    "altIssues": [],
    "imageBytes": 9876,
    "imageFormat": "jpeg",
    "imageWidth": 125,
    "imageHeight": 155,
    "oversized": false,
    "nextGenFormat": false
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
