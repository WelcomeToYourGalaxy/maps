import asyncio,sys,json
from playwright.async_api import async_playwright
page,out=sys.argv[1],sys.argv[2]
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
    pg=await b.new_page(viewport={"width":1400,"height":900}); errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    await pg.goto("file://"+page); await pg.wait_for_timeout(6000)
    d=await pg.evaluate("""(()=>{const out={};const ids=['all','inside','around','outside','cc'];
      Object.keys(T.P).forEach(k=>{const o={};ids.forEach(id=>{const l=T3.L.find(x=>x.id===id);let v=null;try{const r=l.get(T.P[k],T.S.year);v=r&&r.v!=null?r.v:null}catch(e){}o[id]=v});out[k]=o});return out})()""")
    json.dump(d,open(out,"w")); print(len(d),errs[:2]); await b.close()
asyncio.run(main())
