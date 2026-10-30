"""Time Series Forecasting - AI Sales & Demand Forecast: run the Actor on Apify and print the results.

Store page: https://apify.com/tidytools/time-series-forecast
Setup:      pip install apify-client
            export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
Run:        python run.py
"""
import json
import os
from decimal import Decimal

from apify_client import ApifyClient

ACTOR_ID = "tidytools/time-series-forecast"
MAX_TOTAL_CHARGE_USD = Decimal("1.00")  # cost cap: the run stops charging at this amount

RUN_INPUT = {   'data': 'Month,Passengers\n'
            '1957-01,315\n'
            '1957-02,301\n'
            '1957-03,356\n'
            '1957-04,348\n'
            '1957-05,355\n'
            '1957-06,422\n'
            '1957-07,465\n'
            '1957-08,467\n'
            '1957-09,404\n'
            '1957-10,347\n'
            '1957-11,305\n'
            '1957-12,336\n'
            '1958-01,340\n'
            '1958-02,318\n'
            '1958-03,362\n'
            '1958-04,348\n'
            '1958-05,363\n'
            '1958-06,435\n'
            '1958-07,491\n'
            '1958-08,505\n'
            '1958-09,404\n'
            '1958-10,359\n'
            '1958-11,310\n'
            '1958-12,337\n'
            '1959-01,360\n'
            '1959-02,342\n'
            '1959-03,406\n'
            '1959-04,396\n'
            '1959-05,420\n'
            '1959-06,472\n'
            '1959-07,548\n'
            '1959-08,559\n'
            '1959-09,463\n'
            '1959-10,407\n'
            '1959-11,362\n'
            '1959-12,405\n'
            '1960-01,417\n'
            '1960-02,391\n'
            '1960-03,419\n'
            '1960-04,461\n'
            '1960-05,472\n'
            '1960-06,535\n'
            '1960-07,622\n'
            '1960-08,606\n'
            '1960-09,508\n'
            '1960-10,461\n'
            '1960-11,390\n'
            '1960-12,432',
    'horizon': 12,
    'quantiles': [0.1, 0.9],
    'evaluate': True}


def main():
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set the APIFY_TOKEN environment variable first.")
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT, max_total_charge_usd=MAX_TOTAL_CHARGE_USD)
    if run is None:
        raise SystemExit("The run did not finish.")
    # apify-client 1.x/2.x return a dict, 3.x returns a model object
    status = run["status"] if isinstance(run, dict) else run.status
    dataset_id = run["defaultDatasetId"] if isinstance(run, dict) else run.default_dataset_id
    print("Run status:", getattr(status, "value", status))

    items = list(client.dataset(dataset_id).iterate_items())
    for item in items[:3]:
        print(json.dumps(item, ensure_ascii=False, indent=2)[:1500])
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"{len(items)} rows saved to results.json")


if __name__ == "__main__":
    main()
