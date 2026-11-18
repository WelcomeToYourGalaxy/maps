#!/usr/bin/env python3
"""Dedupe OECD Watch complaints against the map, then rank what is worth researching."""
import json, re, os, sys, unicodedata, collections

RAW = "/tmp/oecdw/oecdwatch_raw.json"
BASE = "/home/claude/maps/case-map-src/base.html"

def load_cases():
    s = open(BASE, encoding="utf-8").read()
    i = s.index("window.CASES = ") + len("window.CASES = ")
    return json.JSONDecoder().raw_decode(s[i:])[0]

def norm(t):
    t = unicodedata.normalize("NFKD", (t or "")).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", " ", t.lower())
    return " ".join(t.split())

cases = load_cases()
raw = json.load(open(RAW))

# --- what NCP complaints the map already names, from cx[] rows tagged "ncp"
on_map = {}
for c in cases:
    for h in (c.get("cx") or []):
        if h and h[0] == "ncp":
            on_map[norm(h[1])] = c["id"]
print("NCP complaints already named in cases:", len(on_map))

# also index map cases by company name and by country, for near-matching
by_company = collections.defaultdict(set)
for c in cases:
    for co in (c.get("companies") or []):
        by_company[norm(co.get("name"))].add(c["id"])
    for l in (c.get("lenders") or []):
        by_company[norm(re.sub(r"\(.*", "", l.get("name") or ""))].add(c["id"])

# --- harm words that describe something that happened to people, not a process word
HARM = {
 "killed": r"\b(killed|killing|murder|shot dead|deaths?|died|fatal|massacre)",
 "violence": r"\b(beaten|beating|tortur|assault|shot|wounded|injur|rape|sexual violence|intimidat|threatened|paramilitar|security forces)",
 "detention": r"\b(arrest|detain|detention|imprison|jailed|criminali[sz])",
 "displaced": r"\b(evict|displac|resettl|forced off|relocat|expropriat|land grab|loss of land)",
 "pollution": r"\b(contaminat|pollut|spill|tailings|toxic|poison|waste|emission|deforest|cyanide|mercury|effluent)",
 "health": r"\b(illness|sick|disease|cancer|respiratory|birth defect|health and safety|occupational health)",
 "labour": r"\b(labour|labor|union|collective bargaining|wages?|working condition|dismiss|fired|trafficking|overtime|workers)",
 "water": r"\b(water supply|drinking water|wells?|aquifer|river|fish stock|irrigation)",
 "livelihood": r"\b(livelihood|crops?|farmland|grazing|fishing|harvest|pastoral|subsistence)",
 "indigenous": r"\b(indigenous|tribal|adivasi|first nations|aborigin|prior and informed consent|fpic)",
}


# words that mark an allegation about a process, not an event on the ground
PROC = r"\b(failed to (disclose|consult|respond)|lack of (transparency|disclosure)|due diligence policy|reporting)\b"

DEVELOPED = {"United Kingdom","United States","Germany","France","Netherlands","Canada","Australia",
 "Japan","Norway","Sweden","Denmark","Switzerland","Belgium","Austria","Finland","Ireland","Italy",
 "Spain","New Zealand","Luxembourg","Iceland","Korea, Republic of","Israel","Portugal","Greece"}

out = []
for r in raw:
    text = (r["allegations"] + "\n" + r["outcome"]).lower()
    hits = sorted(k for k, pat in HARM.items() if re.search(pat, text))
    yr = None
    m = re.search(r"\b(19|20)\d{2}\b", r["filed"] or "")
    if m: yr = int(m.group(0))
    countries = r["countries"]
    dev_only = bool(countries) and all(c in DEVELOPED for c in countries)
    key = norm(r["title"])
    match = on_map.get(key)
    if not match:
        # title match is exact-ish only; try the subtitle too
        match = on_map.get(norm(r["subtitle"]))
    comp = norm(r["company_in_violation"] or r["defendant"])
    comp_cases = sorted(by_company.get(comp, []))
    severe = [h for h in hits if h in ("killed","violence","detention","displaced","pollution","health")]
    score = 0
    score += 3 * len(severe)
    score += 1 if ("livelihood" in hits or "water" in hits) else 0
    score += 2 if not dev_only else 0
    score += 2 if len(r["allegations"]) > 900 else (1 if len(r["allegations"]) > 400 else 0)
    score += 1 if r["outcome"] else 0
    score -= 3 if re.search(PROC, text) and not severe else 0
    out.append({**r, "harm_flags": hits, "severe_flags": severe, "year_filed": yr,
                "developed_country_only": dev_only, "already_on_map": match,
                "company_appears_in_cases": comp_cases, "score": score})

out.sort(key=lambda r: (-r["score"], r["year_filed"] or 9999))
json.dump(out, open("/tmp/oecdw/oecdwatch_leads.json","w"), indent=1, ensure_ascii=False)

already = [r for r in out if r["already_on_map"]]
open_ = [r for r in out if not r["already_on_map"]]
print("already matched to a case by title:", len(already))
print("not yet on the map:", len(open_))
print("\nof those not on the map:")
print("  with a severe harm flag:      ", sum(1 for r in open_ if r["severe_flags"]))
print("  harm in a developing country: ", sum(1 for r in open_ if not r["developed_country_only"]))
print("  both:                         ", sum(1 for r in open_ if r["severe_flags"] and not r["developed_country_only"]))
print("  company already in a case:    ", sum(1 for r in open_ if r["company_appears_in_cases"]))
print("\nflag spread (not on map):")
for k,v in collections.Counter(f for r in open_ for f in r["harm_flags"]).most_common():
    print("  %-12s %d" % (k, v))
print("\nby decade filed (not on map):")
for k,v in sorted(collections.Counter((r["year_filed"]//10*10 if r["year_filed"] else 0) for r in open_).items()):
    print("  %s %d" % (k, v))
