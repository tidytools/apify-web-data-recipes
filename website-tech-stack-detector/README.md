# Tech Stack Detector - BuiltWith & Wappalyzer Alternative

Tech stack detector and website technology lookup for site lists: CMS, e-commerce, JS frameworks, analytics, CDN, hosting, payments. 480+ technologies with evidence. $7/1,000 sites; none found = free.

- Apify Store: [https://apify.com/tidytools/website-tech-stack-detector](https://apify.com/tidytools/website-tech-stack-detector)
- Actor ID: `tidytools/website-tech-stack-detector` (`znF3B0Qjf11cv97Wa`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-tech-stack-detector`

## Use case

**Tech stack detector and BuiltWith / Wappalyzer alternative for $7 per 1,000 websites: get the CMS, e-commerce platform, frameworks, analytics, hosting and e-mail provider of any list of domains, with the evidence for every detection. Sites with no technology detected and sites that fail are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Analyzed website | $7.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "wordpress.org",
    "allbirds.com",
    "vercel.com",
    "python.org"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output (real result, shortened)"):

```json
{
    "input": "wordpress.org",
    "success": true,
    "technologyCount": 5,
    "technologyNames": "WordPress 7.2, Google Tag Manager, Nginx, PHP, Jetpack",
    "cms": "WordPress",
    "analytics": "Google Tag Manager",
    "technologies": [
        { "name": "WordPress", "category": "CMS", "confidence": "high", "version": "7.2", "evidence": ["meta: generator: WordPress 7.2-alpha-63999", "..."] },
        { "name": "Nginx", "category": "Web server", "confidence": "high", "version": null, "evidence": ["header: server: nginx"] }
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
