# Shopify Scraper - Shopify Products, Prices & Stock Monitor (available from 2026-10-11)

All products of any Shopify store from its public products.json: variants, SKUs, prices, compare-at prices, stock, images. Price and stock change alerts, collections, Shopify store check. $1/1k.

- Apify Store: `apify.com/tidytools/shopify-store-products-scraper` (public from 2026-10-11)
- Actor ID: `tidytools/shopify-store-products-scraper` (`99dLaQ0LJuZveBXc2`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/shopify-store-products-scraper`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-11**. Until then the recipes below return an error.

## Use case

It returns **every product of any Shopify store** from the store's own **public product feed** (`/products.json`), with all variants, SKUs, prices, compare-at prices, stock status and images. Paste store URLs or domains, collection URLs or product URLs; get one clean row per product (or per variant). It can also tell you **whether a site is a Shopify store** and watch stores for **price and stock changes**.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Product | $1.00 |
| Collection | $0.30 |
| Shopify store detected | $1.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "stores": [
    "https://www.allbirds.com",
    "https://www.tentree.com"
  ],
  "maxProductsPerStore": 20
}
```

## Sample output

From the Actor's documentation (section "Output example: product"):

```json
{
    "type": "product",
    "input": "https://www.allbirds.com",
    "store": "https://www.allbirds.com",
    "storeName": "Allbirds",
    "productId": 7340901859408,
    "title": "Women's Allbirds Flip Flop - Dusty Pink",
    "handle": "womens-allbirds-flip-flop-dusty-pink",
    "url": "https://www.allbirds.com/products/womens-allbirds-flip-flop-dusty-pink",
    "vendor": "Allbirds",
    "productType": "Shoes",
    "price": 25,
    "priceMax": 25,
    "compareAtPrice": 50,
    "onSale": true,
    "discountPercent": 50,
    "currency": "USD",
    "currencySource": "store page",
    "available": true,
    "variantsCount": 7,
    "variantsAvailable": 1,
    "skus": ["A12513W050", "A12513W060", "A12513W070", "A12513W080", "A12513W090", "A12513W100", "A12513W110"],
    "options": [{ "name": "Size", "values": ["5", "6", "7", "8", "9", "10", "11"] }],
    "imageUrl": "https://cdn.shopify.com/s/files/1/1104/4168/files/A12513_26Q2_Allbirds-Flip-Flop-Dusty-Pink_PDP_LEFT.png?v=1774646345",
    "imagesCount": 5,
    "description": "Sun on your feet. Comfort underneath. Light, easy, and made for warm weather, these flip flops bring everyday comfort to sunny days, beach walks, and everything in between. Just slip them on and go.",
    "publishedAt": "2026-09-25T23:58:13.000Z",
    "updatedAt": "2026-09-30T09:33:49.000Z",
    "variants": [
        { "variantId": 42146889039952, "title": "5", "sku": "A12513W050", "price": 25, "compareAtPrice": 50, "available": false, "option1": "5", "grams": 455 }
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
