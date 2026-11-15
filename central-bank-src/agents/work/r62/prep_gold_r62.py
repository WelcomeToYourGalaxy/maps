#!/usr/bin/env python3
"""Round 62, gold custodians: decide each record and bank the confirmed blanks.

The agent read a gold note in about 25 countries and found four custodians. One
of the four is not filable as it stands, and the 41 confirmed blanks are worth
more than they look: each one names the report and the note already read, so a
later round does not spend a call re-reading it.
"""
import json
import sys

R = '/root/cb/agents/work/r62/'
REL = 'holds its gold reserves in custody'

FILE = {
    'IRQ': ("The Central Bank of Iraq's 2025 financial statements split the holding into "
            "three lines in note 4: gold reserve abroad, gold reserve at the CBI vault and "
            "gold coins at the CBI vault. Only the bank's own vault is named; the note names "
            "no institution for the much larger holding held abroad, so that part is recorded "
            "as a blank rather than guessed at."),
    'RUS': ("Russia holds 2,283 tonnes, the sixth largest holding on the map. The Bank of "
            "Russia's own Annual Report 2025 says only that the assets are stored in Russia, "
            "naming no institution; the record is the Bank's own statement, quoted by Interfax, "
            "that all of the gold sits in its own vaults on Russian territory."),
    'COM': ("The Banque Centrale des Comores' 2024 auditor's report, note 5, puts eighteen "
            "bars in the bank's own strongroom in Moroni."),
}

HOLD = {
    'MWI': ("HELD, and it needs the owner's decision on two points. The Reserve Bank of "
            "Malawi's 2025 accounts, note 6, say the Bank holds monetary gold ON DEPOSIT WITH "
            "THE FEDERAL RESERVE BANK. First, the note does not say which Reserve Bank: there "
            "are twelve, and only the New York one holds foreign official gold, but the note "
            "does not say so and that is my knowledge rather than the source's. Filing the "
            "bare words 'Federal Reserve Bank' would put a second party on the map beside the "
            "existing Federal Reserve Bank of New York node, which is the duplicate-party "
            "problem this round was spent removing. Second, 'on deposit with' may be custody "
            "or may be a placement: the row's own rule says gold lent or deposited in return "
            "for interest does not say where the metal sits, and this note mentions no "
            "interest. One line in a later Malawi report, or a Federal Reserve list of "
            "earmarked gold by holder, settles both.")
}


def main():
    g = json.load(open(R + 'gold.json'))
    recs = {r['cb_iso3']: r for r in g['gold']}
    missing = set(FILE) | set(HOLD) ^ set(recs)
    unaccounted = [k for k in recs if k not in FILE and k not in HOLD]
    if unaccounted:
        sys.exit('REFUSED: gold records on neither list: %s' % unaccounted)
    for k in FILE:
        if k not in recs:
            sys.exit('REFUSED: no incoming record for %s' % k)

    out = []
    for iso, detail in FILE.items():
        r = recs[iso]
        tie = {'entity': r['custodian'],
               'entity_type': "central bank's own vault",
               'entity_hq_city': r.get('custodian_hq_city'),
               'entity_hq_iso3': r.get('custodian_hq_iso3'),
               'cb_iso3': iso,
               'relation': REL,
               'detail': detail,
               'as_of': r.get('as_of'),
               'source_title': r['source_title'],
               'source_url': r['source_url']}
        if r.get('custodian_as_stated'):
            tie['name_as_stated'] = r['custodian_as_stated']
        q = (r.get('source_quote') or '').strip()
        if q and len(q.split()) < 15:      # the standing quote limit
            tie['quote'] = q
        out.append(tie)

    json.dump({'records': out}, open(R + 'to_merge_gold.json', 'w'),
              ensure_ascii=False, indent=1)
    print('gold ties to file: %d  (%s)' % (len(out), ', '.join(FILE)))
    print('held: %s' % ', '.join(HOLD))
    for t in out:
        print('  %-4s %-52s quote=%s' % (t['cb_iso3'], t['entity'], 'yes' if t.get('quote') else 'no'))

    # bank the confirmed blanks in gaps.json, beside auditors_unavailable
    gp = json.load(open('/root/cb/agents/gaps.json'))
    blanks = {r['iso3']: r['note'] for r in g['not_found'] if r.get('iso3')}
    gp['gold_unavailable'] = dict(sorted(blanks.items()))
    json.dump(gp, open('/root/cb/agents/gaps.json', 'w'), ensure_ascii=False, indent=1)
    print('\ngaps.json: gold_unavailable now records %d checked places' % len(blanks))


if __name__ == '__main__':
    main()
