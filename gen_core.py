#!/usr/bin/env python3
"""gen_core.py — homepage, products hub, 6 category pages."""
from sitegen import *

# ---------------------------------------------------------------- HOME
home_faq = [
    ("What is your minimum order quantity (MOQ) for custom buttons?",
     "MOQ starts at 500–1,000 pieces per color and size for most resin and metal buttons. Stock designs can ship from 100 pieces. Custom-mold projects typically start at 5,000 pieces."),
    ("Can you engrave or print our brand logo on buttons?",
     "Yes. We offer laser engraving, embossing/debossing, electroplating, enamel fill and pad printing for logos on resin, metal, snap and jeans buttons. Free digital mock-up before production."),
    ("How fast can you deliver samples and bulk orders?",
     "Stock samples ship in 1–2 days by DHL/FedEx. Custom samples take 5–7 days. Bulk production is typically 10–15 days after sample approval, plus shipping."),
    ("Are your buttons tested and compliant for the EU and US markets?",
     "We supply buttons made with OEKO-TEX® compliant, nickel-free and lead-safe materials, and can arrange third-party testing (SGS/Intertek) for REACH, CPSIA and needle-detection requirements on request."),
]

home_body = f'''
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Garment buttons · Factory direct · Wenzhou, China</p>
    <h1>Custom buttons, <em>engineered to spec</em> for apparel brands worldwide</h1>
    <p class="lead">Merit Trims manufactures resin, metal, snap, jeans, corozo and horn buttons — plus cord locks, eyelets and buckles. From 14L shirt buttons to 44L coat buttons, with your logo, in your Pantone color, at factory prices.</p>
    <div class="cta-row">
      <a class="btn brass" href="/contact">Get a Quote in 12 Hours</a>
      <a class="btn ghost" href="/products/">Browse Product Lines</a>
    </div>
    <div class="spec-strip">
      <div><b>17+</b><span>years exporting</span></div>
      <div><b>60+</b><span>countries served</span></div>
      <div><b>500</b><span>pcs low MOQ</span></div>
      <div><b>12h</b><span>quote response</span></div>
    </div>
  </div>
  <div class="hero-art"><img src="/images/hero-button-drawing.svg" alt="Engineering drawing of a 44-ligne four-hole garment button" width="640" height="640" loading="eager"></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">Product lines</p>
    <h2>Six product families. One supplier. Every closure your garment needs.</h2>
  </div>
  <div class="grid c3">
    <article class="card">
      <div class="ph"><span class="tag">14L–54L</span><img src="/images/cat-resin-buttons.svg" alt="Resin and polyester sewing buttons, 4-hole, in ivory and pearl finishes" loading="lazy"></div>
      <div class="body"><h3><a href="/products/resin-buttons">Resin &amp; Polyester Buttons</a></h3>
      <p class="meta">4-hole · 2-hole · pearl · shank · DTM dye</p>
      <p>Shirt, polo, blouse and suit buttons in any Pantone color. Pearl, matte, marble and engraved-logo finishes.</p>
      <a class="more" href="/products/resin-buttons">View resin buttons</a></div>
    </article>
    <article class="card">
      <div class="ph"><span class="tag">ZINC · BRASS</span><img src="/images/cat-metal-buttons.svg" alt="Custom metal shank buttons in zinc alloy with engraved logo" loading="lazy"></div>
      <div class="body"><h3><a href="/products/metal-buttons">Metal Buttons</a></h3>
      <p class="meta">zinc alloy · brass · shank · sew-on · plated</p>
      <p>Embossed and engraved logo buttons for blazers, coats and uniforms. 10+ plating colors, nickel-free options.</p>
      <a class="more" href="/products/metal-buttons">View metal buttons</a></div>
    </article>
    <article class="card">
      <div class="ph"><span class="tag">4-PART</span><img src="/images/cat-snap-buttons-color-caps.webp" alt="Brass spring snap fastener button set in gold finish" loading="lazy"></div>
      <div class="body"><h3><a href="/products/snap-buttons">Snap Buttons &amp; Fasteners</a></h3>
      <p class="meta">spring snap · ring snap · prong snap · press studs</p>
      <p>Four-part brass and alloy snap fasteners for jackets, workwear, babywear and bags. Logo-engraved caps available.</p>
      <a class="more" href="/products/snap-buttons">View snap buttons</a></div>
    </article>
    <article class="card">
      <div class="ph"><span class="tag">DENIM</span><img src="/images/cat-jeans-buttons.svg" alt="Brass jeans tack button with embossed logo for denim" loading="lazy"></div>
      <div class="body"><h3><a href="/products/jeans-buttons">Jeans &amp; Tack Buttons</a></h3>
      <p class="meta">move/fixed tack · rivets · burrs · 17–25 mm</p>
      <p>Hammer-on denim buttons and rivets with custom embossed logos. Antique brass, copper, gunmetal finishes.</p>
      <a class="more" href="/products/jeans-buttons">View jeans buttons</a></div>
    </article>
    <article class="card">
      <div class="ph"><span class="tag">NATURAL</span><img src="/images/cat-natural-buttons.svg" alt="Natural corozo two-hole button with visible grain" loading="lazy"></div>
      <div class="body"><h3><a href="/products/natural-buttons">Corozo, Horn &amp; Wood Buttons</a></h3>
      <p class="meta">corozo (tagua) · buffalo horn · wood · coconut</p>
      <p>Sustainable natural buttons for premium shirting, suiting and eco-conscious brands. Laser logo engraving.</p>
      <a class="more" href="/products/natural-buttons">View natural buttons</a></div>
    </article>
    <article class="card">
      <div class="ph"><span class="tag">TRIMS</span><img src="/images/cat-hardware.svg" alt="Plastic cord lock stopper and metal eyelet grommet" loading="lazy"></div>
      <div class="body"><h3>
</h3>
      <p class="meta">stoppers · grommets · side-release buckles</p>
      <p>Functional trims for outdoor wear, hoodies and bags: cord stoppers, metal eyelets, adjusters and quick-release buckles.</p>
</div>
    </article>
  </div>
</div></section>

<div class="ruler" role="presentation"></div>

<section class="band tint"><div class="wrap">
  <div class="grid c2" style="align-items:center">
    <div>
      <p class="eyebrow">Why buyers switch to us</p>
      <h2>Factory pricing from the button capital of China — without the trading-company markup</h2>
      <p>Wenzhou produces the majority of the world's garment buttons. We sit inside that supply chain: molds, polishing, dyeing, plating and laser engraving all within our industrial cluster, so you get shorter lead times and 15–30% lower cost than buying through intermediaries.</p>
      <ul class="ticks">
        <li><strong>Low MOQ, real flexibility</strong> — from 500 pcs per color/size; stock items from 100 pcs.</li>
        <li><strong>DTM color matching</strong> — dye-to-match any Pantone or fabric swatch, with lab dips before bulk.</li>
        <li><strong>Logo customization</strong> — laser engraving, embossing, enamel fill, plating in 10+ finishes.</li>
        <li><strong>Compliance-ready</strong> — OEKO-TEX® compliant materials, nickel-free plating, SGS/Intertek testing on request.</li>
        <li><strong>Export experience</strong> — 17+ years shipping to the US, EU, UK, Middle East, South America and Southeast Asia.</li>
      </ul>
      <a class="btn" href="/about">About our factory</a>
    </div>
    <div><img src="/images/factory-placeholder.svg" alt="Merit Trims factory in Wenzhou, Zhejiang, China" loading="lazy" style="border-radius:8px"></div>
  </div>
</div></section>

<section class="band dark"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow" style="color:#C9A961">How ordering works</p>
    <h2>From tech pack to delivered cartons in 5 steps</h2>
  </div>
  <div class="steps">
    <div><h3>Send your requirement</h3><p>A photo, sketch or tech pack with size (mm or ligne), material and quantity is enough to start.</p></div>
    <div><h3>Quote in 12 hours</h3><p>Itemized FOB/CIF quote with material options, MOQ tiers and lead time.</p></div>
    <div><h3>Sample approval</h3><p>Free stock samples, or custom samples in 5–7 days with digital mock-up first.</p></div>
    <div><h3>Production &amp; QC</h3><p>Bulk in 10–15 days. In-line and final inspection, needle detection, pull-force testing for snaps.</p></div>
    <div><h3>Shipping</h3><p>DHL/FedEx/UPS for small lots; sea or air consolidation with full export documents for bulk.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Who we supply</p><h2>Built for B2B buyers</h2></div>
  <div class="grid c4">
    <div class="card"><div class="body"><h3>Apparel brands &amp; designers</h3><p>Custom-logo buttons that match your tech pack, from sampling to repeat bulk programs.</p></div></div>
    <div class="card"><div class="body"><h3>Garment factories</h3><p>Reliable bulk supply with consistent dye lots, carded or bagged per your production line's needs.</p></div></div>
    <div class="card"><div class="body"><h3>Uniform &amp; workwear makers</h3><p>Chef coat buttons, anchor-crest blazer buttons, heavy-duty snaps and jeans tacks that survive industrial laundering.</p></div></div>
    <div class="card"><div class="body"><h3>Trim wholesalers &amp; importers</h3><p>Container and mixed-carton programs, private labeling, and fast restock on best-selling lines.</p></div></div>
  </div>
</div></section>

<section class="band tint"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Quick answers</p><h2>Frequently asked questions</h2></div>
  {faq_html(home_faq)}
  <p style="margin-top:18px"><a class="btn ghost" href="/faq">See all 20 FAQs</a></p>
</div></section>
'''

