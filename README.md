# Apify web data recipes (TidyTools)

Copy-paste recipes for the [TidyTools Actors on Apify](https://apify.com/tidytools): **Python, JavaScript, curl and n8n**.
Each Actor has its own folder with a short description, the minimal input, a sample output row and three ready-to-run scripts.
The Actors cover web scraping for LLMs and RAG (Markdown, embeddings, documents, audio), SEO and AI-search (GEO) audits, lead generation and monitoring.

Catalog with prices: [tools.yukai.uk](https://tools.yukai.uk/). For AI agents: [tools.yukai.uk/llms.txt](https://tools.yukai.uk/llms.txt).

**Try without an account (free, no key, rate limited):** `https://tools.yukai.uk/md/<url>` returns any web page as clean Markdown, and `https://tools.yukai.uk/ai-crawlers/<domain>` says which AI crawlers the site's robots.txt allows.

22 Actors: 22 are public on the Apify Store now; the others show the date from which they are available.

## Actors

Prices are per 1,000 events on the Apify Free plan (pay per event: no subscription, compute included).

| Actor | What it does | Price per 1,000 (Free plan) | Code |
|---|---|---|---|
| [AI Crawler Checker - robots.txt Checker for GPTBot & AI Bots](https://apify.com/tidytools/ai-crawler-access-checker) | Which AI bots can read a site? Bulk-check up to 10,000 domains for 29 AI crawlers (GPTBot, ClaudeBot, PerplexityBot...) in robots.txt: AI search score, fix snippet, Content Signals, change alerts. $2/1k sites. | Checked website: $2.00<br>Re-checked website (unchanged): $0.50 | [recipes](ai-crawler-access-checker/) |
| [AI Web Scraper - Extract Structured Data & URL to JSON](https://apify.com/tidytools/ai-web-data-extractor) | AI scraper and AI extractor: list the fields or describe what you want, and an LLM reads each page and returns JSON. No selectors or code. One row per list item, follows detail links. $0.015/page. | Extracted page: $15.00 | [recipes](ai-web-data-extractor/) |
| [Apple App Store Reviews Scraper - iOS App Reviews & Ratings](https://apify.com/tidytools/apple-app-store-reviews) | App Store scraper for iOS app reviews and app details from Apple's official public feeds, many countries. Star, date and keyword filters, new-review alerts, optional AI summary. $0.10/1,000 reviews. | Review: $0.10<br>App details: $1.00<br>AI insights: $20.00 | [recipes](apple-app-store-reviews/) |
| [ATS Jobs Scraper - Career Sites, Greenhouse, Lever, Workday](https://apify.com/tidytools/ats-career-site-jobs) | Give company domains or career-page URLs, get their live open jobs: Greenhouse, Lever, Ashby, Workday + 13 more ATSs, auto-detected. Salary, remote, new-job alerts. $2/1,000 jobs. | Job: $2.00<br>Company ATS detected: $2.00 | [recipes](ats-career-site-jobs/) |
| [Audio Transcription - Speech to Text, Audio to Text, Whisper](https://apify.com/tidytools/audio-transcriber) | Speech to text transcription with Whisper: audio to text, video to text, MP3 to text, podcast RSS, Drive/Dropbox links. SRT/VTT subtitle generator, speaker diarization, TXT/Markdown, 90+ languages. $0.006/min. | Audio minute: $6.00<br>Audio minute with speaker labels: $15.00<br>AI summary and chapters: $10.00<br>Translated subtitles (per minute and language): $2.00 | [recipes](audio-transcriber/) |
| [Broken Link Checker - Find 404 & Dead Links on Any Website](https://apify.com/tidytools/broken-link-checker) | Crawl a website and find every broken link and image (404, 410, 5xx, dead domains, SSL errors) with the page and anchor text. Alerts on new broken links. $1/1k pages + $0.50/1k links. | Crawled page: $1.00<br>Checked link: $0.50 | [recipes](broken-link-checker/) |
| [Bulk Email Validator & Email List Cleaner - Disposable Check](https://apify.com/tidytools/bulk-email-validator) | Email list cleaner without SMTP pings: bulk-check syntax, domain and MX records, disposable email, role and free-provider flags, and typos (gmial.com → gmail.com). CSV upload or another Actor's dataset. Failed lines are free. $0.50 per 1,000. | E-mail validated: $0.50 | [recipes](bulk-email-validator/) |
| [Bulk URL Status Checker - HTTP Status & Redirect Checker](https://apify.com/tidytools/bulk-url-status-checker) | Check thousands of URLs, a sitemap or a CSV for HTTP status codes, redirect chains, 404s, DNS and SSL errors. Verify a redirect map for site migrations, track changes. $1 per 1,000 URLs. | Checked URL: $1.00 | [recipes](bulk-url-status-checker/) |
| [Google Maps Lead Enrichment - Company Enrichment & Contact Data](https://apify.com/tidytools/company-website-enrichment) | Company data and lead enrichment for domains or Google Maps leads: emails, phones, socials, AI one-line description, industry, B2B/B2C, tech stack. Rows map back to the source. $6/1,000. | Enriched company: $6.00 | [recipes](company-website-enrichment/) |
| [PDF to Markdown & Document to Markdown - Text Extractor, OCR](https://apify.com/tidytools/document-to-markdown) | Document parser and PDF parser for LLMs: convert PDF, Word (DOCX/DOC), PowerPoint, Excel and CSV to clean Markdown text. PDF OCR for scanned files, RAG chunks. URLs, uploads, base64. $3/1,000 docs. | Converted document: $3.00<br>OCR page: $10.00 | [recipes](document-to-markdown/) |
| [Image to Text OCR API - Extract Text from Images with AI](https://apify.com/tidytools/image-to-text-ocr) | Extract text from images with AI OCR: receipts, screenshots, signs, document photos and tables as Markdown, in English, Chinese, Japanese and more. URLs, a dataset or base64. $4/1,000 images. | Image transcribed: $4.00 | [recipes](image-to-text-ocr/) |
| [Google Maps Scraper Alternative - Local Business Leads by City](https://apify.com/tidytools/places-database) | Business lead lists for any city, box or country from the open Overture Maps places data: name, category, address, coordinates, website, phone, role emails (info@) and socials. No proxies, no blocking. $1/1,000 places. | Place: $1.00<br>Place enriched (contacts): $3.00 | [recipes](places-database/) |
| [SEO Audit Tool - SEO Checker, Site Audit & Core Web Vitals](https://apify.com/tidytools/seo-audit-crawler) | SEO crawler for technical SEO audits, JS sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional Core Web Vitals. $8/1k pages. | Audited page: $8.00<br>PageSpeed measurement: $5.00 | [recipes](seo-audit-crawler/) |
| [Shopify Product Scraper & Shopify Price Monitor](https://apify.com/tidytools/shopify-store-products-scraper) | Every product of any Shopify store from its public products.json: variants, SKUs, prices, stock, images. Shopify price monitor with price-drop and back-in-stock alerts. $1/1k products, no start fee. | Product: $1.00<br>Collection: $0.30<br>Shopify store detected: $1.00 | [recipes](shopify-store-products-scraper/) |
| [Schema Markup Validator - JSON-LD Structured Data Checker](https://apify.com/tidytools/structured-data-validator) | Validate JSON-LD and Microdata schema markup on a URL list, a sitemap or a whole site against Google rich result rules (Product, FAQ, Recipe, Event, Job...), plus Open Graph. $2 per 1,000 pages. | Validated page: $2.00 | [recipes](structured-data-validator/) |
| [AI Translator - Bulk Translate Text, JSON, Subtitles & Pages](https://apify.com/tidytools/web-page-translator) | Translate texts, JSON and datasets, SRT/VTT subtitles and web pages into many languages at once. Glossary, tone, Markdown kept. A Google Translate / DeepL alternative, no API key. $1.50/1M chars. | 1,000 source characters: $1.50 | [recipes](web-page-translator/) |
| [Website Change Monitor - Page Change Detection & Alerts](https://apify.com/tidytools/website-change-monitor) | Website change tracker and content monitor: text and price changes, CSS selector per URL, keyword triggers, noise filters, screenshots, email, Slack, Discord, webhook alerts, AI summary. $2/1k checks. | Page check: $2.00<br>AI change summary: $5.00<br>Change screenshot: $3.00 | [recipes](website-change-monitor/) |
| [Google Maps Email Extractor - Website Emails, Phones & Socials](https://apify.com/tidytools/website-contact-extractor) | Google Maps email extractor: add emails to Google Maps results. Reads each business's own website (from a Maps scraper dataset or a domain list) for emails, best email with MX check, phones, socials. Does not scrape Maps itself. $2/1,000 sites; nothing found = free. | Processed website: $2.00 | [recipes](website-contact-extractor/) |
| [Website to Markdown Crawler - Content Crawler for LLM & RAG](https://apify.com/tidytools/website-markdown-crawler) | Markdown crawler for AI: crawl a website or docs site into clean, LLM-ready Markdown (URL to Markdown, HTML to Markdown) with RAG chunks. Sitemaps, JavaScript pages, linked PDFs and Word. $1.50/1k pages. | Page (fast mode): $1.50<br>Page (browser mode): $2.50 | [recipes](website-markdown-crawler/) |
| [Website Screenshot API - Full Page Screenshot & URL to PDF](https://apify.com/tidytools/website-screenshot-pdf-markdown) | Bulk website screenshots: full page, one element, mobile or tablet. URL to PDF and HTML to PDF for any web page, plus clean Markdown, in one run. Hides ads, cookie banners and pop-ups. Failures free. | Screenshot: $1.00<br>PDF: $2.50<br>Markdown: $2.00 | [recipes](website-screenshot-pdf-markdown/) |
| [Tech Stack Detector - BuiltWith & Wappalyzer Alternative](https://apify.com/tidytools/website-tech-stack-detector) | Tech stack detector and website technology lookup for site lists: CMS, e-commerce, JS frameworks, analytics, CDN, hosting, payments. 480+ technologies with evidence. $7/1,000 sites; none found = free. | Analyzed website: $7.00 | [recipes](website-tech-stack-detector/) |
| [YouTube Transcript Scraper - Captions, Timestamps & Metadata](https://apify.com/tidytools/youtube-transcript) | Get YouTube transcripts with timestamps from videos, whole channels or playlists: manual or auto-generated captions in any language, plus title, channel, duration, views and publish date. Optional speech-to-text for videos without captions. Failed videos are free. | Video transcript: $3.00<br>Speech-to-text minute: $8.00 | [recipes](youtube-transcript/) |

## Get an Apify API token

1. Create an Apify account at [apify.com](https://apify.com) (the Free plan is enough to try these recipes).
2. Open **Apify Console > Settings > API & Integrations** ([console.apify.com/settings/integrations](https://console.apify.com/settings/integrations)) and copy your personal API token.
3. Put it in an environment variable. The scripts read `APIFY_TOKEN` and never contain a token:

```bash
export APIFY_TOKEN=your_token        # macOS / Linux
$env:APIFY_TOKEN="your_token"        # Windows PowerShell
```

## Run a recipe

```bash
# Python
pip install -r requirements.txt
python website-markdown-crawler/python/run.py

# JavaScript (Node.js 18+)
npm install
node website-markdown-crawler/js/run.mjs

# curl
sh website-markdown-crawler/curl.sh
```

Every recipe runs the Actor with its prefilled example input and a $1.00 cost cap (`maxTotalChargeUsd`). Edit the input at the top of the script.

## Use with AI agents (MCP)

Every Actor can be called as a tool by Claude, Cursor, VS Code or any MCP client through Apify's hosted MCP server. Add one URL:

```
https://mcp.apify.com/?tools=tidytools/<actor-name>
```

For several tools at once, separate names with commas, for example
`https://mcp.apify.com/?tools=tidytools/website-markdown-crawler,tidytools/ai-crawler-access-checker`.
A ready-made configuration for six of these Actors, listed in the official MCP Registry, is in [tidytools/tidytools-apify-mcp](https://github.com/tidytools/tidytools-apify-mcp).

## Open data

[AI Crawler Index](https://tools.yukai.uk/ai-crawler-index): a daily robots.txt check of 1,005 popular websites against 26 AI crawlers (GPTBot, ClaudeBot, PerplexityBot and more), by category and for the top 100, with the full table as CSV. It uses the same checks as the AI Crawler Access Checker.

## n8n

[`n8n/`](n8n/) has five workflows that were executed end to end: a weekly AI crawler access check with Slack alerts, a competitor pricing page monitor with Slack alerts, new job openings at target companies to Google Sheets, Google Maps leads enriched with emails and company data, and podcast episodes to transcripts and translated subtitles.

## Benchmarks

[`benchmarks/markdown-vs-wcc/`](benchmarks/markdown-vs-wcc/): Website Markdown Crawler vs Apify's Website Content Crawler on 5 sites (speed, cost, body-text recall, clutter), with the scripts and per-run results.

## Notes

- The inputs and output samples come from each Actor's own input schema and README. Output fields are documented on each Store page.
- Runs are billed to your Apify account per result; see each Store page for what is not charged (failed pages, errors and so on).
- Issues with an Actor: use the Issues tab on its Apify Store page.

## License

MIT (the code and text in this repository, see [LICENSE](LICENSE)). The Actors themselves are paid services on Apify.
