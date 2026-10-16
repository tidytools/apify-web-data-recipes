# Amazon Scraper - Products, Best Sellers & Price Tracker

Amazon product data from 20 Amazon sites: price, list price, stock, rating, reviews, Best Sellers Rank, bought in past month, seller, variations. Search and Best Sellers lists. Price, stock and rank tracking. $3 per 1,000 products, failed pages free.

- Apify Store: [https://apify.com/tidytools/amazon-product-scraper](https://apify.com/tidytools/amazon-product-scraper)
- Actor ID: `tidytools/amazon-product-scraper` (`ZlyK9cEqyTay2vp1R`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/amazon-product-scraper`

## Use case

**Paste Amazon product URLs or ASINs, search terms, or Best Sellers / New Releases list URLs (20 Amazon sites), and get one row per product or list position with price, rating, rank and stock, at $3 per 1,000 products and $1 per 1,000 search or list rows, with no start fee.** Blocked pages, robot checks and missing products are free, and we never solve robot checks.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Product | $3.00 |
| Search or list row | $1.00 |
| Unchanged product check | $0.50 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "urls": [
    "https://www.amazon.com/dp/B0DCH8VDXF",
    "https://www.amazon.com/gp/bestsellers/electronics"
  ],
  "searchTerms": [
    "wireless earbuds"
  ],
  "maxResultsPerInput": 10,
  "maxItems": 50
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "type": "product",
    "marketplace": "com",
    "asin": "B0DCH8VDXF",
    "parentAsin": "B0FFMX7Y3Q",
    "url": "https://www.amazon.com/dp/B0DCH8VDXF",
    "title": "Apple EarPods Headphones with USB-C Plug, Wired Ear Buds with Built-in Remote to Control Music, Phone Calls, and Volume",
    "brand": "Apple",
    "price": 19,
    "currency": "USD",
    "availability": "In Stock",
    "inStock": true,
    "rating": 4.5,
    "reviewCount": 18580,
    "boughtPastMonth": 10000,
    "boughtPastMonthText": "10K+ bought in past month",
    "seller": "Amazon.com",
    "shipsFrom": "Amazon.com",
    "features": ["SUPERIOR COMFORT — Unlike traditional circular ear buds, the design of EarPods is defined by the geometry of the ear. ..."],
    "mainImage": "https://m.media-amazon.com/images/I/513OSdW4elL._AC_SL1500_.jpg",
    "variationCount": 3,
    "variations": [{ "asin": "B0DCH8VDXF", "options": { "Size": "One Size", "Style": "USB-C" } }],
    "details": { "Item Weight": "1.12 ounces", "Item model number": "MYQY3AM/A", "Date First Available": "August 7, 2024" },
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
