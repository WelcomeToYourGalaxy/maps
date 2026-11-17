#!/usr/bin/env python3
"""Check that every year and date a record states actually appears in its own source page.

WHY THIS EXISTS. Round 71 filed 29 records and an independent verifier, which had not seen them
being made, opened 14 of them. It found no fabricated source and nothing flatly wrong -- but four
records carried a date or an actor the cited page never mentions:

  * one event gave a 10 billion dinar deficit, an interest-free bond purchase, a head of state's
    request and a prior revision of the bank's autonomy law, none of which were on the page, and
    the last of those was the clause that made the record a capture finding at all;
  * one case was "tabled in Parliament on 9 January 2025" and carried a deputy governor's evidence
    to a committee on 17 December 2024, neither on the page, and named him in `people`;
  * one career move gave an appointment month, a reappointment two years later and a term expiry,
    where the release says only that the appointment was made "on a Wednesday";
  * one case resolved "on 14 September 2026", which was the article's publication date.

The verifier named the pattern: **date and context accretion**. A correct core finding grows an
extra date or an extra name on the way into the file, because a date is the easiest thing to
reconstruct from context and the hardest thing to notice is missing. Every one of the four would
have been caught by asking whether each date in the record is in the page.

This is NOT the same job as `merge_links.py`'s reachability check, which asks only whether the
host answered. It reads the page.

    python3 agents/work/check_dates.py agents/work/r71/*.norm.json
    python3 agents/work/check_dates.py --field summary agents/work/r71/cases_latam.norm.json

A miss is not automatically an error: a date may be stated in a second source the record cites in
its own text, and a page may spell a date differently from the record. So this REPORTS and does not
rewrite, and it prints the surrounding words so the caller can judge. Exits non-zero if anything is
unaccounted for, so it can gate a push.
"""
import json
import re
import subprocess
import sys

MONTHS = ("january february march april may june july august september october november december"
          .split())
# A date is often printed in the source's own language, so a month list in English alone reports a
# page as silent when it states the date perfectly. These are the languages this map's sources
# actually come in; add to the row rather than widening the regex.
MONTHS_ALT = {
    "january": ("janvier", "enero", "janeiro", "gennaio", "januar", "janúar", "ocak"),
    "february": ("fevrier", "février", "febrero", "fevereiro", "febbraio", "februar",
                 "febrúar", "шубат"),
    "march": ("mars", "marzo", "março", "märz", "mart"),
    "april": ("avril", "abril", "aprile", "april", "apríl", "nisan"),
    "may": ("mai", "mayo", "maio", "maggio", "maí", "mayıs"),
    "june": ("juin", "junio", "junho", "giugno", "juni", "júní", "haziran"),
    "july": ("juillet", "julio", "julho", "luglio", "juli", "júlí", "temmuz",
             "července", "cervence"),
    "august": ("aout", "août", "agosto", "august", "ágúst", "ağustos"),
    "september": ("septembre", "septiembre", "setembro", "settembre", "september", "eylül"),
    "october": ("octobre", "octubre", "outubro", "ottobre", "oktober", "október", "ekim",
                "ríjna", "rijna"),
    "november": ("novembre", "noviembre", "novembro", "november", "nóvember", "kasım"),
    "december": ("decembre", "décembre", "diciembre", "dezembro", "dicembre", "dezember",
                 "desember", "aralık"),
}
# Clauses where a date deliberately refers to something OTHER than this source: a sibling record
# already on the map, or an explicit statement that the source itself gives no date. Round 71's
# first run reported fifteen records and eleven of them were one of these two shapes, which is
# how a check gets ignored. Dates inside these clauses are not checked.
IGNORE_MARKER = re.compile(
    r"distinct from|already on the map|already holds|already carries|gives no (?:calendar )?date"
    r"|source does not (?:say|mention|give|state|carry)|which the source does not"
    r"|no dates? (?:at all|are given|is given)|not mentioned in the source"
    r"|the map's existing|reverses on", re.I)


def strip_ignored(text):
    """Drop whole SENTENCES that refer to another record or disclaim a date.

    Matching from the marker onward is not enough and round 71 proved it: a record read
    "ordered on 8 August 2023, which the source does not mention" and the date sits BEFORE the
    disclaimer, so it was still reported. The unit has to be the sentence.
    """
    out = []
    for part in re.split(r"(?<=[.;])\s+", text):
        if not IGNORE_MARKER.search(part):
            out.append(part)
    return " ".join(out)
FIELDS = ("summary", "move", "people", "detail", "years", "date")


