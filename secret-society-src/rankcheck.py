#!/usr/bin/env python3
"""Use `rank` as a ruling-11 detector across the whole map.

    python3 rankcheck.py [--all]

Ruling 11 requires a NAMED BODY. The round-14 handoff observed, without acting
on it, that a record whose description names no body cannot produce a valid
`rank`, because `rank` is the post held inside the body reached -- so `rank` is
a cheap ruling-11 detector over the whole file at once. This is that detector.

THREE SIGNALS WERE TRIED. The first two are recorded because they look right
and are not:

  1. "rank carries no post word" over-flagged by an order of magnitude (963 of
     3,388). "Istanbul public prosecutors" and "CEO of Pemex" both name a body
     perfectly well while matching no fixed vocabulary of post words.
  2. "rank carries no capital letter" cut it to 2, but missed every one of the
     records the handoff had already found by hand -- because their ranks begin
     with a capitalised GENERIC noun: "Investment funds and payment fintechs",
     "Sports clubs and player transfers", "Commodity trader", "Ramp, catering
     and baggage staff". A capital at the start of a field says nothing.

  3. WHAT WORKS: a genuine proper noun recurs capitalised MID-SENTENCE in `d`,
     or is an acronym, or is a place the map itself knows. A capitalised
     generic noun at the start of `rank` does none of those. So: tokenise
     `rank`, and ask whether any token is a confirmed proper noun by that test.

Output, worst first:

  NO-NAMED-BODY - no token of `rank` is a confirmed proper noun, and `d` names
                  no body either. Nothing here for ruling 11 to point at.
  SECTOR-RANK   - no confirmed proper noun in `rank`, but `d` does name a body.
                  Usually it is `rank` that is weak and the record stands --
                  the distinction the handoff drew for the Mone record.

It reports. It removes nothing: the owner has said editorial selection is his.
"""
import json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data')
cases = json.load(open(os.path.join(D, 'cases.json'), encoding='utf-8'))

# The map's own gazetteer: every country and city it uses.
GAZ = set()
for c in cases:
    for k in ('c', 'city'):
        for w in re.findall(r"[A-Z][a-zà-ÿ'’\-]{2,}", str(c.get(k) or '')):
            GAZ.add(w.lower())
for f in ('capitals.json', 'iso3.json'):
    try:
        j = json.load(open(os.path.join(D, f), encoding='utf-8'))
        for k, v in (j.items() if isinstance(j, dict) else []):
            for w in re.findall(r"[A-Z][a-zà-ÿ'’\-]{2,}", str(k) + ' ' + str(v)):
                GAZ.add(w.lower())
    except Exception:
        pass

CAP = re.compile(r"[A-Z][a-zà-ÿ'’\-]{2,}")
ACRONYM = re.compile(r'\b[A-Z]{2,}\b')
BODYNOUN = re.compile(r'(?i)\b(ministry|ministries|department|agency|authority|bureau|'
 r'commission|council|court|tribunal|police|gendarmerie|carabinieri|army|navy|'
 r'military|intelligence|directorate|administration|institute|university|'
 r'hospital|bank|treasury|customs|inspectorate|parliament|congress|senate|'
 r'assembly|legislature|municipality|comune|prefecture|corporation|'
 r'enterprise|port|airport|railway|prison|penitentiary|brigade|regiment|'
 r'guard|secretariat|chamber|service|office|force|corps)\b')

def proper_tokens(s):
    """Tokens of s that are confirmed proper nouns."""
    out = set()
    for w in CAP.findall(str(s or '')):
        out.add(w)
    return out

def confirmed(tok, d):
    """A proper noun recurs capitalised mid-sentence in d, or is a known place."""
    if tok.lower() in GAZ:
        return True
    # mid-sentence means not preceded by start-of-string or sentence punctuation
    return bool(re.search(r'(?<![.!?]\s)(?<!^)(?<![.!?]\s\s)\b' + re.escape(tok) + r'\b', str(d or '')))

def names_body(d):
    d = str(d or '')
    if ACRONYM.search(d):
        return True
    for m in BODYNOUN.finditer(d):
        a, b = max(0, m.start() - 45), m.end() + 45
        seg = d[a:b]
        for tok in CAP.findall(seg):
            if confirmed(tok, d):
                return True
    return False

# A post that implies its own body: "prime minister" needs no "of X" to say
# which premiership. A sector label implies nothing.
IMPLIES_BODY = re.compile(r'(?i)^(?:the\s+)?(?:former\s+|acting\s+|interim\s+|senior\s+|'
 r'deputy\s+|vice[- ]|first\s+|chief\s+)*'
 r'(president|prime minister|state president|head of state|head of government|'
 r'minister|ministre|cabinet minister|secretary of state|chancellor|governor|'
 r'mayor|municipal mayor|premier|chief minister|judge|judges|senior judge|'
 r'justice|magistrate|prosecutor|prosecutors|public prosecutor|'
 r'federal judges|judges and prosecutors|attorney general|'
 r'police officers?|army|soldiers?|generals?|admirals?|officers?)\b')

def main():
    nonamed, implied, sector = [], [], []
    for i, c in enumerate(cases):
        r = str(c.get('rank') or '').strip()
        d = c.get('d') or ''
        toks = proper_tokens(r)
        if ACRONYM.search(r) or any(confirmed(t, d) for t in toks):
            continue
        if names_body(d):
            sector.append((i, c))
        elif IMPLIES_BODY.match(r):
            implied.append((i, c))
        else:
            nonamed.append((i, c))
    print('%d records. rank as a ruling-11 detector:' % len(cases))
    print('  NO-NAMED-BODY %4d  rank names a SECTOR and d names no body -- read these' % len(nonamed))
    print('  POST-IMPLIES  %4d  rank is a post that implies its own body (prime minister)' % len(implied))
    print('  SECTOR-RANK   %4d  rank names a sector, but d names a body' % len(sector))
    showall = '--all' in sys.argv
    for label, rows in (('NO-NAMED-BODY', nonamed), ('POST-IMPLIES', implied), ('SECTOR-RANK', sector)):
        if not rows: continue
        print('\n=== %s (%d) ===' % (label, len(rows)))
        for i, c in (rows if showall else rows[:50]):
            print('  %4d [%s/%s] %-12s %-15s rank=%-38r %s'
                  % (i, c.get('inf'), c.get('bk'), str(c.get('status'))[:12],
                     str(c.get('c'))[:15], str(c.get('rank'))[:38], str(c.get('n'))[:48]))
        if not showall and len(rows) > 50:
            print('  ... %d more (run with --all)' % (len(rows) - 50))
    print('\nNO-NAMED-BODY by cell:',
          collections.Counter('%s/%s' % (c.get('inf'), c.get('bk')) for _, c in nonamed).most_common(10))

main()
