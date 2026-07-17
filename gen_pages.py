#!/usr/bin/env python3
"""gen_pages.py — custom, about, contact, faq, blog, 404."""
from sitegen import *

# ---------------------------------------------------------------- CUSTOM BUTTONS
custom_body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Custom Buttons</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">OEM / ODM service</p>
  <h1>Custom Button Manufacturing — Your Logo, Your Spec</h1>
  <p class="lead">From a sketch on a napkin to 500,000 identical pieces: we develop molds, match colors, engrave logos and run production QC so the button in the carton matches the button in your tech pack.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><p class="eyebrow">What we customize</p><h2>Five levers, infinite combinations</h2></div>
  <div class="grid c3">
    <div class="card"><div class="body"><h3>Logo &amp; branding</h3><p>Laser engraving (no mold cost), 3D embossed/debossed molds (US$40–80, refunded on volume), pad printing, enamel fill, epoxy dome.</p></div></div>
    <div class="card"><div class="body"><h3>Color (DTM)</h3><p>Dye-to-match any Pantone/TPX or physical swatch. Lab dips in 3–5 days; bulk only after your written approval.</p></div></div>
    <div class="card"><div class="body"><h3>Material &amp; finish</h3><p>Polyester resin, zinc alloy, brass, corozo, horn, wood; pearl, matte, antique, plated, oxidized, two-tone finishes.</p></div></div>
    <div class="card"><div class="body"><h3>Shape &amp; size</h3><p>Standard rounds 14L–54L, plus squares, flowers, toggles, shanks and fully bespoke 3D shapes from your CAD or sample.</p></div></div>
    <div class="card"><div class="body"><h3>Packing &amp; labeling</h3><p>Bulk bags, carded retail packs, private-label boxes, size-sorted kits for your production line.</p></div></div>
    <div class="card"><div class="body"><h3>Compliance &amp; testing</h3><p>OEKO-TEX® compliant materials, nickel-free plating, needle detection, SGS/Intertek reports for REACH, CPSIA, EN 71.</p></div></div>
  </div>
</div></section>

<section class="band dark"><div class="wrap">
  <div class="section-head"><p class="eyebrow" style="color:#C9A961">Development timeline</p><h2>Custom development, week by week</h2></div>
  <div class="steps">
    <div><h3>Day 0–1: RFQ review</h3><p>Send artwork, size, material, quantity. We confirm feasibility and quote within 12 hours.</p></div>
    <div><h3>Day 1–3: Digital proof</h3><p>Free 2D/3D mock-up of your button with dimensions and finish callouts.</p></div>
    <div><h3>Day 3–10: Mold &amp; sample</h3><p>Tooling cut and first physical samples shipped by express for approval.</p></div>
    <div><h3>Day 10–25: Bulk production</h3><p>Production with in-line QC; pre-shipment photos and inspection report.</p></div>
    <div><h3>Day 25+: Delivery</h3><p>Express, air or sea with full export documents. Mold stored free for reorders.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap split">
  <div class="prose">
    <h2>What to include in your RFQ</h2>
    <p>The more of these you send, the faster and tighter the quote:</p>
    <ul class="ticks">
      <li><strong>Size</strong> — in mm or ligne (L). Not sure? See our <a href="/blog/button-size-chart-ligne-guide">ligne size chart</a>.</li>
      <li><strong>Material</strong> — resin, metal, corozo/horn, or "recommend for me" with the garment type.</li>
      <li><strong>Logo file</strong> — AI/EPS/PDF vector preferred; a clear photo works for quoting.</li>
      <li><strong>Quantity</strong> — per color/size, plus expected annual volume for better tiered pricing.</li>
      <li><strong>Color target</strong> — Pantone code or a fabric swatch you can mail/photograph.</li>
      <li><strong>Compliance needs</strong> — destination market (EU/US/JP) and any testing standards.</li>
    </ul>
    <h2>Mold &amp; tooling policy</h2>
    <p>Embossing molds cost US$40–80 and remain your exclusive property — we never reuse a customer's mold for another buyer. The fee is credited back once cumulative orders pass 10,000 pieces. Molds are stored free for at least three years for instant reorders.</p>
  </div>
  <aside class="rail">
    <div class="rail-box"><h3>Start your custom project</h3><p style="font-size:0.9rem">Attach your logo and tech pack — digital mock-up is free.</p>
      <a class="btn brass" style="width:100%;text-align:center" href="/contact">Send RFQ</a></div>
    <div class="rail-box"><h3>Product lines</h3><ul>
      <li><a href="/products/resin-buttons">Resin Buttons</a></li>
      <li><a href="/products/metal-buttons">Metal Buttons</a></li>
      <li><a href="/products/jeans-buttons">Jeans Buttons</a></li>
      <li><a href="/products/snap-buttons">Snap Fasteners</a></li>
      <li><a href="/products/natural-buttons">Corozo &amp; Horn</a></li>
    </ul></div>
  </aside>
