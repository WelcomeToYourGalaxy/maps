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

# ---------------------------------------------------------------- Spain

ES_ART = ("la", "el", "los", "las", "o", "a", "os", "as", "es", "l",
          "les", "els", "lo")

def es_key(name):
    """The canonical form of a Spanish official municipality name.

    Three things have to be undone, and all three are how the register
    writes a name rather than anything inferred:

    - the article sits at the end of an official name (`Vall de Gallinera,
      la`) where ordinary prose puts it in front, so it is moved off and
      dropped;
    - a bilingual official name is written in either order — REL has
      `Alacant/Alicante` where DIR3 has `Alicante/Alacant` — so the halves
      are sorted. Both sides must still hold the same two names spelled the
      same way, so this adds no fuzziness; it cost 19 municipalities until
      round sixteen found it;
    - accents and punctuation are dropped, because the two files disagree
      about them and about nothing else.
    """
    t = str(name or "").strip()
    t = re.sub(r"^ayuntamiento\s+(de\s+la|de\s+los|de\s+las|del|de|d')\s*", "",
               t, flags=re.I)
    t = re.sub(r"^ayuntamiento\s+", "", t, flags=re.I)
    m = re.match(r"^(.*),\s*([A-Za-zÀ-ÿ']{1,4})$", t)
    if m and fold(m.group(2)) in ES_ART:
        t = m.group(1)
    parts = [fold(x) for x in re.split(r"\s*/\s*", t) if fold(x)]
    return "/".join(sorted(parts))

def cif_code(cif):
    """The five digits a Spanish local-authority tax number carries between
    its letters. **Never a key**: those digits are the Registro de Entidades
    Locales' own sequence and they diverge from the INE code wherever a
    municipality has been created or dissolved — joining on them gives 59%
    of Spain a neighbouring town's address. They are only ever the check,
    below, because the join never touches them."""
    m = re.match(r"^[A-Za-z](\d{5})", str(cif or "").strip())
    return m.group(1) if m else None

