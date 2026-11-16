#!/bin/bash
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
OUT=/root/cb/agents/work/r67/dl/mgr
page(){ curl -sL -A "$UA" --max-time 45 "$1" 2>/dev/null; }
# $1 = iso tag, rest = urls to scan for pdf links
scan(){ tag=$1; shift; for u in "$@"; do page "$u" | grep -oiE '(href|HREF)="[^"]+\.pdf[^"]*"' | sed 's/^[hH][rR][eE][fF]="//;s/"$//' ; done | sort -u | grep -iE 'annual|report|financ|statement|rapport|memoria|jaarver|bilan|godis' | head -12 | sed "s|^|$tag |" ; }
