#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
use_local_images.py — 把 images/ 里的真实图片一键替换进网站
============================================================
用法：
  1. 从 store-images/_gallery.html 图册里挑好图，复制到网站的 images/ 文件夹，
     并按下面的名字重命名（jpg/jpeg/png/webp 都可以）：
        hero-button-drawing   首页首屏大图
        cat-resin-buttons     树脂/聚酯纽扣
        cat-metal-buttons     金属纽扣
        cat-snap-buttons      四合扣
        cat-jeans-buttons     牛仔扣/铆钉
        cat-natural-buttons   天然材质纽扣
        cat-hardware          绳扣/鸡眼/插扣
        factory-placeholder   工厂/车间图
  2. 在网站根目录运行：  python tools\\use_local_images.py
     脚本自动：检测哪些图已就位 → 压缩裁剪为 4:3 1200x900（装了 Pillow 时）
     → 把所有 HTML 里对应的 .svg 引用改为新图 → 输出报告。
  放几张就替换几张，没放的保留 SVG 占位图。可重复运行。
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGDIR = os.path.join(ROOT, "images")
NAMES = ["hero-button-drawing", "cat-resin-buttons", "cat-metal-buttons",
         "cat-snap-buttons", "cat-jeans-buttons", "cat-natural-buttons",
         "cat-hardware", "factory-placeholder"]
EXTS = [".jpg", ".jpeg", ".png", ".webp"]

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("提示：未装 Pillow，跳过压缩（建议 pip install pillow）\n")

def compress(path):
    """裁剪4:3、缩放至1200宽、另存为同名.jpg，返回最终文件名"""
    base = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(IMGDIR, base + ".jpg")
    if not HAS_PIL:
        return os.path.basename(path)
    im = Image.open(path).convert("RGB")
    w, h = im.size
    tw, th = (w, int(w*3/4)) if w/h <= 4/3 else (int(h*4/3), h)
    L, T = (w-tw)//2, (h-th)//2
    im = im.crop((L, T, L+tw, T+th))
    if im.width > 1200:
        im = im.resize((1200, 900), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    if os.path.abspath(out) != os.path.abspath(path):
        try: os.remove(path)
        except OSError: pass
    return base + ".jpg"

def main():
    found = {}
    for name in NAMES:
        for ext in EXTS:
            p = os.path.join(IMGDIR, name + ext)
            if os.path.exists(p):
                found[name] = compress(p)
                break
    if not found:
        sys.exit("images/ 里还没有按规定名字放置任何图片，请先放图（见脚本顶部说明）。")

    print("检测到以下图片，开始替换：")
    for k, v in found.items():
        kb = os.path.getsize(os.path.join(IMGDIR, v)) // 1024
        print(f"  ✓ {k}  →  images/{v}（{kb} KB）")

    n = 0
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in
                   ("tools", "__pycache__", ".git", "store-images")]
        for fn in files:
            if not fn.endswith(".html"):
                continue
            p = os.path.join(dirpath, fn)
            s = open(p, encoding="utf-8").read(); orig = s
            for name, newfile in found.items():
                s = re.sub(rf"images/{re.escape(name)}\.(svg|jpg|jpeg|png|webp)",
                           f"images/{newfile}", s)
            if s != orig:
                open(p, "w", encoding="utf-8").write(s); n += 1

    missing = [x for x in NAMES if x not in found]
    print(f"\n✅ 完成：替换 {len(found)} 张图，更新 {n} 个 HTML 文件。")
    if missing:
        print("尚未替换（保留占位图）：" + "、".join(missing))
    print("本地确认后提交 GitHub 即可，Vercel 会自动重新部署。")

if __name__ == "__main__":
    main()
