#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_scene_art.py — 应用场景线稿图（衬衫门襟/牛仔腰头/连帽绳扣/制服）"""
import os
os.makedirs("images/scene", exist_ok=True)

INK="#283A52"; BRASS="#B08D3E"; BRASSL="#C9A961"; PAPER="#FBFBF9"
CREAM="#EDE9DE"; LINE="#C9C3B4"; GREY="#8A8575"; DENIM="#3E5A78"

def frame(title):
    title = title.replace("&","&amp;")
    return f'''<svg viewBox="0 0 480 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">
<rect width="480" height="360" fill="{PAPER}"/>
<rect x="10" y="10" width="460" height="340" fill="none" stroke="{LINE}" stroke-width="1.1"/>
<text x="24" y="338" fill="{GREY}" font-family="IBM Plex Mono,monospace" font-size="10" letter-spacing="1.5">{title}</text>
<circle cx="452" cy="332" r="3" fill="{BRASS}"/>'''

def btn(cx,cy,r,fill=CREAM,holes=True):
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="1.6"/>'
    if holes:
        for dx,dy in [(-r*0.28,-r*0.28),(r*0.28,-r*0.28),(-r*0.28,r*0.28),(r*0.28,r*0.28)]:
            g+=f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{r*0.13}" fill="{INK}"/>'
    return g

# 1) 衬衫门襟
s=frame("APPLICATION · SHIRT PLACKET")
s+=f'<path d="M150 40 L150 330 L210 330 L210 40 Z" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<path d="M270 40 L270 330 L330 330 L330 40 Z" fill="{CREAM}" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<line x1="210" y1="40" x2="210" y2="330" stroke="{LINE}" stroke-width="1" stroke-dasharray="4 4"/>'
s+=f'<line x1="270" y1="40" x2="270" y2="330" stroke="{LINE}" stroke-width="1"/>'
for i,y in enumerate(range(75,331,52)):
    s+=btn(240,y,13)
    if i==1:
        s+=f'<line x1="253" y1="{y}" x2="400" y2="{y-30}" stroke="{INK}" stroke-width="0.8"/><circle cx="253" cy="{y}" r="2.2" fill="{BRASS}"/>'
        s+=f'<text x="404" y="{y-40}" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">14–18L</text>'
        s+=f'<text x="404" y="{y-26}" fill="{GREY}" font-family="IBM Plex Sans,sans-serif" font-size="10">resin · DTM</text>'
s+='</svg>'
open("images/scene/shirt-placket.svg","w").write(s)

# 2) 牛仔腰头
s=frame("APPLICATION · DENIM WAISTBAND")
s+=f'<path d="M60 120 L420 120 L420 230 L60 230 Z" fill="{DENIM}" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<line x1="60" y1="140" x2="420" y2="140" stroke="{BRASSL}" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>'
s+=f'<line x1="60" y1="210" x2="420" y2="210" stroke="{BRASSL}" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>'
# tack button
s+=f'<circle cx="150" cy="175" r="26" fill="url(#bg)"/>'
s=s.replace("<rect width","<defs><radialGradient id='bg' cx='38%' cy='34%'><stop offset='0%' stop-color='#F0DDAA'/><stop offset='60%' stop-color='#C9A961'/><stop offset='100%' stop-color='#7A5E26'/></radialGradient></defs><rect width",1)
s+=f'<circle cx="150" cy="175" r="26" fill="none" stroke="{INK}" stroke-width="1.6"/><circle cx="150" cy="175" r="16" fill="none" stroke="{INK}" stroke-width="1" opacity="0.5"/>'
s+=f'<text x="150" y="179" text-anchor="middle" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="9" opacity="0.6">LOGO</text>'
# rivets
for x in [320,360]:
    s+=f'<circle cx="{x}" cy="175" r="9" fill="url(#bg)" stroke="{INK}" stroke-width="1.4"/>'
