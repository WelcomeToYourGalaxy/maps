#!/usr/bin/env python3
"""Normalise and pre-validate agent output before merge_links.py sees it. (round 65)

With six agents in a round, the same handful of shape faults arrive again and again and each one
costs a merge run to discover. This fixes the mechanical ones and REPORTS the ones that need a
decision, so a big round is processed in one pass instead of six.

Mechanical, fixed here:
  - `people` or any other scalar field written as a list -> joined into one string
  - a tie record's `relation` or a career record's `role` given with odd case or spacing
  - whitespace collapsed in long text fields

Needs a decision, reported not fixed:
  - a relation or role outside the vocabulary (a new one needs a SAY entry in app.js and a REL
    entry in build_net.py, so it is a decision, not an agent's phrasing)
  - a record keyed to a currency union
  - a summary or detail under 90 characters
  - a party named as the central bank itself, which would draw a diamond for the bank
  - a brief instruction printed as prose, which check_drafts.py cannot see because it comes from
    the brief and not from the box

Usage: python3 normalise_agent_output.py <file.json> [...]   -- writes <file>.norm.json
"""
import json, re, sys, os

ROLES = {"owns shares", "bribery or misconduct with the bank", "paid or bribed the bank's officials",
         "received leaked information", "received money, favors or contracts from the bank",
         "member and shareholder of the bis", "member of the financial stability board",
         "member of the same forum", "represented in the group of thirty",
         "paid a former official for speeches or advice",
         "employed an official before or after (revolving door)", "sits on the board",
         "appoints or directs the bank's board", "audited or investigated", "named in the case",
         "named in the event", "pressured, dismissed or prosecuted bank officials",
         "froze or seized the bank's reserves",
         "guarantees the currency under a cooperation agreement", "audits its accounts",
         "manages its reserves or programmes", "manages its sovereign wealth fund",
         "holds its gold reserves in custody",
         "owned or ran an asset officials held", "prints its banknotes", "makes its banknote paper",
         "prints some of its banknotes",
         "supplies its banknote substrate", "directs the bank's management of a state fund", "other"}
UNION = {"ECB", "EMU", "BCEAO", "BEAC", "ECCB"}
# entity_type has its own small closed vocabulary and agents reach for synonyms every round --
# "asset manager", "multilateral institution", "commercial bank". merge_links refuses the record
# and the whole batch has to be re-run, so the common synonyms are mapped here. (round 65)
ETYPE = {'firm', 'state body', 'forum', 'state printing works', 'international body', 'person',
         'state works', "central bank's own vault", "central bank's own works", 'central bank',
         'central bank subsidiary', 'bank', 'state mint', 'agency', 'government', 'court',
         'company', 'other'}
# A network tie (a record with a 'relation') carries its head office as entity_hq_city /
# entity_hq_iso3. Written as hq_city / hq_iso3 the build silently ignores them, and the marker
# lands on the firm's fallback head office or nowhere at all. Round 66 found 14 ties like that.
TIE_HQ = {"hq_city": "entity_hq_city", "hq_iso3": "entity_hq_iso3"}
def fix_tie_hq(r, notes):
    if not r.get("relation"):
        return
    for a, b in TIE_HQ.items():
        if a in r:
            v = r.pop(a)
            if v is not None and not r.get(b):
                r[b] = v
            notes.append("renamed %s to %s" % (a, b))

ETYPE_ALIAS = {
 'asset manager': 'firm', 'fund manager': 'firm', 'investment manager': 'firm',
 'asset management firm': 'firm', 'insurer': 'firm', 'insurance company': 'firm',
 'auditor': 'firm', 'audit firm': 'firm', 'accounting firm': 'firm', 'printer': 'firm',
 'multilateral institution': 'international body', 'multilateral': 'international body',
 'international organisation': 'international body', 'international organization': 'international body',
 'development bank': 'international body', 'commercial bank': 'bank', 'private bank': 'bank',
 'state-owned bank': 'bank', 'ministry': 'government', 'legislature': 'government',
 'parliament': 'government', 'regulator': 'agency', 'supreme audit institution': 'agency',
 'audit office': 'agency', 'prosecutor': 'agency', 'individual': 'person',
 'sovereign wealth fund': 'state body', 'pension fund': 'state body', 'state agency': 'state body',
}
SCALARS = ('iso3', 'country', 'central_bank', 'people', 'move', 'summary', 'detail', 'status',
           'kind', 'entity', 'relation', 'source_url', 'source_title', 'quote', 'years',
           'name_as_stated', 'entity_type', 'hq_city', 'hq_iso3', 'cb_iso3', 'category')
