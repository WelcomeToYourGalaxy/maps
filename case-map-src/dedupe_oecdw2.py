#!/usr/bin/env python3
"""Second-pass dedupe: find OECD Watch leads whose underlying event is already a case,
even where the complaint is not named in any cx. Round 46 found four such leads in one
batch of twelve, so the first-pass title match is not enough."""
import json, re, unicodedata, collections, os

S = os.path.dirname(os.path.abspath(__file__)) + "/"

def norm(t):
    t = unicodedata.normalize("NFKD", (t or "")).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", t.lower()).split())

STOP = set("the of and for ltd ltd. limited inc inc. plc sa s.a a.g ag nv n.v bv b.v co corp "
           "corporation company group holdings holding international co. gmbh pty se oyj asa ab "
           "as a s spa s.p.a srl mining energy resources power engineering construction "
           "bank banking finance financial development developments project projects industries "
           "industry oil gas petroleum coal gold minerals mineral metals commodities agro agri "
           "plantation plantations water services service systems technologies global national "
           "state enterprise trading trade investments investment capital fund funds partners "
           "consortium joint venture subsidiary works plant plants company's export import credit "
           "agency authority public private union federation association foundation institute "
           # round 47: corporate-form words in other jurisdictions, which pair any two companies
           # from the same country. "sdn"/"bhd" matched a Malaysian electronics supplier to a
           # Malaysian railway case; they are the local equivalent of "Ltd".
           "sdn bhd tbk llc llp ltda cia cie oy oyj kk kgaa pjsc jsc ooo sarl sas aps "
           # round 47: generic organisational words. "committee" matched the International
           # Olympic Committee to a Chinese industrial zone's Management Committee.
           "committee council board commission organisation organization secretariat ministry "
           "department office bureau".split())

# country and place words carry no company identity: a lead in Nigeria matching a case in
# Nigeria on the word "nigeria" is not a match. Round 46's first pass produced a dozen of these.
PLACEWORDS = set()


def toks(name):
    return {w for w in norm(name).split()
            if w not in STOP and w not in PLACEWORDS and len(w) > 2}

s = open(S + "base.html", encoding="utf-8").read()
i = s.index("window.CASES = ") + len("window.CASES = ")
CASES = json.JSONDecoder().raw_decode(s[i:])[0]

# ISO3 for the country names OECD Watch uses, built from the cases themselves where possible
iso_by_name = {}
for c in CASES:
    iso_by_name.setdefault(norm(c.get("place","").split(",")[-1]), c.get("iso3"))

case_names = []
for c in CASES:
    names = set()
    for co in (c.get("companies") or []):
        names |= toks(co.get("name"))
    for l in (c.get("lenders") or []):
        names |= toks(re.sub(r"\(.*", "", l.get("name") or ""))
    blob = norm(" ".join([c.get("title",""), c.get("place",""), c.get("point","") or "",
                          c.get("community","") or "", c.get("outcome","") or ""]))
    case_names.append((c["id"], c.get("iso3"), names, blob, norm(c.get("title",""))))

leads = json.load(open(S + "docs/leads_oecdwatch.json"))

# fill PLACEWORDS: every word of every country name a lead uses, and of every case's place
for r in leads:
    for cn in (r.get("countries") or []):
        PLACEWORDS.update(norm(cn).split())
for c in CASES:
    PLACEWORDS.update(norm(c.get("place","")).split())
PLACEWORDS.discard("")

# rebuild the case name sets now that PLACEWORDS is known
case_names = []
for c in CASES:
    names = set()
    for co in (c.get("companies") or []):
        names |= toks(co.get("name"))
    for l in (c.get("lenders") or []):
        names |= toks(re.sub(r"\(.*", "", l.get("name") or ""))
    blob = norm(" ".join([c.get("title",""), c.get("place",""), c.get("point","") or "",
                          c.get("community","") or "", c.get("outcome","") or ""]))
    case_names.append((c["id"], c.get("iso3"), names, blob, norm(c.get("title",""))))

# a token shared by many cases identifies nothing; keep only distinctive ones
df = collections.Counter()
for _, _, names, _, _ in case_names:
    df.update(names)
DISTINCT = {w for w, n in df.items() if n <= 4}
print("company tokens in cases:", len(df), "— distinctive (in 4 cases or fewer):", len(DISTINCT))

hits = []
for r in leads:
    if r["already_on_map"]:
        continue
    # round 47: a pair a checker settled as a false match is not re-proposed. The lead stays
    # open as a possible case of its own; it is this pairing that is closed.
    if r.get("r47_false_match"):
        continue
    want = toks(r.get("company_in_violation") or "") | toks(r.get("defendant") or "")
    if not want:
        continue
    ctry = {norm(x) for x in r.get("countries") or []}
    for cid, iso, names, blob, ctitle in case_names:
        shared = (want & names) & DISTINCT
        if not shared:
            continue
        # the company matches; now require the country or the place to line up too
        same_place = any(x and x in blob for x in ctry)
        if same_place:
            hits.append({"slug": r["slug"], "title": r["title"], "case": cid,
                         "shared_company_words": sorted(shared),
                         "countries": r["countries"], "status": r["status"]})
            break

json.dump(hits, open(S + "docs/oecdw_probable_dupes.json", "w"), indent=1, ensure_ascii=False)
print("open leads checked:", sum(1 for r in leads if not r["already_on_map"]))
print("probable duplicates of existing cases:", len(hits))
by = collections.Counter(h["case"] for h in hits)
print("\ncases they point at (top 15):")
for k, v in by.most_common(15):
    print("  %-40s %d" % (k, v))
print("\nfirst 20 pairs:")
for h in hits[:20]:
    print("  %-46s -> %-34s %s" % (h["title"][:46], h["case"][:34], ",".join(h["shared_company_words"])[:28]))
