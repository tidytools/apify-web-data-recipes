# Website Contact Extractor — Bulk Company Domains

Extract public company website emails, phone numbers and social links from bulk domain lists or a source dataset. One site result by default; $0.002 per site with a contact, free when none is found.

- Apify Store: [https://apify.com/tidytools/website-contact-extractor-bulk](https://apify.com/tidytools/website-contact-extractor-bulk)
- Actor ID: `tidytools/website-contact-extractor-bulk` (`YFFurB9PsbH0GAj7E`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-contact-extractor-bulk`

## Use case

Paste a list of public company websites or domains, or select a dataset that contains their websites. The Actor reads each site and returns its best email, phone number and social profiles. The default `sites` output keeps one result per source website or row. It does not log in, crawl LinkedIn people, or discover companies from a directory.

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
    "katzsdelicatessen.com",
    "hofbraeuhaus.de"
  ]
}
```

## Sample output

See the output examples on the [Store page](https://apify.com/tidytools/website-contact-extractor-bulk).

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