</div></section>
'''
write_page("custom-buttons.html", layout(
    page_id="custom",
    title="Custom Buttons Manufacturer — OEM Logo Buttons, Low MOQ | Merit Trims",
    description="OEM/ODM custom button manufacturing: your logo engraved or embossed, any Pantone color, molds from $40 (refunded on volume). Digital proof free, samples in 5–7 days.",
    canonical_path="/custom-buttons", body=custom_body,
    jsonld=[breadcrumb_ld([("Home", "/"), ("Custom Buttons", None)]),
            {"@context": "https://schema.org", "@type": "Service", "name": "Custom Button Manufacturing (OEM/ODM)",
             "provider": {"@id": DOMAIN + "/#organization"}, "areaServed": "Worldwide",
             "description": "Custom garment button development: logo molds, DTM color matching, sampling and bulk production."}],
    depth=0))

# ---------------------------------------------------------------- ABOUT
about_body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>About</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About us</p>
  <h1>Merit Trims (Wenzhou) Co., Ltd.</h1>
  <p class="lead">A factory-direct button and trims manufacturer in Wenzhou, Zhejiang — the city that makes most of the world's garment buttons — exporting to apparel brands, garment factories and trim wholesalers in 60+ countries since 2008.</p>
</div></section>

<section class="band"><div class="wrap split">
  <div class="prose">
    <h2>Inside the button capital of China</h2>
    <p>Wenzhou's Qiaotou and Ouhai districts form the densest button-making cluster on earth: resin casting plants, zinc die-casters, electroplating lines, laser engravers and dye houses all within a short drive of each other. Merit Trims was founded inside this ecosystem, which is why we can move from artwork to approved sample in a week and hold pricing that trading companies can't match.</p>
    <h2>What we actually do in-house</h2>
    <p>We operate resin button turning and laser engraving lines in-house, and run dedicated, long-term production cells with our cluster partners for metal die-casting, plating and natural-material machining. Every order — whether turned on our own machines or in a partner cell — passes through our QC room: size and thickness gauging, colorfastness checks, snap pull-force testing and needle detection before packing.</p>
    <h2>Numbers that matter to buyers</h2>
    <table class="spec">
      <tbody>
      <tr><td><strong>Founded</strong></td><td>2008, Wenzhou, Zhejiang, China</td></tr>
      <tr><td><strong>Export markets</strong></td><td>60+ countries: US, EU, UK, Middle East, South America, SE Asia</td></tr>
      <tr><td><strong>Monthly capacity</strong></td><td>30+ million pieces across all lines</td></tr>
      <tr><td><strong>Response time</strong></td><td>≤ 12 hours for quotations, ≤ 2 hours on WhatsApp in business hours</td></tr>
      <tr><td><strong>Quality system</strong></td><td>Incoming material grading, in-line QC, AQL final inspection, needle detection</td></tr>
      <tr><td><strong>Compliance</strong></td><td>OEKO-TEX® compliant materials; SGS/Intertek third-party testing on request</td></tr>
      </tbody>
    </table>
    <h2>How we work with buyers</h2>
    <p>Most of our customers start with one sample order and stay for years of repeat programs. We keep your molds, dye recipes and packing specs on file so reorders are one email: "same as last time, 50,000 pieces." For new development, send whatever you have — a tech pack, a competitor's garment, a photo — and our sales engineers will spec material, size and attachment method for you.</p>
    <p><a class="btn brass" href="/contact">Start a conversation</a></p>
  </div>
  <aside class="rail">
    <div class="rail-box"><img src="/images/factory-placeholder.svg" alt="Merit Trims factory, Wenzhou" style="border-radius:6px;margin-bottom:14px">
      <p class="mono" style="font-size:0.78rem">{ADDRESS}</p></div>
    <div class="rail-box"><h3>Verified storefront</h3><p style="font-size:0.9rem">Check our trade history and buyer reviews on Alibaba.</p>
      <a href="https://merittrims.en.alibaba.com/" rel="noopener">merittrims.en.alibaba.com →</a></div>
  </aside>
</div></section>
'''
write_page("about.html", layout(
    page_id="about",
    title="About Merit Trims (Wenzhou) Co., Ltd. — Button Factory in Wenzhou, China",
    description="Merit Trims is a factory-direct garment button manufacturer in Wenzhou, China, exporting resin, metal, snap and natural buttons to 60+ countries since 2008.",
    canonical_path="/about", body=about_body,
    jsonld=[breadcrumb_ld([("Home", "/"), ("About", None)])], depth=0))

