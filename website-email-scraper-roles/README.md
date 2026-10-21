# Website Email Scraper - Role Mailboxes from Domains

Scrape shared role mailboxes (info@, sales@, support@) from company websites and domain lists. One row per email with the page it was found on. Personal-looking addresses dropped; $2/1,000 sites with an email, others free.

- Apify Store: [https://apify.com/tidytools/website-email-scraper-roles](https://apify.com/tidytools/website-email-scraper-roles)
- Actor ID: `tidytools/website-email-scraper-roles` (`XoMGiATCsXyfI7N8z`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-email-scraper-roles`

## Use case

Get the shared company mailboxes (info@, sales@, support@, office@...) that businesses publish on their own public websites. Paste a list of company websites or domains into **Company websites or domains**; you get one Dataset row per mailbox with the domain, the mailbox type and the page it was found on, ready for a CRM or outreach import. The first-run form contains two public example sites; replace them with your own list.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Processed website | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "dauntbooks.co.uk",
    "hofbraeuhaus.de"
  ]
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/website-email-scraper-roles).

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
