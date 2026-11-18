#!/usr/bin/env python3
"""Where the map stands, per layer and per field, measured rather than estimated.

Run this at the end of every round and paste the two tables it prints into
the round's section of HOW_TO_REACH_THEM_HANDOFF.md.  The point is not
bookkeeping: the second table is what decides which country the next round
should touch, because it separates "no contact published anywhere" from
"published and not joined yet".

    python3 -I tools/completeness.py            # the whole chart
    python3 -I tools/completeness.py --quick    # layers only, no per-country
    python3 -I tools/completeness.py --record 23   # and add a row to the ledger
    python3 -I tools/completeness.py --history     # the ledger, as a table

`--record N` appends this round's figures to `tools/rounds.json` and prints
the whole ledger. Run it once at the end of every round and paste the
history table into the round's section, because a single round's chart says
where the map stands and only the ledger says whether a round moved it:
rounds five to eleven in this file added no municipal records at all, and
nothing in the file at the time said so.

QLever first and Wikidata's own service second, for the reason round
nineteen gives: WDQS has been answering `429 Aggressively rate-limiting to
1 req / min` through an outage, which makes a census of this shape
impossible, and QLever answers the same dump in milliseconds.  QLever is a
third party and its index is a dump rather than the live store, so a figure
from it is "as of that dump" and the two are spot-checked against each
other on the totals.
"""
import json, os, sys, time, urllib.parse, urllib.request

# Run from anywhere: the ledger sits beside this file and the shards above it.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

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
        idx = json.load(open(os.path.join(ROOT, "muni", "index.json")))
    except Exception:
        return ("`muni/` is not in this checkout, so the register layer "
                "cannot be counted here. If the shards exist only on a local "
                "machine they are not deployed: the page fetches them from "
                "this repo.")
    # `import os` here would make `os` local to this whole function and the
    # path join above would raise before the import ran, which the except
    # then reported as "not in this checkout" while the shards sat there.
    import glob
    recs, fields = 0, {}
    for f in glob.glob(os.path.join(ROOT, "muni", "[0-9]*.json")):
        for q, v in json.load(open(f)).items():
            recs += 1
            for k in v:
                fields[k] = fields.get(k, 0) + 1
    line = ", ".join(f"{k} {v:,}" for k, v in sorted(fields.items(),
                     key=lambda kv: -kv[1]))
    return (f"Shards: {recs:,} records across "
            f"{len(idx.get('countries', idx) or [])} registers. Fields: {line}")

LEDGER = os.path.join(HERE, "rounds.json")

def municipal_fields():
    """The three columns the municipal rounds are about, measured."""
    cls, keep = "wd:Q15284", ""
    tot = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { " + live(cls, keep) + "}")
    out = {"municipalities": tot}
    for fname, pid in [("website", "P856"), ("email", "P968"),
                       ("telephone", "P1329"), ("street", "P6375")]:
        out[fname] = one("SELECT (COUNT(DISTINCT ?x) AS ?n) WHERE { "
                         + live(cls, "; wdt:%s ?v" % pid) + "}")
    return out

def shard_counts():
    try:
        idx = json.load(open(os.path.join(ROOT, "muni", "index.json")))
    except Exception:
        return {}, 0
    per = {k: v["shipped"] for k, v in (idx.get("counts") or {}).items()}
    return per, sum(per.values())

def record(n):
    try:
        led = json.load(open(LEDGER))
    except Exception:
        led = []
    per, tot = shard_counts()
    row = {"round": int(n), "date": time.strftime("%Y-%m-%d"),
           "shards": tot, "registers": len(per), "per_register": per}
    row.update(municipal_fields())
    led = [r for r in led if r.get("round") != int(n)] + [row]
    led.sort(key=lambda r: r["round"])
    json.dump(led, open(LEDGER, "w"), indent=1)
    return led

def history():
    try:
        led = json.load(open(LEDGER))
    except Exception:
        return "(no ledger yet — run with --record N)"
    out = ["| Round | Date | Registers | Records in the shards | "
           "Municipal website | email | telephone | street |",
           "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for r in led:
        m = r.get("municipalities") or 0
        pc = lambda k: (f"{round(100*r.get(k,0)/m)}%" if m else "—")
        out.append(f"| {r['round']} | {r['date']} | {r.get('registers',0)} | "
                   f"{r.get('shards',0):,} | {pc('website')} | {pc('email')} | "
                   f"{pc('telephone')} | {pc('street')} |")
    led2 = [r for r in led if r.get("shards") is not None]
    if len(led2) >= 2:
        d = led2[-1]["shards"] - led2[0]["shards"]
        n = led2[-1]["round"] - led2[0]["round"]
        if n > 0:
            out.append(f"\nAcross those {n} rounds the shards grew by {d:,} "
                       f"records, {round(d/n):,} a round. The municipal "
                       f"percentages are Wikidata alone and move slowly; the "
                       f"shards are what a round adds.")
    return "\n".join(out)

if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--history" in argv:
        print("### The ledger, one row per round\n")
        print(history())
        raise SystemExit(0)
    rec = None
    if "--record" in argv:
        i = argv.index("--record")
        rec = argv[i+1] if len(argv) > i+1 else None
        if rec is None:
            raise SystemExit("--record needs a round number")
    quick = "--quick" in argv
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
    if rec is not None:
        record(rec)
        print("\n### The ledger, one row per round\n")
        print(history())
