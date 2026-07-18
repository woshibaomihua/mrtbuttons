/* Merit Button — site JS */
document.addEventListener('DOMContentLoaded', function () {
  // mobile menu
  var hamb = document.querySelector('.hamb');
  var menu = document.querySelector('nav.menu');
  if (hamb && menu) {
    hamb.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      hamb.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // mark current nav item
  var path = location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('nav.menu a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href && href !== '/' && path.indexOf(href.replace(/\.html$/, '')) === 0) {
      a.setAttribute('aria-current', 'page');
    } else if (href === '/' && (path === '/' || path === '/index.html')) {
      a.setAttribute('aria-current', 'page');
    }
  });

  // inquiry form: AJAX submit to Formspree (replace YOUR_FORM_ID in HTML action)
  document.querySelectorAll('form.inq, form.mini-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      var action = form.getAttribute('action') || '';
      if (action.indexOf('YOUR_FORM_ID') !== -1 || action.indexOf('PENDING_NEW_FORM_ID') !== -1) {
        // not configured yet — fall back to mailto so inquiries are never lost
        e.preventDefault();
        var data = new FormData(form);
        var body = '';
        data.forEach(function (v, k) {
          if (v && typeof File !== 'undefined' && v instanceof File) {
            if (v.name) body += k + ': ' + v.name + ' (' + Math.round(v.size / 1024) + ' KB)' + '\n';
          } else {
            body += k + ': ' + v + '\n';
          }
        });
        location.href = 'mailto:' + (form.dataset.email || 'mrtmaggie0010@gmail.com') +
          '?subject=' + encodeURIComponent('Inquiry from website') +
          '&body=' + encodeURIComponent(body);
        return;
      }
      e.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      var orig = btn.textContent;
      btn.textContent = 'Sending…'; btn.disabled = true;
      fetch(action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function (r) {
        if (r.ok) {
          form.innerHTML = '<h3>Inquiry received ✓</h3><p>Thank you. Our sales team will reply within 12 hours (usually much faster). Please also check your spam folder for our reply from mrtmaggie0010@gmail.com.</p>';
        } else { throw new Error('failed'); }
      }).catch(function () {
        btn.textContent = orig; btn.disabled = false;
        alert('Could not send right now. Please email us directly: mrtmaggie0010@gmail.com');
      });
    });
  });

  // current year in footer
  document.querySelectorAll('.year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
});


/* ===== Premium v2 interactions ===== */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // header scrolled state
  var hd = document.querySelector("header.site");
  if (hd) {
    var onScroll = function () { hd.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  // scroll reveal — only hide elements once we know JS+observer will reveal them
  var targets = document.querySelectorAll(".card, .section-head, .steps > div, .rail-box, details.faq, .prose > h2");
  if ("IntersectionObserver" in window && !reduce && targets.length) {
    document.documentElement.classList.add("js-reveal");
    targets.forEach(function (el, i) {
      el.classList.add("reveal");
      el.style.transitionDelay = Math.min((i % 6) * 70, 350) + "ms";
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    targets.forEach(function (el) { io.observe(el); });
    // failsafe: if anything is still hidden after 3.5s (e.g. tall page, no scroll), reveal it
    setTimeout(function () { targets.forEach(function (el) { el.classList.add("in"); }); }, 3500);
  }

  // hero stat count-up
  var stats = document.querySelectorAll(".spec-strip b, .trust-stat b");
  if (stats.length && !reduce && "IntersectionObserver" in window) {
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, raw = el.textContent.trim(),
            m = raw.match(/^(\d+)(.*)$/);
        if (m) {
          var end = +m[1], suf = m[2], t0 = null;
          var step = function (ts) {
            if (!t0) t0 = ts;
            var p = Math.min((ts - t0) / 1100, 1);
            el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suf;
            if (p < 1) requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
        }
        so.unobserve(el);
      });
    }, { threshold: 0.6 });
    stats.forEach(function (el) { so.observe(el); });
  }
})();