# ---------------------------------------------------------------- CONTACT
contact_body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Contact</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Request a quote</p>
  <h1>Contact Merit Trims — Quote Within 12 Hours</h1>
  <p class="lead">Tell us the size, material and quantity (or just attach a photo of the button you need). A sales engineer — not a bot — replies with pricing, MOQ tiers and lead time.</p>
</div></section>

<section class="band"><div class="wrap split">
  <div>
    <form class="inq" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" data-email="{EMAIL}">
      <h2 style="margin-bottom:6px">Send your inquiry</h2>
      <p style="color:var(--grey);font-size:0.92rem">Fields marked <span style="color:#B3382C">*</span> are required.</p>
      <div class="row">
        <div><label for="f-name">Your name <span class="req">*</span></label>
        <input id="f-name" name="name" required autocomplete="name"></div>
        <div><label for="f-company">Company</label>
        <input id="f-company" name="company" autocomplete="organization"></div>
      </div>
      <div class="row">
        <div><label for="f-email">Email <span class="req">*</span></label>
        <input id="f-email" type="email" name="email" required autocomplete="email"></div>
        <div><label for="f-wa">WhatsApp / phone</label>
        <input id="f-wa" name="whatsapp" autocomplete="tel"></div>
      </div>
      <div class="row">
        <div><label for="f-product">Product interest</label>
        <select id="f-product" name="product">
          <option>Resin / polyester buttons</option><option>Metal buttons</option>
          <option>Snap buttons / fasteners</option><option>Jeans / tack buttons</option>
          <option>Corozo / horn / wood buttons</option><option>Cord locks / eyelets / buckles</option>
          <option>Custom development</option><option>Other / not sure</option>
        </select></div>
        <div><label for="f-qty">Estimated quantity</label>
        <select id="f-qty" name="quantity">
          <option>Under 1,000 pcs</option><option>1,000 – 10,000 pcs</option>
          <option>10,000 – 100,000 pcs</option><option>100,000+ pcs</option>
        </select></div>
      </div>
      <label for="f-msg">Requirements <span class="req">*</span></label>
      <textarea id="f-msg" name="message" required placeholder="e.g. 20L (12.5mm) 4-hole resin buttons, Pantone 19-4052, engraved logo, 20,000 pcs, ship to Rotterdam…"></textarea>
      <input type="text" name="_gotcha" style="display:none" tabindex="-1" aria-hidden="true">
      <button class="btn brass" type="submit">Send Inquiry</button>
      <p class="form-note">Prefer email? Write directly to <a href="mailto:{EMAIL}">{EMAIL}</a> — attach logos, tech packs or photos. Files over 10&nbsp;MB: send a download link.</p>
    </form>
  </div>
  <aside class="rail">
    <div class="rail-box"><h3>Direct channels</h3><ul>
      <li>📧 <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>💬 <a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp: +{WHATSAPP}</a></li>
      <li>☎️ <a href="tel:{PHONE}">{PHONE}</a></li>
      <li>🏪 <a href="https://merittrims.en.alibaba.com/" rel="noopener">Alibaba storefront</a></li>
    </ul></div>
    <div class="rail-box"><h3>Office hours</h3><p style="font-size:0.9rem">Mon–Sat 8:30–18:00 China time (GMT+8).<br>Inquiries outside hours are answered first thing next morning — within 12 hours guaranteed.</p></div>
    <div class="rail-box"><h3>Visit the factory</h3><p class="mono" style="font-size:0.78rem">{ADDRESS}</p>
    <p style="font-size:0.9rem">Buyers visiting Wenzhou or the Canton Fair: tell us your dates, we'll arrange pickup and a showroom tour.</p></div>
  </aside>
