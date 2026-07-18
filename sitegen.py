#!/usr/bin/env python3
"""sitegen.py — shared layout, SEO meta, JSON-LD helpers for Merit Trims site.

⚠️  DEPRECATED — DO NOT RUN THIS OR ANY gen_*.py SCRIPT.
This was the one-off scaffold generator. The live site has since been
hand-maintained and is the single source of truth: it has 28 pages (incl. 7
hardware/trim category pages), an updated homepage, and a 27-URL sitemap that
these generators do NOT reproduce. ROOT below is also a stale Linux path that
does not exist on this machine. Re-running gen_core.py / gen_pages.py /
gen_sitemap.py will OVERWRITE and regress the current pages.
To change the site, edit the HTML files directly.
"""
import os, json

ROOT = "/home/claude/merittrims-site"  # STALE PATH — do not run this generator
DOMAIN = "https://mrtbuttons.com"   # ← 上线前全局替换为你的真实域名
COMPANY = "Wenzhou Merit Garment Co., Ltd."
BRAND = "Merit Trims"
EMAIL = "mrtmaggie0010@gmail.com"          # ← 替换为真实邮箱
PHONE = "+86 15869483966"               # ← 替换为真实电话
WHATSAPP = "8615869483966"               # ← 替换为真实WhatsApp号码（国家码+号码，无+号）
ADDRESS = "Louqiao Industrial Zone, Ouhai District, Wenzhou, Zhejiang 325000, China"

LOGO_SVG = '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="#283A52"/><circle cx="20" cy="20" r="14.5" fill="none" stroke="#C9A961" stroke-width="1.6"/><circle cx="15" cy="15" r="2.6" fill="#E8D9B5"/><circle cx="25" cy="15" r="2.6" fill="#E8D9B5"/><circle cx="15" cy="25" r="2.6" fill="#E8D9B5"/><circle cx="25" cy="25" r="2.6" fill="#E8D9B5"/><path d="M15 15 L25 25 M25 15 L15 25" stroke="#C9A961" stroke-width="2.2" stroke-linecap="round"/></svg>'''

WA_ICON = '<img class="wa-float__icon" src="/images/whatsapp-float-custom.png" alt="WhatsApp" width="1280" height="1280" loading="lazy">'

def nav_active(page_id, target):
    return ' aria-current="page"' if page_id == target else ''

def layout(*, page_id, title, description, canonical_path, body, jsonld=None,
           depth=0, og_image="/images/og-default.png", noindex=False):
    """Wrap body content in the full HTML shell."""
    pre = "../" * depth
    canonical = DOMAIN + canonical_path
    jsonld_blocks = ""
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": DOMAIN + "/#organization",
        "name": COMPANY,
        "alternateName": BRAND,
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/images/logo.png",
        "description": "Custom garment buttons manufacturer in Wenzhou, China: resin, metal, snap, jeans, corozo and horn buttons, cord locks, eyelets and buckles for apparel brands worldwide.",
        "foundingLocation": {"@type": "Place", "name": "Wenzhou, Zhejiang, China"},
        "address": {"@type": "PostalAddress", "streetAddress": "Louqiao Industrial Zone, Ouhai District",
                    "addressLocality": "Wenzhou", "addressRegion": "Zhejiang", "postalCode": "325000", "addressCountry": "CN"},
        "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": EMAIL,
                          "telephone": PHONE, "availableLanguage": ["en", "zh"]}],
        "sameAs": ["https://merittrims.en.alibaba.com/"]
    }
    blocks = [org] + (jsonld or [])
    for b in blocks:
        jsonld_blocks += '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + '</script>\n'

    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{robots}
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400;1,9..144,500&family=Inter:wght@400;450;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/style.css">
<link rel="stylesheet" href="{pre}assets/css/v3.css">
{jsonld_blocks}</head>
<body>
<div class="topbar"><div class="wrap">
  <span>Factory-direct garment buttons · Wenzhou, China · Exporting since 2008</span>
  <span><a href="mailto:{EMAIL}">{EMAIL}</a> &nbsp;·&nbsp; <a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp</a></span>
