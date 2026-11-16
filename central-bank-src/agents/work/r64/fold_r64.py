#!/usr/bin/env python3
"""Round 64: fold "Citibank, N.A." into Citi, and country-qualify Paraguay's Banco Union.

Both were flagged in the round-63 handoff and in dup_parties.py's own output.

1. CITI. The map drew Citi with ten ties and "Citibank, N.A." with one -- the 42.8 per cent
   shareholding in the Federal Reserve Bank of New York -- so a reader comparing concentration
   between firms read a split count, which is the thing round 60 was spent removing. "Citibank"
   already folded to "Citi" in node(); the string with ", N.A." did not. Same group, same city,
   wholly-owned subsidiary, and the source's own wording is kept in name_as_stated, so this is
   the PIMCO/State Street case and not the UBS (UK) case, where folding would have moved a
   marker to another country. The Citi paragraph is rewritten because the node gains a tie its
   paragraph did not describe, and the orphaned paragraph is archived rather than deleted.

2. BANCO UNION. Two different banks in two different countries: Paraguay's failed Banco Union,
   named in a case, and Bolivia's Banco Union S.A., named in a career move. The Bolivian node is
   already country-qualified; the Paraguayan one was not, which is the reverse of the duplicate
   bug -- a name unique only inside its own country, waiting to merge with the next record that
   spells it the same way. It gets the treatment "National Bank (Sudan)" got.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
L = lambda n: json.load(open(os.path.join(A, n), encoding='utf-8'))
W = lambda n, d: json.dump(d, open(os.path.join(A, n), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
dry = '--dry' in sys.argv

# --- 1. the alias, in build_net.py's own fold map -------------------------------------------
bn = os.path.join(A, '..', 'build_net.py')
s = open(bn, encoding='utf-8').read()
old, new = '"Citibank": "Citi",', '"Citibank": "Citi", "Citibank, N.A.": "Citi",'
assert s.count(old) == 1, f'anchor appears {s.count(old)} times'
assert '"Citibank, N.A.": "Citi"' not in s, 'alias already present'
print('build_net.py: adding "Citibank, N.A." -> "Citi"')

# --- 2. the rename, in parties.json --------------------------------------------------------
par = L('parties.json')
hits = [l for l in par['links'] if l.get('party') == 'Banco Union']
assert len(hits) == 1, f'expected 1 Banco Union link, found {len(hits)}'
assert hits[0].get('cb_iso3') == 'PRY', 'the Banco Union link is not the Paraguayan one'
print(f"parties.json: renaming 'Banco Union' -> 'Banco Unión (Paraguay)' "
      f"(name_as_stated stays {hits[0].get('name_as_stated')!r})")
for l in hits:
    l['party'] = 'Banco Unión (Paraguay)'

# --- 3. the writeups ------------------------------------------------------------------------
wr = L('writeups.json')
assert 'n:Citibank, N.A.' in wr and 'n:Citi' in wr and 'n:Banco Union' in wr

CITI = (
 "Citi is a bank in New York with ties to several central banks and the Group of Thirty, and it "
 "also owns part of one. Citibank, N.A., the group's national banking association, held "
 "87,900,000 shares, 42.8 per cent, of the Federal Reserve Bank of New York as of 31 December "
 "2018. At the Federal Reserve, the member banks that hold a Reserve Bank's shares elect six of "
 "its nine directors, and since 2010 the bankers' three Class A directors no longer vote on "
 "choosing its president. On the career side, Catherine L Mann came from Global Chief Economist "
 "at Citibank to the Bank of England's Monetary Policy Committee, Michael Saunders from UK "
 "economist at Citigroup, and Mervyn King went from Bank of England Governor to senior adviser "
 "at Citigroup. The source says it paid former Federal Reserve chair Janet Yellen for speeches, "
 "and Stanley Fischer, Governor of the Bank of Israel from 2005 to 2013, had been a Citigroup "
 "vice chairman. Jane Fraser, Citi's Chair of the Board and CEO, represents it in the Group of "
 "Thirty, where central bankers also sit.")

arch_path = os.path.join(A, 'work', 'r64', 'orphaned_writeups.json')
arch = {'n:Citibank, N.A.': wr['n:Citibank, N.A.'],
        'note': 'Folded into n:Citi at round 64; its facts are carried in the Citi paragraph. '
                'Archived rather than deleted, as round 60 did for 28 folded spellings.'}
print("writeups.json: rewriting n:Citi to carry the shareholding; archiving n:Citibank, N.A.")
print(f"writeups.json: migrating 'n:Banco Union' -> 'n:Banco Unión (Paraguay)'")

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)

open(bn, 'w', encoding='utf-8').write(s.replace(old, new, 1))
W('parties.json', par)
wr['n:Citi'] = CITI
del wr['n:Citibank, N.A.']
wr['n:Banco Unión (Paraguay)'] = wr.pop('n:Banco Union')
W('writeups.json', wr)
json.dump(arch, open(arch_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'\nwritten. writeups.json now holds {len(wr)} paragraphs; '
      f'orphan archived in agents/work/r64/orphaned_writeups.json')
