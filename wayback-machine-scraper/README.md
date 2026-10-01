# Wayback Machine Scraper - Archived URLs & Website History (available from 2026-10-12)

Internet Archive Wayback Machine data: every archived URL of a website, a page's versions over time, the closest snapshot per URL, site history and old page content as Markdown. $1/1,000 rows.

- Apify Store: `apify.com/tidytools/wayback-machine-scraper` (public from 2026-10-12)
- Actor ID: `tidytools/wayback-machine-scraper` (`3TEyg9Aw7AqXgERUM`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/wayback-machine-scraper`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-12**. Until then the recipes below return an error.

## Use case

It reads the **Internet Archive's Wayback Machine** for any list of websites or pages and returns clean rows you can filter, export or feed to other tools. Four modes:

- 🗂️ **Archived URLs of a site**: every page the Wayback Machine has ever captured for a domain, a host or a path (e.g. `example.com/blog/`), with the first capture date and snapshot links. Find deleted pages, old URLs for redirect maps after a site migration, or content to recover
- 🕰️ **Snapshots of a page over time**: every archived version of one page. By default **only captures where the content changed** (one row per version), or at most one per day, month or year
- 🎯 **Closest snapshot per URL**: the snapshot nearest to a date, or the latest one. Paste a list of dead links and get a working archive link for each
- 📈 **Site history summary**: one row per domain or page with first and last capture, the last month (and day) with a real page (HTTP 200), months that only redirected, captures per year, number of content versions and the longest gap without captures. Useful before buying an expired domain or when researching a company's past
- 📝 **Optional page content**: in Snapshots and Closest modes, each archived page can be downloaded and returned as **clean Markdown** (or plain text), ready for an LLM, a diff or a report
- 🧹 **Clean, de-duplicated rows**: `http://example.com:80/a/` and `https://www.example.com/a` count once; malformed index entries are skipped; the same fields on every row
- 🤝 **Polite by design**: all requests share one rate limit (default one index query per second, page downloads every 2 seconds), with automatic back-off when the Internet Archive is busy
- 💵 **$1 per 1,000 rows** ($0.001 per archived URL or snapshot). No start fee. Inputs that were never archived are free

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Archived URL or snapshot | $1.00 |
| Site history summary | $3.00 |
| Archived page content | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "apify.com"
  ],
  "maxResultsPerInput": 50
}
```

## Sample output

From the Actor's documentation (section "Output example: archived URL (Archived URLs mode)"):

```json
{
  "type": "url",
  "input": "python.org",
  "success": true,
  "url": "http://www.python.org/1.5/",
  "host": "www.python.org",
  "path": "/1.5/",
  "extension": null,
  "firstCapturedAt": "1998-01-19T01:50:21Z",
  "statusCode": 200,
  "mimeType": "text/html",
  "firstSnapshotUrl": "https://web.archive.org/web/19980119015021/http://www.python.org:80/1.5/",
  "latestSnapshotUrl": "https://web.archive.org/web/http://www.python.org/1.5/",
  "timestamp": "19980119015021",
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