/* ===== Premium v3: conversion & motion ===== */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* scroll progress hairline */
  var prog = document.createElement("div");
  prog.className = "scroll-progress";
  document.body.appendChild(prog);
  var onScrollP = function () {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    prog.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + "%";
  };
  window.addEventListener("scroll", onScrollP, { passive: true }); onScrollP();

  /* hero parallax: cluster image drifts subtly with cursor */
  var stage = document.querySelector(".cluster-wrap");
  if (stage && !reduce && matchMedia("(pointer:fine)").matches) {
    var hero = document.querySelector(".hero");
    var cluster = stage.querySelector(".cluster");
    hero.addEventListener("mousemove", function (e) {
      var r = hero.getBoundingClientRect();
      var dx = (e.clientX - r.left) / r.width - 0.5,
          dy = (e.clientY - r.top) / r.height - 0.5;
      if (cluster) cluster.style.transform = "translate(" + dx * 14 + "px," + dy * 14 + "px)";
    });
    hero.addEventListener("mouseleave", function () {
      if (cluster) cluster.style.transform = "";
    });
  }
})();

/* ===== Product image detail viewer: hover zoom + loupe + click lightbox ===== */
(function () {
  function closest(el, sel) {
    return el && el.closest ? el.closest(sel) : null;
  }
  function text(el) {
    return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : '';
  }
  function absUrl(src) {
    var a = document.createElement('a');
    a.href = src;
    return a.href;
  }
  function shouldMagnify(img, card) {
    var hay = [img.alt, img.src, text(card && card.querySelector('h3')), text(card && card.querySelector('.tag')), text(card && card.querySelector('.chips'))].join(' ').toLowerCase();
    return /(board|sample|size|range|matrix|grid|assort|assorted|collection|catalog|catalogue|chart|lineup|mixed|style|styles|sheet|family|set)/i.test(hay);
  }
  function getCardInfo(img) {
    var card = closest(img, '.sheet-card, .product-showcase .card');
    var title = text(card && card.querySelector('h3')) || img.alt || 'Product detail image';
    var desc = text(card && card.querySelector('figcaption p, .body p')) || img.alt || '';
    var chips = [];
    if (card) card.querySelectorAll('.tag, .chips span, .meta').forEach(function (el) {
      var raw = text(el);
      if (!raw) return;
      raw.split('·').forEach(function (part) {
        var v = part.trim(); if (v && chips.indexOf(v) === -1) chips.push(v);
      });
    });
    return { card: card, title: title, desc: desc, chips: chips.slice(0, 8) };
  }
  function createLightbox() {
    var lb = document.createElement('div');
    lb.className = 'product-lightbox';
    lb.setAttribute('aria-hidden', 'true');
    lb.innerHTML = '' +
      '<div class="product-lightbox__backdrop" data-close="true"></div>' +
      '<div class="product-lightbox__panel" role="dialog" aria-modal="true" aria-label="Product image detail viewer">' +
        '<button class="product-lightbox__close" type="button" aria-label="Close image viewer">×</button>' +
        '<div class="product-lightbox__stage" tabindex="0">' +
          '<img class="product-lightbox__img" alt="" draggable="false">' +
          '<div class="product-lightbox__hint">Wheel / pinch to zoom · drag to pan</div>' +
        '</div>' +
        '<aside class="product-lightbox__info">' +
          '<p class="product-lightbox__eyebrow">Product detail</p>' +
          '<h3 class="product-lightbox__title"></h3>' +
          '<p class="product-lightbox__desc"></p>' +
          '<div class="product-lightbox__chips"></div>' +
          '<div class="product-lightbox__tools">' +
            '<a class="price-sample-cta" href="/contact">Request price &amp; samples →</a>' +
            '<p class="product-lightbox__small">Use the large image to confirm texture, hole position, rim shape, color tone and sample-board details before RFQ.</p>' +
          '</div>' +
        '</aside>' +
      '</div>';
    document.body.appendChild(lb);
    return lb;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var imgs = Array.prototype.slice.call(document.querySelectorAll('.product-showcase .card .ph img, figure.sheet-card > img'));
    if (!imgs.length) return;

    var finePointer = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var loupe = document.createElement('div');
    loupe.className = 'product-detail-loupe';
    loupe.setAttribute('aria-hidden', 'true');
    document.body.appendChild(loupe);

    var lightbox = null, stage, modalImg, titleEl, descEl, chipsEl, closeBtn;
    var scale = 1, panX = 0, panY = 0;
    var activePointers = new Map();
    var dragStart = null, pinchStart = null;

    function ensureLightbox() {
      if (lightbox) return;
      lightbox = createLightbox();
      stage = lightbox.querySelector('.product-lightbox__stage');
      modalImg = lightbox.querySelector('.product-lightbox__img');
      titleEl = lightbox.querySelector('.product-lightbox__title');
      descEl = lightbox.querySelector('.product-lightbox__desc');
      chipsEl = lightbox.querySelector('.product-lightbox__chips');
      closeBtn = lightbox.querySelector('.product-lightbox__close');

      closeBtn.addEventListener('click', closeLightbox);
      lightbox.querySelector('.product-lightbox__backdrop').addEventListener('click', closeLightbox);
      document.addEventListener('keydown', function (e) {
        if (!lightbox.classList.contains('open')) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === '+' || e.key === '=') { setZoom(scale + .25); }
        if (e.key === '-') { setZoom(scale - .25); }
        if (e.key === '0') { resetZoom(); }
      });
      stage.addEventListener('wheel', function (e) {
        if (!lightbox.classList.contains('open')) return;
        e.preventDefault();
        var next = scale + (e.deltaY < 0 ? .25 : -.25);
        setZoom(next);
      }, { passive: false });
      stage.addEventListener('pointerdown', function (e) {
        activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
        stage.setPointerCapture(e.pointerId);
        stage.classList.add('dragging');
        if (activePointers.size === 1) {
          dragStart = { x: e.clientX, y: e.clientY, panX: panX, panY: panY };
        } else if (activePointers.size === 2) {
          var pts = Array.from(activePointers.values());
          pinchStart = { dist: distance(pts[0], pts[1]), scale: scale };
        }
      });
      stage.addEventListener('pointermove', function (e) {
        if (!activePointers.has(e.pointerId)) return;
        activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
        if (activePointers.size >= 2 && pinchStart) {
          var pts = Array.from(activePointers.values());
          var ratio = distance(pts[0], pts[1]) / Math.max(1, pinchStart.dist);
          setZoom(pinchStart.scale * ratio);
        } else if (dragStart && scale > 1) {
          panX = dragStart.panX + (e.clientX - dragStart.x);
          panY = dragStart.panY + (e.clientY - dragStart.y);
          applyTransform();
        }
      });
      ['pointerup','pointercancel','pointerleave'].forEach(function (ev) {
        stage.addEventListener(ev, function (e) {
          activePointers.delete(e.pointerId);
          if (!activePointers.size) {
            stage.classList.remove('dragging');
            dragStart = null; pinchStart = null;
          }
        });
      });
    }
    function distance(a, b) {
      var dx = a.x - b.x, dy = a.y - b.y;
      return Math.sqrt(dx * dx + dy * dy);
    }
    function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }
    function setZoom(next) {
      var old = scale;
      scale = clamp(next, 1, 4);
      if (scale === 1 && old !== 1) { panX = 0; panY = 0; }
      applyTransform();
    }
    function resetZoom() { scale = 1; panX = 0; panY = 0; applyTransform(); }
    function applyTransform() {
      if (!modalImg) return;
      modalImg.style.setProperty('--zoom', scale.toFixed(2));
      modalImg.style.setProperty('--pan-x', panX.toFixed(1) + 'px');
      modalImg.style.setProperty('--pan-y', panY.toFixed(1) + 'px');
    }
    function openLightbox(img) {
      ensureLightbox();
      var info = getCardInfo(img);
      resetZoom();
      modalImg.src = absUrl(img.currentSrc || img.src);
      modalImg.alt = img.alt || info.title;
      titleEl.textContent = info.title;
      descEl.textContent = info.desc;
      chipsEl.innerHTML = '';
      info.chips.forEach(function (c) {
        var s = document.createElement('span');
        s.textContent = c;
        chipsEl.appendChild(s);
      });
      lightbox.classList.add('open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.classList.add('detail-viewer-open');
      setTimeout(function () { closeBtn.focus(); }, 10);
    }
    function closeLightbox() {
      if (!lightbox) return;
      lightbox.classList.remove('open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('detail-viewer-open');
      activePointers.clear();
      loupe.classList.remove('show');
    }
    function moveLoupe(e, img) {
      if (!finePointer || reduceMotion) return;
      var viewer = closest(img, '.product-media-viewer');
      if (!viewer || viewer.dataset.magnify !== 'true') return;
      var rect = img.getBoundingClientRect();
      if (rect.width < 80 || rect.height < 80) return;
      var x = clamp(e.clientX - rect.left, 0, rect.width);
      var y = clamp(e.clientY - rect.top, 0, rect.height);
      var zoom = 3;
      var lw = loupe.offsetWidth || 190, lh = loupe.offsetHeight || 190;
      var bgW = rect.width * zoom, bgH = rect.height * zoom;
      var bgX = -(x * zoom - lw / 2);
      var bgY = -(y * zoom - lh / 2);
      var left = e.clientX + 24;
      var top = e.clientY + 24;
      if (left + lw + 14 > window.innerWidth) left = e.clientX - lw - 24;
      if (top + lh + 14 > window.innerHeight) top = e.clientY - lh - 24;
      loupe.style.left = Math.max(10, left) + 'px';
      loupe.style.top = Math.max(10, top) + 'px';
      loupe.style.backgroundImage = 'url("' + absUrl(img.currentSrc || img.src) + '")';
      loupe.style.backgroundSize = bgW + 'px ' + bgH + 'px';
      loupe.style.backgroundPosition = bgX + 'px ' + bgY + 'px';
      loupe.classList.add('show');
    }

    imgs.forEach(function (img) {
      if (img.dataset.viewerReady === 'true') return;
      img.dataset.viewerReady = 'true';
      img.classList.add('product-zoom-img');
      var card = closest(img, '.sheet-card, .product-showcase .card');
      var viewer = null;
      if (img.parentElement && img.parentElement.classList.contains('ph')) {
        viewer = img.parentElement;
      } else {
        viewer = document.createElement('div');
        viewer.className = 'product-media-viewer';
        img.parentNode.insertBefore(viewer, img);
        viewer.appendChild(img);
      }
      viewer.classList.add('product-media-viewer');
      viewer.dataset.magnify = shouldMagnify(img, card) ? 'true' : 'false';
      viewer.setAttribute('role', 'button');
      viewer.setAttribute('tabindex', '0');
      viewer.setAttribute('aria-label', 'Open large product image: ' + (getCardInfo(img).title || img.alt || 'product image'));
      if (!viewer.querySelector('.product-zoom-icon')) {
        var icon = document.createElement('span');
        icon.className = 'product-zoom-icon';
        icon.setAttribute('aria-hidden', 'true');
        icon.textContent = '⌕';
        viewer.appendChild(icon);
      }
      viewer.addEventListener('click', function () { openLightbox(img); });
      viewer.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openLightbox(img); }
      });
      viewer.addEventListener('pointermove', function (e) { moveLoupe(e, img); });
      viewer.addEventListener('pointerleave', function () { loupe.classList.remove('show'); });
      viewer.addEventListener('blur', function () { loupe.classList.remove('show'); });
    });
  });
})();

