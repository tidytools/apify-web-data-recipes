# CSV to JSON & JSON to CSV Converter - Batch, JSON Lines

CSV to JSON and JSON to CSV converter: batch up to 20 pasted CSV, JSON or JSON Lines files per run with Miller; keep, rename and sort columns, download each result. $0.003 per converted file; empty, invalid or too large files are free.

- Apify Store: [https://apify.com/tidytools/tabular-transformer](https://apify.com/tidytools/tabular-transformer)
- Actor ID: `tidytools/tabular-transformer` (`yCPXHdvZWvIgO7HEl`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/tabular-transformer`

## Use case

Give it up to **20 CSV, JSON or JSON Lines files** in one run; it converts each one with [Miller](https://github.com/johnkerl/miller) and saves the result as a file you can download: **CSV to JSON, JSON to CSV, JSON Lines to CSV** and every other pair of the three. Along the way it can **keep only some columns, rename columns and sort the rows**.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Converted file | $3.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "files": [
    {
      "name": "example.csv",
      "dataText": "color,shape,flag,k,index,quantity,rate\nyellow,triangle,true,1,11,43.6498,9.8870\nred,square,true,2,15,79.2778,0.0130\n"
    }
  ]
}
```

## Sample output

From the Actor's documentation (section "Output example (one converted file and the free row of an empty file)"):

```json
[
    {
        "inputIndex": 0,
        "name": "example.csv",
        "outputKey": "OUTPUT-01-example.csv",
        "outputUrl": "https://api.apify.com/v2/key-value-stores/<store id>/records/OUTPUT-01-example.csv",
        "inputBytes": 116,
        "outputBytes": 39,
        "recordCount": 2,
        "success": true,
        "charged": true,
        "errorType": null
    },
    {
        "inputIndex": 1,
        "name": "empty.csv",
        "outputKey": null,
        "inputBytes": 0,
        "outputBytes": null,
        "recordCount": null,
        "success": false,
        "charged": false,
        "errorType": "invalid_input",
        "error": "the file is empty (not charged)"
    }
]
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
