// Time Series Forecasting - AI Sales & Demand Forecast: run the Actor on Apify and print the results.
// Store page: https://apify.com/tidytools/time-series-forecast
// Setup: npm install apify-client
//        export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
// Run:   node run.mjs
import { writeFileSync } from 'node:fs';
import { ApifyClient } from 'apify-client';

const ACTOR_ID = 'tidytools/time-series-forecast';
const MAX_TOTAL_CHARGE_USD = 1.0; // cost cap: the run stops charging at this amount

const input = {
    "data": "Month,Passengers\n1957-01,315\n1957-02,301\n1957-03,356\n1957-04,348\n1957-05,355\n1957-06,422\n1957-07,465\n1957-08,467\n1957-09,404\n1957-10,347\n1957-11,305\n1957-12,336\n1958-01,340\n1958-02,318\n1958-03,362\n1958-04,348\n1958-05,363\n1958-06,435\n1958-07,491\n1958-08,505\n1958-09,404\n1958-10,359\n1958-11,310\n1958-12,337\n1959-01,360\n1959-02,342\n1959-03,406\n1959-04,396\n1959-05,420\n1959-06,472\n1959-07,548\n1959-08,559\n1959-09,463\n1959-10,407\n1959-11,362\n1959-12,405\n1960-01,417\n1960-02,391\n1960-03,419\n1960-04,461\n1960-05,472\n1960-06,535\n1960-07,622\n1960-08,606\n1960-09,508\n1960-10,461\n1960-11,390\n1960-12,432",
    "horizon": 12,
    "quantiles": [
        0.1,
        0.9
    ],
    "evaluate": true
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
