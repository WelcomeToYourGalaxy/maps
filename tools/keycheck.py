#!/usr/bin/env python3
"""Which identifiers a country's municipalities actually carry, counted.

Run this before touching any country. Rounds seven and twelve each picked
the property they expected — the KSH code for Hungary, the TERC code for
Poland — counted how many municipalities carried it, and concluded from a
miss that the country had nothing to join on. That finds what you already
suspected and nothing else: Germany was written off for two rounds as
carrying "no national statistical code at all", and it carries `P439`, the
municipality key, on 81% of them. Asking the other way round — every
literal-valued property these items hold, ranked — took one query and put
it near the top of the list.

    python3 -I tools/keycheck.py DEU
    python3 -I tools/keycheck.py DEU POL HUN SVK      # one call each
    python3 -I tools/keycheck.py --class Q10864048 ESP   # another tier

What to do with the answer, which is round seven's order and has not
changed: a code on Wikidata, then the register carrying that same code,
and only then download anything. And the code has to identify the *body*:
a `municipality.code` on an address is the municipality the address sits
in, which is what rounds thirteen and seventeen refused for Slovakia and
for Italy's provinces.
"""
import json, re, sys, time, urllib.parse, urllib.request

ENDPOINTS = ["https://qlever.dev/api/wikidata",
             "https://qlever.cs.uni-freiburg.de/api/wikidata",
             "https://query.wikidata.org/sparql"]
PRE = ("PREFIX wdt: <http://www.wikidata.org/prop/direct/> "
       "PREFIX wd: <http://www.wikidata.org/entity/> "
       "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> ")

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
                time.sleep(2 * (att + 1))
    raise SystemExit("every endpoint refused: " + last)

CENSUS = """
SELECT ?p (COUNT(DISTINCT ?x) AS ?n) WHERE {
  ?x wdt:P31/wdt:P279* wd:%(cls)s ; wdt:P17 ?c .
  ?c wdt:P298 "%(iso)s" .
  FILTER NOT EXISTS { ?x wdt:P576 ?d }
  ?x ?p ?v . FILTER(isLiteral(?v))
} GROUP BY ?p ORDER BY DESC(?n) LIMIT 60
"""
TOTAL = """
SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE {
  ?x wdt:P31/wdt:P279* wd:%(cls)s ; wdt:P17 ?c . ?c wdt:P298 "%(iso)s" .
  FILTER NOT EXISTS { ?x wdt:P576 ?d } }
"""
# the four fields the page draws, so they can be told apart from identifiers
CONTACT = {"P856": "website", "P968": "email", "P1329": "telephone",
           "P6375": "street address", "P281": "postal code"}

def labels(pids):
    if not pids:
        return {}
    vals = " ".join("wd:" + p for p in pids)
    rows = ask("SELECT ?p ?l WHERE { VALUES ?p { %s } ?p rdfs:label ?l . "
               "FILTER(LANG(?l)='en') }" % vals)
    return {r["p"]["value"].rsplit("/", 1)[-1]: r["l"]["value"] for r in rows}

def one(iso, cls):
    tot = int(ask(TOTAL % {"cls": cls, "iso": iso})[0]["n"]["value"])
    if not tot:
        print(f"\n## {iso}: no undissolved items of {cls} with that country\n")
        return
    rows = ask(CENSUS % {"cls": cls, "iso": iso})
    seen = []
    for r in rows:
        m = re.search(r"/(P\d+)$", r["p"]["value"])
        if m:
            seen.append((m.group(1), int(r["n"]["value"])))
    lab = labels([p for p, _ in seen[:40]])
    print(f"\n## {iso}: {tot:,} undissolved units of {cls}\n")
    print("| Property | What it is | Carrying it | Share |")
    print("| --- | --- | ---: | ---: |")
    for p, n in seen[:30]:
        what = CONTACT.get(p) or lab.get(p, "")
        mark = " **(contact field)**" if p in CONTACT else ""
        print(f"| {p} | {what}{mark} | {n:,} | {round(100*n/tot)}% |")
    best = [(p, n) for p, n in seen if p not in CONTACT and n >= tot * 0.5]
    if best:
        print("\nJoinable on: " + ", ".join(
            f"{p} ({lab.get(p,'?')}, {round(100*n/tot)}%)" for p, n in best[:6]))
    else:
        print("\nNo identifier on half or more of them. A register cannot be "
              "joined to this country until one is imported — which is the "
              "wall Slovakia, Estonia, Greece and Japan are behind, and "
              "importing it is a smaller job than finding a second register.")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    cls = "Q15284"
    if "--class" in args:
        i = args.index("--class"); cls = args[i+1]; del args[i:i+2]
    if not args:
        raise SystemExit(__doc__)
    for iso in args:
        one(iso.upper(), cls)
