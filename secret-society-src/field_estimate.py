#!/usr/bin/env python3
"""Estimate of who infiltrates and what they get into, for the whole field since 2000.

    python3 field_estimate.py     -> writes data/field_estimate.json

Nobody has counted this field, so this is an estimate. The published anchors below are
real; the ranges around them and the coverage assumptions are the map author's judgement.
A simulation draws each uncertain input from its range to give a likely range per type.
"""
import json, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
INF = ['crime', 'corp', 'state', 'movement', 'faith', 'money', 'elite', 'lodge', 'lender']
BK = ['security', 'company', 'cabinet', 'legis', 'exec', 'court', 'finance', 'intl']

# Global Organized Crime Index 2025, world average score out of 10
GOCI_EMBEDDED, GOCI_PRIVATE = 6.04, 4.89
# Stanford FCPA Clearinghouse: DOJ and SEC actions a year, ten-year average 2015-2024
FCPA_PER_YEAR = 36
# CSIS: 224 reported Chinese espionage incidents aimed at the US, 2003 to February 2023
CHINA_PER_YEAR = 224 / 20
# CSIS targets, % of incidents
CSIS = {'company': 54, 'security': 29, 'government': 17}
# OECD Foreign Bribery Report 2014, 427 cases, % by recipient
OECD = {'company': 27, 'security': 11 + 6, 'cabinet': 7 + 2.5, 'exec': 2.5}


def mix(cases, inf, rnd=None):
    # The map's own mix stands in where no outside count exists, so it is treated as rough:
    # each share is moved up or down by a random factor before use.
    c = collections.Counter(x['bk'] for x in cases if x['inf'] == inf)
    v = {b: c[b] * (rnd.lognormvariate(0, .4) if rnd else 1) for b in BK}
    t = sum(v.values()) or 1
    return {b: v[b] / t for b in BK}


def draw(cases, n_map, rnd):
    crime_per_corp = (GOCI_EMBEDDED / GOCI_PRIVATE) * rnd.uniform(0.8, 1.3)
    other_states = rnd.uniform(1.5, 3)      # China's incidents times this = all states
    state_per_corp = CHINA_PER_YEAR * other_states / FCPA_PER_YEAR
    big = {'crime': crime_per_corp, 'corp': 1, 'state': state_per_corp}
    t = sum(big.values())
    big = {k: v / t for k, v in big.items()}
    # Smaller kinds: the map's own count since 2000 scaled by how much of each it likely has
    cov_big = rnd.uniform(.05, .15)
    cov_mov = rnd.uniform(.10, .25)
    cov_small = rnd.uniform(.20, .50)
    all_big = sum(n_map[k] for k in big) / cov_big
    small = {'movement': n_map['movement'] / cov_mov}
    for k in ('faith', 'money', 'elite', 'lodge', 'lender'):
        small[k] = n_map[k] / cov_small
    total = all_big + sum(small.values())
    share = {k: v * all_big / total for k, v in big.items()}
    share.update({k: v / total for k, v in small.items()})
    # What they get into
    corp_known = {b: OECD.get(b, 0) / 100 for b in BK}
    rest = 1 - sum(corp_known.values())
    m = mix(cases, 'corp', rnd)
    tgt = {'corp': {b: corp_known[b] + rest * m[b] for b in BK}}
    w = rnd.uniform(.3, .7)                 # weight on CSIS against the map's mix for states
    ms = mix(cases, 'state', rnd)
    civil = {b: ms[b] for b in BK if b not in ('company', 'security')}
    ct = sum(civil.values())
    csis = {b: 0 for b in BK}
    csis['company'] = CSIS['company'] / 100
    csis['security'] = CSIS['security'] / 100
    for b, v in civil.items():
        csis[b] = CSIS['government'] / 100 * v / ct
    tgt['state'] = {b: w * csis[b] + (1 - w) * ms[b] for b in BK}
    for k in INF:
        if k not in tgt:
            tgt[k] = mix(cases, k, rnd)
    into = {b: sum(share[k] * tgt[k][b] for k in INF) for b in BK}
    return share, into


def main():
    cases = [c for c in json.load(open(os.path.join(HERE, 'data', 'cases.json'))) if c['y'] >= 2000]
    n_map = collections.Counter(c['inf'] for c in cases)
    rnd = random.Random(2026)
    runs = [draw(cases, n_map, rnd) for _ in range(20000)]
    def summ(keys, idx):
        out = {}
        for k in keys:
            v = sorted(r[idx][k] * 100 for r in runs)
            out[k] = {'mid': round(v[len(v) // 2], 1), 'lo': round(v[len(v) // 10], 1), 'hi': round(v[len(v) * 9 // 10], 1)}
        return out
    res = {'inf': summ(INF, 0), 'bk': summ(BK, 1)}
    json.dump(res, open(os.path.join(HERE, 'data', 'field_estimate.json'), 'w'), indent=1)
    for g in res:
        print(g, round(sum(x['mid'] for x in res[g].values()), 1))
        for k, x in res[g].items():
            print('  ', k, x)


if __name__ == '__main__':
    main()
