# News Scraper - Keyword News Search & Monitoring API

Search 250+ news publishers by keyword in one run: headline, link, time, publisher, description, keywords. Country, language and topic filters, your own sites and feeds, duplicate stories collapsed, only-new alerts. $1 per 1,000 articles.

- Apify Store: [https://apify.com/tidytools/news-scraper](https://apify.com/tidytools/news-scraper)
- Actor ID: `tidytools/news-scraper` (`c8LZvugrqlfaTaBDe`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/news-scraper`

## Use case

**Enter keywords (and optionally countries, languages, topics or your own sites), get one row per news article with headline, link, publisher, time and the publisher's own description and keywords, at $1 per 1,000 articles.** Article page details cost $0.50 per 1,000 and are optional. Filtered-out articles, duplicate stories, articles returned by earlier runs, unreadable sources and invalid inputs are free. No start fee.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Article | $1.00 |
| Article details | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "keywords": [
    "OpenAI OR Anthropic",
    "\"electric vehicle\" battery -recall"
  ],
  "languages": [
    "en"
  ],
  "maxArticles": 50
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "article",
    "rank": 3,
    "title": "Former Anthropic security leader warns AI agents are becoming too autonomous for humans to keep them in check",
    "url": "https://www.foxnews.com/tech/former-anthropic-security-leader-warns-ai-agents-becoming-too-autonomous-humans-keep-check",
    "publisher": "Fox News",
    "sourceDomain": "foxnews.com",
    "publishedAt": "2026-10-03T17:26:10.000Z",
    "country": "US",
    "language": "en",
    "topics": ["general", "politics"],
    "matchedQueries": ["OpenAI OR Anthropic"],
    "matchedInTitle": true,
    "description": "Jeffrey Ladish, a former Anthropic security team member, warns AI agents are colluding and hacking with no reliable solution to keep them in check.",
    "keywords": [],
    "categories": ["Fox News", "fox-news/tech/artificial-intelligence", "fox-news/politics", "fox-news/tech"],
    "author": null,
    "imageUrl": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2026/10/931/523/jeffrey-ladish.jpg?ve=1&tl=1",
    "foundVia": ["news-sitemap", "feed"],
    "alsoPublishedBy": [],
    "success": true,
    "charged": true,
    "scrapedAt": "2026-10-03T19:02:11.000Z"
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
