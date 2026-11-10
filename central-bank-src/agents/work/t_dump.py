import asyncio,sys,json
from playwright.async_api import async_playwright
S=sys.argv[1]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        pg = await b.new_page(viewport={"width":1500,"height":900}); errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file://"+S+"/t/dump.html"); await pg.wait_for_timeout(5000)
        await pg.evaluate("document.querySelector('#det').classList.add('open');T.S.latest=true")
        d=await pg.evaluate("""(()=>{const o={};const b=document.querySelector('#detBody');
          Object.keys(T.P).forEach(k=>{T3.detail(k);o['p:'+k]=b.innerText});
          T.NET.nodes.forEach((n,i)=>{T3.entityBox(i);o['n:'+n.name]=b.innerText});return o})()""")
        json.dump(d,open(S+"/boxes.json","w"),ensure_ascii=False)
        print(len(d),sum(len(v) for v in d.values()),errs[:3]); await b.close()
asyncio.run(main())
