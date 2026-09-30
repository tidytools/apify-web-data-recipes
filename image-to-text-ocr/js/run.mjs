// Image to Text OCR API - Extract Text from Images with AI: run the Actor on Apify and print the results.
// Store page: https://apify.com/tidytools/image-to-text-ocr
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/image-to-text-ocr';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "urls": [
        "https://upload.wikimedia.org/wikipedia/commons/6/67/Japanese_Road_Sign_119_%28Street_name%29.jpg",
        "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b3/Sahan_Supermarket_receipt%2C_Hillegersberg%2C_Rotterdam_%282021%29_02.jpg/1280px-Sahan_Supermarket_receipt%2C_Hillegersberg%2C_Rotterdam_%282021%29_02.jpg"
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