</div></section>
'''
write_page("contact.html", layout(
    page_id="contact",
    title="Contact & Request a Quote — Merit Trims | Garment Buttons Factory",
    description="Request a wholesale quote for custom garment buttons. Reply within 12 hours with pricing, MOQ and lead time. Email, WhatsApp, or send your tech pack via the RFQ form.",
    canonical_path="/contact", body=contact_body,
    jsonld=[breadcrumb_ld([("Home", "/"), ("Contact", None)]),
            {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Merit Trims",
             "url": DOMAIN + "/contact"}],
    depth=0))

# ---------------------------------------------------------------- FAQ (20 Q&A)
all_faqs = [
    ("What is your minimum order quantity (MOQ)?",
     "MOQ depends on the product: resin buttons 1,000 pcs per color/size; metal buttons 500 pcs per design; snap fasteners 1,000 sets; jeans buttons 1,000 sets; eyelets 5,000 pcs. Stock designs ship from as few as 100 pcs."),
    ("How quickly will I receive a quotation?",
     "Within 12 hours of receiving your requirements, often within 2 hours during Chinese business hours. Quotes itemize unit price, mold cost (if any), MOQ tiers, sample cost and lead time."),
    ("Do you provide free samples?",
     "Stock samples are free — you cover express shipping (typically US$25–40 by DHL, refunded against your first bulk order). Custom samples carry a small sampling fee that is also credited back on bulk."),
    ("How long does production take?",
     "Custom samples: 5–7 days. Bulk production: 10–15 days after sample/lab-dip approval for most items; 15–20 days for new-mold metal buttons in large volumes."),
    ("Can you put our logo on the buttons?",
     "Yes — laser engraving (no tooling cost), embossed/debossed molds (US$40–80, refunded over 10,000 pcs), pad printing, enamel fill and epoxy doming. You receive a free digital proof before any tooling is cut."),
    ("Can you match a specific Pantone color?",
     "Yes. We dye resin and mold plastics to match any Pantone/TPX reference or physical swatch, with a lab dip sent for approval before bulk dyeing."),
    ("What payment terms do you accept?",
     "T/T bank transfer (30% deposit, balance against shipping documents), PayPal for samples and small orders, and Alibaba Trade Assurance for buyers who prefer platform protection. L/C for large container orders."),
    ("How do you ship, and can you handle door-to-door?",
     "Samples and small lots go by DHL/FedEx/UPS (3–7 days worldwide). Bulk ships by air or sea, FOB Ningbo/Shanghai or CIF/DDP to your port or door. We prepare full export documentation."),
    ("Are your products tested for EU REACH / US CPSIA?",
     "We use OEKO-TEX® compliant materials and nickel-free, lead-safe plating by default, and arrange SGS or Intertek third-party testing (REACH, CPSIA, EN 71-3, nickel release EN 1811) on request at cost."),
    ("Do you do needle detection?",
     "Yes — orders can be passed through a needle detector before packing and shipped with a detection certificate, as required by many Japanese and European retailers."),
    ("Can I order multiple products in one shipment?",
     "Absolutely. Most customers consolidate buttons, snaps, rivets, cord locks and eyelets into one shipment with a single set of documents. MOQs apply per item, not per shipment."),
    ("What is a ligne (L) and how do I convert it to millimeters?",
     "Ligne is the traditional button size unit: 1L = 0.635 mm. Common sizes: 14L = 9 mm, 18L = 11.5 mm, 20L = 12.5 mm, 24L = 15 mm, 32L = 20 mm, 36L = 23 mm, 44L = 28 mm. See our size-chart guide for a full table."),
    ("Who pays for the mold, and who owns it?",
     "You pay a one-time mold fee (US$40–80 for most button molds), the mold is exclusively yours, we store it free for 3+ years, and the fee is refunded once cumulative orders exceed 10,000 pieces."),
    ("Can you copy a button from a photo or physical sample?",
     "Yes — mail us a sample or send clear photos with a ruler in frame. We reverse-engineer size, material and finish, and quote an equivalent or improved version. We do not copy third-party trademarked logos."),
    ("Do you sell to small brands and startups?",
     "Yes. Stock buttons from 100 pcs and laser-engraved logos (no mold cost) make small first runs practical. Many of our largest accounts started with one carton."),
    ("What packing options are available?",
     "Bulk poly bags (500–1,000 pcs), boxed by size/color, carded retail packs, or private-label packaging with your brand. Cartons are export-grade with shipping marks per your instruction."),
    ("How do you control quality?",
     "Incoming material grading, first-article inspection, in-line checks during production, and AQL 2.5 final inspection covering size, thickness, color, plating adhesion and snap pull-force. Pre-shipment photos or video on request."),
    ("Can buttons survive industrial laundering or stone washing?",
     "Yes, with the right spec: high-temperature resin grades for hospital/hotel laundering, and brass/stainless denim hardware for stone and enzyme washing. Tell us the wash process and we'll spec accordingly."),
    ("Do you offer Alibaba Trade Assurance?",
     "Yes — you can place orders through our Alibaba storefront (merittrims.en.alibaba.com) with Trade Assurance protection, or work with us directly for better pricing on repeat programs."),
    ("Which countries do you export to?",
     "60+ countries across North and South America, the EU and UK, the Middle East, Africa, and Southeast Asia. We're familiar with destination-specific compliance for the US, EU, UK and Japan."),
]
faq_body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>FAQ</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Buyer's FAQ</p>
  <h1>Frequently Asked Questions</h1>
  <p class="lead">Twenty straight answers about MOQs, sampling, logos, color matching, compliance, payment and shipping. Can't find yours? <a href="/contact">Ask us directly</a> — 12-hour reply.</p>
</div></section>
<section class="band"><div class="wrap" style="max-width:860px">
  {faq_html(all_faqs)}
</div></section>
'''
write_page("faq.html", layout(
    page_id="faq",
    title="FAQ — MOQ, Samples, Custom Logos, Shipping | Merit Trims",
    description="Answers to the 20 questions B2B button buyers ask most: MOQ from 500 pcs, free stock samples, $40–80 logo molds, Pantone matching, REACH/CPSIA testing, payment and shipping terms.",
    canonical_path="/faq", body=faq_body,
    jsonld=[breadcrumb_ld([("Home", "/"), ("FAQ", None)]), faq_ld(all_faqs)], depth=0))

