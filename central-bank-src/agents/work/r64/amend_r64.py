#!/usr/bin/env python3
"""Round 64: write this round's ownership findings into the two held career records themselves.

Neither converts, but the evidence moved, and a working file is the wrong place to keep that --
three scripts and two held-record files have already been lost with their sessions. Each edit is
keyed on (iso3, a token that must appear in that record) and the script writes nothing unless the
key matches exactly one record and the fragment appears exactly once in it.

SDN: round 64 DID find the employer's own ownership statement, which earlier rounds could not --
and found that it contradicts the dates. The National Bank of Sudan says it was established in
1981; the central bank's page puts Nimir as its general manager from 1980. A bank cannot have
been managed the year before it existed, so either the date is wrong or it is a different
institution of a similar name. That is a different reason for holding the leg than "ownership
unstated", and it tells the next round what to go after.

BOL: the evidence for Banco de Cochabamba is now three sentences in a 1989 United States country
study, none of which says who owned the bank -- it is placed among the top five banks, commercial
banks are called the core of the private financial sector, and it is absent from the enumerated
public-sector list. Absence from a list is not an ownership statement, and the CV gives no dates
for the post, so even a correct 1988 snapshot need not cover his tenure.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'corruption.json')
cor = json.load(open(P, encoding='utf-8'))
rd = cor['revolving_door']
dry = '--dry' in sys.argv

SDN_OLD = ("Neither employer's ownership is stated on that page, and nothing found this round "
           "states who owned either bank in those years; Sudan nationalised its banks in 1970 and "
           "reversed course in stages afterwards, so the years matter and these two legs are not "
           "settled either way.")
SDN_NEW = ("The National Bank of Sudan does state its own ownership, on its own site: it says it "
           "was established in 1981 as an initiative by a group of national Sudanese businessmen, "
           "and that in July 2006 the Lebanese Bank Audi acquired 75 per cent of its shares. That "
           "does not settle this leg, because it contradicts the dates. The bank gives its own "
           "founding year as 1981, while the central bank's page puts Nimir as its general manager "
           "from 1980, so either that date is wrong or the bank he ran was a different institution "
           "of a similar name. Nothing found states who owned the Workers National Bank in "
           "1989-1992 either. Sudan nationalised its banks in 1970 and reversed course in stages "
           "afterwards, so the years decide both legs and neither is settled.")

BOL_OLD = "The ownership of one of the three is now stated, and it points the other way:"
BOL_NEW = "The ownership of one of the three is stated, and it points the other way:"
BOL_EXTRA = (
    " On the second of the three, a 1989 United States country study on Bolivia places the Bank of "
    "Cochabamba among the country's top five banks, holding 61 per cent of deposits at the end of "
    "1988, says commercial banks were the core of the private financial sector, and lists the "
    "public-sector institutions without naming it. None of those sentences says who owned the "
    "bank, and the central bank's CV gives no dates for the post, so a 1988 snapshot need not "
    "cover the years he was there.")

EDITS = [('SDN', 'General Manager, Workers National Bank, 1989 - 1992', SDN_OLD, SDN_NEW),
         ('BOL', 'Compania Boliviana de Seguros S.A.', BOL_OLD, BOL_NEW)]

def one(iso, token):
    hits = [i for i, r in enumerate(rd)
            if r.get('iso3') == iso and token in json.dumps(r, ensure_ascii=False)]
    assert len(hits) == 1, f'{iso} / {token!r}: matched {len(hits)} records, expected 1'
    return hits[0]

for iso, token, old, new in EDITS:
    i = one(iso, token)
    t = rd[i]['summary']
    assert t.count(old) == 1, f'{iso}[{i}]: fragment appears {t.count(old)} times, expected 1'
    j = t.index(old)
    print(f'{iso}[{i}] ...{t[max(0,j-50):j+len(old)+120]!r}...\n')
    rd[i]['summary'] = t.replace(old, new)

i = one('BOL', 'Compania Boliviana de Seguros S.A.')
assert rd[i]['summary'].rstrip().endswith('.'), 'BOL summary does not end on a full stop'
rd[i]['summary'] = rd[i]['summary'].rstrip() + BOL_EXTRA
print(f'BOL[{i}] appended {len(BOL_EXTRA.split())} words')

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(cor, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('\nwritten: corruption.json')
