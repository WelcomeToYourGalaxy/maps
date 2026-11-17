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
# Three other indices are also printed as "NN of 100": the World Bank control of
# corruption score, the Corruption Perceptions Index and the financial secrecy
# score. (?<![\d.]) only keeps the matcher off the decimal forms ("72.4 of 100");
# the integer forms ("financial secrecy is 77 of 100") still match, and taking the
# first match blindly made this tool report 17 paragraphs that were in fact right
# -- and, worse, would have had --fix overwrite another index with the exposure
# score. So a match is disqualified when its OWN sentence names another index.
# The window is the clause since the last full stop, not a fixed number of
# characters: Panama states a secrecy score in one sentence and its exposure
# score in the next, and a fixed lookback swallows the sentence boundary.
OTHER_INDEX = re.compile(r'corruption|secrecy|Perceptions', re.I)


def find_score(text):
    """First "NN of 100" in text that is the exposure score, or None."""
    for m in SCORE.finditer(text):
        clause = text[:m.start()].rsplit('.', 1)[-1]
        if not OTHER_INDEX.search(clause):
            return m
    return None
# "leaving it less exposed than 95 percent of the places measured"
PARA_PCTL = re.compile(r'\b(less|more)(?P<mid> exposed than )(\d+)(?P<tail> ?(?:percent|per cent|%))', re.I)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    boxes = json.load(open(sys.argv[1]))
    # Two input shapes. The original was a dump of RENDERED box text, matched with
    # PANEL below; nothing has written one for several rounds, so the check was
    # reporting "checked 0" and passing. agents/work/mk_scores.py now emits the
    # page's own arithmetic as {"p:ISO": {score, groups, pctl_dir, pctl_share}},
    # and that is the shape to prefer.
    computed = bool(boxes) and isinstance(next(iter(boxes.values())), dict)
    # ROUND 71: refuse the legacy shape instead of passing on it. Round 70 found this script
    # had reported "checked 0 country paragraphs" and then "no stale figures" for several
    # rounds while 189 paragraphs went unverified, and fixed it by ADDING the computed shape
    # above. The blind path itself was left in place: PANEL below still matches the uppercase
    # heading ULTERIOR INFLUENCE, ALL AROUND, which app.js stopped printing when the heading
    # went sentence case and which now appears nowhere in this repo except this file, mk_scores.py
    # and the rendered dumps in r57-r63. So a boxes.json passed here again would match nothing,
    # check nothing, and print a clean run -- the same silent pass, waiting for the next caller.
    # A check that cannot fire must be loud about it, because a check that prints "ok" gets
    # BELIEVED, which is worse than one that cries wolf.
    if not computed:
        sys.exit("check_scores.py: this input is a dump of rendered box text, and the panel "
                 "heading it would have to match is no longer printed by app.js, so this run "
                 "would verify nothing and report a clean pass.\n"
                 "Run:  python3 agents/work/mk_scores.py   then pass agents/work/scores.json")
    fix = '--fix' in sys.argv[1:]
    wr = json.load(open(WR))

    stale_score, stale_pctl, no_panel, checked = [], [], [], 0

    for k, para in wr.items():
        if not k.startswith('p:'):
            continue                      # only country boxes carry an exposure score
        box = boxes.get(k)
        if box is None:
            if find_score(para):
                no_panel.append(k)        # paragraph quotes a score the map no longer shows
            continue
        if computed:
            score = int(box['score'])
            want_pctl = (box.get('pctl_dir'), box.get('pctl_share'))
        else:
            m = PANEL.search(box)
            if not m:
                if find_score(para):
                    no_panel.append(k)
                continue
            score = int(m.group(1))
            want_pctl = None
        checked += 1
        new = para

        ms = find_score(new)
        if ms and int(ms.group(1)) != score:
            stale_score.append((k, int(ms.group(1)), score))
            new = new[:ms.start()] + str(score) + new[ms.end():]

        if computed:
            mp = want_pctl if want_pctl and want_pctl[0] else None
        else:
            mp = PCTL.search(box)
        mq = PARA_PCTL.search(new)
        if mp and mq:
            want_dir, want_pct = ((mp[0].lower(), int(mp[1])) if computed
                                  else (mp.group(1).lower(), int(mp.group(2))))
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