s+=f'<line x1="176" y1="175" x2="250" y2="90" stroke="{INK}" stroke-width="0.8"/><circle cx="176" cy="175" r="2.2" fill="{BRASS}"/>'
s+=f'<text x="254" y="86" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">tack button 17–20mm</text>'
s+=f'<line x1="320" y1="166" x2="330" y2="100" stroke="{INK}" stroke-width="0.8"/><circle cx="320" cy="166" r="2.2" fill="{BRASS}"/>'
s+=f'<text x="334" y="96" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">rivets</text>'
s+='</svg>'
open("images/scene/denim-waistband.svg","w").write(s)

# 3) 连帽绳扣
s=frame("APPLICATION · HOODIE DRAWCORD")
s+=f'<path d="M120 60 Q240 30 360 60 L360 90 Q240 70 120 90 Z" fill="{CREAM}" stroke="{INK}" stroke-width="1.6"/>'
# eyelets
s+=f'<circle cx="200" cy="78" r="8" fill="{PAPER}" stroke="{BRASS}" stroke-width="2.5"/>'
s+=f'<circle cx="280" cy="78" r="8" fill="{PAPER}" stroke="{BRASS}" stroke-width="2.5"/>'
# cords
s+=f'<path d="M200 86 Q210 180 230 250" fill="none" stroke="{INK}" stroke-width="2.5"/>'
s+=f'<path d="M280 86 Q270 180 250 250" fill="none" stroke="{INK}" stroke-width="2.5"/>'
# cord lock
s+=f'<rect x="222" y="195" width="36" height="30" rx="9" fill="{CREAM}" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<rect x="231" y="186" width="18" height="12" rx="5" fill="{CREAM}" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<line x1="258" y1="210" x2="360" y2="180" stroke="{INK}" stroke-width="0.8"/><circle cx="258" cy="210" r="2.2" fill="{BRASS}"/>'
s+=f'<text x="364" y="176" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">cord lock</text>'
s+=f'<line x1="208" y1="78" x2="150" y2="140" stroke="{INK}" stroke-width="0.8"/><circle cx="208" cy="78" r="2.2" fill="{BRASS}"/>'
s+=f'<text x="80" y="155" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">eyelet</text>'
s+='</svg>'
open("images/scene/hoodie-drawcord.svg","w").write(s)

# 4) 西装/制服排扣
s=frame("APPLICATION · BLAZER FRONT")
s+=f'<path d="M180 40 L150 60 L150 330 L240 330 L240 40 Z" fill="{CREAM}" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<path d="M300 40 L330 60 L330 330 L240 330 L240 40 Z" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
s+=f'<path d="M180 40 L150 60 L165 110 L210 70 Z" fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>'
s+=f'<path d="M300 40 L330 60 L315 110 L270 70 Z" fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>'
s=s.replace("<rect width","<defs><radialGradient id='bg2' cx='38%' cy='34%'><stop offset='0%' stop-color='#F0DDAA'/><stop offset='60%' stop-color='#C9A961'/><stop offset='100%' stop-color='#7A5E26'/></radialGradient></defs><rect width",1)
for i,y in enumerate([170,230,290]):
    s+=f'<circle cx="240" cy="{y}" r="14" fill="url(#bg2)" stroke="{INK}" stroke-width="1.6"/>'
    s+=f'<circle cx="240" cy="{y}" r="8" fill="none" stroke="{INK}" stroke-width="1" opacity="0.5"/>'
    if i==0:
        s+=f'<line x1="254" y1="{y}" x2="400" y2="{y-30}" stroke="{INK}" stroke-width="0.8"/><circle cx="254" cy="{y}" r="2.2" fill="{BRASS}"/>'
        s+=f'<text x="404" y="{y-40}" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="10">24–32L</text>'
        s+=f'<text x="404" y="{y-26}" fill="{GREY}" font-family="IBM Plex Sans,sans-serif" font-size="10">metal shank</text>'
s+='</svg>'
open("images/scene/blazer-front.svg","w").write(s)

print("4张场景图已生成 → images/scene/")
