#!/usr/bin/env python3
"""Check writeup drafts against the box text they were written from.
Flags numbers and capitalised words that appear in a draft but not its source box,
which is how model knowledge leaks past the no-fabrication rule.
Usage: check_drafts.py <drafts.json> <boxes.json>"""
import json, re, sys, unicodedata
drafts = json.load(open(sys.argv[1])); boxes = json.load(open(sys.argv[2]))
_MAP = str.maketrans({'đ': 'dj', 'Đ': 'Dj', 'ø': 'o', 'Ø': 'O', 'ł': 'l', 'Ł': 'L',
                      'ı': 'i', 'ß': 'ss', 'æ': 'ae', 'œ': 'oe', 'Æ': 'Ae', 'Œ': 'Oe'})
def norm(s):
    # NFKD leaves stroked and ligature letters intact, so map them first
    return unicodedata.normalize('NFKD', s.translate(_MAP)).encode('ascii', 'ignore').decode().lower()
STOP = set("""The It Its His Her Their In From No A An That This He She They After Before When Both
One Two Three Four Five Six Seven Eight Nine Ten Chairman Governor Deputy President Bank Central
Board Director Managing Vice Group Limited Company Corporation Inc Ltd And But Neither Either
Afterwards Moving Apart Several Where While Although Under Since Until During""".split())
BANNED = ['the box', 'the record', 'does not say', 'on the map', ' our ', 'excerpt']
bad = {}
for k, t in drafts.items():
    src = boxes.get(k, '')
    if not src:
        bad[k] = ['NO SOURCE BOX']; continue
    n = norm(src); probs = []
    for num in set(re.findall(r'\b\d[\d,.]*\b', t)):
        if num.replace(',', '') not in src.replace(',', '') and num not in src:
            probs.append('number ' + num)
    # strip possessives, and ignore words that only ever start a sentence
    sent_start = set(re.findall(r'(?:^|[.!?]\s+)([A-Z][a-zA-Z\'-]{2,})', t))
    for w in set(re.findall(r'\b[A-Z][a-zA-Z\'-]{2,}\b', t)):
        base = w[:-2] if w.endswith("'s") else w
        if base in STOP: continue
        if norm(base) in n: continue
        # an adjective form of something in the box (Estonian <- Estonia)
        if len(base) > 4 and norm(base[:-2]) in n: continue
        if w in sent_start and norm(base) not in n and base.lower() in (
            'taking who nothing those almost many being auditing moving afterwards apart several'
            ' neither governments').split(): continue
        probs.append('name ' + w)
    for b in BANNED:
        if b in t.lower(): probs.append('phrase ' + b.strip())
    if probs: bad[k] = sorted(probs)
print(f'{len(bad)} of {len(drafts)} drafts flagged')
for k, v in sorted(bad.items()):
    print(' ', k, '->', v[:10])
sys.exit(1 if bad else 0)