# ---------------------------------------------------------------- BLOG
def article(slug, title, h1, description, date, read, body_html, summary):
    body = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / <span>{h1}</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Buying guide · {date} · {read} min read</p>
  <h1>{h1}</h1>
</div></section>
<section class="band"><div class="wrap split">
  <article class="prose">{body_html}
    <div style="margin-top:40px;background:var(--corozo);border:1px solid var(--line);border-radius:8px;padding:26px">
      <h3 style="margin-bottom:6px">Sourcing buttons for a production run?</h3>
      <p style="margin-bottom:14px">Send your tech pack — we'll spec material, size and finish and quote within 12 hours.</p>
      <a class="btn brass" href="/contact">Get a quote</a>
    </div>
  </article>
  <aside class="rail">
    <div class="rail-box"><h3>More guides</h3><ul>
      <li><a href="/blog/button-size-chart-ligne-guide">Button size chart (ligne → mm)</a></li>
      <li><a href="/blog/resin-vs-corozo-vs-metal-buttons">Resin vs corozo vs metal</a></li>
      <li><a href="/blog/how-to-choose-jeans-buttons">Choosing denim hardware</a></li>
    </ul></div>
    <div class="rail-box"><h3>Product lines</h3><ul>
      <li><a href="/products/resin-buttons">Resin Buttons</a></li>
      <li><a href="/products/metal-buttons">Metal Buttons</a></li>
      <li><a href="/products/jeans-buttons">Jeans Buttons</a></li>
      <li><a href="/products/natural-buttons">Corozo &amp; Horn</a></li>
    </ul></div>
  </aside>
</div></section>'''
    ld = [breadcrumb_ld([("Home", "/"), ("Blog", "/blog/"), (h1, None)]),
          {"@context": "https://schema.org", "@type": "Article", "headline": h1,
           "description": summary, "datePublished": date, "dateModified": date,
           "author": {"@type": "Organization", "name": BRAND},
           "publisher": {"@id": DOMAIN + "/#organization"},
           "mainEntityOfPage": DOMAIN + "/blog/" + slug}]
    write_page(f"blog/{slug}.html", layout(
        page_id="blog", title=title, description=description,
        canonical_path=f"/blog/{slug}", body=body, jsonld=ld, depth=1))

article("button-size-chart-ligne-guide",
    "Button Size Chart: Ligne to mm Conversion + How to Choose | Merit Trims",
    "Button Size Chart: Ligne (L) to Millimeters, and How to Choose the Right Size",
    "Complete button size chart converting ligne (L) to mm and inches, with recommended sizes for shirts, polos, suits, coats and jeans. 1L = 0.635 mm.",
    "2026-05-10", 6,
    '''<p>Button sizes are quoted in <strong>ligne</strong> (written “L”), a unit inherited from 18th-century French button makers and still the global standard on tech packs. The conversion is simple: <strong>1 ligne = 0.635&nbsp;mm</strong>, so a 20L button is 12.5&nbsp;mm across.</p>
