#!/usr/bin/env python3
"""Round 64: add a `cases_unavailable` map to gaps.json, on the model of gold_unavailable and
managers_unavailable.

The corruption row had no place to record a documented negative, so eleven rounds of "searched and
found nothing" have lived only in working files. Round 63 settled the standard: a confirmed-blank
entry has to name the document AND the section read, or it is not a close, it is a note that
somebody looked somewhere. These entries are written that way, and each one says which of four
things it is, because treating "the vein is closed" as "the country is closed" is how a round gets
wasted re-reading a document that was never the right document:

  confirmed blank  -- the document that would name a case was read, and names none
  vein closed      -- the audit-institution route is exhausted here; other routes are not
  not reached      -- the document exists or may exist and was never opened
  refused          -- a real candidate was found and failed a settled rule

Nothing in the build reads this key, exactly as nothing reads gold_unavailable; it is research
state, and it is worth as much as a record because it stops the next round spending a call.
"""
import json, os, sys

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(A, 'gaps.json')
g = json.load(open(P, encoding='utf-8'))
dry = '--dry' in sys.argv

ENTRIES = {
 'SGP': "confirmed blank. Auditor-General's Office of Singapore, Annual Report FY2023/24, Part II "
        "'Financial Statements Audits' para 1(c) and its footnote 1, plus every audit observation "
        "in Parts I-III. The Monetary Authority of Singapore appears twice and in neither case as "
        "a body with lapses: it is listed among the statutory boards given an unmodified opinion "
        "for 2023/24, and footnote 1 says MAS is audited by the AGO annually because the MAS Act "
        "names no other auditor. So the supreme audit institution examines this central bank every "
        "year and has found nothing to report. That also makes each AGO annual report from "
        "FY2012/13 to FY2024/25 a separate checkable document; only FY2023/24 has been read.",
 'PSE': "confirmed blank for the sections read. (1) AMAN study No. 302 (2025), 'Managing "
        "Corruption Risks at the Palestine Monetary Authority', chars 0-100,000 of 106,017: it "
        "says in its own words that it does not investigate cases that have actually happened, and "
        "rates licensing-deviation probability as low. A risk assessment, not a finding. (2) SAACB "
        "Annual Report 2020, chars 0-100,000 and 200,000-300,000 of about 500,000: the Monetary "
        "Authority appears twice and never as the audited body -- once as the Ministry of "
        "Finance's undisclosed creditor for about 2,130,918 dinars of exchange-company licence "
        "fees, once as the employer of people paid under a Ministry of Labour programme. Fifteen "
        "audited entities are named in that portion and the Authority is not among them. The "
        "unread middle of that report is the one remaining section.",
 'BHR': "confirmed blank for the document read. Bahrain's National Audit Office 2024 annual "
        "report, as reported in full by the Daily Tribune: the Central Bank of Bahrain is not an "
        "audited body in it and is not criticised. The bodies audited are ministries, state-owned "
        "entities, Gulf Air, Bapco Energies, the Sunni Waqf Directorate, public hospitals and the "
        "National Health Regulatory Authority. The NAO's own full report was not obtained.",
 'QAT': "vein closed, country not closed. Qatar's State Audit Bureau publishes no entity-level "
        "findings at all -- the only 2026 coverage is of law amendments expanding the Bureau's own "
        "powers -- and Shura Council finance committee coverage names no institution. So the "
        "audit-institution route cannot produce a Qatari record whatever the facts are. Other "
        "routes are untried.",
 'SAU': "vein closed on the inversion test. About a dozen Nazaha monthly case statements were "
        "surfaced and the two most detailed read case by case: every named employer is a "
        "municipality, the Traffic Department, Health Affairs, the Ministry of Health, a hospital, "
        "a school, a private firm or a charity. The Saudi Central Bank appears only in the phrase "
        "'in cooperation with the Presidency of State Security and the Saudi Central Bank' -- it is "
        "the detector, not the subject. Filing any of these would credit Saudi Arabia with a "
        "corruption case for catching wrongdoing.",
 'BMU': "lead closed. Bermuda Auditor General, 'Report on the Implementation of Recommendations "
        "from selected Government related entities' (June 2023), Appendix III 'Audits In Progress', "
        "read at offset 90,000: the Bermuda Monetary Authority does not appear. The six entities "
        "listed are the Berkeley Institute and Sandys Secondary capitation grant accounts, the "
        "Bermuda Educators Council, the Trustees of the National Sports Centre, the Bermuda "
        "Economic Development Corporation and the Bermuda Gaming Commission.",
 'SLV': "refused, with a real candidate. Carlos Federico Paredes was president of the Banco "
        "Central de Reserva from June to November 2019 and was sentenced to eight years on 25 "
        "November 2020 for fraud against three women over promised land lots, upheld on appeal on "
        "18 August 2021, then annulled by the Sala de lo Penal with a definitive dismissal because "
        "the offence was time-barred from facts of 2008. It fails twice over: the conduct was a "
        "private land sale eleven years before he held office, so the bank is not the subject, and "
        "the outcome maps to 'conviction annulled (time-barred)', which this map does not count. "
        "Separately, the Corte de Cuentas' bitcoin work targets government procurement and the "
        "Chivo company, not the central bank, and the Corte de Cuentas' own site was never reached.",
 'WSM': "vein searched, nothing against the bank. The Samoa Audit Office and the Ministry of "
        "Finance's internal audit matters that search returns have as their subjects the Ministry "
        "of Health's procurement, the Ministry of Finance's accounts division and the Samoa Land "
        "Corporation. Samoa's existing finding on government debt is flagged counterparty_only "
        "because its recommendations went to the Ministry of Finance. What is needed is a finding "
        "whose subject is the Central Bank of Samoa or its officials.",
 'CPV': "not reached. The Tribunal de Contas de Cabo Verde's own site never appeared in a search "
        "result, so its Relatorio e Parecer sobre a Conta Geral do Estado is unread and Cabo Verde "
        "has not actually been tested on this vein. One trap recorded: search surfaces the "
        "PORTUGUESE Tribunal de Contas' Novo Banco audit, which has nothing to do with Cabo Verde "
        "and must not be keyed to CPV. A Cabo Verdean prosecutor's finding of indications of crime "
        "after an audit concerns the Presidency, not the bank.",
 'BRN': "not reached. Brunei's Auditor General report is not published online in any form search "
        "returns. Everything surfaced is either the central bank's own publications, a commercial "
        "bank's report, or the FATF/APG Mutual Evaluation Report 2023, which assesses the "
        "anti-money-laundering system as a methodology exercise and is not a finding of misconduct "
        "at the bank. Legislative Council proceedings naming the bank were not obtained.",
 'EGY': "one fact away. On 13 June 2018 Egypt's Administrative Control Authority arrested the "
        "'director of the supervision and oversight sector at one of the banks' for taking bribes "
        "from a private exchange-company owner to overlook its violations, including off-channel "
        "foreign-currency trading, and for leaking the dates of planned inspections of that "
        "company; he was referred to the public prosecution. That is a supervisory failure with "
        "named conduct, a date and an arresting body -- which is squarely what this row carries. It "
        "is not filed because two outlets both say only 'one of the banks': supervising exchange "
        "companies is a Central Bank of Egypt function and the sector name matches the CBE's own, "
        "but that is inference and not a source. THE REVERSING FACT: any source naming the "
        "employer as the Central Bank of Egypt. A separate 5 May 2018 round-up names four Ministry "
        "of Finance officials and officials from 'many banks around the state' and names no bank.",
}

assert 'cases_unavailable' not in g, 'cases_unavailable already exists -- merge rather than overwrite'
print(f'adding cases_unavailable with {len(ENTRIES)} entries')
for k, v in sorted(ENTRIES.items()):
    assert len(v) > 120, f'{k}: note too short to be a close'
    print(f'  {k}  {v.split(".")[0]}')
g['cases_unavailable'] = dict(sorted(ENTRIES.items()))

if dry:
    print('\n(dry run; nothing written)'); sys.exit(0)
json.dump(g, open(P, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('\nwritten: gaps.json')
