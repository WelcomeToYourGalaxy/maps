"""Build the Public Futures point layer.

Reads every case from /home/claude/dl/pf/pf_all.json, decodes classification and
service ids, places each case at the OpenStreetMap feature the database links to
(Nominatim lookup), or, when no feature is linked, by searching the case's place
name within its country (marked approximate). Writes /home/claude/work/pf_rows.json.
"""
import json, time, urllib.request, urllib.parse, os

DIR = "/home/claude/dl/pf/"
UA = {"User-Agent": "WelcomeToYourGalaxy-loan-conditions-map/1.0 (wheelock.chris@gmail.com)"}
CACHE = DIR + "geocache.json"
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}


def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(3 * (i + 1))
    return None


cases = json.load(open(DIR + "pf_all.json"))
types = {t["id"]: t for t in json.load(open(DIR + "types.json"))}
opts = {o["id"]: o for o in json.load(open(DIR + "options.json"))}
svcs = {s["id"]: s for s in json.load(open(DIR + "services.json"))}
secs = {s["id"]: s for s in json.load(open(DIR + "sectors.json"))}

# 1. OSM features linked by the database
need = set()
for c in cases:
    for g in c["location"]["geoFeatures"]:
        f = g["geoFeature"]
        bc = f.get("boundaryCenter")
        key = ("N" + bc["osmIdentifier"]) if bc else (f["osmType"][0].upper() + f["osmIdentifier"])
        if key not in cache: need.add(key)
need = sorted(need)
for i in range(0, len(need), 50):
    chunk = need[i:i + 50]
    res = get("https://nominatim.openstreetmap.org/lookup?format=json&osm_ids=" + ",".join(chunk)) or []
    got = {r["osm_type"][0].upper() + str(r["osm_id"]): [float(r["lon"]), float(r["lat"])] for r in res}
    for k in chunk: cache[k] = got.get(k)
    time.sleep(1.2)
json.dump(cache, open(CACHE, "w"))

# 2. Place-name search for cases with no linked feature (or a failed lookup)
def search(name, cc):
    key = "S|" + (cc or "") + "|" + name
    if key in cache: return cache[key]
    P = {"q": name, "format": "json", "limit": 1}
    if cc: P["countrycodes"] = cc.lower()
    q = urllib.parse.urlencode(P)
    r = get("https://nominatim.openstreetmap.org/search?" + q)
    v = [float(r[0]["lon"]), float(r[0]["lat"])] if r else None
    if v is None and "," in name:  # try the wider part of the name ("Town, Province" -> "Province")
        P["q"] = name.split(",")[-1].strip(); q = urllib.parse.urlencode(P)
        time.sleep(1.1)
        r = get("https://nominatim.openstreetmap.org/search?" + q)
        v = [float(r[0]["lon"]), float(r[0]["lat"])] if r else None
    cache[key] = v
    if len(cache) % 25 == 0: json.dump(cache, open(CACHE, "w"))
    time.sleep(1.1)
    return v


def cls(c, slug):
    out = []
    for x in c["classifications"]:
        t = types.get(x["typeId"])
        if not t or t["slug"] != slug: continue
        if x["optionId"]: out.append(opts.get(x["optionId"], {}).get("name", x["optionId"]))
        elif x["value"] not in (None, ""): out.append(str(x["value"]))
        elif x["number"] is not None: out.append(x["number"])
    return out


rows, unplaced = [], []
seen_slugs = set()
for c in cases:
    for x in c["classifications"]:
        if x["typeId"] in types: seen_slugs.add(types[x["typeId"]]["slug"])
    loc = c["location"]
    xy, approx = None, 0
    for g in loc["geoFeatures"]:
        f = g["geoFeature"]; bc = f.get("boundaryCenter")
        key = ("N" + bc["osmIdentifier"]) if bc else (f["osmType"][0].upper() + f["osmIdentifier"])
        if cache.get(key): xy = cache[key]; break
    if xy is None and loc.get("altName"):
        xy = search(loc["altName"], loc["countryCode"]); approx = 1
    if xy is None:
        unplaced.append({"id": c["id"], "place": loc.get("altName"), "cc": loc["countryCode"]}); continue
    yi = cls(c, "implementation-year"); yd = cls(c, "decision-year")
    services = []
    for s in c["services"]:
        sv = svcs.get(s["serviceId"])
        if sv: services.append(sv["name"] + (" (" + secs[sv["sectorId"]]["name"] + ")" if sv.get("sectorId") in secs else ""))
    J = lambda l: "; ".join(str(v) for v in l)
    rows.append([round(xy[0], 5), round(xy[1], 5), loc["countryCode"], (loc.get("altName") or "").strip(),
                 yi[0] if yi else None, yd[0] if yd else None, J(cls(c, "deprivatisation-type")), J(services),
                 J(cls(c, "previous-provider")), J(cls(c, "current-provider")), J(cls(c, "ownership")), J(cls(c, "actors")),
                 J(cls(c, "actions")), J(cls(c, "governance")), J(cls(c, "organisation")), J(cls(c, "motivation")),
                 approx, c["id"], loc.get("population"), c.get("summary") or "", J(cls(c, "outcome"))])
json.dump(cache, open(CACHE, "w"))
json.dump({"rows": rows, "unplaced": unplaced, "total": len(cases), "slugs": sorted(seen_slugs)}, open("/home/claude/work/pf_rows.json", "w"))
print(len(cases), "cases;", len(rows), "placed;", sum(r[16] for r in rows), "approximate;", len(unplaced), "unplaced")
print("classification types used:", sorted(seen_slugs))