<h2>Ligne to millimeter conversion chart</h2>
<table class="spec"><thead><tr><th>Ligne</th><th>Millimeters</th><th>Inches</th><th>Typical use</th></tr></thead><tbody>
<tr><td>12L</td><td>7.5 mm</td><td>0.30"</td><td>Baby clothes, doll clothes, shirt collars</td></tr>
<tr><td>14L</td><td>9 mm</td><td>0.35"</td><td>Shirt collars &amp; sleeve plackets</td></tr>
<tr><td>16L</td><td>10 mm</td><td>0.40"</td><td>Shirt fronts (slim), blouses</td></tr>
<tr><td>18L</td><td>11.5 mm</td><td>0.45"</td><td>Dress shirt fronts — the classic size</td></tr>
<tr><td>20L</td><td>12.5 mm</td><td>0.50"</td><td>Polo shirts, casual shirts</td></tr>
<tr><td>24L</td><td>15 mm</td><td>0.60"</td><td>Trousers, shirt-jackets, sleeve buttons on suits</td></tr>
<tr><td>28L</td><td>18 mm</td><td>0.70"</td><td>Cardigans, light jackets</td></tr>
<tr><td>32L</td><td>20 mm</td><td>0.80"</td><td>Suit jacket fronts, blazers</td></tr>
<tr><td>36L</td><td>23 mm</td><td>0.90"</td><td>Heavy blazers, light coats</td></tr>
<tr><td>40L</td><td>25 mm</td><td>1.00"</td><td>Coats, jackets</td></tr>
<tr><td>44L</td><td>28 mm</td><td>1.10"</td><td>Overcoats, duffle coats</td></tr>
<tr><td>54L</td><td>34 mm</td><td>1.35"</td><td>Statement coats, capes, decorative</td></tr>
</tbody></table>
<h2>Three rules of thumb when choosing size</h2>
<h3>1. Match the buttonhole, not the other way round</h3>
<p>A buttonhole should be the button diameter plus 2–3&nbsp;mm (plus thickness for domed or shank buttons). If the garment is already patterned, measure the buttonhole and work backwards.</p>
<h3>2. Heavier fabric, bigger button</h3>
<p>Fabric weight and button size scale together: 18L on poplin shirting, 32L on a wool blazer, 44L on a Melton overcoat. An undersized button on heavy fabric slips; an oversized one distorts light fabric.</p>
<h3>3. Keep thickness in mind for machine sewing</h3>
<p>Automatic button-sew machines have thickness limits (commonly 2–4&nbsp;mm for flat 4-hole buttons). If your factory sews by machine, confirm button thickness as well as diameter — we list both on every quotation.</p>
<h2>Jeans buttons and snaps use millimeters, not ligne</h2>
<p>Denim tack buttons are sold by mm: 17&nbsp;mm for most fashion jeans, 20&nbsp;mm for heavyweight, 22–25&nbsp;mm for workwear. Snap fasteners are likewise quoted by cap diameter (9.5–20&nbsp;mm). When in doubt, mail us a sample garment and we'll measure and match it.</p>''',
    "Ligne-to-mm conversion table with recommended button sizes per garment type."),

