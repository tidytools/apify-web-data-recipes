# Gemini Brand Visibility Tracker - Share of Voice & Citations

Ask Google-Search-grounded Gemini the category questions your buyers ask and see which brands it names: your brand vs competitors, mention order, cited URLs. $0.12 per successful query; failed queries free.

- Apify Store: [https://apify.com/tidytools/gemini-brand-visibility](https://apify.com/tidytools/gemini-brand-visibility)
- Actor ID: `tidytools/gemini-brand-visibility` (`SiedmIAxpVn8Warb2`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/gemini-brand-visibility`

## Use case

**Ask Google Gemini the category questions your buyers ask, and see which brands it recommends.** Each question ("What is the best issue tracker for a startup engineering team?") is sent to **Gemini with Google Search grounding**. For every answer you get whether your brand is named, its mention order against your competitors, which competitors were named, the source URLs Gemini cited and a short answer excerpt. `SUMMARY` adds up your **visibility score** and how many answers named each competitor: your share of voice in Gemini. Successful answers cost $0.12 each; failed answers are free.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Successful AI engine query | $120.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "brand": "Linear",
  "domain": "linear.app",
  "competitors": [
    "Jira",
    "Asana",
    "ClickUp"
  ],
  "queries": [
    "What is the best issue tracker for a startup engineering team?",
    "Which project management tool do software teams switch to from Jira?",
    "What is a good bug tracking tool for a small SaaS company?"
  ]
}
```

## Sample output

From the Actor's documentation (section "Output"):

```json
{
  "type": "ANSWER", "brand": "Linear", "domain": "linear.app",
  "query": "What is the best issue tracker for a startup engineering team?", "engine": "gemini",
  "success": true, "brandMentioned": true, "mentionPosition": 1, "competitorMentions": ["Jira"],
  "citations": ["https://..."], "answerSummary": "For a startup engineering team, Linear is ...",
  "grounded": true, "geoAuditUrl": null, "charged": true
}
```

## Run it

Set your Apify API token first (Apify Console > Settings > API & Integrations):

```bash
export APIFY_TOKEN=your_token      # PowerShell: $env:APIFY_TOKEN="your_token"
```

| Language | File | Command |
|---|---|---|
| Python | [`python/run.py`](python/run.py) | `pip install apify-client && python python/run.py` |
| JavaScript (Node.js 18+) | [`js/run.mjs`](js/run.mjs) | `npm install apify-client && node js/run.mjs` |
| curl | [`curl.sh`](curl.sh) | `sh curl.sh` |

Python and JavaScript save all rows to `results.json`. The curl recipe uses `run-sync-get-dataset-items`, which waits up to 300 seconds; use the Python or JavaScript client for longer runs.
Every recipe sets a cost cap (`maxTotalChargeUsd`, $1.00): the run stops charging at that amount. Change it for bigger inputs.
