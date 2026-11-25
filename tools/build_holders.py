#!/usr/bin/env python3
"""Who holds each office now, for the government diagrams and the panel.

Reads the OpenSanctions "Politically Exposed Persons" collection
(https://www.opensanctions.org/datasets/peps/), which gathers some 230
official and public sources into one file: national parliaments, regional
assemblies, mayors' registers, cabinet lists, judiciary lists, the US Plum
Book, Plural's state-legislator data, EveryPolitician and Wikidata among
them. OpenSanctions publishes it under CC BY-NC 4.0, free for
non-commercial use with credit; the page credits it wherever a name from
it is shown.

What is kept, and nothing else:
  - a post (OpenSanctions "Position") that has at least one holder whom
    the source marks as current, and that has no dissolution date;
  - for each such holder, the name, the OpenSanctions entity id (so the
    reader can check the record) and the start date where given.
Holders with an end date already past, or a date of death, are left out.
Party posts (topic pol.party) are left out: a party is not a government.
Relatives and close associates, birth dates, addresses, ID numbers and
the rest of a person's record are never read into the output.

Where the post is a Wikidata item, Wikidata says which jurisdiction it
belongs to (P1001); otherwise the source's own "subnational area" text
does. Posts are written per country:

  holders/index.json         built date, credit, per-country counts
  holders/<Q>.json           the country's national posts
  holders/<Q>/<k>.json       posts below the country, in shards; a
                             level of the map finds its own by the key
                             of its Wikidata item ("Q123") or of its name
                             ("n:" + folded name), hashed with FNV-1a

Usage:
  python3 -I tools/build_holders.py                 # download and build
  python3 -I tools/build_holders.py --file X.json   # build from a copy
"""
import json, os, re, sys, shutil, tempfile, unicodedata, urllib.request
from collections import defaultdict, Counter
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_govtree as G          # noqa: E402  (QLever access)

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "holders")
INDEX = "https://data.opensanctions.org/datasets/latest/peps/index.json"
UA = {"User-Agent": "HowToReachThem-holders/1.0 (welcometoyourgalaxy.com)"}
SHARD_BYTES = 180_000
TODAY = date.today().isoformat()

RX_JUD = re.compile(r"\b(court|judge|justice|magistrat|prosecut|tribunal|juez|richter|juge|"
                    r"procura|fiscal|gericht|staatsanwalt)", re.I)
RX_LEG = re.compile(r"\b(parliament|assembly|senat|deput|congress|legislat|councillor|"
                    r"council member|member of|alderm|diet\b|duma|rada|sejm|bundestag|"
                    r"landtag|abgeordnet|conseill|concejal|vereador|regidor|mp\b)", re.I)

def fold(s):
    s = unicodedata.normalize("NFD", str(s or "").lower())
    return "".join(c for c in s if not unicodedata.combining(c) and c.isalnum())

def fnv(s):
    h = 0x811C9DC5
    for b in s.encode("utf-8"):
        h ^= b
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h

# a place name inside a post's title, for local posts the source files
# without a place: "Mayor of Zams", "Councilor, Perolândia-GO",
# "Departmental Councillor for Pas-de-Calais"
RX_PLACE = re.compile(r"(?:,| - | – | of | for | in )\s*([^,]+?)\s*(?:-[A-Za-z]{2})?\s*$")
# the body a post belongs to, where the title names it after the role:
# "Judge, Sofia District Court", "Principal Deputy Director - Office of
# Foreign Missions"
RX_ORG = re.compile(r"^[^,–-]+?(?:,| - | – )\s*(.+)$")
RX_PAREN = re.compile(r"\(([^()]{4,})\)\s*$")
# another country's envoy, filed under the country it is posted to
RX_FOREIGN = re.compile(r"\bambassador of .+ to |\b\w+ ambassador to |\bnuncio to |"
                        r"\bhigh commissioner of .+ to ", re.I)
RX_PARTY = re.compile(r"\bparty\b", re.I)
STOP = {"municipality", "municipal", "city", "town", "village", "county", "district",
        "province", "region", "commune", "of", "the", "de", "do", "da", "des", "du",
        "la", "le", "del", "di", "von", "council", "office", "mayors"}

def place_key(s):
    """the folded name a place is found by, from the source and from the page"""
    s = re.sub(r"\s*\([^)]*\)", "", str(s or ""))
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"['’]s\b", "", s)
    return "".join(w for w in re.split(r"[^\w]+", s) if w and w not in STOP)

