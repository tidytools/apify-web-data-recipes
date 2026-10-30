# n8n workflows

Ten previously published workflows plus one WhatsApp voice-note example. The WhatsApp example has only local JSON and simulated-payload tests; its n8n import and live provider delivery have not been verified.

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
| [Fill missing emails in a Google Sheet](#fill-missing-emails-in-a-google-sheet) | manual | Google Sheets | website-contact-extractor |
| [Fill missing emails for a places dataset](#add-missing-emails-to-a-google-maps-or-places-dataset) | manual | Google Sheets | website-contact-extractor |
| [Verified emails and company data](#domain-sheet-to-verified-emails-and-company-data) | manual | Google Sheets | website-contact-extractor, bulk-email-validator, company-website-enrichment |
| [Drive recording to transcript Doc](#google-drive-recording-to-transcript-google-doc) | on new file | Google Docs | audio-transcriber |
| [Link to transcript Doc](#recording-link-to-transcript-google-doc-webhook-or-dropbox) | webhook | Google Docs | audio-transcriber |
| [WhatsApp voice note to transcript](#whatsapp-voice-note-to-transcript) | webhook | local success / free error branches | audio-transcriber |

Tests of the first five: self-hosted n8n 2.41.4, Apify node 0.8.0, 2026-09-30. Slack and Google Sheets nodes were swapped for No-Op in the tests; everything else is the file as published. The five added later are described in their own sections, with their test dates (2026-10-03 and 2026-10-06).

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

## Fill missing emails in a Google Sheet

File: [`n8n-sheets-fill-missing-emails.workflow.json`](n8n-sheets-fill-missing-emails.workflow.json)

Reads a Google Sheet of companies, sends only the rows without an email to [Google Maps Email Extractor](https://apify.com/tidytools/website-contact-extractor), and writes the email and a status back to the same row. Rows marked `retry:` are tried again on the next run.

Tested on 2026-10-03 with a temporary self-hosted n8n and the Apify node 0.8.0, with real Apify runs. The Google Sheets read and write nodes were No-Op (mocked data), so the write-back to a real sheet has not been run with a real Google account.

## Add missing emails to a Google Maps or places dataset

File: [`n8n-dataset-fill-missing-emails.workflow.json`](n8n-dataset-fill-missing-emails.workflow.json)

Takes the dataset of an earlier Google Maps (or other places) run, finds an email through [Google Maps Email Extractor](https://apify.com/tidytools/website-contact-extractor) for the places that have none, and appends one lead row per place to Google Sheets. The `websiteField` setting (default `website`) says which dataset column holds the website.

Tested on 2026-10-03 (same setup as above). The test found a wrong default column, which was fixed before publishing. The Google Maps Scraper step itself was not run (it is a third-party Actor); a prepared dataset was used. The Google Sheets node was No-Op.

## Domain sheet to verified emails and company data

File: [`n8n-maps-leads-verified-emails-sheets.workflow.json`](n8n-maps-leads-verified-emails-sheets.workflow.json)

Reads a sheet of domains, finds emails with [Google Maps Email Extractor](https://apify.com/tidytools/website-contact-extractor), checks them with [Bulk Email Validator](https://apify.com/tidytools/bulk-email-validator), adds company data with [Lead & Company Enrichment](https://apify.com/tidytools/company-website-enrichment), and writes a "Ready to send" tab. When no email is found, the flow skips verification and still adds company data.

Tested on 2026-10-06 with a temporary self-hosted n8n 2.41.7 and real Apify runs, with a list of websites and with a places dataset as input; the three Actors ran in sequence. The Google Sheets nodes were No-Op.

## Google Drive recording to transcript Google Doc

File: [`n8n-drive-recording-transcript-doc.workflow.json`](n8n-drive-recording-transcript-doc.workflow.json)

When a new audio or video file appears in a Drive folder, [Audio & Video Transcriber](https://apify.com/tidytools/audio-transcriber) transcribes it from its link (no 25 MB limit) and a Google Doc with the transcript is created. A temporary view-only link is added only when the file is not already shared, and removed after the run.

Tested on 2026-10-03 with a temporary self-hosted n8n and a real Apify run. The Google Drive trigger, the Drive permission calls and the Google Docs nodes were No-Op. It has not been run with a real Google account, so try it on a non-sensitive file first.

## Recording link to transcript Google Doc (webhook or Dropbox)

File: [`n8n-link-recording-transcript-doc.workflow.json`](n8n-link-recording-transcript-doc.workflow.json)

Send a recording link to the webhook (or a Dropbox path), and the flow transcribes it with [Audio & Video Transcriber](https://apify.com/tidytools/audio-transcriber) and creates a Google Doc. A source id taken from the link and a resume store make a re-sent link return the saved transcript instead of being transcribed and charged again.

Tested on 2026-10-03 with a temporary self-hosted n8n and a real Apify run. The Dropbox and Google Drive/Docs requests were No-Op. The duplicate-link bug found in testing was fixed before publishing. It has not been run with a real Dropbox or Google account.

## WhatsApp voice note to transcript

File: [`n8n-whatsapp-voice-transcript.workflow.json`](n8n-whatsapp-voice-transcript.workflow.json). This is an adaptable **single-file** example for uazapiGO or Evolution webhook envelopes. The workflow returns HTTP 200 immediately, skips non-audio, outgoing and sequential duplicate messages, and sends one approved direct-download URL to `tidytools/audio-transcriber`. It does not send a WhatsApp reply. The last nodes are local outputs for a successful transcript, a free failure, a missing direct URL and an ignored event; connect your own storage or reply action after testing.

### Field mapping / Mapeamento de campos / Mapeo de campos

| Provider | Verified event and audio indicators | Candidate URL in this workflow | Before calling the Actor |
|---|---|---|---|
| uazapiGO | `EventType=messages`; `message.id`, `message.messageType`, `message.fromMe`, `message.content` are documented. The workflow accepts `audio` or `AudioMessage`. | `message.content.directDownloadUrl` is **user-supplied enrichment**, not a confirmed uazapi field. Native direct-download field: **unconfirmed**. | Confirm your version's payload; fetch media with your own provider credential in n8n if needed, then supply a short-lived, anonymously downloadable HTTPS URL on an approved host. |
| Evolution API | `event=MESSAGES_UPSERT`; the example reads `data.key.id`, `data.key.fromMe`, `data.messageType` or `data.message.audioMessage`. | `data.message.mediaUrl` is only a conditional candidate; its presence and anonymous accessibility in your installed version are **unconfirmed**. | A base64-only media payload must first become a downloadable URL. Never place base64 or an encrypted WhatsApp CDN URL in `urls`. Verify the actual envelope and media access. |
| WAHA | The documented `message` event has `payload.media.url`; `payload.hasMedia` can be true while the URL is `null`. | **No WAHA parsing branch exists in this JSON.** The URL can be `localhost` or require an API key. | Add and verify a WAHA-specific parser or upstream adapter, download media locally if necessary, then provide the same approved short-lived HTTPS URL. An unconfirmed voice-type field must be checked against your payload. |

Source references checked 2026-10-27: [uazapiGO messages webhook](https://docs.uazapi.com/webhook/messages), [Evolution webhook documentation](https://github.com/evolution-foundation/evolution-docs/blob/main/docs/02-Configuration/Webhooks.md), and [WAHA receive messages](https://waha.devlike.pro/docs/how-to/receive-messages/). These describe provider versions and may differ from your installation.

### Configuração (PT-BR)

1. Importe o JSON com **Workflows > Import from file**. Instale `@apify/n8n-nodes-apify`, escolha sua credencial no node **Transcribe single file** e configure **Header Auth** no **WhatsApp webhook**; faça o provedor ou seu proxy enviar o cabeçalho. O arquivo não contém credenciais. O webhook responde 200 antes de concluir a transcrição.
2. Envie um payload de teste e confirme os campos na tabela. Em **Prepare one audio**, ajuste o mapeamento da sua versão; `message.content.directDownloadUrl` é um campo que você deve acrescentar, não um campo uazapi confirmado. Para WAHA, acrescente seu próprio adaptador antes desse node: o JSON publicado só analisa uazapiGO e Evolution.
3. Troque `media.example.org` em `PUBLIC_HOSTS` por um host HTTPS sob seu controle. Verifique com GET anônimo que o link baixa o áudio sem cabeçalho de autorização. Se vier somente base64, `localhost`, URL de API protegida ou URL nula, disponibilize o áudio em armazenamento seu com link direto temporário; o ramo **Provide short-lived direct URL** não chama o Actor. Não deixe o áudio público indefinidamente.
4. O node envia `{"urls":[url],"fileConcurrency":1,"language":"pt"}`. Teste uma mensagem de áudio, uma de texto e uma com URL inválida antes de ativar. **Success — local output** contém `text`; **Free error — local output** mantém `errorType`, `retryable`, `text` e `error`. Uma falha de execução do próprio node n8n pode não gerar linha de Dataset; monitore-a separadamente. Evite guardar payloads sensíveis nos dados de execução.

Preço: somente minutos de áudio transcritos com sucesso são cobrados, US$0.006 por minuto iniciado nas faixas FREE/BRONZE; arquivos com falha são gratuitos. Consulte o preço atual antes de ativar.

### Configuración (es)

1. Importe el JSON mediante **Workflows > Import from file**. Instale `@apify/n8n-nodes-apify`, seleccione su credencial en **Transcribe single file** y configure **Header Auth** en **WhatsApp webhook**; el proveedor o su proxy debe enviar ese encabezado. El archivo no contiene credenciales. El webhook responde 200 antes de terminar la transcripción.
2. Envíe un payload de prueba y confirme los campos de la tabla. Adapte **Prepare one audio** a su versión: `message.content.directDownloadUrl` es un campo adicional que usted debe proporcionar, no un campo uazapi confirmado. Para WAHA, agregue un adaptador propio; este JSON solo procesa uazapiGO y Evolution.
3. Sustituya `media.example.org` en `PUBLIC_HOSTS` por un host HTTPS bajo su control y pruebe una descarga GET anónima sin encabezado de autorización. Si solo hay base64, `localhost`, una URL de API protegida o `null`, primero genere un enlace directo temporal en su almacenamiento. **Provide short-lived direct URL** no llama al Actor. No deje el audio publicado indefinidamente.
4. Cambie `language: 'pt'` por `language: 'es'` en **Prepare one audio**; así el Actor recibe `{"urls":[url],"fileConcurrency":1,"language":"es"}`. Pruebe un audio, un texto y una URL inválida antes de activar. **Success — local output** conserva `text`; **Free error — local output** conserva `errorType`, `retryable`, `text` y `error`. Un fallo del propio node de n8n puede no producir una fila de Dataset; vigílelo por separado. Evite almacenar payloads sensibles en las ejecuciones.

Precio: solo se cobran los minutos de audio transcritos correctamente, US$0.006 por minuto iniciado en los niveles FREE/BRONZE; los archivos fallidos son gratuitos. Consulte el precio vigente antes de activar.

**Price / Preço / Precio:** the current `audio-minute` event is US$0.006 per **started minute** on FREE and BRONZE; `webcapture/actors/audio-transcriber/.actor/pricing.json` in the GetMoney source is the source of truth for all tiers. Only successfully transcribed minutes incur this event; failed file rows are free. The workflow's Apify node has `maxTotalChargeUsd: 0.5`, a run charge cap, not a per-file price. Check the live Store price before enabling it.

**Verification:** local JSON graph and simulated webhook/row tests only (2026-10-27). Real uazapiGO/Evolution webhooks, WAHA adapter, n8n import, public media download, and Apify execution remain untested. The static-data dedupe is for sequential published deliveries; concurrent runs need a durable unique message key.
