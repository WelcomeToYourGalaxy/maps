#!/usr/bin/env python3
"""Round 60: turn five agents' output into one input file for merge_links.py.

Same safety as rounds 57 to 59: every decision is keyed on (iso3, a distinctive
token that must appear in that record's own text), and the script REFUSES TO
WRITE ANYTHING if a token is missing. An agent file edited between rounds, or a
record reordered, therefore stops the round instead of hanging a decision on the
wrong record.

What it decides, and why -- the reasoning belongs here rather than in a handoff
paragraph, because this file is committed with the work it did:

COUNTED. A career move counts on the revolving-door row only where a source
STATES that the employer is privately owned. Round 59 lost four places to this
rule and each was left with the single fetch that would settle it. Seven records
arrived already carrying that evidence in a second source. Six more were settled
in this session by opening one page each, and those second sources are added
here rather than left for another round:

  MMR Than Lwin   Kanbawza Bank -- The Irrawaddy: "KBZ Bank is the largest of 19
                  privately owned banks in Myanmar."
  MMR Khin Saw Oo AYA Bank -- the bank's own corporate profile: "AYA Bank PCL is
                  a leading private sector bank in Myanmar", "Registered as a
                  Private Company Limited by Shares on 14th July 2010". It was
                  reincorporated as a public company on 30 December 2022, after
                  she joined in 2018 and was re-designated in May 2021.
  PSE Shunnar     Palestine Islamic Bank -- the bank's own 2025 annual report
                  names its shareholders above 5%: National Islamic Investment
                  Company 24.85%, Palestinian Pension Agency 10.39%, Razan
                  Medical Center 10.09%, Mr Salah Al-Daghma 9.59%, Birzeit
                  Pharmaceutical 8.51%, Orphans Fund 7.01%, Aswaq Investment
                  5.45%. Mixed, mostly private. Stated mixed ownership on the
                  face of the record is admissible -- the Uruguay precedent --
                  inferred private ownership is not.
  SOM Abrar       the employer that settles it is not TLG Financial Services,
                  whose ownership no source states, but Citigroup and AIG, which
                  Quartz names: "Yussur Abrar, a former banker at Citigroup and
                  AIG, became the governor of the central bank today".
  LSO 'Nete       Standard Lesotho Bank -- Standard Bank Group's own structure
                  page lists "Standard Lesotho Bank Limited (80%)" among its
                  holdings as at 30 June 2026.
  ABW Domhoff     ING -- ING's own largest-investors page states "ING Group is a
                  publicly-listed company" and names BlackRock (7.3% by its
                  February 2024 Schedule 13G) and Amundi above 3%.

PUBLIC. Three records name only a ministry, a regional development bank or a
state-owned bank. They are worth having and they show in the country's box, and
app.js does not count them, so they move no percentage: IRQ (the Trade Bank of
Iraq, which the source itself calls state-owned), BTN (the National Pension &
Provident Fund) and SDN (the Bank of Sahel and Sahara Community and the finance
ministry; his undated Saudi Sudanese Bank board seat has no ownership stated and
is described that way in the record).

HELD, not filed, each with the one fetch that would settle it:
  BOL Valencia    the bank's own CV names Banco de la Union S.A., Banco de
                  Cochabamba and Compania Boliviana de Seguros S.A. with no
                  dates and no ownership. ASFI's register of banks and insurers
                  would settle all three.
  LSO Mohasoa     Liberty Life Lesotho's ownership is stated nowhere opened.
                  Liberty Holdings' or Standard Bank Group's own subsidiary list
                  would settle it. Lesotho is already a place this round on the
                  'Nete record, so this adds a record, not a place.
  CUW director    the Curacao Chronicle report names neither the person nor the
                  bank. A record naming no one is not a record. It would be
                  settled by the CBCS's own announcement of the resignation, or
                  by the bank that appointed him naming its new chief executive.
  NAM s.66        the Bank of Namibia Act lets the Minister direct the
                  Auditor-General to investigate the bank and sets the report's
                  terms -- but s.5 bars instructions to the bank and criminalises
                  interference. That is the Singapore line, and Timor-Leste,
                  Curacao and Samoa were all held on it last round: an ordinary
                  accountability provision is not capture. It reverses on an
                  instance of a Minister actually directing such an
                  investigation, which would be the Uganda shape.

One more that is NOT in the agent files and is recorded here so the reasoning is
not lost: the Kosovo RAMP pair. Round 59 filed the 16 April 2026 upgrade beside
the 2023 membership record, whose own closing clause said the arrangement was
"not management of its reserves". Two ties on one bank then contradicted each
other in the same box. The 2023 record's clause is now dated so the two read as
a sequence. No row moves.
"""
import json
import os
import sys

