# Tech Stack Detector - BuiltWith & Wappalyzer Alternative (available from 2026-10-02)

Find the technologies behind any list of websites: CMS, e-commerce, JS frameworks, analytics, ads, CDN, hosting, payments. 320+ technologies with evidence. $4/1,000 sites; none found = free.

- Apify Store: [https://apify.com/tidytools/website-tech-stack-detector](https://apify.com/tidytools/website-tech-stack-detector)
- Actor ID: `tidytools/website-tech-stack-detector` (`znF3B0Qjf11cv97Wa`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/website-tech-stack-detector`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-02**. Until then the recipes below return an error.

## Use case

Give it a list of websites (bare domains like `stripe.com` or full URLs) and get the **technologies each site runs**, with the evidence for every detection:

- 🧱 **CMS and site builders**: WordPress, Drupal, Joomla, Ghost, Wix, Squarespace, Webflow, HubSpot CMS, Framer, Duda, Weebly, headless CMSs (Contentful, Sanity, Storyblok, Prismic)…
- 🛒 **E-commerce**: Shopify, WooCommerce, Magento, BigCommerce, PrestaShop, Salesforce Commerce Cloud, Ecwid…
- ⚛️ **JavaScript frameworks and libraries**: Next.js, Nuxt, React, Vue.js, Angular, Svelte/SvelteKit, Astro, Gatsby, Remix, jQuery (with version), Bootstrap, Tailwind CSS…
- 📊 **Analytics, tag managers and ads**: Google Analytics, Google Tag Manager, Hotjar, Microsoft Clarity, Mixpanel, Segment, Meta Pixel, LinkedIn Insight, TikTok Pixel, Google Ads…
- ☁️ **CDN, hosting and web servers**: Cloudflare, Fastly, Akamai, CloudFront, Vercel, Netlify, Heroku, WP Engine, Kinsta, Nginx (with version), Apache, LiteSpeed…
- 💳 **Payments, chat, marketing automation, A/B testing, cookie consent, bot protection, fonts, maps and video**: Stripe, PayPal, Klarna, Intercom, Zendesk, HubSpot, Klaviyo, Optimizely, OneTrust, Cookiebot, reCAPTCHA, DataDome, Google Fonts, YouTube…

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Analyzed website | $4.00 |

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

From the Actor's documentation (section "Output example (real result, September 2026)"):

```json
{
    "input": "wordpress.org",
    "inputIndex": 0,
    "url": "https://wordpress.org",
    "site": "wordpress.org",
    "finalUrl": "https://wordpress.org/",
    "httpStatus": 200,
    "success": true,
    "technologyCount": 5,
    "technologyNames": "WordPress 7.2, Google Tag Manager, Nginx, PHP, Jetpack",
    "cms": "WordPress",
    "ecommerce": null,
    "jsFramework": null,
    "analytics": "Google Tag Manager",
    "hosting": null,
    "technologies": [
        {
            "name": "WordPress",
            "category": "CMS",
            "confidence": "high",
            "version": "7.2",
            "evidence": [
                "header: link: <https://wordpress.org/wp-json/>; rel=\"https://api.w.org/\", <https://wordpress.…",
                "meta: generator: WordPress 7.2-alpha-63999",
                "script: https://wordpress.org/wp-content/mu-plugins/pub-sync/blocks/language-suggest/build/front.js?ver=5f3f8a2de66964d2bf04"
            ]
        },
        { "name": "Google Tag Manager", "category": "Tag manager", "confidence": "high", "version": null,
          "evidence": ["iframe: https://www.googletagmanager.com/ns.html?id=GTM-P24PF4B", "..."] },
        { "name": "Nginx", "category": "Web server", "confidence": "high", "version": null, "evidence": ["header: server: nginx"] },
        { "name": "PHP", "category": "Programming language", "confidence": "high", "version": null, "evidence": ["implied by WordPress"], "impliedBy": "WordPress" },
        { "name": "Jetpack", "category": "WordPress plugin", "confidence": "high", "version": null, "evidence": ["script: https://stats.wp.com/e-202640.js"] }
    ],
    "categories": { "CMS": ["WordPress"], "Tag manager": ["Google Tag Manager"], "Web server": ["Nginx"], "Programming language": ["PHP"], "WordPress plugin": ["Jetpack"] },
    "pagesChecked": ["https://wordpress.org/"],
    "signals": "full",
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
