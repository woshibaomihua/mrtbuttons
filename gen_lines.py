# -*- coding: utf-8 -*-
"""Rebuild the homepage product section into:
   A) Buttons (6 sub-families)  B) Trims & accessories (zippers, cord stoppers,
   cords/webbing, buckles, eyelets/hooks, labels, hardware + browse-all).
Real product photos: <img src=local webp> with onerror fallback to a sourced
real photo URL (shows immediately in a browser, localises cleanly for prod).
"""
import re

idx = open("index.html", encoding="utf-8").read()

# sourced real product photos (load in browser; localise via images-map.txt)
REMOTE = {
 "cat-rhinestone": "https://m.media-amazon.com/images/I/714ceB02jIL._AC_UF894,1000_QL80_.jpg",
 "cat-zippers":    "https://m.media-amazon.com/images/I/71v1etJOQTL._AC_UF894,1000_QL80_.jpg",
 "cat-cord-stoppers":"https://m.media-amazon.com/images/I/71lSXR7yoJL._AC_UY1000_.jpg",
 "cat-cords-webbing":"https://m.media-amazon.com/images/I/81Oj6alCdcL._AC_UF894,1000_QL80_.jpg",
 "cat-buckles":    "https://m.media-amazon.com/images/I/619UZHeodPL._AC_UF894,1000_QL80_.jpg",
 "cat-eyelets":    "https://m.media-amazon.com/images/I/71Js9Gl2ieL._AC_UF894,1000_QL80_.jpg",
 "cat-labels":     "https://m.media-amazon.com/images/I/61l5RHwAG3L._AC_UF894,1000_QL80_.jpg",
}

def img(slug, alt):
    """local webp src with real-photo URL fallback (no SVG)."""
    remote = REMOTE[slug]
    return (f'<img src="/images/{slug}.webp" alt="{alt}" loading="lazy" '
            f'referrerpolicy="no-referrer" '
            f'onerror="this.onerror=null;this.src=\'{remote}\'">')

def card(tag, image_html, href, title, meta, desc, more):
    return f'''    <article class="card">
      <div class="ph"><span class="tag">{tag}</span>{image_html}<div class="ph-overlay">{meta}</div></div>
      <div class="body"><h3><a href="{href}">{title}</a></h3>
      <p class="meta">{meta}</p>
      <p>{desc}</p>
      <a class="more" href="{href}">{more}</a></div>
    </article>'''

# ---- existing 5 button photo cards (kept verbatim) + rhinestone ----
btn_existing = re.search(r'<div class="grid c3 cat">(.*?)</div>\s*</div></section>', idx, re.S).group(1)
# keep only the 5 button articles (drop the 6th "Cord Locks" trims card → moves to accessories)
arts = re.findall(r'<article class="card">.*?</article>', btn_existing, re.S)
btn_cards = "\n".join(a for a in arts if "cord-stoppers" not in a)  # 5 button cards
rhinestone = card("DECOR", img("cat-rhinestone","Rhinestone and faux-pearl decorative shank buttons on white"),
    "/catalogue?cat=buttons&sub=rhinestone-pearl-buttons",
    "Rhinestone, Pearl &amp; Cover Buttons",
    "rhinestone · pearl · crystal · fabric-covered",
    "Diamante, faux-pearl and fabric-covered buttons and button covers for womenswear, eveningwear and bridal.",
    "View decorative buttons")
btn_cards = btn_cards + "\n" + rhinestone