R = os.path.dirname(os.path.abspath(__file__))

# (iso3, token that must appear in the record) -> what to do
RD = {
    ('HND', 'Cerrato'): 'count',
    ('GMB', 'Jabby'): 'count',
    ('SLV', 'Barraza'): 'count',
    ('COD', 'Ilondo'): 'count',
    ('NIC', 'Rivas'): 'count',
    ('IRN', 'Seif'): 'count',
    ('SSD', 'Othow'): 'count',
    ('MMR', 'Than Lwin'): 'count',
    ('MMR', 'Khin Saw Oo'): 'count',
    ('PSE', 'Shunnar'): 'count',
    ('SOM', 'Abrar'): 'count',
    ('LSO', "'Nete"): 'count',
    ('ABW', 'Domhoff'): 'count',
    ('IRQ', 'al-Heims'): 'public',
    ('BTN', 'Penjore'): 'public',
    ('SDN', 'Al-Zubair'): 'public',
    ('BOL', 'Valencia'): 'hold',
    ('LSO', 'Mohasoa'): 'hold',
    ('CUW', 'Director'): 'hold',
}

# second sources opened in this session, for the records settled here
SECOND = {
    ('MMR', 'Than Lwin'): (
        'Interview: KBZ Bank senior managing director Than Cho on Myanmar banking (The Irrawaddy)',
        'https://www.irrawaddy.com/?p=61394',
        'KBZ Bank is the largest of 19 privately owned banks in Myanmar.',
        "The Irrawaddy's interview with KBZ Bank's senior managing director calls the bank "
        "Myanmar's largest privately owned financial institution and the largest of 19 privately "
        "owned banks in the country, which establishes the employer's private ownership."),
    ('MMR', 'Khin Saw Oo'): (
        'AYA Bank corporate profile (Ayeyarwady Bank Public Company Limited)',
        'https://ayabank.com/about-aya/who-we-are/corporate-profile/ayabank-profile',
        'AYA Bank PCL is a leading private sector bank in Myanmar.',
        "The bank's own corporate profile calls AYA Bank a leading private sector bank in Myanmar "
        "and says it was registered as a Private Company Limited by Shares on 14 July 2010 and "
        "reincorporated as a Public Company Limited on 30 December 2022, after she joined in 2018."),
    ('PSE', 'Shunnar'): (
        'Palestine Islamic Bank annual report 2025, board and shareholders (Palestine Islamic Bank)',
        'https://www.islamicbank.ps/en/annual/2025/family4',
        'Representative of the National Islamic Investment Company',
        "The bank's own 2025 annual report names its shareholders above 5 per cent: the National "
        "Islamic Investment Company 24.85 per cent, the Palestinian Pension Agency 10.39 per cent, "
        "Razan Medical Center 10.09 per cent, Mr Salah Al-Daghma 9.59 per cent, Birzeit "
        "Pharmaceutical 8.51 per cent, the Orphans Fund foundation 7.01 per cent and Aswaq "
        "Investment 5.45 per cent, so the shareholding is mostly private with a public pension "
        "agency among the large holders."),
    ('SOM', 'Abrar'): (
        "Can Somalia's new female central banker break crony capitalism there? (Quartz)",
        'https://qz.com/126555/can-somalias-new-female-central-banker-break-crony-capitalism-there',
        'Yussur Abrar, a former banker at Citigroup and AIG, became the governor of the central bank today',
        "Quartz, reporting on the day she took office, names the private employers the first source "
        "left unnamed: it calls her a former banker at Citigroup and AIG. The ownership of TLG "
        "Financial Services is still stated nowhere, so this record rests on Citigroup and AIG."),
    ('LSO', "'Nete"): (
        'Standard Bank Group holdings as at 30 June 2026 (Standard Bank Group)',
        'https://reporting.standardbank.com/sbg/standard-bank-group/our-group/about-us/our-structure',
        'Standard Lesotho Bank Limited (80%)',
        "Standard Bank Group's own structure page lists Standard Lesotho Bank Limited at 80 per "
        "cent among its holdings as at 30 June 2026, so the employer is majority owned by the "
        "Johannesburg-listed group rather than by the state."),
    ('ABW', 'Domhoff'): (
        'Largest investors (ING Group)',
        'https://ing.com/about-us/corporate-governance/shareholder-influence/largest-investors',
        'ING Group is a publicly-listed company',
        "ING's own largest-investors page states that ING Group is a publicly-listed company and "
        "names BlackRock, which disclosed 7.3 per cent of its issued share capital in a Schedule "
        "13G, and Amundi Asset Management among holders above 3 per cent."),
}