article("resin-vs-corozo-vs-metal-buttons",
    "Resin vs Corozo vs Metal Buttons: Which Should Your Brand Use? | Merit Trims",
    "Resin vs Corozo vs Metal Buttons: a Sourcing Manager's Comparison",
    "Side-by-side comparison of polyester resin, corozo (tagua) and metal buttons: cost, durability, washing, sustainability, MOQ and branding options — with recommendations by garment type.",
    "2026-04-22", 7,
    '''<p>Three materials cover the vast majority of garment buttons sourced today. Here's how they actually compare on the factors buyers care about — cost, wash performance, branding and sustainability — and where each one wins.</p>
<h2>The comparison at a glance</h2>
<table class="spec"><thead><tr><th>Factor</th><th>Polyester resin</th><th>Corozo (tagua)</th><th>Metal (zinc/brass)</th></tr></thead><tbody>
<tr><td><strong>Typical unit cost</strong></td><td>Lowest ($0.01–0.05)</td><td>Mid ($0.04–0.15)</td><td>Mid–high ($0.05–0.40)</td></tr>
<tr><td><strong>Color options</strong></td><td>Unlimited, DTM dyeable</td><td>Dyeable, grain shows through</td><td>Plating finishes, enamel fill</td></tr>
<tr><td><strong>Machine washing</strong></td><td>Excellent (40°C+)</td><td>Good</td><td>Excellent (check plating)</td></tr>
<tr><td><strong>Dry cleaning</strong></td><td>Excellent</td><td>Good</td><td>Excellent</td></tr>
<tr><td><strong>Branding</strong></td><td>Laser engraving, printing</td><td>Laser engraving</td><td>Embossed 3D logo — strongest branding</td></tr>
<tr><td><strong>Sustainability story</strong></td><td>Recycled-resin options</td><td>Strongest: renewable &amp; biodegradable</td><td>Durable, recyclable metal</td></tr>
<tr><td><strong>Feel / perceived value</strong></td><td>Good, very consistent</td><td>Premium, natural grain</td><td>Premium, weighty</td></tr>
<tr><td><strong>Typical MOQ</strong></td><td>1,000 pcs</td><td>1,000 pcs</td><td>500 pcs</td></tr>
</tbody></table>
<h2>When resin wins</h2>
<p>Volume programs where color consistency and cost rule: shirts, polos, uniforms, childrenswear, private-label basics. Polyester resin is dimensionally stable, takes any Pantone, survives industrial washing in high-temp grades, and at $0.01–0.05 a piece it barely registers in your garment cost sheet. <a href="/products/resin-buttons">See our resin button line</a>.</p>
<h2>When corozo wins</h2>
<p>Premium shirting, tailoring, and any collection with a sustainability claim on the hangtag. Corozo is the dried seed of the tagua palm — harvested without cutting the tree, fully biodegradable, and its porcelain-like grain reads as quality at arm's length. It dyes like resin but every button keeps a unique figure. <a href="/products/natural-buttons">See corozo and horn options</a>.</p>
<h2>When metal wins</h2>
<p>Whenever the button must carry the brand: blazers, coats, uniforms, denim. A 3D-embossed zinc-alloy or brass button is jewelry that closes a garment — and the mold that makes it is exclusively yours. For denim, metal isn't a style choice but an engineering requirement: tack buttons and rivets must survive stone washing. <a href="/products/metal-buttons">See metal buttons</a> and <a href="/products/jeans-buttons">denim hardware</a>.</p>
<h2>A practical mixed-spec example</h2>
<blockquote>A typical contemporary menswear brand we supply uses 18L dyed corozo on shirts, 32L embossed zinc-alloy on blazers, 17&nbsp;mm brass tacks on denim, and 20L pearl resin on polos — four materials, one consolidated shipment, one set of documents.</blockquote>
<p>That's the real answer: most brands shouldn't choose one material — they should spec each garment correctly and consolidate the purchasing. That's exactly what a factory-direct supplier with all four lines lets you do.</p>''',
    "Cost, durability, washing, sustainability and branding comparison of the three main button materials."),

article("how-to-choose-jeans-buttons",
    "How to Choose Jeans Buttons & Rivets: Size, Finish, Wash Survival | Merit Trims",
    "How to Choose Jeans Buttons and Rivets for Denim Production",
    "Denim hardware sourcing guide: tack button sizes (17/20/22mm), move vs fixed shank, finishes that survive stone washing, rivet placement, and logo embossing for jeans buttons.",
    "2026-03-15", 6,
    '''<p>Denim hardware fails in two ways: it falls off, or it rusts in the wash plant. Both are spec problems, not luck. Here's the checklist we walk new denim buyers through.</p>
<h2>1. Pick the size by garment weight</h2>
<table class="spec"><thead><tr><th>Button size</th><th>Denim weight</th><th>Typical garment</th></tr></thead><tbody>
<tr><td>17 mm</td><td>8–12 oz</td><td>Women's jeans, fashion denim, shirts</td></tr>
<tr><td>20 mm</td><td>12–14 oz</td><td>Standard 5-pocket jeans — the default</td></tr>
<tr><td>22 mm</td><td>14–16 oz</td><td>Heavyweight selvedge, jackets</td></tr>
<tr><td>25 mm</td><td>16 oz+</td><td>Workwear, carpenter pants, overalls</td></tr>
</tbody></table>
<h2>2. Move shank vs fixed shank</h2>
<p>A <strong>move-shank</strong> (swivel) button rotates slightly on its nail, relieving stress on the waistband as the wearer moves — the standard for fashion jeans. A <strong>fixed shank</strong> is rigid and suits very heavy canvas where the fabric itself doesn't flex. If you're unsure, move shank is the safe default.</p>
<h2>3. Specify wash-proof materials — this is where money is lost</h2>
<p>Stone washing, enzyme washing and bleaching destroy the wrong hardware. The rules:</p>
<ul class="ticks">
<li><strong>Shell:</strong> brass or copper for garments that go through wet processing; zinc alloy is fine for raw/rinse-only denim.</li>
<li><strong>Nail:</strong> always brass or stainless steel. Iron nails rust during washing and bleed onto the fabric — the most common (and most expensive) denim hardware failure.</li>
<li><strong>Finish:</strong> antique finishes (antique brass, copper, gunmetal) hide wash abrasion; bright plating shows it. Ask your supplier for wash-tested finish samples — we pre-test ours against the wash recipe you specify.</li>
</ul>
<h2>4. Rivets: placement and burr matching</h2>
<p>Rivets reinforce pocket corners and the coin pocket. Standard is 8–9&nbsp;mm caps with copper burrs; spec the same finish family as your tack button so the garment reads coherent. Open-top (donut) rivets save a little weight and lean vintage; closed caps carry embossed logos better.</p>
<h2>5. Put the logo where the eye lands</h2>
<p>The waistband button is the most-photographed hardware on a pair of jeans. A 3D embossed logo mold costs US$40–60, is exclusively yours, and is refunded at volume — there is no cheaper permanent branding on a garment. Rim text (brand name around the button edge) adds a second branding surface at no extra mold complexity.</p>
<h2>6. Order the attachment tooling with the hardware</h2>
<p>Tack buttons and rivets are hammered or pressed, not sewn. Confirm your factory's press type (hand, DOT, pneumatic) and order matched dies with the first shipment — we include them free above 50,000 sets. <a href="/products/jeans-buttons">See our jeans button specifications</a> or <a href="/contact">send your wash recipe for a matched quote</a>.</p>''',
    "Denim hardware guide: sizes, shank types, wash-proof materials, rivets and logo embossing.")

