# RAG Web Browser - Web Search to Markdown for AI

Search the web (DuckDuckGo, Bing) and read the top pages as Markdown for LLMs and RAG, or read a list of URLs. Searching is free; blocked pages are free.

- Apify Store: [https://apify.com/tidytools/rag-web-browser](https://apify.com/tidytools/rag-web-browser)
- Actor ID: `tidytools/rag-web-browser` (`fKOhB9ri7Mo9XsfqC`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/rag-web-browser`

## Use case

Search the web and return up to 1–10 readable results as clean Markdown for LLMs, AI agents and RAG pipelines, or read a list of URLs. Search result pages are rendered in a real Chrome (DuckDuckGo first, then Bing) and parsed into ranked results; each candidate page is then read with the TidyTools Smart Fetch backend. Searching is free: you pay only for pages returned as Markdown.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Page | $1.30 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "query": "best open source vector database"
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{"url":"https://realpython.com/async-io-python/","title":"Python's asyncio: A Hands-On Walkthrough – Real Python","rank":1,"engine":"duckduckgo",
 "searchResult":{"rank":1,"title":"Python's asyncio: A Hands-On Walkthrough – Real Python","snippet":"Python's asyncio library enables you to write concurrent code …","engine":"duckduckgo"},
 "markdown":"# Python's asyncio: A Hands-On Walkthrough …","fetchedAt":"2026-10-22T05:52:10.000Z","success":true,"charged":null,"chargedEvents":null}
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