home_ld = [
    {"@context": "https://schema.org", "@type": "WebSite", "@id": DOMAIN + "/#website",
     "url": DOMAIN + "/", "name": BRAND, "publisher": {"@id": DOMAIN + "/#organization"}},
    faq_ld(home_faq),
]

write_page("index.html", layout(
    page_id="home",
    title="Custom Garment Buttons Manufacturer & Wholesale Supplier | Merit Trims",
    description="Factory-direct buttons manufacturer in Wenzhou, China. Custom resin, metal, snap, jeans, corozo & horn buttons with your logo. Low MOQ 500 pcs, quotes in 12 hours.",
    canonical_path="/", body=home_body, jsonld=home_ld, depth=0))

# ---------------------------------------------------------------- CATEGORY PAGE FACTORY
def category_page(*, slug, page_title, h1, description, lead, img, img_alt, tag,
                  intro_html, spec_rows, products, faqs, related):
    spec_table = '<table class="spec"><thead><tr><th>Attribute</th><th>Specification</th></tr></thead><tbody>'
    for k, v in spec_rows:
        spec_table += f"<tr><td><strong>{k}</strong></td><td>{v}</td></tr>"
    spec_table += "</tbody></table>"

    prod_cards = ""
    item_list = []
    for i, (pname, pdesc, pmeta) in enumerate(products):
        prod_cards += f'''<article class="card"><div class="ph"><span class="tag">{tag}</span><img src="{img}" alt="{pname} — {img_alt}" loading="lazy"></div>
        <div class="body"><h3>{pname}</h3><p class="meta">{pmeta}</p><p>{pdesc}</p>
        <a class="more" href="/contact">Request price &amp; samples</a></div></article>\n'''
        item_list.append({
            "@type": "ListItem", "position": i + 1,
            "item": {"@type": "Product", "name": pname, "description": pdesc,
                     "image": DOMAIN + img,
                     "brand": {"@type": "Brand", "name": BRAND},
                     "manufacturer": {"@id": DOMAIN + "/#organization"},
                     "offers": {"@type": "AggregateOffer", "priceCurrency": "USD",
                                "lowPrice": "0.01", "highPrice": "0.80",
                                "availability": "https://schema.org/InStock",
                                "url": DOMAIN + "/products/" + slug}}})

    related_html = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in related)

    body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/products/">Products</a> / <span>{h1}</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Product line</p>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="cta-row" style="margin-top:20px;display:flex;gap:12px;flex-wrap:wrap">
    <a class="btn brass" href="/contact">Get a Quote</a>
    <a class="btn ghost" href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp Us</a>
  </div>