# blog index
blog_index = f'''
<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <span>Blog</span></nav></div>
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Blog</p>
  <h1>Button Sourcing Guides</h1>
  <p class="lead">Practical references written by our sales engineers — the same charts and checklists we use to spec customer orders every day.</p>
</div></section>
<section class="band"><div class="wrap">
  <div class="grid c3">
    <article class="card"><div class="body">
      <p class="meta">GUIDE · 6 MIN</p>
      <h3><a href="/blog/button-size-chart-ligne-guide">Button Size Chart: Ligne to mm Conversion</a></h3>
      <p>The full 12L–54L conversion table, plus three rules for choosing the right size per garment.</p>
      <a class="more" href="/blog/button-size-chart-ligne-guide">Read guide</a></div></article>
    <article class="card"><div class="body">
      <p class="meta">COMPARISON · 7 MIN</p>
      <h3><a href="/blog/resin-vs-corozo-vs-metal-buttons">Resin vs Corozo vs Metal Buttons</a></h3>
      <p>Cost, wash performance, branding and sustainability compared — with recommendations by garment type.</p>
      <a class="more" href="/blog/resin-vs-corozo-vs-metal-buttons">Read guide</a></div></article>
    <article class="card"><div class="body">
      <p class="meta">GUIDE · 6 MIN</p>
      <h3><a href="/blog/how-to-choose-jeans-buttons">How to Choose Jeans Buttons &amp; Rivets</a></h3>
      <p>Sizes, move vs fixed shank, finishes that survive stone washing, and logo embossing for denim.</p>
      <a class="more" href="/blog/how-to-choose-jeans-buttons">Read guide</a></div></article>
  </div>
</div></section>
'''
write_page("blog/index.html", layout(
    page_id="blog",
    title="Button Sourcing Guides & Size Charts — Merit Trims Resources",
    description="Free B2B sourcing guides from a button factory: ligne-to-mm size charts, material comparisons (resin vs corozo vs metal), and denim hardware selection.",
    canonical_path="/blog/", body=blog_index,
    jsonld=[breadcrumb_ld([("Home", "/"), ("Blog", None)])], depth=1))

# 404
body_404 = '''
<section class="band"><div class="wrap" style="text-align:center;max-width:640px">
  <p class="eyebrow" style="justify-content:center">Error 404</p>
  <h1>This page came unstitched</h1>
  <p class="lead" style="margin:14px auto 26px">The page you're looking for doesn't exist or has moved. Try the catalog, or tell us what you were looking for — we answer fast.</p>
  <p><a class="btn" href="/products/">Browse Products</a> &nbsp; <a class="btn ghost" href="/contact">Contact Us</a></p>
</div></section>'''
write_page("404.html", layout(
    page_id="none", title="Page Not Found — Merit Trims",
    description="The page you requested was not found.",
    canonical_path="/404", body=body_404, noindex=True, depth=0))

print("all pages done")
