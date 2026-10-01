"""Run one benchmark crawl (one tool x one site) on Apify, wait for it, save raw output to runs/<tool>-<mode>-<site>.json.

Usage: py run_bench.py <ours|wcc> <site-key> [cheap] [--memory MB] [--tag suffix] [--pages N]
Only one run at a time (the script blocks until the run finishes).
"""
import json, os, sys, time
from apify_api import api

HERE = os.path.dirname(os.path.abspath(__file__))
SITES = json.load(open(os.path.join(HERE, "sites.json"), encoding="utf-8"))
OURS = "tidytools~website-markdown-crawler"
WCC = "apify~website-content-crawler"
PAGES = 25
CAP = 40_000  # characters of Markdown kept per page in the saved file

# Console prefill of apify/website-content-crawler build 0.3.97, taken from its input schema (see README).
WCC_PREFILL = json.load(open(os.path.join(HERE, "wcc_prefill.json"), encoding="utf-8"))


def wcc_input(url, cheap):
    # WCC "defaults" = the Console prefill (what a new user runs), plus the start URL and the page cap.
    inp = dict(WCC_PREFILL)
    inp["startUrls"] = [{"url": url}]
    inp["maxCrawlPages"] = PAGES
    if cheap:
        inp["crawlerType"] = "cheerio"  # raw HTTP, no browser: WCC's cheapest mode
    return inp


def ours_input(url, cheap, pages=PAGES):
    inp = {"urls": [url], "maxPages": pages}
    if cheap:
        inp["mode"] = "fast"  # HTTP only, $1 / 1,000 pages
    return inp


def main():
    args = sys.argv[1:]
    tool, site = args[0], args[1]
    cheap = "cheap" in args
    memory = int(args[args.index("--memory") + 1]) if "--memory" in args else None
    tag = args[args.index("--tag") + 1] if "--tag" in args else ""
    pages = int(args[args.index("--pages") + 1]) if "--pages" in args else PAGES
    url = SITES[site]["url"]
    actor = OURS if tool == "ours" else WCC
    inp = ours_input(url, cheap, pages) if tool == "ours" else wcc_input(url, cheap)
    qs = "?timeout=420"
    if memory:
        qs += f"&memory={memory}"
    if tool == "ours":
        qs += "&maxTotalChargeUsd=0.2"
    t0 = time.time()
    run = api("POST", f"/acts/{actor}/runs{qs}", inp)["data"]
    print("started", run["id"], tool, site, "cheap" if cheap else "default", flush=True)
    while run["status"] in ("READY", "RUNNING", "TIMING-OUT", "ABORTING"):
        time.sleep(10)
        run = api("GET", f"/actor-runs/{run['id']}")["data"]
    items = api("GET", f"/datasets/{run['defaultDatasetId']}/items?clean=1&format=json", timeout=600)
    pages = []
    for it in items:
        if tool == "ours":
            if not it.get("success"):
                pages.append({"url": it.get("url"), "ok": False, "error": it.get("error")})
                continue
            md = it.get("markdown") or ""
            pages.append({"url": it.get("url"), "finalUrl": it.get("finalUrl"), "title": it.get("title"), "ok": True,
                          "mode": it.get("mode"), "canonicalUrl": it.get("canonicalUrl"), "mdChars": len(md),
                          "truncated": len(md) > CAP, "markdown": md[:CAP]})
        else:
            md = it.get("markdown") or ""
            crawl = it.get("crawl") or {}
            meta = it.get("metadata") or {}
            pages.append({"url": it.get("url"), "finalUrl": crawl.get("loadedUrl"), "title": meta.get("title"),
                          "ok": bool(md.strip()), "httpStatus": crawl.get("httpStatusCode"), "canonicalUrl": meta.get("canonicalUrl"),
                          "mdChars": len(md), "truncated": len(md) > CAP, "markdown": md[:CAP]})
    stats = run.get("stats") or {}
    out = {
        "tool": tool, "site": site, "startUrl": url, "cheap": cheap, "input": inp,
        "run": {"id": run["id"], "status": run["status"], "buildNumber": run.get("buildNumber"),
                "runTimeSecs": stats.get("runTimeSecs"), "computeUnits": stats.get("computeUnits"),
                "memoryMbytes": (run.get("options") or {}).get("memoryMbytes"),
                "usageTotalUsd": run.get("usageTotalUsd"), "usageUsd": run.get("usageUsd"),
                "chargedEventCounts": run.get("chargedEventCounts"), "statusMessage": run.get("statusMessage"),
                "wallSecs": round(time.time() - t0, 1)},
        "pages": pages,
    }
    name = f"{tool}-{'cheap' if cheap else 'default'}-{site}{('-' + tag) if tag else ''}.json"
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, "runs", name), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ok = sum(1 for p in pages if p["ok"])
    print(f"{name}: {run['status']} pages ok={ok}/{len(pages)} runtime={stats.get('runTimeSecs')}s usage=${run.get('usageTotalUsd')} "
          f"events={run.get('chargedEventCounts')} mem={out['run']['memoryMbytes']}")


if __name__ == "__main__":
    main()
