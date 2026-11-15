import sys
t=open(f'dig/d{int(sys.argv[1]):02d}.txt').read()
for block in t.split('\n\n'):
    L=block.split('\n'); H=[l for l in L if l.startswith('  H ')]; F=[l for l in L if l.startswith('  F ')]; S=[l for l in L if l.startswith('  S ')]
    keepH=set(H[:3]+H[-14:]); keepF=set(F[-7:]); keepS=set(S[-4:])
    for l in L:
        if l.startswith('  H ') and l not in keepH: continue
        if l.startswith('  F ') and l not in keepF: continue
        if l.startswith('  S ') and l not in keepS: continue
        print(l[:175])
    print()
