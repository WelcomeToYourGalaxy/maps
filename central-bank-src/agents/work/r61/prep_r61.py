#!/usr/bin/env python3
"""Round 61: turn the agents' output into one input file for merge_links.py.

Same safety as rounds 57 to 60: every decision is keyed on (iso3, a distinctive
token that must appear in that record's own text), and the script REFUSES TO
WRITE ANYTHING if a token matches no record or more than one.

THE DECISIONS, AND WHY.

Counted career moves:

  TJK x4  Four officials of the National Bank of Tajikistan sat on the boards of
          Spitamen Bank -- Khuseynova (2024), Dzhabirova (2023), Hamralizoda
          (2023) and Samandarzoda (2018, now chairman of its Management Board).
          Ownership is settled by the bank's OWN 2024 charter, which calls it a
          commercial organization and names a sole shareholder, the insurer
          Spitamen Insurance. Tajikistan is a new place on the row.
  AFG     Ajmal Ahmady, Acting Governor of Da Afghanistan Bank from 3 June 2020
          to 15 August 2021, came from T. Rowe Price, Acadian Asset Management
          and Fortress Investment Group. It keeps weak_source: true, because the
          DATED career is Wikipedia's, but a second source is added here that is
          not Wikipedia: Harvard Kennedy School's own page for him, which says he
          "worked in a variety of positions in the asset management industry"
          and names those three firms. Afghanistan is a new place.

  ON THE OWNERSHIP TEST, which this round refines rather than bends. The test
  exists because an employer may turn out to be STATE-owned: it was set by Peru's
  Velarde, whose employer Banco Central Hipotecario was state-owned with its
  ownership unstated, and it cost four places at round 59. It bites where the
  ownership is genuinely in doubt -- a local bank, insurer or finance company in
  a country that has state-owned banks. It does not bite for a firm a source
  itself places in private finance by sector and by name, and about a hundred
  records already on this map name Goldman Sachs, BlackRock, Morgan Stanley or
  UBS as private-finance employers on exactly that footing. ING needed a separate
  ownership page at round 60 for a reason that proves the point rather than
  contradicting it: its record's source named it bare in a list that also held
  ABN Amro, which IS partly state-owned.

Public moves -- filed, shown in the country's box, counted nowhere:

  BTN     Damche Tenzin, from Bank of Bhutan Limited to the Royal Monetary
          Authority. Bank of Bhutan is 80% owned by Druk Holding & Investments,
          which the state owns, so this is public on its face.
  TLS     Helder Lopes, Governor from 2023: Minister of Finance, Vice Minister,
          adviser to the President, and a senior economist on an Asian
          Development Bank initiative. Every employer is public. It opens
          Timor-Leste's box, which held no career move at all, and moves no
          percentage.

Moves against the bank:

  MKD     The State Audit Office's own final report 11-107/8 of 4 March 2005 on
          the National Bank's 2003 accounts, audited on site from 12 October to
          20 December 2004. This is the Uganda shape -- a supreme audit
          institution auditing the bank itself. WebFetch returns "[binary data]"
          for the .doc, so the file was downloaded with curl and converted
          locally, and every figure in the record was verified against the file:
          20.759.515 US dollars drawn from the bank's guarantee deposit,
          30.210 thousand denars of procurement outside the Public Procurement
          Law, 35,61% of audited procurement, the report number, the heading
          about improper and unlawful use of funds, and article 83. The file's own
          metadata says it was last printed on 4 March 2005, the report's date.
  WSM     The Central Bank of Samoa objected IN WRITING, in a letter to the
          Attorney-General's office, to changes widening the Finance Minister's
          role. That is the filed family that Mexico, Romania and Peru are in,
          and it is the different fact Samoa needed: it was held last round on
          the Singapore line, where the statute bars instructions to the bank.
  NAM     President Nandi-Ndaitwah told parliament on 13 April 2026 that reported
          losses at the Bank of Namibia were "smelling of corruption" and must be
          investigated. This is the marginal one and it was filed on a
          consistency test rather than a feel: the map already carries Trump's
          "should resign immediately" of 2 July 2025 and Poilievre's pledge to
          fire the Governor of the Bank of Canada as public pressure, both with no
          act following. It is distinguishable from the Armenian exclusion, where
          the actor was a deputy chairman of an oversight body rather than a head
          of state. The record says plainly that no investigation is reported as
          ordered.

Corruption cases:

  BHS     $232.3m of IMF special drawing rights drawn through the Central Bank of
          The Bahamas in December 2022, which the opposition's finance spokesman
          said was contrary to section 21 of the Central Bank Act, after which the
          government tabled a bill disapplying section 21 to that transaction and
          deemed in force from 1 December 2022. The retroactive amendment is a
          fact in the source; the breach is an assertion, so the status is
          `alleged`. It is the same shape as the Barbados record already on the
          map, where the government's overdraft exceeded its statutory limit.
  WSM     A 2014 Samoa Audit Office performance audit of government debt
          servicing, finding repayments made late by the Central Bank of Samoa and
          no formalised arrangement between the bank and the Ministry of Finance,
          with the recommendations aimed at the Ministry. `counterparty_only` is
          set true. It is filed rather than dropped because the standing rule is
          not to filter a source and because the row already carries this shape
          -- Guyana's dormant state accounts, and three of the Barbados five --
          and because the owner is deciding that question, for which the flag is
          how the records are found. It alleges no wrongdoing and says so.

  CUW     Jose Jardim, a member of the CBCS board until 30 June 2025, became chief
          executive of Banco di Caribe on 1 July 2025. This is round 60's held
          Curacao record settled: that round had only a report naming NEITHER the
          person nor the bank, and a record naming no one is not a record. Both
          are now named, and the same report states the bank "has been wholly
          owned by United Group Holdings since 2022". Curacao had held only a
          public career move, so it converts to a counted place.
  LSO     Mrs M. Mohasoa, a non-executive director of the Central Bank of Lesotho,
          from the board of Liberty Life Lesotho where she chaired the audit and
          risk committee from 2017 to 2021. Round 60 held it for want of an
          ownership statement; it is settled by the South African Reserve Bank's
          designated-entity list placing Liberty Life Lesotho in the Liberty
          Insurance Group, and Liberty Holdings' own 2019 annual report stating
          that Standard Bank Group holds 53.6% of Liberty. Lesotho was already a
          place, so this adds a record.
  DZA     Mohamed Lamine Lebbou, Governor of the Banque d'Algerie, began at BNP
          Paribas El Djazair from 2004 to 2006. That bank's own 2018 annual report
          says it is "detenue a 100% par BNP Paribas France". His later posts at
          BNA and BEA are state-owned and are excluded rather than counted.
          Algeria is a new place.

  One record arrived that is ALREADY ON THE MAP: Mr O. 'Nete of the Central Bank
  of Lesotho, filed at round 60 from the same board page. It is marked `dup` here
  and left out, and `merge_links.py` would have dropped it anyway on its
  (iso3, source_url, people) key. Two agents reading the same board page a round
  apart is the ordinary way this happens and costs nothing.

HELD, each with the one fetch that settles it:

  BOL     Jaime Valencia Valencia, between the Banco Central de Bolivia's general
          managership and Banco de la Union, Banco de Cochabamba and Compania
          Boliviana de Seguros. Held for the SECOND round running: the CV was
          re-fetched and lists the three firms with no titles, no dates and no
          ownership, ASFI's history-of-supervision page returned a client error,
          and the article on the insurer's successor names no shareholders. ASFI's
          register of banks and of insurers is still the fetch that settles it.
  UGA     Blasio Kizza, a member of the Bank of Uganda board, whom Central Banking
          calls "an ex-Uganda Commercial Bank banker" with no date and no
          ownership statement. Uganda Commercial Bank was state-owned for most of
          its life and was sold to Stanbic in 2002, so WHICH YEARS he was there
          decides whether this counts at all. A dated biography is the fetch.
  KOR     Jeong Gyu-il, Bank of Korea Deputy Governor to chief executive of Seoul
          Foreign Exchange Brokerage in 2021. The asiae report names no
          shareholder at all. `smbs.biz`, the brokerage's own site, would settle
          it. Korea already counts, so this is a record, not a place.
  SDN     Ibrahim Mohammed Ali Nimir, between the Central Bank of Sudan's
          governorship and Elneilin Bank, National Bank and Workers National
          Bank. The bank's own page on former governors states none of the three
          employers' ownership. **This one is worth doing first next round**: it
          would take Sudan off the list of places whose only career moves are
          public. The Central Bank of Sudan's own register of licensed banks, or
          Elneilin Bank's own history page, would settle it.
"""
import json
import os
import sys

