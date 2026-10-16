# Telegram Channel Scraper - Public Posts, Views & Reactions

Scrape public Telegram channels without login or API keys: post text, date, views, reactions, photos and videos, links, hashtags, forwards and replies, plus channel subscribers. Date and keyword filters, new-post monitoring. $1 per 1,000 posts; failed channels are free.

- Apify Store: [https://apify.com/tidytools/telegram-channel-scraper](https://apify.com/tidytools/telegram-channel-scraper)
- Actor ID: `tidytools/telegram-channel-scraper` (`VaQRGy2pRk3siLAbs`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/telegram-channel-scraper`

## Use case

**Paste public Telegram channels (t.me/name or @name), get one row per post (text, date, views, reactions, media links, forwards, polls) and one profile row per channel, at $1 per 1,000 posts and $1 per 1,000 channels, with no start fee.** Missing channels, filtered posts and duplicates are free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Post | $1.00 |
| Channel info | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "channels": [
    "https://t.me/telegram"
  ],
  "maxPostsPerChannel": 20
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "post",
    "channel": "whale_alert_io",
    "channelTitle": "Whale Alert",
    "postId": 103692,
    "url": "https://t.me/whale_alert_io/103692",
    "date": "2026-10-03T14:07:56+00:00",
    "text": "🚨 🚨 🚨  20,000 $ETH (53,573,068 USD) transferred from #Bitfinex to #Aave\nDetails",
    "views": 1120,
    "viewsText": "1.12K",
    "reactionCount": null,
    "mediaTypes": [],
    "links": ["https://whale-alert.io/transaction/ethereum/0x6193864a7b6eb0070fb3929666545feb1b842049d10ff6b6668a1566c36e27fb"],
    "hashtags": ["#Bitfinex", "#Aave"],
    "forwardedFrom": null,
    "replyTo": null,
    "isEdited": false,
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
