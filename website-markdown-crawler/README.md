# Website Content Crawler - Website to Markdown for LLM & RAG

Markdown crawler for AI: crawl a website or docs site into clean, LLM-ready Markdown (URL to Markdown, HTML to Markdown) with RAG chunks. Sitemaps, JavaScript pages, linked PDFs and Word. $1/1k pages.

- Apify Store: [https://apify.com/tidytools/website-markdown-crawler](https://apify.com/tidytools/website-markdown-crawler)
- Actor ID: `tidytools/website-markdown-crawler` (`TpZrf66Jvgs26hMby`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-markdown-crawler`

## Use case

Website content crawler for AI: it crawls a docs site, help center, blog or knowledge base into **clean, LLM-ready Markdown** for RAG pipelines, vector databases and ChatGPT / Claude context. In our 5-site test, each 25-page site took **3–34 seconds**, where Website Content Crawler's default settings took 56–200 seconds, and this Actor kept **at least 97% of the sampled body paragraphs on every site**. On a Next.js docs site and an Intercom help center, WCC's defaults kept 0% and 34% ([method and raw data](https://github.com/tidytools/apify-web-data-recipes/tree/main/benchmarks/markdown-vs-wcc)). **$1 per 1,000 pages**, no start fee, failed pages free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Page (fast mode) | $1.00 |
| Page (browser mode) | $2.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://docs.apify.com/academy"
  ],
  "removeBoilerplate": true
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://docs.apify.com/academy/actor-marketing-playbook/actor-basics/actor-description",
    "finalUrl": "https://docs.apify.com/academy/actor-marketing-playbook/actor-basics/actor-description",
    "startUrl": "https://docs.apify.com/academy",
    "title": "Actor description & SEO description | Academy | Apify Documentation",
    "depth": 0,
    "httpStatus": 200,
    "contentType": "text/html; charset=utf-8",
    "mode": "fast",
    "via": "backend",
    "success": true,
    "charged": true,
    "description": "Learn about Actor description and meta description. Where to set them and best practices for both content and length.",
    "language": "en",
    "canonicalUrl": "https://docs.apify.com/academy/actor-marketing-playbook/actor-basics/actor-description",
    "wordCount": 1205,
    "foundIn": "sitemap",
    "markdown": "# Actor description & SEO description\n\nCopy for LLM\n\nLearn about Actor description and meta description. …\n\n## What is an Actor description?\n\n…",
    "text": "Actor description & SEO description\n\nCopy for LLM\n\nLearn about Actor description and meta description. …",
    "chunks": [
        { "index": 1, "text": "… ### Is there any benefit in the description and meta description being different?\n\n…", "headingPath": ["Actor description & SEO description", "Regular description vs. SEO description", "Is there any benefit in the description and meta description being different?"], "charCount": 1850 }
    ],
    "crawledAt": "2026-09-29T03:56:19.278Z"
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
