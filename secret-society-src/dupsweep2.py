#!/usr/bin/env python3
"""Sweep the whole map for internal duplicates: the same event written twice.

    python3 dupsweep2.py            list candidate pairs, highest score first

WHY A MAP-WIDE SWEEP AND NOT A PER-CELL ONE. Agents check duplicates against
`cells/<inf>_<bk>.txt`, which shows only the cell they are writing in. A record
that duplicates theirs but was coded into a DIFFERENT cell is invisible to that
check, and an agent put it plainly: "the cell files did not catch these, because
the held records sit in different cells from the ones I would have assigned.
Recommend future rounds grep data/cases.json directly."

It found a real pair that way: the Houthi Sana'a overflight-fees finding was
written in round 11 and again in round 12, same cell, same year, same UN
paragraph, and neither a title check nor a figure check caught it because the
titles share few tokens and the case carries no distinctive figure.

The three signals are the ones flagleads.py uses, weighted the same way: a
shared figure, a shared named body, and a shared single-case locator each count
only in proportion to how rare they are across the map.
"""
import json, re, os, sys, collections, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
RARE_FIG, RARE_BODY = 2, 3
sys.path.insert(0, HERE)
from flagleads import toks, figs, bodies, locs, rare_tokens  # noqa: E402


def main(thresh=0.95):
    cs = json.load(open(os.path.join(HERE, 'data', 'cases.json'), encoding='utf-8'))
    dff, dfb, dft = collections.Counter(), collections.Counter(), collections.Counter()
    F = []
    for i, c in enumerate(cs):
        blob = c.get('n', '') + ' ' + (c.get('d') or '') + ' ' + str(c.get('undone') or '')
        f = figs(blob)
        b = bodies(str(c.get('rank', ''))) | bodies(c.get('n', '')) | bodies((c.get('d') or '')[:400])
        l = locs(str(c.get('url', '')) + ' ' + str(c.get('cite', '')))
        F.append((i, c, toks(c.get('n', '')), f, b, l))
        for x in f: dff[x] += 1
        for x in b: dfb[x] += 1
        for x in toks(c.get('n', '')): dft[x] += 1

    # only compare within a country and year window: a duplicate is the same event
    by = collections.defaultdict(list)
    for rec in F:
        by[rec[1].get('c')].append(rec)
    pairs = []
    for c, group in by.items():
        for a in range(len(group)):
            for b2 in range(a + 1, len(group)):
                i, ci, ti, fi, bi, li = group[a]
                j, cj, tj_, fj, bj, lj = group[b2]
                ya, yb = ci.get('y'), cj.get('y')
                if isinstance(ya, int) and isinstance(yb, int) and abs(ya - yb) > 2:
                    continue
                s, why = 0.0, []
                if li & lj:
                    k = sorted(li & lj)[0]
                    # A SINGLE-CASE LOCATOR IS NOT ALWAYS SINGLE-CASE. Measured on the
                    # whole map: 120 locators, exactly one of them shared by two records,
                    # and that one firing was a false positive. DNA release 12750 sends two
                    # separate prosecutions to trial in one notice - Dumitrescu at the
                    # Prahova county council and Iacomi, mayor of Lehliu-Gara - and round
                    # 14 counted 81 monthly digests in ids 159-5,499, each covering many
                    # cases. So the locator keeps its full weight only where the two
                    # records name the same body; where they name different ones it is the
                    # multi-case-document shape and scores a fifth of that.
                    same_body = (str(ci.get('rank', '')).lower() == str(cj.get('rank', '')).lower())
                    s += 1.0 if same_body else 0.2
                    why.append('same %s %s%s' % (k + ('' if same_body else
                               ' BUT the two name different bodies, so it may be one notice '
                               'covering two prosecutions',)))
                ov = len(ti & tj_) / max(1, len(ti | tj_))
                if ov > 0:
                    s += ov; why.append('title overlap %.2f' % ov)
                for v in (fi & fj):
                    n = dff.get(v, 0)
                    # A company-wide disgorgement or settlement total is identical across
                    # every count of one enforcement action - that is, across records that
                    # ruling 11 makes DISTINCT. Measured as the single worst signal: it
                    # paired Oracle, Ultra Electronics and Asabri records that are all
                    # distinct. So a figure in three or more records scores nothing.
                    if n > 2:
                        continue
                    s += 0.6; why.append('rare figure %s (in %d)' % (v, n))
                for v in (bi & bj):
                    n = dfb.get(v, 0)
                    if n <= RARE_BODY:
                        s += 0.7; why.append('both name "%s" (in %d)' % (v, n))
                # A recurring title prefix naming the investigating agency or the
                # jurisdiction is near-zero evidence: "Odisha Vigilance:", "Mato Grosso do
                # Sul", "Tenaga Nasional" and "Bouches-du-Rhone" produced five clean false
                # positives. The useful rare token is a person or a payer, so require two.
                shared_rare = rare_tokens(dft, ci.get('n', '')) & rare_tokens(dft, cj.get('n', ''))
                if len(shared_rare) >= 2:
                    for v in sorted(shared_rare)[:3]:
                        s += 0.55; why.append('both titles use "%s" (in %d titles)' % (v, dft[v]))
                # Same supplier and same price but a different named buyer is DISTINCT:
                # one CAMEC backhoe at P13,950,000 sold to two municipalities is two cases.
                if (bi & bj) and not (bi == bj) and (fi & fj) and ci.get('rank') != cj.get('rank'):
                    s -= 0.4; why.append('different body named, so a shared price is weak')
                if s >= thresh:
                    pairs.append((s, i, j, '; '.join(why[:3])))
    pairs.sort(reverse=True)
    print('%d candidate duplicate pairs at score >= %.2f\n' % (len(pairs), thresh))
    for s, i, j, why in pairs:
        print('  score %.2f  %s' % (s, why))
        print('    %d [%s/%s %s] %s' % (i, cs[i].get('inf'), cs[i].get('bk'), cs[i].get('y'), cs[i]['n'][:72]))
        print('    %d [%s/%s %s] %s' % (j, cs[j].get('inf'), cs[j].get('bk'), cs[j].get('y'), cs[j]['n'][:72]))
        print('    added: %s / %s\n' % (cs[i].get('added'), cs[j].get('added')))
    return pairs


if __name__ == '__main__':
    main(float(sys.argv[1]) if len(sys.argv) > 1 else 0.95)
