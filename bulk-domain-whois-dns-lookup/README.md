# Bulk WHOIS & DNS Lookup - Domain Age, Expiry, Availability (available from 2026-10-06)

Look up many domains at once: registrar, creation and expiry dates, status and name servers via RDAP (WHOIS fallback), availability, A/MX/NS/TXT/CAA records, SPF/DMARC grade. $1/1,000.

- Apify Store: `apify.com/tidytools/bulk-domain-whois-dns-lookup` (public from 2026-10-06)
- Actor ID: `tidytools/bulk-domain-whois-dns-lookup` (`zgj89sxvwUhvsPnpA`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/bulk-domain-whois-dns-lookup`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-06**. Until then the recipes below return an error.

## Use case

Bulk WHOIS and DNS lookup: give it a list of domains, URLs or e-mail addresses and get the registrar, creation and expiry dates (domain age), availability and DNS records for each domain. In detail, each domain gets:

- 📅 **Registration data (WHOIS)**: registrar and IANA ID, **creation, update and expiry dates**, **days to expiry**, domain age, status codes (e.g. `clientTransferProhibited`), name servers, DNSSEC, and the **registrant organization and country** when the registry or registrar publishes them
- 🌐 **DNS records**: A, AAAA, MX, NS, TXT and CAA, the CNAME of `www`, and the `_dmarc` record
- ✉️ **E-mail security grade (A-F)**: SPF policy (`-all`, `~all`...), DMARC policy (`reject`, `quarantine`, `none`), MX present, plus a list of issues (no SPF, two SPF records, `p=none`, more than 10 SPF lookups...)
- 🔎 **Availability guess** (optional): `registered`, `likely_available` or `unknown`, always worded as a guess

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Domain looked up | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "github.com",
    "https://www.bbc.co.uk/news",
    "spiegel.de",
    "sony.jp"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real result, September 2026)"):

```json
{
    "input": "github.com",
    "inputs": ["github.com", "www.github.com"],
    "domain": "github.com",
    "tld": "com",
    "success": true,
    "registered": true,
    "registrar": "MarkMonitor Inc.",
    "registrarIanaId": "292",
    "createdAt": "2007-10-09T18:20:50Z",
    "updatedAt": "2026-09-07T09:22:52Z",
    "expiresAt": "2028-10-09T18:20:50Z",
    "daysToExpiry": 741,
    "domainAgeDays": 6930,
    "status": ["clientDeleteProhibited", "clientTransferProhibited", "clientUpdateProhibited"],
    "nameservers": ["dns1.p08.nsone.net", "dns2.p08.nsone.net", "dns3.p08.nsone.net", "dns4.p08.nsone.net", "ns-1283.awsdns-32.org", "ns-1707.awsdns-21.co.uk", "ns-421.awsdns-52.com", "ns-520.awsdns-01.net"],
    "dnssec": false,
    "registrantOrg": "GitHub, Inc.",
    "registrantCountry": "US",
    "registrationSource": "rdap",
    "registrationServer": "rdap.verisign.com",
    "availability": "registered",
    "dnsResolves": true,
    "dns": {
        "a": ["140.82.112.4"],
        "aaaa": [],
        "mx": [{ "priority": 0, "host": "github-com.mail.protection.outlook.com" }],
        "ns": ["dns1.p08.nsone.net", "..."],
        "txt": ["MS=ms44452932", "google-site-verification=…", "v=spf1 ip4:192.30.252.0/22 include:spf.protection.outlook.com … ~all"],
        "caa": [{ "flags": 0, "tag": "issue", "value": "digicert.com" }, { "flags": 0, "tag": "issue", "value": "letsencrypt.org" }, "..."],
        "wwwCname": "github.com",
        "dmarc": "v=DMARC1; p=quarantine; sp=reject; pct=100; rua=mailto:dmarc@github.com; ruf=mailto:dmarc@github.com; fo=1"
    },
    "emailSecurity": {
        "grade": "B",
        "hasMx": true,
        "spfPolicy": "softfail",
        "dmarcPolicy": "quarantine",
        "spf": { "policy": "softfail", "includes": ["spf.protection.outlook.com", "_netblocks.google.com", "..."], "dnsLookups": 8, "multipleRecords": false },
        "dmarc": { "policy": "quarantine", "subdomainPolicy": "reject", "pct": 100, "rua": ["mailto:dmarc@github.com"] },
        "issues": [],
        "note": "DKIM is not checked (it needs the sender's selector)."
    },
    "emailGrade": "B",
    "checkedAt": "2026-09-29T14:16:25.456Z"
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
