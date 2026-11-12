#!/usr/bin/env python3
"""Coverage figures for the central bank capture map.
Breadth = share of monetary authorities on the map holding at least one record
of that kind. Computed exactly from the data files. Depth estimates live in
about.html and are a judgement, not a computation."""
import json, sys, os
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
cats['Corruption cases']        = (iso(cor['cases']),            len(cor['cases']))
cats['Revolving door']          = (iso(cor['revolving_door']),   len(cor['revolving_door']))
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

print(f"Monetary authorities on the map: {N}\n")
print(f"{'Category':34} {'Records':>8} {'Places':>7} {'Breadth':>8}")
for k, (s, n) in cats.items():
    print(f"{k:34} {n:8d} {len(s & places) or len(s):7d} {100*len(s & places)/N if (s & places) else 100*len(s)/N:7.0f}%")

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
    print(f"  {k} — {len(real)} to go")
    print("    " + " ".join(real))
    extra = [c for c in ab if c in UNION_CODES or c in NOCB]
    if extra: print("    not targets: " + " ".join(extra))
    print()

_only_other = sorted(iso(ev['events']) - iso(_evc))
if _only_other:
    print("Places holding only uncounted ('other') events, blank on the layer: " + " ".join(_only_other))
    print("  Their events show in the country box but are not counted by app.js or by the row above.\n")
