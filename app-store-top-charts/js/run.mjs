// App Store Charts & Keyword Rank Tracker - Top Charts, ASO: run the Actor on Apify and print the results.
// Store page: apify.com/tidytools/app-store-top-charts (public from 2026-10-14)
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/app-store-top-charts';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "mode": "charts",
    "countries": [
        "us",
        "gb"
    ],
    "chartTypes": [
        "topfree"
    ],
    "genres": [
        "all",
        "Productivity"
    ],
    "maxRank": 10,
    "keywords": [
        "habit tracker"
    ],
    "trackApps": [
        "https://apps.apple.com/us/app/habitkit/id6443918070"
    ],
    "resultsPerKeyword": 5
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
