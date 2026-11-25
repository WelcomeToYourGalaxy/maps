#!/usr/bin/env python3
"""
Refine the coordinates behind global_sanctions.html.

What it does
------------
Most points on the map sit at a city centre or a country centre, because that is
all the sanctions list published. This script takes every listing whose address
looks more precise than where its point currently sits, asks a street geocoder
where that address is, and writes out replacement data files.

It is safe to stop it at any time (Ctrl-C) and run it again; it picks up where it
left off. Expect it to take several hours the first time.

How to run it
-------------
    cd ~/Desktop/sanctions-geocoding      (any folder you like)
    python3 refine_sanctions_geocoding.py

No pip install needed — standard library only.

When it finishes it writes a folder called `global_sanctions_data` next to the
script. Copy those files over the ones in the maps repo, in the folder of the
same name, and the map picks up the better coordinates with no other change.

Options
-------
    --rate 2.0      requests per second (default 2.0; raise only if the geocoder
                    is comfortable with it — be considerate, it is a free service)
    --limit 5000    stop after this many addresses this run
    --rebuild       skip geocoding and just rebuild the data files from
                    whatever progress has already been saved
"""

import argparse, gzip, json, math, os, queue, random, re, sys, threading, time
import unicodedata, urllib.parse, urllib.request

BASE = "https://welcometoyourgalaxy.github.io/maps/global_sanctions_data/"
SHARDS = ["sanctions", "crime", "debarment", "wanted", "special_interest", "enforcement"]
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache")
PROGRESS = os.path.join(HERE, "geocode_progress.jsonl")
OUTDIR = os.path.join(HERE, "global_sanctions_data")
UA = {"User-Agent": "welcometoyourgalaxy-sanctions-map/1.0 (civic education map)"}
PHOTON = "https://photon.komoot.io/api/?limit=1&q="

CITY_TYPES = {"city", "locality", "district", "county", "borough",
              "village", "town", "suburb", "municipality"}
JUNK = re.compile(
    r"\b(p\.?\s?o\.?\s*box|apt|apartment|suite|ste|floor|room|rm|unit|office|pom|kom|kv|"
    r"korp|bldg|building|block|blok|etazh|litera|lit|pod|antr|prim|kimn|bud)\b[^,;]*", re.I)


def log(*a):
    print(*a, flush=True)


def fetch(url, timeout=40):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def download_inputs():
    os.makedirs(CACHE, exist_ok=True)
    out = {}
    meta_path = os.path.join(CACHE, "meta.json")
    if not os.path.exists(meta_path):
        log("downloading meta.json")
        open(meta_path, "wb").write(fetch(BASE + "meta.json"))
    out["meta"] = json.load(open(meta_path, encoding="utf-8"))
    for name in SHARDS:
        p = os.path.join(CACHE, name + ".json.gz")
        if not os.path.exists(p):
            log("downloading %s.json.gz" % name)
            try:
                open(p, "wb").write(fetch(BASE + name + ".json.gz", timeout=600))
            except Exception as e:
                log("  could not download %s (%s) — skipping it" % (name, e))
                continue
        try:
            out[name] = json.loads(gzip.decompress(open(p, "rb").read()).decode("utf-8"))
        except Exception as e:
            log("  %s is unreadable (%s); delete cache/ and run again" % (name, e))
            sys.exit(1)
    return out


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s)).strip()


def clean(a):
    s = re.sub(r"\([^)]*\)", " ", a)
    s = JUNK.sub(" ", s)
    s = re.sub(r"\b\d{4,6}\b", " ", s)
    s = re.sub(r"[№#]", "", s)
    s = re.sub(r"\s*,\s*", ", ", s)
    s = re.sub(r"(,\s*)+", ", ", s)
    return re.sub(r"\s{2,}", " ", s).strip(" ,;-")


def tail(a, n=2):
    segs = [x.strip() for x in re.split(r"[,\n]", a)
            if x.strip() and not re.fullmatch(r"[\d\s\-/.]+", x.strip())]
    return ", ".join(segs[-n:]) if segs else a


def ask(text, rate_lock):
    """One geocoder call, with backoff. Returns the first feature or None."""
    for attempt in range(4):
        with rate_lock:
            pass
        try:
            raw = fetch(PHOTON + urllib.parse.quote(text[:200]), timeout=30)
            feats = json.loads(raw).get("features") or []
            return feats[0] if feats else None
        except Exception as e:
            if "429" in str(e):
                time.sleep(2 + attempt * 3 + random.random())
            elif attempt == 3:
                return None
            else:
                time.sleep(1 + attempt)
    return None


class Pacer:
    """Lets through at most `rate` calls a second, across all threads."""
    def __init__(self, rate):
        self.gap = 1.0 / max(0.2, rate)
        self.lock = threading.Lock()
        self.next = time.time()

    def __enter__(self):
        with self.lock:
            now = time.time()
            if now < self.next:
                time.sleep(self.next - now)
            self.next = max(now, self.next) + self.gap

    def __exit__(self, *a):
        return False


def targets_from(data):
    """Every address whose point is not already street level, with its countries."""
    want = {}
    for name in SHARDS:
        for r in data.get(name) or []:
            if r[2] == 0 or not r[6]:
                continue
            ccs = [c.strip().upper() for c in (r[10] or "").split(";") if c.strip()]
            want.setdefault(r[6], set()).update(ccs)
    # the worst-placed first, so a short run still helps the map most
    order = {}
    for name in SHARDS:
        for r in data.get(name) or []:
            if r[6] in want:
                order[r[6]] = min(order.get(r[6], 9), 0 if r[2] == 2 else 1)
    return sorted(((a, sorted(c)) for a, c in want.items()), key=lambda t: order.get(t[0], 9))


