# Website Email Extractor - Bulk Contact Details & Socials

Email extractor and contact details scraper for company websites or Google Maps results: emails (incl. obfuscated), phones, social links, address, contact form. $2/1,000 sites; nothing found = free.

- Apify Store: [https://apify.com/tidytools/website-contact-extractor](https://apify.com/tidytools/website-contact-extractor)
- Actor ID: `tidytools/website-contact-extractor` (`kFhBWk7SCYTakF6Fn`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-contact-extractor`

## Use case

A bulk email extractor for a list of domains or for Google Maps results: give it company or business websites (URLs or bare domains, up to 50,000 per run) or the dataset of a Google Maps run, and get one clean record per website:

- 📧 **Emails**: `mailto:` links, addresses written in the text, **obfuscated addresses** ("info [at] firm [dot] de", "info(at)firm.de", the full-width "info＠firm.com.tw", addresses written backwards or put together by a script, WordPress email-encoder plugins) and **Cloudflare-protected emails** (decoded). Lower-cased, de-duplicated, and junk is filtered out: image file names such as `logo@2x.png`, placeholder and example addresses (`you@example.com`, `name@domain.com`), error-tracking IDs and no-reply addresses.
- 📞 **Phone and fax numbers** in international format (`+12122542246`), from `tel:` links, schema.org data and the page text. Every number is checked with Google's libphonenumber rules for its country, and numbers in text are only taken after a label ("Tel:", "Phone", "電話"...), in international format, or in a typical phone layout, so order numbers, dates and prices are not picked up.
- 👥 **Social profiles**: Facebook, X, LinkedIn, Instagram, YouTube, TikTok, GitHub, Pinterest, Threads, Trustpilot, Discord, Telegram and WhatsApp. Only real profile URLs count (share buttons, posts and videos are ignored), and default profiles from website templates (e.g. `facebook.com/wix`) are skipped.
- 🏢 **Organization name, logo and postal address** from the site's schema.org data (JSON-LD or Microdata: Organization, LocalBusiness, Restaurant, Dentist...).
- 📝 **Contact form URL**: the page with a contact form (HTML forms with a message box, or HubSpot, Contact Form 7, Typeform, Jotform and other embeds).
- 🔎 **Where each value was found**: the page and the method (`mailto`, `text`, `obfuscated`, `cloudflare`, `jsonld`, `attribute`, `script`, `tel-link`), plus the list of pages checked.

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

From the Actor's documentation (section "Output example (real result, September 2026)"):

```json
{
    "input": "stumptowncoffee.com",
    "inputIndex": 0,
    "url": "https://stumptowncoffee.com/",
    "domain": "stumptowncoffee.com",
    "finalUrl": "https://www.stumptowncoffee.com/",
    "success": true,
    "organizationName": "Stumptown Coffee Roasters",
    "primaryEmail": "info@stumptowncoffee.com",
    "primaryPhone": "+18777113385",
    "emailsText": "info@stumptowncoffee.com, legal@stumptown.com, customerservice@stumptown.com",
    "phonesText": "+18777113385, +18332672844, +18557113385",
    "emails": ["info@stumptowncoffee.com", "legal@stumptown.com", "customerservice@stumptown.com"],
    "phones": ["+18777113385", "+18332672844", "+18557113385"],
    "faxes": [],
    "socialProfiles": {
        "instagram": "https://www.instagram.com/stumptowncoffee",
        "facebook": "https://www.facebook.com/stumptowncoffee",
        "x": "https://twitter.com/stumptowncoffee",
        "youtube": "https://www.youtube.com/channel/UC0yk_H5Np-uGvy98UM-jj6w",
        "tiktok": "https://www.tiktok.com/@stumptowncoffee",
        "pinterest": "https://www.pinterest.com/stumptowncoffee"
    },
    "address": "700 SW 5th Ave, 3rd Floor, #400, 97214 Portland, OR",
    "logo": "https://customers.seomanager.com/knowledgegraph/logo/stumptowncoffee_myshopify_com_logo.png",
    "contactFormUrl": null,
    "emailDetails": [
        { "email": "info@stumptowncoffee.com", "page": "https://www.stumptowncoffee.com/", "method": "jsonld", "sameDomain": true, "mailbox": "role" },
        { "email": "legal@stumptown.com", "page": "https://www.stumptowncoffee.com/pages/terms-and-conditions", "method": "text", "sameDomain": false, "mailbox": "role" }
    ],
    "phoneDetails": [
        { "number": "+18777113385", "display": "877-711-3385", "national": "(877) 711-3385", "country": "US", "type": "phone", "page": "https://www.stumptowncoffee.com/", "method": "jsonld" }
    ],
    "pagesChecked": [
        { "url": "https://www.stumptowncoffee.com/", "kind": "home", "via": "direct", "httpStatus": 200 },
        { "url": "https://www.stumptowncoffee.com/pages/contact-us", "kind": "contact", "via": "direct", "httpStatus": 200 },
        { "url": "https://www.stumptowncoffee.com/pages/locations", "kind": "locations", "via": "direct", "httpStatus": 200 },
        { "url": "https://www.stumptowncoffee.com/pages/our-story", "kind": "about", "via": "direct", "httpStatus": 200 },
        { "url": "https://www.stumptowncoffee.com/pages/terms-and-conditions", "kind": "legal", "via": "direct", "httpStatus": 200 }
    ],
    "charged": true,
    "via": "direct"
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