</div></section>

<section class="band"><div class="wrap split">
  <div class="prose">
    {intro_html}
    <h2>Specifications at a glance</h2>
    {spec_table}
    <h2>Popular {h1.lower()} we manufacture</h2>
    <div class="grid c2" style="margin:22px 0 34px">{prod_cards}</div>
    <h2>Frequently asked questions</h2>
    {faq_html(faqs)}
  </div>
  <aside class="rail">
    <div class="rail-box">
      <h3>Get pricing for {h1.lower()}</h3>
      <p style="font-size:0.9rem">Send size, material, quantity and your logo file. Quote within 12 hours.</p>
      <a class="btn brass" style="width:100%;text-align:center" href="/contact">Request a Quote</a>
    </div>
    <div class="rail-box">
      <h3>Other product lines</h3>
      <ul>{related_html}</ul>
    </div>
    <div class="rail-box">
      <h3>Buying guides</h3>
      <ul>
        <li><a href="/blog/button-size-chart-ligne-guide">Button size chart: ligne to mm</a></li>
        <li><a href="/blog/resin-vs-corozo-vs-metal-buttons">Resin vs corozo vs metal</a></li>
        <li><a href="/blog/how-to-choose-jeans-buttons">Choosing denim hardware</a></li>
      </ul>
    </div>
  </aside>
</div></section>
'''
    ld = [
        breadcrumb_ld([("Home", "/"), ("Products", "/products/"), (h1, None)]),
        {"@context": "https://schema.org", "@type": "ItemList", "name": h1, "itemListElement": item_list},
        faq_ld(faqs),
    ]
    write_page(f"products/{slug}.html", layout(
        page_id="products", title=page_title, description=description,
        canonical_path=f"/products/{slug}", body=body, jsonld=ld, depth=1))

# ---------------------------------------------------------------- 6 CATEGORIES
category_page(
    slug="resin-buttons",
    page_title="Resin & Polyester Buttons Wholesale — 4-Hole, Pearl, Shank | Merit Trims",
    h1="Resin & Polyester Buttons",
    description="Wholesale resin and polyester buttons from a Wenzhou factory: 4-hole, 2-hole, pearl, shank and engraved-logo buttons in any Pantone color. MOQ 1,000 pcs, DTM dyeing.",
    lead="Polyester resin is the workhorse of garment closures: colorfast, machine-washable and infinitely customizable. We rod-cast and sheet-cast in house, then dye to match your fabric exactly.",
    img="/images/cat-resin-buttons.svg", img_alt="resin polyester button from Merit Trims factory", tag="RESIN",
    intro_html='''<p>As a <strong>resin button manufacturer in Wenzhou</strong> — the production hub for the majority of the world's polyester buttons — we supply shirt, polo, blouse, suit and coat buttons from 14L (9&nbsp;mm) to 54L (34&nbsp;mm). Every order is dyed to match (DTM) your Pantone reference or physical fabric swatch, with lab dips approved before bulk dyeing.</p>