/* 2026-06-28: keep Products mega-menu open while moving from nav link to dropdown */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var fineHover = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (!fineHover) return;
    document.querySelectorAll('nav.menu > .has-sub').forEach(function (item) {
      var closeTimer = null;
      var open = function () {
        if (closeTimer) window.clearTimeout(closeTimer);
        item.classList.add('is-open');
      };
      var close = function () {
        if (closeTimer) window.clearTimeout(closeTimer);
        closeTimer = window.setTimeout(function () {
          item.classList.remove('is-open');
        }, 260);
      };
      item.addEventListener('mouseenter', open);
      item.addEventListener('mouseleave', close);
      item.addEventListener('focusin', open);
      item.addEventListener('focusout', function (event) {
        if (!item.contains(event.relatedTarget)) close();
      });
    });
  });
})();


/* ===== RFQ handoff: product cards -> contact page, plus upload/paste support ===== */
(function () {
  function cleanText(el) {
    return el ? (el.textContent || '').replace(/\s+/g, ' ').trim() : '';
  }
  function toAbsPath(src) {
    if (!src) return '';
    try {
      var u = new URL(src, window.location.href);
      return u.pathname + (u.search || '');
    } catch (e) { return src; }
  }
  function productLine() {
    return cleanText(document.querySelector('.page-hero h1, h1')) || document.title.replace(/\s*\|.*$/, '');
  }
  function buildRfqUrl(link) {
    var card = link.closest('.sheet-card, .product-showcase .card, .card');
    var title = '';
    var img = '';
    var desc = '';

    var lightbox = link.closest('.product-lightbox');
    if (lightbox) {
      title = cleanText(lightbox.querySelector('.product-lightbox__title'));
      desc = cleanText(lightbox.querySelector('.product-lightbox__desc'));
      img = lightbox.querySelector('.product-lightbox__img') ? lightbox.querySelector('.product-lightbox__img').getAttribute('src') : '';
    }
    if (!title && card) {
      title = cleanText(card.querySelector('h3')) || productLine();
      desc = cleanText(card.querySelector('p'));
      img = card.querySelector('img') ? card.querySelector('img').getAttribute('src') : '';
    }
    if (!title) title = productLine();

    var url = new URL('/contact', window.location.origin);
    url.searchParams.set('product', title);
    url.searchParams.set('line', productLine());
    url.searchParams.set('source', window.location.pathname.replace(/\/index\.html$/, '/'));
    if (img) url.searchParams.set('image', toAbsPath(img));
    if (desc) url.searchParams.set('note', desc.slice(0, 220));
    return url.pathname + url.search;
  }

  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('a.price-sample-cta');
    if (!link) return;
    link.setAttribute('href', buildRfqUrl(link));
  }, true);

  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form.inq');
    if (!form) return;

    var params = new URLSearchParams(window.location.search);
    var product = params.get('product') || '';
    var line = params.get('line') || '';
    var image = params.get('image') || '';
    var source = params.get('source') || '';
    var note = params.get('note') || '';

    if (product) {
      var card = document.getElementById('selected-product-card');
      var nameEl = document.getElementById('selected-product-name');
      var pageEl = document.getElementById('selected-product-page');
      var imgEl = document.getElementById('selected-product-img');
      if (card && nameEl) {
        card.hidden = false;
        nameEl.textContent = product;
        if (pageEl) pageEl.textContent = (line ? line + ' · ' : '') + (source || 'Product page');
        if (imgEl && image) {
          imgEl.src = image;
          imgEl.alt = product;
        }
      }
      var hiddenProduct = document.getElementById('f-selected-product');
      var hiddenImage = document.getElementById('f-selected-image');
      var hiddenSource = document.getElementById('f-selected-source');
      if (hiddenProduct) hiddenProduct.value = product;
      if (hiddenImage) hiddenImage.value = image;
      if (hiddenSource) hiddenSource.value = source;

      var select = document.getElementById('f-product');
      if (select && line) {
        var low = line.toLowerCase();
        Array.prototype.some.call(select.options, function (opt) {
          var txt = (opt.textContent || '').toLowerCase();
          if ((low.indexOf('metal') >= 0 && txt.indexOf('metal') >= 0) ||
              (low.indexOf('resin') >= 0 && txt.indexOf('resin') >= 0) ||
              (low.indexOf('snap') >= 0 && txt.indexOf('snap') >= 0) ||
              (low.indexOf('jeans') >= 0 && txt.indexOf('jeans') >= 0) ||
              ((low.indexOf('natural') >= 0 || low.indexOf('horn') >= 0 || low.indexOf('shell') >= 0) && (txt.indexOf('corozo') >= 0 || txt.indexOf('horn') >= 0)) ||
              ((low.indexOf('cord') >= 0 || low.indexOf('buckle') >= 0 || low.indexOf('eyelet') >= 0) && txt.indexOf('cord') >= 0)) {
            select.value = opt.value || opt.textContent;
            return true;
          }
          return false;
        });
      }
      var msg = document.getElementById('f-msg');
      if (msg && !msg.value) {
        msg.value = 'I am interested in: ' + product + (line ? ' (' + line + ')' : '') + '.\n' +
          (source ? 'Source page: ' + source + '\n' : '') +
          (image ? 'Reference image: ' + image + '\n' : '') +
          (note ? 'Product note: ' + note + '\n' : '') +
          '\nPlease quote MOQ, unit price, sample lead time and bulk lead time.';
      }
    }

    // File upload / drag-drop / paste support
    var input = document.getElementById('f-attachments');
    var drop = document.getElementById('file-drop');
    var list = document.getElementById('file-list');
    if (!input || !drop || !list || typeof DataTransfer === 'undefined') return;

    var dt = new DataTransfer();
    var previewUrls = [];

    function formatFileSize(file) {
      if (!file || !file.size) return '';
      if (file.size < 1024 * 1024) return (file.size / 1024).toFixed(0) + ' KB';
      return (file.size / 1024 / 1024).toFixed(1) + ' MB';
    }

    function fileExt(file) {
      var name = file && file.name ? file.name : 'file';
      var parts = name.split('.');
      return parts.length > 1 ? parts.pop().slice(0, 5).toUpperCase() : 'FILE';
    }

    function syncInputFiles() {
      input.files = dt.files;
    }

    function addFiles(files) {
      Array.prototype.forEach.call(files || [], function (file) {
        var exists = Array.prototype.some.call(dt.files, function (f) {
          return f.name === file.name && f.size === file.size && f.lastModified === file.lastModified;
        });
        if (!exists) dt.items.add(file);
      });
      syncInputFiles();
      renderFiles();
    }

    function removeFile(index) {
      var next = new DataTransfer();
      Array.prototype.forEach.call(dt.files || [], function (file, i) {
        if (i !== index) next.items.add(file);
      });
      dt = next;
      syncInputFiles();
      renderFiles();
    }

    function clearPreviewUrls() {
      previewUrls.forEach(function (url) {
        try { URL.revokeObjectURL(url); } catch (e) {}
      });
      previewUrls = [];
    }

    function renderFiles() {
      clearPreviewUrls();
      list.innerHTML = '';
      var files = Array.prototype.slice.call(input.files || []);
      list.classList.toggle('has-files', files.length > 0);
      if (!files.length) return;

      var summary = document.createElement('div');
      summary.className = 'file-preview-summary';
      summary.textContent = files.length + ' file' + (files.length > 1 ? 's' : '') + ' added. You can paste more, select files, or remove any item below.';
      list.appendChild(summary);

      var grid = document.createElement('div');
      grid.className = 'file-preview-grid';
      list.appendChild(grid);

      files.forEach(function (file, index) {
        var card = document.createElement('div');
        card.className = 'file-preview-card';

        var remove = document.createElement('button');
        remove.type = 'button';
        remove.className = 'file-preview-remove';
        remove.setAttribute('aria-label', 'Remove ' + (file.name || 'file'));
        remove.textContent = '×';
        remove.addEventListener('click', function () { removeFile(index); });
        card.appendChild(remove);

        var thumb = document.createElement('div');
        thumb.className = 'file-preview-thumb';
        if (file.type && file.type.indexOf('image/') === 0) {
          var img = document.createElement('img');
          var url = URL.createObjectURL(file);
          previewUrls.push(url);
          img.src = url;
          img.alt = file.name || 'Pasted image';
          thumb.appendChild(img);
          var badge = document.createElement('span');
          badge.className = 'file-preview-badge';
          badge.textContent = file.name && file.name.indexOf('pasted-image-') === 0 ? 'Pasted' : 'Image';
          thumb.appendChild(badge);
        } else {
          var doc = document.createElement('div');
          doc.className = 'file-preview-doc';
          doc.innerHTML = '<strong>' + fileExt(file) + '</strong><span>Attachment</span>';
          thumb.appendChild(doc);
        }
        card.appendChild(thumb);

        var meta = document.createElement('div');
        meta.className = 'file-preview-meta';
        var name = document.createElement('b');
        name.textContent = file.name || 'attachment';
        var size = document.createElement('small');
        size.textContent = formatFileSize(file);
        meta.appendChild(name);
        meta.appendChild(size);
        card.appendChild(meta);

        grid.appendChild(card);
      });
    }

    input.addEventListener('change', function () {
      // Append newly selected files to the existing attachment queue.
      // This prevents pasted/dragged files from being cleared when Select Files is used later.
      var chosen = Array.prototype.slice.call(input.files || []);
      addFiles(chosen);
    });
    drop.addEventListener('click', function () { drop.focus(); });
    
    ['dragenter','dragover'].forEach(function (ev) {
      drop.addEventListener(ev, function (e) {
        e.preventDefault();
        drop.classList.add('is-drag');
      });
    });
    ['dragleave','drop'].forEach(function (ev) {
      drop.addEventListener(ev, function () { drop.classList.remove('is-drag'); });
    });
    drop.addEventListener('drop', function (e) {
      e.preventDefault();
      addFiles(e.dataTransfer && e.dataTransfer.files);
    });
    form.addEventListener('paste', function (e) {
      var items = e.clipboardData && e.clipboardData.items;
      if (!items) return;
      var files = [];
      Array.prototype.forEach.call(items, function (item, index) {
        if (item.kind === 'file') {
          var file = item.getAsFile();
          if (file) {
            if (!file.name || file.name === 'image.png') {
              file = new File([file], 'pasted-image-' + (Date.now() + index) + '.png', { type: file.type || 'image/png', lastModified: Date.now() });
            }
            files.push(file);
          }
        }
      });
      if (files.length) addFiles(files);
    });
  });
})();
