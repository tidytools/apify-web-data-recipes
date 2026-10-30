# Time Series Forecasting - AI Sales & Demand Forecast

Forecast sales, demand, traffic or any time series from CSV, a Google Sheet or JSON with Mistral AI's Timestral model: median forecast, prediction intervals, future dates and an optional backtest. Runs inside the Actor. $0.02 per series; too-short series are free.

- Apify Store: [https://apify.com/tidytools/time-series-forecast](https://apify.com/tidytools/time-series-forecast)
- Actor ID: `tidytools/time-series-forecast` (`COSoOaCPkdPftrS9W`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/time-series-forecast`

## Use case

**Forecast any time series in one step**: paste a CSV, upload a spreadsheet export, link a Google Sheet or send JSON, and get the **median forecast**, **prediction intervals** (any quantiles you choose) and the **future dates** for every series. Sales, demand, orders, website traffic, prices, sensor readings, KPIs: if it is a column of numbers over time, it can be forecast. **$0.02 per series, no start fee; series that are too short or unreadable are free.**

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Series forecast | $20.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "data": "Month,Passengers\n1957-01,315\n1957-02,301\n1957-03,356\n1957-04,348\n1957-05,355\n1957-06,422\n1957-07,465\n1957-08,467\n1957-09,404\n1957-10,347\n1957-11,305\n1957-12,336\n1958-01,340\n1958-02,318\n1958-03,362\n1958-04,348\n1958-05,363\n1958-06,435\n1958-07,491\n1958-08,505\n1958-09,404\n1958-10,359\n1958-11,310\n1958-12,337\n1959-01,360\n1959-02,342\n1959-03,406\n1959-04,396\n1959-05,420\n1959-06,472\n1959-07,548\n1959-08,559\n1959-09,463\n1959-10,407\n1959-11,362\n1959-12,405\n1960-01,417\n1960-02,391\n1960-03,419\n1960-04,461\n1960-05,472\n1960-06,535\n1960-07,622\n1960-08,606\n1960-09,508\n1960-10,461\n1960-11,390\n1960-12,432",
  "horizon": 12,
  "quantiles": [
    0.1,
    0.9
  ],
  "evaluate": true
}
```

## Sample output

From the Actor's documentation (section "Output example (local test run, 22 October 2026: airline passengers, monthly, linked from GitHub)"):

```json
{
    "seriesId": "Passengers",
    "success": true,
    "charged": true,
    "model": "Timestral-123M",
    "frequency": "month",
    "horizon": 12,
    "lastTimestamp": "1960-12-01",
    "lastValue": 432,
    "forecastStart": "1961-01-01",
    "forecastEnd": "1961-12-01",
    "nextMedian": 446.494,
    "nextLow": 431.479,
    "nextHigh": 462.438,
    "forecast": [
        { "step": 1, "timestamp": "1961-01-01", "median": 446.494, "q10": 431.479, "q90": 462.438 },
        { "step": 2, "timestamp": "1961-02-01", "median": 417.213, "q10": 398.03, "q90": 436.536 },
        { "step": 3, "timestamp": "1961-03-01", "median": 469.775, "q10": 447.229, "q90": 491.618 }
    ],
    "backtest": {
        "holdoutSteps": 12,
        "holdoutStart": "1960-01-01",
        "maeModel": 9.0749,
        "maeSeasonalNaive": 47.8333,
        "maseModel": 0.298,
        "maseSeasonalNaive": 1.5709,
        "errorVsSeasonalNaivePct": -81,
        "beatsSeasonalNaive": true,
        "intervalLevel": "10-90",
        "intervalCoverage": 0.917
    },
    "runtimeSecs": 0.644
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
