#!/usr/bin/env python3
"""Coverage figures for the central bank capture map.
Breadth = share of monetary authorities on the map holding at least one record
of that kind. Computed exactly from the data files. Depth estimates live in
about.html and are a judgement, not a computation."""
import json
import os, sys
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
L = lambda n: json.load(open(os.path.join(A, n)))

cor = L('corruption.json'); gaps = L('gaps.json'); net = L('networks.json')
ev = L('events_gold.json'); sw = L('swaps.json'); own = L('owners.json')
core = json.load(open(os.path.join(A, '..', 'out', 'core.json')))

places = set(core['E'])
N = len(places)

import sys as _s; _s.path.insert(0, os.path.join(A, '..'))
from cbnames import UNION
# A tie held by a currency union is held by every member country: expand it, the way cases already expand.
def expand(s):
    out = set()
    for x in s:
        out |= set(UNION.get('ECB' if x == 'EMU' else x, [x]))
        if x in UNION or x == 'EMU': continue
        out.add(x)
    return out

def iso(rows, k='iso3'):
    return expand({r[k] for r in rows if r.get(k)})

cats = {}
# app.js counts a case only if it is not counterparty_only (ccN in app.js): a finding whose
# subject is another body, with this central bank only the counterparty, is listed in the box and
# not counted. Use the same rule or the row claims places the layer renders blank.
_ccc = [r for r in cor['cases'] if not r.get('counterparty_only')]
cats['Corruption cases']        = (iso(_ccc),                    len(_ccc))
# app.js counts a career move only if it is not a public_move (rdN in app.js): a move whose only
# outside employer is the IMF, World Bank or another state body is listed in the box but not counted,
# and insideParts gives such a place no group at all. Use the same rule or the row claims places the
# layer renders blank -- the same mistake the 'other' events and the union-expansion bugs made.
_rdc = [r for r in cor['revolving_door'] if not r.get('public_move')]
cats['Revolving door']          = (iso(_rdc),   len(_rdc))
# app.js counts an event only if its kind is not 'other' (evN in app.js), so the places figure
# must use the same rule or it claims places the layer renders blank.
_evc = [r for r in ev['events'] if r.get('kind') != 'other']
cats['Governor removals and pressure'] = (iso(_evc),            len(ev['events']))
aud = iso(gaps['auditors'], 'cb_iso3') | expand({l['cb_iso3'] for l in net['links'] if 'audit' in l.get('relation','').lower()})
naud = len(gaps['auditors']) + sum(1 for l in net['links'] if 'audit' in l.get('relation','').lower())
cats['External auditors']       = (aud, naud)
pr = [l for l in net['links'] if 'print' in l.get('relation','').lower()]
cats['Banknote printers']       = (expand({l['cb_iso3'] for l in pr}), len(pr))
rm = [l for l in net['links'] if l.get('relation') == 'manages its reserves or programmes']
cats['Outside reserve managers']= (expand({l['cb_iso3'] for l in rm}), len(rm))
gd = [l for l in net['links'] if l.get('relation') == 'holds its gold reserves in custody']
cats['Gold custodians']         = (expand({l['cb_iso3'] for l in gd}), len(gd))
cats['Named shareholders']      = (iso(own['holdings'], 'cb_iso3'), len(own['holdings']))
swl = sw['swaps'] if isinstance(sw, dict) and 'swaps' in sw else sw
sws = set()
for s_ in swl:
    for k in ('provider_iso3','counterparty_iso3','iso3'):
        if s_.get(k): sws.add(s_[k])
# a swap line held by a currency union is held by every member country, as above
cats['Swap lines']              = (expand(sws), len(swl))

# Fourteen of the places can never carry a record: ten have no central bank, and four are
# the currency-union keys whose member countries are counted individually. Report both
# denominators -- the user asked for the reachable one as well as the raw 206.
NOCB = set((gaps.get('no_central_bank') or {}).get('places') or [])
UKEYS = {'ECB', 'BCEAO', 'BEAC', 'ECCB'}
unreachable = (NOCB | UKEYS) & places
R = N - len(unreachable)

print(f"Monetary authorities on the map: {N}")
print(f"Reachable (excluding the {len(NOCB & places)} places with no central bank and the "
      f"{len(UKEYS & places)} currency-union keys): {R}\n")
