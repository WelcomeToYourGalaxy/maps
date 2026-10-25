"""Merge the cases into data.json under D.cases.

From the globalization map: its privatization, trade-opening and austerity cases, as published there.
New: the researched cases after fact-checking (cases/checked*.json), minus any marked remove.
"""
import json, glob

D = json.load(open("/home/claude/work/data.json"))
KEEP = ["id", "title", "place", "iso3", "lat", "lng", "point", "start", "end", "mechanism", "lenders", "conditions", "companies",
        "community", "suppression", "killed", "killed_note", "outcome", "sources", "confidence", "confidence_note"]
old = json.load(open("/home/claude/work/cases/from_glob.json"))
new = []
for f in sorted(glob.glob("/home/claude/work/cases/checked*.json")):
    new += json.load(open(f))
removed = [c for c in new if c.get("remove")]
new = [c for c in new if not c.get("remove")]
# Company head-office cities the fact-checkers found no source for.
NOHQ = {"Tractebel", "Southern Bank Berhad", "ABSA", "Hydro-Québec", "Elyo", "Globeleq", "Eskom", "Mando", "Actis", "Unión Fenosa", "Union Fenosa", "BSES"}
out = []
for c in old + new:
    x = {k: c.get(k) for k in KEEP}
    for co in x["companies"] or []:
        for k in ("hq_lat", "hq_lng"): co.pop(k, None)
        if c in new and "orissa" in c["id"].lower() and (co.get("name") or "").startswith("AES"): co["hq"] = None
        if c in new and any((co.get("name") or "").startswith(n) for n in NOHQ): co["hq"] = None
    assert isinstance(x["lat"], (int, float)) and isinstance(x["lng"], (int, float)), x["id"]
    assert x["mechanism"] in ("privatization", "austerity", "trade", "law"), (x["id"], x["mechanism"])
    out.append(x)
ids = [c["id"] for c in out]
assert len(ids) == len(set(ids)), [i for i in ids if ids.count(i) > 1]
D["cases"] = out
json.dump(D, open("/home/claude/work/data.json", "w"))
print(len(old), "from the globalization map;", len(new), "new;", len(removed), "removed by checkers:", [c["title"] for c in removed])
