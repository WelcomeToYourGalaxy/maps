import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome", args=["--use-gl=swiftshader","--enable-webgl"])
        pg = await b.new_page()
        pg.on("pageerror", lambda e: print("PAGEERROR", e.name, e.message, str(e.stack)[:500]))
        pg.on("console", lambda m: print("CONSOLE", m.type, m.text[:300]) if m.type in ("error",) else None)
        await pg.goto("file:///home/claude/work/loan-conditions.html"); await pg.wait_for_timeout(6000)
        await b.close()
asyncio.run(main())
