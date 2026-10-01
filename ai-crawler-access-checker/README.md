# AI Crawler Checker - robots.txt Checker for GPTBot & AI Bots

Which AI bots can read a site? Bulk-check up to 10,000 domains for 26 AI crawlers (GPTBot, ClaudeBot, PerplexityBot...) in robots.txt: AI search score, fix snippet, Content Signals. $2/1k sites.

- Apify Store: [https://apify.com/tidytools/ai-crawler-access-checker](https://apify.com/tidytools/ai-crawler-access-checker)
- Actor ID: `tidytools/ai-crawler-access-checker` (`fHmxS3tQMVb1EfQBu`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/ai-crawler-access-checker`

## Use case

It tells you **which AI crawlers are allowed to read a website** according to its `robots.txt`, scores it, gives you a **ready-to-paste robots.txt fix**, and can **track changes week to week**. It also reads **Cloudflare Content Signals** (`Content-Signal: search=yes, ai-train=no`), and checks for an **llms.txt** file and `noai` directives. Check one site or **up to 10,000 domains per run for $2 per 1,000 sites**.

For a live benchmark of how popular sites treat these crawlers, see the [AI Crawler Index](https://tools.yukai.uk/ai-crawler-index) (1,005 sites, updated daily, CSV download).

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Checked website | $2.00 |
| Re-checked website (unchanged) | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "websites": [
    "https://www.nytimes.com",
    "python.org",
    "docs.anthropic.com"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real result, September 2026, shortened)"):

```json
{
    "site": "https://nytimes.com",
    "verdict": "Some AI search/assistant crawlers are blocked (OAI-SearchBot, Claude-SearchBot, PerplexityBot, meta-webindexer, DuckAssistBot, ChatGPT-User, Claude-User, Perplexity-User, meta-externalfetcher): the site may not appear in those AI answers.",
    "policy": "blocks-search",
    "aiSearchScore": 47,
    "aiAccessScore": 35,
    "blockedBots": ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "..."],
    "partialBots": ["Google-GeminiNotebook", "Google-Agent", "Applebot", "Amazonbot", "..."],
    "contentSignals": null,
    "recommendedRobotsSnippet": "# Allow AI search and assistant crawlers (they decide whether the site can appear in AI answers)\n# Also remove \"Disallow: /\" from the existing group(s) for: OAI-SearchBot, ChatGPT-User, ...\nUser-agent: OAI-SearchBot\nUser-agent: ChatGPT-User\n...\nAllow: /\nDisallow: /ads/\n...",
    "suggestedPolicy": "# AI model training crawlers: blocked (does not affect AI search answers)\nUser-agent: GPTBot\n...\nDisallow: /\n\n# AI search and assistant crawlers: allowed\nUser-agent: OAI-SearchBot\n...",
    "robotsTxt": { "status": 200, "found": true, "state": "found", "reason": null, "sitemaps": ["https://www.nytimes.com/sitemaps/new/news.xml.gz", "..."] },
    "llmsTxt": { "found": false, "url": "https://nytimes.com/llms.txt", "status": 404 },
    "noAiDirective": false,
    "comparison": {
        "status": "changed",
        "changedBots": [{ "bot": "MistralAI-User", "before": "allowed", "after": "partial" }],
        "llmsTxtChanged": false,
        "policyChanged": null,
        "previousCheckedAt": "2026-09-29T02:18:46.163Z"
    },
    "bots": [
        { "bot": "GPTBot", "company": "OpenAI", "purpose": "training", "status": "blocked", "allowedAll": false, "matchedGroup": "GPTBot",
          "paths": [{ "path": "/", "allowed": false, "rule": "Disallow: /" }] }
    ],
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
