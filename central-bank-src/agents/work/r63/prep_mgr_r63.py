#!/usr/bin/env python3
"""Round 63, outside reserve managers: resolve each firm's NAME and HEAD OFFICE by hand.

An agent names the firm the source names, which is right, but it also supplied a head office for
every one of them and flagged only one as coming from general knowledge. A reserves-management
report names the manager, not the manager's head office, so they are all suspect and three of them
contradicted the map: UBS Asset Management was given as London and as Chicago where the map has a
Zurich head office sourced to the Seychelles reserves report.

The standing rule is that a head office comes from the record's own text, else `agents/hq.json`,
else the spelling already on the map, and is left NULL otherwise, because `build_net.py` then places
the party at the country centre and says so in its output, while a guessed city puts a marker
somewhere false and the map's markers are fixed points.

So each firm is resolved here into one of three cases:
  FOLD   the party is already on the map under another spelling -> reuse the map's name, city and
         country, and keep the source's wording in name_as_stated
  SOURCED the record's own text states the address -> use it
  BLANK  neither -> city and country left null, and the firm goes on the needs_hq list below

On folding: a wholly-owned asset-management arm IS folded into its group's node here, while the
national member firms of an audit network were kept SEPARATE at round 63's decision 4. Those look
alike and are not: EY Moldova is a legally separate firm with no common owner, whereas UBS Asset
Management (UK) Ltd is one group's business. The map's own precedent for keeping a subsidiary
separate -- Societe Generale Albania, BNP Paribas El Djazair -- is for records whose POINT is the
parent's ownership. These records are about who manages reserves.
"""
import json
import sys

R = '/root/cb/agents/work/r63/'

# entity as the agent filed it -> (map name, name_as_stated, city, iso3, why)
RESOLVE = {
    'UBS Asset Management (UK) Ltd': (
        'UBS Asset Management (UK) Ltd', 'UBS Asset Management (UK) Ltd', 'London', 'GBR',
        "SOURCED. The Irish contract award notice names the contractor as UBS Asset Management "
        "(UK) Ltd of 5 Broadgate, London, so the address is in the record itself. Kept separate "
        "from the map's `UBS Asset Management` node, whose head office is Zurich: this is the "
        "named contracting entity at a stated London address, and folding it would publish a "
        "Zurich marker for a contract awarded to a London company."),
    'Amundi Asset Management': (
        'Amundi', 'Amundi Asset Management', 'Paris', 'FRA',
        "FOLD. The award notice gives 90 Boulevard Pasteur, Paris, which is where the map already "
        "places its `Amundi` node, so folding loses nothing and avoids a second diamond for one "
        "firm in one city."),
    'JPMorgan Asset Management (UK) Limited': (
        'JPMorgan Asset Management (UK) Limited', 'JPMorgan Asset Management (UK) Limited',
        None, 'GBR',
        "Colombia's reserves report names the firm and gives no address. Kept separate from the "
        "map's `JPMorgan Asset Management` node, which is New York: a UK-incorporated entity does "
        "not sit in New York. The country comes from the firm's own registered name, which is the "
        "source stating it; the city is left null, so it is placed at the country centre."),
    'State Street Global Advisors': (
        'State Street Global Advisors', None, 'Boston', 'USA',
        "Already on the map at Boston. Timor-Leste's report names it without the Trust Co. suffix."),
    'State Street Global Advisors Trust Co.': (
        'State Street Global Advisors', 'State Street Global Advisors Trust Co.', 'Boston', 'USA',
        "FOLD into the map's existing node, same firm and same city."),
    'UBS Asset Management (Americas) Inc.': (
        'UBS Asset Management (Americas) Inc.', 'UBS Asset Management (Americas) Inc.', None, None,
        "BLANK, and this is the one the agent flagged: it gave Chicago from general knowledge. "
        "Nothing states this entity's address, and `(Americas)` is a business region rather than a "
        "country, so inferring the United States from `Inc.` would be a guess. Both fields left "
        "null and the firm goes on the needs_hq list."),
    'Pacific Investment Management Company LLC': (
        'PIMCO', 'Pacific Investment Management Company LLC', 'Newport Beach', 'USA',
        "FOLD. This is PIMCO's full legal name and the map already carries PIMCO at Newport Beach."),
    'Wellington Management Company LLP': (
        'Wellington Management Company LLP', 'Wellington Management Company LLP', None, None,
        "BLANK. New to the map and no source states an address. Needs HQ research."),
    'Goldman Sachs Asset Management L.P.': (
        'Goldman Sachs Asset Management L.P.', 'Goldman Sachs Asset Management L.P.', None, None,
        "BLANK. Kept separate from `Goldman Sachs`, the way the map already keeps UBS Asset "
        "Management from UBS and JPMorgan Asset Management from JPMorgan Chase. No sourced address."),
    'Schroders': (
        'Schroder Investment Management', 'Schroders', 'London', 'GBR',
        "FOLD. The map and `agents/hq.json` already carry Schroder Investment Management at "
        "London. That hq.json entry rests on Wikipedia and is on the list of eight to re-source."),
    'BlackRock': (
        'BlackRock', 'BlackRock', 'New York', 'USA', "Already on the map at New York."),
    'Barings LLC': (
        'Barings LLC', 'Barings LLC', None, None,
        "BLANK. New to the map, no sourced address. Needs HQ research."),
    'Franklin Templeton': (
        'Franklin Templeton', 'Franklin Templeton', None, None,
        "BLANK. New to the map, no sourced address. Needs HQ research."),
    'Bank for International Settlements': (
        'Bank for International Settlements', None, 'Basel', 'CHE',
        "Already on the map at Basel."),
}

