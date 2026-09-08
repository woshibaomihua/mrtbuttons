/* Merit Trims — specification builder for a written quotation */
(function () {
  "use strict";
  var WA = "8615869483966";
  var host = document.getElementById("q-cats");
  if (!host) return;
  var DATA = null, sel = { cat: "", mat: "", qty: 5000, logo: "Custom logo" };

  function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function fmt(n){return n.toLocaleString("en-US");}
  function ph(label){label=(label||"Merit Trims").slice(0,20);
    var s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#283A52"/><stop offset="1" stop-color="#1C2A3E"/></linearGradient></defs><rect width="400" height="400" fill="url(#g)"/><circle cx="200" cy="185" r="62" fill="none" stroke="#C29A4E" stroke-width="6"/><circle cx="182" cy="167" r="6.5" fill="#E4C77E"/><circle cx="218" cy="167" r="6.5" fill="#E4C77E"/><circle cx="182" cy="203" r="6.5" fill="#E4C77E"/><circle cx="218" cy="203" r="6.5" fill="#E4C77E"/></svg>';
    return "data:image/svg+xml;charset=utf-8,"+encodeURIComponent(s);}

  function inCat(){return DATA.products.filter(function(p){return p.category===sel.cat;});}
  function pool(){return DATA.products.filter(function(p){return p.category===sel.cat && (!sel.mat||p.material===sel.mat);});}

  function catBtns(){
    var order=["buttons","zippers","cord-stoppers","cords-webbing-tapes","buckles","eyelets-hooks","labels-tags","hardware-accessories"];
    host.innerHTML=order.filter(function(c){return DATA.taxonomy[c];}).map(function(c){
      return '<button class="t-opt" data-c="'+c+'">'+esc(DATA.taxonomy[c].name)+'</button>';
    }).join("");
    host.querySelectorAll(".t-opt").forEach(function(b){b.addEventListener("click",function(){
      sel.cat=b.dataset.c;sel.mat="";
      host.querySelectorAll(".t-opt").forEach(function(x){x.classList.remove("is-on");});
      b.classList.add("is-on");matBtns();compute();
    });});
  }
  function matBtns(){
    var box=document.getElementById("q-mats"),m={};
    inCat().forEach(function(p){if(p.material)m[p.material]=(m[p.material]||0)+1;});
    var keys=Object.keys(m).sort(function(a,b){return m[b]-m[a];});
    var h='<button class="t-opt is-on" data-m="">Any material</button>';
    keys.forEach(function(k){h+='<button class="t-opt" data-m="'+esc(k)+'">'+esc(k)+'</button>';});
    box.innerHTML=h;
    box.querySelectorAll(".t-opt").forEach(function(b){b.addEventListener("click",function(){
      sel.mat=b.dataset.m;
      box.querySelectorAll(".t-opt").forEach(function(x){x.classList.remove("is-on");});
      b.classList.add("is-on");compute();
    });});
  }
  function card(p){
    var cat=(DATA.taxonomy[p.category]||{}).name||p.category;
    var t="Hi Merit Trims, I'd like a quote on: "+p.title+" (ref "+p.id+").";
    return '<div class="t-card"><div class="t-card__img"><img loading="lazy" alt="'+esc(p.title)+'" data-label="'+esc(cat)+'" src="'+esc(p.image)+'"></div>'+
      '<div class="t-card__b"><div class="t-card__cat">'+esc(cat)+'</div><div class="t-card__t">'+esc(p.title)+'</div>'+
      '<div class="t-card__m"><span>Price &amp; MOQ confirmed after specification review</span></div>'+
      '<a class="t-card__q" href="https://wa.me/'+WA+'?text='+encodeURIComponent(t)+'" target="_blank" rel="noopener">Request quote</a></div></div>';
  }
  function wireImgs(){document.querySelectorAll("#q-styles .t-card__img img:not([data-w])").forEach(function(im){im.setAttribute("data-w","1");im.addEventListener("error",function h(){im.removeEventListener("error",h);im.src=ph(im.alt);});});}

  function compute(){
    if(!sel.cat)return;
    var items=pool();
    if(!items.length)items=inCat();
    document.getElementById("q-value").textContent=fmt(sel.qty)+" pcs requested";
    // matches
    var top=items.slice().sort(function(a,b){return a.rank_score-b.rank_score;}).slice(0,4);
    document.getElementById("q-styles").innerHTML=top.map(card).join("");wireImgs();
    // spec + wa
    var catName=DATA.taxonomy[sel.cat].name;
    var spec=catName+(sel.mat?(" · "+sel.mat):"")+" · "+fmt(sel.qty)+" pcs · "+sel.logo;
    document.getElementById("q-spec").value=spec;
    var t="Hi Merit Trims, quotation request:\n"+spec+"\nPlease confirm price, MOQ, sampling and lead time after reviewing my specification.";
    document.getElementById("q-wa").href="https://wa.me/"+WA+"?text="+encodeURIComponent(t);
  }

  // qty + logo controls
  var qty=document.getElementById("q-qty"),out=document.getElementById("q-qty-out");
  qty.addEventListener("input",function(){sel.qty=+qty.value;out.textContent=fmt(sel.qty)+" pcs";compute();});
  document.querySelectorAll("#q-logo .t-opt").forEach(function(b){b.addEventListener("click",function(){
    sel.logo=b.dataset.v;document.querySelectorAll("#q-logo .t-opt").forEach(function(x){x.classList.remove("is-on");});b.classList.add("is-on");compute();
  });});

  fetch("/data/product-data.json").then(function(r){return r.json();}).then(function(d){
    DATA=d;catBtns();
    // preselect Buttons
    var first=host.querySelector('[data-c="buttons"]')||host.querySelector(".t-opt");
    if(first){first.classList.add("is-on");sel.cat=first.dataset.c;matBtns();compute();}
  }).catch(function(){host.innerHTML='<p style="color:#6A7180">Could not load product data. Serve over HTTP to use the configurator.</p>';});
})();