<p>Finishes include high-gloss pearl, matte, marble/horn-imitation, ocean-pearl, rainbow and two-tone. Logos can be laser-engraved on the face or rim. All buttons pass 40°C machine-wash and dry-clean colorfastness testing, and OEKO-TEX® compliant raw polyester is standard.</p>''',
    spec_rows=[
        ("Sizes", "14L / 16L / 18L / 20L / 24L / 28L / 32L / 36L / 40L / 44L / 54L (9–34 mm)"),
        ("Styles", "4-hole, 2-hole, shank, fisheye, rim, pearl dome, fancy combined"),
        ("Material", "Unsaturated polyester resin (rod & sheet casting), urea, ABS pearl"),
        ("Colors", "Any Pantone / TPX; DTM dye with lab dip approval"),
        ("Logo options", "Laser engraving (face or side), printed, embossed mold"),
        ("MOQ", "1,000 pcs per color & size (stock: 100 pcs)"),
        ("Lead time", "Samples 5–7 days · bulk 10–15 days"),
        ("Compliance", "OEKO-TEX® compliant materials; SGS / Intertek testing on request"),
    ],
    products=[
        ("4-Hole Polyester Shirt Buttons", "Classic 14L–20L shirt and blouse buttons with rim or fisheye face, dyed to match your fabric.", "14L–20L · DTM · 4-hole"),
        ("Pearl Resin Polo Buttons", "High-gloss pearl-effect buttons for polo shirts and knitwear, in white, ivory and custom shades.", "16L–24L · pearl finish"),
        ("Engraved Logo Suit Buttons", "32L–44L jacket and coat buttons with laser-engraved brand logo, horn-imitation or matte finish.", "32L–44L · laser logo"),
        ("Chef Coat & Uniform Buttons", "Stud-style and flat-back plastic buttons for chef jackets and hospitality uniforms; industrial-wash safe.", "removable stud · flat back"),
    ],
    faqs=[
        ("What is the MOQ for custom-color resin buttons?",
         "1,000 pieces per color and size for DTM dyed buttons. White, black and ivory stock buttons ship from 100 pieces."),
        ("Can you match our fabric color exactly?",
         "Yes. Send a Pantone code or a physical swatch; we produce a lab dip within 3–5 days for approval before bulk dyeing. Color tolerance is within commercial DTM standards."),
        ("Are resin buttons safe for baby and children's clothing?",
         "We supply OEKO-TEX® compliant polyester and can arrange CPSIA/EN 71-3 testing. For babywear we also recommend pull-force tested shank styles or our prong snaps."),
        ("Do resin buttons survive industrial laundering?",
         "Standard polyester buttons handle 40°C machine washing and dry cleaning. For hospital/hotel industrial laundering at 75–90°C we recommend our high-temperature resin grade — mention it in your RFQ."),
    ],
    related=[("Metal Buttons", "/products/metal-buttons"), ("Natural Corozo & Horn", "/products/natural-buttons"),
             ("Snap Buttons", "/products/snap-buttons"), ("Custom Button Service", "/custom-buttons")])

category_page(
    slug="metal-buttons",
    page_title="Custom Metal Buttons — Zinc Alloy & Brass, Engraved Logo | Merit Trims",
    h1="Metal Buttons",
    description="Custom metal buttons factory: zinc alloy and brass shank buttons with embossed or engraved logos for blazers, coats and uniforms. 10+ plating finishes, nickel-free options, MOQ 500 pcs.",
    lead="Die-cast zinc alloy and stamped brass buttons with your crest, monogram or logo in relief — the closure that turns a jacket into a brand asset.",
    img="/images/cat-metal-buttons.svg", img_alt="zinc alloy metal button with engraved logo", tag="METAL",
    intro_html='''<p>We manufacture <strong>custom metal buttons</strong> by zinc-alloy die casting and brass stamping, then finish them in our plating line: shiny/antique gold, silver, nickel, gunmetal, antique brass, copper, matte black and custom paint or enamel fill. Nickel-free plating is available for EU REACH compliance.</p>