print(f"{'Category':34} {'Records':>8} {'Places':>7} {'of 206':>7} {'of ' + str(R):>7}")
ROWS = {}
for k, (s, n) in cats.items():
    have = len(s & places) or len(s)
    ROWS[k] = {"records": n, "places": have, "pct206": 100 * have / N, "pct192": 100 * have / R}
    print(f"{k:34} {n:8d} {have:7d} {100*have/N:6.0f}% {100*have/R:6.0f}%")

# ---- the comparison table, in PERCENTAGES ----------------------------------------------------
# The owner asked at round 71 that the comparison carry its diffs as percentages rather than
# record and place counts. Counts answer "how much did we add"; percentages answer "how much
# closer is this", which is the question this map's reporting is for -- and on a depth round the
# two diverge sharply, because the records column can move several per cent while the coverage
# column does not move at all. Both are shown so that divergence is visible rather than hidden.
#
# Records and places are RELATIVE change (a per cent of where the row stood). Coverage is change
# in percentage POINTS, because a percentage of a percentage is unreadable: a row going from 91%
# to 92% has gained 1.1% of its own level and 1.0 point of the subject, and the point is the one
# that means anything to a reader.
#
#   python3 agents/work/coverage.py --snapshot agents/work/baselines/r71.json
#   python3 agents/work/coverage.py --since    agents/work/baselines/r71.json
if "--snapshot" in sys.argv:
    _out = sys.argv[sys.argv.index("--snapshot") + 1]
    os.makedirs(os.path.dirname(_out), exist_ok=True)
    json.dump(ROWS, open(_out, "w"), indent=1)
    print(f"\nsnapshot of these rows written to {_out}")

if "--since" in sys.argv:
    _base = sys.argv[sys.argv.index("--since") + 1]
    _b = json.load(open(_base))
    _lbl = os.path.basename(_base).replace(".json", "")
    def _pc(now, was):
        if not was:
            return "     new" if now else "       -"
        d = 100.0 * (now - was) / was
        return f"{d:+7.1f}%" if d else "    0.0%"
    print(f"\nChange since {_lbl}, as percentages")
    print(f"{'Category':34} {'Records':>9} {'Places':>9} {'of 192':>9}   level now")
    for k, v in ROWS.items():
        w = _b.get(k)
        if not w:
            print(f"{k:34} {'new row':>9}")
            continue
        pp = v["pct192"] - w["pct192"]
        pps = f"{pp:+7.1f}pp" if abs(pp) >= 0.05 else "   0.0pp"
        print(f"{k:34} {_pc(v['records'], w['records']):>9} "
              f"{_pc(v['places'], w['places']):>9} {pps:>9}   {v['pct192']:.0f}% of 192")
    _r = sum(x["records"] for x in ROWS.values())
    _rw = sum(_b[k]["records"] for k in ROWS if k in _b)
    print(f"{'ALL ROWS TOGETHER':34} {_pc(_r, _rw):>9}")

# THE CASES ROW HAS TWO HONEST PLACE FIGURES AND THEY DIFFER BY 19. The row above counts a
# place that holds a case record. app.js colours a place only if ccN > 0, and ccN also drops the
# cleared outcomes on CC_OUT -- acquitted, case dismissed, charge withdrawn, investigation closed,
# conviction annulled. So 19 places hold nothing but cleared cases and render BLANK on the layer
# while the row above counts them, eight of those being ECCB members sharing one dismissed case.
# Found at round 63 by check_about.py disagreeing with this script. Both are printed because both
# are true of different claims -- "has a documented case" and "is coloured on the case layer" --
# and burying either one is how the 'other' events and public_move mismatches survived for rounds.
CC_OUT = {'acquitted', 'case dismissed', 'charge withdrawn', 'investigation closed',
          'conviction annulled (time-barred)'}
