#!/usr/bin/env python3
"""Catch writeup paragraphs that quote a stale exposure score or percentile.

The exposure score is recomputed from the data on every build, so adding a case
or an event moves the score of every country it touches, and any paragraph that
states the old number is then wrong. Round 50 added records to 25 countries and
left 22 paragraphs quoting a score one or two points out; audit_data.py and
check_drafts.py both passed, because neither compares a figure in a paragraph
against the same figure in the box.

Usage:
    python3 check_scores.py <boxes.json>          report only
    python3 check_scores.py <boxes.json> --fix    rewrite the stale figures in place

Run it after every round, before pushing.

Two traps are handled. A paragraph may also carry a financial secrecy score
written as "72.4 of 100", so the score pattern refuses a figure preceded by a
digit or a decimal point. And the percentile is printed in the box as a
percentage with its direction ("Less exposed than 96% of the 194 places"), so
both the number and the direction word are compared -- a country that crossed
the midpoint needs "more" where the paragraph says "less".
"""
import json, re, sys, os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
WR = os.path.join(A, 'writeups.json')

# the authoritative figures, as the country box prints them
PANEL = re.compile(r'ULTERIOR INFLUENCE, ALL AROUND\s*\n+\s*(\d+) of 100 \((\d+) of (\d+)\)')
PCTL  = re.compile(r'(Less|More) exposed than (\d+)% of the (\d+) places')
# the exposure score as a paragraph states it: the first bare "NN of 100".
# (?<![\d.]) keeps it off "72.4 of 100" and "3.99 of 10".
SCORE = re.compile(r'(?<![\d.])(\d+)(?= of 100)')
# "leaving it less exposed than 95 percent of the places measured"
PARA_PCTL = re.compile(r'\b(less|more)(?P<mid> exposed than )(\d+)(?P<tail> ?(?:percent|per cent|%))', re.I)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    boxes = json.load(open(sys.argv[1]))
    fix = '--fix' in sys.argv[1:]
    wr = json.load(open(WR))

    stale_score, stale_pctl, no_panel, checked = [], [], [], 0

    for k, para in wr.items():
        if not k.startswith('p:'):
            continue                      # only country boxes carry an exposure score
        box = boxes.get(k)
        if box is None:
            continue
        m = PANEL.search(box)
        if not m:
            if SCORE.search(para):
                no_panel.append(k)        # paragraph quotes a score the box no longer shows
            continue
        checked += 1
        score = int(m.group(1))
        new = para

        ms = SCORE.search(new)
        if ms and int(ms.group(1)) != score:
            stale_score.append((k, int(ms.group(1)), score))
            new = new[:ms.start()] + str(score) + new[ms.end():]

        mp = PCTL.search(box)
        mq = PARA_PCTL.search(new)
        if mp and mq:
            want_dir, want_pct = mp.group(1).lower(), int(mp.group(2))
            got_dir, got_pct = mq.group(1).lower(), int(mq.group(3))
            if (got_dir, got_pct) != (want_dir, want_pct):
                stale_pctl.append((k, f'{got_dir} {got_pct}%', f'{want_dir} {want_pct}%'))
                new = (new[:mq.start()] + want_dir + mq.group('mid') + str(want_pct)
                       + mq.group('tail') + new[mq.end():])

        if fix and new != para:
            wr[k] = new

    print(f'checked {checked} country paragraphs against their box')
    if stale_score:
        print(f'\n{len(stale_score)} paragraphs quote a stale exposure score:')
        for k, was, now in stale_score:
            print(f'  {k:10s} says {was:3d} of 100, the box says {now:3d}')
    if stale_pctl:
        print(f'\n{len(stale_pctl)} paragraphs quote a stale percentile:')
        for k, was, now in stale_pctl:
            print(f'  {k:10s} says "{was}", the box says "{now}"')
    if no_panel:
        print(f'\n{len(no_panel)} paragraphs quote a score for a place whose box shows none '
              f'(check by hand, not rewritten): {" ".join(no_panel)}')
    if not (stale_score or stale_pctl):
        print('no stale figures')

    if fix and (stale_score or stale_pctl):
        json.dump(wr, open(WR, 'w'), indent=1, ensure_ascii=False)
        print(f'\nrewrote {len(stale_score) + len(stale_pctl)} figures in writeups.json')
    elif stale_score or stale_pctl:
        print('\nrun again with --fix to rewrite them')
    return 1 if (stale_score or stale_pctl) else 0


if __name__ == '__main__':
    sys.exit(main())
