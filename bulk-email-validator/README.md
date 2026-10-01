# Bulk Email Validator & Checker - MX, Disposable, Typos (available from 2026-10-15)

Clean e-mail lists without SMTP pings: syntax, domain and MX records, disposable, role and free-provider flags, typo fixes (gmial.com → gmail.com), score and verdict. $0.50/1,000.

- Apify Store: `apify.com/tidytools/bulk-email-validator` (public from 2026-10-15)
- Actor ID: `tidytools/bulk-email-validator` (`haMAC5lJnzZmQcyqh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/bulk-email-validator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-15**. Until then the recipes below return an error.

## Use case

It **cleans e-mail lists before you send**: for every address it checks the **syntax**, whether the **domain exists and accepts mail (MX records)**, and flags **disposable, role, no-reply and free-provider addresses** and **typos** such as `gmial.com` or `gmail.con`. Each address gets a **verdict** (`valid`, `risky`, `invalid`, `unknown`), a **score from 0 to 100** and a plain-English **reason**.

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