# ---- 8 accessory cards (c4) ----
acc = [
 ("ZIPPERS", "cat-zippers", "Nylon coil zipper roll with matching sliders for garments and bags",
  "/catalogue?cat=zippers", "Zippers",
  "nylon · resin · metal · invisible · waterproof · adhesive",
  "No.3–No.8 zippers by the piece or roll, with auto-lock sliders and custom pulls.", "View zippers"),
 ("CORD LOCKS", "cat-cord-stoppers", "Plastic spring cord lock stoppers and toggles in black",
  "/catalogue?cat=cord-stoppers", "Cord Stoppers",
  "metal · plastic · spring · single / double-hole",
  "Spring cord locks and toggles for hoodies, jackets and bags — nickel-free platings.", "View cord stoppers"),
 ("CORDS · TAPES", "cat-cords-webbing", "Woven webbing strap roll with hook and loop tape",
  "/catalogue?cat=cords-webbing-tapes", "Cords, Webbing &amp; Tapes",
  "drawcord · elastic band · elastic cord · hook &amp; loop",
  "Drawstrings, elastics, woven webbing and hook-and-loop (velcro) tape in custom widths.", "View cords &amp; tapes"),
 ("BUCKLES", "cat-buckles", "Plastic side-release buckle for backpack and bag straps",
  "/catalogue?cat=buckles", "Buckles",
  "metal · plastic · side-release · adjuster",
  "Side-release buckles, strap adjusters and bag hardware in zinc alloy and engineering plastic.", "View buckles"),
 ("EYELETS", "cat-eyelets", "Metal eyelets and grommets in silver for garments and canvas",
  "/catalogue?cat=eyelets-hooks", "Eyelets &amp; Pants Hooks",
  "eyelet · grommet · pants hook · hook &amp; bar",
  "Reinforcement eyelets and grommets plus waistband hooks and bars — washable, corrosion-resistant.", "View eyelets &amp; hooks"),
 ("LABELS", "cat-labels", "Custom woven clothing labels and brand tags",
  "/catalogue?cat=labels-tags", "Labels &amp; Tags",
  "woven · metal · leather · PVC · hang tag",
  "Custom woven, metal, leather and silicone labels and hang tags to carry your brand.", "View labels &amp; tags"),
 ("HARDWARE", None, "Cord locks, eyelets and metal hardware accessories",
  "/catalogue?cat=hardware-accessories", "Hardware Accessories",
  "D-ring · O-ring · hook · clasp",
  "Rings, hooks, clasps and connectors to finish bags, straps and accessories.", "View hardware"),
]
acc_cards = []
for tag, slug, alt, href, title, meta, desc, more in acc:
    image_html = (f'<img src="/images/cat-hardware.webp" alt="{alt}" loading="lazy">'
                  if slug is None else img(slug, alt))
    acc_cards.append(card(tag, image_html, href, title, meta, desc, more))
# browse-all card
acc_cards.append(f'''    <article class="card card--cta">
      <div class="ph"><span class="tag">843 STYLES</span><img src="/images/hero-disc.webp" alt="Full Merit Trims catalogue of buttons and trims" loading="lazy"><div class="ph-overlay">filter by category · material · MOQ</div></div>
      <div class="body"><h3><a href="/catalogue">Browse the full catalogue</a></h3>
      <p class="meta">all categories · 843 styles</p>
      <p>Search and filter every button and trim style we make, then request a quote in one click.</p>
      <a class="more" href="/catalogue">Open catalogue</a></div>
    </article>''')
acc_cards = "\n".join(acc_cards)

# ---- assemble two sections, replace the original one ----
new_sections = f'''<section class="band" data-wm="BUTTONS"><div class="wrap">
  <div class="section-head">
    <span class="no">01 / BUTTONS</span>
    <p class="eyebrow">Buttons — our main line</p>
    <h2>Every button your garment needs, made to your spec.</h2>
  </div>
  <div class="grid c3 cat">
{btn_cards}
  </div>
</div></section>

<section class="band alt" data-wm="TRIMS"><div class="wrap">
  <div class="section-head">
    <span class="no">02 / TRIMS &amp; ACCESSORIES</span>
    <p class="eyebrow">Trims &amp; accessories</p>
    <h2>Plus every matching trim — from one supplier.</h2>
  </div>
  <div class="grid c4 cat">
{acc_cards}
  </div>
</div></section>'''

idx2 = re.sub(r'<section class="band" data-wm="CATALOG">.*?</section>', new_sections, idx, count=1, flags=re.S)
assert idx2 != idx, "section not replaced"
open("index.html", "w", encoding="utf-8").write(idx2)
print("homepage rebuilt: 6 button cards + 8 accessory cards")

# ---- record sources in images-map.txt ----
extra = "\n# ── NEW: trims & accessories category photos (added by optimization) ──\n"
extra += "# These show in-browser via remote fallback now; run replace_images.py to localise.\n"
for slug, url in REMOTE.items():
    extra += f"{slug:18s} = {url}\n"
open("tools/images-map.txt", "a", encoding="utf-8").write(extra)
print("appended", len(REMOTE), "image sources to tools/images-map.txt")
