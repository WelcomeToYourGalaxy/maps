import asyncio
from playwright.async_api import async_playwright
S="/tmp/claude-0/-home-claude/75909650-1f0a-5efd-9cac-fb1ffc4eeffb/scratchpad/"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=swiftshader","--enable-unsafe-swiftshader"])
        pg=await b.new_page(viewport={"width":1400,"height":860}); errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        await pg.goto("file:///home/claude/work/loan-conditions.html"); await pg.wait_for_timeout(11000)
        print(await pg.evaluate('[...document.querySelectorAll("details.secd")].map(d=>d.dataset.sec+":"+d.open+":"+(d.parentElement.closest("details.secd")?.dataset.sec||d.closest("aside").id))'))
        await pg.evaluate('document.querySelector("#sidescroll").scrollTop=330'); await pg.wait_for_timeout(300)
        await pg.screenshot(path=S+"u1.png")
        # deselect
        await pg.click('.row[data-id="all"] label.pick input'); await pg.wait_for_timeout(1500)
        print("NOW", await pg.evaluate('document.querySelector("#now").textContent'), await pg.evaluate('document.querySelector(".row[data-id=all] input").checked'))
        # patterns on the right
        await pg.click('#patbox details.secd > summary'); await pg.wait_for_timeout(400)
        await pg.click('.row[data-id="pat_cold-war-loans-reward-punish"] label.pick input'); await pg.wait_for_timeout(1500)
        await pg.click('#basemap button[data-base="atlas"]'); await pg.wait_for_timeout(1500)
        await pg.evaluate("window.loanConditionsMap.jumpTo({center:[-50,10],zoom:1.7})"); await pg.wait_for_timeout(5000)
        await pg.screenshot(path=S+"u2.png")
        await pg.click('#basemap button[data-base="night"]'); await pg.wait_for_timeout(1500)
        await pg.click('.row[data-id="pat_revolving-door-wall-street-lenders"] label.pick input'); await pg.wait_for_timeout(1500)
        await pg.evaluate("window.loanConditionsMap.jumpTo({center:[-30,40],zoom:2.4})"); await pg.wait_for_timeout(4000)
        await pg.screenshot(path=S+"u3.png")
        # deselect pattern
        await pg.click('.row[data-id="pat_revolving-door-wall-street-lenders"] label.pick input'); await pg.wait_for_timeout(1200)
        print("LINES", await pg.evaluate("window.loanConditionsMap.getSource('pat-lines')._data.features?.length"))
        print("ERRS",errs); await b.close()
asyncio.run(main())
