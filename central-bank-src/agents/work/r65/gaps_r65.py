#!/usr/bin/env python3
"""Round 65: file this round's documented negatives and holds into gaps.json.

Each entry names the DOCUMENT AND THE SECTION read, which is the standard round 63 settled: a
confirmed-blank entry that names neither is not a close, it is a note that somebody looked
somewhere. Two "confirmed blanks" have already fallen because an earlier round read one document
or one section and the answer was in another.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'gaps.json')
g = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

GOLD = {
 'LUX': "confirmed blank. Banque centrale du Luxembourg, Rapport annuel 2025, NOTE 3 'Avoirs et "
        "creances en or' read in full, plus the gold accounting policy and the reserve-management "
        "sections 'Portefeuille de reserves en devises' and 'Services de gestion des reserves'. "
        "The note is two lines: 72,101.30 ounces, 264.55 million euro. No institution anywhere.",
 'BWA': "confirmed blank, and a different kind. Bank of Botswana Annual Report 2024 including the "
        "Annual Financial Statements to 31 December 2024: the word gold does not appear in the "
        "statements or notes at all, only in the economic review as mineral exports. So this is not "
        "an undisclosed custodian, it is a bank with no gold line to disclose. Host note: the "
        "/sites/default/files/publications/ path returns a 12 kB HTML page; /news-files/ works.",
 'HRV': "confirmed blank. Hrvatska narodna banka, Godisnje izvjesce 2022, balance-sheet item 1 "
        "'Zlato i potrazivanja u zlatu', the gold valuation policies, and the FX-reserve structure "
        "section 'Upravljanje medunarodnim pricuvama'. Line item and valuation rules only; the one "
        "gold event named is the 15-per-cent-in-gold transfer to the ECB on euro entry.",
 'ETH': "confirmed blank BY THE YIELD RULE, which is worth stating because a firm IS named. "
        "National Bank of Ethiopia Annual Financial Statements to 30 June 2020, policy 3(s) 'Gold' "
        "and Note 10 'Gold' (a) Monetary gold: the gold is held as an interest-bearing TIME DEPOSIT "
        "at Commerzbank, capped at 8,000 ounces. Gold deposited at interest does not say where the "
        "metal sits, so Commerzbank is not a custodian here and must not be filed as one.",
 'SLB': "confirmed blank, and structurally so. Central Bank of Solomon Islands Annual Report 2024, "
        "all 311,960 characters in three passes: chapter 4 reserves and 'Gold Investment Policy', "
        "the Middle Office counterparty section, and Note 5 'Gold' with Note 2(m). The Bank SOLD "
        "its bullion and now trades only unallocated paper gold, SBD 44,364 thousand at end-2024, "
        "so there is no metal to hold and no custodian to name. BRED Banque (Paris) and Crown "
        "Agents Investment Management (London) appear as reserve counterparties, not as gold "
        "holders. Host note: cbsi.com.sb 404s to curl and serves fine through WebFetch.",
 'MDV': "confirmed blank. Maldives Monetary Authority Annual Report 2013, policy 'a) Gold' and "
        "Note 11 'Gold and silver assets' (11.1): MVR 29,132,185 of gold at fair value, one "
        "sentence of valuation policy, no institution.",
 'UGA': "not yet a target. New Vision, 'BoU to secure global custodian for gold reserves', April "
        "2026: the Governor says the Bank of Uganda PLANS to appoint a global custodian, so none "
        "exists yet and there is nothing to file. EuroGold Refinery Ltd and Feldstein Trading "
        "Limited are named as the refineries it buys through, not as holders, and the Bank of "
        "England reference is a general industry remark. Worth revisiting once an appointment is "
        "announced.",
 'AGO': "HELD, not blank, and one line away. VerAngola/Lusa of 25 October 2018, reading the Banco "
        "Nacional de Angola's own Relatorio e Contas 2017, says the bank 'tera a sua guarda quase "
        "19 toneladas de ouro', more than 602,000 troy ounces (18,700 kilogrammes), worth over 128 "
        "billion kwanzas at end-2017. So the holder is the BNA itself -- but NO VAULT AND NO CITY "
        "IS STATED, and this row's own rule is that a bank recorded as holding its own gold must "
        "name the place that holds it; merge_links.py refuses it on exactly that ground. Every "
        "self-custody node on the map is named '<Bank> vaults, <City>' or '<Bank> strongroom, "
        "<City>' for that reason. THE FETCH THAT SETTLES IT: the BNA's own Relatorio e Contas, "
        "which the press item is reading, since the accounts themselves would state the location.",
}
MGR = {
 'MUS': "confirmed blank. Bank of Mauritius Annual Report 2025: Note 10(i) ('funds entrusted to "
        "external fund managers'), Note 24, Note 29 (management fees to external fund managers "
        "plus custodian fees), Note 34(b)(ii) (level 2 instruments valued at the external fund "
        "managers' NAV), and chapter 3 'Reserves'. It uses external managers and names none. Host "
        "note: bom.mu fails TLS verification for curl through the proxy and is reachable with "
        "WebFetch, so a TLS error on a central bank host is worth one retry with the other tool.",
 'MOZ': "confirmed blank. Banco de Mocambique, Relatorio Anual 2022, notes to the financial "
        "statements: it 'contrata gestores externos para a gestao das suas reservas', with a "
        "separate benchmark for each externally managed portfolio and a monthly custodian breach "
        "report, and section 5.4.1 sets their exposure, duration and stop-loss limits. It names no "
        "firm and no custodian.",
 'SRB': "confirmed blank, and in-house rather than undisclosed. National Bank of Serbia Annual "
        "Report 2023, the FX reserve management policy section and chapter VI.3 'FX reserve "
        "management' with 'Credit risk' and Table VI.3.1: management runs Strategic Guidelines to "
        "Investment Committee to Tactical Guidelines, wholly internal. The custody banks that "
        "appear belong to supervised pension funds, not to the NBS.",
 'FJI': "confirmed blank, and internal. Reserve Bank of Fiji Annual Report August 2023 to July "
        "2024: the reserves narrative, Table 5 'Return on External Reserves', Figure 12 and the "
        "financial instruments note. Reserves are presented as 'the RBF portfolio' against a "
        "benchmark, with no outside manager.",
 'BRB': "searched, not closed. Central Bank of Barbados Annual Report 2025 returned only a job "
        "title, 'Director, Foreign Exchange and Fund Management', and an internal project-portfolio "
        "framework. Separately published audited statements, if any, were NOT read, so Barbados has "
        "not actually been tested on this row.",
}

for key, add, label in (('gold_unavailable', GOLD, 'gold'),
                        ('managers_unavailable', MGR, 'managers')):
    d = g[key]
    for k, v in sorted(add.items()):
        assert len(v) > 150, f'{k}: note too short to be a close'
        print(f"  {label:9} {k}  {'REPLACES existing' if k in d else 'new'}  "
              f"{v.split('.')[0][:70]}")
        d[k] = v
    g[key] = dict(sorted(d.items()))
    print(f'  -> {key} now {len(g[key])} entries')

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(g, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('\nwritten: gaps.json')
