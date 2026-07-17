#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crawl_store.py — 阿里国际站店铺图片一键全量下载器
==================================================
功能：从店铺首页出发，自动发现并访问【首页 / 产品列表页 / 所有产品详情页 /
公司介绍页】，渲染 JS 动态内容，提取每个页面的原图，并：

  ✓ 按产品自动建文件夹（文件夹名 = 序号-产品标题）
  ✓ 缩略图地址自动还原为原图
  ✓ 生成 manifest.csv（图片文件 ↔ 产品标题 ↔ 页面网址 ↔ 原图地址 对照表）
  ✓ 生成 _gallery.html 可视化图册（浏览器打开，按产品分组浏览所有图）
  ✓ 支持断点续传（已下载的自动跳过，可重复运行）

使用方法（在你自己的电脑上）：
  1. 安装依赖（只需一次）：
       pip install playwright
       playwright install chromium
  2. 运行：
       python3 tools/crawl_store.py
     可选参数：
       python3 tools/crawl_store.py --max-products 200 --out store-images
  3. 完成后打开 store-images/_gallery.html 查看图片↔产品对照图册

注意：
  - 请只用于抓取【你自己拥有的店铺】内容
  - 脚本带 1.5 秒访问间隔，行为与正常浏览一致
  - 若个别页面有滑块验证，加 --show 参数以可视模式运行，手动滑一下即可继续