NEEDS_HQ = ['UBS Asset Management (Americas) Inc.', 'JPMorgan Asset Management (UK) Limited',
            'Wellington Management Company LLP', 'Goldman Sachs Asset Management L.P.',
            'Barings LLC', 'Franklin Templeton']


def main():
    d = json.load(open(R + 'managers.json'))
    recs = d['records']
    unknown = sorted({r['entity'] for r in recs} - set(RESOLVE))
    if unknown:
        sys.exit('REFUSED: no decision recorded for: %s' % unknown)

    out = []
    for r in recs:
        name, stated, city, iso3, _ = RESOLVE[r['entity']]
        t = dict(r)
        t['entity'] = name
        if stated and stated != name:
            t['name_as_stated'] = stated
        else:
            t.pop('name_as_stated', None)
        t['entity_hq_city'] = city
        t['entity_hq_iso3'] = iso3
        # The vocabulary merge_links.py enforces says 'international body'; the agent wrote
        # 'international organisation', which is refused outright. Map it rather than widening
        # the vocabulary, which would need a SAY entry in app.js as well.
        if t.get('entity_type') == 'international organisation':
            t['entity_type'] = 'international body'
        q = (t.get('quote') or '').strip()
        if not q or len(q.split()) >= 15:
            t.pop('quote', None)
        out.append(t)

    json.dump({'records': out}, open(R + 'to_merge_mgr.json', 'w'), ensure_ascii=False, indent=1)
    seen = []
    for t in out:
        k = (t['cb_iso3'], t['entity'])
        if k in seen:
            continue
        seen.append(k)
        print('%-4s %-42s %-14s %s' % (t['cb_iso3'], t['entity'], t['entity_hq_city'] or '(centre)',
                                       t['entity_hq_iso3'] or '(unplaced)'))
    print('\n%d ties, %d firms needing a sourced head office next round:' % (len(out), len(NEEDS_HQ)))
    for n in NEEDS_HQ:
        print('   ' + n)
    print('\nwrote ' + R + 'to_merge_mgr.json')


if __name__ == '__main__':
    main()
