/* ============================================================
   grab_images.js — 阿里店铺图片地址一键提取器
   用法：
   1. 用 Chrome/Edge 打开你的店铺页面（店铺首页或任意产品页）
      https://meritbutton.en.alibaba.com/
   2. 按 F12 打开开发者工具 → 切到 Console（控制台）标签
   3. 把本文件全部内容复制粘贴进去，回车
   4. 页面所有产品图的【原图地址】会自动复制到剪贴板，
      同时在控制台打印出来
   5. 粘贴到 tools/images-map.txt 里，给每张图配上目标文件名
      （格式见 images-map.txt 内说明），然后运行 replace_images.py
   提示：多翻几个产品页、"Company Profile"公司页各跑一次，
        就能把产品图+车间图都收集齐。
   ============================================================ */
(function () {
  const urls = new Set();
  document.querySelectorAll("img").forEach((img) => {
    let s = img.currentSrc || img.src || img.dataset.src || "";
    if (!s || !/alicdn\.com/.test(s)) return;
    // 去掉缩略图尺寸后缀，还原为原图：xxx.jpg_220x220.jpg / _.webp 等
    s = s.replace(/_\d+x\d+[a-z0-9]*\.(jpg|png|webp)$/i, "");
    s = s.replace(/_\.webp$/i, "");
    s = s.replace(/\.(jpg|png)_\.webp$/i, ".$1");
    if (/\.(jpg|jpeg|png|webp)$/i.test(s)) urls.add(s.split("?")[0]);
  });
  const list = [...urls].join("\n");
  console.log("共提取到 " + urls.size + " 张图片：\n" + list);
  if (navigator.clipboard) {
    navigator.clipboard
      .writeText(list)
      .then(() => console.log("✅ 已复制到剪贴板，直接粘贴即可"));
  }
})();
