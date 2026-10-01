"""Re-read run stats from Apify (usage and charged events are finalised a little after a run ends) into runs/*.json."""
import glob, json, os
from apify_api import api
HERE = os.path.dirname(os.path.abspath(__file__))
for f in glob.glob(os.path.join(HERE, "runs", "*.json")):
    d = json.load(open(f, encoding="utf-8"))
    r = api("GET", "/actor-runs/" + d["run"]["id"])["data"]
    st = r.get("stats") or {}
    d["run"].update({"runTimeSecs": st.get("runTimeSecs"), "computeUnits": st.get("computeUnits"), "usageTotalUsd": r.get("usageTotalUsd"),
                     "usageUsd": r.get("usageUsd"), "chargedEventCounts": r.get("chargedEventCounts")})
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("refreshed", len(glob.glob(os.path.join(HERE, "runs", "*.json"))), "runs")
