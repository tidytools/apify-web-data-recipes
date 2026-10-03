"""Speech to Text: Audio to Text & Video to Text - Whisper, SRT: run the Actor on Apify and print the results.

Store page: https://apify.com/tidytools/audio-transcriber
Setup:      pip install apify-client
            export APIFY_TOKEN=your_token   (Apify Console > Settings > API & Integrations)
Run:        python run.py
"""
import json
import os
from decimal import Decimal

from apify_client import ApifyClient

ACTOR_ID = "tidytools/audio-transcriber"
MAX_TOTAL_CHARGE_USD = Decimal("1.00")  # cost cap: the run stops charging at this amount

RUN_INPUT = {   'urls': ['https://webcapture-api.yukailin.workers.dev/samples/speech-sample.wav'],
    'podcastFeeds': ['https://www.nasa.gov/feeds/podcasts/small-steps-giant-leaps'],
    'maxEpisodesPerFeed': 1,
    'subtitleLanguages': []}


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
