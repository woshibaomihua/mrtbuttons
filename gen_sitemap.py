from sitegen import DOMAIN

pages = [
    ("/", "1.0", "weekly"),
    ("/products/", "0.9", "weekly"),
    ("/products/resin-buttons", "0.9", "monthly"),
    ("/products/metal-buttons", "0.9", "monthly"),
    ("/products/snap-buttons", "0.9", "monthly"),
    ("/products/jeans-buttons", "0.9", "monthly"),
    ("/products/natural-buttons", "0.9", "monthly"),
    ("/products/cord-stoppers", "0.8", "monthly"),
    ("/custom-buttons", "0.9", "monthly"),
    ("/about", "0.6", "yearly"),
    ("/contact", "0.8", "yearly"),
    ("/faq", "0.7", "monthly"),
    ("/blog/", "0.6", "weekly"),
    ("/blog/button-size-chart-ligne-guide", "0.7", "yearly"),
    ("/blog/resin-vs-corozo-vs-metal-buttons", "0.7", "yearly"),
    ("/blog/how-to-choose-jeans-buttons", "0.7", "yearly"),
]

LASTMOD = "2026-06-12"
items = "\n".join(
    f"""  <url>
    <loc>{DOMAIN}{path}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>""" for path, pri, freq in pages)

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
"""
open("sitemap.xml", "w").write(xml)
print("sitemap.xml written,", len(pages), "urls")
