import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader"])
        pg = await b.new_page(viewport={"width":int(__import__("os").environ.get("W","1500")),"height":900})
        errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto("file:///root/cb/dist/central_bank_independence.html")
        await pg.wait_for_timeout(12000)
        steps=sys.argv[1:]
        for i,s in enumerate(steps):
            await pg.evaluate(s); await pg.wait_for_timeout(4000)
            await pg.screenshot(path=f"/root/cb/shots/s{i}.png", timeout=120000)
        print("ERRORS:",errs)
        await b.close()
asyncio.run(main())
