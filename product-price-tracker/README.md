# E-commerce Scraper & Price Tracker - Products from Any Store (available from 2026-10-16)

Product name, price, sale price, stock, SKU, GTIN, brand, rating and variants from any online store's product pages, category pages or sitemap. Schedule it to track price drops and back-in-stock. $2 per 1,000 products, $0.50 per 1,000 unchanged checks.

- Apify Store: `apify.com/tidytools/product-price-tracker` (public from 2026-10-16)
- Actor ID: `tidytools/product-price-tracker` (`beBAgbCSEHDaC5Aor`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/product-price-tracker`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-16**. Until then the recipes below return an error.

## Use case

It reads **product data from any online store**: give it product pages, category pages or just a store's home page, and it returns one clean row per product with **name, price, sale price, currency, stock, SKU, GTIN/EAN, brand, rating, image and every variant** (size, color ...) with its own price and stock.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Product | $2.00 |
| Unchanged product check | $0.50 |
| Browser rendering | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.allbirds.com/products/mens-tree-runners",
    "https://www.deathwishcoffee.com/products/death-wish-instant-coffee-1",
    "https://www.ikea.com/us/en/p/billy-bookcase-white-00263850/"
  ],
  "maxProductsPerInput": 10,
  "maxProducts": 50
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "input": "https://www.allbirds.com/products/mens-tree-runners",
    "url": "https://www.allbirds.com/products/mens-tree-runners",
    "finalUrl": "https://www.allbirds.com/products/mens-tree-runners",
    "success": true,
    "store": "allbirds.com",
    "platform": "Shopify",
    "name": "Men's Tree Runner - Jet Black (White Sole)",
    "brand": "Allbirds",
    "sku": "TR3MJBW080",
    "gtin": "843416184854",
    "price": 100,
    "currency": "USD",
    "listPrice": null,
    "onSale": false,
    "discountPercent": null,
    "priceMin": 100,
    "priceMax": 100,
    "availability": "in_stock",
    "inStock": true,
    "condition": "new",
    "category": "Shoes",
    "image": "https://cdn.shopify.com/s/files/1/1104/4168/files/TR3MJBW080_SHOE_LEFT_GLOBAL_MENS_TREE_RUNNER_JET_BLACK_WHITE.png?v=1751165486",
    "variantCount": 7,
    "variantsInStock": 1,
    "variants": [
        { "id": "33179624669264", "name": "8", "sku": "TR3MJBW080", "gtin": "843416184854", "price": 100, "listPrice": null, "currency": "USD", "availability": "in_stock", "options": { "size": "8" } },
        { "id": "33179624702032", "name": "9", "sku": "TR3MJBW090", "gtin": "843416184861", "price": 100, "listPrice": null, "currency": "USD", "availability": "out_of_stock", "options": { "size": "9" } }
    ],
    "dataSource": "shopify-json+json-ld",
    "via": "direct",
    "charged": true,
    "checkedAt": "2026-10-03T14:47:14.018Z"
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
