#!/usr/bin/env python3
"""One diagram per country of how its national government is organised.

Writes govtree/<Q-id>.json (one file per country) and govtree/index.json.
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

def ask(q, tries=3):
    body = urllib.parse.urlencode({"query": PRE + q}).encode()
    last = ""
    for ep in EP:
        for a in range(tries):
            try:
                rq = urllib.request.Request(ep, data=body, headers={
                    "Accept": "application/sparql-results+json",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "HowToReachThem-govtree/1.0 (welcometoyourgalaxy.com)"})
                with urllib.request.urlopen(rq, timeout=900) as r:
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
    """child -> parents, for organisations placed under any of `parents`"""
    out = defaultdict(set)
    for ch in chunks(parents, 400):
        rows = ask(f"""SELECT DISTINCT ?X ?P ?court WHERE {{ VALUES ?P {{ {vals(ch)} }}
          {{ ?X p:P361 ?s . ?s ps:P361 ?P . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?X p:P749 ?s . ?s ps:P749 ?P . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?P p:P527 ?s . ?s ps:P527 ?X . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?P p:P355 ?s . ?s ps:P355 ?X . FILTER NOT EXISTS {{ ?s pq:P582 ?_q }} }}
          UNION {{ ?X wdt:P31 ?P }}
          {{ ?X wdt:P31/wdt:P279* wd:Q43229 }} UNION {{ ?X wdt:P279+ wd:Q43229 }}
          OPTIONAL {{ ?X wdt:P31/wdt:P279* ?_ct . VALUES ?_ct {{ wd:Q41487 wd:Q105985 }} BIND(1 AS ?court) }}
          {ENDED} {NOTBODY_F} }}""")
        for r in rows:
            out[v(r, "X")].add(v(r, "P"))
            if r.get("court"): COURT.add(v(r, "X"))
    return out
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

ALLEDGE = defaultdict(set)
WEIGHTY = re.compile(r"\b(ministry|department|agency|authority|commission|administration|bureau|"
                     r"service|directorate|court|tribunal|house|senate|chamber|assembly|council|"
                     r"committee|office)\b", re.I)
MINOR = re.compile(r"\b(group|forum|panel|unit|team|task ?force|working|stakeholder|network|"
                   r"programme|program|project|initiative|small (and disadvantaged )?business)\b", re.I)

def main():
    # --as Q29999 Q55: build Q55's government and file it as Q29999's,
    # for a country whose code sits on one item and its government on another
    AS = None
    args = sys.argv[1:]
    if args[:1] == ["--as"]: AS = args[1]; args = args[2:]
    global REGIONS, P17C
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
