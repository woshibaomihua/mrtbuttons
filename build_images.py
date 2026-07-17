#!/usr/bin/env python3
"""Generate professional SVG placeholder illustrations for each product category."""
import os

OUT = "/home/claude/merittrims-site/images"
os.makedirs(OUT, exist_ok=True)

PALETTES = {
    "resin":   {"bg": "#EDE9DE", "main": "#F6F1E7", "rim": "#D9CDB4", "accent": "#B08D3E", "label": "RESIN · POLYESTER"},
    "metal":   {"bg": "#E4E6EA", "main": "#C9CDD4", "rim": "#9AA1AC", "accent": "#283A52", "label": "METAL · ALLOY"},
    "snap":    {"bg": "#E8E4DA", "main": "#C9A961", "rim": "#9A7A32", "accent": "#283A52", "label": "SNAP FASTENER"},
    "jeans":   {"bg": "#DDE3EC", "main": "#B08D3E", "rim": "#8A6C2C", "accent": "#283A52", "label": "JEANS · TACK"},
    "natural": {"bg": "#EAE4D5", "main": "#D7C7A8", "rim": "#A98F62", "accent": "#6B5232", "label": "COROZO · HORN · WOOD"},
    "hardware":{"bg": "#E6E8E4", "main": "#AEB6B0", "rim": "#7E867F", "accent": "#283A52", "label": "CORD LOCK · EYELET"},
}

def button_svg(name, p, holes=4, shank=False, ring=False):
    cx, cy, r = 400, 280, 170
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="{p['label']} button illustration">
<rect width="800" height="600" fill="{p['bg']}"/>
<g opacity="0.35">
  <line x1="60" y1="540" x2="740" y2="540" stroke="{p['accent']}" stroke-width="1"/>
  {''.join(f'<line x1="{60+i*34}" y1="{533 if i%5 else 526}" x2="{60+i*34}" y2="540" stroke="{p["accent"]}" stroke-width="1"/>' for i in range(21))}
</g>
<circle cx="{cx}" cy="{cy+10}" r="{r}" fill="#1E2229" opacity="0.10"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="{p['main']}" stroke="{p['rim']}" stroke-width="6"/>
<circle cx="{cx}" cy="{cy}" r="{r-28}" fill="none" stroke="{p['rim']}" stroke-width="2.5" opacity="0.7"/>
<ellipse cx="{cx-55}" cy="{cy-70}" rx="62" ry="34" fill="#FFFFFF" opacity="0.45" transform="rotate(-28 {cx-55} {cy-70})"/>''']
    if ring:
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="{p["bg"]}" stroke="{p["rim"]}" stroke-width="6"/>')
    elif shank:
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="20" fill="{p["rim"]}" opacity="0.85"/>')
    elif holes == 4:
        for dx, dy in [(-30,-30),(30,-30),(-30,30),(30,30)]:
            parts.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="13" fill="{p["bg"]}" stroke="{p["rim"]}" stroke-width="3"/>')
        parts.append(f'<path d="M{cx-30} {cy-30} L{cx+30} {cy+30} M{cx+30} {cy-30} L{cx-30} {cy+30}" stroke="{p["accent"]}" stroke-width="7" stroke-linecap="round" opacity="0.55"/>')
    elif holes == 2:
        for dx in (-32, 32):
            parts.append(f'<circle cx="{cx+dx}" cy="{cy}" r="14" fill="{p["bg"]}" stroke="{p["rim"]}" stroke-width="3"/>')
        parts.append(f'<line x1="{cx-32}" y1="{cy}" x2="{cx+32}" y2="{cy}" stroke="{p["accent"]}" stroke-width="7" stroke-linecap="round" opacity="0.55"/>')
    parts.append(f'''<text x="400" y="565" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="22" letter-spacing="4" fill="{p['accent']}">{p['label']}</text>
