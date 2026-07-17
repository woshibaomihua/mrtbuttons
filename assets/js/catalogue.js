/* Merit Trims — full catalogue browser over all 843 SKUs */
(function () {
  "use strict";
  var WA = "8615869483966";
  var grid = document.getElementById("t-grid");
  if (!grid) return;
  var DATA = null, FILTERED = [], shown = 0, PAGE = 24;
  var st = { cat: "", sub: "", mat: "", q: "", sort: "relevance" };
  var p = new URLSearchParams(location.search);
  st.cat = p.get("cat") || ""; st.sub = p.get("sub") || ""; st.q = p.get("q") || "";

  function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function ph(label){label=(label||"Merit Trims").slice(0,20);
    var s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#283A52"/><stop offset="1" stop-color="#1C2A3E"/></linearGradient></defs><rect width="400" height="400" fill="url(#g)"/><circle cx="200" cy="185" r="62" fill="none" stroke="#C29A4E" stroke-width="6"/><circle cx="182" cy="167" r="6.5" fill="#E4C77E"/><circle cx="218" cy="167" r="6.5" fill="#E4C77E"/><circle cx="182" cy="203" r="6.5" fill="#E4C77E"/><circle cx="218" cy="203" r="6.5" fill="#E4C77E"/><text x="200" y="295" fill="#9aa6bd" font-family="Inter,Arial" font-size="19" font-weight="600" text-anchor="middle">'+label+'</text></svg>';
    return "data:image/svg+xml;charset=utf-8,"+encodeURIComponent(s);}

  function waLink(pr){
    var t="Hi Merit Trims, I'd like a quote on: "+pr.title+" (ref "+pr.id+", MOQ "+(pr.moq||"")+"). Please advise price, MOQ and customization.";
    return "https://wa.me/"+WA+"?text="+encodeURIComponent(t);
  }
  function card(pr){
    var cat=(DATA.taxonomy[pr.category]||{}).name||pr.category;
    return '<div class="t-card"><div class="t-card__img">'+
      '<img loading="lazy" alt="'+esc(pr.title)+'" data-label="'+esc(cat)+'" src="'+esc(pr.image)+'"></div>'+
      '<div class="t-card__b"><div class="t-card__cat">'+esc(cat)+'</div>'+
      '<div class="t-card__t">'+esc(pr.title)+'</div>'+
      '<div class="t-card__m"><span>MOQ <b>'+esc(pr.moq||"—")+'</b></span><span><b>'+esc(pr.price_display)+'</b></span></div>'+
      '<a class="t-card__q" href="'+esc(waLink(pr))+'" target="_blank" rel="noopener">Request quote</a>'+
      '</div></div>';
  }
  function wireImgs(scope){
    (scope||document).querySelectorAll(".t-card__img img:not([data-w])").forEach(function(im){
      im.setAttribute("data-w","1");
      im.addEventListener("error",function h(){im.removeEventListener("error",h);im.src=ph(im.getAttribute("data-label")||im.alt);});
    });
  }
  function apply(){
    var q=st.q.toLowerCase();
    FILTERED=DATA.products.filter(function(pr){
      if(st.cat&&pr.category!==st.cat)return false;
      if(st.sub&&pr.subcategory!==st.sub)return false;
      if(st.mat&&pr.material!==st.mat)return false;
      if(q&&(pr.title+" "+pr.title_original).toLowerCase().indexOf(q)===-1)return false;
      return true;
    });
    if(st.sort==="price-asc")FILTERED.sort(function(a,b){return(a.price_lo||1e9)-(b.price_lo||1e9);});
    else if(st.sort==="price-desc")FILTERED.sort(function(a,b){return(b.price_lo||0)-(a.price_lo||0);});
    else FILTERED.sort(function(a,b){return a.rank_score-b.rank_score;});
    shown=0;grid.innerHTML="";render();
    document.getElementById("t-count").textContent=FILTERED.length+" styles";
  }
  function render(){
    var slice=FILTERED.slice(shown,shown+PAGE);
    grid.insertAdjacentHTML("beforeend",slice.map(card).join(""));
    wireImgs(grid);shown+=slice.length;
    document.getElementById("t-more").style.display=shown<FILTERED.length?"inline-flex":"none";
  }
  function chips(){
    var w=document.getElementById("t-chips");
    var h='<button class="t-chip'+(st.cat?"":" is-on")+'" data-c="">All categories</button>';
    Object.keys(DATA.taxonomy).forEach(function(c){
      h+='<button class="t-chip'+(st.cat===c?" is-on":"")+'" data-c="'+c+'">'+esc(DATA.taxonomy[c].name)+'</button>';
    });
    w.innerHTML=h;
    w.querySelectorAll(".t-chip").forEach(function(b){b.addEventListener("click",function(){
      st.cat=b.dataset.c;st.sub="";
      w.querySelectorAll(".t-chip").forEach(function(x){x.classList.remove("is-on");});
      b.classList.add("is-on");subFilter();apply();
    });});
  }
  function subFilter(){
    var box=document.getElementById("t-sub");
    if(!st.cat){box.innerHTML="";return;}
    var subs=DATA.taxonomy[st.cat].subs,cnt={};
    DATA.products.forEach(function(pr){if(pr.category===st.cat)cnt[pr.subcategory]=(cnt[pr.subcategory]||0)+1;});
    var h="<h4>"+esc(DATA.taxonomy[st.cat].name)+" type</h4>";
    h+='<label><input type="radio" name="t-sub" value="" '+(st.sub?"":"checked")+"> All</label>";
    Object.keys(subs).forEach(function(s){if(!cnt[s])return;
      h+='<label><input type="radio" name="t-sub" value="'+s+'" '+(st.sub===s?"checked":"")+"> "+esc(subs[s])+" ("+cnt[s]+")</label>";});
    box.innerHTML=h;
    box.querySelectorAll('input[name="t-sub"]').forEach(function(r){r.addEventListener("change",function(){st.sub=r.value;apply();});});
  }
  function matFilter(){
    var box=document.getElementById("t-mat"),m={};
    DATA.products.forEach(function(pr){if(pr.material)m[pr.material]=(m[pr.material]||0)+1;});
    var h="<h4>Material</h4>";
    h+='<label><input type="radio" name="t-mat" value="" checked> All materials</label>';
    Object.keys(m).sort().forEach(function(k){h+='<label><input type="radio" name="t-mat" value="'+esc(k)+'"> '+esc(k)+" ("+m[k]+")</label>";});
    box.innerHTML=h;
    box.querySelectorAll('input[name="t-mat"]').forEach(function(r){r.addEventListener("change",function(){st.mat=r.value;apply();});});
  }
  var se=document.getElementById("t-search");se.value=st.q;
  var tmr;se.addEventListener("input",function(){clearTimeout(tmr);tmr=setTimeout(function(){st.q=se.value;apply();},200);});
  document.getElementById("t-sort").addEventListener("change",function(){st.sort=this.value;apply();});
  document.getElementById("t-more").addEventListener("click",render);

  grid.innerHTML='<p style="color:#6A7180">Loading 843 styles…</p>';
  fetch("/data/product-data.json").then(function(r){return r.json();}).then(function(d){
    DATA=d;chips();subFilter();matFilter();apply();
  }).catch(function(){grid.innerHTML='<p style="color:#6A7180">Could not load the catalogue. Serve the site over HTTP (e.g. <code>python3 -m http.server</code>).</p>';});
})();
