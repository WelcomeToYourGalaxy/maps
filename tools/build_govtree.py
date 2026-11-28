#!/usr/bin/env python3
"""One diagram per country of how its national government is organised.

Writes govtree/<Q-id>.json (one file per country) and govtree/index.json.
--coords adds coordinates to the charts on disk without rebuilding them;
--coextensive writes govtree/coextensive.json (places that are one ground).
--directories applies each country's own register of its bodies (DIRECTORIES).
With --regions it does the same one level down - every first-level division
of every country (US states, German Länder, Indian states, French regions…) -
and indexes them in govtree/regions.json. The page draws a region's file
under the country; below the regions it uses the offices it has loaded.
The page reads a country's file when a place in that country is searched,
draws it as a Mermaid chart in the box hung off the panel's bottom-left
corner, and adds the levels below the country from the offices the page
has already loaded for the searched place.

    python3 -I tools/build_govtree.py            # every country
    python3 -I tools/build_govtree.py Q30 Q145   # just these

Everything comes from Wikidata through QLever (WDQS second), for the
reason tools/completeness.py gives. Nothing is written by hand: a body is
on a country's chart because Wikidata places it in that government.

What decides membership
  roots      the country's legislature (P194), its executive body (P208),
             its highest court (P209), and the offices of head of state
             (P1906) and head of government (P1313)
  ministries anything that is a kind of ministry (Q192350) in the country
             and is national: it applies to the country (P1001), is
             located in the country itself (P131), or is part of the
             executive body. P17 alone is not enough - every US state
             department of transportation carries P17 United States.
  below      organisations that are part of (P361) or subordinate to
             (P749) anything already on the chart, or that a body on the
             chart lists as a part (P527) or a subsidiary (P355), three
             levels down from a branch's root and two below a ministry
  national   government agencies (Q327333) and courts (Q41487) applying
  bodies     to the country or located in the country itself that were
             not reached from a root
What keeps a body off
  ended      dissolution (P576), end time (P582), replaced by (P1366),
             or an end time on the very statement that places it
  not a body military units, schools, hospitals, museums, research
             institutes, companies, diplomatic missions, prisons,
             buildings, websites, periodicals, parties - organisations
             a government owns or runs rather than parts of how it
             governs
  ad hoc     a legislative committee named for one bill, which ends with
             the bill and is rarely given an end date
Offices (positions) that direct a body (P2389) or are a position within it
(P361) are recorded against it as `a`, so that the page can light the body
when the reader opens one of those offices.
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "govtree")
EP = ["https://qlever.dev/api/wikidata",
      "https://qlever.cs.uni-freiburg.de/api/wikidata",
      "https://query.wikidata.org/sparql"]
PRE = ("PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
       "PREFIX wd: <http://www.wikidata.org/entity/> "
       "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "
       "PREFIX schema: <http://schema.org/> "
       "PREFIX p: <http://www.wikidata.org/prop/> "
       "PREFIX ps: <http://www.wikidata.org/prop/statement/> "
       "PREFIX pq: <http://www.wikidata.org/prop/qualifier/> ")

def ask(q, tries=3, timeout=900):
    body = urllib.parse.urlencode({"query": PRE + q}).encode()
    last = ""
    for ep in EP:
        for a in range(tries):
            try:
                rq = urllib.request.Request(ep, data=body, headers={
                    "Accept": "application/sparql-results+json",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "HowToReachThem-govtree/1.0 (welcometoyourgalaxy.com)"})
                with urllib.request.urlopen(rq, timeout=timeout) as r:
                    return json.loads(r.read())["results"]["bindings"]
            except Exception as e:
                last = f"{ep}: {e}"
                time.sleep(3 * (a + 1))
    raise SystemExit("every endpoint refused: " + last)

def v(r, k):
    x = r.get(k)
    if not x: return None
    s = x["value"]
    return s.rsplit("/", 1)[-1] if s.startswith("http://www.wikidata.org/entity/") else s

def chunks(xs, n):
    xs = list(xs)
    for i in range(0, len(xs), n): yield xs[i:i + n]

def vals(qs): return " ".join("wd:" + q for q in qs)

ENDED = """
 FILTER NOT EXISTS { ?X wdt:P576 ?_d }
 FILTER NOT EXISTS { ?X wdt:P582 ?_e }
 FILTER NOT EXISTS { ?X wdt:P1366 ?_r }
