#!/bin/sh
# download one archive PDF (if missing) and save its first page's text
n=$1; d=/home/claude/dl/imfarch
[ -s $d/$n.pdf ] || curl -sS --retry 3 -o $d/$n.pdf "https://stoprdcom01e2.blob.core.windows.net/allfiles/IG/Production%20Hosting/Adlib/Public%20Documents/EB/$n.PDF"
[ -s $d/p1/$n.txt ] || pdftotext -l 1 $d/$n.pdf $d/p1/$n.txt 2>/dev/null
