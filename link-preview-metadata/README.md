# Link Preview API - Open Graph, Meta Tags & URL Metadata (available from 2026-10-08)

Get title, description, preview image, favicon, site name, author, dates and Open Graph / Twitter tags for any list of URLs. JavaScript pages too. $1 per 1,000 URLs.

- Apify Store: `apify.com/tidytools/link-preview-metadata` (public from 2026-10-08)
- Actor ID: `tidytools/link-preview-metadata` (`ACySefAmKCzI7W4KG`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/link-preview-metadata`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-08**. Until then the recipes below return an error.

## Use case

Give it URLs (as many as you like, in one run) and get the information you need to show a **rich link preview** or to catalogue pages:

- 🏷️ **Title and description** (Open Graph first, then Twitter Card tags, then the HTML title and meta description)
- 🖼️ **Preview image** (`og:image` / `twitter:image`, then schema.org JSON-LD) as an absolute URL
- 🌐 **Site name, page type, favicon, language, theme color, charset**
- ✍️ **Author, published and modified time, publisher and logo**, with a **JSON-LD fallback** when Open Graph tags are missing, and a `sources` object that says where each value came from (`og`, `twitter`, `html` or `jsonld`)
- 👥 **Social profiles**: Facebook, X, LinkedIn, Instagram, YouTube, TikTok, GitHub, Pinterest, Threads, Trustpilot and Discord links found on the page (share buttons and posts are ignored)
- 📰 **RSS/Atom feeds, oEmbed endpoint, web app manifest, all icons** (with sizes) and **email addresses** (`mailto:` links)
- 🔗 **Canonical URL, keywords, Twitter card type, JSON-LD types**, and optionally the raw JSON-LD
- 📦 **All Open Graph and Twitter tags** in one object

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| URL preview | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urlList": [
    "https://github.com/apify/crawlee",
    "https://www.bbc.com/news"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real result, September 2026)"):

```json
{
    "input": "https://www.theverge.com/tech/1001797/nothings-headphone-1-pro-review",
    "inputUrl": "https://www.theverge.com/tech/1001797/nothings-headphone-1-pro-review",
    "inputIndex": 0,
    "url": "https://www.theverge.com/tech/1001797/nothings-headphone-1-pro-review",
    "success": true,
    "title": "The Nothing Headphone 1 Pro put you in the studio",
    "description": "Nothing’s new flagship headphones surprised me.",
    "image": "https://platform.theverge.com/wp-content/uploads/sites/2/2026/09/268785_Nothing_pro_1_headphones_JHIGGINS_1.jpg?quality=90&strip=all&...",
    "siteName": "The Verge",
    "type": "article",
    "author": "John Higgins",
    "publishedTime": "2026-09-29T01:00:00+00:00",
    "modifiedTime": "2026-09-29T01:00:00+00:00",
    "publisher": "The Verge",
    "logo": "https://platform.theverge.com/wp-content/uploads/sites/2/2025/01/verge-placeholder_f212b3.png?...",
    "lang": "en-US",
    "twitterCard": "summary_large_image",
    "structuredDataTypes": ["NewsArticle", "BreadcrumbList"],
    "socialProfiles": {
        "tiktok": "https://www.tiktok.com/@verge",
        "youtube": "https://www.youtube.com/theverge",
        "instagram": "https://www.instagram.com/verge",
        "facebook": "https://www.facebook.com/verge",
        "threads": "https://www.threads.net/@verge",
        "x": "https://x.com/verge"
    },
    "feeds": [{ "url": "https://www.theverge.com/rss/index.xml", "type": "application/rss+xml", "title": "The Verge" }],
    "oembedUrl": null,
    "icons": [{ "href": "https://www.theverge.com/static-assets/icons/apple-touch-icon.png", "rel": "apple-touch-icon", "sizes": "180x180" }, "..."],
    "charset": "utf-8",
    "emails": [],
    "sources": { "title": "og", "description": "og", "image": "og", "author": "html", "publishedTime": "jsonld", "modifiedTime": "jsonld", "siteName": "og", "publisher": "jsonld", "logo": "jsonld" },
    "httpStatus": 200,
    "mode": "fast",
    "via": "backend",
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