</div></div>
<header class="site"><div class="wrap nav">
  <a class="brand" href="/" aria-label="{BRAND} home">{LOGO_SVG}<span>Merit Trims<small>Wenzhou Merit Garment Co., Ltd.</small></span></a>
  <button class="hamb" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="menu" aria-label="Main">
    <a href="/"{nav_active(page_id,'home')}>Home</a>
    <span class="has-sub">
      <a href="/products/"{nav_active(page_id,'products')}>Products</a>
      <span class="sub">
        <a href="/products/resin-buttons">Resin &amp; Polyester Buttons <span>4-hole · 2-hole · pearl · shank</span></a>
        <a href="/products/metal-buttons">Metal Buttons <span>zinc alloy · brass · engraved logo</span></a>
        <a href="/products/snap-buttons">Snap Buttons / Fasteners <span>spring · ring · prong snaps</span></a>
        <a href="/products/jeans-buttons">Jeans &amp; Tack Buttons <span>denim hardware · rivets</span></a>
        <a href="/products/natural-buttons">Corozo, Horn &amp; Wood <span>natural · sustainable</span></a>
</span>
    </span>
    <a href="/custom-buttons"{nav_active(page_id,'custom')}>Custom Buttons</a>
    <a href="/about"{nav_active(page_id,'about')}>About</a>
    <a href="/blog/"{nav_active(page_id,'blog')}>Blog</a>
    <a href="/faq"{nav_active(page_id,'faq')}>FAQ</a>
    <a href="/contact"{nav_active(page_id,'contact')}>Contact</a>
  </nav>
  <a class="btn sm brass" href="/contact">Get a Quote</a>
</div></header>

{body}

<section class="cta-band"><div class="wrap">
  <div><h2>Send your tech pack or a photo — get a quote in 12 hours</h2>
  <p>Free samples for stock items · Low MOQ from 500–1,000 pcs · OEKO-TEX® compliant materials</p></div>
  <a class="btn brass" href="/contact">Request a Quote</a>
</div></section>

<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <div class="f-brand">Merit Trims</div>
      <p>{COMPANY} — factory-direct manufacturer of garment buttons and trims in Wenzhou, the button capital of China. Serving apparel brands, uniform makers and trim wholesalers in 60+ countries.</p>
      <p class="mono">{ADDRESS}</p>
    </div>
    <div>
      <h3>Products</h3>
      <a href="/products/resin-buttons">Resin Buttons</a><br>
      <a href="/products/metal-buttons">Metal Buttons</a><br>
      <a href="/products/snap-buttons">Snap Buttons</a><br>
      <a href="/products/jeans-buttons">Jeans Buttons</a><br>
      <a href="/products/natural-buttons">Corozo &amp; Horn Buttons</a><br>
</div>
    <div>
      <h3>Company</h3>
      <a href="/about">About Us</a><br>
      <a href="/custom-buttons">Custom Service</a><br>
      <a href="/blog/">Blog &amp; Guides</a><br>
      <a href="/faq">FAQ</a><br>
      <a href="/contact">Contact &amp; RFQ</a><br>
      <a href="https://merittrims.en.alibaba.com/" rel="noopener">Alibaba Storefront</a>
    </div>
    <div>
      <h3>Contact</h3>
      <a href="mailto:{EMAIL}">{EMAIL}</a><br>
      <a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp: +{WHATSAPP}</a><br>
      <a href="tel:{PHONE}">{PHONE}</a><br>
      <p style="margin-top:10px">Mon–Sat 8:30–18:00 (GMT+8)<br>Replies within 12 hours, any time zone.</p>
    </div>
  </div>
  <div class="legal">
    <span>© <span class="year">2026</span> {COMPANY}. All rights reserved.</span>
    <span><a href="/sitemap.xml">Sitemap</a></span>
  </div>
</div></footer>

<a class="wa-float" href="https://wa.me/{WHATSAPP}?text=Hi%2C%20I%27d%20like%20a%20quote%20for%20buttons" rel="noopener" aria-label="Chat on WhatsApp">{WA_ICON}</a>
<script src="{pre}assets/js/main.js" defer></script>
</body>
</html>'''

def write_page(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)

def breadcrumb_ld(items):
    """items: list of (name, path or None for current)"""
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             **({"item": DOMAIN + p} if p else {})}
            for i, (n, p) in enumerate(items)
        ]
    }

def faq_ld(pairs):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
    }

def faq_html(pairs):
    out = ""
    for q, a in pairs:
        out += f'<details class="faq"><summary>{q}</summary><div class="a"><p>{a}</p></div></details>\n'
    return out
