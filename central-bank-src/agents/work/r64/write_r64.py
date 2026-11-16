#!/usr/bin/env python3
"""Round 64: Eritrea's country paragraph and the three new party paragraphs.

The country paragraph is edited rather than replaced: the new material is inserted and the two
figures the record moved (exposure 52 -> 56, percentile 97% -> 99%, outside influence 19 -> 26)
are corrected in place. rep() asserts the old string appears exactly once AND prints what
follows it, because a replacement on text that was truncated once left a stranded tail that
survived a build, an audit and a push.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'writeups.json')
w = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

def rep(key, old, new):
    t = w[key]
    n = t.count(old)
    assert n == 1, f'{key}: old string appears {n} times, expected 1: {old[:60]!r}'
    i = t.index(old)
    print(f'  {key}: ...{t[max(0,i-60):i+len(old)+140]!r}...')
    w[key] = t.replace(old, new)

print('EDITS to p:ERI')
rep('p:ERI', 'scores 52 of 100 on exposure', 'scores 56 of 100 on exposure')
rep('p:ERI', 'rank 7 of 194, more exposed than 97% of the 194',
            'rank 2 of 194, more exposed than 99% of the 194')
rep('p:ERI', 'Outside influence scores 19 and', 'Outside influence scores 26 and')
rep('p:ERI',
    'No documented case at the central bank was found, which does not prove none happened.',
    'No documented case at the central bank was found, which does not prove none happened. '
    'The law that governs the bank puts its appointments in one person’s hands. Proclamation '
    '93/1997 of 21 January 1997 keeps in being the bank created by Proclamation 32/1993 and gives '
    'the President the appointment of the Governor for a five-year term, with the legislature’s '
    'approval, the appointment of the Deputy Governor, the Governor’s pay on the Board’s '
    'recommendation, the appointment of every nominated Board member, and approval of the fee a '
    'Board member is paid for each meeting attended; a director who resigns writes to the President '
    'and leaves only once the President accepts. The Board also seats a representative of the '
    'Ministry of Finance and the Auditor General. The same law says in Article 6 that the bank is '
    'not subject to instructions from the Government in performing its functions, determining its '
    'budget or setting its procedures, and that the Governor may be relieved only for just cause '
    'after the legislature is consulted, so what the record carries is control of the posts rather '
    'than a power to direct the bank’s decisions.')

NODES = {
 'n:Government of the State of Eritrea':
   'The Government of the State of Eritrea, in Asmara, fills and pays the posts at the Bank of '
   'Eritrea, the country’s central bank. Proclamation 93/1997, the law that governs the bank, '
   'gives the President the appointment of the Governor for a five-year term with the national '
   'legislature’s approval, the appointment of the Deputy Governor, and the setting of the '
   'Governor’s pay on the Board’s recommendation. The names of all nominated Board members '
   'go to the President for appointment, the fee each Board member is paid for a meeting attended '
   'is approved by the President, and a director who wishes to resign writes to the President and '
   'leaves only when the President accepts the resignation. The same law says the bank is not '
   'subject to instructions from the Government over its functions, its budget or its procedures, '
   'and the Governor may be relieved only for just cause after the legislature is consulted. The '
   'arrangement has no end date.',
 'n:Ministry of Finance of Eritrea':
   'The Ministry of Finance of Eritrea, in Asmara, has a seat on the board of the Bank of Eritrea. '
   'Under Article 8 of Proclamation 93/1997 the board is made up of the Governor, the Deputy '
   'Governor, a representative of the Ministry of Finance, the Auditor General and three other '
   'members. The Ministry nominates its own representative, and that representative is one of the '
   'four people who jointly draw up the list of candidates from which the three other members are '
   'chosen. A minister of the government may also be asked to take part in board meetings, without '
   'a vote.',
 'n:Auditor General of Eritrea':
   'The Auditor General of Eritrea sits on the board of the Bank of Eritrea. Article 8 of '
   'Proclamation 93/1997 names the Auditor General as one of the seven board members, alongside '
   'the Governor, the Deputy Governor, a representative of the Ministry of Finance and three '
   'members drawn from commerce, finance, industry or agriculture. The Auditor General is also one '
   'of the four officials who jointly prepare the candidate lists for those three seats. Which firm '
   'or body audits the bank’s own accounts is not recorded on this map: a 1999 United States '
   'government guide says an independent local accounting firm audits it and names no firm.',
}
print('\nNEW node paragraphs')
for k, v in NODES.items():
    assert k not in w, f'{k} already exists -- edit it rather than overwriting'
    print(f'  {k}  ({len(v.split())} words)')
    w[k] = v

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(w, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'\nwritten: writeups.json now holds {len(w)} paragraphs')
