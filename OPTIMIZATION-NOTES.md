# Merit Trims — optimization pass (what changed & what's left)

This package builds on the previous `meritbutton-site` and applies the agreed
optimizations. Brand is now **Merit Trims** (domain `merittrims.com`) with your
real contact details.

## ✅ Done in this pass

### Contact / brand (your data)
- Email → **mrtmaggie0010@gmail.com** (every page, footer, schema, form fallback)
- WhatsApp → **+86 15869483966** (`wa.me/8615869483966`) — topbar, footer, float button, tools
- Domain → **merittrims.com** across canonical / OG / sitemap / schema / llms.txt
- Rebranded "Merit Button" → "Merit Trims"; legal entity → "Merit Trims (Wenzhou) Co., Ltd."

### Performance (the biggest defect fixed)
- **All raster images converted to WebP** (OG image → compressed JPG for social compatibility) and resized to sensible caps.
  - Image payload **3,831 KB → 925 KB (−76%)**; `images/` folder now ~1 MB total.
- Hero image **preloaded** with `fetchpriority="high"` (faster LCP).
- All image references in HTML/CSS rewritten to the new files; **0 broken references** verified.

### New high-value pages (use the 843-SKU data asset)
- **/catalogue** — filterable browser over **all 843 styles** (category, sub-type, material, search, sort, load-more). Each card → one-click WhatsApp quote. Adds depth + long-tail SEO; CollectionPage schema.
- **/instant-quote** — interactive **configurator** (category → material → quantity → logo) that computes an **indicative unit price, MOQ and est. order value from your live range**, shows matching styles, and captures the lead (form + WhatsApp). This is the differentiator few peers offer. WebApplication schema.
- Both wired into the **global navigation** (Products submenu + top-level "Instant Quote") on every page.

### Trust / compliance wording
- Certification row reworded to a compliance-safe claim: *"We manufacture to these standards — SGS/Intertek test reports & certificates available on request."* (No false "we are certified" claims.)

### Analytics
- **GA4 snippet** added site-wide (placeholder `G-XXXXXXXXXX`, config line commented until you paste your real ID).

### SEO
- `sitemap.xml` (now 18 URLs) and `llms.txt` updated with the new pages and domain.

## 🔴 Before you launch (P0 — needs your accounts/data)
1. **Form backend** — create a free Formspree form and replace `YOUR_FORM_ID` in `contact.html`, `index.html`, `instant-quote.html` (`action="https://formspree.io/f/…"`). Until then the form falls back to a `mailto:mrtmaggie0010@gmail.com`.
2. **GA4** — replace `G-XXXXXXXXXX` (3 lines per page) and uncomment the `gtag('config', …)` line; connect Google Search Console + Bing.
3. **Verify the hard facts** — Wenzhou address, "MOQ 500", "12-hour quote", "exporting since 2008", "98% on-time", "60+ countries". Keep only what is true.
4. **Certifications** — swap the badge SVGs for certificates you actually hold, or keep the "available on request" wording and remove badges you can't back up.
5. **Domain** — point `merittrims.com` DNS to your host (Vercel-ready via `vercel.json` cleanUrls).

## 🟡 Recommended next (P1–P3, not yet done)
- **Curated product detail pages** (~20–40 best SKUs) with `Product`+`Offer` schema and real photos → more long-tail capture. (Catalogue currently routes to WhatsApp quote rather than per-SKU pages.)
- **Expand the blog** 3 → 10–12 buying guides (size, material, MOQ, plating, sustainability, tech-pack prep) for AEO authority.
- **PDF line-card** lead magnet (could not be generated here — the PDF library's crypto dependency is broken in this build env; generate on your machine or export `/catalogue` to print-PDF).
- **Real social proof** — client logos, named testimonials, factory photos/video, case studies.

## Rebuild / preview
```bash
# preview (clean URLs need a host that rewrites; basic preview):
python3 -m http.server 8000     # serve from this folder root
# new pages are data-driven — /data/product-data.json must be served (it is)
```
Deploy: import the folder to **Vercel** (uses `vercel.json`). `/catalogue` and
`/instant-quote` resolve via `cleanUrls`.

## Update — homepage product section restructured

The single "Six product families" grid was split into two clear sections:

**01 / Buttons (main line)** — 6 sub-family cards: Resin & Polyester, Metal,
Snap, Jeans & Tack, Corozo/Horn/Wood, and **Rhinestone/Pearl & Cover** (new).

**02 / Trims & Accessories** — 8 cards, each with its sub-types:
Zippers (nylon·resin·metal·invisible·waterproof·adhesive) · Cord Stoppers
(metal·plastic·spring) · Cords, Webbing & Tapes (drawcord·elastic·hook&loop) ·
Buckles (metal·plastic·side-release) · Eyelets & Pants Hooks · Labels & Tags ·
Hardware · + a "Browse all 843 styles" card → /catalogue (deep-links filter the catalogue).

### Real photos (important)
This sandbox cannot download images — **every image host (Amazon, eBay, Etsy,
Shopify, alicdn, Walmart…) returns HTTP 403** from the build IP. So each new
category card uses `<img src="/images/cat-*.webp">` with an `onerror` fallback to
a **sourced real product-photo URL** — meaning the real photo shows immediately
in your browser (no SVG), and once you localise the files it uses the local WebP.

The source URLs are recorded in `tools/images-map.txt`. To localise for production:
run the existing `tools/replace_images.py` (in an environment with normal internet)
to download them to `/images/cat-*.webp`, then they load locally.

⚠️ The sourced photos are third-party reference images (marketplace listings).
Before commercial launch, replace them with **your own or licensed product
photography** — ideally your real factory shots, dropped in at the same filenames.
