import sys,re
f=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]) if len(sys.argv)>3 else a
txt=open(f,errors='replace').read()
parts=re.split(r'\[\[page (\d+)\]\]',txt)
# parts: [pre, n1, body1, n2, body2...]
out=[]
for i in range(1,len(parts),2):
    n=int(parts[i])
    if a<=n<=b: out.append('[[page %d]]\n'%n+parts[i+1])
print(''.join(out))
