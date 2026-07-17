# Merit Button 独立站 — 部署与使用指南

为 **温州 Merit 服装辅料（Wenzhou Merit Garment Co., Ltd.）** 构建的 B2B 纽扣外贸独立站。
纯静态 HTML，无需任何后端，开箱即可部署到 Vercel。

---

## 一、网站包含什么

| 页面 | 路径 | 说明 |
|---|---|---|
| 首页 | `/` | Hero 工程图 + 6 大品类 + 优势 + 流程 + FAQ |
| 产品中心 | `/products/` | 全品类导航 |
| 树脂纽扣 | `/products/resin-buttons` | 含规格表、产品卡、FAQ、Product 结构化数据 |
| 金属纽扣 | `/products/metal-buttons` | 同上 |
| 四合扣 | `/products/snap-buttons` | 同上 |
| 牛仔扣/铆钉 | `/products/jeans-buttons` | 同上 |
| 天然材质纽扣 | `/products/natural-buttons` | corozo/牛角/木/椰壳 |
| 绳扣·鸡眼·插扣 | `/products/cord-stoppers` | 辅料五金 |
| OEM 定制 | `/custom-buttons` | logo 定制、模具、潘通配色 |
| 关于我们 | `/about` | 公司介绍 |
| 联系/询盘 | `/contact` | RFQ 表单（Formspree） |
| FAQ | `/faq` | 20 条问答 + FAQPage 结构化数据 |
| 博客 | `/blog/` | 3 篇 SEO 引流文章（尺码表/材质对比/牛仔扣选购） |
| 404 | `/404` | 自动生效 |

SEO/AEO 已内置：每页独立 title/description/canonical/OG 标签、JSON-LD 结构化数据（Organization、Product、FAQPage、Article、BreadcrumbList）、`sitemap.xml`、`robots.txt`（已放行 GPTBot/ClaudeBot/PerplexityBot 等 AI 爬虫）、`llms.txt`（供 AI 助手引用推荐）。

---

## 二、上线前检查：联系方式与域名

当前仓库已配置为下面信息；如后续更换联系人或域名，用 VS Code 全局搜索替换（Ctrl+Shift+H）对整个文件夹执行：

| 当前值 | 用途 | 出现位置 |
|---|---|---|
| `https://www.merittrims.com` | 真实域名（含 https://，不带末尾斜杠） | 所有 HTML、sitemap.xml、robots.txt、llms.txt |
| `maggie@merittrims.com` | 业务邮箱 | 所有 HTML、llms.txt |
| `+86 15869483966` | 电话/WhatsApp 展示文案 | 所有 HTML、llms.txt |
| `8615869483966` | WhatsApp 链接号码（国家码+号码，无+号无空格） | 所有 HTML、JS、llms.txt |
| `YOUR_FORM_ID` | 待配置 Formspree 表单 ID（见下文第五节） | contact.html 等含表单页面 |

> 公司地址目前写的是 "Wenzhou, Zhejiang, China"，如需详细地址请搜索替换补充。

---

## 三、部署到 Vercel（GitHub 方式，推荐）

1. **建 GitHub 仓库**：新建私有仓库（如 `meritbutton-site`），把本文件夹全部内容上传（含 `vercel.json`）。
   - 可删除的构建脚本：`sitegen.py`、`gen_core.py`、`gen_pages.py`、`gen_sitemap.py`、`build_images.py`、`__pycache__/`。建议保留在仓库里方便日后改版，它们不影响部署。
2. **Vercel 导入**：登录 vercel.com → Add New → Project → 选择该仓库 → Framework 选 **Other** → 不需要任何 Build 设置（静态站）→ Deploy。
3. 部署完成后会得到 `xxx.vercel.app` 临时域名，先打开检查页面是否正常。

`vercel.json` 已配置 `cleanUrls: true`，站内链接均为无 `.html` 的干净 URL（如 `/products/resin-buttons`）。
**注意**：本地直接双击 HTML 预览时这些链接打不开属正常现象；本地预览请用支持 clean URL 的服务器，或直接看 Vercel 预览。

## 四、绑定自有域名（Cloudflare DNS）

1. Vercel 项目 → Settings → Domains → 添加 `www.你的域名.com` 和根域名。
2. 在 Cloudflare DNS 按 Vercel 提示添加记录：
   - `www` → CNAME → `cname.vercel-dns.com`
   - 根域名 → A → `76.76.21.21`
3. Cloudflare 中这两条记录建议先设为 **DNS only（灰云）**，由 Vercel 签发 SSL，最稳妥。
4. 在 Vercel 里把 `www` 设为主域名（根域名自动 301 跳转）。

### Cloudflare R2 放产品图（可选）
真实产品图较多时可放 R2：建 bucket → 开启公开访问/绑定自定义子域（如 `img.你的域名.com`）→ 上传图片 → 把 HTML 中 `images/xxx.webp` 的引用改为 R2 完整 URL。图片不多时直接放在仓库 `images/` 目录即可，无需 R2。

## 五、询盘表单（Formspree）

1. 注册 formspree.io（免费档每月 50 条询盘够用）→ New Form → 拿到形如 `mqkrxxxx` 的 ID。
2. 全局把 `YOUR_FORM_ID` 替换为该 ID。
3. 在 Formspree 后台把通知邮箱设为你的业务邮箱。
4. 未配置 Formspree 时表单会自动降级为打开邮件客户端（mailto），不会丢询盘入口。
5. WhatsApp 浮动按钮全站常驻，替换号码后即可直达对话。

## 六、上线后 SEO 动作清单

1. **Google Search Console**：添加并验证域名 → 提交 `https://你的域名/sitemap.xml` → 对首页和主要品类页用"网址检查"请求编入索引。
2. **Bing Webmaster Tools**：可直接从 GSC 导入，提交同一 sitemap（Bing 收录会被 ChatGPT 等引用）。
3. 在阿里国际站店铺简介、邮件签名、WhatsApp 资料中加上独立站链接（外链+品牌信号）。
4. 替换 SVG 占位图为真实产品图：`tools/` 目录有半自动工具（浏览器一键提取店铺图片地址 + 脚本自动下载压缩替换），详见 `IMAGE-GUIDE.md`。
5. 之后每月在 `/blog/` 增加 1–2 篇英文行业文章（可参考现有 3 篇的写法），持续积累长尾词。

## 七、日常修改

- 改文字：直接编辑对应 HTML 文件，提交到 GitHub，Vercel 自动重新部署（约 30 秒）。
- 批量改版：修改 `sitegen.py` / `gen_core.py` / `gen_pages.py` 后本地运行 `python3 gen_core.py && python3 gen_pages.py` 重新生成。
- 新增页面后记得更新 `sitemap.xml`（或改 `gen_sitemap.py` 后重跑）。