def org_of(name):
    m = RX_PAREN.search(name)
    if m and "," in m.group(1): return m.group(1).split(",")[-1].strip()
    m = RX_ORG.match(name)
    if m: return m.group(1).strip()
    m = RX_PAREN.search(name)
    return m.group(1).strip() if m else ""

def dumps(x): return json.dumps(x, ensure_ascii=False, separators=(",", ":"), sort_keys=True)

def isq(s): return bool(s) and re.fullmatch(r"Q\d+", s) is not None

def fetch_file():
    with urllib.request.urlopen(urllib.request.Request(INDEX, headers=UA), timeout=120) as r:
        ix = json.loads(r.read())
    url = next(x["url"] for x in ix["resources"] if x["name"] == "entities.ftm.json")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ftm.json")
    print("downloading", url, flush=True)
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=3600) as r:
        shutil.copyfileobj(r, tmp, 1 << 20)
    tmp.close()
    return tmp.name, ix.get("updated_at", "")

def branch(topics, name):
    t = set(topics)
    if t & {"gov.judicial", "role.judge"}: return "jud"
    if "gov.legislative" in t and "gov.executive" not in t: return "leg"
    if t & {"gov.executive", "gov.head", "gov.security", "gov.financial", "gov.soe",
            "gov.admin", "role.diplo"}: return "exe"
    if "gov.legislative" in t: return "leg"
    if "gov.religion" in t: return "other"
    if RX_JUD.search(name): return "jud"
    if RX_LEG.search(name): return "leg"
    return "exe"

def read(path):
    pos, occ, ppl = {}, [], {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            e = json.loads(line)
            s, p = e["schema"], e["properties"]
            if s == "Position":
                if p.get("dissolutionDate"): continue
                tp = p.get("topics", [])
                if "pol.party" in tp: continue
                nm = e.get("caption") or (p.get("name") or [""])[0]
                if RX_FOREIGN.search(nm): continue
                if RX_PARTY.search(nm) and not re.search(r"working party", nm, re.I): continue
                wd = e["id"] if isq(e["id"]) else next((x for x in p.get("wikidataId", []) if isq(x)), None)
                pos[e["id"]] = {"l": nm, "q": wd,
                                "cc": p.get("country", []), "sub": p.get("subnationalArea", []),
                                "tp": tp, "ds": e.get("datasets", [])}
            elif s == "Occupancy":
                if p.get("status") != ["current"]: continue
                end = min(p.get("endDate", []) or ["9999"])
                if end < TODAY: continue
                occ.append((p["post"][0], p["holder"][0], min(p.get("startDate", []) or [""])))
            elif s == "Person":
                if p.get("deathDate"): continue
                ppl[e["id"]] = e.get("caption") or (p.get("name") or [""])[0]
    return pos, occ, ppl

def jurisdictions(qs):
    """position Q -> the jurisdictions Wikidata gives it (P1001)"""
    out = defaultdict(list)
    for ch in G.chunks(sorted(qs), 2000):
        rows = G.ask("SELECT ?p ?j WHERE { VALUES ?p { %s } ?p wdt:P1001 ?j }" % G.vals(ch), timeout=600)
        for r in rows:
            j = G.v(r, "j")
            if isq(j): out[G.v(r, "p")].append(j)
    return out

def countries():
    """ISO 3166-1 alpha-2 (lower case) -> the country item the diagrams use"""
    gov = set(json.load(open(os.path.join(ROOT, "govtree", "index.json")))["c"])
    rows = G.ask("SELECT ?c ?iso WHERE { ?c wdt:P297 ?iso }")
    m = {}
    for r in rows:
        c, iso = G.v(r, "c"), (G.v(r, "iso") or "").lower()
        if not iso: continue
        if c in gov or iso not in m: m[iso] = c
    if "nl" in m and "Q55" in gov: m["nl"] = "Q55"
    return m

# ---------- France: every elected councillor, from the Répertoire national
# des élus (Ministry of the Interior, Licence Ouverte 2.0). OpenSanctions
# carries France's mayors and parliament; the register adds every
# municipal, departmental and regional councillor and the assemblies of
# Corsica, Martinique and Guiana. Places are found by their INSEE codes
# (P374 commune, P2586 department, P2585 region), which Wikidata holds.
RNE_DS = "https://www.data.gouv.fr/api/1/datasets/repertoire-national-des-elus-1/"
RNE_PAGE = "https://www.data.gouv.fr/fr/datasets/repertoire-national-des-elus-1/"
RNE_FILES = [  # title words, post label, INSEE property, code column, name column
    ("conseillers-municipaux", "Municipal council", "P374", "commune", "commune"),
    ("conseillers-departementaux", "Departmental council", "P2586", "departement", "departement"),
    ("conseillers-regionaux", "Regional council", "P2585", "region", "region"),
    ("membres-assemblee", "Assembly", None, "collectivite", "collectivite"),
]

def _hfold(h):
    h = unicodedata.normalize("NFD", h.lower())
    return "".join(c for c in h if c.isalpha())

def _insee(prop):
    out = {}
    rows = G.ask("SELECT ?x ?c WHERE { ?x wdt:%s ?c . FILTER NOT EXISTS { ?x wdt:P576 [] } "
                 "FILTER NOT EXISTS { ?x wdt:P1366 [] } }" % prop, timeout=600)
    for r in rows:
        c = (G.v(r, "c") or "").upper().lstrip("0") or "0"
        x = G.v(r, "x")
        if isq(x) and c not in out: out[c] = x
    return out

def _fr_date(s):
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s or "")
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else (s or "")[:10]

