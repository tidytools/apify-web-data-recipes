// CSV to JSON & JSON to CSV Converter - Batch, JSON Lines: run the Actor on Apify and print the results.
// Store page: https://apify.com/tidytools/tabular-transformer
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/tabular-transformer';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "files": [
        {
            "name": "example.csv",
            "dataText": "color,shape,flag,k,index,quantity,rate\nyellow,triangle,true,1,11,43.6498,9.8870\nred,square,true,2,15,79.2778,0.0130\n"
        }
    ]
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
