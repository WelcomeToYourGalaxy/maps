import urllib.request, urllib.parse, re, json, sys
base = "https://stoprdcom01e2.blob.core.windows.net/allfiles?restype=container&comp=list&maxresults=5000&prefix=" + urllib.parse.quote("IG/Production Hosting/Adlib/Public Documents/EB/")
out = {}; marker = ""
for pre in sys.argv[1:]:
    marker = ""
    while True:
        u = base + pre + ("&marker=" + urllib.parse.quote(marker) if marker else "")
        x = urllib.request.urlopen(u, timeout=120).read().decode("utf-8-sig")
        for n, l in re.findall(r"<Name>[^<]*/EB/(\d+)\.PDF</Name>.*?<Content-Length>(\d+)</Content-Length>", x): out[int(n)] = int(l)
        marker = (re.search(r"<NextMarker>([^<]*)</NextMarker>", x) or [None, ""])[1]
        if not marker: break
json.dump(out, open("eb_blobs.json", "w")); 
ks = sorted(out); print(len(out), ks[:3], ks[-3:])
sel = {k: v for k, v in out.items() if 222000 <= k <= 239000}
print(len(sel), sum(sel.values()) / 1e9, "GB")
