# Website Email Finder - Fill Missing Company Emails

Fill missing Email cells in a company list that already has Website and Email columns. Read public company websites, keep source row IDs, and charge only sites where an email is found. No email verification or person lookup.

- Apify Store: [https://apify.com/tidytools/website-email-finder-crm](https://apify.com/tidytools/website-email-finder-crm)
- Actor ID: `tidytools/website-email-finder-crm` (`ARXGZVaVxl12jbt1v`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-email-finder-crm`

## Use case

Fill empty **Email** cells in a company list that already has **Website** and **Email** columns. This focused form uses the existing Website Email Extractor engine to read the public company websites you provide. It returns one Dataset row per source row by default, so you can match results back to your list. It does not find a person's email from a name or LinkedIn profile, and it does not verify deliverability.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Processed website | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "rows": [
    {
      "row_number": 1,
      "Website": "hofbraeuhaus.de",
      "Email": ""
    }
  ],
  "domains": []
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/website-email-finder-crm).

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
