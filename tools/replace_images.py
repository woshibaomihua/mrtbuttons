#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
replace_images.py — 一键下载店铺图片并自动替换进网站
====================================================
在【你自己的电脑】上运行（沙盒/服务器无法访问阿里图片CDN）。

用法：
  1. 先用 tools/grab_images.js 在店铺页面提取图片地址
  2. 编辑 tools/images-map.txt，把地址填到对应行
  3. 在网站根目录运行：
       python3 tools/replace_images.py
     （Windows: 双击或 python tools\\replace_images.py）

脚本会自动：
  ✓ 下载每张图片（带浏览器 UA，绕过基础防盗链）
  ✓ 裁剪为 4:3 并缩放到 1200x900，压缩为 JPG（需要 Pillow；
    没装 Pillow 则原样保存，建议先 pip install pillow）
  ✓ 存入 images/ 目录
  ✓ 自动把所有 HTML 中对应的 .svg 占位引用改为新 .jpg
  ✓ 生成替换报告

可重复运行：改了 map 再跑一次即可，已替换过的会更新。
"""
import os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "tools", "images-map.txt")
IMGDIR = os.path.join(ROOT, "images")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("⚠ 未安装 Pillow，图片将不做裁剪压缩。建议: pip install pillow\n")

def parse_map():
    pairs = []
    if not os.path.exists(MAP):
        sys.exit("找不到 tools/images-map.txt")
    for ln in open(MAP, encoding="utf-8"):
        ln = ln.strip()
        if not ln or ln.startswith("#") or "=" not in ln:
            continue
        name, url = [x.strip() for x in ln.split("=", 1)]
        if url.startswith("http") and "粘贴" not in url and "地址" not in url:
            pairs.append((name, url))
    return pairs

def download(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Referer": "https://www.alibaba.com/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def process(name, raw):
    out = os.path.join(IMGDIR, name + ".jpg")
    if HAS_PIL:
        import io
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        w, h = im.size
        # 居中裁剪为 4:3
        tw, th = (w, int(w * 3 / 4)) if w / h <= 4 / 3 else (int(h * 4 / 3), h)
        L, T = (w - tw) // 2, (h - th) // 2
        im = im.crop((L, T, L + tw, T + th))
        if im.width > 1200:
            im = im.resize((1200, 900), Image.LANCZOS)
        im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    else:
        open(out, "wb").write(raw)
    return out

def patch_html(replaced):
    n = 0
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ("tools", "__pycache__", ".git")]
        for fn in files:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            s = open(p, encoding="utf-8").read()
            orig = s
            for name in replaced:
                s = s.replace(f"images/{name}.svg", f"images/{name}.jpg")
            if s != orig:
                open(p, "w", encoding="utf-8").write(s)
                n += 1
    return n

def main():
    pairs = parse_map()
    if not pairs:
        sys.exit("images-map.txt 里还没有填任何有效的图片地址，请先填写。")
    ok = []
    for name, url in pairs:
        try:
            print(f"下载 {name} ← {url[:70]}...")
            out = process(name, download(url))
            print(f"  ✓ 已保存 {os.path.relpath(out, ROOT)}"
                  f"（{os.path.getsize(out)//1024} KB）")
            ok.append(name)
        except Exception as e:
            print(f"  ✗ 失败：{e}（可在浏览器打开该地址右键另存，"
                  f"手动按 {name}.jpg 命名放入 images/，"
                  f"再把 HTML 里 {name}.svg 改成 {name}.jpg）")
    if ok:
        n = patch_html(ok)
        print(f"\n✅ 完成：成功替换 {len(ok)} 张图，更新了 {n} 个 HTML 文件。")
        print("   本地预览确认后提交到 GitHub，Vercel 会自动重新部署。")

if __name__ == "__main__":
    main()
