"""Put every part of the map's data together into data.json.
data_base.json: the rows that were on the map before 25 Oct 2026 (decoded from the live page) plus the privatization database.
Then: cases (cases_build.py), Public Futures (pf_rows.json), Mass Mobilization (mm_rows.json), contract awards (wbca.json),
capitals (cap.json), and patterns (waves.json from waves_build.py plus patterns/checked*.json from research)."""
import json, glob, subprocess

W = "/home/claude/work/"
D = json.load(open(W + "data_base.json"))
json.dump(D, open(W + "data.json", "w"))
subprocess.run(["python3", W + "cases_build.py"], check=True)  # adds D.cases into data.json
D = json.load(open(W + "data.json"))
D["pf"] = {"rows": json.load(open(W + "pf_rows.json"))["rows"]}
mm = json.load(open(W + "mm_rows.json"))
D["mm"] = {k: mm[k] for k in ("cols", "rows", "events_in_file")}
D["wbca"] = json.load(open(W + "wbca.json"))
D["cap"] = json.load(open(W + "cap.json"))
pats = []
for f in sorted(glob.glob(W + "patterns/checked*.json")):
    for p in json.load(open(f)):
        if not p.get("remove"): pats.append(p)
pats += json.load(open(W + "waves.json"))
for p in pats:
    p.pop("check_note", None); p.pop("dropped", None)
D["pats"] = pats
json.dump(D, open(W + "data.json", "w"))
print("cases", len(D["cases"]), "pf", len(D["pf"]["rows"]), "mm", len(D["mm"]["rows"]), "patterns", [p["id"] for p in pats])
