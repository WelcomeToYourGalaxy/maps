"""Mass Mobilization Project: every protest event, placed on the map.

Source: Clark and Regan, Mass Mobilization Protest Data, Harvard Dataverse doi:10.7910/DVN/HTTWYL (v5.1, file mmALL_073120).
Placing: the free-text `location` is matched against GeoNames places (cities of 1,000+ people and first-level regions)
inside the event's country, trying the whole text and then each part. Matched to a town or city -> placed there (pc=1);
matched to a region -> region's largest town (pc=2); "national"/no match -> the country's capital (pc=3).
Writes /home/claude/work/mm_rows.json.
"""
import pandas as pd, json, re, unicodedata, collections

G = "/home/claude/dl/geonames/"

def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# country names -> ISO2/ISO3 and capital
ci = {}
for line in open(G + "countryInfo.txt", encoding="utf8"):
    if line.startswith("#"): continue
    f = line.rstrip("\n").split("\t")
    ci[f[0]] = {"iso3": f[1], "name": f[4], "capital": f[5]}
name2iso2 = {norm(v["name"]): k for k, v in ci.items()}
name2iso2.update({norm(k): v for k, v in {
    "Bosnia": "BA", "Congo Brazzaville": "CG", "Congo Kinshasa": "CD", "Ivory Coast": "CI", "Kyrgyzstan": "KG",
    "Laos": "LA", "Macedonia": "MK", "North Korea": "KP", "South Korea": "KR", "Russia": "RU", "Serbia and Montenegro": "RS",
    "Slovak Republic": "SK", "Swaziland": "SZ", "Timor Leste": "TL", "East Timor": "TL", "Burma": "MM", "Myanmar": "MM",
    "Cape Verde": "CV", "Czech Republic": "CZ", "Czechoslovakia": "CZ", "Yugoslavia": "RS", "Germany East": "DE",
    "Germany West": "DE", "Gambia": "GM", "Kosovo": "XK", "Taiwan": "TW", "United Arab Emirate": "AE",
    "United Arab Emirates": "AE", "Vietnam": "VN", "Zaire": "CD", "Democratic Republic of Congo": "CD",
    "Republic of the Congo": "CG", "Netherlands": "NL", "The Netherlands": "NL", "Central African Republic": "CF", "Papua New Guinea": "PG", "Hong Kong": "HK",
}.items()})

places = collections.defaultdict(dict)  # iso2 -> norm name -> (pop, lng, lat, name, fcode)
for line in open(G + "cities1000.txt", encoding="utf8"):
    f = line.split("\t")
    cc, pop = f[8], int(f[14] or 0)
    rec = (pop, float(f[5]), float(f[4]), f[1], f[7], f[10])
    names = {norm(f[1]), norm(f[2])} | {norm(a) for a in f[3].split(",") if a and len(a) < 40}
    for n in names:
        if len(n) < 3: continue
        old = places[cc].get(n)
        if old is None or pop > old[0]: places[cc][n] = rec
# regions -> largest town in that region
adm = collections.defaultdict(dict)
for line in open(G + "admin1CodesASCII.txt", encoding="utf8"):
    code, name, ascii_, _ = line.rstrip("\n").split("\t")
    cc, a1 = code.split(".")
    adm[cc][norm(name)] = a1; adm[cc][norm(ascii_)] = a1
biggest = {}
for cc, d in places.items():
    for rec in d.values():
        k = (cc, rec[5])
        if k not in biggest or rec[0] > biggest[k][0]: biggest[k] = rec
capital = {}
for cc, v in ci.items():
    r = places.get(cc, {}).get(norm(v["capital"]))
    if r: capital[cc] = r

STOP = {"national", "nationwide", "national level", "various", "several cities", "across the country", "countrywide", "unknown", "city", "capital"}

