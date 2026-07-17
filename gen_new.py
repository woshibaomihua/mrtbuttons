# -*- coding: utf-8 -*-
"""Build Merit Trims optimizations onto the base site:
 - inject Catalogue + Instant Quote into global nav
 - inject GA4 placeholder
 - generate /catalogue.html (filter all 843 SKUs) + /instant-quote.html (configurator)
 - write tools.css, catalogue.js, quote.js
 - soften certification wording (compliance-safe)
 - refresh sitemap.xml + llms.txt
"""
import re, json, os, glob, html

DOMAIN = "https://www.merittrims.com"
WA = "8615869483966"
EMAIL = "maggie@merittrims.com"

html_files = glob.glob("**/*.html", recursive=True)

# ---------------------------------------------------------------- nav + GA4
NAV_CAT = ('
')
NAV_CAT_NEW = NAV_CAT + ('\n        <a href="/catalogue">Full Catalogue <span>browse all 843 styles</span></a>'
                         '\n        <a href="/instant-quote">Instant Quote Tool <span>price &amp; MOQ in seconds</span></a>')
NAV_TOP = '<a href="/custom-buttons">Custom Buttons</a>'
NAV_TOP_NEW = '<a href="/instant-quote">Instant Quote</a>\n    ' + NAV_TOP

GA = ('\n<!-- Google Analytics 4 — replace G-XXXXXXXXXX with your real Measurement ID to activate -->'
      '\n<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>'
      '\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
      "gtag('js',new Date());/* gtag('config','G-XXXXXXXXXX'); */</script>\n")

for f in html_files:
    s = open(f, encoding="utf-8").read(); o = s
    if NAV_CAT in s and "/catalogue" not in s:
        s = s.replace(NAV_CAT, NAV_CAT_NEW)
    if NAV_TOP in s and '>Instant Quote<' not in s:
        s = s.replace(NAV_TOP, NAV_TOP_NEW, 1)
    if "googletagmanager" not in s:
        s = s.replace("</head>", GA + "</head>", 1)
    if s != o:
        open(f, "w", encoding="utf-8").write(s)

# ---------------------------------------------------------------- chrome
idx = open("index.html", encoding="utf-8").read()
HEADER = re.search(r'(<div class="topbar">.*?</header>)', idx, re.S).group(1)
FOOTER = re.search(r'(<footer class="site">.*?</html>)', idx, re.S).group(1)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Inter:wght@400;450;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

def page(path, title, desc, main, jsonld="", extra_js=""):
    canon = DOMAIN + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Merit Trims">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/images/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="stylesheet" href="/assets/css/v3.css">
<link rel="stylesheet" href="/assets/css/tools.css">
{jsonld}{GA}</head>
<body>
{HEADER}
<main>
{main}
</main>
{FOOTER.replace('<script src="assets/js/main.js" defer></script>', '<script src="/assets/js/main.js" defer></script>'+extra_js)}"""

# ---------------------------------------------------------------- catalogue page
cat_main = """
<section class="t-hero">
  <div class="wrap">
    <p class="t-eyebrow">Full catalogue · 843 styles</p>
    <h1>Browse every button &amp; trim we make</h1>
    <p class="t-lead">Filter our complete production range by category, material and keyword. Found something close? Request a quote or send us a reference — we customise logo, size, color and plating on any style.</p>
  </div>
</section>
<section class="wrap t-cat">
  <div class="t-toolbar">
    <input id="t-search" type="search" placeholder="Search 843 styles (e.g. metal shank, corozo, cord lock)…" aria-label="Search catalogue">
    <select id="t-sort" aria-label="Sort">
      <option value="relevance">Sort: Most relevant</option>
      <option value="price-asc">Price: Low to High</option>
      <option value="price-desc">Price: High to Low</option>
    </select>
  </div>
  <div id="t-chips" class="t-chips"></div>
  <div class="t-layout">
    <aside class="t-filters">
      <div id="t-sub"></div>
      <div id="t-mat"></div>
    </aside>
    <div>
      <div class="t-count" id="t-count"></div>
      <div id="t-grid" class="t-grid"></div>
      <div class="t-center"><button id="t-more" class="btn primary">Load more</button></div>
    </div>
  </div>
</section>
"""
cat_jsonld = ('<script type="application/ld+json">'
    + json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"Merit Trims Full Catalogue",
       "url":DOMAIN+"/catalogue","description":"Browse all 843 button and garment-trim styles by category, material and keyword.",
       "isPartOf":{"@id":DOMAIN+"/#website"}}) + '</script>')

open("catalogue.html","w",encoding="utf-8").write(
    page("/catalogue",
         "Full Button & Trims Catalogue — 843 Styles | Merit Trims",
         "Browse all 843 custom button and garment-trim styles by Merit Trims. Filter by category, material and keyword; request a quote with logo, size and color customization.",
         cat_main, cat_jsonld, extra_js='<script src="/assets/js/catalogue.js" defer></script>'))

# ---------------------------------------------------------------- instant quote page
quote_main = """
<section class="t-hero t-hero--quote">
  <div class="wrap">
    <p class="t-eyebrow">Instant quote tool</p>
    <h1>Price &amp; MOQ in seconds — then we confirm</h1>
    <p class="t-lead">Configure your button or trim and get an indicative unit price, MOQ and matching styles drawn from our live production range. Send it through and Maggie replies with a firm quote within 12 hours.</p>
  </div>
</section>
<section class="wrap t-quote">
  <div class="t-q-grid">
    <div class="t-q-config">
      <div class="t-step"><span class="t-step-n">1</span><h3>Choose a product</h3></div>
      <div id="q-cats" class="t-opts"></div>
      <div class="t-step"><span class="t-step-n">2</span><h3>Material</h3></div>
      <div id="q-mats" class="t-opts"></div>
      <div class="t-step"><span class="t-step-n">3</span><h3>Order quantity</h3></div>
      <div class="t-qty">
        <input id="q-qty" type="range" min="100" max="100000" step="100" value="5000">
        <output id="q-qty-out">5,000 pcs</output>
      </div>
      <div class="t-step"><span class="t-step-n">4</span><h3>Logo customization</h3></div>
      <div id="q-logo" class="t-opts t-opts--sm">
        <button class="t-opt is-on" data-v="Custom logo">Custom logo</button>
        <button class="t-opt" data-v="No logo">No logo</button>
      </div>
    </div>
    <aside class="t-q-result">
      <div class="t-q-card">
        <p class="t-q-k">Indicative unit price</p>
        <p class="t-q-price" id="q-price">—</p>
        <div class="t-q-row"><span>Typical MOQ</span><b id="q-moq">—</b></div>
        <div class="t-q-row"><span>Est. order value</span><b id="q-value">—</b></div>
        <div class="t-q-row"><span>Sampling</span><b>5–7 days</b></div>
        <p class="t-q-note">Indicative only, based on our live range. Final price depends on size, plating and logo — confirmed in your written quote.</p>
        <form id="q-form" class="inq" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" data-email="maggie@merittrims.com">
          <input type="hidden" name="_subject" value="Instant-quote request">
          <input type="hidden" name="configured_spec" id="q-spec">
          <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
          <input type="text" name="name" placeholder="Your name" required>
          <input type="email" name="email" placeholder="Work email" required>
          <input type="text" name="whatsapp" placeholder="WhatsApp (optional)">
          <button class="btn primary block" type="submit">Get my firm quote</button>
        </form>
        <a class="t-q-wa" href="#" id="q-wa" target="_blank" rel="noopener">or send this spec on WhatsApp →</a>
      </div>
    </aside>
  </div>
  <div class="t-q-matches">
    <h3>Matching styles from our range</h3>
    <div id="q-styles" class="t-grid"></div>
  </div>
</section>
"""
quote_jsonld = ('<script type="application/ld+json">'
    + json.dumps({"@context":"https://schema.org","@type":"WebApplication","name":"Merit Trims Instant Quote Tool",
       "url":DOMAIN+"/instant-quote","applicationCategory":"BusinessApplication","operatingSystem":"Web",
       "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},
       "description":"Configure a custom button or garment trim and get an indicative unit price and MOQ instantly."}) + '</script>')

open("instant-quote.html","w",encoding="utf-8").write(
    page("/instant-quote",
         "Instant Button Quote Tool — Price & MOQ Calculator | Merit Trims",
         "Configure your custom button or trim and get an indicative unit price, MOQ and matching styles instantly, then receive a firm quote from Merit Trims within 12 hours.",
         quote_main, quote_jsonld, extra_js='<script src="/assets/js/quote.js" defer></script>'))

print("built catalogue.html + instant-quote.html; nav + GA injected into", len(html_files), "pages")
