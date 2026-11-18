#!/usr/bin/env python3
"""Build muni/ — the municipal contact shards the page fetches per level.

    python3 -I tools/build_muni.py                # every country
    python3 -I tools/build_muni.py ITA            # one of them
    python3 -I tools/build_muni.py --out /tmp/m   # somewhere else

Each country is one entry in COUNTRIES: read the government's own register,
join it to Wikidata on a code both sides publish, and key the result by the
Wikidata id, which is what the panel has already resolved for the level a
reader clicked. No name matching at read time and none at build time either,
except where a country publishes no shared code at all and the four
conditions in the handoff's round-fifteen section are all met.

The rules the whole file turns on, and none of them is negotiable:

1. **Never derive an address.** A record states one or there is none. No
   guessing `cityname.gov`, no appending `/contact`.
2. **Refuse an ambiguous join in both directions.** A code that maps to two
   live Wikidata items is dropped and counted; so is a Wikidata id claimed
   by two register rows, which is the one `put()` was missing until round
   twelve found 76 of them — the second row simply overwrote the first and
   the page then showed one municipality's telephone number under
   another's name.
3. **Check the join against a field it never touches**, with a floor under
   it that stops the country shipping. Italy's check is the official name
   against Wikidata's Italian label; Quebec's is the name against the French
   label, because its two code systems are nearly the same code and a slip
   could in principle land on another municipality.
4. **Say where every record came from.** `src` per record, so three sources
   can disagree visibly rather than silently overwriting each other.
5. **Ship what the register publishes, not a tidied subset.** A row with a
   telephone number and no email is a record, not a blank.
"""
import csv, io, json, os, re, sys, time, unicodedata
import urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHARDS = 512

# ---------------------------------------------------------------- endpoints

QL = ["https://qlever.dev/api/wikidata",
      "https://qlever.cs.uni-freiburg.de/api/wikidata",
      "https://query.wikidata.org/sparql"]
PRE = ("PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
       "PREFIX wd: <http://www.wikidata.org/entity/> "
       "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ")
UA = "HowToReachThem/1.0 (welcometoyourgalaxy.com; municipal contact build)"

