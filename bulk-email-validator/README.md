# Email Verification — Bulk CSV List Cleaner

Email verification for bulk CSV lists without SMTP mailbox checks: syntax, domain and MX, disposable, role and free-provider flags, and typo suggestions. Upload CSV, use API or another Actor's dataset. Failed lines free. $0.50 per 1,000.

- Apify Store: [https://apify.com/tidytools/bulk-email-validator](https://apify.com/tidytools/bulk-email-validator)
- Actor ID: `tidytools/bulk-email-validator` (`haMAC5lJnzZmQcyqh`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/bulk-email-validator`

## Use case

**Verify and clean a bulk CSV email list, pasted addresses or a lead scraper's dataset (in Apify Console or through the API). Each address gets a verdict (valid, risky or invalid), a 0–100 score and a reason from syntax, domain and MX, disposable, role and typo checks. Mailboxes are not probed with SMTP. Pay $0.50 per 1,000 addresses; syntax errors, failed lookups and duplicates are free.**

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

From the Actor's documentation (section "Output (real result, shortened)"):

```json
[
    {
        "email": "jane@apify.com",
        "verdict": "valid",
        "score": 90,
        "reason": "domain accepts e-mail; mailbox not verified (no SMTP check)",
        "mailProvider": "Google",
        "disposable": false,
        "charged": true
    },
    { "email": "someone@gmial.com", "verdict": "risky", "score": 20, "reason": "disposable (temporary) e-mail domain", "didYouMean": "someone@gmail.com", "charged": true },
    { "email": "zed@gmail.con", "verdict": "invalid", "reason": "the domain does not exist (NXDOMAIN)", "didYouMean": "zed@gmail.com", "charged": true },
    { "email": "bad..address@gmail.com", "verdict": "invalid", "reason": "invalid syntax: consecutive dots in the local part", "charged": false }
]
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
