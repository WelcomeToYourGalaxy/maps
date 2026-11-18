#!/usr/bin/env python3
"""Refuse a shard build that lost records, before it is committed.

A register that answers with half a file must not quietly delete data, and
the failure is silent by nature: the build succeeds, the counts fall, and
the page shows fewer municipalities than it did last month with nothing
said. So each country is compared against what it built last time.

Two floors, and the second one matters more than it looks. A fall below
80% of the previous build fails the run; so does an absolute count under
50 for a country. This started as a flat 1,000 per country, which was a
sound guard while the countries were France and Italy and is a permanent
veto on a province of 341 municipalities.

    python3 -I tools/check_muni_build.py          # against HEAD
    python3 -I tools/check_muni_build.py --new    # first build, no compare
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FLOOR_ABS = 50
FLOOR_REL = 0.8


def previous():
    try:
        out = subprocess.check_output(
            ["git", "-C", ROOT, "show", "HEAD:muni/index.json"], text=True,
            stderr=subprocess.DEVNULL)
        return json.loads(out).get("counts", {})
    except Exception as e:
        print("no previous index to compare against:", e)
        return {}


def main():
    new = json.load(open(os.path.join(ROOT, "muni", "index.json")))["counts"]
    old = {} if "--new" in sys.argv else previous()
    bad = []
    for iso, c in sorted(new.items()):
        n = c["shipped"]
        if n < FLOOR_ABS:
            bad.append(f"{iso}: {n} records, under the floor of {FLOOR_ABS}")
        o = (old.get(iso) or {}).get("shipped")
        if o and n < FLOOR_REL * o:
            bad.append(f"{iso}: {n} records against {o} in the last build")
    for iso in sorted(old):
        if iso not in new:
            bad.append(f"{iso}: built last time and absent now")
    if bad:
        print("\n".join(bad))
        return 1
    print("counts: " + ", ".join(f"{k} {v['shipped']:,}"
                                 for k, v in sorted(new.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
