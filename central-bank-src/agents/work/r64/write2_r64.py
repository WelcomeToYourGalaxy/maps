#!/usr/bin/env python3
"""Round 64, second writing pass: the Timor-Leste and North Macedonia paragraphs, and the two
new party paragraphs. rep() asserts the fragment appears exactly once and prints what follows it.
Figures are left exactly as check_scores.py has already set them from the boxes."""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'writeups.json')
w = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

def rep(key, old, new):
    t = w[key]
    n = t.count(old)
    assert n == 1, f'{key}: fragment appears {n} times, expected 1'
    i = t.index(old)
    print(f'  {key}: ...{t[max(0,i-40):i+len(old)+150]!r}...\n')
    w[key] = t.replace(old, new)

print('EDITS')
rep('p:TLS',
    "The bank is also the day-to-day manager of the country's Petroleum Fund, and it hires "
    "outside firms to run parts of that money.",
    "The bank is also the day-to-day manager of the country's Petroleum Fund, and it hires "
    "outside firms to run parts of that money. That arrangement is set by the Petroleum Fund "
    "Law, Law No. 9/2005 of 3 August, republished with amendments by Law No. 12/2011, and it "
    "leaves the decisions with the government. Article 11 says the Government is responsible "
    "for the overall management of the Fund, that the Minister of Finance takes the decisions "
    "on its investment strategy and management after first obtaining the opinion of the "
    "Investment Advisory Board, and that the Minister signs a contract with the central bank "
    "for the Fund's operational management. Article 12(5) requires an investment manager to act "
    "within any instructions the Minister issues and within that operational management "
    "contract, and Article 16(1)(b) has the Advisory Board advise the Minister on the investment "
    "instructions he gives. Ministerial Diploma No. 4/2019 of 1 March 2019 shows this version of "
    "the law still in force and names the bank as the Fund's Operational Manager. It covers the "
    "Petroleum Fund only: the law says nothing about who sets interest rates.")

rep('p:MKD',
    "One case is recorded, running from 2017 to 2020, and it is unproven:",
    "In January 2025 a group of members of the Assembly moved on the bank's own money. Their "
    "bill, tabled under the shortened procedure, would rewrite article 15 of the Law on the "
    "National Bank so that the Council pays 30 per cent of the financial result into general "
    "reserves, 15 per cent once base capital is reached, and the remainder into the Budget of "
    "the Republic of North Macedonia, and it would oblige the bank to move the special reserves "
    "it had built up, which the bill puts at almost 27 million euros, into general reserves "
    "within 30 days and not to use them in the meantime. An amendment to that law was enacted "
    "as Sluzben vesnik 16/25, which the bank's own decisions cite from 4 February 2025, but the "
    "enacted text could not be read, so whether these are the provisions that passed is not "
    "confirmed. One case is recorded, running from 2017 to 2020, and it is unproven:")

NODES = {
 'n:Government of Timor-Leste':
   "The Government of Timor-Leste, in Dili, decides what the Banco Central de Timor-Leste does "
   "with the country's Petroleum Fund, which the bank manages day to day. Article 11 of the "
   "Petroleum Fund Law, Law No. 9/2005 of 3 August as amended by Law No. 12/2011, says the "
   "Government is responsible for the overall management of the Fund, and that the Minister of "
   "Finance signs a contract with the central bank for its operational management. Article 12(5) "
   "requires an investment manager to act within any instructions the Minister issues and within "
   "that contract. Ministerial Diploma No. 4/2019 of 1 March 2019 shows the arrangement in use: "
   "the Government had decided that the Fund's investments in petroleum operations would be "
   "carried out by the state oil company TIMOR GAP, under a contract to be signed by the bank as "
   "the Fund's Operational Manager. The arrangement covers the Fund and not the bank's other work.",
 'n:Assembly of the Republic of North Macedonia':
   "The Assembly of the Republic of North Macedonia, in Skopje, is where a bill to take part of "
   "the National Bank's money was tabled. In January 2025 a group of its members put forward, "
   "under the shortened procedure, amendments to the Law on the National Bank that would send the "
   "remainder of the Bank's annual financial result to the state Budget once 30 per cent has gone "
   "to general reserves, or 15 per cent after base capital is reached, and that would require the "
   "Bank to transfer the special reserves it had already formed, which the bill puts at almost 27 "
   "million euros, into general reserves within 30 days and not to use them before then. An "
   "amendment to that law was enacted as Sluzben vesnik 16/25 and the Bank's own decisions cite "
   "it from 4 February 2025; the enacted text itself has not been read, so what it contains is "
   "not confirmed here.",
}
print('NEW node paragraphs')
for k, v in NODES.items():
    assert k not in w, f'{k} already exists'
    assert "’" not in v, f'{k}: use a straight apostrophe, as the data files do'
    print(f'  {k}  ({len(v.split())} words)')
    w[k] = v

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(w, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'\nwritten: writeups.json now holds {len(w)} paragraphs')
