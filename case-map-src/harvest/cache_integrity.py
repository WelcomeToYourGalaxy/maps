#!/usr/bin/env python3
"""Check every harvested file actually belongs to the project it is filed under.

Round 31's China writer found that `cache/P106956/ICR_2016-10-20_26901073.txt`
is the Dominican Republic Social Protection Investment Project's completion
report, sitting in a Chinese project's folder, and that a candidate sentence
from it reached that project's brief. A writer who trusted the brief would have
put a Dominican Republic sentence on a Ningbo card.

The same writer found `cache/P117470/RP_2012-12-18_17282165.txt` is 243 bytes:
the "Public Disclosure Authorized" watermark layer and no body, and it was the
only document that brief listed.

Two checks, both content-based:

* country mismatch — the Bank's documents name their country on the cover and in
  the title line. A file whose opening names a different country, and does not
  name the lead's own country anywhere in its first pages, is flagged.
* near-empty — a text extraction under 1,200 bytes carries no body.

A P-number appearing in a file's URL is NOT used as evidence: the handoff
records that the Bank's archive builds URLs whose path segments carry a
different project's number, which is why dedupe_leads.py reports URL-only hits
separately.
"""
import json, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')

COUNTRIES = [
 'Afghanistan','Albania','Algeria','Angola','Argentina','Armenia','Azerbaijan',
 'Bangladesh','Belize','Benin','Bhutan','Bolivia','Bosnia','Botswana','Brazil',
 'Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Cape Verde',
 'Cabo Verde','Central African Republic','Chad','Chile','China','Colombia',
 'Comoros','Costa Rica','Croatia','Djibouti','Dominican Republic','Ecuador',
 'Egypt','El Salvador','Eritrea','Ethiopia','Gabon','Gambia','Georgia','Ghana',
 'Guatemala','Guinea-Bissau','Guinea','Guyana','Haiti','Honduras','India',
 'Indonesia','Iran','Iraq','Jamaica','Jordan','Kazakhstan','Kenya','Kiribati',
 'Kosovo','Kyrgyz','Lao','Lebanon','Lesotho','Liberia','Libya','Macedonia',
 'Madagascar','Malawi','Maldives','Mali','Mauritania','Mauritius','Mexico',
 'Moldova','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia',
 'Nepal','Nicaragua','Niger','Nigeria','Pakistan','Panama','Papua New Guinea',
 'Paraguay','Peru','Philippines','Poland','Romania','Rwanda','Senegal','Serbia',
 'Sierra Leone','Solomon Islands','Somalia','South Africa','South Sudan',
 'Sri Lanka','Sudan','Swaziland','Tajikistan','Tanzania','Thailand',
 'Timor-Leste','Togo','Tunisia','Turkey','Turkiye','Uganda','Ukraine',
 'Uruguay','Uzbekistan','Vanuatu','Vietnam','Viet Nam','West Bank','Yemen',
 'Zambia','Zimbabwe',"Cote d'Ivoire",'Côte d’Ivoire','Congo','Botswana','Bolivia',
]
ALIAS = {'Viet Nam': 'Vietnam', 'Turkiye': 'Turkey', 'Cabo Verde': 'Cape Verde',
         'Côte d’Ivoire': "Cote d'Ivoire", 'Kyrgyz': 'Kyrgyzstan',
         'Lao': 'Laos', 'Macedonia': 'North Macedonia'}


def canon(c):
    return ALIAS.get(c, c)


def main():
    M = json.load(open(os.path.join(HERE, 'harvest_manifest.json')))
    R = json.load(open(os.path.join(HERE, 'resolved.json')))
    lead_country = {}
    for r in R:
        if 'pid' in r:
            cs = [canon(c) for c in r.get('countries', [])]
            lead_country.setdefault(r['pid'], cs)
            for s in r.get('sibling_pids', []):
                lead_country.setdefault(s, cs)

    wrong, empty, unchecked = [], [], []
    n = 0
    for pid in sorted(M):
        want = set(lead_country.get(pid, []))
        for d in M[pid].get('docs', []):
            p = d.get('path')
            if not p or not p.endswith('.txt'):
                continue
            full = os.path.join(HERE, p)
            if not os.path.exists(full):
                continue
            n += 1
            size = os.path.getsize(full)
            if size < 1200:
                empty.append({'pid': pid, 'path': p, 'bytes': size,
                              'tag': d.get('tag'), 'title': d.get('title', '')[:90]})
                continue
            if not want:
                unchecked.append(p)
                continue
            head = open(full, encoding='utf-8', errors='replace').read(6000)
            named = {canon(c) for c in COUNTRIES if re.search(r'\b' + re.escape(c) + r'\b', head, re.I)}
            if named and not (named & want):
                wrong.append({'pid': pid, 'path': p, 'tag': d.get('tag'),
                              'expected': sorted(want), 'found': sorted(named),
                              'title': d.get('title', '')[:100],
                              'first_line': head.strip().split('\n')[0][:90]})

    print(f"checked {n} text files across {len(M)} project folders\n", file=sys.stderr)
    print(f"WRONG PROJECT (no expected country named, another country named): {len(wrong)}",
          file=sys.stderr)
    for w in wrong:
        print(f"  {w['path']}", file=sys.stderr)
        print(f"     tag={w['tag']} expected={w['expected']} found={w['found']}", file=sys.stderr)
        print(f"     title={w['title']!r}", file=sys.stderr)
    print(f"\nNEAR-EMPTY (<1200 bytes, no body): {len(empty)}", file=sys.stderr)
    for e in empty:
        print(f"  {e['path']} {e['bytes']}b {e['tag']} {e['title']!r}", file=sys.stderr)
    print(f"\nnot checked (no country on the lead): {len(unchecked)}", file=sys.stderr)

    json.dump({'wrong_project': wrong, 'near_empty': empty,
               'unchecked': unchecked, 'files_checked': n},
              open(os.path.join(HERE, 'cache_integrity.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
