"""Recompute every benchmark metric from runs/*.json (+ refs/*.json, fetched once and cached).

Usage: py metrics.py            -> writes metrics.json and prints Markdown tables
       py metrics.py --refetch  -> re-download the reference pages (otherwise refs/ is reused)
"""
import glob, hashlib, json, os, re, sys
from urllib.parse import urlsplit

import refs as R

HERE = os.path.dirname(os.path.abspath(__file__))
SITES = json.load(open(os.path.join(HERE, "sites.json"), encoding="utf-8"))
SAMPLES = 5
PRICE_OURS = {"page-fast": 0.001, "page-browser": 0.0025}  # FREE tier event prices (USD)


def norm_url(u):
    p = urlsplit(u or "")
    path = re.sub(r"/index\.html?$", "/", p.path).rstrip("/") or "/"
    return f"{p.netloc.lower().replace('www.', '')}{path}"


# ---------- Markdown helpers ----------
FENCE = re.compile(r"^\s{0,3}(```|~~~)")


def split_fences(md):
    """Return (prose_lines, code_blocks) where code_blocks are the contents of fenced blocks."""
    prose, blocks, cur, fence = [], [], None, None
    for line in md.split("\n"):
        m = FENCE.match(line)
        if fence:
            if m and m.group(1) == fence:
                blocks.append("\n".join(cur))
                fence, cur = None, None
            else:
                cur.append(line)
            continue
        if m:
            fence, cur = m.group(1), []
            continue
        prose.append(line)
    if cur is not None:
        blocks.append("\n".join(cur))
    return prose, blocks


def md_to_text(md):
    t = re.sub(r"^---\n[\s\S]*?\n---\n", "", md)
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", t)
    for _ in range(2):
        t = re.sub(r"\[([^\]]*)\]\((?:[^()]|\([^)]*\))*\)", r"\1", t)
    t = re.sub(r"\\([\\`*_{}\[\]()#+\-.!<>=|~])", r"\1", t)  # Markdown escapes
    # leftover HTML tags only (JSX such as <Suspense> in inline code is page text and must stay)
    t = re.sub(r"</?(?:div|span|p|br|a|img|b|i|em|strong|sup|sub|u|small|section|figure|figcaption|details|summary|"
               r"table|tr|td|th|thead|tbody|ul|ol|li|kbd|code|pre|hr|button|svg|path)\b[^>\n]*>", " ", t, flags=re.I)
    t = t.replace("¶", "").replace("​", "").replace("\xa0", " ")
    return t


def words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def shingles(ws, n=6):
    return {" ".join(ws[i:i + n]) for i in range(max(1, len(ws) - n + 1))}


def found_text(item, md_words_joined, md_shingles):
    ws = words(item)
    if not ws:
        return True
    if len(ws) < 8:
        return f" {' '.join(ws)} " in md_words_joined
    sh = shingles(ws)
    return len(sh & md_shingles) / len(sh) >= 0.8


def code_key(s):
    return re.sub(r"\s+", "", R.html.unescape(s))


def unescape_md(s):
    return re.sub(r"\\([\\`*_{}\[\]()#+\-.!<>=|~])", r"\1", s)


def code_found(code, md, fenced_blocks):
    """(found anywhere in the Markdown, found inside a fenced code block, whitespace/escapes normalised)."""
    lines = [code_key(l) for l in code.split("\n") if code_key(l)]
    if not lines:
        return True, True
    md_lines = {code_key(unescape_md(l)) for l in md.split("\n")}
    fenced_lines = {code_key(l) for b in fenced_blocks for l in b.split("\n")}
    hit_any = sum(1 for l in lines if l in md_lines or any(l in x for x in ()))
    # Lines inside Markdown tables or inline paragraphs: fall back to substring search on the whole document.
    if hit_any / len(lines) < 0.8:
        blob = code_key(unescape_md(md))
        hit_any = sum(1 for l in lines if l in blob)
    hit_fenced = sum(1 for l in lines if l in fenced_lines)
    return hit_any / len(lines) >= 0.8, hit_fenced / len(lines) >= 0.8