"""
# organisations a government runs or owns, as against parts of how it governs
NOTBODY = ["Q3917681", "Q176799", "Q2385804", "Q16917", "Q33506", "Q31855", "Q4830453",
           "Q7843791", "Q40357", "Q41176", "Q35127", "Q1002697", "Q7278",
           "Q15893266", "Q618779", "Q1194093", "Q4287745", "Q3914",
           "Q178706", "Q1785733", "Q11032", "Q4671277", "Q132821",
           "Q1530022", "Q2061186", "Q640506", "Q20926517"]
# a class from the first list keeps a body on even when it also carries one
# from the second: the US Department of Agriculture is also filed as an
# academic publisher, which is a kind of company
KEEP = ["Q327333", "Q192350", "Q2659904", "Q41487", "Q11204", "Q865588",
        "Q35798", "Q1752346"]
NOTBODY_F = ("FILTER ( EXISTS { ?X wdt:P31/wdt:P279* ?_ok . VALUES ?_ok { %s } } || "
             "NOT EXISTS { ?X wdt:P31/wdt:P279* ?_bad . VALUES ?_bad { %s } } )"
             % (vals(KEEP), vals(NOTBODY)))
ADHOC = re.compile(r"\b(bill|draft)\b", re.I)
# a mission accredited to the country is not part of its government; the
# page's own RX_DIPLO plus the missions themselves
DIPLO = re.compile(r"\b(embassy|embassies|consulate|nunciature|high commission of|high commission in|"
                   r"delegate of the government|delegation of|interests section|representative office|permanent representative|permanent mission|"
                   r"mission to the|representation of the|generalitat|legation|consula[a-z]*|konsulat[a-z]*|"
                   r"ambassade|embajada|embaixada|botschaft|ambasciata|ambasada|velvyslanectv|"
                   r"ba\u015fkonsolos[a-z\u0131\u011f\u00fc]*|b\u00fcy\u00fckel\u00e7il[a-z\u0131\u011f]*|"
                   r"missionary|province in the|province of the society|high commission|trade office|"
                   r"general mission|\u0633\u0641\u0627\u0631\u0629)\b", re.I)
# court cases filed as if they were courts: "X v Y", "[1978]"
CASE = re.compile(r"\sv\.?\s|\[\d{4}\]|\bcase\b", re.I)
DEFUNCT_DESC = re.compile(r"\b(former|defunct|abolished|dissolved|disbanded|historical|historic)\b", re.I)

# a ministry must also be filed under the country itself; a region's own
# departments carry the country in P17, so in --regions mode it is dropped
P17C = "?X wdt:P17 ?c ."
REGIONS = False
PARENT = {}

def regions(only):
    """first-level divisions of every country, current ones only"""
    rows = ask("""SELECT DISTINCT ?r ?c WHERE { ?c wdt:P31 wd:Q6256 .
      ?c p:P150 ?st . ?st ps:P150 ?r . FILTER NOT EXISTS { ?st pq:P582 ?e }
      FILTER NOT EXISTS { ?r wdt:P576 ?d } FILTER NOT EXISTS { ?r wdt:P582 ?e2 } }""")
    out = {}
    for r in rows:
        q = v(r, "r")
        if only and q not in only: continue
        if q in out: continue
        out[q] = {"iso3": None, "num": None}; PARENT[q] = v(r, "c")
    return out

def countries(only):
    if only:
        # named on the command line: built whether or not the item
        # carries a country code (the Netherlands' government hangs off
        # Q55, which has none; the page knows the kingdom, Q29999)
        rows = ask(f"""SELECT DISTINCT ?c ?iso3 ?num WHERE {{ VALUES ?c {{ {vals(only)} }}
          OPTIONAL {{ ?c wdt:P299 ?num }} OPTIONAL {{ ?c wdt:P298 ?iso3 }} }}""")
        return {v(r, "c"): {"iso3": v(r, "iso3"), "num": v(r, "num")} for r in rows}
    rows = ask("""SELECT DISTINCT ?c ?iso3 ?num WHERE { ?c wdt:P31 wd:Q6256 ; wdt:P299 ?num .
      OPTIONAL { ?c wdt:P298 ?iso3 } }""")
    out = {}
    for r in rows:
        q = v(r, "c")
        if only and q not in only: continue
        out[q] = {"iso3": v(r, "iso3"), "num": v(r, "num")}
    return out

def apex(cs):
    out = defaultdict(lambda: defaultdict(list))
    for ch in chunks(cs, 300):
        for prop, key in (("P194", "leg"), ("P208", "exe"), ("P209", "court"),
                          ("P1906", "hos"), ("P1313", "hog")):
            rows = ask(f"""SELECT DISTINCT ?c ?X WHERE {{ VALUES ?c {{ {vals(ch)} }}
               ?c wdt:{prop} ?X . {ENDED} }}""")
            for r in rows: out[v(r, "c")][key].append(v(r, "X"))
    return out

def ministries(cs, ap):
    out = defaultdict(set)
    for ch in chunks(cs, 300):
        rows = ask(f"""SELECT DISTINCT ?c ?X WHERE {{ VALUES ?c {{ {vals(ch)} }}
          ?X wdt:P31/wdt:P279* wd:Q192350 . {P17C}
          {{ ?X wdt:P1001 ?c }} UNION {{ ?X wdt:P131 ?c }}
          UNION {{ ?c wdt:P208 ?g . ?X wdt:P361|wdt:P749 ?g }}
          {ENDED} {NOTBODY_F} }}""".replace("{P17C}", P17C))
        for r in rows: out[v(r, "c")].add(v(r, "X"))
    return out

def national(cs, cls, strict=False):
    out = defaultdict(set)
    where = "?X wdt:P1001 ?c ." if strict else "{ ?X wdt:P1001 ?c } UNION { ?X wdt:P131 ?c }"
    for ch in chunks(cs, 300):
        rows = ask(f"""SELECT DISTINCT ?c ?X WHERE {{ VALUES ?c {{ {vals(ch)} }}
          ?X wdt:P31/wdt:P279* wd:{cls} . {P17C}
          {where}
          {ENDED} {NOTBODY_F} }}""".replace("{P17C}", P17C))
        for r in rows: out[v(r, "c")].add(v(r, "X"))
    return out

def children(parents):
    """child -> parents, for organisations placed under any of `parents`.
    A batch the endpoint times out on is split in half and asked again, so
    one heavy parent costs a few requests rather than the whole build."""
    out = defaultdict(set)
    todo = list(chunks(parents, 100))
    while todo:
        ch = todo.pop()
        try:
            rows = _children_rows(ch)
        except SystemExit:
            if len(ch) == 1:
                print("  gave up on the parts of", ch[0], file=sys.stderr); continue
            todo += [ch[:len(ch)//2], ch[len(ch)//2:]]; continue
        for r in rows:
            out[v(r, "X")].add(v(r, "P"))
            if r.get("court"): COURT.add(v(r, "X"))
    return out

def _children_rows(ch):
    if True:
        return ask(f"""SELECT DISTINCT ?X ?P ?court WHERE {{ VALUES ?P {{ {vals(ch)} }}
          {{ ?X p:P361 ?s . ?s ps:P361 ?P . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?X p:P749 ?s . ?s ps:P749 ?P . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?P p:P527 ?s . ?s ps:P527 ?X . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?P p:P355 ?s . ?s ps:P355 ?X . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?X wdt:P31 ?P }}
          {{ ?X wdt:P31/wdt:P279* wd:Q43229 }} UNION {{ ?X wdt:P279+ wd:Q43229 }}
          OPTIONAL {{ ?X wdt:P31/wdt:P279* ?_ct . VALUES ?_ct {{ wd:Q41487 wd:Q105985 }} BIND(1 AS ?court) }}
          {ENDED} {NOTBODY_F} }}""", tries=1, timeout=240)
COURT = set()

def aliases(nodes):
    out = defaultdict(set)
    for ch in chunks(nodes, 400):
        rows = ask(f"""SELECT DISTINCT ?X ?O WHERE {{ VALUES ?X {{ {vals(ch)} }}
          {{ ?O wdt:P2389 ?X }} UNION {{ ?O wdt:P361 ?X . ?O wdt:P31/wdt:P279* wd:Q4164871 }}
          FILTER NOT EXISTS {{ ?O wdt:P576 ?_d }} FILTER NOT EXISTS {{ ?O wdt:P582 ?_e }} }}""")
        for r in rows: out[v(r, "X")].add(v(r, "O"))
    return out

def divisions(cs):
    out = defaultdict(set)
    for ch in chunks(cs, 300):
        rows = ask(f"""SELECT DISTINCT ?c ?l WHERE {{ VALUES ?c {{ {vals(ch)} }}
          ?c wdt:P150 ?d . ?d rdfs:label ?l FILTER(LANG(?l)="en") }}""")
        for r in rows: out[v(r, "c")].add(r["l"]["value"])
    return out

LAWDOC = re.compile(r"\b(act|statute|ordinance|amendment|code)(\s+of\s+\d{4}|\s+\d{4})?$", re.I)
TENURE_MIN = re.compile(r"^(?!.*\bof\b)(?!.*\bdepartment\b).*\bministry$", re.I)
CAUCUS = re.compile(r"\b(caucus|friendship group|parliamentary group of)\b", re.I)
TENURE = re.compile(r"\bcabinet\b", re.I)
TENURE_OK = re.compile(r"\b(office|secretariat|division|department|committee|council|"
                       r"of the united states|of ministers)\b", re.I)

def current(qs):
    """Bodies with some sign on the record that they still exist: an
    official website, a chair or director, an office heading them with a
    holder in post since 2000 and no end date, or a founding date since
    2015. A body without any of these is drawn, but marked as not
    confirmed current rather than dropped: Wikidata gives most abolished
    ministries no end date, and leaving them out would also leave out
    real ones that simply have no website recorded."""
    ok = set()
    for ch in chunks(qs, 300):
        rows = ask(f"""SELECT DISTINCT ?X WHERE {{ VALUES ?X {{ {vals(ch)} }}
          {{ ?X wdt:P856 ?w }} UNION {{ ?X p:P488 ?a . FILTER NOT EXISTS {{ ?a pq:P582 ?e1 }} }}
          UNION {{ ?X p:P1037 ?b . FILTER NOT EXISTS {{ ?b pq:P582 ?e2 }} }}
          UNION {{ ?X wdt:P2388 ?pos . ?h p:P39 ?st . ?st ps:P39 ?pos .
                   FILTER NOT EXISTS {{ ?st pq:P582 ?e3 }} ?st pq:P580 ?s . FILTER(YEAR(?s) >= 2000) }}
          UNION {{ ?X wdt:P571 ?i . FILTER(YEAR(?i) >= 2015) }} }}""")
        ok |= {v(r, "X") for r in rows}
    return ok

def labels(qs):
    lab, desc, site = {}, {}, {}
    for ch in chunks(qs, 400):
        rows = ask(f"""SELECT ?X ?en ?any ?d ?w WHERE {{ VALUES ?X {{ {vals(ch)} }}
          OPTIONAL {{ ?X rdfs:label ?en FILTER(LANG(?en)="en") }}
          OPTIONAL {{ ?X rdfs:label ?any }}
          OPTIONAL {{ ?X schema:description ?d FILTER(LANG(?d)="en") }}
          OPTIONAL {{ ?X wdt:P856 ?w }} }}""")
        for r in rows:
            x = v(r, "X")
            if r.get("en"): lab[x] = r["en"]["value"]
            elif x not in lab and r.get("any"): lab.setdefault("~" + x, r["any"]["value"])
            if r.get("d"): desc[x] = r["d"]["value"]
            if r.get("w") and x not in site: site[x] = r["w"]["value"]
    for k in [k for k in lab if k.startswith("~")]:
        if k[1:] not in lab: lab[k[1:]] = lab[k]
        del lab[k]
    return lab, desc, site

def coords(qs):
    """Where a body sits, so the page can move the map to it: its own
    coordinates (P625), or failing that its headquarters' (P159), which
    is usually a city and is marked as such. Nothing is estimated."""
    out = {}
    for ch in chunks(qs, 400):
        rows = ask(f"""SELECT ?X ?c ?hq WHERE {{ VALUES ?X {{ {vals(ch)} }}
          {{ ?X wdt:P625 ?c }} UNION {{ ?X wdt:P159 ?h . ?h wdt:P625 ?c BIND(1 AS ?hq) }} }}""")
        for r in rows:
            x = v(r, "X")
            m = re.match(r"(?i)Point\(([-\d.eE]+) ([-\d.eE]+)\)", r["c"]["value"])
            if not m: continue
            hq = bool(r.get("hq"))
            if x in out and (out[x][2] == 0 or hq): continue
            out[x] = [round(float(m.group(1)), 5), round(float(m.group(2)), 5), 1 if hq else 0]
    return out

ALLEDGE = defaultdict(set)
WEIGHTY = re.compile(r"\b(ministry|department|agency|authority|commission|administration|bureau|"
                     r"service|directorate|court|tribunal|house|senate|chamber|assembly|council|"
                     r"committee|office)\b", re.I)
MINOR = re.compile(r"\b(group|forum|panel|unit|team|task ?force|working|stakeholder|network|"
                   r"programme|program|project|initiative|small (and disadvantaged )?business)\b", re.I)

def coextensive():
    """Places Wikidata says cover the same ground as one another (P3403),
    among administrative units: the District of Columbia and Washington,
    for instance. The page merges levels of a chain that are one
    government, so they draw as one chart rather than two or three."""
    rows = ask("""SELECT DISTINCT ?a ?b WHERE { ?a wdt:P3403 ?b .
      ?a wdt:P31/wdt:P279* wd:Q56061 . ?b wdt:P31/wdt:P279* wd:Q56061 . }""")
    out = defaultdict(set)
    for r in rows:
        a, b = v(r, "a"), v(r, "b")
        if a != b: out[a].add(b); out[b].add(a)
    os.makedirs(OUT, exist_ok=True)
    json.dump({k: sorted(x) for k, x in sorted(out.items())},
              open(os.path.join(OUT, "coextensive.json"), "w"), separators=(",", ":"))
    print(len(out), "places with a coextensive twin", file=sys.stderr)

# ---------------------------------------------------------------- official directories
#
# A government's own list of its bodies says what Wikidata cannot: which
# ones exist today. Each source below is applied to that country's chart
# after it is built: a body the directory lists is marked current and
# credited to it; a body it says has closed is taken off; a body it lists
# that Wikidata lacks is added under the parent the directory gives.
# Matching is on the official website first (both sides publish it), then
# on the name with the country's own name and articles taken off.

def _host_path(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://", "", u); u = re.sub(r"^www\.", "", u)
    return u.rstrip("/")

def _name_key(s, country_words):
    s = (s or "").lower()
    s = re.sub(r"[\u2019']", "", s)
    for w in country_words: s = s.replace(w, " ")
    s = re.sub(r"\b(the|of|and|for|u\.s\.|us|hm|his majesty's|her majesty's|de|du|des|la|le|les|l|et|d)\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)

def _get_json(url):
    rq = urllib.request.Request(url, headers={"User-Agent": "HowToReachThem-govtree/1.0 (welcometoyourgalaxy.com)",
                                              "Accept": "application/json"})
    with urllib.request.urlopen(rq, timeout=120) as r:
        return json.loads(r.read())

def _labels_in(qs, lang):
    out = defaultdict(set)
    qs = [q for q in qs if re.match(r"^Q\d+$", q)]
    for ch in chunks(qs, 400):
        for r in ask(f"""SELECT ?X ?l WHERE {{ VALUES ?X {{ {vals(ch)} }}
                         ?X rdfs:label|skos:altLabel ?l FILTER(LANG(?l)="{lang}") }}""".replace(
                         "skos:altLabel", "<http://www.w3.org/2004/02/skos/core#altLabel>")):
            out[v(r, "X")].add(r["l"]["value"])
    return out

def _apply(path, entries, src, country_words, drop_closed=True, lang="en", complete_min=False):
    """entries: dicts with id, l, w, parent (entry id or None), b, top
    ('@min', '@agencies', '@courts' or None), live (bool)"""
    d = json.load(open(path))
    N = d["n"]
    by_web, by_name, by_host = {}, {}, defaultdict(set)
    other = _labels_in(list(N), lang) if lang != "en" else {}
    for q, e in N.items():
        if e.get("w"):
            by_web.setdefault(_host_path(e["w"]), q); by_host[_host_path(e["w"]).split("/")[0]].add(q)
        by_name.setdefault(_name_key(e["l"], country_words), q)
        for l in other.get(q, ()): by_name.setdefault(_name_key(l, country_words), q)
    for h in d.get("heads", []):
        by_name.setdefault(_name_key(h["l"], country_words), h["q"])
    # A website or a name shared by several entries of the directory (every
    # sub-directorate of a French ministry gives the ministry's site; most
    # ministries have a "general secretariat") identifies none of them.
    wc = defaultdict(int); nc = defaultdict(int); hc = defaultdict(int)
    for x in entries:
        if x.get("w"): wc[_host_path(x["w"])] += 1; hc[_host_path(x["w"]).split("/")[0]] += 1
        nc[_name_key(x["l"], country_words)] += 1
    match, claimed = {}, defaultdict(int)
    for x in entries:
        hw, nk = _host_path(x.get("w")), _name_key(x["l"], country_words)
        q = by_web.get(hw) if x.get("w") and wc[hw] == 1 else None
        # the same site under another path: one body on each side using it
        # — and only when the two names share a word: an Ontario agency
        # and the ministry it sits in can use one host between them
        if not q and x.get("w"):
            h = hw.split("/")[0]
            if hc[h] == 1 and len(by_host.get(h, ())) == 1:
                cand = next(iter(by_host[h]))
                w1 = {t for t in re.findall(r"[a-zà-ÿ]{5,}", x["l"].lower())}
                w2 = {t for t in re.findall(r"[a-zà-ÿ]{5,}", N[cand]["l"].lower())}
                if w1 & w2 - {"ministry", "department", "office", "government", "national", "federal"}: q = cand
        if not q and nk and nc[nk] == 1: q = by_name.get(nk)
        if q: match[x["id"]] = q; claimed[q] += 1
    # and a chart body two entries both claim is matched to neither
    for xid in [i for i, q in match.items() if claimed[q] > 1]: match.pop(xid)
    added = confirmed = dropped = 0
    # closed bodies go, with whatever sits under them that the directory
    # does not list as live
    live_ids = {match[x["id"]] for x in entries if x["live"] and x["id"] in match}
    if drop_closed:
        gone = {match[x["id"]] for x in entries if not x["live"] and x["id"] in match} - live_ids
        changed = True
        while changed:
            changed = False
            for q, e in list(N.items()):
                if q in gone: continue
                if e.get("p") in gone and q not in live_ids: gone.add(q); changed = True
        for q in gone:
            if q in N: N.pop(q); dropped += 1
    # Where the directory is the whole list of a country's ministries, a
    # ministry on the chart it does not list is a former one (Wikidata
    # rarely closes them): it comes off, and what sat under it is kept
    # among the country's other bodies rather than lost with it.
    if complete_min:
        listed = set(match.values())
        for q in [q for q, e in N.items() if e.get("p") == "@min" and q not in listed and re.match(r"^Q\d+$", q)]:
            for k, e in N.items():
                if e.get("p") == q: e["p"] = "@agencies"
            N.pop(q); dropped += 1
    for x in entries:
        if not x["live"]: continue
        q = match.get(x["id"])
        if q and q in N:
            N[q].pop("u", None); N[q]["src"] = src; confirmed += 1
            # the directory's own name is the current one (a department
            # renamed in 2023 still carries its old name on Wikidata)
            if lang == "en" and x["l"] and x["l"] != N[q]["l"]:
                N[q].setdefault("wd", N[q]["l"]); N[q]["l"] = x["l"]
            # the register's own name, in its own language, beside an
            # English label Wikidata may not have kept up to date: a
            # renamed ministry reads under its current name as well
            elif lang != "en" and x["l"] and x["l"] != N[q]["l"]:
                N[q]["on"] = x["l"]
            if not N[q].get("w") and x.get("w"): N[q]["w"] = x["w"]
    tag = re.sub(r"[^a-z]", "", src.split()[0].lower())[:8] or "dir"
    key = lambda x: match.get(x["id"]) or (tag + ":" + str(x["id"]))
    for x in entries:
        if not x["live"] or x["id"] in match: continue
        k = key(x)
        par = None
        if x.get("parent"):
            pk = None
            for y in entries:
                if y["id"] == x["parent"]: pk = key(y); break
            if pk and (pk in N or any(y["id"] == x["parent"] and y["live"] for y in entries)): par = pk
        e = {"l": x["l"], "b": x["b"], "src": src, "s": 1}
        if par: e["p"] = par
        elif x.get("top"): e["p"] = x["top"]
        if x.get("w"): e["w"] = x["w"]
        N[k] = e; added += 1
    # a parent added after its child is fine; a parent never added is not
    for k, e in N.items():
        p = e.get("p")
        if p and not p.startswith("@") and p not in N: e["p"] = None if e["b"] == "leg" else "@agencies"
    d.setdefault("dirs", [])
    if src not in d["dirs"]: d["dirs"].append(src)
    json.dump(d, open(path, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"  {src}: {confirmed} confirmed current, {added} added, {dropped} taken off as closed",
          file=sys.stderr)

def dir_uk():
    """GOV.UK's register of every UK government organisation, with its
    status (live, closed, replaced…) and its parent organisations."""
    out, page = [], 1
    while True:
        j = _get_json(f"https://www.gov.uk/api/organisations?page={page}")
        for r in j["results"]:
            det = r.get("details") or {}
            slug = det.get("slug") or r["id"].rsplit("/", 1)[-1]
            fmt = (r.get("format") or "").lower()
            par = (r.get("parent_organisations") or [{}])[0].get("id", "")
            out.append({"id": slug, "l": r["title"], "w": r.get("web_url"),
                        "parent": par.rsplit("/", 1)[-1] if par else None,
                        "b": "leg" if "parliament" in fmt else ("jud" if "court" in fmt or "tribunal" in fmt else "exe"),
                        "top": "@min" if "ministerial department" == fmt else "@agencies",
                        "live": det.get("govuk_status") in ("live", "exempt", "transitioning", "joining")})
        if page >= j.get("pages", 1): break
        page += 1
    return out

def dir_us():
    """The United States Government Manual (GPO, GovInfo bulk data): the
    official handbook of the federal government, every top-level body by
    branch with its website. Newest edition on GovInfo."""
    import io, zipfile, xml.etree.ElementTree as ET
    years = _get_json("https://www.govinfo.gov/bulkdata/json/GOVMAN")["files"]
    yr = sorted((f["name"] for f in years if f["name"].isdigit()), reverse=True)[0]
    files = _get_json(f"https://www.govinfo.gov/bulkdata/json/GOVMAN/{yr}")["files"]
    z = [f["link"] for f in files if f["name"].endswith(".zip")][0]
    rq = urllib.request.Request(z, headers={"User-Agent": "HowToReachThem-govtree/1.0"})
    raw = urllib.request.urlopen(rq, timeout=300).read()
    zf = zipfile.ZipFile(io.BytesIO(raw))
    root = ET.fromstring(zf.read([n for n in zf.namelist() if n.endswith(".xml")][0]))
    out = []
    for e in root.findall("Entity"):
        cat = (e.findtext("Category") or "").strip()
        if cat.startswith("International"): continue      # not part of the US government
        name = (e.findtext("AgencyName") or "").strip()
        web = ""
        for a in e.iter("WebAddress"):
            if (a.text or "").strip(): web = a.text.strip(); break
        b = "leg" if cat.startswith("Legislative") else ("jud" if cat.startswith("Judicial") else "exe")
        top = "@min" if "Departments" in cat else (None if b != "exe" else "@agencies")
        if "The President" in cat: continue                # the heads are on the chart already
        out.append({"id": e.get("EntityId"), "l": name, "w": web, "parent": None,
                    "b": b, "top": top, "live": True})
    return out

def _get_bytes(url, timeout=300):
    rq = urllib.request.Request(url, headers={"User-Agent": "HowToReachThem-govtree/1.0 (welcometoyourgalaxy.com)"})
    with urllib.request.urlopen(rq, timeout=timeout) as r:
        return r.read()

FR_TYPES = ["Administration centrale (ou Ministère)", "Autorité administrative indépendante",
            "Autorité publique indépendante", "Institution", "Juridiction",
            "Service à compétence nationale", "Conseil, comité, commission (organisme consultatif)",
            "Établissement public"]

def dir_fr():
    """L'annuaire de l'administration (DILA, api-lannuaire.service-public.fr):
    the French state's own live directory of its services. National
    services only (catégorie SI); ministries, independent authorities,
    institutions, national courts, national services, advisory councils and
    public establishments, three tiers deep (a ministry, its directorates
    and their sub-directorates). The bureaux below that are in the
    directory too and are left off the chart: five thousand more boxes
    than a browser can lay out in one diagram."""
    where = " or ".join('type_organisme="%s"' % t for t in FR_TYPES)
    q = urllib.parse.urlencode({"select": "id,nom,type_organisme,hierarchie,site_internet,categorie",
                                "where": where})
    rows = json.loads(_get_bytes("https://api-lannuaire.service-public.fr/api/explore/v2.1/catalog/"
                                 "datasets/api-lannuaire-administration/exports/json?" + q))
    rows = [r for r in rows if r.get("categorie") == "SI" and not DIPLO.search(r.get("nom") or "")
            and not re.search(r"(?i)\b(délégation|représentation) permanente|\bambassad", r.get("nom") or "")]
    by = {r["id"]: r for r in rows}
    par = {}
    for r in rows:
        h = r.get("hierarchie")
        if isinstance(h, str):
            try: h = json.loads(h)
            except Exception: h = []
        for x in h or []:
            if x.get("type_hierarchie") == "Service Fils" and x.get("service") in by:
                par.setdefault(x["service"], r["id"])
    def depth(i):
        n = 0
        while i in par and n < 30: i = par[i]; n += 1
        return n
    out = []
    for r in rows:
        if depth(r["id"]) > 2: continue
        nm = (r.get("nom") or "").strip()
        web = ""
        try:
            si = r.get("site_internet")
            si = json.loads(si) if isinstance(si, str) else si
            if si: web = si[0].get("valeur") or ""
        except Exception: pass
        t = r.get("type_organisme") or ""
        b = ("leg" if re.search(r"(?i)assemblée nationale|\bsénat\b|parlement", nm) else
             "jud" if (t == "Juridiction" or re.search(r"(?i)\bcour\b|conseil d.état|tribunal|conseil constitutionnel", nm)) else "exe")
        top = ("@min" if nm.lower().startswith("ministère") else
               "@courts" if b == "jud" else (None if b == "leg" else "@agencies"))
        out.append({"id": r["id"], "l": nm, "w": web, "parent": par.get(r["id"]),
                    "b": b, "top": top, "live": True})
    return out

def dir_ca():
    """The Treasury Board's reference list of Government of Canada
    organization names and codes: every federal organization with its
    status (active, or wound down) and the department it reports through."""
    import csv, io
    t = _get_bytes("https://open.canada.ca/data/dataset/57180b36-3428-4a7f-afe3-2161a6b44ec5/"
                   "resource/cb5b5566-f599-4d12-abae-8279a0230928/download/gc_org_info.csv").decode("utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(t)))
    name_id = {r["harmonized_name"]: r["gc_orgID"] for r in rows}
    out = []
    for r in rows:
        nm = r["harmonized_name"].strip()
        lead = (r.get("lead_department") or "").strip()
        parent = name_id.get(lead) if lead and lead != nm else None
        b = "leg" if re.search(r"(?i)parliament|senate|house of commons|library of parliament", nm) else \
            ("jud" if re.search(r"(?i)\bcourt|tribunal|judicial|judges", nm) else "exe")
        is_dept = lead == nm
        out.append({"id": r["gc_orgID"], "l": nm, "w": "", "parent": parent, "b": b,
                    "top": "@min" if is_dept and b == "exe" else ("@courts" if b == "jud" else (None if b == "leg" else "@agencies")),
                    "live": (r.get("status_statut") or "").strip().lower() == "a"})
    return out

def dir_au():
    """The Australian Government Organisations Register (Department of
    Finance, directory.gov.au), newest quarterly snapshot on data.gov.au:
    every Commonwealth body with its portfolio, parent and website. Joint
    ventures and companies the government holds an interest in (type L),
    and international and inter-jurisdictional bodies (type J), are not
    parts of the Australian Government and are not drawn."""
    import csv, io
    pk = _get_json("https://data.gov.au/data/api/3/action/package_show?id=c77cface-69aa-4dd0-b99f-b065dc33c8e6")
    res = [r for r in pk["result"]["resources"] if (r.get("format") or "").upper() == "CSV"]
    url = sorted(res, key=lambda r: r.get("name", ""))[-1]["url"]
    t = _get_bytes(url).decode("cp1252", errors="replace").lstrip("\ufeff")
    rows = list(csv.DictReader(io.StringIO(t)))
    rows = [r for r in rows if not (r.get("Type of Body") or "").startswith(("J.", "L."))]
    by_title = {}
    for r in rows: by_title.setdefault(r["Title"].strip(), r["Id"])
    dept_of = {r["Portfolio"]: r["Id"] for r in rows if (r.get("Portfolio Dept?") or "").strip().lower().startswith("y")}
    out = []
    for r in rows:
        nm = r["Title"].strip()
        is_dept = (r.get("Portfolio Dept?") or "").strip().lower().startswith("y")
        parent = by_title.get((r.get("Parent Organisation") or "").strip()) or (None if is_dept else dept_of.get(r.get("Portfolio")))
        if parent == r["Id"]: parent = None
        b = "leg" if re.search(r"(?i)parliament|senate|house of representatives", nm) else \
            ("jud" if re.search(r"(?i)\bcourt\b|tribunal", nm) else "exe")
        out.append({"id": r["Id"], "l": nm, "w": (r.get("Website Address") or "").strip(), "parent": parent,
                    "b": b, "top": None if b == "leg" else ("@min" if is_dept else ("@courts" if b == "jud" else "@agencies")), "live": True})
    return out

def dir_br():
    """SIORG, the federal government's own register of its organisational
    structure (Ministério da Gestão, estruturaorganizacional.dados.gov.br):
    the executive branch, current version. Drawn: every órgão and entidade,
    and the units directly under each órgão (its secretariats); the ninety
    thousand units below those are in SIORG too and left off the chart."""
    d = json.loads(_get_bytes("https://estruturaorganizacional.dados.gov.br/doc/estrutura-organizacional/"
                              "resumida?codigoPoder=1&codigoEsfera=1", timeout=600))
    idf = lambda x: (x or "").rsplit("/", 1)[-1]
    U = {idf(x["codigoUnidade"]): x for x in d["unidades"] if not x.get("dataFinalVersaoConsulta")}
    typ = lambda x: idf(x["codigoTipoUnidade"])
    org = {k for k, x in U.items() if typ(x) in ("orgao", "entidade", "ente")}
    keep = set(org) | {k for k, x in U.items() if typ(x) == "unidade-administrativa"
                       and idf(x["codigoUnidadePai"]) in org and typ(U[idf(x["codigoUnidadePai"])]) == "orgao"}
    out = []
    for k in keep:
        x = U[k]; nm = (x.get("nome") or "").strip()
        p = idf(x["codigoUnidadePai"])
        is_min = typ(x) == "orgao" and nm.startswith("Ministério")
        out.append({"id": k, "l": nm, "w": "", "parent": None if is_min or p not in keep else p,
                    "b": "exe", "top": "@min" if is_min else "@agencies", "live": True})
    return out

def _ckan_latest(base, pkg, pick):
    res = _get_json(f"{base}/api/3/action/package_show?id={pkg}")["result"]["resources"]
    res = [r for r in res if pick(r)]
    return sorted(res, key=lambda r: r.get("last_modified") or r.get("created") or "")[-1]["url"]

def dir_on():
    """Ontario's own lists (data.ontario.ca): current and former ministries,
    from the government's official names reference, and every provincial
    agency with the ministry it reports to and its website."""
    import csv, io, openpyxl
    murl = _ckan_latest("https://data.ontario.ca", "government-official-names",
                        lambda r: "ministries" in (r.get("name") or "").lower() and r["url"].endswith("en-utf8-" + r["url"].rsplit("en-utf8-", 1)[-1]) and "-en-" in r["url"])
    mins = list(csv.DictReader(io.StringIO(_get_bytes(murl).decode("utf-8-sig"))))
    out, short = [], {}
    for r in mins:
        nm = r["English"].strip()
        out.append({"id": "m:" + nm, "l": nm, "w": "", "parent": None, "b": "exe", "top": "@min",
                    "live": r["Current/former ministry"].strip().lower().startswith("current")})
        if out[-1]["live"]: short[(r.get("Short form (English)") or "").strip().lower()] = "m:" + nm
    aurl = _ckan_latest("https://data.ontario.ca", "list-of-provincial-agencies",
                        lambda r: (r.get("format") or "").upper() == "XLSX")
    ws = openpyxl.load_workbook(io.BytesIO(_get_bytes(aurl)), read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    h = next(i for i, r in enumerate(rows) if r and r[0] == "Agency Name")
    head = list(rows[h])
    for r in rows[h + 1:]:
        if not r or not r[0]: continue
        x = dict(zip(head, r))
        nm = str(x["Agency Name"]).strip()
        b = "jud" if re.search(r"(?i)\btribunal|\bcourt|board of review", nm) else "exe"
        out.append({"id": "a:" + nm, "l": nm, "w": str(x.get("Website") or "").strip(),
                    "parent": short.get(str(x.get("Ministry") or "").strip().lower()),
                    "b": b, "top": "@agencies", "live": True})
    return out

def dir_it():
    """IndicePA, the official index of Italy's public administrations
    (AgID, indicepa.gov.it), refreshed daily: the national bodies — the
    Presidency of the Council and the ministries, the constitutional
    organs, the fiscal agencies, the independent authorities, national
    non-economic public bodies, research bodies, police forces,
    autonomous state administrations, public social-security bodies and
    the government's extraordinary commissioners. Regions, municipalities,
    schools, health trusts and the rest are other levels."""
    import csv, io
    url = _ckan_latest("https://indicepa.gov.it/ipa-dati", "amministrazioni",
                       lambda r: (r.get("format") or "").upper() in ("TXT", "CSV"))
    rows = list(csv.DictReader(io.StringIO(_get_bytes(url).decode("utf-8-sig")), delimiter="\t"))
    NAT = {"Presidenza del Consiglio dei Ministri, Ministeri e Avvocatura dello Stato": "@min",
           "Organi Costituzionali e di Rilievo Costituzionale": None,
           "Agenzie Fiscali": "@agencies", "Autorita' Amministrative Indipendenti": "@agencies",
           "Enti Pubblici Non Economici": "@agencies", "Enti e Istituzioni di Ricerca Pubblici": "@agencies",
           "Forze di Polizia ad Ordinamento Civile e Militare per la Tutela dell'Ordine e della Sicurezza Pubblica": "@agencies",
           "Aziende ed Amministrazioni dello Stato ad Ordinamento Autonomo": "@agencies",
           "Enti di Previdenza ed Assistenza Sociale in Conto Economico Consolidato pubblici": "@agencies",
           "Commissari Straordinari Governativi": "@agencies"}
    out = []
    for r in rows:
        cat = (r.get("tipologia_istat") or "").strip()
        if cat not in NAT: continue
        nm = (r.get("des_amm") or "").strip()
        if nm.isupper(): nm = nm[:1] + nm[1:].lower()
        b = "leg" if re.search(r"(?i)camera dei deputati|senato della repubblica", nm) else \
            ("jud" if re.search(r"(?i)\bcorte\b|consiglio di stato|consiglio superiore della magistratura|tribunal", nm) else "exe")
        top = NAT[cat] or (None if b == "leg" else ("@courts" if b == "jud" else "@agencies"))
        if top == "@min" and not re.search(r"(?i)^ministero|presidenza del consiglio", nm): top = "@agencies"
        w = (r.get("sito_istituzionale") or "").strip()
        if w and not w.startswith("http"): w = "https://" + w
        out.append({"id": r["cod_amm"], "l": nm, "w": w, "parent": None, "b": b, "top": top, "live": True})
    return out

def dir_no():
    """The Central Coordinating Register for Legal Entities
    (Brønnøysundregistrene, data.brreg.no), live: every unit in the
    sector "state administration" (institusjonell sektor 6100) with the
    unit above it, so ministries, their directorates and the courts come
    with their own hierarchy. Units with a deletion date are gone."""
    E, page = [], 0
    while True:
        d = _get_json("https://data.brreg.no/enhetsregisteret/api/enheter?institusjonellSektorkode=6100"
                      f"&size=500&page={page}")
        E += (d.get("_embedded") or {}).get("enheter", [])
        if page + 1 >= d["page"]["totalPages"]: break
        page += 1
    ids = {e["organisasjonsnummer"] for e in E}
    def nice(n):
        """the register writes every name in capitals; sentence case, with
        abbreviations — the company form at the end, a bracketed short
        name — left as they are"""
        if not n.isupper(): return n
        w = n.split(" ")
        out = [x if (x.startswith("(") or (i == len(w) - 1 and len(x) <= 3 and i > 0)) else x.lower()
               for i, x in enumerate(w)]
        s2 = " ".join(out)
        return s2[:1].upper() + s2[1:]
    out = []
    for e in E:
        nm = e["navn"].strip(); form = e["organisasjonsform"]["kode"]
        is_min = form == "STAT" and re.search(r"(?i)departementet|statsministerens kontor", nm)
        b = "leg" if re.search(r"(?i)stortinget|sivilombudet|riksrevisjonen", nm) else \
            ("jud" if re.search(r"(?i)tingrett|lagmannsrett|høyesterett|domstol|jordskifterett|rettsvesen", nm) else "exe")
        p = e.get("overordnetEnhet")
        out.append({"id": e["organisasjonsnummer"], "l": nice(nm), "w": (e.get("hjemmeside") or "").strip(),
                    "parent": p if p in ids and not is_min else None, "b": b,
                    "top": "@min" if is_min else (None if b == "leg" else ("@courts" if b == "jud" else "@agencies")),
                    "live": not e.get("slettedato") and not e.get("konkurs")})
    for x in out:
        if x["w"] and not x["w"].startswith("http"): x["w"] = "https://" + x["w"]
    return out

def dir_nl():
    """The Register van Overheidsorganisaties (organisaties.overheid.nl),
    the Dutch government's own register, exported daily: every national
    body — ministries, agencies, inspectorates, independent
    administrative bodies, advisory boards, High Councils of State, the
    courts, the police — with the ministry it belongs to. Municipalities,
    provinces, water boards and regional bodies are other levels; bodies
    with an end date are gone."""
    import xml.etree.ElementTree as ET
    raw = _get_bytes("https://organisaties.overheid.nl/archive/exportOO.xml", timeout=600)
    root = ET.fromstring(raw)
    ns = {"p": root.tag.split("}")[0].strip("{")}
    LOCAL = {"Gemeente", "Provincie", "Waterschap", "Regionaal samenwerkingsorgaan", "Caribisch openbaar lichaam",
             "Grensoverschrijdend regionaal samenwerkingsorgaan", "Provinciale Rekenkamer", "Brandweer"}
    orgs = root.find("p:organisaties", ns)
    sid = lambda o: o.get("{%s}systeemId" % ns["p"])
    out = []
    for o in orgs:
        types = [t.text or "" for t in o.findall("p:types/p:type", ns)]
        if not types or set(types) <= LOCAL: continue
        nm = (o.findtext("p:naam", "", ns) or "").strip()
        rel = o.find("p:relatieMetMinisterie", ns)
        is_min = "Ministerie" in types
        if is_min and not nm.lower().startswith("ministerie"): nm = "Ministerie van " + nm
        b = "leg" if re.search(r"(?i)kamer der staten-generaal|staten-generaal", nm) else \
            ("jud" if "Rechtspraak" in types or re.search(r"(?i)\b(rechtbank|gerechtshof|hoge raad|raad van state|college van beroep)", nm) else "exe")
        url = o.findtext("p:contact/p:internetadressen/p:internetadres/p:url", "", ns) or ""
        out.append({"id": sid(o), "l": nm, "w": url.strip(),
                    "parent": None if is_min or rel is None else sid(rel), "b": b,
                    "top": "@min" if is_min else (None if b == "leg" else ("@courts" if b == "jud" else "@agencies")),
                    "live": o.find("p:eindDatum", ns) is None})
    have = {x["id"] for x in out}
    for x in out:
        if x["parent"] not in have: x["parent"] = None
    return out

DIRECTORIES = [
    ("Q145", "GOV.UK organisations register", dir_uk, ["united kingdom", "uk "], True, "en"),
    ("Q30", "US Government Manual", dir_us, ["united states", "u.s.", "federal"], False, "en"),
    ("Q142", "annuaire de l'administration (service-public.fr)", dir_fr,
     ["république française", "france", "français", "française"], False, "fr"),
    ("Q16", "Government of Canada organization names and codes", dir_ca, ["government of canada", "canada", "canadian"], True, "en"),
    ("Q408", "Australian Government Organisations Register", dir_au, ["australian government", "australia", "australian"], False, "en"),
    ("Q1904", "Government of Ontario ministries and provincial agencies lists (data.ontario.ca)", dir_on,
     ["ontario", "government of ontario"], False, "en"),
    ("Q155", "SIORG, the federal organisational register (dados.gov.br)", dir_br,
     ["república federativa do brasil", "brasil", "brazil", "federal"], False, "pt"),
    ("Q38", "IndicePA, the index of Italian public administrations (indicepa.gov.it)", dir_it,
     ["repubblica italiana", "italia", "italiano", "italiana", "nazionale"], False, "it"),
    ("Q20", "Central Coordinating Register for Legal Entities (data.brreg.no)", dir_no,
     ["norge", "norsk", "norway", "statens"], True, "nb"),
    ("Q55", "Register van Overheidsorganisaties (organisaties.overheid.nl)", dir_nl,
     ["nederland", "nederlandse", "rijks", "rijk"], True, "nl"),
]

def directories(only=None):
    for q, src, fn, words, drop, lang in DIRECTORIES:
        if only and q not in only: continue
        path = os.path.join(OUT, q + ".json")
        if not os.path.exists(path): continue
        try:
            entries = fn()
        except Exception as e:
            print(f"  {src}: not reachable ({e}); chart left as built", file=sys.stderr); continue
        _apply(path, entries, src, words, drop, lang,
               complete_min=any(x.get("top") == "@min" for x in entries))

def patch_coords():
    """Add coordinates to every chart already on disk without rebuilding
    it: one query per 400 bodies rather than the whole build."""
    import glob
    files = sorted(glob.glob(os.path.join(OUT, "Q*.json")))
    qs = set()
    docs = {}
    for f in files:
        d = json.load(open(f)); docs[f] = d
        qs |= set(d.get("n", {})); qs |= {h["q"] for h in d.get("heads", [])}
    print(len(files), "charts,", len(qs), "bodies", file=sys.stderr)
    xy = coords(qs)
    n = 0
    for f, d in docs.items():
        for q, e in d.get("n", {}).items():
            if q in xy: e["c"] = xy[q]; n += 1
        for h in d.get("heads", []):
            if h["q"] in xy: h["c"] = xy[h["q"]]
        with open(f, "w") as fh:
            json.dump(d, fh, ensure_ascii=False, separators=(",", ":"))
    print(n, "bodies placed", file=sys.stderr)

def main():
    # --as Q29999 Q55: build Q55's government and file it as Q29999's,
    # for a country whose code sits on one item and its government on another
    AS = None
    args = sys.argv[1:]
    if args[:1] == ["--as"]: AS = args[1]; args = args[2:]
    global REGIONS, P17C
    if args[:1] == ["--coords"]:
        return patch_coords()
    if args[:1] == ["--coextensive"]:
        return coextensive()
    if args[:1] == ["--directories"]:
        return directories(set(args[1:]))
    if args[:1] == ["--regions"]:
        REGIONS = True; P17C = ""; args = args[1:]
    only = set(a for a in args if re.match(r"^Q\d+$", a))
    cs = regions(only) if REGIONS else countries(only)
    print(len(cs), "countries", file=sys.stderr)
    ql = list(cs)
    ap = apex(ql); mins = ministries(ql, ap)
    agen = national(ql, "Q327333", strict=True); crts = national(ql, "Q41487")
    print("apex, ministries, agencies, courts read", file=sys.stderr)

    # the tree, breadth first, one country at a time but asked in bulk
    trees = {}
    frontier = {}   # node -> (country, branch, depth-left)
    parent = {}     # (country,node) -> parent
    branch_of = {}
    for c in ql:
        a = ap[c]
        t = {"leg": [], "exe": [], "jud": [], "hos": a["hos"], "hog": a["hog"]}
        seen = set()
        def put(n, br, par, depth):
            if (c, n) in parent or n in a["hos"] or n in a["hog"]: return
            parent[(c, n)] = par; branch_of[(c, n)] = br
            frontier[(c, n)] = depth
        for n in a["leg"]: put(n, "leg", None, 3)
        for n in a["exe"]: put(n, "exe", None, 1)
        for n in a["court"]: put(n, "jud", None, 2)
        for n in mins[c]: put(n, "exe", "@min", 2)
        trees[c] = t
    level = dict(frontier)
    global ALLEDGE
    while level:
        open_ = {k: d for k, d in level.items() if d > 0}
        if not open_: break
        byq = defaultdict(list)
        for (c, n), d in open_.items(): byq[n].append((c, d))
        kids = children(list(byq))
        for x, ps in kids.items(): ALLEDGE[x] |= ps
        nxt = {}
        for x, ps in kids.items():
            for p in sorted(ps):
                for (c, d) in byq.get(p, []):
                    if (c, x) in parent: continue
                    if x in ap[c]["hos"] or x in ap[c]["hog"]: continue
                    parent[(c, x)] = p; branch_of[(c, x)] = branch_of[(c, p)]
                    nxt[(c, x)] = d - 1
                    # a court reached through the executive (the US federal
                    # courts are filed under the federal government) belongs
                    # to the judiciary, and its own courts are read below it
                    if x in COURT:
                        branch_of[(c, x)] = "jud"; nxt[(c, x)] = max(d - 1, 2)
        level = nxt
        print("level done:", len(nxt), file=sys.stderr)
    # a ministry that is subordinate to another body on the chart (the US
    # Department of the Navy to Defense) hangs under it, not beside it
    extra = children(list(set(n for c in ql for n in mins[c])))
    for x, ps in extra.items(): ALLEDGE[x] |= ps
    for c in ql:
        for n in mins[c]:
            if parent.get((c, n)) != "@min": continue
            for p in sorted(ALLEDGE.get(n, ())):
                if (c, p) not in parent or p == n or p not in mins[c]: continue
                a, ok = p, True
                for _ in range(12):
                    if a == n: ok = False; break
                    a = parent.get((c, a))
                    if not a or a.startswith("@"): break
                if ok: parent[(c, n)] = p; break
    # national bodies not reached from a root
    for c in ql:
        for n in sorted(crts[c]):
            if (c, n) not in parent: parent[(c, n)] = "@courts"; branch_of[(c, n)] = "jud"
        for n in sorted(agen[c]):
            if (c, n) not in parent: parent[(c, n)] = "@agencies"; branch_of[(c, n)] = "exe"

    allq = set(ql) | set(n for (_, n) in parent) | set(x for c in ql for k in ("hos", "hog") for x in ap[c][k])
    lab, desc, site = labels(allq)
    al = aliases(allq)
    cur = current(allq)
    xy = coords(allq)
    al_lab = labels(set(o for s in al.values() for o in s))[0]

    divs = divisions(ql)
    os.makedirs(OUT, exist_ok=True)
    index = {}
    for c in ql:
        nodes = {}
        for (cc, n), p in parent.items():
            if cc != c: continue
            L = lab.get(n)
            if not L or re.match(r"^Q\d+$", L): continue
            if DEFUNCT_DESC.search(desc.get(n, "")): continue
            if DIPLO.search(L): continue
            if CASE.search(L): continue
            # a law filed as if it were a body, and a ministry named for
            # the leader who formed it, which is a term of office
            if LAWDOC.search(L) or TENURE_MIN.search(L): continue
            # a caucus is a club of members, not a body of the legislature
            if CAUCUS.search(L): continue
            p0 = parent[(cc, n)]
            if p0 is not None:
                # a cabinet named for one leader is a term of office
                if TENURE.search(L) and not TENURE_OK.search(L): continue
                # a state's own department filed under the national one
                if any(L.startswith(dv + " ") and dv not in lab.get(c, "") for dv in divs[c]
                       if len(dv) > 3): continue
            nodes[n] = {"l": L, "p": p, "b": branch_of[(c, n)]}
        # a body whose parent fell out goes with it: the parent was dropped
        # as ended, ad hoc or not part of government, and what sat under
        # it almost always shares that fate (the House Resources
        # subcommittees outlived their committee on Wikidata, not in fact)
        def drop_orphans():
            gone = True
            while gone:
                gone = [n for n, o in nodes.items()
                        if o["p"] and not o["p"].startswith("@") and o["p"] not in nodes]
                for n in gone: nodes.pop(n)
        drop_orphans()
        # committees named for one bill end with it
        for n in [n for n, o in nodes.items() if o["b"] == "leg" and ADHOC.search(o["l"])]:
            nodes.pop(n)
        drop_orphans()
        heads = []
        for k, nm in (("hos", "Head of state"), ("hog", "Head of government")):
            for x in ap[c][k]:
                if x in lab and not any(h["q"] == x for h in heads):
                    heads.append({"q": x, "l": lab[x], "r": nm})
                    if x in xy: heads[-1]["c"] = xy[x]
        for h in heads:
            if any(x["q"] == h["q"] for x in heads if x is not h): pass
        # a single office that is both
        if len(heads) == 2 and heads[0]["q"] == heads[1]["q"]: heads = heads[:1]
        both = set(ap[c]["hos"]) & set(ap[c]["hog"])
        for h in heads:
            if h["q"] in both: h["r"] = "Head of state and government"
        out = {"q": c, "iso3": cs[c]["iso3"], "heads": heads, "n": {}}
        if REGIONS: out["in"] = PARENT.get(c)
        for n, o in nodes.items():
            e = {"l": o["l"], "b": o["b"]}
            if o["p"]: e["p"] = o["p"]
            if n in desc: e["d"] = desc[n]
            if n in site: e["w"] = site[n]
            if al.get(n): e["a"] = sorted(al[n])
            if n not in cur: e["u"] = 1
            if n in xy: e["c"] = xy[n]
            out["n"][n] = e
        kids = defaultdict(int)
        for n, e in out["n"].items():
            if e.get("p"): kids[e["p"]] += 1
        for n, e in out["n"].items():
            sc = 0
            if e.get("w"): sc += 2
            if e.get("a"): sc += 2
            if kids[n]: sc += 1 + min(kids[n], 20) / 10
            if WEIGHTY.search(e["l"]): sc += 1
            if MINOR.search(e["l"]): sc -= 2
            if e.get("u"): sc -= 4
            e["s"] = round(sc, 1)
        # alias labels, so the page can say what lit a body
        out["al"] = {o: al_lab[o] for n in out["n"] for o in out["n"][n].get("a", []) if o in al_lab}
        if not out["n"] and not heads: continue
        if AS:
            out["via"] = c; out["q"] = AS
            old = os.path.join(OUT, AS + ".json")
            if os.path.exists(old): out["iso3"] = json.load(open(old)).get("iso3")
            c = AS
        with open(os.path.join(OUT, c + ".json"), "w") as f:
            json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
        index[c] = {"iso3": out["iso3"], "n": len(out["n"]),
                    "leg": sum(1 for x in out["n"].values() if x["b"] == "leg"),
                    "exe": sum(1 for x in out["n"].values() if x["b"] == "exe"),
                    "jud": sum(1 for x in out["n"].values() if x["b"] == "jud"),
                    "heads": len(heads),
                    "cur": sum(1 for x in out["n"].values() if not x.get("u"))}
    IX = "regions.json" if REGIONS else "index.json"
    if only and os.path.exists(os.path.join(OUT, IX)):
        old = json.load(open(os.path.join(OUT, IX)))
        old.get("c", {}).update(index); index = old["c"]
    json.dump({"built": time.strftime("%Y-%m-%d"), "source": "Wikidata via QLever", "c": index},
              open(os.path.join(OUT, IX), "w"), separators=(",", ":"))
    print(len(index), "countries written", file=sys.stderr)
    thin = sorted((v["n"], k, v["iso3"]) for k, v in index.items() if v["n"] < 10)
    if thin and not only and not REGIONS:
        print("thin charts - check whether the government is filed on another item "
              "and rebuild with --as:", thin, file=sys.stderr)

if __name__ == "__main__":
    main()
