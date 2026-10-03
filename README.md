# Apify web data recipes (TidyTools)

Copy-paste recipes for the [TidyTools Actors on Apify](https://apify.com/tidytools): **Python, JavaScript, curl and n8n**.
Each Actor has its own folder with a short description, the minimal input, a sample output row and three ready-to-run scripts.
The Actors cover web scraping for LLMs and RAG (Markdown, embeddings, documents, audio), SEO and AI-search (GEO) audits, lead generation and monitoring.

Catalog with prices: [tools.yukai.uk](https://tools.yukai.uk/). For AI agents: [tools.yukai.uk/llms.txt](https://tools.yukai.uk/llms.txt).

**Try without an account (free, no key, rate limited):** `https://tools.yukai.uk/md/<url>` returns any web page as clean Markdown, and `https://tools.yukai.uk/ai-crawlers/<domain>` says which AI crawlers the site's robots.txt allows.

38 Actors: 16 are public on the Apify Store now; the others show the date from which they are available.

## Actors

Prices are per 1,000 events on the Apify Free plan (pay per event: no subscription, compute included).

| Actor | What it does | Price per 1,000 (Free plan) | Code |
|---|---|---|---|
| [AI Crawler Checker - robots.txt Checker for GPTBot & AI Bots](https://apify.com/tidytools/ai-crawler-access-checker) | Which AI bots can read a site? Bulk-check up to 10,000 domains for 29 AI crawlers (GPTBot, ClaudeBot, PerplexityBot...) in robots.txt: AI search score, fix snippet, Content Signals, change alerts. $2/1k sites. | Checked website: $2.00<br>Re-checked website (unchanged): $0.50 | [recipes](ai-crawler-access-checker/) |
| [AI Web Scraper - Extract Structured Data & URL to JSON](https://apify.com/tidytools/ai-web-data-extractor) | AI scraper and AI extractor: list the fields or describe what you want, and an LLM reads each page and returns JSON. No selectors or code. One row per list item, follows detail links. $0.01/page. | Extracted page: $10.00 | [recipes](ai-web-data-extractor/) |
| [Apple App Store Reviews Scraper - iOS App Reviews & Ratings](https://apify.com/tidytools/apple-app-store-reviews) | App Store scraper for iOS app reviews and app details from Apple's official public feeds, many countries. Star, date and keyword filters, new-review alerts, optional AI summary. $0.10/1,000 reviews. | Review: $0.10<br>App details: $1.00<br>AI insights: $20.00 | [recipes](apple-app-store-reviews/) |
| [ATS Jobs Scraper - Career Sites, Greenhouse, Lever, Workday](https://apify.com/tidytools/ats-career-site-jobs) | Give company domains or career-page URLs, get their live open jobs: Greenhouse, Lever, Ashby, Workday + 13 more ATSs, auto-detected. Salary, remote, new-job alerts. $1/1,000 jobs. | Job: $1.00<br>Company ATS detected: $2.00 | [recipes](ats-career-site-jobs/) |
| [Speech to Text: Audio to Text & Video to Text - Whisper, SRT](https://apify.com/tidytools/audio-transcriber) | Speech to text transcription with Whisper: audio to text, video to text, MP3 to text, podcast RSS, Drive/Dropbox links. SRT/VTT subtitle generator, speaker diarization, TXT/Markdown, 90+ languages. $0.006/min. | Audio minute: $6.00<br>Audio minute with speaker labels: $15.00<br>AI summary and chapters: $10.00<br>Translated subtitles (per minute and language): $2.00 | [recipes](audio-transcriber/) |
| [Bulk Email Validator - MX, Disposable Email & Typo Check](https://apify.com/tidytools/bulk-email-validator) | Email list cleaner without SMTP pings: bulk-check syntax, domain and MX records, disposable email, role and free-provider flags, and typos (gmial.com → gmail.com). CSV upload or another Actor's dataset. Failed lines are free. $0.50 per 1,000. | E-mail validated: $0.50 | [recipes](bulk-email-validator/) |
| [Bulk URL Status Checker - HTTP Status & Redirect Checker](https://apify.com/tidytools/bulk-url-status-checker) | Check thousands of URLs, a sitemap or a CSV for HTTP status codes, redirect chains, 404s, DNS and SSL errors. Verify a redirect map for site migrations, track changes. $1 per 1,000 URLs. | Checked URL: $1.00 | [recipes](bulk-url-status-checker/) |
| [Lead Enrichment - Company Enrichment for Google Maps Leads](https://apify.com/tidytools/company-website-enrichment) | Company data and lead enrichment for domains or Google Maps leads: emails, phones, socials, AI one-line description, industry, B2B/B2C, tech stack. Rows map back to the source. $6/1,000. | Enriched company: $6.00 | [recipes](company-website-enrichment/) |
| [PDF Text Extractor & PDF to Markdown - OCR, Word, Excel](https://apify.com/tidytools/document-to-markdown) | Document parser and PDF parser for LLMs: convert PDF, Word (DOCX/DOC), PowerPoint, Excel and CSV to clean Markdown text. PDF OCR for scanned files, RAG chunks. URLs, uploads, base64. $2/1,000 docs. | Converted document: $2.00<br>OCR page: $5.00 | [recipes](document-to-markdown/) |
| [Image to Text OCR API - Extract Text from Images with AI](https://apify.com/tidytools/image-to-text-ocr) | Extract text from images with AI OCR: receipts, screenshots, signs, document photos and tables as Markdown, in English, Chinese, Japanese and more. URLs, a dataset or base64. $3/1,000 images. | Image transcribed: $3.00 | [recipes](image-to-text-ocr/) |
| [SEO Audit Tool - SEO Checker, Site Audit & Core Web Vitals](https://apify.com/tidytools/seo-audit-crawler) | SEO crawler for technical SEO audits, JS sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional Core Web Vitals. $5/1k pages. | Audited page: $5.00<br>PageSpeed measurement: $5.00 | [recipes](seo-audit-crawler/) |
| [Website Change Monitor - Page Change Detection & Alerts](https://apify.com/tidytools/website-change-monitor) | Website change tracker and content monitor: text and price changes, CSS selector per URL, keyword triggers, noise filters, screenshots, email, Slack, Discord, webhook alerts, AI summary. $2/1k checks. | Page check: $2.00<br>AI change summary: $5.00<br>Change screenshot: $3.00 | [recipes](website-change-monitor/) |
| [Email Extractor - Website Contact Details Scraper & Socials](https://apify.com/tidytools/website-contact-extractor) | Email extractor and contact details scraper for company websites or Google Maps results: emails (incl. obfuscated), phones, social links, address, contact form. $2/1,000 sites; nothing found = free. | Processed website: $2.00 | [recipes](website-contact-extractor/) |
| [Website Content Crawler - Website to Markdown for LLM & RAG](https://apify.com/tidytools/website-markdown-crawler) | Markdown crawler for AI: crawl a website or docs site into clean, LLM-ready Markdown (URL to Markdown, HTML to Markdown) with RAG chunks. Sitemaps, JavaScript pages, linked PDFs and Word. $1/1k pages. | Page (fast mode): $1.00<br>Page (browser mode): $2.50 | [recipes](website-markdown-crawler/) |
| [Website Screenshot API - Full Page Screenshot & URL to PDF](https://apify.com/tidytools/website-screenshot-pdf-markdown) | Bulk website screenshots: full page, one element, mobile or tablet. URL to PDF and HTML to PDF for any web page, plus clean Markdown, in one run. Hides ads, cookie banners and pop-ups. Failures free. | Screenshot: $1.00<br>PDF: $2.50<br>Markdown: $2.00 | [recipes](website-screenshot-pdf-markdown/) |
| [Tech Stack Detector - BuiltWith & Wappalyzer Alternative](https://apify.com/tidytools/website-tech-stack-detector) | Tech stack detector and website technology lookup for site lists: CMS, e-commerce, JS frameworks, analytics, CDN, hosting, payments. 480+ technologies with evidence. $7/1,000 sites; none found = free. | Analyzed website: $7.00 | [recipes](website-tech-stack-detector/) |
| Local Business Leads by City and Category - Places Database (public from 2026-10-04) | Business lead lists for any city, box or country from the open Overture Maps places data: name, category, address, coordinates, website, phone, role emails (info@) and socials. No proxies, no blocking. $1/1,000 places. | Place: $1.00<br>Place enriched (contacts): $3.00 | [recipes](places-database/) |
| Shopify Product Scraper & Price Monitor (public from 2026-10-04) | Every product of any Shopify store from its public products.json: variants, SKUs, prices, stock, images. Shopify price monitor with price-drop and back-in-stock alerts. $1/1k products, no start fee. | Product: $1.00<br>Collection: $0.30<br>Shopify store detected: $1.00 | [recipes](shopify-store-products-scraper/) |
| AI Translator - Bulk Translate Text, JSON, Subtitles & Pages (public from 2026-10-04) | Translate texts, JSON and datasets, SRT/VTT subtitles and web pages into many languages at once. Glossary, tone, Markdown kept. A Google Translate / DeepL alternative, no API key. $1.50/1M chars. | 1,000 source characters: $1.50 | [recipes](web-page-translator/) |
| Broken Link Checker - Find 404 & Dead Links on Any Website (public from 2026-10-05) | Crawl a website and find every broken link and image (404, 410, 5xx, dead domains, SSL errors) with the page and anchor text. Alerts on new broken links. $1/1k pages + $0.30/1k links. | Crawled page: $1.00<br>Checked link: $0.30 | [recipes](broken-link-checker/) |
| Schema Markup Validator - JSON-LD Structured Data Checker (public from 2026-10-05) | Validate JSON-LD and Microdata schema markup on a URL list, a sitemap or a whole site against Google rich result rules (Product, FAQ, Recipe, Event, Job...), plus Open Graph. $2 per 1,000 pages. | Validated page: $2.00 | [recipes](structured-data-validator/) |
| Substack Scraper & Medium Scraper - Newsletter & Blog Posts (public from 2026-10-05) | Posts from Substack, Medium, Ghost, Beehiiv, WordPress or any RSS/Atom feed: title, author, date, text, tags, image. Date and keyword filters, new-post alerts, paywall-aware full text. $1/1k posts. | Post: $1.00<br>Full text from the post page: $1.00 | [recipes](substack-medium-posts-scraper/) |
| Bulk WHOIS & DNS Lookup - Domain Age, Expiry, Availability (public from 2026-10-06) | Look up many domains at once: registrar, creation and expiry dates, status and name servers via RDAP (WHOIS fallback), availability, A/MX/NS/TXT/CAA records, SPF/DMARC grade. $1/1,000. | Domain looked up: $1.00 | [recipes](bulk-domain-whois-dns-lookup/) |
| Bulk Phone Number Validator - Format, Type & Country (public from 2026-10-06) | Validate and format phone numbers in bulk, offline: valid or not, E.164 / international / national format, country, line type (mobile, fixed line, toll free, VoIP) and time zones. CSV upload or another Actor's dataset. Invalid numbers are free. $0.30 per 1,000. | Phone number validated: $0.30 | [recipes](phone-validator/) |
| Trade Show Exhibitor List Scraper - Company, Booth, Website (public from 2026-10-06) | Exhibitor lists from trade show and expo directories: company, booth, hall, categories, country, website, description, logo. a2z (Personify) and ExpoFP natively; other sites via AI. Company data only. | Exhibitor: $2.00<br>Exhibitor (name and booth only): $0.50<br>Exhibitor (AI-extracted): $3.00 | [recipes](trade-show-exhibitor-list-scraper/) |
| Sitemap URL Extractor & Sitemap Scraper - All Website URLs (public from 2026-10-07) | Get every URL of a website from its sitemaps: finds them via robots.txt, follows indexes and .gz files, returns lastmod, images and hreflang, optional status codes and changes. $0.30/1k URLs. | URL: $0.30<br>URL status check: $0.30 | [recipes](sitemap-url-extractor/) |
| Wayback Machine Scraper - Archived URLs & Website History (public from 2026-10-07) | Internet Archive Wayback Machine data: every archived URL of a website, a page's versions over time, the closest snapshot per URL, site history and old page content as Markdown. $1/1,000 rows. | Archived URL or snapshot: $1.00<br>Site history summary: $3.00<br>Archived page content: $3.00 | [recipes](wayback-machine-scraper/) |
| Article Summarizer & Text Summarizer - Summarize Web Pages (public from 2026-10-07) | AI summarizer for URLs, articles or your own text: TL;DR, bullets or executive summary, plus key points, topics, sentiment and keywords. Any language, JavaScript sites. No API key. $6/1,000. | Summarized page: $6.00<br>Summarized long page (deep): $12.00 | [recipes](web-page-summarizer/) |
| Background Remover - Image Converter, Compressor & Resizer (public from 2026-10-08) | Remove image backgrounds in bulk with AI (hair and fur kept): transparent PNG/WebP or any color, crop to subject. Plus resize, convert to WebP/AVIF/JPEG and compress. | Background removed: $5.00<br>Image resized, converted or compressed: $2.00 | [recipes](ai-image-toolkit/) |
| App Store Keyword Rank Tracker & Top Charts - ASO (public from 2026-10-08) | Apple App Store keyword rank tracker and top charts (free, paid, grossing, new) by country and category, plus Apple Podcasts charts and daily rank changes. Official Apple feeds, $0.50/1k rows. | Chart entry or search result: $0.50<br>Tracked app keyword rank: $1.00 | [recipes](app-store-top-charts/) |
| Link Preview API - Open Graph, Meta Tags & URL Metadata (public from 2026-10-08) | Get title, description, preview image, favicon, site name, author, dates and Open Graph / Twitter tags for any list of URLs. JavaScript pages too. $2 per 1,000 URLs. | URL preview: $2.00 | [recipes](link-preview-metadata/) |
| AI Alt Text Generator - Image Alt Text & Image Captions (public from 2026-10-09) | Find images missing alt text on pages, a sitemap or a whole site and write AI alt text in any language. Optional SEO title, caption and file name. WCAG accessibility, image SEO. $4/1,000. | Described image: $4.00<br>Described image with SEO fields: $6.00 | [recipes](ai-alt-text-generator/) |
| Website Classifier & Text Classifier - Industry & Sentiment (public from 2026-10-09) | Classify URLs, domains or texts with AI: industry with B2B/B2C, page type, topic, IAB category, sentiment, content moderation or your own labels, with confidence and reason. $4/1,000. | Classified page: $4.00<br>Classified page (quick): $3.00<br>Classified page (deep): $8.00 | [recipes](ai-page-classifier/) |
| Website Embeddings for RAG - Vector DB, Pinecone, Qdrant (public from 2026-10-09) | Crawl a site or docs, chunk the pages and get 1024-dim multilingual bge-m3 embeddings with stable IDs for Pinecone, Qdrant, pgvector or any vector database. No OpenAI key. From $0.20/1k chunks. | Page (fast mode): $1.00<br>Page (browser mode): $2.50<br>Embedded chunk: $0.20 | [recipes](website-to-embeddings/) |
| Job Search API - Greenhouse, Lever, Ashby & Workday Jobs Index (public from 2026-10-10) | Search 1.4M+ live jobs from 54,000+ company career boards (Greenhouse, Lever, Ashby, Workday, Workable, Personio and 10 more ATSs) in one query, refreshed daily. Posted vs first-seen dates, reposts, duplicates, hiring companies. $1.50/1,000 jobs. | Actor Start: $0.50<br>Job: $1.50<br>Hiring company: $3.00 | [recipes](ats-job-search/) |
| GEO Audit - AI SEO & AEO Checker for ChatGPT & AI Overviews (public from 2026-10-10) | GEO audit: can ChatGPT, Perplexity and Google AI Overviews reach and cite your site? GEO/AEO score, AI crawler and firewall test, llms.txt, schema, prioritized fixes, HTML report. From $0.03/site. | Audited website: $30.00<br>Sampled page: $4.00 | [recipes](geo-readiness-audit/) |
| llms.txt Generator & Checker - llms-full.txt, AI SEO (GEO) (public from 2026-10-10) | Generate llms.txt and llms-full.txt for any website from its sitemap or a crawl, with sections and AI descriptions, or validate existing llms.txt files in bulk. $2 per 1,000 pages or sites. | Indexed page: $2.00<br>Validated llms.txt: $2.00<br>AI page description: $5.00 | [recipes](llms-txt-generator/) |
| Smart Fetch - URL to Markdown from US, Singapore, EU or Taiwan (public from 2026-10-11) | Fetch any public URL as clean Markdown, HTML and JSON metadata. Pick the region it is fetched from (US, Singapore, EU, Taiwan residential) or let Auto switch region when a site blocks. JavaScript rendering, robots.txt respected, failed pages free. From $1/1,000 pages. | Page (HTTP): $1.00<br>Page (browser): $3.00<br>Region fee: $2.00 | [recipes](smart-fetch/) |

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
