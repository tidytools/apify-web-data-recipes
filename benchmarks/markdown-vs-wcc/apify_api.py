"""Tiny Apify API helper for the Markdown benchmark. Reads your token from the APIFY_TOKEN environment variable."""
import json, os, urllib.request


def token():
    t = os.environ.get("APIFY_TOKEN", "").strip()
    if not t:
        raise SystemExit("Set APIFY_TOKEN (https://console.apify.com/settings/integrations) to start or refresh runs.")
    return t


def api(method, path, body=None, raw=False, timeout=300):
    req = urllib.request.Request("https://api.apify.com/v2" + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"authorization": "Bearer " + token(), "content-type": "application/json"})
    r = urllib.request.urlopen(req, timeout=timeout).read()
    return r.decode("utf-8", "replace") if raw else json.loads(r)