def rne(area):
    import csv, io
    with urllib.request.urlopen(urllib.request.Request(RNE_DS, headers=UA), timeout=120) as r:
        ds = json.loads(r.read())
    total = 0
    for words, label, prop, codecol, namecol in RNE_FILES:
        res = next((x for x in ds["resources"] if words in x["title"].lower()), None)
        if not res:
            print("RNE: no file for", words); continue
        with urllib.request.urlopen(urllib.request.Request(res["url"], headers=UA), timeout=900) as r:
            raw = r.read()
        try: text = raw.decode("utf-8-sig")
        except UnicodeDecodeError: text = raw.decode("latin-1")
        first = text.split("\n", 1)[0]
        delim = max(";,\t", key=first.count)
        rd = csv.reader(io.StringIO(text), delimiter=delim)
        head = [_hfold(h) for h in next(rd)]
        print("RNE", words, "columns:", head, flush=True)
        def col(*need, avoid=()):
            for i, h in enumerate(head):
                if all(n in h for n in need) and not any(a in h for a in avoid): return i
            return None
        c_last = col("nom", avoid=("prenom", "libelle", "code", "usage"))
        c_first = col("prenom")
        c_code = col("code", codecol, avoid=("libelle",))
        c_name = col("libelle", namecol)
        c_dept = col("libelle", "departement")
        c_start = col("date", "debut", "mandat")
        c_end = col("date", "fin", "mandat")
        c_fn = col("libelle", "fonction")
        if c_last is None or c_first is None or c_name is None:
            print("RNE: columns not recognised in", words); continue
        codes = _insee(prop) if prop else {}
        posts = {}
        for row in rd:
            if len(row) < len(head): continue
            if c_end is not None and row[c_end].strip() and _fr_date(row[c_end]) < TODAY: continue
            place = row[c_name].strip()
            code = (row[c_code].strip().upper().lstrip("0") or "0") if c_code is not None else ""
            # a commune code is department + commune; Wikidata holds the
            # five-character form, the register sometimes the three
            if prop == "P374" and c_dept is not None and len(code) <= 3:
                dc = row[col("code", "departement", avoid=("libelle",))].strip() if col("code", "departement", avoid=("libelle",)) is not None else ""
                code = (dc + row[c_code].strip().zfill(3)).upper().lstrip("0")
            key = codes.get(code) or ("n:" + place_key(place) if place_key(place) else None)
            if not key: continue
            fn = row[c_fn].strip() if c_fn is not None else ""
            name = (row[c_first].strip() + " " + row[c_last].strip()).strip()
            if fn: name += " (" + fn + ")"
            p = posts.get(key)
            if not p:
                p = posts[key] = {"l": label, "b": "leg", "src": "rne", "h": []}
                if key.startswith("n:"):
                    if prop != "P374": p["lv"] = "s"
                    else:
                        p["lv"] = "m"
                        if c_dept is not None and place_key(row[c_dept]): p["in"] = place_key(row[c_dept])
            p["h"].append([name, "", _fr_date(row[c_start]) if c_start is not None else ""])
        for key, p in posts.items():
            # the head of the council first, then everyone by name
            p["h"].sort(key=lambda x: (0 if re.search(r"\((maire|pr[ée]sident)", x[0], re.I) else 1, x[0]))
            area[key].append(p)
            total += len(p["h"])
        print(f"RNE {words}: {len(posts)} places, {sum(len(p['h']) for p in posts.values())} councillors", flush=True)
    return total