LEAK = re.compile(r'not an accusation|not wrongdoing|not an allegation of|is not evidence'
                  r'|does not imply|which is not to say|this does not mean', re.I)
# Comparing a party name against a pattern like "^bank of" flags every commercial bank in the
# world -- the first draft of this check called Banco de Cochabamba and the National Bank of Sudan
# central banks. A check that cries wolf gets ignored, so it compares against the ACTUAL central
# bank name for that country, from cbnames.py, folded. (round 65)
_here = os.path.dirname(os.path.abspath(__file__))
_ns = {}
exec(open(os.path.join(_here, '..', '..', 'cbnames.py'), encoding='utf-8').read(), _ns)
CB_NAME = _ns.get('CB', {})
_fold = lambda x: re.sub(r'[^a-z0-9]+', '', (x or '').lower())

def is_the_central_bank(party, iso):
    want = _fold(CB_NAME.get(iso or '', ''))
    got = _fold(party)
    return bool(want) and bool(got) and (want == got or want in got or got in want)

def main(paths):
    for path in paths:
        d = json.load(open(path, encoding='utf-8'))
        recs = d.get('records') or []
        fixed, flags = 0, []
        for i, r in enumerate(recs):
            tag = f"{r.get('iso3','???')}[{i}]"
            _n = []
            fix_tie_hq(r, _n)
            if _n:
                fixed += len(_n)
            for k in SCALARS:
                v = r.get(k)
                if isinstance(v, list):
                    r[k] = '; '.join(str(x) for x in v); fixed += 1
                elif isinstance(v, str) and '  ' in v:
                    r[k] = re.sub(r'\s+', ' ', v).strip(); fixed += 1
            for holder in [r] + list(r.get('parties') or []):
                et = holder.get('entity_type') or holder.get('party_type')
                if isinstance(et, str):
                    low = re.sub(r'\s+', ' ', et).strip().lower()
                    low = ETYPE_ALIAS.get(low, low)
                    key = 'entity_type' if 'entity_type' in holder else 'party_type'
                    if low != holder.get(key):
                        holder[key] = low; fixed += 1
                    if low not in ETYPE:
                        flags.append(f'{tag} {key}={low!r} is OUTSIDE THE VOCABULARY; the closed '
                                     f'list is {sorted(ETYPE)}')
            for k in ('role', 'relation'):
                if isinstance(r.get(k), str):
                    low = re.sub(r'\s+', ' ', r[k]).strip().lower()
                    if low != r[k]: r[k] = low; fixed += 1
                    if low not in ROLES:
                        flags.append(f'{tag} {k}={low!r} is OUTSIDE THE VOCABULARY -- a new one '
                                     'needs a SAY entry in app.js and a REL entry in build_net.py, '
                                     'so it is a decision')
            for p in (r.get('parties') or []):
                if isinstance(p.get('role'), str):
                    low = re.sub(r'\s+', ' ', p['role']).strip().lower()
                    if low != p['role']: p['role'] = low; fixed += 1
                    if low not in ROLES:
                        flags.append(f'{tag} party role {low!r} is OUTSIDE THE VOCABULARY')
                if is_the_central_bank(p.get('party'), r.get('iso3')):
                    flags.append(f"{tag} party {p.get('party')!r} IS THE CENTRAL BANK ITSELF -- "
                                 'a party node is an OUTSIDE party, and a diamond for the bank '
                                 'would read as an outside tie; drop it')
            if (r.get('iso3') or '') in UNION or (r.get('cb_iso3') or '') in UNION:
                flags.append(f'{tag} is keyed to a CURRENCY UNION -- it would expand to every '
                             'member and put a false record in eight to twenty boxes')
            for k in ('summary', 'detail'):
                if r.get(k) is not None and len(str(r[k])) < 90:
                    flags.append(f'{tag} {k} is {len(str(r[k]))} characters; it renders as a '
                                 'standalone sentence in a popup and must be at least 90')
            blob = ' '.join(str(r.get(k) or '') for k in ('summary', 'detail'))
            for m in LEAK.finditer(blob):
                flags.append(f'{tag} prints a rule from the brief as prose: '
                             f'...{blob[max(0,m.start()-60):m.end()+30]}...')
        out = path.replace('.json', '') + '.norm.json'
        json.dump(d, open(out, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
        print(f'{os.path.basename(path)}: {len(recs)} records, {fixed} mechanical fixes -> '
              f'{os.path.basename(out)}')
        for f in flags: print('    FLAG ' + f)

main(sys.argv[1:])