<p>Typical applications include blazer and military-style buttons with anchor or crest motifs, designer coat buttons, uniform buttons for hotels and airlines, and decorative rivets. A new embossing mold costs from US$40–80 and is refunded on orders above 10,000 pieces.</p>''',
    spec_rows=[
        ("Sizes", "15 / 18 / 20 / 23 / 25 / 28 / 30 mm (24L–48L)"),
        ("Construction", "Shank (loop back), 4-hole sew-on, screw-back, snap-cap"),
        ("Material", "Zinc alloy (die-cast), brass (stamped), iron core options"),
        ("Plating", "Gold, antique gold, silver, nickel, nickel-free, gunmetal, copper, matte black"),
        ("Logo options", "Embossed (3D relief), debossed, laser engraved, soft enamel fill, epoxy dome"),
        ("MOQ", "500 pcs per design (new mold from 1,000 pcs)"),
        ("Mold cost", "US$40–80, refunded over 10,000 pcs"),
        ("Compliance", "Nickel-free & lead-safe plating; REACH testing on request"),
    ],
    products=[
        ("Embossed Logo Blazer Buttons", "Zinc alloy shank buttons with 3D embossed crest or logo, antique gold or silver plating.", "15–28 mm · shank · die-cast"),
        ("Brass Stamped Coat Buttons", "Stamped brass buttons with fine engraved detail for premium coats and heritage brands.", "brass · stamped · engraved"),
        ("Uniform & Military-Style Buttons", "Anchor, eagle and custom-insignia buttons for uniforms, with screw-back or shank fixing.", "uniform · screw-back"),
        ("Enamel-Fill Fashion Buttons", "Color enamel inlay on plated alloy for statement jackets and womenswear.", "soft enamel · custom color"),
    ],
    faqs=[
        ("How much does a custom logo mold cost?",
         "US$40–80 depending on size and detail, with a 5–7 day mold lead time. The mold fee is refunded once cumulative orders pass 10,000 pieces, and the mold remains exclusive to you."),
        ("Can metal buttons be nickel-free for the EU market?",
         "Yes — we offer nickel-free plating that passes EN 1811 nickel-release testing, suitable for direct-skin-contact garments sold in the EU."),
        ("Will the plating tarnish after washing?",
         "Our standard plating passes 24–48h salt-spray testing. For garments that are machine-washed frequently we recommend an extra clear e-coating; specify wash requirements in your RFQ."),
        ("Shank or 4-hole — which should I choose?",
         "Shank buttons suit thick fabrics (coats, blazers) because the loop gives thread clearance. 4-hole sew-on metal buttons suit shirts and machine attachment. We'll advise based on your garment."),
    ],
    related=[("Jeans & Tack Buttons", "/products/jeans-buttons"), ("Snap Buttons", "/products/snap-buttons"),
             ("Resin Buttons", "/products/resin-buttons"), ("Custom Button Service", "/custom-buttons")])

category_page(
    slug="snap-buttons",
    page_title="Metal Snap Buttons & Snap Fasteners — Spring, Ring & Prong | Merit Trims",
    h1="Snap Buttons & Fasteners",
    description="Four-part metal snap button supplier: spring snaps, ring snaps and prong snaps for jackets, workwear, babywear and bags. Custom logo caps, pull-force tested, MOQ 1,000 sets.",
    lead="Four-part press studs that open and close 10,000+ times without failing. Brass construction, logo-engraved caps, and pull-force testing on every batch.",
    img="/images/cat-snap-buttons-color-caps.webp", img_alt="brass four-part spring snap fastener", tag="SNAP",
    intro_html='''<p>We supply the three workhorse families of <strong>snap fasteners</strong>: <strong>spring (S-spring) snaps</strong> for shirts and light jackets, <strong>ring snaps</strong> for heavier outerwear and bags, and <strong>prong snaps</strong> that grip knit and jersey fabrics — the standard for babywear. All are four-part sets (cap, socket, stud, post) in brass or stainless options that won't rust in the wash.</p>
<p>Caps can be engraved, embossed, printed or finished with a colored lacquer or pearl insert to match your design. Every production batch is checked for snap-open force and pull-off strength, and babywear snaps can be certified to EN 71 / CPSIA on request.</p>''',
    spec_rows=[
        ("Types", "Spring snap (S-spring), ring snap, prong/cap snap, hidden snap"),
        ("Sizes", "9.5 / 10 / 12.5 / 15 / 17 / 20 mm cap diameter"),
        ("Material", "Brass (rust-proof), copper, stainless steel, zinc alloy caps"),
        ("Finishes", "Nickel, gunmetal, antique brass, gold, matte black, painted, pearl cap"),
        ("Logo options", "Engraved cap, embossed cap, printed, lacquer color"),
        ("MOQ", "1,000 sets per finish (stock: 200 sets)"),
        ("Testing", "Snap force, pull-off strength; EN 71 / CPSIA for babywear on request"),
        ("Tooling", "Compatible with standard hand presses and pneumatic die sets — dies supplied"),
    ],
    products=[
        ("Spring Snap Buttons (S-Spring)", "Smooth-action snaps for western shirts, light jackets and accessories, with logo-engraved caps.", "9.5–15 mm · brass"),
        ("Ring Snap Fasteners", "High-retention ring snaps for denim jackets, workwear and leather goods.", "12.5–20 mm · heavy duty"),
        ("Prong Snaps for Babywear", "Five-prong snaps that grip knit fabrics without tearing; EN 71 / CPSIA testable.", "9.5–12 mm · knitwear"),
        ("Pearl & Painted Cap Snaps", "Western-style pearl-top snaps and color-lacquered caps matched to your Pantone.", "pearl cap · custom color"),
    ],
    faqs=[
        ("What's the difference between spring snaps and ring snaps?",
         "Spring snaps use two parallel S-springs in the socket — lighter action, ideal for shirts. Ring snaps use a circular wire ring — stronger retention for jackets, bags and workwear."),
        ("Do you supply attaching dies and presses?",
         "We supply matched die sets for every snap size, compatible with standard hand presses, DOT presses and pneumatic machines. Dies are free with bulk orders above 50,000 sets."),
        ("Will brass snaps rust after laundering?",
         "Solid brass and stainless components are rust-proof. Avoid iron-core snaps for garments that are washed; we'll always state core material on the quotation."),
        ("Can snap caps carry our logo?",
         "Yes — engraved or embossed logos on caps from 10 mm up. Mold cost US$40–60, refunded on volume, with a digital proof before tooling."),
    ],
    related=[("Jeans & Tack Buttons", "/products/jeans-buttons"), ("Metal Buttons", "/products/metal-buttons"),
             ("Cord Stoppers", "/products/cord-stoppers"), ("Custom Service", "/custom-buttons")])

category_page(
    slug="jeans-buttons",
    page_title="Jeans Buttons & Tack Buttons Manufacturer — Custom Logo Denim Hardware | Merit Trims",
    h1="Jeans & Tack Buttons",
    description="Custom jeans button factory: move & fixed tack buttons, rivets and burrs with embossed logos. Antique brass, copper, gunmetal. 17–25 mm, MOQ 1,000 sets, mold from $40.",
    lead="Hammer-on denim hardware with your logo in relief: tack buttons that hold through years of wear, and rivets that reinforce every stress point.",
    img="/images/cat-jeans-buttons.svg", img_alt="embossed brass jeans tack button", tag="DENIM",
    intro_html='''<p>Denim hardware is brand real estate. We manufacture <strong>jeans tack buttons</strong> (move-shank and fixed-shank), <strong>rivets and burrs</strong> in 17, 20, 22 and 25&nbsp;mm with embossed or engraved logos, plus matching nail posts in brass or stainless that won't rust in stone-washing.</p>
