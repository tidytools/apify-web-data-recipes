# Website Embeddings for RAG - Vector DB, Pinecone, Qdrant (available from 2026-10-09)

Crawl a site or docs, chunk the pages and get 1024-dim multilingual bge-m3 embeddings with stable IDs for Pinecone, Qdrant, pgvector or any vector database. No OpenAI key. From $0.20/1k chunks.

- Apify Store: `apify.com/tidytools/website-to-embeddings` (public from 2026-10-09)
- Actor ID: `tidytools/website-to-embeddings` (`69AbOL4uxESijjy3s`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-to-embeddings`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-09**. Until then the recipes below return an error.

## Use case

Website embeddings in one run: it crawls a website or documentation portal, converts every page to clean text, **splits it into chunks** and returns a **1024-dimension embedding for each chunk**, ready to load into Pinecone, Qdrant, Weaviate, Milvus, Chroma, pgvector or any other vector database. One run replaces a crawler, a chunker and an embedding API.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Page (fast mode) | $1.00 |
| Page (browser mode) | $2.50 |
| Embedded chunk | $0.20 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://docs.apify.com/academy/web-scraping-for-beginners"
  ],
  "maxPages": 5,
  "removeBoilerplate": true
}
```

## Sample output

From the Actor's documentation (section "Output: one item per chunk"):

```json
{
    "id": "28eedd07-a3b0-52a2-b015-079e3cec641e",
    "type": "chunk",
    "source": "web",
    "url": "https://docs.apify.com/academy/actor-marketing-playbook/actor-basics/actors-and-emojis",
    "startUrl": "https://docs.apify.com/academy/web-scraping-for-beginners",
    "title": "Actors and emojis | Academy | Apify Documentation",
    "chunkIndex": 1,
    "text": "…to explain things about Actors, and we want to avoid users needing to open extra tabs or pages. …",
    "headingPath": ["Actors and emojis", "On the use of emojis in Actors"],
    "charCount": 1188,
    "wordCount": 198,
    "description": "Discover how emojis can boost your Actors by grabbing attention, simplifying navigation, and enhancing clarity. …",
    "language": "en",
    "canonicalUrl": "https://docs.apify.com/academy/actor-marketing-playbook/actor-basics/actors-and-emojis",
    "contentHash": "0484f7301da3d86ade63f5a7c135edaabf9ad668",
    "pageContentHash": "7cd55fb178f0a9d85e9f240c141752dd40cfad33",
    "via": "backend",
    "crawledAt": "2026-09-29T02:16:40.384Z",
    "embedding": [0.0123, -0.0456, "… 1024 numbers …"],
    "dimensions": 1024,
    "model": "bge-m3",
    "charged": true
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
