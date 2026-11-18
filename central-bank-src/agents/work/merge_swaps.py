#!/usr/bin/env python3
"""Merge swap-line records into swaps.json, refusing duplicates and unreadable sources.

WHY THIS EXISTS. merge_links.py handles cases, career moves, events and network ties; swaps have
been merged by hand or by round-specific scripts since round 4, which is how a row gets a
duplicate. Round 76 added 41 records across six providers and three multilateral arrangements, so
it needed doing properly once.

The duplicate key is (provider_iso3, counterparty_iso3, kind, signed_or_renewed). That is
deliberately tighter than provider-and-counterparty alone, because a renewed line is a real second
record on this row and collapsing renewals would lose the thing the row is for -- when a line was
signed and when it lapsed.

    python3 agents/work/merge_swaps.py --dry agents/work/r76/swaps_providers.json
    python3 agents/work/merge_swaps.py       agents/work/r76/swaps_providers.json

Refuses a record whose source_url cannot be read, with --url-ok to waive after a hand read, on
merge_links.py's pattern.
"""
import json, os, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.dirname(os.path.dirname(HERE))
REQ = ("provider_cb", "provider_iso3", "counterparty_cb", "counterparty_iso3", "kind",
       "source_title", "source_url")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"

def readable(u, waived):
    if u in waived:
        return True, "waived"
    try:
        r = urllib.request.Request(u, headers={"User-Agent": UA})
        with urllib.request.urlopen(r, timeout=40) as f:
            return (f.status or 200) < 400, str(f.status)
    except urllib.error.HTTPError as e:
        return False, "HTTP %s" % e.code
    except Exception as e:
        return False, type(e).__name__

def apply_status_updates(rows, files, dry):
    """Apply record-level status changes from agent output.

    Matched on (counterparty_iso3, provider name substring, signed_or_renewed). A change is
    applied only when exactly one record matches: zero matches means the agent was aiming at a
    record that is not there, and two means the key does not identify a record, and in both cases
    the right answer is to stop and look rather than to guess which one was meant. An entry whose
    new_status begins "no change" records a finding and is never written.
    """
    applied, noop, miss, amb = [], [], [], []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        for u in (d.get("status_updates") or []):
            iso, prov = u.get("counterparty_iso3"), (u.get("provider") or "")
            want = u.get("match_signed_or_renewed")
            new = (u.get("new_status") or "").strip()
            hits = [r for r in rows
                    if r.get("counterparty_iso3") == iso
                    and prov.lower() in (r.get("provider_cb") or "").lower()
                    and (r.get("signed_or_renewed") or None) == (want or None)]
            if len(hits) != 1:
                (miss if not hits else amb).append((iso, prov, want, len(hits)))
                continue
            r = hits[0]
            if new.lower().startswith("no change"):
                noop.append((iso, want)); continue
            if (r.get("status") or "") == new:
                noop.append((iso, want)); continue
            applied.append((iso, want, (r.get("status") or "")[:28], new[:46]))
            if not dry:
                r["status"] = new
                r["status_source_url"] = u.get("source_url")
    print("\n%s %d status changes:" % ("WOULD APPLY" if dry else "APPLIED", len(applied)))
    for iso, when, was, now in applied:
        print("  %-4s %-12s %-28s -> %s" % (iso, when or "(null)", was or "(blank)", now))
    if noop:
        print("\nNO CHANGE, recorded only %d: %s" % (len(noop), " ".join(
            "%s/%s" % (a, b or "null") for a, b in noop)))
    if miss:
        print("\nNO RECORD MATCHES %d -- look at these by hand:" % len(miss))
        for iso, prov, when, n in miss:
            print("  %-4s %-26s %s" % (iso, prov[:26], when))
    if amb:
        print("\nKEY MATCHES MORE THAN ONE RECORD %d -- refused:" % len(amb))
        for iso, prov, when, n in amb:
            print("  %-4s %-26s %-12s %d records" % (iso, prov[:26], when, n))
    return bool(applied)


def main(argv):
    dry = "--dry" in argv
    waived = {a.split("=", 1)[1] for a in argv if a.startswith("--url-ok=")}
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        sys.exit(__doc__)

    p = os.path.join(CB, "agents", "swaps.json")
    raw = json.load(open(p, encoding="utf-8"))
    rows = raw if isinstance(raw, list) else raw[list(raw)[0]]
    key = lambda r: (r.get("provider_iso3"), r.get("counterparty_iso3"), r.get("kind"),
                     str(r.get("signed_or_renewed") or ""))
    have = {key(r) for r in rows}

    filed, dupes, refused, bad = [], [], [], []
    seen_now = set()
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        for r in (d.get("records") or []):
            miss = [k for k in REQ if not r.get(k)]
            if miss:
                bad.append((r.get("counterparty_iso3"), "missing " + ", ".join(miss))); continue
            k = key(r)
            if k in have or k in seen_now:
                dupes.append((r.get("provider_iso3"), r.get("counterparty_iso3"))); continue
            ok, why = readable(r["source_url"], waived)
            if not ok:
                refused.append((r.get("counterparty_iso3"), why, r["source_url"])); continue
            seen_now.add(k); filed.append(r)

    print("read %d candidate records" % sum(len(json.load(open(f, encoding="utf-8")).get("records") or []) for f in files))
    print("\n%s %d swap records:" % ("WOULD FILE" if dry else "FILED", len(filed)))
    for r in filed:
        print("  %-4s <- %-34s %-13s %s" % (r.get("counterparty_iso3"), (r.get("provider_cb") or "")[:34],
                                            r.get("kind"), r.get("status") or ""))
    if dupes:
        print("\nALREADY FILED, skipped %d: %s" % (len(dupes), " ".join(
            "%s<-%s" % (b, a) for a, b in dupes)))
    if refused:
        print("\nREFUSED, source not readable %d:" % len(refused))
        for iso, why, u in refused:
            print("  %-4s %-10s %s" % (iso, why, u))
        print("  re-run with --url-ok=<url> after reading it by hand")
    if bad:
        print("\nMALFORMED %d:" % len(bad))
        for iso, why in bad:
            print("  %-4s %s" % (iso, why))

    touched = apply_status_updates(rows, files, dry)

    if dry:
        print("\n(dry run; nothing written)")
        return 0
    if filed or touched:
        rows.extend(filed)
        json.dump(raw, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("\nwritten: swaps.json now holds %d records. Rebuild, then run audit_data.py and "
              "coverage.py." % len(rows))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