<p>Finishes cover the full denim vocabulary — antique brass, antique copper, antique silver, gunmetal, matte black, vintage tin — and we can oxidize or tumble for a worn look out of the box. All hardware is needle-detector safe on request and tested for pull-off strength after attachment.</p>''',
    spec_rows=[
        ("Types", "Move-shank tack, fixed-shank tack, donut/hollow button, rivets & burrs"),
        ("Sizes", "17 / 20 / 22 / 25 mm button; 8–9 mm rivets"),
        ("Material", "Brass, copper, zinc alloy shell, stainless or brass nail (rust-proof)"),
        ("Finishes", "Antique brass, antique copper, gunmetal, matte black, vintage tin, custom"),
        ("Logo options", "Embossed 3D logo, debossed, engraved rim text, laser"),
        ("MOQ", "1,000 sets (button + nail); rivets 2,000 sets"),
        ("Mold cost", "US$40–60, refunded over 10,000 sets"),
        ("Testing", "Pull-off strength, stone-wash & enzyme-wash resistance, needle detection"),
    ],
    products=[
        ("Move-Shank Jeans Buttons", "Industry-standard swivel tack buttons that flex with the waistband; embossed logo face.", "17–25 mm · move shank"),
        ("Fixed Tack Buttons", "Rigid tack buttons for heavyweight denim and workwear waistbands.", "17–22 mm · fixed shank"),
        ("Custom Logo Rivets & Burrs", "Pocket-corner rivets with embossed branding, in matching finishes.", "8–9 mm · copper/brass"),
        ("Donut & Hollow Buttons", "Open-center jeans buttons for a lighter, vintage workwear look.", "17–20 mm · hollow"),
    ],
    faqs=[
        ("Will jeans buttons survive stone washing and enzyme washing?",
         "Yes — choose brass or copper shells with brass/stainless nails. We pre-test finishes against stone-wash abrasion; avoid iron nails, which rust during wet processing."),
        ("What size jeans button should I use?",
         "17 mm suits most 5-pocket jeans and women's denim; 20 mm is the heavyweight standard; 22–25 mm for workwear and statement waistbands. We'll send a size card with samples."),
        ("Move shank or fixed shank?",
         "Move-shank (swivel) buttons rotate slightly and reduce stress on the denim — standard for fashion jeans. Fixed shanks suit very heavy canvas and workwear."),
        ("Can you make our buttons needle-detector safe?",
         "Yes. We supply detector-safe brass/zinc compositions and verify each batch through a needle detector before packing — important for Japanese and EU retail compliance."),
    ],
    related=[("Snap Buttons", "/products/snap-buttons"), ("Metal Buttons", "/products/metal-buttons"),
             ("Eyelets & Buckles", "/products/cord-stoppers"), ("Denim hardware guide", "/blog/how-to-choose-jeans-buttons")])

category_page(
    slug="natural-buttons",
    page_title="Corozo, Horn & Wood Buttons — Natural Sustainable Buttons Factory | Merit Trims",
    h1="Corozo, Horn & Wood Buttons",
    description="Natural button supplier: corozo (tagua nut), buffalo horn, wood and coconut buttons for premium shirting and sustainable fashion. Laser logo engraving, MOQ 1,000 pcs.",
    lead="Nature's own polymers: corozo's porcelain grain, horn's smoky depth, wood's warmth. The closures that premium and eco-conscious brands specify by name.",
    img="/images/cat-natural-buttons.svg", img_alt="natural corozo tagua button with visible grain", tag="NATURAL",
    intro_html='''<p><strong>Corozo buttons</strong> (tagua nut, "vegetable ivory") take dye beautifully while keeping their signature grain visible — the default choice for premium shirting and Italian-style tailoring. <strong>Buffalo horn buttons</strong> bring unrepeatable natural variegation to suiting and coats. <strong>Wood and coconut buttons</strong> suit casualwear, linen and resort lines.</p>
