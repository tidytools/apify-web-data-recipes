# Eventbrite Scraper & Luma Scraper - Events, Venues, Organizers (available from 2026-10-16)

Events from Eventbrite and Luma by city, keyword and date in one table: date and time, venue and address with coordinates, price, sold out, organizer with events hosted and attendees, category. New-event alerts. $2 per 1,000 events, no start fee.

- Apify Store: `apify.com/tidytools/eventbrite-luma-events` (public from 2026-10-16)
- Actor ID: `tidytools/eventbrite-luma-events` (`FuauC7YIAgMTglXiq`)
- MCP (AI agents): `https://mcp.apify.com/?tools=tidytools/eventbrite-luma-events`

> **Not public yet.** This Actor is scheduled to be available on the Apify Store from **2026-10-16**. Until then the recipes below return an error.

## Use case

It collects **events from Eventbrite and Luma in one table**, by city, keyword and date: "AI events in San Francisco this month", "startup events in Berlin", "online marketing webinars". Each event comes with its **date and time (local and UTC), venue, address and coordinates, price range, sold-out state, category and organizer**, including how many events the organizer has run and how many attendees it has hosted.

## Price (pay per event, Apify Free plan)

| Event | Price per 1,000 |
|---|---|
| Event | $2.00 |
| Organizer profile | $2.00 |

Paid plans get the same or lower prices. See the Store page for what is and is not charged.

## Minimal input

This is the Actor's prefilled example input. All other fields have defaults; the full list is on the Store page (Input tab).

```json
{
  "searches": [
    "AI"
  ],
  "locations": [
    "San Francisco, CA"
  ],
  "dateTo": "+30 days",
  "maxEventsPerSearch": 20,
  "maxEvents": 100
}
```

## Sample output

From the Actor's documentation (section "Output example"):

```json
{
    "platform": "eventbrite",
    "eventId": "2000526458490",
    "url": "https://www.eventbrite.com/e/travel-with-ai-tickets-2000526458490",
    "title": "Travel with AI",
    "summary": "Travel with AI is a hands-on introduction to using AI as a practical travel companion.",
    "startDate": "2026-10-09T14:00:00-07:00",
    "startDateUtc": "2026-10-09T21:00:00.000Z",
    "timezone": "America/Los_Angeles",
    "durationMinutes": 60,
    "eventType": "in_person",
    "venueName": "Mechanics' Institute",
    "address": "57 Post Street, San Francisco, CA 94104",
    "city": "San Francisco",
    "region": "CA",
    "country": "US",
    "latitude": 37.7888045,
    "longitude": -122.4030162,
    "isFree": false,
    "priceMin": 0,
    "priceMax": 7.18,
    "currency": "USD",
    "soldOut": false,
    "salesStatus": "on_sale",
    "status": "scheduled",
    "category": "Community",
    "subcategory": "Other",
    "format": "Seminar",
    "organizerName": "Mechanics' Institute",
    "organizerUrl": "https://www.eventbrite.com/o/mechanics-institute-2495482952",
    "organizerEventCount": 1962,
    "organizerTotalAttendees": 57813,
    "organizerFollowers": 2300,
    "organizerWebsite": "https://www.milibrary.org/",
    "organizerSocial": { "x": "https://x.com/milibrary", "facebook": "https://www.facebook.com/MILibrary" },
    "organizerProfileCharged": true,
    "charged": true
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