"""
import argparse, csv, os, re, sys, time, html
from urllib.parse import urljoin, urlparse

STORE_URL = "https://merittrims.en.alibaba.com/"   # ← 你的店铺首页

# 图片域名过滤（阿里图片CDN）；测试时可用环境变量 CRAWL_IMG_RE 覆盖
IMG_RE = re.compile(os.environ.get("CRAWL_IMG_RE", r"alicdn\.com"))
PRODUCT_LINK_RE = re.compile(r"/(product|product-detail)/", re.I)
LIST_LINK_RE = re.compile(r"product(group)?list", re.I)
COMPANY_LINK_RE = re.compile(r"(company_profile|contactinfo|minisiteentrance)", re.I)
MIN_IMG_PX = 180          # 过滤小图标
DELAY = 1.5               # 页面间隔秒数

def slug(s, maxlen=60):
    s = re.sub(r"[^\w\- ]+", "", s, flags=re.U).strip()
    s = re.sub(r"\s+", "-", s)
    return (s[:maxlen].rstrip("-") or "untitled")

def restore_original(u):
    """把阿里缩略图地址还原为原图: xxx.jpg_220x220xz.jpg / xxx.jpg_.webp -> xxx.jpg"""
    u = u.split("?")[0]
    u = re.sub(r"_\d+x\d+[a-z0-9]*\.(jpg|jpeg|png|webp)$", "", u, flags=re.I)
    u = re.sub(r"\.(jpg|jpeg|png)_\.webp$", r".\1", u, flags=re.I)
    u = re.sub(r"_\.webp$", "", u, flags=re.I)
    return u

JS_COLLECT = """
(minPx) => {
  const imgs = [];
  document.querySelectorAll('img').forEach(im => {
    const src = im.currentSrc || im.src || im.getAttribute('data-src') || '';
    if (!src.startsWith('http')) return;
    const w = im.naturalWidth || 0, h = im.naturalHeight || 0;
    imgs.push({src, w, h});
  });
  const links = [...document.querySelectorAll('a[href]')].map(a => a.href);
  const title = (document.querySelector('h1')?.innerText
      || document.title || '').trim().split('\\n')[0];
  return {imgs, links, title, minPx};
}
"""

def auto_scroll(page):
    page.evaluate("""async () => {
        await new Promise(res => {
          let y = 0; const t = setInterval(() => {
            window.scrollBy(0, 700); y += 700;
            if (y >= document.body.scrollHeight + 1400) {clearInterval(t); res();}
          }, 120);
        });
        window.scrollTo(0, 0);
    }""")

def collect_page(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=45000)
    page.wait_for_timeout(2500)       # 等 JS 渲染
    auto_scroll(page)
    page.wait_for_timeout(1200)       # 等懒加载
    data = page.evaluate(JS_COLLECT, MIN_IMG_PX)
    images, seen = [], set()
    for it in data["imgs"]:
        if not IMG_RE.search(it["src"]):
            continue
        if max(it["w"], it["h"]) and max(it["w"], it["h"]) < MIN_IMG_PX:
            continue
        u = restore_original(it["src"])
        if re.search(r"\.(gif|svg)$", u, re.I):
            continue
        if u not in seen:
            seen.add(u); images.append(u)
    return data["title"], images, data["links"]

def save_image(reqctx, url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return "skip"
    r = reqctx.get(url, timeout=30000)
    if not r.ok:
        raise RuntimeError(f"HTTP {r.status}")
    body = r.body()
    if len(body) < 3000:              # 过滤占位小图
        return "tiny"
    open(path, "wb").write(body)
    return "ok"

def ext_of(url):
    m = re.search(r"\.(jpg|jpeg|png|webp)$", url, re.I)
    return ("." + m.group(1).lower()) if m else ".jpg"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=STORE_URL)
    ap.add_argument("--out", default="store-images")
    ap.add_argument("--max-products", type=int, default=300)
    ap.add_argument("--show", action="store_true", help="可视模式（处理滑块验证用）")
    a = ap.parse_args()

    from playwright.sync_api import sync_playwright
    os.makedirs(a.out, exist_ok=True)
    manifest_path = os.path.join(a.out, "manifest.csv")
    rows = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not a.show)
        ctx = browser.new_context(
            user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/124.0 Safari/537.36"),
            viewport={"width": 1366, "height": 900})
        page = ctx.new_page()
        host = urlparse(a.store).netloc

        # ── 第1步：从首页+列表页发现所有产品链接 ─────────────────
        to_scan = [a.store.rstrip("/") + "/",
                   urljoin(a.store, "productlist.html")]
        scanned, product_urls, extra_pages = set(), [], []
        print("● 正在发现产品页面 ...")
        while to_scan:
            url = to_scan.pop(0)
            if url in scanned: continue
            scanned.add(url)
            try:
                title, imgs, links = collect_page(page, url)
            except Exception as e:
                print(f"  跳过 {url} ({e})"); continue
            kind = ("首页" if url.rstrip('/') == a.store.rstrip('/')
                    else "列表页" if LIST_LINK_RE.search(url) else "页面")
            print(f"  {kind}: {url}  (发现 {len(links)} 个链接)")
            # 首页/列表页本身的图也归档
            extra_pages.append((url, title or kind, imgs))
            for l in links:
                pu = urlparse(l)
                is_detail = ("alibaba.com" in pu.netloc
                             and "/product-detail/" in pu.path)
                if pu.netloc != host and not is_detail: continue
                if PRODUCT_LINK_RE.search(pu.path):
                    clean = l.split("?")[0].split("#")[0]
                    if clean not in product_urls:
                        product_urls.append(clean)
                elif (LIST_LINK_RE.search(pu.path) or COMPANY_LINK_RE.search(pu.path)) \
                        and l.split("#")[0] not in scanned and len(scanned) < 40:
                    to_scan.append(l.split("#")[0])
            time.sleep(DELAY)

        product_urls = product_urls[: a.max_products]
        print(f"\n● 共发现 {len(product_urls)} 个产品页，开始逐个抓取图片 ...\n")

        # ── 第2步：店铺页面图（首页/列表/公司页）─────────────────
        for purl, ptitle, imgs in extra_pages:
            if not imgs: continue
            name = "store-" + slug(ptitle, 40)
            d = os.path.join(a.out, "store-pages", name)
            os.makedirs(d, exist_ok=True)
            for i, u in enumerate(imgs, 1):
                f = os.path.join(d, f"{i:02d}{ext_of(u)}")
                try:
                    st = save_image(ctx.request, u, f)
                    if st in ("ok", "skip"):
                        rows.append([os.path.relpath(f, a.out), ptitle, purl, u])
                except Exception as e:
                    print(f"    图片失败 {u[:60]} ({e})")

        # ── 第3步：逐个产品页抓取 ────────────────────────────────
        for idx, purl in enumerate(product_urls, 1):
            try:
                title, imgs, _ = collect_page(page, purl)
            except Exception as e:
                print(f"[{idx}/{len(product_urls)}] 打开失败 {purl} ({e})")
                continue
            if (not title) or "Manufacturer Directory" in title \
                    or "Suppliers, Manufa" in title or "captcha" in title.lower():
                print(f"[{idx}/{len(product_urls)}] 被重定向/拦截，跳过 {purl[:70]}"
                      "（若大量出现请加 --show 手动过一次滑块验证）")
                continue
            folder = f"{idx:03d}-{slug(title)}"
            d = os.path.join(a.out, "products", folder)
            os.makedirs(d, exist_ok=True)
            ok = 0
            for i, u in enumerate(imgs, 1):
                f = os.path.join(d, f"{i:02d}{ext_of(u)}")
                try:
                    st = save_image(ctx.request, u, f)
                    if st in ("ok", "skip"):
                        ok += 1
                        rows.append([os.path.relpath(f, a.out), title, purl, u])
                except Exception as e:
                    print(f"    图片失败 {u[:60]} ({e})")
            print(f"[{idx}/{len(product_urls)}] {title[:50]}  → {ok} 张")
            time.sleep(DELAY)

        browser.close()

    # ── 第4步：写对照清单 + 可视化图册 ───────────────────────────
    with open(manifest_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["图片文件", "产品/页面标题", "页面网址", "原图地址"])
        w.writerows(rows)

    groups = {}
    for fp, title, purl, u in rows:
        groups.setdefault((title, purl), []).append(fp)
    cards = []
    for (title, purl), fps in groups.items():
        thumbs = "".join(
            f'<a href="{html.escape(fp)}" target="_blank">'
            f'<img src="{html.escape(fp)}" loading="lazy"></a>' for fp in fps)
        cards.append(
            f'<section><h2>{html.escape(title)} '
            f'<small>({len(fps)} 张)</small></h2>'
            f'<p><a href="{html.escape(purl)}" target="_blank">{html.escape(purl)}</a></p>'
            f'<div class="g">{thumbs}</div></section>')
    open(os.path.join(a.out, "_gallery.html"), "w", encoding="utf-8").write(
        "<!doctype html><meta charset=utf-8><title>店铺图片图册</title><style>"
        "body{font-family:system-ui;margin:24px;background:#fafafa}"
        "section{background:#fff;border:1px solid #ddd;border-radius:8px;"
        "padding:16px;margin-bottom:20px}h2{margin:0 0 4px;font-size:16px}"
        "p{margin:0 0 10px;font-size:12px}.g{display:flex;flex-wrap:wrap;gap:8px}"
        ".g img{width:140px;height:140px;object-fit:cover;border:1px solid #eee;"
        "border-radius:4px}</style><h1>店铺图片 ↔ 产品对照图册</h1>"
        + "".join(cards))

    print(f"\n✅ 完成！共下载 {len(rows)} 张图")
    print(f"   对照清单: {manifest_path}")
    print(f"   可视图册: {os.path.join(a.out, '_gallery.html')}（浏览器打开）")

if __name__ == "__main__":
    main()