<p>All natural buttons are biodegradable and support sustainability claims in your product story. We grade raw material strictly (corozo from Ecuador, horn from food-industry byproduct), machine and polish in Wenzhou, and laser-engrave logos without compromising the material. Expect natural variation between pieces — that's the point.</p>''',
    spec_rows=[
        ("Materials", "Corozo (tagua), buffalo horn, ox horn, wood (sandalwood, maple), coconut shell"),
        ("Sizes", "14L–54L (9–34 mm)"),
        ("Styles", "2-hole, 4-hole, shank, rim, suit sets (front + sleeve)"),
        ("Finishes", "Natural polish, dyed (corozo), smoked, matte, burnt edge (wood)"),
        ("Logo options", "Laser engraving (recommended), branded burn (wood)"),
        ("MOQ", "1,000 pcs per size; horn suit-sets from 300 sets"),
        ("Sustainability", "Biodegradable; corozo is a renewable rainforest crop; horn is a byproduct"),
        ("Note", "Natural variation in grain and shade is inherent and expected"),
    ],
    products=[
        ("Corozo Shirt Buttons", "Dyed or natural 4-hole corozo buttons with visible grain for premium shirting.", "14L–20L · dyeable"),
        ("Buffalo Horn Suit Buttons", "Front and sleeve button sets in genuine horn, each piece unique.", "24L–44L · suit sets"),
        ("Engraved Wood Buttons", "Laser-engraved logo buttons in maple and sandalwood for casual and linen lines.", "18L–44L · laser logo"),
        ("Coconut Shell Buttons", "Rustic coconut buttons for resortwear, crafts and eco collections.", "14L–40L · eco"),
    ],
    faqs=[
        ("Are corozo buttons really more sustainable than plastic?",
         "Corozo is the dried seed of the tagua palm — a renewable crop harvested without felling trees, and the finished button is biodegradable. It's widely used by brands to replace polyester buttons in sustainability programs."),
        ("Can horn buttons be identical in color?",
         "No two horn buttons are identical — variegation is the material's value. We grade and batch-match so variation stays within an agreed range; ask for a graded sample card."),
        ("How should garments with natural buttons be washed?",
         "Corozo handles normal machine washing well. Horn prefers dry cleaning; prolonged soaking can dull the polish. We include care guidance with every bulk shipment."),
        ("Can you laser-engrave our logo on natural buttons?",
         "Yes — laser engraving works cleanly on corozo, wood and horn with no mold cost, making it ideal for smaller premium runs from 1,000 pieces."),
    ],
    related=[("Resin Buttons", "/products/resin-buttons"), ("Metal Buttons", "/products/metal-buttons"),
             ("Material comparison guide", "/blog/resin-vs-corozo-vs-metal-buttons"), ("Custom Service", "/custom-buttons")])

category_page(
    slug="cord-stoppers",
    page_title="Cord Stoppers Supplier — Garment Trims & Hardware | Merit Trims",
    h1="Cord Stoppers",
    description="Garment hardware supplier: plastic & metal cord locks, eyelets/grommets, side-release buckles and adjusters for outdoor wear, hoodies and bags. MOQ 1,000 pcs.",
    lead="The functional trims that finish a garment: spring-loaded cord stoppers, clean-set eyelets, and buckles that click with authority.",
    img="/images/cat-hardware.svg", img_alt="cord lock stopper and metal eyelet trims", tag="TRIMS",
    intro_html='''<p>Beyond buttons, we supply the hardware that activewear, outdoor and bag designers need: <strong>cord locks</strong> (single- and double-hole, spring-loaded, in POM plastic or zinc alloy), <strong>eyelets and grommets</strong> from 3–20&nbsp;mm in brass and stainless, and <strong>side-release buckles, ladder locks and sliders</strong> in POM and metal.</p>
<p>Everything ships with consistent spring tension, burr-free eyelet edges, and salt-spray-tested plating. DTM color matching on plastic parts means your cord lock disappears into the hood — or pops as an accent, your call.</p>''',
    spec_rows=[
        ("Cord locks", "Single/double hole, ball, cylinder, mini; POM plastic or zinc alloy; fits 2–6 mm cord"),
        ("Eyelets / grommets", "3–20 mm inner diameter; brass, stainless, alloy; with washers"),
        ("Buckles", "Side-release 10–50 mm, ladder locks, sliders, D-rings, hooks"),
        ("Colors", "DTM any Pantone on plastic; 8+ plating finishes on metal"),
        ("Logo options", "Engraved (metal), molded or printed (plastic)"),
        ("MOQ", "1,000 pcs (cord locks/buckles); 5,000 pcs (eyelets)"),
        ("Testing", "Spring-cycle testing, salt spray, pull strength"),
        ("Applications", "Hoodies, outdoor jackets, sportswear, bags, footwear, medical garments"),
    ],
    products=[
        ("Spring Cord Lock Stoppers", "Single and double-hole toggles in POM or metal, DTM colors, for 2–6 mm drawcords.", "POM / zinc · 2–6 mm cord"),
        ("Brass Eyelets & Grommets", "Burr-free eyelets with washers for lacing, drawstrings and ventilation.", "3–20 mm · brass / stainless"),
        ("Side-Release Buckles", "Quick-release buckles and ladder locks for bags, belts and outerwear.", "10–50 mm · POM / alloy"),
        ("Metal Cord Ends & Adjusters", "Plated cord tips, sliders and adjusters that finish drawcords cleanly.", "zinc alloy · plated"),
    ],
    faqs=[
        ("Can cord locks be color-matched to our fabric?",
         "Yes — POM plastic parts are molded in any Pantone with a small color fee, MOQ 1,000 pieces per color. Lab chip approval before bulk."),
        ("Do you supply eyelet-setting tools?",
         "We supply matched setting dies for hand presses and pneumatic machines with every eyelet size, free on orders above 50,000 pieces."),
        ("Are your buckles strong enough for backpacks?",
         "Our POM side-release buckles are pull-tested; for load-bearing straps we recommend the heavy-duty series (tested to 80–120 kgf depending on width). State your load requirement in the RFQ."),
        ("Can you ship mixed trims in one order?",
         "Yes — most customers combine buttons, snaps, cord locks and eyelets in one consolidated shipment with one set of export documents. MOQs apply per item."),
    ],
    related=[("Snap Buttons", "/products/snap-buttons"), ("Jeans Buttons", "/products/jeans-buttons"),
             ("Resin Buttons", "/products/resin-buttons"), ("Custom Service", "/custom-buttons")])

