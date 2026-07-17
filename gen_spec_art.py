#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_spec_art.py — 为每个产品款式生成"工程规格图纸"风格 SVG 插图
顶尖纽扣供应商（YKK 等）官网常用的技术制图视觉：正视图 + 尺寸标注 +
剖面 + 刻度，纸白底 + 靛蓝线稿 + 黄铜点缀。统一作用于全部品类页。
"""
import os, math

OUT = "images/spec"
os.makedirs(OUT, exist_ok=True)

INK = "#283A52"; BRASS = "#B08D3E"; BRASSL = "#C9A961"
PAPER = "#FBFBF9"; CREAM = "#EDE9DE"; LINE = "#C9C3B4"; GREY = "#8A8575"

W = H = 600
CX, CY = 300, 268

def escape(t):
    return t.replace('&','&amp;')

def head(title, sub):
    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)} technical drawing">
<defs>
<radialGradient id="brassG" cx="38%" cy="34%" r="72%">
<stop offset="0%" stop-color="#F0DDAA"/><stop offset="42%" stop-color="{BRASSL}"/>
<stop offset="78%" stop-color="{BRASS}"/><stop offset="100%" stop-color="#7A5E26"/>
</radialGradient>
<radialGradient id="steelG" cx="38%" cy="34%" r="72%">
<stop offset="0%" stop-color="#F4F5F7"/><stop offset="50%" stop-color="#C4CBD4"/>
<stop offset="100%" stop-color="#7E8896"/></radialGradient>
<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
<circle cx="1" cy="1" r="1" fill="{INK}" opacity="0.06"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="{PAPER}"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{LINE}" stroke-width="1.2"/>
<rect x="14" y="14" width="{W-28}" height="34" fill="{INK}"/>
<text x="30" y="36" fill="#fff" font-family="IBM Plex Mono, monospace" font-size="13" letter-spacing="1.5">{escape(title)}</text>
<text x="{W-30}" y="36" text-anchor="end" fill="{BRASSL}" font-family="IBM Plex Mono, monospace" font-size="11">{escape(sub)}</text>
'''

def foot(specs):
    # 底部规格条
    cells = ""
    n = len(specs); cw = (W-28)/n
    for i,(k,v) in enumerate(specs):
        x = 14 + i*cw
        cells += f'''<line x1="{x}" y1="{H-78}" x2="{x}" y2="{H-14}" stroke="{LINE}" stroke-width="1"/>
<text x="{x+12}" y="{H-56}" fill="{GREY}" font-family="IBM Plex Mono, monospace" font-size="9" letter-spacing="1">{k}</text>
<text x="{x+12}" y="{H-34}" fill="{INK}" font-family="IBM Plex Sans, sans-serif" font-size="13" font-weight="600">{v}</text>'''
    return f'''<line x1="14" y1="{H-78}" x2="{W-14}" y2="{H-78}" stroke="{LINE}" stroke-width="1.2"/>{cells}
</svg>'''

def dim_h(x1, x2, y, label):
    """水平尺寸标注线"""
    return f'''<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{BRASS}" stroke-width="1"/>
<line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" stroke="{BRASS}" stroke-width="1"/>
<line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" stroke="{BRASS}" stroke-width="1"/>
<rect x="{(x1+x2)/2-26}" y="{y-10}" width="52" height="16" fill="{PAPER}"/>
<text x="{(x1+x2)/2}" y="{y+2}" text-anchor="middle" fill="{BRASS}" font-family="IBM Plex Mono, monospace" font-size="11">{label}</text>'''

def leader(x, y, tx, ty, label):
    """引线标注"""
    return f'''<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{INK}" stroke-width="0.8"/>
<circle cx="{x}" cy="{y}" r="2.2" fill="{BRASS}"/>
<text x="{tx+(6 if tx>=x else -6)}" y="{ty+4}" text-anchor="{'start' if tx>=x else 'end'}" fill="{INK}" font-family="IBM Plex Mono, monospace" font-size="10.5">{label}</text>'''

def holes(cx, cy, r, n=4, hr=7, gap=20):
    g = ""
    if n == 4:
        pts = [(-gap,-gap),(gap,-gap),(-gap,gap),(gap,gap)]
    elif n == 2:
        pts = [(-gap,0),(gap,0)]
    else:
        pts = []
    for dx,dy in pts:
        g += f'<circle cx="{cx+dx}" cy="{cy+dy}" r="{hr}" fill="{PAPER}" stroke="{INK}" stroke-width="1.6"/>'
    return g

# ---- 各款式绘制函数 ----
def flat_button(fill, n_holes=4, rim=True):
    R = 120
    g = f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    if rim:
        g += f'<circle cx="{CX}" cy="{CY}" r="{R-16}" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.55"/>'
    g += holes(CX, CY, R, n=n_holes)
    g += dim_h(CX-R, CX+R, CY+R+34, "Ø D mm")
    g += leader(CX+R*0.62, CY-R*0.62, CX+R+30, CY-R-20, "rim")
    g += leader(CX-20, CY-20, CX-R-30, CY-50, f"{n_holes}-hole")
    return g

def shank_button(fill):
    R = 110
    g = f'<circle cx="{CX}" cy="{CY-14}" r="{R}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    g += f'<circle cx="{CX}" cy="{CY-14}" r="{R-22}" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.5"/>'
    # shank loop
    g += f'<path d="M{CX-14} {CY+R-8} q14 26 28 0" fill="none" stroke="{INK}" stroke-width="3"/>'
    g += leader(CX, CY+R+4, CX+R-10, CY+R+44, "metal shank")
    g += dim_h(CX-R, CX+R, CY+R+44, "Ø D mm")
    return g

def snap_set():
    # 四件套排成2x2
    cells = [("CAP","socket"),("SOCKET","cap"),("STUD","stud"),("POST","post ring")]
    g = ""
    pos = [(CX-86,CY-70),(CX+86,CY-70),(CX-86,CY+58),(CX+86,CY+58)]
    for (px,py),(lab,_) in zip(pos, cells):
        g += f'<circle cx="{px}" cy="{py}" r="50" fill="url(#brassG)" stroke="{INK}" stroke-width="1.8"/>'
        g += f'<circle cx="{px}" cy="{py}" r="30" fill="none" stroke="{INK}" stroke-width="1.4" opacity="0.6"/>'
        g += f'<circle cx="{px}" cy="{py}" r="11" fill="{PAPER}" stroke="{INK}" stroke-width="1.4"/>'
        g += f'<text x="{px}" y="{py+72}" text-anchor="middle" fill="{GREY}" font-family="IBM Plex Mono,monospace" font-size="9">{lab}</text>'
    g += f'<text x="{CX}" y="{CY-2}" text-anchor="middle" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="11" opacity="0.5">4-PART SET</text>'
    return g

def jeans_tack():
    R = 116
    g = f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#brassG)" stroke="{INK}" stroke-width="2"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R-14}" fill="none" stroke="{INK}" stroke-width="1.4" opacity="0.5"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R-30}" fill="none" stroke="{INK}" stroke-width="1" opacity="0.4"/>'
    # logo area
    g += f'<text x="{CX}" y="{CY+6}" text-anchor="middle" fill="{INK}" font-family="IBM Plex Mono,monospace" font-size="15" letter-spacing="1" opacity="0.65">LOGO</text>'
    g += dim_h(CX-R, CX+R, CY+R+34, "17–25 mm")
    g += leader(CX-R*0.7, CY-R*0.7, CX-R-26, CY-R-16, "tack cap")
    # 侧面铆钉pin
    g += f'<rect x="{CX-4}" y="{CY+R+2}" width="8" height="40" fill="url(#steelG)" stroke="{INK}" stroke-width="1.2"/>'
    g += f'<polygon points="{CX-4},{CY+R+42} {CX+4},{CY+R+42} {CX},{CY+R+54}" fill="{INK}"/>'
    g += leader(CX+4, CY+R+30, CX+50, CY+R+40, "tack pin")
    return g

def ring_snap():
    R = 110
    g = f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="url(#brassG)" stroke-width="20"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R-20}" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    # prongs
    for a in range(0, 360, 45):
        x = CX + (R+4)*math.cos(math.radians(a)); y = CY + (R+4)*math.sin(math.radians(a))
        g += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{INK}"/>'
    g += f'<text x="{CX}" y="{CY+5}" text-anchor="middle" fill="{GREY}" font-family="IBM Plex Mono,monospace" font-size="11">RING SNAP</text>'
    g += dim_h(CX-R-10, CX+R+10, CY+R+40, "9.5–15 mm")
    g += leader(CX+R*0.7, CY-R*0.7, CX+R+28, CY-R-10, "prong ring")
    return g

def eyelet():
    R = 110
    g = f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#brassG)" stroke="{INK}" stroke-width="2"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R-34}" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{R-18}" fill="none" stroke="{INK}" stroke-width="1" opacity="0.5"/>'
    g += dim_h(CX-R, CX+R, CY+R+34, "outer Ø")
    g += dim_h(CX-(R-34), CX+(R-34), CY-2, "inner Ø")
    g += leader(CX+R*0.72, CY-R*0.72, CX+R+24, CY-R-12, "flange")
    return g

def cord_lock():
    g = f'<rect x="{CX-70}" y="{CY-58}" width="140" height="116" rx="30" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>'
    g += f'<rect x="{CX-30}" y="{CY-86}" width="60" height="36" rx="14" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>'
    g += f'<ellipse cx="{CX}" cy="{CY}" rx="34" ry="20" fill="{PAPER}" stroke="{INK}" stroke-width="1.6"/>'
    # cord
    g += f'<path d="M{CX-60} {CY+90} q60 -40 0 -80 M{CX+60} {CY+90} q-60 -40 0 -80" fill="none" stroke="{BRASS}" stroke-width="3" stroke-dasharray="2 4"/>'
    g += leader(CX+30, CY-70, CX+R if False else CX+96, CY-60, "spring barrel")
    g += leader(CX, CY, CX-96, CY+10, "cord channel")
    g += dim_h(CX-70, CX+70, CY+72, "body W")
    return g

def buckle():
    g = f'<rect x="{CX-96}" y="{CY-50}" width="92" height="100" rx="12" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>'
    g += f'<rect x="{CX+4}" y="{CY-50}" width="92" height="100" rx="12" fill="{CREAM}" stroke="{INK}" stroke-width="2"/>'
    # prongs
    g += f'<path d="M{CX+4} {CY-30} q-30 0 -30 30 q0 30 30 30" fill="none" stroke="{INK}" stroke-width="2"/>'
    g += f'<path d="M{CX-4} {CY-30} q30 0 30 30 q0 30 -30 30" fill="none" stroke="{INK}" stroke-width="2"/>'
    g += f'<rect x="{CX-96}" y="{CY-12}" width="40" height="24" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    g += f'<rect x="{CX+56}" y="{CY-12}" width="40" height="24" fill="none" stroke="{INK}" stroke-width="1.4"/>'
    g += f'<text x="{CX}" y="{CY+78}" text-anchor="middle" fill="{GREY}" font-family="IBM Plex Mono,monospace" font-size="9">SIDE-RELEASE BUCKLE</text>'
    g += leader(CX-50, CY-30, CX-96-4, CY-66, "webbing slot")
    return g

# ---- 款式登记表：文件名 → (标题, 副标题, 绘制函数, 底部规格) ----
ITEMS = {
 # resin
 "resin-4hole":   ("4-HOLE SHIRT BUTTON","RESIN · 14L–20L", lambda: flat_button(CREAM,4),
                   [("MATERIAL","Polyester"),("SIZE","9–13 mm"),("HOLES","4"),("COLOR","DTM")]),
 "resin-pearl":   ("PEARL POLO BUTTON","RESIN · 16L–24L", lambda: flat_button("#EDEAE0",2),
                   [("MATERIAL","Urea pearl"),("SIZE","10–15 mm"),("FINISH","Pearl"),("HOLES","2")]),
 "resin-suit":    ("ENGRAVED SUIT BUTTON","RESIN · 32L–44L", lambda: flat_button("#3A2F26",4,rim=True),
                   [("MATERIAL","Resin"),("SIZE","20–28 mm"),("LOGO","Laser"),("HOLES","4")]),
 "resin-chef":    ("CHEF / UNIFORM STUD","RESIN · removable", lambda: shank_button("#F4F4F0"),
                   [("MATERIAL","Nylon"),("TYPE","Removable"),("WASH","90°C"),("BACK","Flat")]),
 # metal
 "metal-blazer":  ("EMBOSSED BLAZER BUTTON","METAL · shank", lambda: shank_button("url(#brassG)"),
                   [("MATERIAL","Zinc alloy"),("SIZE","15–25 mm"),("LOGO","Emboss"),("PLATE","10+")]),
 "metal-coat":    ("BRASS STAMPED COAT BUTTON","METAL · 2-hole", lambda: flat_button("url(#brassG)",2),
                   [("MATERIAL","Brass"),("SIZE","18–30 mm"),("FINISH","Antique"),("HOLES","2")]),
 "metal-uniform": ("UNIFORM / MILITARY BUTTON","METAL · shank", lambda: shank_button("url(#brassG)"),
                   [("MATERIAL","Brass"),("SIZE","15–22 mm"),("LOGO","3D mold"),("PLATE","Gold")]),
 "metal-enamel":  ("ENAMEL-FILL FASHION BUTTON","METAL · 4-hole", lambda: flat_button("url(#brassG)",4),
                   [("MATERIAL","Alloy"),("SIZE","15–28 mm"),("FILL","Enamel"),("HOLES","4")]),
 # snap
 "snap-spring":   ("S-SPRING SNAP BUTTON","SNAP · 4-part", snap_set,
                   [("MATERIAL","Brass"),("SIZE","12.5–15 mm"),("TYPE","S-spring"),("PARTS","4")]),
 "snap-ring":     ("RING SNAP FASTENER","SNAP · prong", ring_snap,
                   [("MATERIAL","Brass"),("SIZE","9.5–15 mm"),("TYPE","Ring"),("PRONGS","Open")]),
 "snap-prong":    ("PRONG SNAP (BABYWEAR)","SNAP · prong", ring_snap,
                   [("MATERIAL","Nickel-free"),("SIZE","9.5–11 mm"),("USE","Babywear"),("TEST","Pull")]),
 "snap-pearl":    ("PEARL / PAINTED CAP SNAP","SNAP · cap", snap_set,
                   [("MATERIAL","Brass+ABS"),("CAP","Pearl"),("TYPE","4-part"),("COLOR","Custom")]),
 # jeans
 "jeans-move":    ("MOVE-SHANK JEANS BUTTON","DENIM · tack", jeans_tack,
                   [("MATERIAL","Iron/brass"),("SIZE","17–20 mm"),("SHANK","Move"),("LOGO","Emboss")]),
 "jeans-fixed":   ("FIXED TACK BUTTON","DENIM · tack", jeans_tack,
                   [("MATERIAL","Iron/brass"),("SIZE","17–25 mm"),("SHANK","Fixed"),("LOGO","Emboss")]),
 "jeans-rivet":   ("LOGO RIVET & BURR","DENIM · rivet", lambda: flat_button("url(#brassG)",0),
                   [("MATERIAL","Brass"),("SIZE","7–11 mm"),("LOGO","Emboss"),("SET","Burr")]),
 "jeans-donut":   ("DONUT / HOLLOW BUTTON","DENIM · hollow", eyelet,
                   [("MATERIAL","Iron"),("SIZE","17–20 mm"),("TYPE","Hollow"),("FINISH","Plated")]),
 # natural
 "nat-corozo":    ("COROZO SHIRT BUTTON","NATURAL · tagua", lambda: flat_button("#D8C7A0",4),
                   [("MATERIAL","Corozo"),("SIZE","11–18 mm"),("ECO","Yes"),("HOLES","4")]),
 "nat-horn":      ("BUFFALO HORN SUIT BUTTON","NATURAL · horn", lambda: flat_button("#2E2620",4),
                   [("MATERIAL","Horn"),("SIZE","18–28 mm"),("FINISH","Polished"),("HOLES","4")]),
 "nat-wood":      ("ENGRAVED WOOD BUTTON","NATURAL · wood", lambda: flat_button("#9A7B4F",2),
                   [("MATERIAL","Wood"),("SIZE","12–20 mm"),("LOGO","Laser"),("HOLES","2")]),
 "nat-coconut":   ("COCONUT SHELL BUTTON","NATURAL · coco", lambda: flat_button("#6B4E34",4),
                   [("MATERIAL","Coconut"),("SIZE","11–20 mm"),("ECO","Yes"),("HOLES","4")]),
 # hardware
 "hw-cordlock":   ("SPRING CORD LOCK","HARDWARE · stopper", cord_lock,
                   [("MATERIAL","POM/metal"),("CORD","3–6 mm"),("TYPE","Spring"),("HOLES","1–2")]),
 "hw-eyelet":     ("BRASS EYELET & GROMMET","HARDWARE · eyelet", eyelet,
                   [("MATERIAL","Brass"),("INNER","4–12 mm"),("SET","Washer"),("PLATE","Multi")]),
 "hw-buckle":     ("SIDE-RELEASE BUCKLE","HARDWARE · buckle", buckle,
                   [("MATERIAL","POM"),("WEBBING","10–50 mm"),("TYPE","Quick"),("COLOR","Custom")]),
 "hw-cordend":    ("METAL CORD END / ADJUSTER","HARDWARE · cord end", cord_lock,
                   [("MATERIAL","Zinc"),("CORD","3–5 mm"),("FINISH","Plated"),("LOGO","Option")]),
}

for fname,(title,sub,fn,specs) in ITEMS.items():
    svg = head(title, sub) + fn() + foot(specs)
    open(f"{OUT}/{fname}.svg","w").write(svg)

print(f"已生成 {len(ITEMS)} 张产品规格图 → {OUT}/")
