# Lead Enrichment - Company Enrichment for Google Maps Leads (available from 2026-10-02)

Company data and lead enrichment for domains or Google Maps leads: emails, phones, socials, AI one-line description, industry, B2B/B2C, tech stack. Rows map back to the source. $6/1,000.

- Apify Store: `apify.com/tidytools/company-website-enrichment` (public from 2026-10-02)
- Actor ID: `tidytools/company-website-enrichment` (`RcPuCbK3BPevD8Uau`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/company-website-enrichment`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-02**. Until then the recipes below return an error.

## Use case

Give it a list of company domains, or the dataset of a Google Maps or other lead scraper run, and get one enriched record per company, read from the company's own website:

- 🏢 **Name** and a **one-line description** of what the company does, written by AI from the website text
- 🏷️ **Industry** (31 categories, e.g. `software-saas`, `restaurants-food-service`, `legal-services`) and **business model** (`B2B`, `B2C`, `B2B2C`, `nonprofit`, `government`), with a confidence and a short reason
- 📧 **Emails, phone numbers and social profiles** (Facebook, X, LinkedIn, Instagram, YouTube, TikTok and more), with obfuscated and Cloudflare-protected emails decoded and junk filtered out
- 📍 **Postal address and logo** from the site's schema.org data
- 🌐 **Language** and a **country guess** (from the postal address, else the country of its phone numbers, else the domain ending such as `.de`), with the source of the guess
- 🧰 **Tech stack**: CMS, e-commerce platform, analytics, tag manager, CDN, marketing tools and more, detected from the home page (included in the price; can be turned off)

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Enriched company | $6.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "domains": [
    "basecamp.com",
    "hofbraeuhaus.de"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (real result, September 2026)"):

```json
{
    "input": "dallmayr.com",
    "url": "https://dallmayr.com",
    "domain": "dallmayr.com",
    "success": true,
    "name": "Dallmayr",
    "description": "Dallmayr is a company that sells high-quality food and beverage products, including coffee, tea, and delicatessen items, to consumers through its retail stores, online shop, and vending services.",
    "industry": "consumer-products",
    "businessModel": "B2C",
    "industryConfidence": "high",
    "primaryEmail": "info@dallmayr.de",
    "primaryPhone": "+498921350",
    "emails": ["info@dallmayr.de"],
    "phones": ["+498921350", "+49892135130"],
    "socialProfiles": {
        "facebook": "https://www.facebook.com/dallmayr",
        "instagram": "https://www.instagram.com/dallmayr_de",
        "tiktok": "https://www.tiktok.com/@dallmayr_de",
        "linkedin": "https://de.linkedin.com/company/dallmayr-ohg",
        "youtube": "https://www.youtube.com/user/dallmayrkaffee"
    },
    "address": null,
    "language": "en",
    "countryGuess": "DE",
    "countrySource": "phone",
    "techStack": {
        "CMS": ["TYPO3"],
        "Analytics": ["Google Analytics"],
        "Advertising": ["Google Ads"],
        "CDN": ["Cloudflare"],
        "Programming language": ["PHP"],
        "Cookie consent": ["Cookie Consent (Osano open source)"]
    },
    "via": "direct",
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
