"""Slice the OSM office extract into 2-degree cells the map can fetch one
at a time, instead of one 60 MB file nobody waits for.

Reads offices_<kind>.json from the executive-map repo. Those rows carry
  0 lat  1 lon  2 name  3 website  4 operator  5 address
  6 phone  7 email  8 opening_hours  9 wikidata
and are produced by executive-map/extract_osm_offices.py.

The earlier version of this script read a phone from r[7] and an email
from r[8] of the OLD execmap_local_*.json rows, which only ran to index 5.
Those fields did not exist, so every cell went out with an empty phone and
an empty email -- 1,360 phones and 903 emails across 670,850 features.
"""
import json, os, glob, collections

SRC = "/home/claude/executive-map"
OUT = "/home/claude/maps/contacts"
SZ = 2
KIND = {'townhall': 't', 'govoffice': 'g', 'ministry': 'm', 'police': 'p',
        'firestation': 'f', 'prison': 'r', 'diplomatic': 'd'}

def clean(v):
    if not isinstance(v, str):
        return ""
    v = v.strip()
    return "" if v in ("", "-", "?") else v

def at(r, i):
    return clean(r[i]) if len(r) > i else ""

cells = collections.defaultdict(list)
counts = collections.Counter()
fill = collections.Counter()

for k, code in KIND.items():
    f = os.path.join(SRC, "offices_%s.json" % k)
    if not os.path.exists(f):
        print("missing", f)
        continue
    for r in json.load(open(f)):
        if len(r) < 3:
            continue
        try:
            lat = float(r[0]); lon = float(r[1])
        except (TypeError, ValueError):
            continue
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            continue
        name = clean(r[2])
        if not name:
            continue
        site, oper, addr = at(r, 3), at(r, 4), at(r, 5)
        phone, email = at(r, 6), at(r, 7)
        hours, wd = at(r, 8), at(r, 9)
        rec = [round(lat, 5), round(lon, 5), name, code,
               site, phone, email, addr, oper, hours, wd]
        while len(rec) > 4 and rec[-1] == "":
            rec.pop()
        cells[(int((lon + 180) // SZ), int((lat + 90) // SZ))].append(rec)
        counts[code] += 1
        for nm, v in (("website", site), ("phone", phone), ("email", email),
                      ("address", addr), ("hours", hours), ("wikidata", wd)):
            if v:
                fill[nm] += 1

os.makedirs(OUT, exist_ok=True)
for old in glob.glob(os.path.join(OUT, "*.json")):
    os.remove(old)
idx = []
for (x, y), rs in cells.items():
    p = os.path.join(OUT, "%d_%d.json" % (x, y))
    json.dump(rs, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
    idx.append("%d_%d" % (x, y))
json.dump({"size": SZ, "cells": sorted(idx),
           "kinds": {"t": "town hall", "g": "government office",
                     "m": "ministry or department", "p": "police",
                     "f": "fire station", "r": "prison", "d": "diplomatic"},
           "fields": ["lat", "lon", "name", "kind", "website", "phone",
                      "email", "address", "operator", "hours", "wikidata"],
           "source": "OpenStreetMap via WelcomeToYourGalaxy/executive-map"},
          open(os.path.join(OUT, "index.json"), "w"), separators=(",", ":"))

tot = sum(len(v) for v in cells.values())
print("cells:", len(cells))
print("rows:", tot)
print("by kind:", dict(counts))
print("field fill:", {k: "%d (%.1f%%)" % (v, 100.0 * v / tot) for k, v in fill.items()})
