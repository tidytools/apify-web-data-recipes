"""Noise lines per page for Markdown crawl outputs (one consistent definition of clutter).

A prose line (outside code fences and front matter, link/image syntax removed, >= 4 characters) is NOISE when it is
  - template:  the same line appears on at least half of the run's pages (run of >= 4 pages): menus, footers, banners;
  - keyword:   a short line (< 120 chars) about cookies, legal, sign-in, subscribe/newsletter, share/follow, related
               posts/tags, edit-this-page, was-this-helpful, previous/next, on-this-page, copy URL, powered by ...;
  - taxonomy:  a line made only of links to tag / category / author pages (incl. "By [Name](.../author/...)" bylines).
Each line counts once even when it matches several kinds. Reported per page (average over the run's successful pages).

Usage:
  py noise.py runs/ours-default-cloudflare-blog-q2before.json [...]   # saved benchmark runs (run_bench.py format)
  py noise.py --glob "runs/*-q2*.json"
  py noise.py --dataset <datasetId> [--label name]                     # Apify dataset items with a "markdown" field
                                                                        # (our crawler or WCC); token from the APIFY_TOKEN env var
"""
import glob, json, os, re, sys

import metrics as M

HERE = os.path.dirname(os.path.abspath(__file__))

NOISE_KEYWORDS = re.compile(
    r"cookie|privacy policy|terms of (use|service)|all rights reserved|©|copyright \d|skip to (main )?content|"
    r"edit (this|on) (page|github)|subscribe|newsletter|sign ?up|log ?in|sign ?in|was this (page|article) helpful|"
    r"^\W*(previous|next)\W*$|on this page|table of contents|share (on|this|via)|^\W*share\W*$|follow (us|on)|"
    r"last updated|powered by|related (posts?|articles?|tags|content|reading)|^\W*tags?\W*$|email address|"
    r"copy (url|link)|back to top|you (might|may) also like|read next|recommended (posts|articles|for you)", re.I)
# A line whose links all go to tag / category / author listing pages (and which has little other text).
TAXONOMY_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)[^)]*\)")
TAXONOMY_PATH = re.compile(r"/(tags?|categor(y|ies)|topics?|authors?|label)/", re.I)


def taxonomy_line(raw):
    links = TAXONOMY_LINK.findall(raw)
    if not links or not all(TAXONOMY_PATH.search(u) for u in links):
        return False
    rest = TAXONOMY_LINK.sub("", raw)
    rest = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", rest)
    rest = re.sub(r"(?i)\b(by|and|written by|posted in|filed under|tags?|categories|category)\b|[\s,;:|·•&*_\-]", "", rest)
    return len(rest) <= 3


def prose_raw_lines(md):
    prose, _ = M.split_fences(M.strip_front_matter(md))
    return prose


def norm_line(raw):
    t = re.sub(r"\s+", " ", M.md_to_text(raw)).strip(" -*#>|")
    return t.lower() if len(t) >= 4 else None


def run_noise(pages):
    """pages: list of Markdown strings (successful pages only)."""
    n = len(pages)
    per_page = []
    counts = {}
    for md in pages:
        lines = []
        for raw in prose_raw_lines(md):
            t = norm_line(raw)
            if t is None and not taxonomy_line(raw):
                continue
            lines.append((raw, t))
        per_page.append(lines)
        for t in {t for _, t in lines if t}:
            counts[t] = counts.get(t, 0) + 1
    template = {t for t, c in counts.items() if n >= 4 and c >= max(2, n / 2)}
    tot = {"template": 0, "keyword": 0, "taxonomy": 0, "noise": 0, "lines": 0}
    samples = {}
    for lines in per_page:
        for raw, t in lines:
            kinds = []
            if t and t in template:
                kinds.append("template")
            if t and len(t) < 120 and NOISE_KEYWORDS.search(t):
                kinds.append("keyword")
            if taxonomy_line(raw):
                kinds.append("taxonomy")
            tot["lines"] += 1
            for k in kinds:
                tot[k] += 1
            if kinds:
                tot["noise"] += 1
                key = (t or raw)[:80]
                samples[key] = samples.get(key, 0) + 1
    per = {k: round(v / n, 2) if n else 0 for k, v in tot.items()}
    top = sorted(samples.items(), key=lambda kv: -kv[1])[:8]
    return {"pages": n, "noisePerPage": per["noise"], "templatePerPage": per["template"], "keywordPerPage": per["keyword"],
            "taxonomyPerPage": per["taxonomy"], "linesPerPage": per["lines"],
            "avgChars": round(sum(len(md) for md in pages) / n) if n else 0, "top": top}


def from_run_file(path):
    run = json.load(open(path, encoding="utf-8"))
    pages = [p["markdown"] for p in run["pages"] if p.get("ok")]
    return os.path.basename(path)[:-5], run.get("run", {}).get("id"), pages


def from_dataset(dataset_id):
    from apify_api import api
    items = api("GET", f"/datasets/{dataset_id}/items?clean=1&format=json", timeout=600)
    return [it["markdown"] for it in items if isinstance(it.get("markdown"), str) and it["markdown"].strip() and it.get("success", True) is not False]


def main():
    args = sys.argv[1:]
    rows = []
    if "--dataset" in args:
        ds = args[args.index("--dataset") + 1]
        label = args[args.index("--label") + 1] if "--label" in args else ds
        rows.append((label, ds, from_dataset(ds)))
    else:
        paths = []
        if "--glob" in args:
            paths += sorted(glob.glob(os.path.join(HERE, args[args.index("--glob") + 1])))
        skip = {args[i + 1] for i, a in enumerate(args[:-1]) if a in ("--glob", "--json")}
        paths += [a if os.path.isabs(a) else os.path.join(HERE, a) for a in args if a.endswith(".json") and a not in skip]
        rows += [from_run_file(p) for p in paths]
    out = {}
    print("| run | run id | pages | noise lines/page | template | keyword | tag/author | lines/page | avg chars |")
    print("|---|---|---|---|---|---|---|---|---|")
    for name, rid, pages in rows:
        r = run_noise(pages)
        out[name] = {"runId": rid, **r}
        print(f"| {name} | {rid} | {r['pages']} | {r['noisePerPage']} | {r['templatePerPage']} | {r['keywordPerPage']} | "
              f"{r['taxonomyPerPage']} | {r['linesPerPage']} | {r['avgChars']} |")
    if "--top" in args:
        for name, r in out.items():
            print(name, r["top"])
    if "--json" in args:
        json.dump(out, open(os.path.join(HERE, args[args.index("--json") + 1]), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
