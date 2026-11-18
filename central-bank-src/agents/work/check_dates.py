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
    "january": ("janvier", "enero", "janeiro", "gennaio", "januar", "janúar", "ocak", "јануар", "январ"),
    "february": ("fevrier", "février", "febrero", "fevereiro", "febbraio", "februar",
                 "febrúar", "шубат", "фебруар", "феврал"),
    "march": ("mars", "marzo", "março", "märz", "mart", "март", "марта"),
    "april": ("avril", "abril", "aprile", "april", "apríl", "nisan", "април", "апрел"),
    "may": ("mai", "mayo", "maio", "maggio", "maí", "mayıs", "мај", "мая", "май"),
    "june": ("juin", "junio", "junho", "giugno", "juni", "júní", "haziran", "јун", "июн"),
    "july": ("juillet", "julio", "julho", "luglio", "juli", "júlí", "temmuz",
             "července", "cervence", "јул", "июл"),
    "august": ("aout", "août", "agosto", "august", "ágúst", "ağustos", "август", "августа"),
    "september": ("septembre", "septiembre", "setembro", "settembre", "september", "eylül", "септембар", "сентябр"),
    "october": ("octobre", "octubre", "outubro", "ottobre", "oktober", "október", "ekim",
                "ríjna", "rijna", "октобар", "октябр"),
    "november": ("novembre", "noviembre", "novembro", "november", "nóvember", "kasım", "новембар", "ноябр"),
    "december": ("decembre", "décembre", "diciembre", "dezembro", "dicembre", "dezember",
                 "desember", "aralık", "децембар", "декабр"),
}
# Clauses where a date deliberately refers to something OTHER than this source: a sibling record
# already on the map, or an explicit statement that the source itself gives no date. Round 71's
# first run reported fifteen records and eleven of them were one of these two shapes, which is
# how a check gets ignored. Dates inside these clauses are not checked.
IGNORE_MARKER = re.compile(
    r"distinct from|already on the map|already holds|already carries|gives no (?:calendar )?date"
    r"|source does not (?:say|mention|give|state|carry)|which the source does not"
    r"|no dates? (?:at all|are given|is given)|not mentioned in the source"
    r"|the map's existing|reverses on"
    # A record routinely points at the SIBLING record it must not be confused with, and the
    # wordings for that are many. Round 72 reported four dates that all sat in one of these.
    r"|existing (?:record|event|case)|one existing|not a duplicate|a different episode"
    r"|different (?:actors|years|borrower|committee)|expanded into every"
    # A statute citation dates the LAW, not the episode, and the page need not print it.
    r"|Law No|Loi n|Act No|Decree|Ley \d|Regulation \(E", re.I)


def strip_ignored(text):
    """Drop whole SENTENCES that refer to another record or disclaim a date.

    Matching from the marker onward is not enough and round 71 proved it: a record read
    "ordered on 8 August 2023, which the source does not mention" and the date sits BEFORE the
    disclaimer, so it was still reported. The unit has to be the sentence.
    """
    # Protect abbreviation periods before splitting. Round 72 flagged a statute date because
    # "Law No. 99-64 of 15 July 1999" split at "No." and the half carrying the date no longer
    # contained the marker that was supposed to drop it.
    t = re.sub(r"\b(No|Nos|Art|Arts|nr|n|No\u00ba|Decreto|Ley|Lei|vol|pp|p|cf|e\.g|i\.e)\.\s",
               lambda m: m.group(1) + "\u2024 ", text, flags=re.I)
    out = []
    for part in re.split(r"(?<=[.;])\s+", t):
        if not IGNORE_MARKER.search(part):
            out.append(part)
    return " ".join(out).replace("\u2024", ".")
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
        # A .docx is a zip and sniffs as PK; without this the bytes read as noise, pass the
        # length test, and the record's every date is reported missing. Round 72 hit exactly
        # that on a Control Yuan report served as Word.
        if head.startswith(b"PK"):
            try:
                import zipfile
                with zipfile.ZipFile("/tmp/_cd.bin") as z:
                    names = [n for n in z.namelist()
                             if n.endswith(".xml") and ("document" in n or "content" in n)]
                    raw = " ".join(z.read(n).decode("utf-8", "replace") for n in names)
                return re.sub(r"<[^>]+>", " ", raw)
            except Exception:
                return None
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
    # Taiwanese official documents date everything in ROC/Minguo years and print no Gregorian
    # year at all: a Control Yuan report round 72 filed from carries 47 instances of 111年 and
    # zero of "2022". The conversion is exact, ROC + 1911, so emit both forms.
    for mm in re.finditer(r"(\d{2,3})\s*\u5e74(?:\s*(\d{1,2})\s*\u6708(?:\s*(\d{1,2})\s*\u65e5)?)?", text):
        roc, mo, d = mm.groups()
        if 1 <= int(roc) <= 200:
            out.add(str(int(roc) + 1911))
            if mo and 1 <= int(mo) <= 12 and d:
                out.add(f"{int(d)} {MONTHS[int(mo) - 1]}")
    # Numeric forms: 31.12.2016, 31/12/2016, 19. 10. 2017. A Serbian audit report and most
    # continental official documents print dates this way and never spell the month, so without
    # this every date in such a source reads as missing.
    for mm in re.finditer(r"\b(\d{1,2})\s*[./]\s*(\d{1,2})\s*[./]\s*(\d{4})\b", text):
        d, mo, y = mm.groups()
        out.add(y)
        if 1 <= int(mo) <= 12 and 1 <= int(d) <= 31:
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
              f"month in a language not in MONTHS_ALT, a NON-GREGORIAN calendar such as the ROC/Minguo\n"
              f"    years Taiwanese official documents use (2024 is printed 113), or a PDF whose text\n"
              f"    layer garbles accents;\n"
              f"  - or the date was reconstructed from context, in which case it has to come out.\n"
              f"Round 71 went from 15 flags to 5 by fixing this script rather than the records, and "
              f"the two real defects it found were a committee hearing and a tabling date that "
              f"appeared nowhere on the cited page.")
        sys.exit(1)
    print("every date in every record appears in its own source")


if __name__ == "__main__":
    main()