def sparql(q, tries=3):
    """QLever first. Wikidata's own service has been answering `429
    Aggressively rate-limiting to 1 req / min` through an outage, which makes
    a build of this shape impossible; QLever holds the same dump and answers
    in milliseconds. It is a third party and its index is a dump rather than
    the live store, so every figure here is as of that dump."""
    body = urllib.parse.urlencode({"query": PRE + q}).encode()
    last = ""
    for ep in QL:
        for att in range(tries):
            try:
                rq = urllib.request.Request(ep, data=body, headers={
                    "Accept": "application/sparql-results+json",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": UA})
                with urllib.request.urlopen(rq, timeout=300) as r:
                    return json.loads(r.read())["results"]["bindings"]
            except Exception as e:
                last = f"{ep}: {e}"
                time.sleep(2 * (att + 1))
    raise SystemExit("every endpoint refused: " + last)

def get(url, timeout=300):
    rq = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(rq, timeout=timeout) as r:
        return r.read()

# ---------------------------------------------------------------- the join

class Build:
    """One country's records, with both directions of ambiguity refused."""
    def __init__(self, iso3, src):
        self.iso3, self.src = iso3, src
        self.rec = {}            # qid -> record
        self.claimed = {}        # qid -> how many rows claimed it
        self.dropped_ambig_code = 0
        self.dropped_ambig_item = 0
        self.dropped_nocode = 0
        self.dropped_nocontact = 0

    def put(self, qid, rec):
        if not rec:
            self.dropped_nocontact += 1
            return
        self.claimed[qid] = self.claimed.get(qid, 0) + 1
        if self.claimed[qid] > 1:
            # two register rows for one jurisdiction: the page looks a place
            # up by its id and prints what it finds, so this is the same
            # fault as an ambiguous code reached from the other end. Both go.
            self.rec.pop(qid, None)
            self.dropped_ambig_item += 1
            return
        rec["src"] = self.src
        self.rec[qid] = rec

    def report(self):
        f = {}
        for r in self.rec.values():
            for k in r:
                f[k] = f.get(k, 0) + 1
        return {"shipped": len(self.rec),
                "refused_code_maps_to_two_items": self.dropped_ambig_code,
                "refused_item_claimed_twice": self.dropped_ambig_item,
                "no_shared_code": self.dropped_nocode,
                "register_publishes_no_contact": self.dropped_nocontact,
                "fields": f}

def index_by_code(rows, key):
    """code -> the one live Wikidata id holding it, or nothing. A code on two
    items is not a key, which is the Sardinian lesson from the other end."""
    seen = {}
    for qid, vals in rows.items():
        for v in vals.get(key, []):
            v = str(v).strip()
            if not v:
                continue
            seen.setdefault(v, set()).add(qid)
    return ({c: next(iter(s)) for c, s in seen.items() if len(s) == 1},
            sum(1 for s in seen.values() if len(s) > 1))

def fold(s):
    """For the *check*, never for the join."""
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def gate(name, agree, total, floor):
    share = (agree / total) if total else 0.0
    print(f"    gate: {name} agrees on {agree:,} of {total:,} ({share:.2%}), "
          f"floor {floor:.0%}")
    if share < floor:
        raise SystemExit(f"    REFUSED: {name} below its floor — not shipping "
                         f"this country. A scrambled join sits near zero here, "
                         f"so check the code systems before lowering it.")
    return share

# ---------------------------------------------------------------- Italy

def build_italy():
    """IPA, the index of digital addresses the Italian public administration
    keeps of itself. Category L6 holds the comuni plus their consortia; the
    rows whose name begins "comune" are the comuni themselves.

    Two keys, both exact joins on a published code. Sardinia's provinces were
    reorganised in 2016 and the ISTAT codes reissued, so IPA carries the
    current code and Wikidata the pre-2016 one for a couple of hundred of
    them — the cadastral code did not change and picks up exactly that
    residue."""
    pkg = json.loads(get("https://www.indicepa.gov.it/ipa-dati/api/3/action/"
                         "package_show?id=enti").decode())
    url = next(r["url"] for r in pkg["result"]["resources"]
               if r.get("format") == "XLSX")
    print("    register:", url)
    raw = get(url)
    open("/tmp/enti.xlsx", "wb").write(raw)
    import openpyxl
    sh = openpyxl.load_workbook("/tmp/enti.xlsx", read_only=True).worksheets[0]
    it = sh.iter_rows(values_only=True)
    hdr = list(next(it))
    I = {h: i for i, h in enumerate(hdr)}
    rows = [r for r in it
            if r[I["Codice_Categoria"]] == "L6"
            and str(r[I["Denominazione_ente"]] or "").strip().lower().startswith("comune")]
    print(f"    {len(rows):,} comuni in the register")

    # `wdt:P31/wdt:P279*` and not a direct instance: 298 comuni are typed as a
    # subclass of "comune of Italy" (Valle d'Aosta's among them) and every one
    # of them carries the right code.
    wd = {}
    for r in sparql("""SELECT ?x ?istat ?cad ?lab WHERE {
            ?x wdt:P31/wdt:P279* wd:Q747074 .
            FILTER NOT EXISTS { ?x wdt:P576 ?d }
            OPTIONAL { ?x wdt:P635 ?istat }
            OPTIONAL { ?x wdt:P806 ?cad }
            OPTIONAL { ?x rdfs:label ?lab . FILTER(LANG(?lab)='it') } }"""):
        qid = r["x"]["value"].rsplit("/", 1)[-1]
        e = wd.setdefault(qid, {"istat": set(), "cad": set(), "lab": ""})
        if "istat" in r: e["istat"].add(r["istat"]["value"])
        if "cad" in r: e["cad"].add(r["cad"]["value"])
        if "lab" in r and not e["lab"]: e["lab"] = r["lab"]["value"]
    print(f"    {len(wd):,} live comune items on Wikidata")

    by_istat, amb_i = index_by_code(wd, "istat")
    by_cad, amb_c = index_by_code(wd, "cad")

    b = Build("ITA", "IPA")
    b.dropped_ambig_code = amb_i + amb_c
    agree = checked = 0
    for r in rows:
        istat = str(r[I["Codice_comune_ISTAT"]] or "").strip()
        cad = str(r[I["Codice_catastale_comune"]] or "").strip()
        qid = by_istat.get(istat) or by_cad.get(cad)
        if not qid:
            b.dropped_nocode += 1
            continue
        # the check: the register's own name against Wikidata's Italian label,
        # a field the join never looks at
        nm = fold(re.sub(r"^comune\s+(di|d')\s*", "",
                         str(r[I["Denominazione_ente"]]).strip(), flags=re.I))
        lab = fold(wd[qid]["lab"])
        if lab:
            checked += 1
            if nm == lab or nm in lab or lab in nm:
                agree += 1
        rec = {}
        site = str(r[I["Sito_istituzionale"]] or "").strip()
        if site:
            # IPA prints most of them as a bare hostname. A scheme is not an
            # address derived from anything: it is how a hostname is fetched.
            rec["u"] = site if site.startswith(("http://", "https://")) else "https://" + site
        pec, other = [], []
        for k in range(1, 6):
            m = str(r[I["Mail%d" % k]] or "").strip()
            t = str(r[I["Tipo_Mail%d" % k]] or "").strip().lower()
            if not m:
                continue
            (pec if t == "pec" else other).append(m)
        if other: rec["e"] = other
        # A PEC refuses mail from an ordinary account, so it is offered under
        # its own name saying so, never as an email address.
        if pec: rec["c"] = pec
        addr = str(r[I["Indirizzo"]] or "").strip()
        cap = str(r[I["CAP"]] or "").strip()
        if addr: rec["a"] = (addr + " " + cap).strip()
        b.put(qid, rec)
    gate("official name against the Italian label", agree, checked, 0.95)
    return b

# ---------------------------------------------------------------- Quebec

QC_POSTS = [("dirgen", "Director general"), ("gref", "Clerk"),
            ("tres", "Treasurer"), ("sectres", "Secretary-treasurer"),
            ("dirsecpub", "Director of public safety"), ("polic", "Police"),
            ("incen", "Fire"), ("loisir", "Recreation"),
            ("trvpub", "Public works"), ("mesurg", "Emergency measures"),
            ("urban", "Planning"), ("communic", "Communications"),
            ("permis", "Permits"), ("batim", "Buildings")]

def build_quebec():
    """Canada keeps no national register of municipal contacts and the
    provinces keep their own, so this is a province rather than a country.
    The shards do not care: they are keyed by Wikidata id and the loader
    checks the ISO3 in index.json before fetching anything.

    The trap is two codes that are nearly the same code. The register keys
    each row by the ministry's five-digit geographic code; Wikidata holds the
    seven-digit Statistics Canada code, whose last five digits are usually
    those same five. Usually: where they slip the row does not join and is
    counted, and because a slip could in principle land on another
    municipality's code this is the one join here whose result is verified
    against the official name rather than trusted."""
    t = get("https://donneesouvertes.affmunqc.net/repertoire/MUN.csv").decode("utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(t)))
    print(f"    {len(rows):,} municipal organisations in the register")

    wd = {}
    for r in sparql("""SELECT ?x ?sgc ?lab WHERE {
            ?x wdt:P3012 ?sgc ; wdt:P17 wd:Q16 .
            FILTER NOT EXISTS { ?x wdt:P576 ?d }
            OPTIONAL { ?x rdfs:label ?lab . FILTER(LANG(?lab)='fr') } }"""):
        qid = r["x"]["value"].rsplit("/", 1)[-1]
        e = wd.setdefault(qid, {"sgc": set(), "lab": ""})
        e["sgc"].add(r["sgc"]["value"])
        if "lab" in r and not e["lab"]: e["lab"] = r["lab"]["value"]
    # The last five digits of a seven-digit code, which is what the ministry
    # numbers a municipality by — **inside Quebec only**. The Statistics
    # Canada code is two digits of province, two of census division and three
    # of subdivision, so the last five collide across provinces: taken
    # nationally, 843 of them mapped to more than one item and were refused,
    # which cost a fifth of the province. Quebec is province 24, and that is
    # the published structure of the code rather than a pattern read off the
    # data.
    five = {}
    for qid, e in wd.items():
        for s in e["sgc"]:
            s = str(s).strip()
            if len(s) == 7 and s.startswith("24"):
                five.setdefault(s[-5:], set()).add(qid)
    by5 = {c: next(iter(s)) for c, s in five.items() if len(s) == 1}
    amb = sum(1 for s in five.values() if len(s) > 1)
    print(f"    {len(wd):,} Canadian items with a Statistics Canada code, "
          f"{len(by5):,} usable five-digit keys")

    b = Build("CAN", "Répertoire des municipalités du Québec")
    b.dropped_ambig_code = amb
    agree = checked = 0
    def clean(v):
        v = str(v or "").strip()
        return "" if not v or v.strip("0") == "" else v
    for r in rows:
        qid = by5.get(clean(r.get("mcode")))
        if not qid:
            b.dropped_nocode += 1
            continue
        nm, lab = fold(r.get("munnom")), fold(wd[qid]["lab"])
        if lab:
            checked += 1
            if nm == lab or nm in lab or lab in nm:
                agree += 1
        rec = {}
        site = clean(r.get("mweb"))
        if site:
            rec["u"] = site if site.startswith(("http://", "https://")) else "https://" + site
        mail = clean(r.get("mcourriel"))
        if mail: rec["e"] = [mail]
        tel = re.sub(r"\D", "", clean(r.get("mtel")))
        if len(tel) == 10:
            rec["p"] = f"{tel[0:3]}-{tel[3:6]}-{tel[6:]}"
        elif tel:
            rec["p"] = tel
        street, town, post = clean(r.get("madr1")), clean(r.get("madr2")), clean(r.get("mcodpos"))
        if street:
            rec["o"] = ", ".join(x for x in [street, town, post] if x)
        mayor = clean(r.get("maire"))
        if mayor: rec["m"] = mayor
        cn = [clean(r.get("con%d" % i)) for i in range(1, 76)]
        cn = [x for x in cn if x]
        if cn: rec["cn"] = cn
        # The register publishes the rest of the officials as well, and a
        # reader asking who to write to about a building permit is better
        # served by the name of whoever holds that job than by a switchboard.
        of = [[title, clean(r.get(k))] for k, title in QC_POSTS if clean(r.get(k))]
        if of: rec["of"] = of
        b.put(qid, rec)
    gate("official name against the French label", agree, checked, 0.97)
    return b

# ---------------------------------------------------------------- registry

COUNTRIES = {
    "ITA": ("Italy", build_italy),
    "CAN": ("Canada — Quebec only", build_quebec),
}

FIELDS = {
    "u": "the government's own website, as the register publishes it",
    "e": "public email addresses, every one the register holds",
    "c": "certified email (Italy's PEC): refuses mail from an ordinary account",
    "p": "switchboard",
    "a": "street address as printed, with the place's name added at render time",
    "o": "full postal address",
    "m": "the mayor, by name",
    "cn": "the councillors, by name",
    "of": "other named post-holders, as [title, name]",
    "j": "how the row was joined, where it was not a shared code",
    "src": "which register the record came from",
}

def write_shards(builds, out):
    os.makedirs(out, exist_ok=True)
    shards = {}
    for b in builds:
        for qid, rec in b.rec.items():
            shards.setdefault(int(qid[1:]) % SHARDS, {})[qid] = rec
    # Shards are keyed by the id alone, so two countries share a shard file
    # happily and the loader needs no per-country logic. Every shard is
    # rewritten, including the ones that came out empty, or a country removed
    # from the build would leave its records behind.
    for k in range(SHARDS):
        p = os.path.join(out, f"{k}.json")
        data = shards.get(k, {})
        if data or os.path.exists(p):
            json.dump(data, open(p, "w"), separators=(",", ":"), ensure_ascii=False)
    idx = {"built": time.strftime("%Y-%m-%d"),
           "shards": SHARDS,
           "countries": sorted(b.iso3 for b in builds),
           "registers": {b.iso3: b.src for b in builds},
           "counts": {b.iso3: b.report() for b in builds},
           "fields": FIELDS,
           "note": "Keyed by Wikidata id. shard = int(qid[1:]) % 512. "
                   "A record states what its register publishes; nothing here "
                   "is derived from a name or a pattern."}
    json.dump(idx, open(os.path.join(out, "index.json"), "w"),
              indent=1, ensure_ascii=False)
    return shards, idx

if __name__ == "__main__":
    args = sys.argv[1:]
    out = os.path.join(ROOT, "muni")
    if "--out" in args:
        i = args.index("--out"); out = args[i+1]; del args[i:i+2]
    want = [a.upper() for a in args] or list(COUNTRIES)
    builds = []
    for iso in want:
        if iso not in COUNTRIES:
            raise SystemExit(f"no builder for {iso}; have {sorted(COUNTRIES)}")
        name, fn = COUNTRIES[iso]
        print(f"\n== {iso} — {name}")
        b = fn()
        r = b.report()
        print(f"    shipped {r['shipped']:,}; "
              f"no shared code {r['no_shared_code']:,}; "
              f"register publishes no contact {r['register_publishes_no_contact']:,}; "
              f"refused as ambiguous {r['refused_code_maps_to_two_items']:,} codes "
              f"and {r['refused_item_claimed_twice']:,} rows")
        print("    fields: " + ", ".join(f"{k} {v:,}" for k, v in
              sorted(r["fields"].items(), key=lambda kv: -kv[1]) if k != "src"))
        builds.append(b)
    shards, idx = write_shards(builds, out)
    tot = sum(len(v) for v in shards.values())
    big = max((len(json.dumps(v)) for v in shards.values()), default=0)
    print(f"\nwrote {out}: {tot:,} records, largest shard {big/1024:.0f} KB")