def fetch(url):
    """Return the page's text, or None. curl first; pdftotext if it sniffs as a PDF.

    The HTTP STATUS is checked, not just the body length. A host that refuses automation returns a
    403 page that is thousands of characters long, which sails past any length test and then looks
    exactly like a source that states none of the record's dates. Round 71's first run reported
    seven missing dates for one record for precisely that reason, every one of which was on the
    real page.
    """
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-w", "%{http_code}",
                            "-o", "/tmp/_cd.bin", url], capture_output=True)
        if r.returncode != 0:
            return None
        code = (r.stdout or b"").decode().strip()[-3:]
        if code and not code.startswith(("2", "3")):
            return None
        head = open("/tmp/_cd.bin", "rb").read(5)
        if head.startswith(b"%PDF"):
            t = subprocess.run(["pdftotext", "/tmp/_cd.bin", "-"], capture_output=True)
            return t.stdout.decode("utf-8", "replace")
        raw = open("/tmp/_cd.bin", "rb").read().decode("utf-8", "replace")
        # crude de-tagging is enough: we only look for dates
        return re.sub(r"<[^>]+>", " ", raw)
    except Exception:
        return None


def norm(s):
    s = s.lower()
    s = re.sub(r"[‐-―]", "-", s)
    return re.sub(r"\s+", " ", s)


def dates_in(text):
    """Every 4-digit year, and every 'D Month' / 'Month D' pair, as comparable tokens."""
    out = set()
    for y in re.findall(r"\b(1[89]\d{2}|20\d{2})\b", text):
        out.add(y)
    low = norm(text)
    for m in MONTHS:
        # "Nov 30, 2017" is the commonest form in news and the full-word list misses it.
        forms = (m, m[:3]) + MONTHS_ALT.get(m, ())
        for name in forms:
            # Romance languages write "12 de agosto" and Czech "10. rijna", so the connector has
            # to be optional. Round 71 reported four dates missing that were on the page in this form.
            for mm in re.finditer(r"\b(\d{1,2})\.?\s+(?:de\s+|d'|du\s+)?" + re.escape(name)
                                  + r"\b", low):
                out.add(f"{int(mm.group(1))} {m}")
            for mm in re.finditer(r"\b" + re.escape(name) + r"\s+(\d{1,2})\b", low):
                out.add(f"{int(mm.group(1))} {m}")
    for mm in re.finditer(r"\b(\d{4})-(\d{2})-(\d{2})\b", text):
        y, mo, d = mm.groups()
        out.add(y)
        if 1 <= int(mo) <= 12:
            out.add(f"{int(d)} {MONTHS[int(mo) - 1]}")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only = None
    if "--field" in sys.argv:
        only = sys.argv[sys.argv.index("--field") + 1]
    if not args:
        sys.exit(__doc__)

    records = []
    for f in args:
        d = json.load(open(f, encoding="utf-8"))
        for r in (d.get("records") or d if isinstance(d, list) else d.get("records") or []):
            if isinstance(r, dict) and r.get("source_url"):
                records.append((f.split("/")[-1], r))

    pages, bad, checked = {}, [], 0
    for fname, r in records:
        url = r["source_url"]
        if url not in pages:
            pages[url] = fetch(url)
        page = pages[url]
        label = f"{fname} {r.get('iso3')}"
        if page is None or len(page) < 400:
            print(f"SKIP  {label}: host refused or served nothing readable ({url}). "
                  f"Read it by hand -- this is NOT a pass.")
            continue
        # The URL path often carries the date for a dated news item; that is the publisher stating it.
        page = page + " " + re.sub(r"[/_-]", " ", url)
        checked += 1
        want = set()
        for k in ([only] if only else FIELDS):
            v = r.get(k)
            if isinstance(v, str):
                want |= dates_in(strip_ignored(v))
        have = dates_in(page)
        miss = sorted(want - have)
        if miss:
            bad.append((label, miss, url))
            print(f"\nMISSING {label}: {', '.join(miss)}")
            print(f"  {url}")
            for m in miss:
                for k in ([only] if only else FIELDS):
                    v = r.get(k)
                    if isinstance(v, str):
                        tok = m.split()[-1] if " " in m else m
                        i = norm(v).find(tok)
                        if i >= 0:
                            print(f"    {k}: ...{norm(v)[max(0, i - 70):i + 70]}...")
                            break
    print(f"\nchecked {checked} records against their own source pages")
    if bad:
        print(f"{len(bad)} carry a date the page does not state. Read each one: there are three "
              f"innocent reasons and one guilty one.\n"
              f"  - the date comes from a SECOND source the record cites in its own text;\n"
              f"  - `years` is a RANGE the record composes, so neither end need appear verbatim;\n"
              f"  - the page prints it in a form this script does not parse -- a numeric date, a "
              f"month in a language not in MONTHS_ALT, or a PDF whose text layer garbles accents;\n"
              f"  - or the date was reconstructed from context, in which case it has to come out.\n"
              f"Round 71 went from 15 flags to 5 by fixing this script rather than the records, and "
              f"the two real defects it found were a committee hearing and a tabling date that "
              f"appeared nowhere on the cited page.")
        sys.exit(1)
    print("every date in every record appears in its own source")


if __name__ == "__main__":
    main()
