from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
src = Image.open('culprits.webp').convert('RGBA'); W, H = src.size
a = np.array(src).astype(np.float32)

# 1. Seam: the plate's left and right ends meet in the Pacific, where each end carries half of a
#    compass rose. Replace a band 85 px either side of the join (rows 560-860) with open sea taken
#    from one continuous stretch of the painted Indian Ocean, so the two ends run into each other.
B, Y0, Y1, F = 110, 575, 835, 30
blk = a[815:945, 1035:1035 + 2 * B, :].copy()          # 130 x 220 of open Indian Ocean, the cleanest sea on the plate
pac = np.concatenate([blk, blk[::-1]], axis=0)        # mirrored once to fill the 260-row band
right = pac[:, :B]; left = pac[:, B:]                # right end of the plate, then left end, continuous
def blend(x0, patch, inner_edge):
    h = Y1 - Y0
    for j in range(patch.shape[1]):
        # horizontal weight: full patch near the join, fading out over F px at the inner edge
        d = (patch.shape[1] - 1 - j) if inner_edge == 'right' else j
        wx = min(1.0, (d + 1) / F) if False else 1.0
        dist_inner = (patch.shape[1] - 1 - j) if inner_edge == 'right' else j
        wx = min(1.0, dist_inner / F)
        for i in range(h):
            wy = min(1.0, i / F, (h - 1 - i) / F)
            w = wx * wy
            a[Y0 + i, x0 + j, :3] = a[Y0 + i, x0 + j, :3] * (1 - w) + patch[i, j, :3] * w
# left end of the plate (x 0..B): patch fades out toward x=B
blend(0, left, 'right')
# right end of the plate (x W-B..W): patch fades out toward x=W-B
blend(W - B, right, 'left')

img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'RGBA')

# 2. Cartouche: refill the parchment from its clean margins, then letter it for this map.
x0, y0, x1, y1 = 27, 997, 196, 1112
p = np.array(img).astype(np.float32)
lcol = p[y0:y1, x0:x0 + 10, :3].mean(axis=1); rcol = p[y0:y1, x1 - 10:x1, :3].mean(axis=1)
lcol = np.array(Image.fromarray(lcol.astype(np.uint8)[:, None, :]).filter(ImageFilter.GaussianBlur(4)))[:, 0, :].astype(np.float32)
rcol = np.array(Image.fromarray(rcol.astype(np.uint8)[:, None, :]).filter(ImageFilter.GaussianBlur(4)))[:, 0, :].astype(np.float32)
t = np.linspace(0, 1, x1 - x0)[None, :, None]
fill = lcol[:, None, :] * (1 - t) + rcol[:, None, :] * t
rng = np.random.default_rng(7)
fill += rng.normal(0, 2.2, fill.shape)
p[y0:y1, x0:x1, :3] = np.clip(fill, 0, 255)
img = Image.fromarray(np.clip(p, 0, 255).astype(np.uint8), 'RGBA')
d = ImageDraw.Draw(img)
ink = (78, 60, 37, 255)
font = '8vIU7ww63mVu7gtR-kwKxNvkNOjw-jHgTYo.ttf'   # Cinzel 700
f1 = ImageFont.truetype(font, 16); f2 = ImageFont.truetype(font, 25)
cx = (24 + 198) / 2
def centred(text, f, y, sp):
    w = sum(d.textlength(c, font=f) for c in text) + sp * (len(text) - 1); x = cx - w / 2
    for c in text: d.text((x, y), c, font=f, fill=ink); x += d.textlength(c, font=f) + sp
centred('LOAN', f1, 1011, 2); centred('CONDITIONS', f1, 1031, 1)
d.line([(cx - 50, 1058), (cx + 50, 1058)], fill=ink, width=2)
centred('MAP', f2, 1066, 3)

img.save('loan-conditions-atlas-plate.webp', 'WEBP', quality=90, method=6)
bg = Image.new('RGBA', img.size, (255, 255, 255, 255)); bg.alpha_composite(img); bg = bg.convert('RGB')
bg.crop((0, 960, 260, 1140)).resize((520, 360)).save('check_cart.png')
w = Image.new('RGB', (420, 520)); w.paste(bg.crop((1390, 500, 1600, 1020)), (0, 0)); w.paste(bg.crop((0, 500, 210, 1020)), (210, 0)); w.save('check_seam.png')
