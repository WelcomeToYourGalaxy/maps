"""Where infiltration comes from, derived from this map's own records.

Two layers are built here:

  countries()  how much infiltration ORIGINATES in each country, for the
               country-shading lens, plus how many other countries the
               organisations based there have reached.

  entities()   the same question one level down: which named organisations,
               companies and networks reach into the most institutions.

WHAT THIS CAN AND CANNOT SAY. The map's `c` field is where an infiltration
LANDED, never where it came from. The only origin this data carries is the home
country recorded for a named organisation in orgs.json, so these layers cover
the records that name one and say so plainly. They are a measure of what has
been documented here, not of the whole world: a country with heavy domestic
coverage (Italy, Romania) will show many records and little foreign reach, and
a country whose networks operate abroad (the United States, Russia) the reverse.

FIVE ORGANISATION DOTS ARE AGGREGATORS, not organisations, and their country is
where a dot was placed rather than an origin. Left uncorrected they put Andorra
among the top ten infiltrating countries in the world. They are handled here:
"""

# origin corrections for the aggregator dots, and the reason for each
ORIGIN_FIX = {
    # gathers cases of PRC officials working through people in other countries;
    # its dot sits in Montreal because that is where several of the cases are.
    'prc_state': 'China',
}
# aggregators that have no single origin and are therefore left unattributed
NO_ORIGIN = {
    # "several states" - US, Russian, Chinese and Gulf cases in one dot
    'foreign_state',
    # "other grand lodges" - a number of national lodges, no single seat
    'freemasonry',
}


def _origin(org, og):
    """The home country of an infiltrating organisation, or None."""
    if org in NO_ORIGIN:
        return None
    if org in ORIGIN_FIX:
        return ORIGIN_FIX[org]
    o = og.get(org)
    return (o or {}).get('c') or None


def countries(cases, orgs, names):
    """Per-country origin counts, keyed to the country names the map uses."""
    og = {o['k']: o for o in orgs}
    rec = {k: 0 for k in names}          # records originating here
    abroad = {k: set() for k in names}   # other countries reached from here
    at_home = {k: 0 for k in names}      # records landing in the same country
    orgset = {k: set() for k in names}
    attributed = unattributed = 0
    for c in cases:
        k = c.get('org')
        home = _origin(k, og) if k else None
        if not home or home not in rec:
            unattributed += 1
            continue
        attributed += 1
        rec[home] += 1
        orgset[home].add(k)
        if c['c'] == home:
            at_home[home] += 1
        else:
            abroad[home].add(c['c'])
    return {'rec': rec, 'abroad': {k: sorted(v) for k, v in abroad.items()},
            'at_home': at_home, 'orgs': {k: sorted(v) for k, v in orgset.items()},
            'attributed': attributed, 'unattributed': unattributed}


def entities(cases, orgs):
    """Named organisations ranked by how far they reach, from case records only."""
    og = {o['k']: o for o in orgs}
    acc = {}
    for c in cases:
        k = c.get('org')
        if not k or k not in og:
            continue
        e = acc.setdefault(k, {'k': k, 'recs': 0, 'cs': set(), 'bk': {}, 'y0': 9999, 'y1': 0})
        e['recs'] += 1
        e['cs'].add(c['c'])
        e['bk'][c.get('bk')] = e['bk'].get(c.get('bk'), 0) + 1
        y = c.get('y')
        if isinstance(y, int):
            e['y0'] = min(e['y0'], y); e['y1'] = max(e['y1'], y)
    out = []
    for k, e in acc.items():
        o = og[k]
        home = _origin(k, og)
        out.append({'k': k, 'n': o['n'], 'ty': o.get('ty'), 'home': home,
                    'agg': k in NO_ORIGIN or k in ORIGIN_FIX,
                    'recs': e['recs'], 'nc': len(e['cs']),
                    'cs': sorted(e['cs']),
                    'abroad': sorted(x for x in e['cs'] if home and x != home),
                    'bk': e['bk'],
                    'yr': [e['y0'], e['y1']] if e['y1'] else None})
    # the honest ordering is reach first, then volume
    out.sort(key=lambda r: (-r['nc'], -r['recs']))
    return out
