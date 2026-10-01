# n8n workflows

Five workflows that were imported and executed end to end in n8n before being published here.

**Requirements:** the verified Apify community node `@apify/n8n-nodes-apify` (Settings > Community nodes; on n8n Cloud, enable verified community nodes). The workflows set a cost cap
(`maxTotalChargeUsd`), which needs node version 0.7.0 or newer; on an older version, delete that field. After importing, add your own Apify credential
(API token or OAuth) to each Apify node, plus Slack or Google Sheets where used. The files contain no credentials.

**Import:** in n8n, Workflows > Import from file, then read the yellow sticky note for setup steps.

| Workflow | Schedule | Output | TidyTools Actor |
|---|---|---|---|
| [AI crawler access, weekly](#weekly-ai-crawler-access-check-with-slack-alerts) | weekly | Slack | ai-crawler-access-checker |
| [Competitor pricing pages](#competitor-pricing-page-monitor-with-slack-alerts) | daily | Slack | website-change-monitor |
| [New jobs at target companies](#new-job-openings-at-target-companies-to-google-sheets) | daily | Google Sheets | ats-career-site-jobs |
| [Google Maps leads](#google-maps-leads-with-emails-socials-and-company-descriptions) | manual | Google Sheets | company-website-enrichment |
| [Podcast transcripts and subtitles](#new-podcast-episodes-to-transcript-summary-and-translated-srt-subtitles) | daily | any | audio-transcriber |

All tests: self-hosted n8n 2.41.4, Apify node 0.8.0, 2026-09-30. Slack and Google Sheets nodes were swapped for No-Op in the tests; everything else is the file as published.

## Weekly AI crawler access check with Slack alerts

File: [`n8n-ai-crawler-access-weekly.workflow.json`](n8n-ai-crawler-access-weekly.workflow.json)

Every Monday, [AI Crawler Access Checker](https://apify.com/tidytools/ai-crawler-access-checker) reads robots.txt, llms.txt and the home page `noai` tags of your websites and says which AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended and 30+ others) are allowed or blocked. With a monitor name and `outputOnlyChanges`, only new or changed sites come back, and they are posted to Slack as one message. A week without changes posts nothing.

Tested: nytimes.com, theguardian.com and python.org. Run 1 produced one Slack message with each site's policy and blocked bots, in 5 s. Run 2 returned 0 rows, and the workflow stopped before Slack.

## Competitor pricing page monitor with Slack alerts

File: [`n8n-competitor-price-monitor.workflow.json`](n8n-competitor-price-monitor.workflow.json)

Every morning, [Website Change Monitor](https://apify.com/tidytools/website-change-monitor) checks each pricing page, limited to the part a CSS selector points to (for example `#pricing`), against the previous run. Each significant change becomes one Slack message with the price changes it found (`$19 → $29`) and the added and removed lines. Dates, times and counters are ignored.

Tested: plausible.io with the selector `#pricing`, plus a Hacker News page to force a change. Run 1 saved the baselines. Run 2 skipped the unchanged pricing page and sent one alert for the changed page, in 5 s.

## New job openings at target companies to Google Sheets

File: [`n8n-ats-new-jobs.workflow.json`](n8n-ats-new-jobs.workflow.json)

Every morning, [ATS Career Site Jobs](https://apify.com/tidytools/ats-career-site-jobs) reads the job boards of your companies (Greenhouse, Lever, Ashby, Workable, Workday, SmartRecruiters, Recruitee, Personio and more; a company website is enough). With `onlyNewJobs`, only openings that were not there on the previous run come back, and each one is appended to Google Sheets with company, title, location, department, remote, salary, posted date and link.

Tested: the Lever demo board and Hugging Face (Workable), with the title keyword "engineer". Run 1 wrote 10 rows in 4.5 s. Run 2 found 0 new jobs, and the workflow stopped before Sheets.

## Google Maps leads with emails, socials and company descriptions

File: [`n8n-google-maps-lead-enrichment.workflow.json`](n8n-google-maps-lead-enrichment.workflow.json)

Runs the Google Maps Scraper on Apify for a search term and location, then passes its dataset to Lead Enrichment (`tidytools/company-website-enrichment`, public on the Apify Store from 2026-10-02). Enrichment adds the email, phone, social profiles, a one-line AI description, B2B / B2C and the tech stack. One lead row per place is appended to Google Sheets, and every row joins back to Google Maps by Place ID.

Tested: 5 dentists in Austin, Texas. All 5 rows had a Place ID and phone; Facebook 5/5, description 5/5, CMS 4/5, email 1/5; 23 s.

## New podcast episodes to transcript, summary and translated SRT subtitles

File: [`n8n-podcast-transcript-subtitles.workflow.json`](n8n-podcast-transcript-subtitles.workflow.json)

Every morning, [Audio & Video Transcriber](https://apify.com/tidytools/audio-transcriber) transcribes new episodes of a podcast feed: transcript, summary and SRT/VTT subtitles, taking only episodes newer than the last one transcribed. In the same Apify run, the subtitles are translated into the languages you choose (`subtitleLanguages`), keeping every timestamp and speaker label. The output is one row per episode.

Tested: NASA "Small Steps, Giant Leaps", a 19-minute episode, translated to Spanish. The result was 1 row with the summary, the original SRT and the Spanish SRT. The Spanish file has 297 cues with the same timings as the original. The run took 2 min 8 s.
