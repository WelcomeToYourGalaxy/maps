#!/bin/bash
# usage: grepdoc.sh <url> <tag>
U="$1"; T="$2"
D=/root/cb/dl/r66
curl -sS -L --max-time 120 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" -o "$D/$T.pdf" -w "HTTP:%{http_code} SIZE:%{size_download}\n" "$U"
if [ -s "$D/$T.pdf" ]; then
  pdftotext -layout "$D/$T.pdf" "$D/$T.txt" 2>/dev/null && echo "CHARS:$(wc -c < $D/$T.txt)"
fi