R = os.path.dirname(os.path.abspath(__file__))

RD = {
    ('CUW', 'Jardim'): 'count',
    ('LSO', 'Mohasoa'): 'count',
    ('LSO', "'Nete"): 'dup',
    ('DZA', 'Lebbou'): 'count',
    ('BOL', 'Valencia'): 'hold',
    ('UGA', 'Kizza'): 'hold',
    ('DOM', 'Hazoury'): 'public',
    ('TJK', 'Khuseynova'): 'count',
    ('TJK', 'Dzhabirova'): 'count',
    ('TJK', 'Hamralizoda'): 'count',
    ('TJK', 'Samandarzoda'): 'count',
    ('AFG', 'Ahmady'): 'count',
    ('BTN', 'Damche Tenzin'): 'public',
    ('TLS', 'Helder Lopes'): 'public',
    ('KOR', 'Jeong Gyu-il'): 'hold',
    ('SDN', 'Nimir'): 'hold',
}

SECOND = {
    ('AFG', 'Ahmady'): (
        'M-RCBG Senior Fellow-Led Study Group: Ajmal Ahmady (Harvard Kennedy School)',
        'https://www.hks.harvard.edu/centers/mrcbg/students/sg/ahmady.2021.fall',
        'worked in a variety of positions in the asset management industry',
        "Harvard Kennedy School's own page for him, which is not Wikipedia, describes him as the "
        "former Afghan Central Bank Governor and says that before his government work he worked in "
        "a variety of positions in the asset management industry, naming Fortress Investment Group, "
        "Acadian Asset Management and T. Rowe Price. The dated career in this record rests on "
        "Wikipedia, which is why it stays marked as a weak source."),
}

