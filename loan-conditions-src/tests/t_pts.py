import asyncio
from playwright.async_api import async_playwright
S="/tmp/claude-0/-home-claude/a1308dfa-f9cb-5e0e-8aa6-7a243eefa01e/scratchpad/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-unsafe-swiftshader"])
        pg=await b.new_page(viewport={"width":1400,"height":860}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        await pg.goto("file:///home/claude/work/loan-conditions.html"); await pg.wait_for_timeout(9000)
        await pg.screenshot(path=S+"p_globe.png")
        await pg.check('input[data-pts="wb"]'); await pg.check('input[data-pts="cn"]'); await pg.wait_for_timeout(2500)
        await pg.screenshot(path=S+"p_points.png")
        await pg.click("#proj"); await pg.wait_for_timeout(2500)
        await pg.mouse.move(900,430); await pg.mouse.down(); await pg.mouse.move(1350,700,steps=10); await pg.mouse.up(); await pg.wait_for_timeout(1500)
        await pg.mouse.wheel(0,2000); await pg.wait_for_timeout(1500)
        await pg.screenshot(path=S+"p_flat.png")
        await pg.click('#basemap button[data-base="atlas"]'); await pg.wait_for_timeout(3000)
        await pg.evaluate("window.loanConditionsMap.jumpTo({center:[36.8,-1.3],zoom:6})"); await pg.wait_for_timeout(2500)
        pt=await pg.evaluate("(()=>{const m=window.loanConditionsMap;const f=m.queryRenderedFeatures({layers:['pt-cn']})[0];return f?m.project(f.geometry.coordinates):null})()")
        if pt: await pg.mouse.click(pt["x"],pt["y"]); await pg.wait_for_timeout(800)
        print("POP", await pg.evaluate('(()=>{const e=document.querySelector(".maplibregl-popup-content");return e?e.innerText.slice(0,300):"none"})()'))
        await pg.screenshot(path=S+"p_atlas.png")
        print("ERRS",errs); await b.close()
asyncio.run(main())