# build_final.py applies gaps.json's `case_updates` to the statuses before the page is written, so
# corruption.json's own status can be stale: Kyrgyzstan and Romania both read 'charged' in the data
# file and 'acquitted' / 'conviction annulled (time-barred)' on the map. Any figure here that turns
# on a status has to apply the same updates or it describes a map nobody is looking at. Found at
# round 63, when this script and check_about.py disagreed by two places and the page was right.
_cc_upd = [dict(c) for c in cor['cases']]
for _u in (gaps.get('case_updates') or []):
    _m = (_u.get('match') or '').split('/')[0].split(' (')[0].strip().lower()
    if not _m:
        continue
    for _c in _cc_upd:
        if _m in (_c.get('people') or '').lower() or _m in (_c.get('summary') or '').lower():
            if _u.get('status'):
                _c['status'] = _u['status']
            break
_cc_live = [r for r in _cc_upd
            if not r.get('counterparty_only') and (r.get('status') or '') not in CC_OUT]
_p_rec, _p_live = cats['Corruption cases'][0] & places, iso(_cc_live) & places
print(f"\nCorruption cases, the two place figures:")
print(f"  {len(_p_rec)} places hold a case record = {100*len(_p_rec)/N:.0f}% of {N}, "
      f"{100*len(_p_rec)/R:.0f}% of {R}")
print(f"  {len(_p_live)} of those are coloured on the case layer = {100*len(_p_live)/N:.0f}% of {N}, "
      f"{100*len(_p_live)/R:.0f}% of {R}")
print(f"  the other {len(_p_rec - _p_live)} hold only cleared cases (acquitted, dismissed, "
      f"withdrawn, closed): {' '.join(sorted(_p_rec - _p_live))}")

# A bank with no gold cannot have a gold custodian, so this row's real denominator is the
# places that hold any gold at all, not every place on the map. Settled at round 52.
# A bank with no gold cannot have a gold custodian. The World Gold Council lists 122 places,
# but 14 of them at zero tonnes, so the denominator that matches the sentence "places that hold
# any gold at all" is the 108 with a holding above zero. Round 52 used 122 and so understated
# this row; both are printed here so the figure in about.html can be checked against either.
LISTED = expand({r['iso3'] for r in ev['gold']['rows'] if r.get('iso3')}) & places
GOLDP = expand({r['iso3'] for r in ev['gold']['rows'] if r.get('iso3') and r.get('tonnes')}) & places
_gdp = cats['Gold custodians'][0] & places
print(f"\nGold custodians, measured against the banks that hold gold rather than every place:")
print(f"  {len(_gdp & GOLDP)} of the {len(GOLDP)} places with a holding above zero = "
      f"{100*len(_gdp & GOLDP)/len(GOLDP):.0f}%")
print(f"  {len(_gdp & LISTED)} of the {len(LISTED)} places the World Gold Council lists at all "
      f"({len(LISTED - GOLDP)} of them at zero tonnes) = {100*len(_gdp & LISTED)/len(LISTED):.0f}%")
print(f"  {len(_gdp - LISTED)} further places have a custodian but no gold holding of their own "
      f"(the BCEAO members, whose gold is pooled at the union rather than apportioned)")

# ---- DEPTH: how many places hold exactly one record, on the three priority rows ----
# The three rows the owner cares most about are at their breadth ceiling, so the honest measure of
# a round is no longer the place count: it is how many places move off "exactly one". "One findable
# case" is not "one case", which about.html says in its completeness paragraph.
#
# This lives here rather than in a round's own script on purpose. Round 71 derived it separately and
# got three wrong numbers from two reimplementation bugs -- the EMU/ECB key mismatch that expand()
# handles above, and case_updates' `match` field, whose name it guessed. Both are already solved in
# this file. A second implementation of a filter this map has lost three scripts to drift is not a
# cross-check, it is a fourth bug, so the distribution is computed from the same filtered lists the
# table above uses and its "places with a record" column must equal the figures printed above.
def _depth(rows, key='iso3'):
    n = {}
    for r in rows:
        if not r.get(key):
            continue
        for i in expand({r[key]}) & places:
            n[i] = n.get(i, 0) + 1
    return n

print("\nDepth on the three priority rows -- places by how many records they hold")
print(f"  {'Row':<34}{'with':>6}{'one':>6}{'two':>6}{'3+':>5}")
_DEPTH = {}
for _lbl, _rows in (('Corruption cases', _cc_live),
                    ('Revolving door', _rdc),
                    ('Governor removals and pressure', _evc)):
    _n = _depth(_rows)
    _DEPTH[_lbl] = _n
    _w = [k for k, v in _n.items() if v]
    print(f"  {_lbl:<34}{len(_w):>6}{sum(1 for k in _w if _n[k]==1):>6}"
          f"{sum(1 for k in _w if _n[k]==2):>6}{sum(1 for k in _w if _n[k]>=3):>5}")