# ---------- boilerplate / artifacts ----------
BOILER = re.compile(r"cookie|privacy policy|terms of (use|service)|all rights reserved|©|copyright \d|skip to (main )?content|"
                    r"edit (this|on) (page|github)|subscribe|newsletter|sign ?up|log ?in|sign ?in|was this (page|article) helpful|"
                    r"^\W*(previous|next)\W*$|on this page|table of contents|share (on|this)|follow us|last updated|powered by", re.I)
ARTIFACTS = {
    # heading permalinks: link text only a pilcrow, "#", section sign, zero-width space, link emoji or empty
    "permalinkAnchors": re.compile(r"\[(?:\u00b6|#|\u00a7|\u200b|\U0001F517|)\]\([^)\s]*#[^)\s]*(?:\s+\"[^\"]*\")?\)"),
    # backslash escapes of punctuation outside code (e.g. "\>>> x \= 1" when code lost its fence)
    "backslashEscapes": re.compile(r"\\[!-/:-@\[-`{-~]"),
    "emptyLinks": re.compile(r"(?<!!)\[\s*\]\([^)]*\)"),
    "rawHtmlTags": re.compile(r"</?(div|span|button|svg|path|script|style|iframe)\b", re.I),
    "dataUris": re.compile(r"\(data:[a-z]+/[^)]{20,}\)"),
    "copyButtons": re.compile(r"^\s*(copy|copy code|copied!?|copy to clipboard)\s*$", re.I | re.M),
}


def strip_front_matter(md):
    return re.sub(r"^---\n[\s\S]*?\n---\n+", "", md)


def prose_only(md):
    """Markdown outside fenced code blocks and inline code spans (front matter removed)."""
    prose, _ = split_fences(strip_front_matter(md))
    return re.sub(r"`[^`\n]*`", "", "\n".join(prose))


def page_lines(md):
    prose, _ = split_fences(strip_front_matter(md))
    out = []
    for l in prose:
        t = re.sub(r"\s+", " ", md_to_text(l)).strip(" -*#>|")
        if len(t) >= 4:
            out.append(t.lower())
    return out


