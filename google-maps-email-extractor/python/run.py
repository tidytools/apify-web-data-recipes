"""Google Maps Email Extractor - Place Contacts for CRM: run the Actor on Apify and print the results.

Store page: https://apify.com/tidytools/google-maps-email-extractor
Setup:      pip install apify-client
            export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
Run:        python run.py
"""
import json
import os
from decimal import Decimal

from apify_client import ApifyClient

ACTOR_ID = "tidytools/google-maps-email-extractor"
MAX_TOTAL_CHARGE_USD = Decimal("1.00")  # cost cap: the run stops charging at this amount

RUN_INPUT = {   'mapsData': '[{"title":"Sample Shop A","address":"Example Street '
                '1","categoryName":"Shop","website":"https://example.com"},{"title":"Sample '
                'Shop B","address":"Example Street '
                '2","website":"https://example.org"},{"title":"Sample Shop '
                'C","address":"Example Street 3","website":null}]'}


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