def build_spain():
    """Two registers of the same bodies kept by the same ministry, and no
    code to join them on.

    REL, the Registro de Entidades Locales, is the authority list: every
    municipality with its official name and, inside `NUMERO_INSCRIPCION`,
    the INE code — `01`, then the five-digit code, then a check digit, so
    Abánades is `01190019` against INE 19001. That is the code Wikidata
    holds on 8,205 Spanish municipality items. DIR3 holds the contacts and
    carries no INE code at all: 8,133 top-level ayuntamientos with a tax
    number, a two-digit province and an email, and **exactly one** Spanish
    municipality on Wikidata carries a DIR3 id.

    So this is the one country here joined on a name, and the four
    conditions on that exception are in the code below:

    1. the match is exact on a canonical official name, never fuzzy and
       never nearest;
    2. it is bounded by a published administrative code — the province —
       so two places of one name in different provinces cannot meet;
    3. a name claimed by two rows on either side is refused and counted;
    4. the result is checked against a published field the match never
       uses, with a floor that stops the country shipping.
    """
    # --- REL: the authority list, keyed by the INE code
    rel = get("https://registroentidadeslocales.mpt.es/REL/frontend/"
              "export_data/file_export/export_excel/municipios/all/all",
              timeout=420)
    open("/tmp/rel.xls", "wb").write(rel)
    # The export is a legacy .xls. `xlrd` reads that format in process —
    # the first version of this shelled out to LibreOffice, which is on this
    # machine and is not on the Action's runner, so the build would have
    # worked here and failed there with no file to find.
    import xlrd
    sh = xlrd.open_workbook("/tmp/rel.xls").sheet_by_index(0)
    rows = [[sh.cell_value(i, c) for c in range(sh.ncols)]
            for i in range(sh.nrows)]
    hi = next(i for i, r in enumerate(rows)
              if any(str(x).strip() == "NUMERO_INSCRIPCION" for x in r))
    H = {str(h).strip(): i for i, h in enumerate(rows[hi]) if str(h).strip()}
    rel_rows = []
    for r in rows[hi + 1:]:
        # The column is stored as a number, so the leading zero is not in it
        # and a float arrives: 1189136.0 for the published 01189136. Zero-pad
        # to eight and the INE code is the five digits in the middle —
        # Abánades is 01190019 against INE 19001.
        num = r[H["NUMERO_INSCRIPCION"]]
        if isinstance(num, float):
            num = str(int(num))
        num = str(num or "").strip()
        num = num.zfill(8) if num.isdigit() else num
        if len(num) != 8 or not num.isdigit():
            continue
        ine = num[2:7]
        rel_rows.append({"ine": ine, "prov": ine[:2],
                         "name": str(r[H["DENOMINACION"]] or "").strip()})
    print(f"    REL: {len(rel_rows):,} municipalities with an INE code")

    # --- DIR3: the contacts, keyed by nothing that joins
    d3 = get("https://administracionelectronica.gob.es/ctt/resources/"
             "Soluciones/238/Descargas/Listado%20Unidades%20EELL.xlsx",
             timeout=420)
    open("/tmp/eell.xlsx", "wb").write(d3)
    import openpyxl
    # Not read_only: the file carries no usable dimension record, so a
    # read-only load reports one row by one column and finds nothing.
    sh = openpyxl.load_workbook("/tmp/eell.xlsx")["Unidades EELL"]
    rows = list(sh.iter_rows(values_only=True))
    D = {}
    for i, h in enumerate(rows[1]):
        D.setdefault(str(h), i)
    ay = []
    for r in rows[2:]:
        if str(r[D["C_ID_TIPO_ENT_PUBLICA"]]) != "AY":
            continue
        if str(r[D["N_NIVEL_JERARQUICO"]]) != "1":
            continue
        nm = str(r[D["C_DNM_UD_ORGANICA"]] or "").strip()
        # the file carries a few bodies of other kinds at this level — a
        # regional IT company among them — and they are not ayuntamientos
        if not nm.lower().startswith("ayuntamiento"):
            continue
        prov = str(r[D["C_ID_AMB_PROVINCIA"]] or "").strip().zfill(2)
        ay.append({"name": nm, "prov": prov,
                   "cif": str(r[D["NIF_CIF"]] or "").strip(),
                   "contact": str(r[D["CONTACTOS"]] or "").strip()})
    print(f"    DIR3: {len(ay):,} top-level ayuntamientos, "
          f"{sum(1 for x in ay if x['contact']):,} with a contact")

    # --- the name join, inside a province, one-to-one only
    def one_to_one(items):
        by = {}
        for x in items:
            by.setdefault((x["prov"], es_key(x["name"])), []).append(x)
        return ({k: v[0] for k, v in by.items() if len(v) == 1},
                sum(1 for v in by.values() if len(v) > 1))
    rel_by, rel_dup = one_to_one(rel_rows)
    ay_by, ay_dup = one_to_one(ay)
    pairs = {k: (rel_by[k], ay_by[k]) for k in rel_by if k in ay_by}
    print(f"    matched one-to-one: {len(pairs):,}; "
          f"names claimed twice refused: {rel_dup} in REL, {ay_dup} in DIR3; "
          f"in REL and not in DIR3 under that name: {len(rel_by)-len(pairs):,}")

    # --- the gate: an ordering the join never touches
    # Both the tax number's embedded digits and the INE code number a
    # province's municipalities alphabetically, from different epochs, so a
    # match that had swapped two towns would put a pair in the wrong order.
    # A scrambled match sits near half.
    byprov = {}
    for (prov, _), (rr, ar) in pairs.items():
        c = cif_code(ar["cif"])
        if c:
            byprov.setdefault(prov, []).append((int(rr["ine"]), int(c)))
    agree = total = 0
    for prov, lst in byprov.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                total += 1
                if (lst[i][0] - lst[j][0]) * (lst[i][1] - lst[j][1]) > 0:
                    agree += 1
    gate("the INE and tax-number orderings inside a province", agree, total, 0.95)

    # --- Wikidata on the INE code
    wd = {}
    # The class filter is load-bearing: `P772` is the Instituto Nacional de
    # Estadística id and Spain puts it on twelve thousand other things as
    # well — census areas, districts, entities below the municipality — so
    # asking only for Spanish items with that property returned 37,317 of
    # them and would have let a non-municipality win a code. Municipality
    # items carrying it: 8,205, which is what round fifteen counted.
    for r in sparql("""SELECT ?x ?ine WHERE {
            ?x wdt:P772 ?ine ; wdt:P31/wdt:P279* wd:Q2074737 .
            FILTER NOT EXISTS { ?x wdt:P576 ?d } }"""):
        qid = r["x"]["value"].rsplit("/", 1)[-1]
        wd.setdefault(qid, {"ine": set()})["ine"].add(
            str(r["ine"]["value"]).zfill(5))
    by_ine, amb = index_by_code(wd, "ine")
    print(f"    {len(wd):,} Spanish municipality items with an INE code, "
          f"{len(by_ine):,} usable")

    b = Build("ESP", "DIR3 and the Registro de Entidades Locales")
    b.dropped_ambig_code = amb + rel_dup + ay_dup
    for (prov, _), (rr, ar) in pairs.items():
        qid = by_ine.get(rr["ine"])
        if not qid:
            b.dropped_nocode += 1
            continue
        rec = {}
        # A register can publish more than one address for one council, and
        # which to write to is the reader's choice, so each is its own entry
        # rather than one dead comma-joined string.
        mails = [m.strip() for m in re.split(r"[;,\s]+", ar["contact"])
                 if "@" in m]
        seen, keep = set(), []
        for m in mails:
            if m.lower() not in seen:
                seen.add(m.lower()); keep.append(m)
        if keep:
            rec["e"] = keep
            # every row that got in on a name says so, and the panel prints
            # it under the address
            rec["j"] = "name"
        b.put(qid, rec)
    return b

# ---------------------------------------------------------------- registry

COUNTRIES = {
    "ITA": ("Italy", build_italy),
    "ESP": ("Spain", build_spain),
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