EVENTS = {
    ('MKD', '11-107/8'): 'file',
    ('WSM', 'Attorney-General'): 'file',
    ('NAM', 'smelling of corruption'): 'file',
}

CASES = {
    ('BHS', '232.3'): 'file',
    ('WSM', 'Audit Office'): 'file',
}

# build_final.py refuses to build on a status that is on neither list, and the agents
# wrote two new ones. The nuance each carries stays in its own summary.
STATUS = {
    'alleged; breach asserted by the opposition, the Act amended retroactively': 'alleged',
    'audit finding; no wrongdoing alleged': 'official finding',
}


def text(r):
    return json.dumps(r, ensure_ascii=False)


def pick(records, table, what):
    out, held, problems, dups = [], [], [], []
    used = set()
    for r in records:
        iso = r.get('iso3') or r.get('cb_iso3')
        t = text(r)
        hits = [k for k in table if k[0] == iso and k[1] in t]
        if len(hits) != 1:
            problems.append('%s %s: matched %d entries in the %s table'
                            % (iso, (r.get('people') or r.get('kind') or '')[:40], len(hits), what))
            continue
        k = hits[0]
        if k in used:
            problems.append('%s: table entry %s matched twice' % (iso, k))
            continue
        used.add(k)
        if table[k] == 'dup':
            dups.append((k, r))
            continue
        (held if table[k] == 'hold' else out).append((k, r))
    missing = [k for k in table if k not in used]
    if missing:
        problems.append('table entries that matched no record: %s' % sorted(missing))
    if dups:
        for k, _ in dups:
            print('  already on the map from an earlier round, left out: %s' % (k,))
    return out, held, problems


def main():
    rd = []
    for f in ('rd_a1.json', 'rd_a2.json'):
        p = os.path.join(R, f)
        if os.path.exists(p):
            rd += json.load(open(p, encoding='utf-8'))['records']
    moves = json.load(open(os.path.join(R, 'moves.json'), encoding='utf-8'))['events']
    cases = json.load(open(os.path.join(R, 'cases.json'), encoding='utf-8'))['records']

    rd_ok, rd_held, p1 = pick(rd, RD, 'revolving door')
    ev_ok, ev_held, p2 = pick(moves, EVENTS, 'events')
    ca_ok, ca_held, p3 = pick(cases, CASES, 'cases')
    problems = p1 + p2 + p3
    if problems:
        print('REFUSING TO WRITE. Every decision is keyed on a token that must appear in its own')
        print('record, and these did not line up:')
        for x in problems:
            print('  ' + x)
        return 1

    records = []
    for k, r in rd_ok:
        r = dict(r)
        r.pop('needs_ownership_check', None)
        r['public_move'] = (RD[k] == 'public')
        if k in SECOND:
            title, url, quote, sentence = SECOND[k]
            r['second_source_title'] = title
            r['second_source_url'] = url
            r['second_source_quote'] = quote
            r['summary'] = r['summary'].rstrip() + ' ' + sentence
        records.append(r)
    for k, r in ev_ok:
        records.append(dict(r))
    for k, r in ca_ok:
        r = dict(r)
        r['status'] = STATUS.get(r['status'], r['status'])
        records.append(r)

    json.dump({'records': records}, open(os.path.join(R, 'to_merge.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump([{'key': list(k), 'record': r} for k, r in rd_held + ev_held + ca_held],
              open(os.path.join(R, 'held.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    counted = sum(1 for k, _ in rd_ok if RD[k] == 'count')
    print('wrote %d records' % len(records))
    print('  revolving door: %d counted, %d public' % (counted, len(rd_ok) - counted))
    print('  events: %d   cases: %d' % (len(ev_ok), len(ca_ok)))
    print('held %d, with the fetch that settles each' % len(rd_held + ev_held + ca_held))
    return 0


if __name__ == '__main__':
    sys.exit(main())
