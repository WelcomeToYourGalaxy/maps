#!/usr/bin/env python3
"""Rewrite the Atlas cartouche. plate.py font.ttf"""
import sys,random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
im=Image.open('../secret-society-src/plate.webp').convert('RGBA');a=np.array(im)
# parchment panel, measured from the painting: only its middle is repainted so the frame stays intact
px0,px1,py0,py1=28,194,1000,1112
rng=np.random.default_rng(3)
L=a[py0:py1,px0:px0+6,:3].astype(float).mean(axis=1);R=a[py0:py1,px1-6:px1,:3].astype(float).mean(axis=1)
W=px1-px0;H=py1-py0
t=np.linspace(0,1,W)[None,:,None]
g=L[:,None,:]*(1-t)+R[:,None,:]*t+rng.normal(0,1.3,(H,W,1))
a[py0:py1,px0:px1,:3]=np.clip(g,0,255).astype('uint8')
im=Image.fromarray(a)
d=ImageDraw.Draw(im);f=ImageFont.truetype(sys.argv[1],20)
try:f.set_variation_by_axes([500])
except Exception:pass
ink=(58,43,28,255);cx=(px0+px1)/2;lines=['OUTSIDE','EVERY','COUNTRY'];lh=27;y=(py0+py1)/2-lh*len(lines)/2-2
for T in lines:
    w=d.textlength(T,font=f);d.text((cx-w/2,y),T,font=f,fill=ink);y+=lh
im.save('data/plate.webp','WEBP',quality=90,method=6,exact=True)
im.convert('RGB').crop((0,900,420,1160)).resize((840,520)).save(sys.argv[2])
