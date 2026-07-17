# 图片替换清单（IMAGE-GUIDE）

## 🚀 方案一（最强）：一键全量下载整个店铺图片 — tools/crawl_store.py

自动从店铺首页出发，遍历**首页 + 产品列表页 + 全部产品详情页 + 公司介绍页**，
渲染 JS 动态内容后下载所有原图，并自动建档：

```
store-images/
├── products/
│   ├── 001-New-style-Plastic-white-chef-jacket-button/   ← 每个产品一个文件夹
│   │   ├── 01.jpg  02.jpg  ...
│   ├── 002-xxx/ ...
├── store-pages/          ← 首页、公司介绍页的图片
├── manifest.csv          ← 图片 ↔ 产品标题 ↔ 页面网址 对照表（Excel可直接打开）
└── _gallery.html         ← 可视化图册：浏览器打开，按产品分组浏览全部图片
```

使用（你的电脑上，只需装一次依赖）：
```
pip install playwright
playwright install chromium
python3 tools/crawl_store.py
```
脚本带 1.5 秒访问间隔、断点续传（重跑自动跳过已下载）；
遇到滑块验证时加 `--show` 参数以可视窗口运行，手动滑一次即可继续。
下载完后从 `_gallery.html` 图册里挑图，按下方对照表命名放入网站 `images/`
（或配合方案二的 images-map.txt 自动替换）。

---


## ⚡ 方案二：定向替换 8 张关键图（5 分钟）（5 分钟，tools/ 目录已备好工具）

1. **提取地址**：Chrome 打开你的阿里店铺页 → F12 → Console → 粘贴运行 `tools/grab_images.js` → 所有产品图**原图地址**自动复制到剪贴板（多翻几个产品页和公司介绍页各跑一次，收集更全）
2. **填映射表**：打开 `tools/images-map.txt`，把地址贴到对应行（哪行不填就保留占位图）
3. **一键执行**：在网站根目录运行 `python3 tools/replace_images.py` —— 自动下载、裁剪成 4:3 并压缩到 1200×900、存入 images/、并把所有 HTML 的引用从 .webp 自动改为 .jpg
4. 本地确认后提交 GitHub，Vercel 自动重新部署

> 为什么不能全自动？阿里页面是 JS 动态渲染且图片 CDN 有访问限制，构建环境抓不到；上面的流程把人工部分压缩到了"复制粘贴地址"这一步。
> 提取的缩略图地址脚本会自动还原为原图；个别图若下载失败，按提示在浏览器右键另存并手动命名放入 images/ 即可。

---

## 方案三：纯手动替换（备选）


当前 `images/` 目录内是专业风格的 **SVG 占位插图**（线稿/规格图风格），网站可直接上线使用。
但**真实产品实拍图对 B2B 询盘转化至关重要**，建议尽快按下表替换。

## 替换方法

两种任选其一：

- **方法 A（最简单）**：把真实照片转成 JPG，按下表"建议文件名"命名，放入 `images/`，然后在 HTML 中全局搜索对应的 `.webp` 文件名，替换为新的 `.jpg` 文件名。
- **方法 B（R2）**：图片上传 Cloudflare R2，把 HTML 中 `images/xxx.webp` 替换为 R2 完整 URL。

照片要求：白底或浅灰底、光线均匀、对焦清晰；**比例 4:3，建议 1200×900px**，单张压缩到 200KB 以内（可用 tinypng.com 或 squoosh.app）。

## 对照表

| 当前占位文件 | 应替换为 | 建议文件名 | 用在哪 |
|---|---|---|---|
| `cat-resin-buttons.webp` | 树脂/聚酯纽扣组合图（多色四孔扣平铺） | `cat-resin-buttons.jpg` | 首页品类卡、树脂纽扣页 |
| `cat-metal-buttons.webp` | 金属纽扣（锌合金/黄铜柄扣、西装扣） | `cat-metal-buttons.jpg` | 首页品类卡、金属纽扣页 |
| `cat-snap-buttons.webp` | 四合扣四件套展开图 | `cat-snap-buttons.jpg` | 首页品类卡、四合扣页 |
| `cat-jeans-buttons.webp` | 牛仔扣+铆钉（最好钉在牛仔布上的效果图） | `cat-jeans-buttons.jpg` | 首页品类卡、牛仔扣页 |
| `cat-natural-buttons.webp` | corozo/牛角/木质/椰壳扣组合 | `cat-natural-buttons.jpg` | 首页品类卡、天然纽扣页 |
| `cat-hardware.webp` | 绳扣、鸡眼扣、插扣组合 | `cat-hardware.jpg` | 首页品类卡、辅料五金页 |
| `hero-button-drawing.webp` | 最有质感的一张主打产品大图（首屏门面） | `hero-main.jpg` | 首页首屏 |
| `factory-placeholder.webp` | 工厂车间/生产线/质检实拍 | `factory.jpg` | 关于我们页 |

## 还需要额外准备的图

| 文件 | 规格 | 用途 |
|---|---|---|
| `og-default.png` | **1200×630px** PNG/JPG | 社交分享缩略图（WhatsApp/LinkedIn 转发链接时显示）。做法：产品大图 + 公司名 + "Button Manufacturer Since 2008" 一行字即可。放入 `images/` 后无需改代码（HTML 中已引用该文件名）。 |
| 各品类页产品卡小图（可选） | 4:3，800×600px | 每个品类页有 4 张产品卡，目前共用品类占位图。有条件时为每个单品拍照，分别命名如 `resin-4hole-18l.jpg` 并替换对应 `<img>` 的 src，转化率更高。 |

## 从阿里店铺取图

可直接使用你阿里国际站后台的原始产品图（你拥有版权）。从店铺前台另存的图片分辨率较低且带水印参数，建议从后台素材库下载原图。
