#!/usr/bin/env python3
"""Where the map stands, per layer and per field, measured rather than estimated.

Run this at the end of every round and paste the two tables it prints into
the round's section of HOW_TO_REACH_THEM_HANDOFF.md.  The point is not
bookkeeping: the second table is what decides which country the next round
should touch, because it separates "no contact published anywhere" from
"published and not joined yet".

    python3 -I tools/completeness.py            # the whole chart
    python3 -I tools/completeness.py --quick    # layers only, no per-country

QLever first and Wikidata's own service second, for the reason round
nineteen gives: WDQS has been answering `429 Aggressively rate-limiting to
1 req / min` through an outage, which makes a census of this shape
impossible, and QLever answers the same dump in milliseconds.  QLever is a
third party and its index is a dump rather than the live store, so a figure
from it is "as of that dump" and the two are spot-checked against each
other on the totals.
"""
import json, sys, time, urllib.parse, urllib.request

ENDPOINTS = ["https://qlever.dev/api/wikidata",
             "https://qlever.cs.uni-freiburg.de/api/wikidata",
             "https://query.wikidata.org/sparql"]
PRE = ("PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
       "PREFIX wd: <http://www.wikidata.org/entity/> ")

def ask(q, tries=3):
    body = urllib.parse.urlencode({"query": PRE + q}).encode()
    last = ""
    for ep in ENDPOINTS:
        for att in range(tries):
            try:
                rq = urllib.request.Request(ep, data=body, headers={
                    "Accept": "application/sparql-results+json",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "HowToReachThem/1.0 (welcometoyourgalaxy.com)"})
                with urllib.request.urlopen(rq, timeout=300) as r:
                    return json.loads(r.read())["results"]["bindings"]
            except Exception as e:
                last = f"{ep}: {e}"
                # a 429 asks for a wait; anything else is tried once more then moved on
                time.sleep(2 * (att + 1))
    raise SystemExit("every endpoint refused: " + last)

def one(q):
    b = ask(q)
    return int(b[0]["n"]["value"]) if b else 0

# the layers, each by the class the boundary files and the panel actually use
# The layers, each by the class the chain actually resolves to. The
# second-level row that was here measured nothing and is gone: no country
# types its counties as "second-level administrative division" — they are
# counties, powiats, comarcas, each its own class — so that tier is counted
# by the body that makes its law instead, under the table.
LAYERS = [
    ("Countries",             "wd:Q6256",     "; wdt:P298 ?iso3"),
    ("First-level divisions", "wd:Q10864048", ""),
    ("Municipalities",        "wd:Q15284",    ""),
]
# the fields the panel draws, in the order a reader uses them
FIELDS = [("Website", "P856"), ("Email", "P968"), ("Telephone", "P1329"),
          ("Street address", "P6375"), ("Lawmaking body", "P194")]

def live(cls, extra=""):
    """Undissolved instances of a class, optionally carrying one property.
    The extra triple goes in the pattern and not after the FILTER: a `;`
    following a FILTER is a syntax error, which is what the first version of
    this did and why every endpoint answered 400."""
    return ("?x wdt:P31/wdt:P279* %s %s . "
            "FILTER NOT EXISTS { ?x wdt:P576 ?d } " % (cls, extra))

def layer_table(quick=False):
    rows = []
    for name, cls, keep in LAYERS:
        tot = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { " + live(cls, keep) + "}")
        got = {}
        for fname, p in FIELDS:
            got[fname] = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { "
                             + live(cls, keep + "; wdt:%s ?v" % p) + "}")
        rows.append((name, tot, got))
    out = ["| Layer | Units | " + " | ".join(f for f, _ in FIELDS) + " |",
           "| --- | ---: | " + " | ".join("---:" for _ in FIELDS) + " |"]
    for name, tot, got in rows:
        cells = []
        for fname, _ in FIELDS:
            n = got[fname]
            cells.append(f"{n:,} ({0 if not tot else round(100*n/tot)}%)")
        out.append(f"| {name} | {tot:,} | " + " | ".join(cells) + " |")
    return "\n".join(out), rows

PER_COUNTRY = """
SELECT ?iso (COUNT(DISTINCT ?x) AS ?n)
            (COUNT(DISTINCT ?xw) AS ?w) (COUNT(DISTINCT ?xe) AS ?e)
            (COUNT(DISTINCT ?xp) AS ?p) (COUNT(DISTINCT ?xa) AS ?a) WHERE {
  ?x wdt:P31/wdt:P279* wd:Q15284 ; wdt:P17 ?c .
  ?c wdt:P298 ?iso .
  FILTER NOT EXISTS { ?x wdt:P576 ?d }
  OPTIONAL { ?x wdt:P856  ?vw . BIND(?x AS ?xw) }
  OPTIONAL { ?x wdt:P968  ?ve . BIND(?x AS ?xe) }
  OPTIONAL { ?x wdt:P1329 ?vp . BIND(?x AS ?xp) }
  OPTIONAL { ?x wdt:P6375 ?va . BIND(?x AS ?xa) }
} GROUP BY ?iso ORDER BY DESC(?n) LIMIT 40
"""

def country_table():
    b = ask(PER_COUNTRY)
    out = ["| Country | Municipalities | Website | Email | Telephone | Street |",
           "| --- | ---: | ---: | ---: | ---: | ---: |"]
    tot = 0
    for r in b:
        n = int(r["n"]["value"]); tot += n
        def pc(k):
            v = int(r[k]["value"])
            return f"{round(100*v/n)}%" if n else "—"
        out.append(f"| {r['iso']['value']} | {n:,} | {pc('w')} | {pc('e')} | "
                   f"{pc('p')} | {pc('a')} |")
    out.append(f"\nThose {len(b)} countries hold {tot:,} municipalities.")
    return "\n".join(out)

def shards():
    """What the registers have actually shipped, read off disk."""
    try:
        idx = json.load(open("muni/index.json"))
    except Exception:
        return ("`muni/` is not in this checkout, so the register layer "
                "cannot be counted here. If the shards exist only on a local "
                "machine they are not deployed: the page fetches them from "
                "this repo.")
    import glob, os
    recs, fields = 0, {}
    for f in glob.glob("muni/[0-9]*.json"):
        for q, v in json.load(open(f)).items():
            recs += 1
            for k in v:
                fields[k] = fields.get(k, 0) + 1
    line = ", ".join(f"{k} {v:,}" for k, v in sorted(fields.items(),
                     key=lambda kv: -kv[1]))
    return (f"Shards: {recs:,} records across "
            f"{len(idx.get('countries', idx) or [])} registers. Fields: {line}")

if __name__ == "__main__":
    quick = "--quick" in sys.argv
    t, rows = layer_table()
    print("### Completeness by layer and field\n")
    print(t)
    # The county tier, counted the way round eleven rebuilt it: a territory
    # or a government with a legislature, rather than anything carrying P194.
    terr = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { "
               "?x wdt:P31/wdt:P279* wd:Q56061 ; wdt:P194 ?b . "
               "FILTER NOT EXISTS { ?x wdt:P576 ?d } }")
    govs = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { "
               "?x wdt:P31/wdt:P279* wd:Q7188 ; wdt:P194 ?b . "
               "FILTER NOT EXISTS { ?x wdt:P576 ?d } }")
    print(f"\nJurisdictions of any level with a lawmaking body recorded: "
          f"{terr:,} territories and {govs:,} governments (the SUBLEG universe; "
          f"round eleven exhausted this source).")
    print(f"\n{shards()}\n")
    if not quick:
        print("### Municipalities by country, worst gaps first to work from\n")
        print(country_table())
