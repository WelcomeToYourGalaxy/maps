import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome", args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
        pg = await b.new_page(viewport={"width":1400,"height":860})
        errs=[]
        pg.on("pageerror", lambda e: errs.append(f"PAGEERROR: {e}"))
        pg.on("console", lambda m: errs.append(f"{m.type}: {m.text}") if m.type=="error" else None)
        await pg.goto("file:///home/claude/work/loan-conditions.html"); await pg.wait_for_timeout(9000)
        print("now:", await pg.inner_text("#now"))
        print("order:", await pg.evaluate("[...document.querySelectorAll('.sec')].map(s=>s.textContent).join(' | ')"))
        await pg.screenshot(path="/home/claude/work/n_all.png")
        ids = await pg.evaluate("[...document.querySelectorAll('.row')].map(r=>r.dataset.id)")
        for rid in ids:
            await pg.click(f'.row[data-id="{rid}"] .pick'); await pg.wait_for_timeout(900)
            print(rid, "|", (await pg.inner_text(f"#leg-{rid}")).split("\n")[0], "|", (await pg.inner_text(f"#un-{rid}"))[:160])
        # popups for each row on a few countries
        for rid, ll in [("all",[-1.0,7.9]),("oecd",[34,-6]),("eu",[22.5,39.5]),("pc",[-1.0,7.9]),("cn",[17.8,-12.3]),("hcl",[37.9,0.3]),("imfc",[-10.5,20.5])]:
            await pg.click(f'.row[data-id="{rid}"] .pick'); await pg.wait_for_timeout(700)
            await pg.evaluate(f"window.loanConditionsMap.jumpTo({{center:{ll},zoom:3}})"); await pg.wait_for_timeout(1500)
            pt = await pg.evaluate(f"(()=>{{const p=window.loanConditionsMap.project({ll});return [p.x,p.y]}})()")
            await pg.mouse.click(pt[0], pt[1]); await pg.wait_for_timeout(900)
            t = await pg.locator(".lc-pop").inner_text() if await pg.locator(".lc-pop").count() else "NO POPUP"
            print("POPUP", rid, ":", t[:350].replace("\n"," / "))
            if rid=="imfc": await pg.screenshot(path="/home/claude/work/n_popup.png")
            if await pg.locator(".maplibregl-popup-close-button").count(): await pg.click(".maplibregl-popup-close-button")
        # hover a ? mark
        q = pg.locator('.row[data-id="all"] .q.big'); await q.hover(); await pg.wait_for_timeout(300)
        print("TIP:", (await pg.inner_text("#qtip"))[:150], await pg.evaluate("getComputedStyle(document.querySelector('#qtip')).display"))
        await pg.screenshot(path="/home/claude/work/n_tip.png")
        # flat map + bases
        await pg.click("#proj"); await pg.wait_for_timeout(2500); await pg.evaluate("window.loanConditionsMap.jumpTo({center:[20,10],zoom:1.3})"); await pg.wait_for_timeout(3000)
        await pg.screenshot(path="/home/claude/work/n_flat.png")
        await pg.click('.row[data-id="all"] .pick')
        for base in ["atlas","jurassic"]:
            await pg.click(f'#basemap button[data-base="{base}"]'); await pg.wait_for_timeout(5000); await pg.screenshot(path=f"/home/claude/work/n_{base}.png")
        print("\n".join(errs[:20]))
        await b.close()
asyncio.run(main())