def geocode_all(data, rate, limit):
    done = set()
    if os.path.exists(PROGRESS):
        for line in open(PROGRESS, encoding="utf-8"):
            try:
                done.add(json.loads(line)["a"])
            except Exception:
                pass
    todo = [t for t in targets_from(data) if t[0] not in done]
    if limit:
        todo = todo[:limit]
    log("%d addresses to look up (%d already done)" % (len(todo), len(done)))
    if not todo:
        return
    pacer = Pacer(rate)
    q = queue.Queue()
    for t in todo:
        q.put(t)
    fh = open(PROGRESS, "a", encoding="utf-8")
    lock = threading.Lock()
    counts = {"street": 0, "city": 0, "miss": 0}
    t0 = time.time()

    def accept(f, ccs, qn, want_street):
        p = f["properties"]
        cc = (p.get("countrycode") or "").upper()
        if ccs and cc and cc not in ccs:
            return None
        t = p.get("type", "")
        c = f["geometry"]["coordinates"]
        if want_street and t in ("house", "street"):
            street = norm(p.get("street") or p.get("name") or "")
            if p.get("housenumber") or (street and len(street) > 4 and street in qn):
                return (round(c[1], 6), round(c[0], 6), 0)
            return None
        if t in CITY_TYPES:
            return (round(c[1], 6), round(c[0], 6), 1)
        return None

    def worker():
        while True:
            try:
                addr, ccs = q.get_nowait()
            except queue.Empty:
                return
            rec = {"a": addr, "s": "miss"}
            cq = clean(addr)
            qn = norm(cq)
            f = ask(cq, pacer) if cq else None
            hit = accept(f, ccs, qn, True) if f else None
            if hit is None and f:
                hit = accept(f, ccs, qn, False)
            if hit is None:
                f2 = ask(tail(cq or addr, 2), pacer)
                if f2:
                    hit = accept(f2, ccs, qn, False)
            if hit:
                rec.update(s="ok", lat=hit[0], lon=hit[1], q=hit[2])
            with lock:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                if rec["s"] == "ok":
                    counts["street" if rec["q"] == 0 else "city"] += 1
                else:
                    counts["miss"] += 1
                n = sum(counts.values())
                if n % 200 == 0:
                    fh.flush()
                    el = time.time() - t0
                    left = (len(todo) - n) * el / max(1, n)
                    log("  %d/%d  street %d  city %d  no match %d  ~%d min left"
                        % (n, len(todo), counts["street"], counts["city"], counts["miss"], left / 60))

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(3)]
    for t in threads:
        t.start()
    try:
        while any(t.is_alive() for t in threads):
            time.sleep(1)
    except KeyboardInterrupt:
        log("\nstopping — progress is saved, run the script again to carry on")
    fh.flush()
    fh.close()
    log("this run: street %d, city %d, no match %d" % (counts["street"], counts["city"], counts["miss"]))


def haversine(a, b, c, d):
    R = 6371.0
    p = math.radians
    return 2 * R * math.asin(math.sqrt(
        math.sin((p(c) - p(a)) / 2) ** 2 +
        math.cos(p(a)) * math.cos(p(c)) * math.sin((p(d) - p(b)) / 2) ** 2))


def rebuild(data):
    better = {}
    if os.path.exists(PROGRESS):
        for line in open(PROGRESS, encoding="utf-8"):
            try:
                r = json.loads(line)
                if r.get("s") == "ok":
                    better[r["a"]] = (r["lat"], r["lon"], r["q"])
            except Exception:
                pass
    if not better:
        log("nothing geocoded yet — nothing to rebuild")
        return
    os.makedirs(OUTDIR, exist_ok=True)
    moved = improved = 0
    prec = [0, 0, 0]
    for name in SHARDS:
        rows = data.get(name)
        if rows is None:
            continue
        for r in rows:
            b = better.get(r[6])
            if b and b[2] <= r[2]:
                if haversine(r[0], r[1], b[0], b[1]) > 0.05:
                    moved += 1
                if b[2] < r[2]:
                    improved += 1
                r[0], r[1], r[2] = round(b[0], 5), round(b[1], 5), b[2]
            prec[r[2]] += 1
        blob = json.dumps(rows, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        open(os.path.join(OUTDIR, name + ".json.gz"), "wb").write(gzip.compress(blob, 9))
        log("wrote %s.json.gz (%d rows)" % (name, len(rows)))
    meta = data["meta"]
    meta["precnt"] = prec
    open(os.path.join(OUTDIR, "meta.json"), "w", encoding="utf-8").write(
        json.dumps(meta, separators=(",", ":"), ensure_ascii=False))
    log("wrote meta.json")
    log("\n%d points moved, %d of them to a more precise band" % (moved, improved))
    log("precision now: %d street, %d city, %d country only" % (prec[0], prec[1], prec[2]))
    log("\nCopy everything in:\n  %s\ninto the maps repo folder global_sanctions_data/ and commit." % OUTDIR)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rate", type=float, default=2.0, help="requests per second")
    ap.add_argument("--limit", type=int, default=0, help="stop after this many addresses")
    ap.add_argument("--rebuild", action="store_true", help="rebuild data files only")
    args = ap.parse_args()
    data = download_inputs()
    if not args.rebuild:
        geocode_all(data, args.rate, args.limit)
    rebuild(data)


if __name__ == "__main__":
    main()