def run_metrics(run):
    pages = [p for p in run["pages"] if p["ok"]]
    n = len(pages)
    # Template lines: the same line on at least half of the run's pages (menus, footers, banners).
    counts = {}
    per_page = []
    for p in pages:
        ls = set(page_lines(p["markdown"]))
        per_page.append(ls)
        for l in ls:
            counts[l] = counts.get(l, 0) + 1
    template = {l for l, c in counts.items() if n >= 4 and c >= max(2, n / 2)}
    tmpl_lines = sum(len(ls & template) for ls in per_page)
    boiler = 0
    for p in pages:
        boiler += sum(1 for l in page_lines(p["markdown"]) if len(l) < 120 and BOILER.search(l))
    hashes = [hashlib.sha1(re.sub(r"\s+", " ", p["markdown"]).strip().encode()).hexdigest() for p in pages]
    dup_content = len(hashes) - len(set(hashes))
    urls = [norm_url(p.get("finalUrl") or p["url"]) for p in pages]
    dup_url = len(urls) - len(set(urls))
    art = {k: sum(len(rx.findall(p["markdown"] if k == "permalinkAnchors" else prose_only(p["markdown"]))) for p in pages)
           for k, rx in ARTIFACTS.items()}
    fenced = sum(len(split_fences(p["markdown"])[1]) for p in pages)
    tables = sum(len(re.findall(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", p["markdown"], re.M)) for p in pages)
    rel_links = sum(len(re.findall(r"\]\((?!https?:|#|mailto:)[^)\s]+", p["markdown"])) for p in pages)
    r = run["run"]
    usage = sum((r.get("usageUsd") or {}).values()) if r.get("usageUsd") else r.get("usageTotalUsd")
    ev = r.get("chargedEventCounts") or {}
    if run["tool"] == "ours":
        # list price per converted page by the mode used (what a FREE-tier user pays)
        cost = sum(PRICE_OURS["page-browser" if p.get("mode") == "browser" else "page-fast"] for p in pages)
    else:
        cost = usage
    return {
        "pages": n, "failed": len(run["pages"]) - n, "runTimeSecs": r.get("runTimeSecs"), "memoryMb": r.get("memoryMbytes"),
        "computeUnits": r.get("computeUnits"), "userCostUsd": cost, "platformUsageUsd": usage,
        "costPer1000": round(cost / n * 1000, 3) if n and cost is not None else None,
        "cuPer1000": round(r["computeUnits"] / n * 1000, 2) if n and r.get("computeUnits") and run["tool"] == "wcc" else None,
        "events": ev, "avgChars": round(sum(len(p["markdown"]) for p in pages) / n) if n else 0,
        "truncatedPages": sum(1 for p in pages if p.get("truncated")),
        "templateLinesPerPage": round(tmpl_lines / n, 1) if n else 0, "boilerplateLinesPerPage": round(boiler / n, 2) if n else 0,
        "duplicateContent": dup_content, "duplicateUrls": dup_url, "fencedCodeBlocks": fenced, "markdownTables": tables,
        "relativeLinks": rel_links, "artifacts": art,
        "templateSample": sorted(template)[:15],
    }


def load_refs(site, sample_urls, refetch):
    path = os.path.join(HERE, "refs", f"{site}.json")
    cached = json.load(open(path, encoding="utf-8")) if os.path.exists(path) and not refetch else {}
    out = {}
    for u in sample_urls:
        if u not in cached:
            try:
                cached[u] = R.extract(R.fetch(u))
            except Exception as e:  # noqa: BLE001
                cached[u] = {"error": str(e)}
        out[u] = cached[u]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(cached, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return out


def pick_samples(site, runs):
    """Per tool, 5 sample URLs: pages both default runs returned (evenly spread over the sorted list, start page
    skipped), topped up with the tool's own pages when the two crawls found different pages. Returns {tool: [urls]}."""
    start = norm_url(SITES[site]["url"])
    sets = {}
    for r in runs:
        if not r["cheap"] and not r.get("tag"):
            sets[r["tool"]] = {norm_url(p.get("finalUrl") or p["url"]): (p.get("finalUrl") or p["url"]) for p in r["pages"] if p["ok"] and not p.get("truncated")}
    if not sets:
        return {}
    spread = lambda xs, k: [xs[int(i * len(xs) / min(k, len(xs)))] for i in range(min(k, len(xs)))]
    common = sorted(set.intersection(*[set(s) for s in sets.values()]) - {start})
    base = spread(common, SAMPLES)
    out = {}
    for tool, s in sets.items():
        own = sorted(set(s) - set(base) - {start})
        pick = base + spread(own, SAMPLES - len(base)) if len(base) < SAMPLES else base
        out[tool] = [s.get(u) or next(iter(v[u] for v in sets.values() if u in v)) for u in pick]
    return out


def samples_for_run(site, run, samples):
    """Default runs: the tool's samples. Cheap runs and re-runs (which may crawl other pages): the samples of either
    tool that this run also returned, topped up to 5 with the run's own pages (start page skipped)."""
    if not run["cheap"] and not run.get("tag"):
        return samples.get(run["tool"], [])
    have = {norm_url(p.get("finalUrl") or p["url"]): (p.get("finalUrl") or p["url"]) for p in run["pages"] if p["ok"] and not p.get("truncated")}
    pref = samples.get(run["tool"], []) + [u for v in samples.values() for u in v]
    mine = []
    for u in pref:
        if norm_url(u) in have and u not in mine:
            mine.append(u)
    mine = mine[:SAMPLES]
    start = norm_url(SITES[site]["url"])
    rest = sorted(set(have) - {norm_url(u) for u in mine} - {start})
    k = SAMPLES - len(mine)
    if k > 0 and rest:
        mine += [have[rest[int(i * len(rest) / min(k, len(rest)))]] for i in range(min(k, len(rest)))]
    return mine


def recall(run, sample_refs):
    by_url = {norm_url(p.get("finalUrl") or p["url"]): p for p in run["pages"] if p["ok"]}
    tot = {"headings": [0, 0], "paragraphs": [0, 0], "code": [0, 0], "codeFenced": [0, 0], "tables": [0, 0], "pages": 0}
    for url, ref in sample_refs.items():
        if "error" in ref:
            continue
        page = by_url.get(norm_url(url))
        if not page:  # re-runs may have crawled other pages: only pages present are scored
            continue
        md = page["markdown"]
        tot["pages"] += 1
        text = md_to_text(md)
        ws = words(text)
        joined = f" {' '.join(ws)} "
        sh = shingles(ws)
        for kind in ("headings", "paragraphs"):
            for item in ref[kind]:
                tot[kind][1] += 1
                tot[kind][0] += found_text(item, joined, sh)
        _, fenced = split_fences(md)
        for c in ref["code"]:
            any_, in_fence = code_found(c, md, fenced)
            tot["code"][1] += 1
            tot["code"][0] += any_
            tot["codeFenced"][1] += 1
            tot["codeFenced"][0] += in_fence
        md_tables = len(re.findall(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", md, re.M))
        tot["tables"][1] += ref["tables"]
        tot["tables"][0] += min(md_tables, ref["tables"])
    return {k: (round(v[0] / v[1], 3) if isinstance(v, list) and v[1] else (None if isinstance(v, list) else v)) for k, v in tot.items()} | {
        "counts": {k: v for k, v in tot.items() if isinstance(v, list)}}


def main():
    refetch = "--refetch" in sys.argv
    runs = []
    for f in sorted(glob.glob(os.path.join(HERE, "runs", "*.json"))):
        r = json.load(open(f, encoding="utf-8"))
        base = os.path.basename(f)[:-5]
        r["tag"] = base.split(f"-{r['site']}")[-1].lstrip("-") if not base.endswith(r["site"]) else ""
        r["name"] = base
        runs.append(r)
    result = {"sites": {}}
    for site in SITES:
        sruns = [r for r in runs if r["site"] == site]
        if not sruns:
            continue
        samples = pick_samples(site, sruns)
        result["sites"][site] = {"samples": samples, "runs": {}}
        for r in sruns:
            m = run_metrics(r)
            mine = samples_for_run(site, r, samples)
            sample_refs = load_refs(site, mine, refetch)
            m["recall"] = recall(r, sample_refs)
            m["recallSamples"] = mine
            result["sites"][site]["runs"][r["name"]] = m
    json.dump(result, open(os.path.join(HERE, "metrics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # Console tables
    print("| site | run | pages | secs | $/1k | tmpl lines/pg | boiler/pg | head R | para R | code R | code fenced | tables | dups | anchors | esc | avg chars |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for site, s in result["sites"].items():
        for name, m in s["runs"].items():
            rc = m["recall"]
            print(f"| {site} | {name.replace('-' + site, '')} | {m['pages']} | {m['runTimeSecs'] and round(m['runTimeSecs'])} | {m['costPer1000']} | "
                  f"{m['templateLinesPerPage']} | {m['boilerplateLinesPerPage']} | {rc['headings']} | {rc['paragraphs']} | {rc['code']} | "
                  f"{rc['codeFenced']} | {rc['tables']} | {m['duplicateContent']}/{m['duplicateUrls']} | {m['artifacts']['permalinkAnchors']} | "
                  f"{m['artifacts']['backslashEscapes']} | {m['avgChars']} |")


if __name__ == "__main__":
    main()
