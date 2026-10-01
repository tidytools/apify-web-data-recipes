# Website-to-Markdown benchmark: Website Markdown Crawler vs Website Content Crawler

Scripts, method and aggregated results of a small benchmark run on 2026-09-30.

- **Tool A:** [Website Markdown Crawler](https://apify.com/tidytools/website-markdown-crawler) (`tidytools/website-markdown-crawler`). We built it, so we have a conflict of interest. That is why the method, the scripts and every per-run number are published here.
- **Tool B:** Apify's [Website Content Crawler](https://apify.com/apify/website-content-crawler) (WCC, `apify/website-content-crawler`, build 0.3.97).

## Sites

| Key | Start URL | Kind |
|---|---|---|
| python-sphinx | https://docs.python.org/3/tutorial/ | Sphinx docs (static HTML) |
| docusaurus | https://docusaurus.io/docs/ | Docusaurus docs (pre-rendered React) |
| nextjs | https://nextjs.org/docs/app/ | Next.js docs (JS-heavy) |
| intercom-help | https://www.intercom.com/help/en/ | Help center (Intercom Articles) |
| cloudflare-blog | https://blog.cloudflare.com/ | Blog with long posts and code |

## Settings: what a new user gets

- **WCC:** the Apify Console prefill ([`wcc_prefill.json`](wcc_prefill.json): `crawlerType: playwright:adaptive`, `respectRobotsTxtFile`, `blockMedia`, `clickElementsCssSelector`, the prefilled `removeElementsCssSelector`, ...) plus the start URL and `maxCrawlPages: 25`. Everything else on the Actor's defaults (8,192 MB memory). Cheapest mode: `crawlerType: cheerio`.
- **Website Markdown Crawler:** only `urls` and `maxPages: 25`; everything else on defaults (`mode: auto`). Cheapest mode: `mode: fast`.
- Both crawl the paths under the start URL. One run per tool and site, one run at a time. The cheapest modes were run on `nextjs` only.

## Metrics

All computed by [`metrics.py`](metrics.py) (Python 3.9+, standard library only).

- **Time:** the Apify run's `stats.runTimeSecs`.
- **Cost per 1,000 pages:** WCC = the run's platform usage (on our account, $0.20 per compute unit) divided by pages. Website Markdown Crawler = its pay-per-event price ($1 per 1,000 pages over HTTP, $2.50 with a browser).
- **Body-text recall:** 5 sample pages per site. From each page's static HTML, [`refs.py`](refs.py) extracts the main content (`role=main`, `<main>`, `<article>` or Sphinx `div.body`): headings, paragraphs of 40+ characters, `<pre>` code and tables. Then we check whether each item is in the crawler's Markdown. Headings and short lines must match word for word; long paragraphs match when 80% of their 6-word shingles are found; code matches when 80% of its lines are found, and counts as *fenced* when those lines sit inside a ``` block. Pages both tools crawled are sampled first; pages cut at 40,000 characters are not sampled.
- **Clutter:** "template lines per page" = prose lines that repeat on at least half of a run's pages (menus, footers, banners); "boilerplate lines" = short lines about cookies, sign-in, subscribe, edit this page and the like ([`noise.py`](noise.py) has the exact rules).

## Results

Paragraph recall = sampled reference paragraphs found in the Markdown. "After" = our crawler after the fixes listed below; "blind" = our first run, before any change.

| Site | WCC default: time / paragraphs found / $ per 1,000 | Ours after: time / paragraphs found | Ours blind: time / paragraph recall |
|---|---|---|---|
| python-sphinx | 56 s / 237 of 242 (98%) / $1.55 | 3 s / 239 of 242 (99%) | 4 s / 99% |
| docusaurus | 84 s / 258 of 273 (95%) / $1.57 | 14 s / 144 of 148 (97%) | 4 s / 100% |
| nextjs | 200 s / **0 of 82 (0%)** / $3.64 | 6 s / 82 of 82 (100%) | 4 s / 100% |
| intercom-help | 183 s / **106 of 309 (34%)** / $3.65 | 34 s / 143 of 146 (98%) | 91 s / 97% |
| cloudflare-blog | 159 s / 196 of 199 (98%) / $2.77 | 9 s / 179 of 179 (100%) | 4 s / 98% |

Our crawler costs $1.00 per 1,000 pages on every site in these runs (all pages over HTTP). Each tool's recall is measured on its own 5 sample pages, so the reference counts differ when the two tools crawled different pages.

All runs (including WCC's cheapest mode on nextjs and a later 15-page clean-up round) with every metric:

- [`results/summary.csv`](results/summary.csv): one row per run (time, cost, recall for headings / paragraphs / code / fenced code / tables, clutter, average size).
- [`results/metrics.json`](results/metrics.json): the full output of `metrics.py`, including the sample URLs, charged events and Markdown artifact counts per run.

Run names: `<tool>-<mode>-<site>[-tag]`. `default` = the settings a new user gets, `cheap` = the cheapest mode. No tag = the blind first run; `-after` = after the fixes; `-q2before` / `-q2after` = a later 15-page round before and after a second set of clean-ups.

### Per site

- **python-sphinx:** both kept the body text. WCC turned Sphinx code into plain text with Markdown escapes and no code fences; our blind run also had no fences and kept the footer (both fixed in "after").
- **docusaurus:** our blind run followed the sitemap order and crawled mostly old 2.x docs, and split tables that omit closing tags into one cell per line. WCC kept 78% of headings (mostly missing the page H1) and fenced 18% of code blocks.
- **nextjs:** with the default settings, 22 of 26 WCC pages contained only the version menu. We did not investigate the cause further and ran it once. WCC's cheapest (Cheerio) mode kept all paragraphs but fenced 17% of code.
- **intercom-help:** WCC kept headings but dropped the lists, tables and FAQ text under them (34% of paragraphs).
- **cloudflare-blog:** WCC's output is the cleanest (0 template lines per page vs 8.6 for ours), but 21 of its 30 pages were author listing pages.

### What we changed between "blind" and "after"

Main-content extraction when a page has one clear `<article>` / `<main>`; code fences for bare `<pre>`; repair of tables with omitted closing tags; absolute links; removal of heading permalinks and one-line UI text ("Copy page", "Was this helpful?"); crawl order that puts in-content links before menus, sitemaps, translations, old versions and tag/author pages. These were tuned on the same five sites, so the "after" numbers are optimistic; the blind run is the fair comparison.

### Where WCC is still better

- Clutter on blog-style pages (related posts, tag lists, social links).
- Feature breadth: waiting for selectors, clicking, scrolling, saving HTML / screenshots / files, vector-database integrations and many advanced options.
- Maturity: far more users and runs.
- JavaScript-only sites: all five sites here serve server-rendered HTML, so sites that need a browser for their content were not tested.

## Limits

One run per tool and site, 5 sample pages per site, 5 sites, one day. WCC's cost depends on your plan's compute-unit price and the memory you choose; we kept its default memory because the test is about defaults.

## Reproduce

The raw crawl outputs and the reference extracts contain text from the five sites above, which belongs to their owners, so they are **not** in this repository. Re-create them with your own Apify token (results will differ a little as the sites change):

```bash
export APIFY_TOKEN=...                        # your own token
python run_bench.py wcc docusaurus            # or: ours docusaurus; add "cheap" for the cheapest mode; --tag after to save a variant
python refresh_runs.py                        # re-read final usage and charged events into runs/*.json
python metrics.py                             # fetches the reference pages into refs/, writes metrics.json, prints the tables
python diag.py ours-default-docusaurus        # what one run missed on its sample pages
python noise.py --glob "runs/*.json"          # clutter counts per run
```

A WCC run costs about $0.06 of platform credit per 25 pages on the default 8 GB memory. `run_bench.py` caps each Website Markdown Crawler run at $0.20.

## Files

- `sites.json`: the five sites. `wcc_prefill.json`: WCC's Console prefill values (from its input schema, build 0.3.97).
- `run_bench.py`, `refresh_runs.py`, `apify_api.py`: start runs and save outputs to `runs/` (token from the `APIFY_TOKEN` environment variable).
- `metrics.py`, `refs.py`, `noise.py`, `diag.py`: the metrics.
- `results/`: the aggregated results of the 2026-09-30 runs.

MIT license, like the rest of this repository.