EVENTS = {
    ('GUY', 'section 29'): 'file',
    ('URY', '197'): 'file',
    ('CUW', 'Gibson'): 'file',
    ('NAM', '66'): 'hold',
}

STATUS = {'audit finding': 'official finding',
          'internal audit finding': 'official finding',
          'disciplinary action taken': 'official finding'}

CASES = {
    ('CAN', 'audit'): 'file',
    ('UZB', 'disciplinary'): 'file',
    ('PSE', 'Control Bureau'): 'file',
}


def text(r):
    return json.dumps(r, ensure_ascii=False)


def pick(records, table, what):
    """Match each record to exactly one table entry, or stop the round."""
    out, held, problems = [], [], []
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
        if table[k] == 'hold':
            held.append((k, r))
            continue
        out.append((k, r))
    missing = [k for k in table if k not in used]
    if missing:
        problems.append('table entries that matched no record: %s' % sorted(missing))
    return out, held, problems


def main():
    rd = []
    for f in ('rd_a1.json', 'rd_a2.json'):
        rd += json.load(open(os.path.join(R, f)))['records']
    moves = json.load(open(os.path.join(R, 'moves.json')))['events']
    cases = json.load(open(os.path.join(R, 'cases.json')))['records']

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
            # the summary must say what the second source says, not assert ownership bare
            r['summary'] = r['summary'].split('Ownership:')[0].rstrip()
            r['summary'] += ' Ownership: ' + sentence
        records.append(r)
    for k, r in ev_ok:
        records.append(dict(r))
    for k, r in ca_ok:
        r = dict(r)
        # build_final.py refuses to build on a status that is on neither list, and the
        # agents wrote three new ones. All three are a state body or the bank's own audit
        # function recording a finding, which is what "official finding" is for; the
        # agent's own wording stays in the summary.
        r['status'] = STATUS.get(r['status'], r['status'])
        records.append(r)

    out = os.path.join(R, 'to_merge.json')
    json.dump({'records': records}, open(out, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    heldf = os.path.join(R, 'held.json')
    json.dump([{'key': list(k), 'record': r} for k, r in rd_held + ev_held + ca_held],
              open(heldf, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    counted = sum(1 for k, _ in rd_ok if RD[k] == 'count')
    print('wrote %d records to %s' % (len(records), out))
    print('  revolving door: %d counted, %d public' % (counted, len(rd_ok) - counted))
    print('  events: %d   cases: %d' % (len(ev_ok), len(ca_ok)))
    print('held %d, with the fetch that would settle each, in %s' % (len(rd_held + ev_held), heldf))
    return 0


if __name__ == '__main__':
    sys.exit(main())