<text x="740" y="520" text-anchor="end" font-family="IBM Plex Mono, monospace" font-size="18" fill="{p['accent']}" opacity="0.6">18L · 11.5 mm</text>
</svg>''')
    with open(os.path.join(OUT, name), "w") as f:
        f.write("".join(parts))

button_svg("cat-resin-buttons.svg",  PALETTES["resin"],   holes=4)
button_svg("cat-metal-buttons.svg",  PALETTES["metal"],   shank=True)
button_svg("cat-snap-buttons.svg",   PALETTES["snap"],    ring=True)
button_svg("cat-jeans-buttons.svg",  PALETTES["jeans"],   shank=True)
button_svg("cat-natural-buttons.svg",PALETTES["natural"], holes=2)
button_svg("cat-hardware.svg",       PALETTES["hardware"],ring=True)

# hero engineering-drawing button
hero = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640" role="img" aria-label="Engineering drawing of a four-hole button with ligne dimensions">
<defs>
  <radialGradient id="g1" cx="38%" cy="32%" r="75%">
    <stop offset="0%" stop-color="#F3EDDE"/><stop offset="60%" stop-color="#D8CBAA"/><stop offset="100%" stop-color="#B49A6A"/>
  </radialGradient>
</defs>
<g stroke="#7E8CA3" stroke-width="1" opacity="0.55">
  <line x1="320" y1="20" x2="320" y2="620" stroke-dasharray="10 6"/>
  <line x1="20" y1="320" x2="620" y2="320" stroke-dasharray="10 6"/>
</g>
<circle cx="320" cy="320" r="218" fill="url(#g1)" stroke="#E8D9B5" stroke-width="4"/>
<circle cx="320" cy="320" r="186" fill="none" stroke="#8A6C2C" stroke-width="2" opacity="0.6"/>
<circle cx="320" cy="320" r="80" fill="none" stroke="#8A6C2C" stroke-width="1.4" stroke-dasharray="6 5" opacity="0.7"/>
<g>
  <circle cx="282" cy="282" r="17" fill="#283A52" opacity="0.92"/>
  <circle cx="358" cy="282" r="17" fill="#283A52" opacity="0.92"/>
  <circle cx="282" cy="358" r="17" fill="#283A52" opacity="0.92"/>
  <circle cx="358" cy="358" r="17" fill="#283A52" opacity="0.92"/>
</g>
<path d="M282 282 L358 358 M358 282 L282 358" stroke="#E8D9B5" stroke-width="9" stroke-linecap="round" opacity="0.9"/>
<ellipse cx="248" cy="232" rx="84" ry="44" fill="#FFFFFF" opacity="0.35" transform="rotate(-30 248 232)"/>
<g font-family="IBM Plex Mono, monospace" fill="#C7CFDB" font-size="17">
  <line x1="102" y1="560" x2="538" y2="560" stroke="#C9A961" stroke-width="1.4"/>
  <line x1="102" y1="552" x2="102" y2="568" stroke="#C9A961" stroke-width="1.4"/>
  <line x1="538" y1="552" x2="538" y2="568" stroke="#C9A961" stroke-width="1.4"/>
  <text x="320" y="592" text-anchor="middle" fill="#E8D9B5">Ø 27.5 mm — 44L</text>
  <text x="320" y="70" text-anchor="middle" fill="#9FACBF">DRG NO. MB-44L-04 · 4-HOLE FLAT BACK</text>
</g>
</svg>'''
open(os.path.join(OUT, "hero-button-drawing.svg"), "w").write(hero)

# factory / about placeholder
factory = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" role="img" aria-label="Factory illustration placeholder">
<rect width="800" height="500" fill="#283A52"/>
<g fill="#1C2A3E"><rect x="60" y="200" width="200" height="220"/><rect x="300" y="150" width="240" height="270"/><rect x="580" y="230" width="160" height="190"/></g>
<g fill="#C9A961" opacity="0.9">
  <polygon points="60,200 110,160 160,200"/><polygon points="160,200 210,160 260,200"/>
  <polygon points="300,150 360,105 420,150"/><polygon points="420,150 480,105 540,150"/>
  <polygon points="580,230 630,195 680,230"/><polygon points="680,230 705,212 740,230"/>
</g>
<g fill="#E8D9B5" opacity="0.85">
  <rect x="84" y="240" width="34" height="40"/><rect x="140" y="240" width="34" height="40"/><rect x="196" y="240" width="34" height="40"/>
  <rect x="330" y="195" width="40" height="48"/><rect x="396" y="195" width="40" height="48"/><rect x="462" y="195" width="40" height="48"/>
  <rect x="604" y="266" width="30" height="36"/><rect x="656" y="266" width="30" height="36"/>
</g>
<rect x="0" y="420" width="800" height="80" fill="#16202F"/>
<text x="400" y="468" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="20" letter-spacing="5" fill="#C9A961">WENZHOU · ZHEJIANG · CHINA</text>
</svg>'''
open(os.path.join(OUT, "factory-placeholder.svg"), "w").write(factory)

print("done:", sorted(os.listdir(OUT)))
