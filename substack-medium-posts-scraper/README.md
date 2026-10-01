# Substack Scraper & Medium Scraper - Newsletter & Blog Posts (available from 2026-10-05)

Posts from Substack, Medium, Ghost, Beehiiv, WordPress or any RSS/Atom feed: title, author, date, text, tags, image. Date and keyword filters, new-post alerts, paywall-aware full text. $1/1k posts.

- Apify Store: `apify.com/tidytools/substack-medium-posts-scraper` (public from 2026-10-05)
- Actor ID: `tidytools/substack-medium-posts-scraper` (`qfs46BiUpvLnavTqe`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/substack-medium-posts-scraper`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-05**. Until then the recipes below return an error.

## Use case

It returns the **posts of any newsletter or blog** from its **public feed** (RSS, Atom or JSON Feed): Substack newsletters (also on custom domains), Medium authors, publications and tags, Ghost, Beehiiv, WordPress, Blogger, Hashnode or any site with a feed. Paste newsletter URLs, blog home pages, feed URLs or Medium handles; get one clean row per post. **No start fee, no login**: $1 per 1,000 posts, so small jobs and daily newsletter monitoring stay cheap.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Post | $1.00 |
| Full text from the post page | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "sources": [
    "https://www.lennysnewsletter.com",
    "https://medium.com/@karpathy",
    "https://www.platformer.news"
  ],
  "maxPostsPerSource": 5
}
```

## Sample output

From the Actor's documentation (section "Output example: post (Substack, free)"):

```json
{
    "type": "post",
    "input": "https://www.lennysnewsletter.com",
    "source": "Lenny's Newsletter",
    "sourceUrl": "https://www.lennysnewsletter.com",
    "feedUrl": "https://www.lennysnewsletter.com/feed",
    "platform": "substack",
    "title": "All of the Lenny & Friends Summit talks are now online!",
    "subtitle": "Plus, some reflections and takeaways from the day",
    "url": "https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit",
    "author": "Lenny Rachitsky",
    "publishedAt": "2026-09-29T13:15:57.000Z",
    "excerpt": "Plus, some reflections and takeaways from the day",
    "text": "👋 Hey there, I’m Lenny. Each week, I share deeply researched product, growth, and career advice. …",
    "wordCount": 1275,
    "readingTimeMinutes": 5,
    "postWordCount": 1276,
    "textComplete": true,
    "textSource": "feed",
    "paywalled": false,
    "audience": "everyone",
    "likes": 250,
    "restacks": 3,
    "substackPostType": "newsletter",
    "imageUrl": "https://substack-post-media.s3.amazonaws.com/public/images/9fed347c-0e02-4190-a590-1236719b99de_9213x6142.jpeg",
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
