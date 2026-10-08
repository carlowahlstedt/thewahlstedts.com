"""Fetch each site's wahlstedt.json (listed in sites.json) into cards.json.

The portal reads cards.json from its own origin, so sites that don't send
CORS headers (e.g. ChatGPT Sites) still get their card. A site that can't be
fetched keeps its previously cached card.
"""
import json
import urllib.request
from urllib.parse import urljoin

FIELDS = ("name", "tagline", "color", "avatar", "url", "cursor")


def hotspot(value):
    """Return value if it's [x, y] with two non-negative numbers, else None."""
    if (isinstance(value, list) and len(value) == 2
            and all(isinstance(n, (int, float)) and not isinstance(n, bool)
                    and 0 <= n < float("inf") for n in value)):
        return value
    return None

with open("sites.json") as f:
    sites = json.load(f)

try:
    with open("cards.json") as f:
        old = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    old = {}

cards = {}
for site in sites:
    base = site["base"]
    src = urljoin(base, "wahlstedt.json")
    try:
        req = urllib.request.Request(src, headers={"User-Agent": "thewahlstedts.com card fetcher"})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.load(r)
        if not isinstance(data, dict):
            raise ValueError("not a JSON object")
        card = {k: data[k] for k in FIELDS if isinstance(data.get(k), str)}
        if hotspot(data.get("cursorHotspot")) is not None:
            card["cursorHotspot"] = data["cursorHotspot"]
        cards[base] = card
        print(f"ok   {src}")
    except Exception as e:
        print(f"fail {src}: {e}")
        if base in old:
            cards[base] = old[base]

with open("cards.json", "w") as f:
    json.dump(cards, f, indent=2, sort_keys=True)
    f.write("\n")