def place(cc, text):
    text = re.sub(r"(?i)\b(national level|nationwide|nation wide|national|country ?wide|across the country)\b", " ", str(text))
    t = norm(text)
    if not t or t in STOP:
        return None
    parts = [t] + [norm(p) for p in re.split(r",|;| and |/|\(|\)| in | near | outside ", str(text)) if norm(p)]
    for p in parts:
        p2 = re.sub(r"^(city of|the|province of|state of|region of|district of|downtown|central)\s+", "", p)
        p2 = re.sub(r"\s+(city|province|region|state|district|county|governorate|department)$", "", p2)
        for q in (p, p2):
            if q in places.get(cc, {}): return places[cc][q], 1
    for p in parts:
        p2 = re.sub(r"\s+(province|region|state|district|county|governorate|department)$", "", p)
        for q in (p, p2):
            a1 = adm.get(cc, {}).get(q)
            if a1 and (cc, a1) in biggest: return biggest[(cc, a1)], 2
    # a known place name appearing as words inside the text (longest first)
    words = t.split()
    for n in range(min(4, len(words)), 0, -1):
        for i in range(len(words) - n + 1):
            q = " ".join(words[i:i + n])
            if len(q) >= 4 and q in places.get(cc, {}) and places[cc][q][0] >= 20000: return places[cc][q], 1
    return None

d = pd.read_csv("/home/claude/dl/mm/mm.tab")
nopro = d[d.protest != 1]
p = d[d.protest == 1].copy()
def cl(x):
    if x is None or (isinstance(x, float) and x != x): return None
    x = str(x).strip()
    return None if x in ("", ".") else x
rows, unmatched_cty, how = [], collections.Counter(), collections.Counter()
for _, r in p.iterrows():
    loc_txt = r["location"] if isinstance(r["location"], str) else ""
    if norm(r["country"]) == "ussr":  # the Soviet Union: look in each of its 15 former republics, else Moscow
        got = None
        for cc in ["RU", "UA", "BY", "LT", "LV", "EE", "MD", "GE", "AM", "AZ", "KZ", "UZ", "TJ", "KG", "TM"]:
            got = place(cc, loc_txt)
        for extra in {"CN": ["HK", "MO"], "RS": ["XK", "ME"]}.get(cc, []):
            if not got:
                got = place(extra, loc_txt)
            if got: break
        if not got: cc = "RU"
    else:
        cc = name2iso2.get(norm(r["country"]))
        if not cc: unmatched_cty[r["country"]] += 1; continue
        got = place(cc, loc_txt)
        for extra in {"CN": ["HK", "MO"], "RS": ["XK", "ME"]}.get(cc, []):
            if not got:
                got = place(extra, loc_txt)
    if got: rec, pc = got
    elif cc in capital: rec, pc = capital[cc], 3
    else: unmatched_cty[r["country"]] += 1; continue
    how[pc] += 1
    dem = [cl(r[f"protesterdemand{i}"]) for i in range(1, 5)]
    res = [cl(r[f"stateresponse{i}"]) for i in range(1, 8)]
    notes = cl(r["notes"]) or ""
    imf = 1 if re.search(r"\bIMF\b|International Monetary Fund|World Bank", notes, re.I) else 0
    def iv(x):
        try: return int(x)
        except: return None
    rows.append([round(rec[1], 4), round(rec[2], 4), ci[cc]["iso3"], str(r["country"]), iv(r["year"]),
                 f"{iv(r['startyear'])}-{iv(r['startmonth']):02d}-{iv(r['startday']):02d}" if iv(r['startmonth']) and iv(r['startday']) else None,
                 f"{iv(r['endyear'])}-{iv(r['endmonth']):02d}-{iv(r['endday']):02d}" if iv(r['endmonth']) and iv(r['endday']) else None,
                 cl(r["location"]), pc, rec[3], cl(r["participants"]), cl(r["protesteridentity"]),
                 [x for x in dem if x], [x for x in res if x], iv(r["protesterviolence"]), notes, cl(r["sources"]), imf, int(r["id"])])
out = {"cols": ["lng", "lat", "iso3", "country", "year", "start", "end", "location", "pc", "placed_at", "participants", "who",
                "demands", "responses", "protester_violence", "notes", "sources", "mentions_imf_wb", "id"],
       "rows": rows, "no_protest_country_years": int(len(nopro)), "events_in_file": int(len(p)),
       "unplaced": dict(unmatched_cty)}
json.dump(out, open("/home/claude/work/mm_rows.json", "w"))
print(len(p), "events;", len(rows), "placed;", dict(how), "unplaced by country:", dict(unmatched_cty))
print("notes mention IMF or World Bank:", sum(r[17] for r in rows))
