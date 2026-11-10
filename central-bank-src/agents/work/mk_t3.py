import sys
src,dst=sys.argv[1],sys.argv[2]
t=open(src).read(); k='const NET = D.NET || { nodes: [], links: [] };'
assert t.count(k)==1
t=t.replace(k,k+'window.T={selectEntity,select,openWin,NET,P,D,setKinds,get ALLREL(){return ALLREL},choosePattern,get map(){return map},get S(){return S},setHot,buildSide,update,drawIndex};window.T3={detail,entityBox,L};')
open(dst,'w').write(t)
