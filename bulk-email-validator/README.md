# Bulk Email Validator - MX, Disposable Email & Typo Check

Email list cleaner without SMTP pings: bulk-check syntax, domain and MX records, disposable email, role and free-provider flags, and typos (gmial.com → gmail.com). CSV upload or another Actor's dataset. Failed lines are free. $0.50 per 1,000.

- Apify Store: [https://apify.com/tidytools/bulk-email-validator](https://apify.com/tidytools/bulk-email-validator)
- Actor ID: `tidytools/bulk-email-validator` (`haMAC5lJnzZmQcyqh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/bulk-email-validator`

## Use case

**Email list cleaner** for lists you are about to send or import: give it a list, a CSV or the dataset of a lead scraper and get a verdict, score and reason per address, with no SMTP pings. **$0.50 per 1,000 addresses, no start fee, failed lines free**; the run stops at your maximum charge per run, and a restarted run never charges an address twice.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| E-mail validated | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "emails": [
    "jane.doe@gmail.com",
    "info@stripe.com",
    "sales@apify.com",
    "someone@gmial.com",
    "test@mailinator.com",
    "noreply@github.com",
    "user@example.com",
    "bad..address@gmail.com"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (from a CSV row, real run 1 October 2026)"):

```json
{
    "input": "jane@apify.com",
    "email": "jane@apify.com",
    "verdict": "valid",
    "score": 90,
    "reason": "domain accepts e-mail; mailbox not verified (no SMTP check)",
    "didYouMean": null,
    "syntaxValid": true,
    "domain": "apify.com",
    "domainExists": true,
    "hasMx": true,
    "acceptsMail": true,
    "mailProvider": "Google",
    "disposable": false,
    "role": false,
    "noReply": false,
    "freeProvider": false,
    "mxRecords": [{ "priority": 1, "host": "aspmx.l.google.com" }, { "priority": 5, "host": "alt1.aspmx.l.google.com" }],
    "catchAll": null,
    "mailboxChecked": false,
    "success": true,
    "charged": true,
    "source": "csv",
    "csvRow": 2,
    "duplicates": 1,
    "sourceFields": { "Name": "Jane", "Company": "Acme" }
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
