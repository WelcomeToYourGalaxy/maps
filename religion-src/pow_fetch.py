import subprocess, os, sys, time, concurrent.futures as cf
OUT = "/home/claude/pow/tiles3/"; HOST = "https://maps.mail.ru/osm/tools/overpass/api/interpreter"
Q = '[out:csv(::type,::id,::lat,::lon,name,religion,denomination,building,"name:en";false;"\\t")][timeout:240];nwr["amenity"="place_of_worship"](%s,%s,%s,%s);out center;'
def get(box, depth=0):
    s, w, n, e = box; fn = OUT + "t_%g_%g_%g_%g.tsv" % box
    if os.path.exists(fn): return 0
    for attempt in range(2):
        if os.path.exists(fn + ".part"): os.remove(fn + ".part")
        r = subprocess.run(["curl", "-s", "-m", "270", "-o", fn + ".part", "-w", "%{http_code}", "--data-urlencode", "data=" + Q % box, HOST], capture_output=True, text=True)
        if r.stdout.strip() == "200" and not os.path.exists(fn + ".part"): open(fn + ".part", "w").close()
        ok = r.stdout.strip() == "200" and os.path.exists(fn + ".part")
        if ok:
            head = open(fn + ".part", "rb").read(200)
            if b"<?xml" in head or b"<html" in head or b"runtime error" in head: ok = False
        if ok:
            tail = open(fn + ".part", "rb").read()[-400:]
            if b"runtime error" in tail or b"<remark>" in tail: ok = False
        if ok:
            os.rename(fn + ".part", fn); print("ok", box, os.path.getsize(fn), flush=True); return 1
        time.sleep(5 + 5 * attempt)
    if depth < 3:
        ms, mw = (s + n) / 2, (w + e) / 2
        print("split", box, flush=True)
        for b in [(s, w, ms, mw), (s, mw, ms, e), (ms, w, n, mw), (ms, mw, n, e)]: get(b, depth + 1)
        open(fn, "w").close(); return 1
    print("FAILED", box, flush=True); return 0
boxes = [(s, w, s + 10, w + 10) for s in range(-60, 80, 10) for w in range(-180, 180, 10)]
with cf.ThreadPoolExecutor(2) as ex: list(ex.map(get, boxes))
print("DONE", flush=True)