_DEPTH_SNAP = {}
for _lbl, _n in _DEPTH.items():
    _w = [k for k, v in _n.items() if v]
    _DEPTH_SNAP[_lbl] = {"with": len(_w), "one": sum(1 for k in _w if _n[k] == 1),
                         "two": sum(1 for k in _w if _n[k] == 2),
                         "three_plus": sum(1 for k in _w if _n[k] >= 3)}

# The depth figures go in the snapshot too, and their diff is the one that matters on a depth
# round: "places holding exactly one record" is the number that moves while every published
# coverage percentage stands still. A FALL here is the good direction, so the sign is flipped in
# the label rather than in the arithmetic -- a reader seeing "-12.3%" against "exactly one" should
# read it as progress, and the column header says so.
if "--snapshot" in sys.argv:
    _out = sys.argv[sys.argv.index("--snapshot") + 1]
    _prev = json.load(open(_out))
    _prev["_depth"] = _DEPTH_SNAP
    json.dump(_prev, open(_out, "w"), indent=1)

if "--since" in sys.argv:
    _bd = json.load(open(sys.argv[sys.argv.index("--since") + 1])).get("_depth") or {}
    if _bd:
        print("\n  Depth, change as percentages (a FALL in 'exactly one' is progress)")
        print(f"  {'Row':34}{'exactly one':>14}{'two':>10}{'three+':>10}")
        for _lbl, _v in _DEPTH_SNAP.items():
            _w = _bd.get(_lbl)
            if not _w:
                continue
            def _d(a, b):
                if not b:
                    return "     new" if a else "       -"
                x = 100.0 * (a - b) / b
                return f"{x:+7.1f}%" if abs(x) >= 0.05 else "    0.0%"
            print(f"  {_lbl:34}{_d(_v['one'], _w['one']):>14}"
                  f"{_d(_v['two'], _w['two']):>10}{_d(_v['three_plus'], _w['three_plus']):>10}")

for _lbl, _n in _DEPTH.items():
    _one = sorted(k for k, v in _n.items() if v == 1)
    print(f"\n  {_lbl} -- {len(_one)} places hold exactly one, so a second record moves them:")
    print("    " + ' '.join(_one))

# ---- per-pattern completeness ----
pat = L('patterns.json')['patterns']
TIER = {
 'independence-law-wave':  ('closed', 'Romelli and Garriga publish the full list of reforms'),
 'banking-crisis-waves':   ('closed', 'Laeven-Valencia publish every episode 1970-2025'),
 'central-bankers-clubs':  ('closed', 'all 63 BIS owner central banks are here, plus the FSB and G30 member lists'),
 'cfa-franc-zone':         ('closed', 'the zone has a fixed membership and all of it is here'),
 'gulf-dollar-pegs':       ('closed', 'the pegged Gulf states are a fixed list and all of them are here'),
 'swap-line-blocs':        ('census', 'Swap lines'),
 'governor-removal-wave':  ('census', 'Governor removals and pressure'),
 'finance-revolving-door': ('census', 'Revolving door'),
 'big-four-auditors':      ('census', 'External auditors'),
 'banknote-printer-bribery':('census','Banknote printers'),
 'weaponized-reserves':    ('examples', ''),
 'anglo-american-axis':    ('examples', ''),
 'city-of-london-offshore':('examples', ''),
 'lebanon-financial-engineering': ('examples', ''),
 'money-routes':           ('examples', ''),
 'pressure-routes':        ('examples', ''),
 'money-meets-pressure':   ('examples', ''),
}
print("\nPatterns behind the scenes\n")
for tier, head in (('closed','Complete — the source publishes the whole list'),
                   ('census','A census this map compiles itself'),
                   ('examples','A structure shown by example — no list exists to be complete against')):
    print(f"  {head}")
    for x in pat:
        t, note = TIER.get(x['id'], ('examples',''))
        if t != tier: continue
        if tier == 'census':
            s, n = cats[note]
            print(f"    {x['title']:52} {len(s & places):3d} places  {100*len(s & places)/N:3.0f}%")
        elif tier == 'closed':
            print(f"    {x['title']:52} {note}")
        else:
            print(f"    {x['title']:52} {len(x.get('countries') or []):3d} countries shown")
    print()

