// Google Maps Email Extractor - Place Contacts for CRM: run the Actor on Apify and print the results.
// Store page: https://apify.com/tidytools/google-maps-email-extractor
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/google-maps-email-extractor';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "mapsData": "[{\"title\":\"Hofbräuhaus München\",\"address\":\"Platzl 9, 80331 München\",\"website\":\"https://www.hofbraeuhaus.de/\"},{\"title\":\"Daunt Books Marylebone\",\"address\":\"83-84 Marylebone High Street, London W1U 4QW\",\"website\":\"https://dauntbooks.co.uk/\"}]"
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