# ---------------------------------------------------------------- PRODUCTS HUB
hub_body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Products</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Catalog</p>
  <h1>Garment Buttons &amp; Trims — Full Product Range</h1>
  <p class="lead">Six product families covering every closure and functional trim a garment needs, all manufactured or finished in our Wenzhou facility. Click a line for specifications, MOQs and customization options — or send your tech pack and let us spec it for you.</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="grid c3">
    <article class="card"><div class="ph"><span class="tag">14L–54L</span><img src="/images/cat-resin-buttons.svg" alt="Resin polyester buttons category" loading="lazy"></div>
      <div class="body"><h3><a href="/products/resin-buttons">Resin &amp; Polyester Buttons</a></h3><p class="meta">4-hole · pearl · shank · DTM</p><p>Shirt to coat buttons in any Pantone, with laser-engraved logos.</p><a class="more" href="/products/resin-buttons">Specifications</a></div></article>
    <article class="card"><div class="ph"><span class="tag">METAL</span><img src="/images/cat-metal-buttons.svg" alt="Metal buttons category" loading="lazy"></div>
      <div class="body"><h3><a href="/products/metal-buttons">Metal Buttons</a></h3><p class="meta">zinc alloy · brass · plated</p><p>Embossed-logo shank and sew-on buttons for blazers and uniforms.</p><a class="more" href="/products/metal-buttons">Specifications</a></div></article>
    <article class="card"><div class="ph"><span class="tag">4-PART</span><img src="/images/cat-snap-buttons-color-caps.webp" alt="Snap fasteners category" loading="lazy"></div>
      <div class="body"><h3><a href="/products/snap-buttons">Snap Buttons &amp; Fasteners</a></h3><p class="meta">spring · ring · prong</p><p>Four-part press studs, pull-force tested, babywear-certifiable.</p><a class="more" href="/products/snap-buttons">Specifications</a></div></article>
    <article class="card"><div class="ph"><span class="tag">DENIM</span><img src="/images/cat-jeans-buttons.svg" alt="Jeans tack buttons category" loading="lazy"></div>
      <div class="body"><h3><a href="/products/jeans-buttons">Jeans &amp; Tack Buttons</a></h3><p class="meta">tacks · rivets · burrs</p><p>Stone-wash-proof denim hardware with embossed branding.</p><a class="more" href="/products/jeans-buttons">Specifications</a></div></article>
    <article class="card"><div class="ph"><span class="tag">NATURAL</span><img src="/images/cat-natural-buttons.svg" alt="Corozo horn wood buttons category" loading="lazy"></div>
      <div class="body"><h3><a href="/products/natural-buttons">Corozo, Horn &amp; Wood</a></h3><p class="meta">tagua · buffalo horn · wood</p><p>Sustainable natural buttons for premium and eco collections.</p><a class="more" href="/products/natural-buttons">Specifications</a></div></article>
    <article class="card"><div class="ph"><span class="tag">TRIMS</span><img src="/images/cat-hardware.svg" alt="Cord locks eyelets buckles category" loading="lazy"></div>
      <div class="body"><h3>
</h3>
</div></article>
  </div>
  <div style="margin-top:44px;background:var(--corozo);border:1px solid var(--line);border-radius:8px;padding:30px">
    <h2 style="margin-bottom:8px">Can't find exactly what's in your tech pack?</h2>
    <p style="margin-bottom:16px">We quote against photos, sketches and competitor samples daily. If it closes a garment, we can make it.</p>
    <a class="btn brass" href="/custom-buttons">Explore custom manufacturing</a>
  </div>
</div></section>
'''
write_page("products/index.html", layout(
    page_id="products",
    title="Garment Buttons & Trims Catalog — Resin, Metal, Snap, Jeans, Corozo | Merit Trims",
    description="Full catalog of garment buttons and trims from our Wenzhou factory: resin, metal, snap, jeans, corozo & horn buttons, cord locks, eyelets and buckles. B2B wholesale, low MOQ.",
    canonical_path="/products/", body=hub_body,
    jsonld=[breadcrumb_ld([("Home", "/"), ("Products", None)])], depth=1))

print("core pages done")