# ---- which places hold no record of each kind ----
# The handoff tells each round to build its target list from here, not from prose.
_nocb = gaps.get('no_central_bank') or {}
NOCB = set(_nocb.get('places') or {}) if isinstance(_nocb, dict) else set(_nocb)
UNION_CODES = set(UNION) | {'EMU'}
print("\nPlaces with no record of this kind")
print("  (union codes and the ten places with no central bank are listed separately)\n")
for k in ('External auditors', 'Banknote printers', 'Gold custodians',
          'Outside reserve managers', 'Governor removals and pressure',
          'Corruption cases', 'Revolving door'):
    s_, _n = cats[k]
    ab = sorted(places - (s_ & places))
    real = [c for c in ab if c not in UNION_CODES and c not in NOCB]
    # THE GOLD ROW NEEDS ITS OWN DENOMINATOR HERE TOO, AND FOR ROUNDS IT DID NOT HAVE IT.
    # A bank with no gold cannot have a gold custodian -- the row's percentage has been measured
    # against the 108 places holding gold above zero since round 52, but its ABSENT list was still
    # computed against all 192 reachable places. So it read "133 to go" when 74 of those hold no
    # gold at all and can never be filled, overstating the row's remaining work by more than
    # double. Round 72 found it by subtracting the negatives from the absent list and getting one
    # country, Palestine, which turns out to be absent from the World Gold Council table entirely.
    # These are separated out the same way the ten places with no central bank already are.
    nogold = []
    if k == 'Gold custodians':
        nogold = [c for c in real if c not in GOLDP]
        real = [c for c in real if c in GOLDP]
    print(f"  {k} — {len(real)} to go")
    print("    " + " ".join(real))
    if nogold:
        print(f"    not targets, hold no gold at all so can hold none in custody ({len(nogold)}): "
              + " ".join(nogold))
    extra = [c for c in ab if c in UNION_CODES or c in NOCB]
    if extra: print("    not targets: " + " ".join(extra))
    print()

_only_other = sorted(iso(ev['events']) - iso(_evc))
if _only_other:
    print("Places holding only uncounted ('other') events, blank on the layer: " + " ".join(_only_other))
    print("  Their events show in the country box but are not counted by app.js or by the row above.\n")

# WHY THIS SECTION EXISTS. The standing check on this map is that coverage.py must not
# claim more places than the score diff moves -- that symptom has caught four counting
# bugs. Round 60 hit it with an innocent cause and nearly spent a round on it. Curacao
# gained a move against its bank, the row went up a place, the layer renders it (the
# layer reads evN directly), and its exposure score did not budge. outsideParts in
# app.js pushes the "Moves against it" component only AFTER it has pushed a law or
# pressure component, and returns early if it has neither -- so for a place in neither
# the Romelli nor the Garriga dataset, and with no Dreher pressure figure, an event
# cannot reach the score at all. The places below are the ones where that holds. A
# place listed here moving no score is expected; any OTHER place failing to move is a
# bug worth chasing.
def _built_places():
    """D.P out of the built page, or {} if it has not been built yet."""
    import re as _re
    for f in ('dist/central_bank_independence.html',
              os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                           'dist', 'central_bank_independence.html')):
        try:
            m = _re.search(r'const D = (\{.*?\});\n', open(f, encoding='utf-8').read(), _re.S)
        except OSError:
            continue
        if m:
            return json.loads(m.group(1)).get('P', {})
    return {}


_BP = _built_places()
_no_outside = sorted(i for i in iso(_evc)
                     if i in _BP and not (_BP[i].get('r') or _BP[i].get('g') or _BP[i].get('p')))
if _no_outside:
    print("Places with a counted move whose score cannot move: " + " ".join(_no_outside))
    print("  No independence index and no pressure figure, so app.js gives them no")
    print("  outside-influence group and the event reaches no score. They still render")
    print("  on the layer and still count in the row above.\n")
