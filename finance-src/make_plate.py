# Letters the atlas plate's cartouche for this map. Starts from the plate of religion.html (same painted base).
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, sys
src = Image.open(sys.argv[1]).convert('RGBA')
x0, y0, x1, y1 = 27, 997, 196, 1112
p = np.array(src).astype(np.float32)
lcol = p[y0:y1, x0:x0 + 6, :3].mean(axis=1); rcol = p[y0:y1, x1 - 6:x1, :3].mean(axis=1)
blur = lambda c: np.array(Image.fromarray(c.astype(np.uint8)[:, None, :]).filter(ImageFilter.GaussianBlur(4)))[:, 0, :].astype(np.float32)
lcol, rcol = blur(lcol), blur(rcol)
t = np.linspace(0, 1, x1 - x0)[None, :, None]
fill = lcol[:, None, :] * (1 - t) + rcol[:, None, :] * t
fill += np.random.default_rng(7).normal(0, 2.2, fill.shape)
p[y0:y1, x0:x1, :3] = np.clip(fill, 0, 255)
img = Image.fromarray(np.clip(p, 0, 255).astype(np.uint8), 'RGBA'); d = ImageDraw.Draw(img)
ink = (78, 60, 37, 255)
def font(sz):
    f = ImageFont.truetype('cinzel.ttf', sz)
    try: f.set_variation_by_axes([700])
    except Exception: pass
    return f
f1 = font(19); f2 = font(19); cx = (24 + 198) / 2
def centred(text, f, y, sp):
    w = sum(d.textlength(c, font=f) for c in text) + sp * (len(text) - 1); x = cx - w / 2
    for c in text: d.text((x, y), c, font=f, fill=ink); x += d.textlength(c, font=f) + sp
centred('THE FINE', f1, 1017, 1.5)
d.line([(cx - 52, 1052), (cx + 52, 1052)], fill=ink, width=2)
centred('PRINT', f2, 1062, 2.5)
img.save('plate.webp', 'WEBP', quality=90, method=6)
bg = Image.new('RGBA', img.size, (20, 30, 30, 255)); bg.alpha_composite(img); bg.convert('RGB').crop((0, 960, 260, 1140)).resize((520, 360)).save('/tmp/check_cart.png')
