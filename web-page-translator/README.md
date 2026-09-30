# AI Translator - Bulk Translate Text, JSON, Subtitles & Pages (available from 2026-10-04)

Translate texts, JSON and datasets, SRT/VTT subtitles and web pages into many languages at once. Glossary, tone, Markdown kept. A Google Translate / DeepL alternative, no API key. $1.50/1M chars.

- Apify Store: [https://apify.com/tidytools/web-page-translator](https://apify.com/tidytools/web-page-translator)
- Actor ID: `tidytools/web-page-translator` (`Z8R6afk16yObrJais`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/web-page-translator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-04**. Until then the recipes below return an error.

## Use case

A **bulk text & JSON translator** and web page translator in one: it translates **web pages, your own texts, JSON items or another Actor's dataset into one or many languages** with AI, and keeps the **Markdown structure intact**: headings, lists, tables, bold/italic, links (targets unchanged) and code blocks (not translated). A Google Translate / DeepL alternative with no API key.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| 1,000 source characters | $1.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urlsText": "https://docs.apify.com/academy/web-scraping-for-beginners",
  "targetLanguage": "Spanish"
}
```

## Sample output

From the Actor's documentation (section "Input example: texts into two languages"):

```json
[
    { "source": "text-0", "success": true, "targetLanguage": "Spanish", "sourceCharacters": 32, "translatedMarkdown": "Envío gratuito en pedidos superiores a $50" },
    { "source": "text-0", "success": true, "targetLanguage": "Japanese", "sourceCharacters": 32, "translatedMarkdown": "$50を超える注文には無料配送" },
    { "source": "text-1", "success": true, "targetLanguage": "Spanish", "sourceCharacters": 11, "translatedMarkdown": "Agregar al carrito" },
    { "source": "text-1", "success": true, "targetLanguage": "Japanese", "sourceCharacters": 11, "translatedMarkdown": "カートに追加" }
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
