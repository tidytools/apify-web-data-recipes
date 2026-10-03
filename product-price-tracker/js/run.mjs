// E-commerce Scraper & Price Tracker - Products from Any Store: run the Actor on Apify and print the results.
// Store page: apify.com/tidytools/product-price-tracker (public from 2026-10-16)
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/product-price-tracker';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "urls": [
        "https://www.allbirds.com/products/mens-tree-runners",
        "https://www.deathwishcoffee.com/products/death-wish-instant-coffee-1",
        "https://www.ikea.com/us/en/p/billy-bookcase-white-00263850/"
    ],
    "maxProductsPerInput": 10,
    "maxProducts": 50
};

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first.');
    process.exit(1);
}

const client = new ApifyClient({ token });
const run = await client.actor(ACTOR_ID).call(input, { maxTotalChargeUsd: MAX_TOTAL_CHARGE_USD });
console.log('Run status:', run.status);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items.slice(0, 3)) console.log(JSON.stringify(item, null, 2).slice(0, 1500));
writeFileSync('results.json', JSON.stringify(items, null, 2));
console.log(`${items.length} rows saved to results.json`);
