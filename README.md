# Apify web data recipes (TidyTools)

Copy-paste recipes for the [TidyTools Actors on Apify](https://apify.com/tidytools): **Python, JavaScript, curl and n8n**.
Each Actor has its own folder with a short description, the minimal input, a sample output row and three ready-to-run scripts.
The Actors cover web scraping for LLMs and RAG (Markdown, embeddings, documents, audio), SEO and AI-search (GEO) audits, lead generation and monitoring.

30 Actors: 7 are public on the Apify Store now; the others show the date from which they are available.

## Actors

Prices are per 1,000 events on the Apify Free plan (pay per event: no subscription, compute included).

| Actor | What it does | Price per 1,000 (Free plan) | Code |
|---|---|---|---|
| [AI Crawler Access Checker - robots.txt for GPTBot, ClaudeBot](https://apify.com/tidytools/ai-crawler-access-checker) | Bulk-check up to 10,000 domains: which of 26 AI crawlers (GPTBot, ClaudeBot, PerplexityBot...) robots.txt allows, AI search score, fix snippet, Content Signals, change tracking. $2/1k sites. | Checked website: $2.00<br>Re-checked website (unchanged): $0.50 | [recipes](ai-crawler-access-checker/) |
| [AI Web Scraper - Extract Structured Data to JSON by Prompt](https://apify.com/tidytools/ai-web-data-extractor) | List the fields or just describe what you want: AI reads each page and returns clean JSON. No selectors or code. One row per item on list pages, follows detail links. $0.01 per page. | Extracted page: $10.00 | [recipes](ai-web-data-extractor/) |
| [PDF to Markdown & Text Extractor - Word, Excel, OCR](https://apify.com/tidytools/document-to-markdown) | Convert PDF, Word (DOCX/DOC), PowerPoint, Excel and CSV to clean Markdown text for LLMs and RAG. Optional OCR for scanned PDFs and chunks. URLs, uploads or base64. $2 per 1,000 docs. | Converted document: $2.00<br>OCR page: $5.00 | [recipes](document-to-markdown/) |
| [SEO Audit Tool - Site Crawler, SEO Score & Core Web Vitals](https://apify.com/tidytools/seo-audit-crawler) | Technical SEO site audit, JavaScript sites too: 0-100 SEO score and fix hints per page, site report (duplicate titles, broken pages, missing H1, meta, alt), optional PageSpeed. $5/1k pages. | Audited page: $5.00<br>PageSpeed measurement: $5.00 | [recipes](seo-audit-crawler/) |
| [Website Change Monitor - Page Change Detection & Alerts](https://apify.com/tidytools/website-change-monitor) | Monitor web pages for content and price changes: CSS selector per URL, keyword triggers, noise filters, screenshots, e-mail, Slack, Discord and webhook alerts, AI summaries. $2/1k checks. | Page check: $2.00<br>AI change summary: $5.00<br>Change screenshot: $3.00 | [recipes](website-change-monitor/) |
| [Website Content Crawler to Markdown for LLM & RAG](https://apify.com/tidytools/website-markdown-crawler) | Crawl any website or docs site into clean, LLM-ready Markdown with optional RAG chunks. Sitemap support, JavaScript rendering, linked PDFs and Word files converted. From $1 per 1,000 pages. | Page (fast mode): $1.00<br>Page (browser mode): $2.50 | [recipes](website-markdown-crawler/) |
| [Website Screenshot API - Full Page, URL to PDF & Markdown](https://apify.com/tidytools/website-screenshot-pdf-markdown) | Bulk website screenshots (full page, element, mobile, tablet), URL to PDF and clean Markdown in one run. PNG, JPEG or WebP, ad and cookie banner hiding. Pay only for successful outputs. | Screenshot: $1.00<br>PDF: $2.50<br>Markdown: $2.00 | [recipes](website-screenshot-pdf-markdown/) |
| [ATS & Career Site Jobs Scraper - Greenhouse, Lever, Workday](https://apify.com/tidytools/ats-career-site-jobs) (available from 2026-10-01) | Live jobs from company career sites: paste career pages, domains or board URLs. Auto-detects 17 ATSs incl. Greenhouse, Lever, Ashby, Workday, SmartRecruiters; only-new-jobs alerts. $1/1,000 jobs. | Job: $1.00<br>Company ATS detected: $2.00 | [recipes](ats-career-site-jobs/) |
| [Audio & Video to Text Transcription - Whisper, Podcasts, SRT](https://apify.com/tidytools/audio-transcriber) (available from 2026-10-01) | Transcribe audio and video files, Drive/Dropbox links and podcast RSS feeds to text with timestamps and SRT/VTT subtitles. Speech to text in 90+ languages, speaker labels optional. $0.006/min. | Audio minute: $6.00<br>Audio minute with speaker labels: $15.00<br>AI summary and chapters: $10.00<br>Translated subtitles (per minute and language): $2.00 | [recipes](audio-transcriber/) |
| [Website Contact Details Scraper - Emails, Phones, Socials](https://apify.com/tidytools/website-contact-extractor) (available from 2026-10-01) | Extract emails, phone numbers, social profiles, address and contact forms from company websites (home, contact and imprint pages), incl. obfuscated emails. $2/1,000 sites; nothing found = free. | Processed website: $2.00 | [recipes](website-contact-extractor/) |
| [Apple App Store Reviews Scraper API - iOS Reviews & Ratings](https://apify.com/tidytools/apple-app-store-reviews) (available from 2026-10-02) | App Store reviews and app details from Apple's official public feeds, many countries. Star, date and keyword filters, new-review alerts, optional AI summary. $0.10 per 1,000 reviews. | Review: $0.10<br>App details: $1.00<br>AI insights: $20.00 | [recipes](apple-app-store-reviews/) |
| [Lead Enrichment - Google Maps Emails & Company Data](https://apify.com/tidytools/company-website-enrichment) (available from 2026-10-02) | Enrich company domains or Google Maps / lead scraper results: emails, phones, socials, AI one-line description, industry, B2B/B2C, tech stack. Rows map back to the source. $6/1,000. | Enriched company: $6.00 | [recipes](company-website-enrichment/) |
| [Tech Stack Detector - BuiltWith & Wappalyzer Alternative](https://apify.com/tidytools/website-tech-stack-detector) (available from 2026-10-02) | Find the technologies behind any list of websites: CMS, e-commerce, JS frameworks, analytics, ads, CDN, hosting, payments. 320+ technologies with evidence. $4/1,000 sites; none found = free. | Analyzed website: $4.00 | [recipes](website-tech-stack-detector/) |
| [Bulk URL Status Checker - HTTP Status Codes & Redirects](https://apify.com/tidytools/bulk-url-status-checker) (available from 2026-10-03) | Check thousands of URLs, a sitemap or a CSV for HTTP status codes, redirect chains, 404s, DNS and SSL errors. Verify a redirect map for site migrations, track changes. $1 per 1,000 URLs. | Checked URL: $1.00 | [recipes](bulk-url-status-checker/) |
| [Image to Text OCR API - Extract Text from Images with AI](https://apify.com/tidytools/image-to-text-ocr) (available from 2026-10-03) | Extract text from images with AI OCR: receipts, screenshots, signs, document photos and tables as Markdown, in English, Chinese, Japanese and more. URLs, a dataset or base64. $3/1,000 images. | Image transcribed: $3.00 | [recipes](image-to-text-ocr/) |
| [AI SEO Audit (GEO/AEO) - ChatGPT & Perplexity Readiness](https://apify.com/tidytools/geo-readiness-audit) (available from 2026-10-04) | Can ChatGPT, Perplexity and Google AI Overviews reach and cite your site? GEO/AEO score, AI crawler and firewall test, llms.txt, schema, prioritized fixes and HTML report. From $0.01/site. | Audited website: $10.00<br>Sampled page: $2.00 | [recipes](geo-readiness-audit/) |
| [AI Translator - Bulk Translate Text, JSON, Subtitles & Pages](https://apify.com/tidytools/web-page-translator) (available from 2026-10-04) | Translate texts, JSON and datasets, SRT/VTT subtitles and web pages into many languages at once. Glossary, tone, Markdown kept. A Google Translate / DeepL alternative, no API key. $1.50/1M chars. | 1,000 source characters: $1.50 | [recipes](web-page-translator/) |
| [Broken Link Checker - Find 404 & Dead Links on Any Website](https://apify.com/tidytools/broken-link-checker) (available from 2026-10-05) | Crawl a website and find every broken link and image (404, 410, 5xx, dead domains, SSL errors) with the page and anchor text. Internal and external links. $1/1k pages + $0.30/1k links. | Crawled page: $1.00<br>Checked link: $0.30 | [recipes](broken-link-checker/) |
| [Schema Markup Validator - JSON-LD Structured Data Checker](https://apify.com/tidytools/structured-data-validator) (available from 2026-10-05) | Validate JSON-LD and Microdata schema markup on a URL list, a sitemap or a whole site against Google rich result rules (Product, FAQ, Recipe, Event, Job...), plus Open Graph. $2 per 1,000 pages. | Validated page: $2.00 | [recipes](structured-data-validator/) |
| [AI Alt Text Generator - Bulk Image Descriptions & Captions](https://apify.com/tidytools/ai-alt-text-generator) (available from 2026-10-06) | Find images missing alt text on pages, a sitemap or a whole site and write AI alt text in any language. Optional SEO title, caption and file name. WCAG accessibility, image SEO. $4/1,000. | Described image: $4.00<br>Described image with SEO fields: $6.00 | [recipes](ai-alt-text-generator/) |
| [Website to Vector Embeddings for RAG - Pinecone, Qdrant](https://apify.com/tidytools/website-to-embeddings) (available from 2026-10-06) | Crawl a site or docs, chunk the pages and get 1024-dim multilingual bge-m3 embeddings with stable IDs for Pinecone, Qdrant or pgvector. No OpenAI key needed. From $0.20 per 1,000 chunks. | Page (fast mode): $1.00<br>Page (browser mode): $2.50<br>Embedded chunk: $0.20 | [recipes](website-to-embeddings/) |
| [AI Website & Text Classifier - Industry, Category, Sentiment](https://apify.com/tidytools/ai-page-classifier) (available from 2026-10-07) | Classify URLs, domains or texts with AI: company industry with B2B/B2C, page type, topic, IAB category, sentiment, content moderation or your own labels, with confidence and reason. $4/1,000. | Classified page: $4.00<br>Classified page (quick): $3.00<br>Classified page (deep): $8.00 | [recipes](ai-page-classifier/) |
| [AI Summarizer - Summarize Web Pages, Articles & Text](https://apify.com/tidytools/web-page-summarizer) (available from 2026-10-07) | Summarize URLs, articles or your own text with AI: TL;DR, bullets or executive summary, plus key points, topics, sentiment and keywords. Any language, JavaScript sites. No API key. $6/1,000. | Summarized page: $6.00<br>Summarized long page (deep): $12.00 | [recipes](web-page-summarizer/) |
| [Bulk WHOIS & DNS Lookup - Domain Age, Expiry & Availability](https://apify.com/tidytools/bulk-domain-whois-dns-lookup) (available from 2026-10-08) | Look up many domains at once: registrar, creation and expiry dates, status and name servers via RDAP (WHOIS fallback), availability, A/MX/NS/TXT/CAA records, SPF/DMARC grade. $1/1,000. | Domain looked up: $1.00 | [recipes](bulk-domain-whois-dns-lookup/) |
| [Link Preview API - Open Graph, Meta Tags & URL Metadata](https://apify.com/tidytools/link-preview-metadata) (available from 2026-10-08) | Get title, description, preview image, favicon, site name, author, dates and Open Graph / Twitter tags for any list of URLs. JavaScript pages too. $1 per 1,000 URLs. | URL preview: $1.00 | [recipes](link-preview-metadata/) |
| [llms.txt Generator & Checker - llms-full.txt, AI SEO (GEO)](https://apify.com/tidytools/llms-txt-generator) (available from 2026-10-09) | Generate llms.txt and llms-full.txt for any website from its sitemap or a crawl, with sections and AI descriptions, or validate existing llms.txt files in bulk. $2 per 1,000 pages or sites. | Indexed page: $2.00<br>Validated llms.txt: $2.00<br>AI page description: $5.00 | [recipes](llms-txt-generator/) |
| [Sitemap URL Extractor - Get All URLs of a Website](https://apify.com/tidytools/sitemap-url-extractor) (available from 2026-10-09) | Get every URL of a website from its sitemaps: finds them via robots.txt, follows indexes and .gz files, returns lastmod, images and hreflang, optional status codes and changes. $0.30/1k URLs. | URL: $0.30<br>URL status check: $0.30 | [recipes](sitemap-url-extractor/) |
| [Substack & Medium Posts Scraper (RSS) - Newsletters & Blogs](https://apify.com/tidytools/substack-medium-posts-scraper) (available from 2026-10-10) | Posts from Substack, Medium, Ghost, Beehiiv, WordPress or any RSS/Atom feed: title, author, date, text, tags, image, word count. Date and keyword filters, new-post alerts, paywall-aware full text. $1 per 1,000 posts. | Post: $1.00<br>Full text from the post page: $1.00 | [recipes](substack-medium-posts-scraper/) |
| [Shopify Store Products Scraper (products.json) - Prices & Stock](https://apify.com/tidytools/shopify-store-products-scraper) (available from 2026-10-11) | All products of any Shopify store from its public products.json: variants, SKUs, prices, compare-at prices, stock, images. Price and stock change alerts, collections, 'is it Shopify?' check. $1 per 1,000 products. | Product: $1.00<br>Collection: $0.30<br>Shopify store detected: $1.00 | [recipes](shopify-store-products-scraper/) |
| [Wayback Machine Scraper - Archived URLs, Snapshots & History](https://apify.com/tidytools/wayback-machine-scraper) (available from 2026-10-12) | Internet Archive Wayback Machine data: every archived URL of a website, a page's versions over time, the closest snapshot per URL, site history and old page content as Markdown. $1 per 1,000 rows. | Archived URL or snapshot: $1.00<br>Site history summary: $3.00<br>Archived page content: $3.00 | [recipes](wayback-machine-scraper/) |

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

[AI Crawler Index](https://webcapture-api.yukailin.workers.dev/ai-crawler-index): a daily robots.txt check of 1,005 popular websites against 26 AI crawlers (GPTBot, ClaudeBot, PerplexityBot and more), by category and for the top 100, with the full table as CSV. It uses the same checks as the AI Crawler Access Checker.

## n8n

[`n8n/`](n8n/) has five workflows that were executed end to end: a weekly AI crawler access check with Slack alerts, a competitor pricing page monitor with Slack alerts, new job openings at target companies to Google Sheets, Google Maps leads enriched with emails and company data, and podcast episodes to transcripts and translated subtitles.

## Notes

- The inputs and output samples come from each Actor's own input schema and README. Output fields are documented on each Store page.
- Runs are billed to your Apify account per result; see each Store page for what is not charged (failed pages, errors and so on).
- Issues with an Actor: use the Issues tab on its Apify Store page.

## License

MIT (the code and text in this repository, see [LICENSE](LICENSE)). The Actors themselves are paid services on Apify.
