# n8n workflows

Two workflows that were imported and executed end to end in n8n before being published here.

**Requirements:** the Apify community node `@apify/n8n-nodes-apify` (Settings > Community nodes). The workflows set a cost cap
(`maxTotalChargeUsd`), which needs node version 0.7.0 or newer; on an older version, delete that field. Add your own Apify credential
(API token) to each Apify node after importing; the files contain no credentials.

**Import:** in n8n, Workflows > Import from file, then open each sticky note for setup steps.

## Google Maps leads with emails, socials and company descriptions

File: [`n8n-google-maps-lead-enrichment.workflow.json`](n8n-google-maps-lead-enrichment.workflow.json)

Runs the Google Maps Scraper on Apify for a search term and location, passes its dataset to [Lead Enrichment](https://apify.com/tidytools/company-website-enrichment) (email, phone, social profiles, a one-line AI description, B2B / B2C, tech stack) and appends one lead row per place to Google Sheets. Every row joins back to Google Maps by Place ID.

TidyTools Actors used: company-website-enrichment.

Tested end to end on 2026-09-30 (self-hosted n8n 2.41.4, Apify node 0.8.0): 5 dentists in Austin, Texas: 5 of 5 rows with Place ID and phone, Facebook 5/5, description 5/5, CMS 4/5, email 1/5; 23 s.

## New podcast episodes to transcript, summary and translated SRT subtitles

File: [`n8n-podcast-transcript-subtitles.workflow.json`](n8n-podcast-transcript-subtitles.workflow.json)

Every morning, transcribes new episodes of a podcast feed with [Audio & Video Transcriber](https://apify.com/tidytools/audio-transcriber) (transcript, summary, SRT/VTT subtitles; only episodes from the last 7 days that were not transcribed before) and translates the subtitles with [Bulk Text & JSON Translator](https://apify.com/tidytools/web-page-translator), keeping every timestamp.

TidyTools Actors used: audio-transcriber, web-page-translator.

Tested end to end on 2026-09-30 (self-hosted n8n 2.41.4, Apify node 0.8.0): NASA "Houston We Have a Podcast", 63-minute episode, Spanish + German: 2 rows (one per language) with summary and original + translated SRT; about 9.5 min end to end.