def main():
    a = sys.argv[1:]
    if "--file" in a: path, built = a[a.index("--file") + 1], ""
    else: path, built = fetch_file()
    pos, occ, ppl = read(path)
    print(f"{len(pos)} posts, {len(occ)} current holdings, {len(ppl)} people", flush=True)

    held = defaultdict(dict)
    for post, who, since in occ:
        if post not in pos or who not in ppl: continue
        h = held[post]
        if who not in h or (since and since > (h[who] or "")): h[who] = since
    pos = {k: v for k, v in pos.items() if k in held}
    print(f"{len(pos)} posts with a current holder", flush=True)

    J = jurisdictions({v["q"] for v in pos.values() if v["q"]})
    C = countries()

    nat = defaultdict(list); area = defaultdict(lambda: defaultdict(list)); miss = Counter()
    for pid, v in pos.items():
        rec = {"l": v["l"], "b": branch(v["tp"], v["l"]),
               "h": sorted(([ppl[w], w, s or ""] for w, s in held[pid].items()),
                           key=lambda x: x[0])}
        if v["q"]: rec["q"] = v["q"]
        if "gov.head" in v["tp"]: rec["hd"] = 1
        ccs = [C[c] for c in v["cc"] if c in C] or []
        if not ccs:
            miss[",".join(v["cc"]) or "-"] += 1
            continue
        cq = ccs[0]
        keys = [j for j in J.get(v["q"], []) if j not in ccs]
        if not keys and v["sub"]:
            # "Lyon, Rhône": the place, then what it sits in, which tells
            # one Saint-Martin from the next
            for x in v["sub"]:
                head, _, tail = x.partition(",")
                if place_key(head) and "n:" + place_key(head) not in keys:
                    keys.append("n:" + place_key(head))
                    if place_key(tail) and "in" not in rec: rec["in"] = place_key(tail)
        loc = "m" if "gov.muni" in v["tp"] else "s" if "gov.state" in v["tp"] else ""
        if not keys and loc:
            m = RX_PLACE.search(v["l"])
            if m and place_key(m.group(1)): keys = ["n:" + place_key(m.group(1))]
        if loc and not v["q"]: rec["lv"] = loc
        if not keys:
            o = org_of(v["l"])
            if o: rec["o"] = o
        if keys:
            for k in keys: area[cq][k].append(rec)
        else:
            nat[cq].append(rec)

    also = []
    if "--no-rne" not in a:
        try:
            n_rne = rne(area["Q142"])
            if n_rne: also.append({"src": "rne", "n": "Répertoire national des élus",
                                   "url": RNE_PAGE, "lic": "Licence Ouverte 2.0", "h": n_rne})
        except Exception as e:
            print("RNE skipped:", e, flush=True)

    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    ix = {"built": TODAY, "data": built,
          "src": "OpenSanctions, Politically Exposed Persons",
          "url": "https://www.opensanctions.org/datasets/peps/",
          "lic": "CC BY-NC 4.0", "also": also, "c": {}}
    every = set(nat) | set(area)
    for cq in sorted(every):
        n = sorted(nat.get(cq, []), key=lambda r: (0 if r.get("hd") else 1, r["l"]))
        if n:
            with open(os.path.join(OUT, cq + ".json"), "w", encoding="utf-8") as f:
                f.write('{"q":%s,"p":[\n%s\n]}\n' % (json.dumps(cq), ",\n".join(dumps(r) for r in n)))
        A = area.get(cq, {})
        size = sum(len(json.dumps(r, ensure_ascii=False)) for rs in A.values() for r in rs)
        sh = max(1, -(-size // SHARD_BYTES)) if A else 0
        if A:
            os.makedirs(os.path.join(OUT, cq))
            parts = defaultdict(dict)
            for k, rs in A.items(): parts[fnv(k) % sh][k] = rs
            for i in range(sh):
                P = parts.get(i, {})
                with open(os.path.join(OUT, cq, f"{i}.json"), "w", encoding="utf-8") as f:
                    # one place a line, in a fixed order, so a week's
                    # changes are a few lines in git rather than the file
                    f.write("{\n" + ",\n".join("%s:%s" % (json.dumps(k), dumps(sorted(P[k], key=lambda r: r["l"])))
                                                for k in sorted(P)) + "\n}\n")
        ix["c"][cq] = {"n": len(n), "a": sum(len(x) for x in A.values()), "k": len(A), "sh": sh,
                       "h": sum(len(r["h"]) for r in n) + sum(len(r["h"]) for rs in A.values() for r in rs)}
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
        json.dump(ix, f, ensure_ascii=False, separators=(",", ":"))
    tot = sum(x["h"] for x in ix["c"].values())
    print(f"{len(every)} countries, {tot} current holders written; no country for {sum(miss.values())} posts:",
          miss.most_common(8))
    if "--file" not in a: os.unlink(path)

if __name__ == "__main__":
    main()
