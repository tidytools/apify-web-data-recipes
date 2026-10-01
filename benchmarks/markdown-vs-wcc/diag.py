"""Print which reference items a run misses on its sample pages. Usage: py diag.py <run-name> [kind]"""
import json, os, sys
import metrics as M
name = sys.argv[1]
kinds = sys.argv[2:] or ["headings", "paragraphs", "code"]
run = json.load(open(os.path.join(M.HERE, "runs", name + ".json"), encoding="utf-8"))
res = json.load(open(os.path.join(M.HERE, "metrics.json"), encoding="utf-8"))
urls = res["sites"][run["site"]]["runs"][name].get("recallSamples") or []
refs = json.load(open(os.path.join(M.HERE, "refs", run["site"] + ".json"), encoding="utf-8"))
by = {M.norm_url(p.get("finalUrl") or p["url"]): p for p in run["pages"] if p["ok"]}
for u in urls:
    p, ref = by.get(M.norm_url(u)), refs.get(u, {})
    if not p or "error" in ref:
        continue
    md = p["markdown"]
    ws = M.words(M.md_to_text(md)); j = f" {' '.join(ws)} "; sh = M.shingles(ws)
    _, fenced = M.split_fences(md)
    out = []
    if "headings" in kinds:
        out += ["H: " + h for h in ref["headings"] if not M.found_text(h, j, sh)]
    if "paragraphs" in kinds:
        out += ["P: " + x[:100] for x in ref["paragraphs"] if not M.found_text(x, j, sh)]
    if "code" in kinds:
        for c in ref["code"]:
            a, f = M.code_found(c, md, fenced)
            if not (a and f):
                out.append(f"C(any={a},fenced={f}): " + c[:80].replace("\n", " | "))
    print(u, len(md), *out[:8], sep="\n   ")
