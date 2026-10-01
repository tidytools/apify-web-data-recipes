# Schema Markup Validator - JSON-LD Structured Data Checker (available from 2026-10-05)

Validate JSON-LD and Microdata schema markup on a URL list, a sitemap or a whole site against Google rich result rules (Product, FAQ, Recipe, Event, Job...), plus Open Graph. $2 per 1,000 pages.

- Apify Store: `apify.com/tidytools/structured-data-validator` (public from 2026-10-05)
- Actor ID: `tidytools/structured-data-validator` (`H8eTuBhWOXKumBSIs`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/structured-data-validator`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-05**. Until then the recipes below return an error.

## Use case

It **extracts the structured data (schema.org markup in JSON-LD and Microdata) from your pages and checks it** against what Google needs for rich results: stars, prices, breadcrumbs, recipes, events, job postings and more. It also checks the **Open Graph and X (Twitter) tags** that control how shared links look. Check a list of URLs, every page in your **sitemap**, or crawl a whole website, then export every problem as a table with a **stable issue code**.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Validated page | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.allbirds.com/products/mens-tree-runners",
    "https://www.ikea.com/us/en/p/billy-bookcase-white-00263850/",
    "https://stripe.com/",
    "https://webscraper.io/test-sites/e-commerce/allinone/product/60"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "url": "https://www.allbirds.com/products/mens-tree-runners",
    "inputUrl": "https://www.allbirds.com/products/mens-tree-runners",
    "inputIndex": 0,
    "title": "Men's Tree Runners - Black - Everyday Sneakers | Allbirds",
    "status": "errors",
    "types": ["ProductGroup"],
    "richResults": ["Product variants"],
    "errorCount": 2,
    "warningCount": 0,
    "hasStructuredData": true,
    "jsonLdBlocks": 2,
    "invalidJsonLdBlocks": 0,
    "eligibleRichResultCount": 1,
    "errors": [
        "$[1]: missing \"@context\": \"https://schema.org\"",
        "$[1]: missing \"@type\""
    ],
    "warnings": [],
    "issues": [
        { "code": "MISSING_CONTEXT", "severity": "error", "type": null, "property": "@context", "path": "$[1]", "message": "missing \"@context\": \"https://schema.org\"" },
        { "code": "MISSING_TYPE", "severity": "error", "type": null, "property": "@type", "path": "$[1]", "message": "missing \"@type\"" }
    ],
    "items": [
        { "type": "ProductGroup", "path": "$[0]", "topLevel": true, "richResult": "Product variants", "eligible": true, "errors": [], "warnings": [] }
    ],
    "canonical": "https://www.allbirds.com/products/mens-tree-runners",
    "openGraph": { "og:title": "Men's Tree Runner - Jet Black (White Sole)", "og:type": "product", "og:image": "http://www.allbirds.com/cdn/shop/files/TR3MJBW080_SHOE_LEFT_GLOBAL_MENS_TREE_RUNNER_JET_BLACK_WHITE.png?v=1751165486", "...": "..." },
    "twitterCard": "summary_large_image",
    "socialIssues": [],
    "via": "backend",
    "jsonLd": [ { "@context": "https://schema.org/", "@type": "ProductGroup", "name": "Men's Tree Runner", "...": "..." } ]
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
