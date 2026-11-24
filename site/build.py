import os, json, re
ROOT = os.path.dirname(os.path.abspath(__file__))

# Real photo overrides. Key = seed name used across the site, value = real hotlinked
# photo URL (Unsplash License, free for commercial use, no attribution required).
# Any seed NOT in this dict still falls back to the picsum.photos placeholder below,
# so the site keeps working while we replace these in batches over time.
REAL_IMAGES = {
    "wl-maldives": "https://images.unsplash.com/photo-1602002418209-55d7a55adf42?fm=jpg&q=80&fit=crop",
    "maldivesod": "https://images.unsplash.com/photo-1602002418209-55d7a55adf42?fm=jpg&q=80&fit=crop",
    "wl-mv-hero": "https://images.unsplash.com/photo-1602002418209-55d7a55adf42?fm=jpg&q=80&fit=crop",
    "puntacana": "https://images.unsplash.com/photo-1736876134143-213d77cd09a0?fm=jpg&q=80&fit=crop",
    "wl-pc-hero": "https://images.unsplash.com/photo-1736876134143-213d77cd09a0?fm=jpg&q=80&fit=crop",
    "wl-caribbean": "https://images.unsplash.com/photo-1655299417498-52f3a304c2a4?fm=jpg&q=80&fit=crop",
    "wl-amalfi": "https://images.unsplash.com/photo-1522882018154-6055815a4515?fm=jpg&q=80&fit=crop",
    "wl-ess-hero": "https://images.unsplash.com/photo-1414408718521-f6f6198e9917?fm=jpg&q=80&fit=crop",
    "wl-ess1-hero": "https://images.unsplash.com/photo-1414408718521-f6f6198e9917?fm=jpg&q=80&fit=crop",
    "wl-ess2-hero": "https://images.unsplash.com/photo-1414408718521-f6f6198e9917?fm=jpg&q=80&fit=crop",
    "wlessguide1": "https://images.unsplash.com/photo-1414408718521-f6f6198e9917?fm=jpg&q=80&fit=crop",
    "wlessguide2": "https://images.unsplash.com/photo-1414408718521-f6f6198e9917?fm=jpg&q=80&fit=crop",
    "orlandofl": "https://images.unsplash.com/photo-1609184889233-eff6dd93def4?fm=jpg&q=80&fit=crop",
    "wl-or-hero": "https://images.unsplash.com/photo-1609184889233-eff6dd93def4?fm=jpg&q=80&fit=crop",
}
REAL_IMAGES.update({
    "cr-hub": "https://images.unsplash.com/photo-1548574505-5e239809ee19?fm=jpg&q=80&fit=crop",
    "cr-review": "https://images.unsplash.com/photo-1768270181731-b4234ef5c673?fm=jpg&q=80&fit=crop",
    "cr-ships": "https://images.unsplash.com/photo-1761349319492-16ac128d7e13?fm=jpg&q=80&fit=crop",
    "cr-itin": "https://images.unsplash.com/photo-1599640842225-85d111c60e6b?fm=jpg&q=80&fit=crop",
    "wl-cr-hero": "https://images.unsplash.com/photo-1511316695145-4992006ffddb?fm=jpg&q=80&fit=crop",
    "wl-g8-hero": "https://images.unsplash.com/photo-1580541631950-7282082b53ce?fm=jpg&q=80&fit=crop",
    "wlguide8": "https://images.unsplash.com/photo-1580541631950-7282082b53ce?fm=jpg&q=80&fit=crop",
    "wl-g9-hero": "https://images.unsplash.com/photo-1583157048761-ac1dba033233?fm=jpg&q=80&fit=crop",
    "wlguide9": "https://images.unsplash.com/photo-1583157048761-ac1dba033233?fm=jpg&q=80&fit=crop",
    "wl-ess2-hero": "https://images.unsplash.com/photo-1554254648-2d58a1bc3fd5?fm=jpg&q=80&fit=crop",
    "wlessguide2": "https://images.unsplash.com/photo-1554254648-2d58a1bc3fd5?fm=jpg&q=80&fit=crop",
    "cr-beachship": "https://images.unsplash.com/photo-1645731285912-b64e36194ce5?fm=jpg&q=80&fit=crop",
    "cr-bigship": "https://images.unsplash.com/photo-1693584173813-eba96191d8cf?fm=jpg&q=80&fit=crop",
    "cr-day": "https://images.unsplash.com/photo-1558923240-2672e219374b?fm=jpg&q=80&fit=crop",
    "cr-port": "https://images.unsplash.com/photo-1589786161184-6d43d20526e2?fm=jpg&q=80&fit=crop",
    "cr-beach": "https://images.unsplash.com/photo-1618270707842-748e8faafa3c?fm=jpg&q=80&fit=crop",
    "cr-lagoon": "https://images.unsplash.com/photo-1690682085866-535cb67a4c7d?fm=jpg&q=80&fit=crop",
})
REAL_IMAGES.update({
    "wl-ai-hero": "https://images.unsplash.com/photo-1623718649591-311775a30c43?fm=jpg&q=80&fit=crop",
    "wl-g1-hero": "https://images.unsplash.com/photo-1610641818989-c2051b5e2cfd?fm=jpg&q=80&fit=crop",
    "wl-g16-hero": "https://images.unsplash.com/photo-1597524678053-5e6fef52d8a3?fm=jpg&q=80&fit=crop",
    "wl-fm-hero": "https://images.unsplash.com/photo-1695425812104-8a9963d58887?fm=jpg&q=80&fit=crop",
    "wl-g5-hero": "https://images.unsplash.com/photo-1757924382007-7b3228526d09?fm=jpg&q=80&fit=crop",
    "wl-g4-hero": "https://images.unsplash.com/photo-1582719508461-905c673771fd?fm=jpg&q=80&fit=crop",
    "wl-g17-hero": "https://images.unsplash.com/photo-1584132869994-873f9363a562?fm=jpg&q=80&fit=crop",
    "wl-hm-hero": "https://images.unsplash.com/photo-1774859524660-d26a3742d04b?fm=jpg&q=80&fit=crop",
    "wl-g6-hero": "https://images.unsplash.com/photo-1758717152007-6a2eb7299409?fm=jpg&q=80&fit=crop",
    "wl-g7-hero": "https://images.unsplash.com/photo-1580502304784-8985b7eb7260?fm=jpg&q=80&fit=crop",
    "wl-g12-hero": "https://images.unsplash.com/photo-1601581875309-fafbf2d3ed3a?fm=jpg&q=80&fit=crop",
    "wl-g2-hero": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?fm=jpg&q=80&fit=crop",
    "wl-g13-hero": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?fm=jpg&q=80&fit=crop",
    "wl-g3-hero": "https://images.unsplash.com/photo-1766848377814-a89c782e1d6c?fm=jpg&q=80&fit=crop",
    "wl-g14-hero": "https://images.unsplash.com/photo-1604523350501-4665548f9a3c?fm=jpg&q=80&fit=crop",
    "wl-g15-hero": "https://images.unsplash.com/photo-1645319639077-0834f959fafc?fm=jpg&q=80&fit=crop",
    "wl-g10-hero": "https://images.unsplash.com/photo-1617409123168-8fb039dd3b39?fm=jpg&q=80&fit=crop",
    "wl-g11-hero": "https://images.unsplash.com/photo-1605723517503-3cadb5818a0c?fm=jpg&q=80&fit=crop",
})
def img_url(seed, w, h):
    base = REAL_IMAGES.get(seed)
    if base:
        sep = "&" if "?" in base else "?"
        return base + sep + "w=" + str(w) + "&h=" + str(h) + "&crop=faces,entropy"
    return "https://picsum.photos/seed/" + seed + "/" + str(w) + "/" + str(h)

CSS = r"""
:root{--ink:#20211e;--bg:#faf8f3;--surface:#fff;--green:#2f5d50;--green-dark:#234a40;--sand:#ece4d6;--gold:#b06a2c;--muted:#6c6f69;--line:#e3ddcf;--radius:12px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,system-ui,"Noto Sans",sans-serif;color:var(--ink);background:var(--bg);line-height:1.65;font-size:17px}
h1,h2,h3{font-family:Fraunces,Georgia,"Noto Serif",serif;font-weight:400;line-height:1.18;margin:0 0 .5em}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.narrow{max-width:760px;margin:0 auto;padding:0 24px}
.btn{display:inline-block;padding:13px 22px;border-radius:40px;font-weight:500;font-size:15px;cursor:pointer;border:1px solid transparent;transition:.2s}
.btn-gold{background:var(--gold);color:#fff}.btn-gold:hover{background:#965720}
.btn-green{background:var(--green);color:#fff}.btn-green:hover{background:var(--green-dark)}
.btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.7)}.btn-ghost:hover{background:rgba(255,255,255,.15)}
.eyebrow{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:500}
header.site{position:sticky;top:0;z-index:50;background:rgba(250,248,243,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px}
.brand{font-family:Fraunces,serif;font-size:30px;color:var(--green-dark)}.brand b{font-weight:500}
.nav ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-size:15px}
.nav ul a:hover{color:var(--gold)}
.nav .cta{display:flex;align-items:center;gap:14px}
.lang{font-size:13px;color:var(--muted);border:1px solid var(--line);border-radius:30px;padding:4px 10px}
.burger{display:none;background:none;border:0;font-size:26px;cursor:pointer;color:var(--ink)}
.phero{position:relative;height:46vh;min-height:320px;overflow:hidden;color:#fff;background-size:cover;background-position:center}
.phero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,30,28,.25),rgba(20,30,28,.6))}
.phero .inner{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:flex-end;padding-bottom:34px}
.phero h1{font-size:clamp(32px,5vw,56px);color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.3)}
.crumb{font-size:13px;color:#ffe;opacity:.9;margin-bottom:10px}
.crumb a{color:#fff;opacity:.85}
.section{padding:56px 0}
.answer{font-size:clamp(19px,2.3vw,24px);font-family:Fraunces,serif;line-height:1.4;border-left:3px solid var(--gold);padding-left:18px;margin:0 0 22px;border-radius:0}
.prose p{margin:0 0 18px}.prose h2{font-size:28px;margin:36px 0 12px}.prose h3{font-size:21px;margin:26px 0 8px}
.prose ul{padding-left:20px}.prose li{margin:6px 0}
.costtable{width:100%;border-collapse:collapse;margin:14px 0 6px;font-size:15.5px}
.costtable td{border-bottom:1px solid var(--line);padding:10px 8px}
.costtable td:last-child{text-align:right;color:var(--green-dark);font-weight:500;white-space:nowrap}
.panel{background:var(--sand);border-radius:var(--radius);padding:22px 24px;margin:26px 0}
.panel h3{margin-top:0;font-size:20px}
.panel .links{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px}
.fig{margin:28px 0;border-radius:var(--radius);overflow:hidden;background:var(--sand)}
.fig img{width:100%;height:auto;aspect-ratio:16/8;object-fit:cover}
.fig figcaption{font-size:13.5px;color:var(--muted);padding:10px 14px}
.prose .facts{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:18px 22px;margin:0 0 28px}
.prose .facts h3{font-family:Inter,system-ui,sans-serif;font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--gold);margin:0 0 12px}
.prose .facts ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:12px 24px}
.prose .facts li{margin:0;font-size:16px;line-height:1.4}
.prose .facts li span{display:block;font-size:12.5px;color:var(--muted)}
.prose .tip{border-left:3px solid var(--green);background:#eef3f0;padding:14px 18px;border-radius:0 var(--radius) var(--radius) 0;margin:24px 0}
.prose .tip b{display:block;color:var(--green-dark);margin-bottom:3px}.prose .tip p{margin:0}
@media(max-width:600px){.prose .facts ul{grid-template-columns:1fr}.costtable td:last-child{white-space:normal}}
.disc{font-size:12.5px;color:var(--muted);margin-top:10px}
.faq{border-top:1px solid var(--line);margin-top:8px}
.faq details{border-bottom:1px solid var(--line);padding:14px 0}
.faq summary{font-weight:500;cursor:pointer;font-size:17px;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::before{content:"+";color:var(--gold);margin-right:10px;font-weight:600}
.faq details[open] summary::before{content:"\2013"}
.faq p{margin:10px 0 0;color:var(--ink)}
.ctaband{background:var(--green);color:#fff;border-radius:18px;padding:38px;margin:34px 0;display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.ctaband h2{color:#fff;font-size:27px;margin:0;max-width:20ch}
.related{display:flex;gap:14px;flex-wrap:wrap;margin-top:10px}
.related a{background:var(--surface);border:1px solid var(--line);border-radius:40px;padding:9px 18px;font-size:14px}
.related a:hover{border-color:var(--gold);color:var(--gold)}
.field{margin-bottom:16px}.field label{display:block;font-size:14px;margin-bottom:6px;color:var(--muted)}
.field input,.field textarea,.field select{width:100%;border:1px solid var(--line);border-radius:8px;padding:12px;font:inherit;background:#fcfbf8}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
footer.site{background:#1c2420;color:#cfd6cf;margin-top:30px}
footer.site .wrap{padding-top:54px;padding-bottom:30px}
.fcols{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:30px}
footer .brand{color:#fff}footer p{font-size:14px;color:#a9b2aa;max-width:34ch}
footer h4{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:#fff;margin:0 0 14px}
footer ul{list-style:none;padding:0;margin:0;font-size:14px;display:grid;gap:9px}footer ul a:hover{color:#fff}
.legal{border-top:1px solid rgba(255,255,255,.12);margin-top:36px;padding-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:13px;color:#8b948c}
@media(max-width:860px){.nav ul,.lang{display:none}.burger{display:block}.nav ul.open{display:flex;position:absolute;top:72px;left:0;right:0;flex-direction:column;background:var(--bg);padding:18px 24px;border-bottom:1px solid var(--line);gap:16px}.row2{grid-template-columns:1fr}.fcols{grid-template-columns:1fr 1fr}.ctaband{padding:26px}}
.hlink{font-size:15px;color:var(--ink)}.hlink:hover{color:var(--gold)}.m-only{display:none}
@media(max-width:860px){.hlink{display:none}.nav ul.open .m-only{display:list-item}.brand{font-size:24px}.nav .cta{gap:10px}.nav .cta .btn{white-space:nowrap;padding:10px 16px;font-size:14px}}
"""

# Paste the real Pinterest page URL here once the account exists (example: https://www.pinterest.com/yourname/).
# While empty, the Pinterest links stay hidden instead of pointing nowhere.
PINTEREST_URL = ""
_PIN_HDR = ('<a class="hlink" href="'+PINTEREST_URL+'" target="_blank" rel="noopener">Pinterest</a>' if PINTEREST_URL else "")
_PIN_LI = ('<li class="m-only"><a href="'+PINTEREST_URL+'" target="_blank" rel="noopener">Pinterest</a></li>' if PINTEREST_URL else "")
_FOLLOW = ('<div><h4>Follow</h4><ul><li><a href="'+PINTEREST_URL+'" target="_blank" rel="noopener">Pinterest</a></li></ul></div>' if PINTEREST_URL else "")

HEADER = """<header class="site"><div class="wrap nav">
<a class="brand" href="/"><b>Wonderlocity</b></a>
<nav><ul id="menu">
<li><a href="/destinations/">Destinations</a></li>
<li><a href="/cruises/">Cruises</a></li>
<li><a href="/family/">Family Trips</a></li>
<li><a href="/guides/">Travel Guides</a></li>
""" + _PIN_LI + """</ul></nav>
<div class="cta">""" + _PIN_HDR + """<a class="btn btn-green" href="/contact/">Contact me</a>
<button class="burger" aria-label="Open menu" id="burger">&#9776;</button></div>
</div></header>"""

FOOTER = """<footer class="site"><div class="wrap">
<div class="fcols">
<div><a class="brand" href="/">Wonderlocity</a><p>An independent travel advisory and resource based in Virginia Beach, Virginia, affiliated with the WorldVia Travel Network.</p></div>
<div><h4>Explore</h4><ul><li><a href="/destinations/">Destinations</a></li><li><a href="/cruises/">Cruises</a></li><li><a href="/family/">Family Trips</a></li><li><a href="/guides/">Travel Guides</a></li><li><a href="/essentials/">Travel Essentials</a></li><li><a href="/deals/">Deals</a></li><li><a href="/trip-types/all-inclusive/">All-inclusive</a></li></ul></div>
<div><h4>Work with me</h4><ul><li><a href="/plan/">Planning services</a></li><li><a href="/contact/">Contact me</a></li><li><a href="/about/">About Wonderlocity</a></li><li><a href="/resources/">Free resources</a></li></ul></div>
""" + _FOLLOW + """
</div>
<div class="legal"><span>&copy; 2026 Wonderlocity. All rights reserved.</span><span><a href="/disclosure/">Affiliate disclosure</a> &nbsp; <a href="/privacy/">Privacy</a> &nbsp; <a href="/terms/">Terms</a></span></div>
</div></footer>
<script>(function(){var b=document.getElementById('burger'),m=document.getElementById('menu');if(b)b.addEventListener('click',function(){m.classList.toggle('open');});})();</script>"""

JS_NONE = ""

def page(path, title, desc, canonical, body, schema):
    schema_tag = ""
    if schema:
        schema_tag = '<script type="application/ld+json">' + json.dumps(schema, separators=(',',':')) + '</script>'
    html = ("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>" + title + "</title>"
        "<meta name=\"description\" content=\"" + desc + "\">"
        "<link rel=\"canonical\" href=\"" + canonical + "\">"
        "<link rel=\"alternate\" hreflang=\"en\" href=\"" + canonical + "\">"
        "<link rel=\"alternate\" hreflang=\"x-default\" href=\"" + canonical + "\">"
        "<meta property=\"og:title\" content=\"" + title + "\"><meta property=\"og:description\" content=\"" + desc + "\">"
        "<meta property=\"og:url\" content=\"" + canonical + "\"><meta name=\"twitter:card\" content=\"summary_large_image\">"
        "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\"><link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>"
        "<link href=\"https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500&display=swap\" rel=\"stylesheet\">"
        "<style>" + CSS + "</style></head><body>"
        + HEADER + body + FOOTER + schema_tag + "</body></html>")
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    return len(html)

def crumbs(items):
    parts = []
    for i,(name,url) in enumerate(items):
        if url:
            parts.append('<a href="'+url+'">'+name+'</a>')
        else:
            parts.append(name)
    return ' / '.join(parts)

def breadcrumb_schema(items):
    el = []
    for i,(name,url) in enumerate(items):
        d = {"@type":"ListItem","position":i+1,"name":name}
        if url:
            d["item"] = "https://wonderlocity.com"+url
        el.append(d)
    return {"@type":"BreadcrumbList","itemElement" if False else "itemListElement":el}

def faq_block(faqs):
    h = '<h2>Common questions</h2><div class="faq">'
    for q,a in faqs:
        h += '<details><summary>'+q+'</summary><p>'+a+'</p></details>'
    h += '</div>'
    sch = {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    return h, sch

advisory = ('<div class="ctaband"><h2>Want this trip priced for your exact dates?</h2>'
    '<a class="btn btn-gold" href="/contact/">Start a free planning chat</a></div>')

def affiliate_panel(dest):
    return ('<div class="panel"><h3>Check live prices for '+dest+'</h3>'
        '<p>Compare hotels and tours through our partners. Same price you would pay direct, and it helps keep these guides free.</p>'
        '<div class="links"><a class="btn btn-green" href="/deals/">Search hotels</a>'
        '<a class="btn btn-green" href="/deals/">Browse tours and activities</a></div>'
        '<p class="disc">Wonderlocity earns a commission on some bookings at no extra cost to you. See our <a href="/disclosure/">affiliate disclosure</a>.</p></div>')

def cruise_panel():
    return ('<div class="panel"><h3>Get this cruise priced for your dates</h3>'
        '<p>Cruise fares change daily, and the cheapest cabin is not always the best deal once you add taxes, fees, and extras. Tell me your dates, your group, and your budget, and I will compare the sailings for you.</p>'
        '<div class="links"><a class="btn btn-green" href="/contact/">Start a free planning chat</a>'
        '<a class="btn btn-green" href="/deals/">See current deals</a></div>'
        '<p class="disc">Wonderlocity earns a commission on some bookings at no extra cost to you. See our <a href="/disclosure/">affiliate disclosure</a>.</p></div>')


def dest_page(slug, name, seed, title, desc, answer, expand, besttime, includes, costs, faqs, related):
    canonical = "https://wonderlocity.com/destinations/"+slug+"/"
    cr = [("Home","/"),("Destinations","/destinations/"),(name,None)]
    body = ('<section class="phero" style="background-image:url(\''+img_url(seed,1920,900)+'\')">'
        '<div class="wrap inner"><div class="crumb">'+crumbs(cr)+'</div><h1>'+name+'</h1></div></section>')
    body += '<section class="section"><div class="narrow">'
    body += '<p class="answer">'+answer+'</p>'
    body += '<div class="prose"><p>'+expand+'</p>'
    body += '<h2>Best time to go</h2><p>'+besttime+'</p>'
    body += '<h2>What a Wonderlocity '+name+' trip includes</h2><ul>'
    for it in includes:
        body += '<li>'+it+'</li>'
    body += '</ul>'
    body += '<h2>Typical 2026 cost breakdown</h2><table class="costtable">'
    for label,rng in costs:
        body += '<tr><td>'+label+'</td><td>'+rng+'</td></tr>'
    body += '</table></div>'
    body += affiliate_panel(name)
    fhtml, fsch = faq_block(faqs)
    body += '<div class="prose">'+fhtml+'</div>'
    body += advisory
    body += '<p class="eyebrow">Keep exploring</p><div class="related">'
    for rname,rurl in related:
        body += '<a href="'+rurl+'">'+rname+'</a>'
    body += '</div></div></section>'
    schema = {"@context":"https://schema.org","@graph":[
        breadcrumb_schema(cr),
        {"@type":"TouristDestination","name":name,"description":desc,"url":canonical},
        fsch]}
    return page("destinations/"+slug+"/index.html", title, desc, canonical, body, schema)

def simple_page(slug, title, desc, h1, hero_seed, body_inner, schema_extra=None, crumb_items=None):
    canonical = "https://wonderlocity.com/"+slug+"/"
    cr = crumb_items or [("Home","/"),(h1,None)]
    body = ('<section class="phero" style="background-image:url(\'https://picsum.photos/seed/'+hero_seed+'/1920/900\')">'
        '<div class="wrap inner"><div class="crumb">'+crumbs(cr)+'</div><h1>'+h1+'</h1></div></section>'
        '<section class="section"><div class="narrow">'+body_inner+'</div></section>')
    graph = [breadcrumb_schema(cr)]
    if schema_extra:
        graph.append(schema_extra)
    schema = {"@context":"https://schema.org","@graph":graph}
    return page(slug+"/index.html", title, desc, canonical, body, schema)

sizes = {}

sizes['punta-cana'] = dest_page("punta-cana","Punta Cana","wl-pc-hero",
 "Punta Cana Travel Guide 2026: Real Costs, Best Time, Top Resorts | Wonderlocity",
 "See what a week all-inclusive in Punta Cana really costs in 2026, the best time to go, and how to book it. Get a free itinerary draft in 24 hours.",
 "A week all-inclusive in Punta Cana runs $1,400 - $3,200 per person in 2026, covering round-trip flights from the US East Coast, a 4-star beachfront resort, all food and drinks, and airport transfers.",
 "Punta Cana is the easiest big beach win from the East Coast: nonstop flights are short, the all-inclusive value is strong, and you can go premium or budget on the same stretch of sand. The price gap comes down to season, resort tier, and how far in advance you book.",
 "Best value is late April to early June and November, when weather is still good and rates drop after peak. Avoid the late summer hurricane window if you want certainty. Christmas, New Year, and spring break are the most expensive weeks of the year.",
 ["Round-trip flights from your home airport, priced both nonstop and one-stop",
  "A 4 or 5-star all-inclusive matched to your budget and travel style",
  "Airport transfers and resort selection based on adults-only versus family",
  "One or two tours worth doing, like Saona Island, skip the rest",
  "Travel insurance options and a simple day-by-day plan"],
 [("Flights, US East Coast, round trip","$350 - $750 per person"),
  ("4-star all-inclusive, 7 nights","$900 - $1,800 per person"),
  ("5-star or adults-only upgrade","add $400 - $1,200 per person"),
  ("Transfers and one excursion","$120 - $260 per person"),
  ("All-in per person, week","$1,400 - $3,200")],
 [("Is Punta Cana all-inclusive worth it?","For most beach trips, yes. Bundling flights, hotel, food, and drinks into one all-inclusive rate is usually cheaper than paying separately, and it makes budgeting simple. The exception is travelers who plan to eat off-resort often."),
  ("When is the cheapest time to go to Punta Cana?","Late April to early June and the first half of November give the best mix of low rates and good weather. Prices spike around the December holidays, spring break, and US long weekends."),
  ("How many days do you need in Punta Cana?","Five to seven nights is the sweet spot. Shorter feels rushed after the travel day, and longer is great if you want pure rest rather than touring."),
  ("Do I need a passport for Punta Cana?","Yes. US citizens need a valid passport to enter the Dominican Republic, and it should not expire within the period your airline requires.")],
 [("Maldives","/destinations/maldives/"),("All-inclusive trips","/trip-types/all-inclusive/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/")])

sizes['maldives'] = dest_page("maldives","Maldives","wl-mv-hero",
 "Maldives Honeymoon Cost 2026: What a Week Really Costs | Wonderlocity",
 "What a 7-night Maldives honeymoon costs in 2026, where to splurge, where to save, and the best time to go. Free itinerary draft in 24 hours.",
 "A 7-night Maldives honeymoon costs $4,500 - $11,000 per couple in 2026, covering round-trip flights from the US, an overwater villa, most meals, and the seaplane or speedboat transfer.",
 "The Maldives is the honeymoon benchmark for a reason, but the price range is enormous because the resort you pick drives almost everything. The smart play is to spend on the villa and skip the extras that look good in photos but add little.",
 "The dry season, roughly December to April, has the best weather and the highest prices. May, June, September, and October are quieter and cheaper, with a higher chance of short rain. For a honeymoon on a budget, shoulder months are the value sweet spot.",
 ["Round-trip flights from the US, with the best one-stop routings",
  "An overwater or beach villa matched to your budget",
  "Seaplane or speedboat transfer, which changes both cost and arrival time",
  "Meal plan guidance, since dining adds up fast in the Maldives",
  "Honeymoon perks where the resort offers them, and travel insurance"],
 [("Flights from the US, round trip","$1,400 - $2,600 per couple"),
  ("Overwater villa, 7 nights","$2,400 - $6,500 per couple"),
  ("Transfers, seaplane or speedboat","$300 - $1,000 per couple"),
  ("Meal plan and extras","$400 - $1,400 per couple"),
  ("All-in per couple, week","$4,500 - $11,000")],
 [("How much does a Maldives honeymoon cost?","Plan on $4,500 to $11,000 per couple for a week in 2026. The resort tier and whether you fly in by seaplane are the two biggest swing factors."),
  ("What is the cheapest time to visit the Maldives?","May, June, September, and October bring lower rates and fewer crowds, with a higher chance of brief rain. December to April is the dry, peak, and priciest season."),
  ("How many nights should you stay in the Maldives?","Seven nights is ideal for a honeymoon once you account for the long travel time. Five works if you pair it with a stop in Dubai or Doha."),
  ("Is the Maldives all-inclusive or pay as you go?","Both exist. With dining expensive on remote islands, a half-board or all-inclusive meal plan often saves money versus paying per meal.")],
 [("Punta Cana","/destinations/punta-cana/"),("Honeymoon planning","/trip-types/honeymoon/"),("Plan with me","/plan/")])

sizes['orlando'] = dest_page("orlando","Orlando and Disney","wl-or-hero",
 "Orlando and Disney World Cost 2026: Family of Four Budget | Wonderlocity",
 "What a week in Orlando costs for a family of four in 2026, including Disney tickets, hotels, and where families actually save. Free itinerary draft in 24 hours.",
 "A week in Orlando for a family of four costs $3,800 - $7,500 in 2026, including round-trip flights, a near-park hotel, 4-day Disney World tickets, and a rental car.",
 "Orlando is where a clear plan saves the most money, because tickets, hotel location, and park days interact. Families overspend by buying more park days than they will use and by staying too far from the action. The fix is matching the ticket to the trip.",
 "Avoid summer heat and crowds and the December holidays for the highest prices. Late January to February, late August to September, and early December outside the holidays give lower crowds and better rates. Check the Disney crowd calendar before locking dates.",
 ["Round-trip flights and the best Orlando airport routing",
  "A near-park hotel chosen for value, not just brand",
  "Disney World tickets sized to the right number of park days",
  "A rough park-by-park day plan so you are not paying for unused days",
  "Rental car or transfer guidance and travel insurance"],
 [("Flights, family of four, round trip","$700 - $1,500"),
  ("Hotel near parks, 7 nights","$1,100 - $2,400"),
  ("Disney World 4-day tickets, four people","$1,500 - $2,600"),
  ("Car, food, and extras","$500 - $1,000"),
  ("All-in for four, week","$3,800 - $7,500")],
 [("How much does a Disney World trip cost for a family of four?","Budget $3,800 to $7,500 for a week in 2026 once flights, a near-park hotel, 4-day tickets, and a car are included. Park-day count and hotel choice move the number the most."),
  ("How many days do you need at Disney World?","Four park days suits most families with young kids. Buying more days than you will use is the most common Orlando overspend."),
  ("When is the cheapest time to go to Disney World?","Late January and February, late August into September, and early December outside the holidays bring lower crowds and rates. Summer and the December holidays are the priciest."),
  ("Is it cheaper to stay on-site or off-site at Disney?","It depends. On-site adds convenience and early park access, off-site can be cheaper for larger families. We compare both for your dates before you book.")],
 [("Punta Cana","/destinations/punta-cana/"),("Family trips","/trip-types/family/"),("Plan with me","/plan/")])

about_body = ('<p class="answer">Wonderlocity is an independent travel resource and advisory run from Virginia Beach, Virginia, built on one rule: tell you what a trip really costs before anything else.</p>'
 '<div class="prose">'
 '<p>Most travel sites hide the price until you are emotionally committed. We do the opposite. Every destination here opens with a real 2026 price range, so you can decide with your eyes open. Then you choose your own path: take the guide and book it yourself through our partner links, or hand over the dates and let us plan the whole thing.</p>'
 '<h2>How we work</h2>'
 '<p>Wonderlocity is affiliated with the WorldVia Travel Network, which gives us access to supplier rates, support, and the ability to book and manage trips on your behalf. We specialize in the trips we know best: all-inclusive beach weeks, honeymoons, cruises, family and Disney trips, Europe, and quick getaways from coastal Virginia.</p>'
 '<h2>How we make money, plainly</h2>'
 '<p>Two ways, and neither costs you extra. We earn affiliate commissions when you book hotels, tours, or insurance through our links, and we earn supplier commissions when we plan and book a trip for you through our host network. The price you pay is the same either way. That is why our guides can stay free.</p>'
 '<h2>Why faceless, for now</h2>'
 '<p>This site leads with destinations, not selfies. The focus is the planning and the numbers, not a personal brand. If that changes, you will meet the person behind Wonderlocity here first.</p>'
 '</div>'
 '<div class="ctaband"><h2>Have a trip in mind? Let us price it.</h2><a class="btn btn-gold" href="/contact/">Start a free planning chat</a></div>')

simple_page("about","About Wonderlocity | Honest Trip Costs, Real Planning","Wonderlocity is an independent travel resource and advisory in Virginia Beach, VA, affiliated with WorldVia. Honest costs first, planning when you want it.","About Wonderlocity","wl-about-hero",about_body,
 {"@type":"AboutPage","name":"About Wonderlocity"})

plan_faqs = [("Do you charge a fee to plan my trip?","Most leisure trips, like all-inclusive weeks, cruises, and Disney, have no planning fee, because we are paid a commission by the suppliers. Complex multi-country itineraries may carry a planning fee, quoted up front before any work begins."),
 ("How fast do I get an itinerary?","You get a first draft within 24 hours of our planning chat, then we refine it together until it is right."),
 ("Can you get better prices than booking myself?","Often yes. Through the WorldVia host network we can access rates and perks that are not always public, and we watch for price drops after booking."),
 ("What if I just want to book it myself?","That is welcome too. Every guide on the site links to our booking partners, so you can self-serve and still support Wonderlocity at no extra cost.")]
plan_fhtml, plan_fsch = faq_block(plan_faqs)
plan_body = ('<p class="answer">Working with me is free to start: send your dates and budget, and you get a draft itinerary within 24 hours, booked through my WorldVia host network, often at rates you will not find online.</p>'
 '<div class="prose">'
 '<h2>How planning works</h2>'
 '<p>It is four simple steps, and you can stop at any point with no obligation.</p>'
 '<ul>'
 '<li>You share your dates, budget, and the kind of trip you want, through the contact form.</li>'
 '<li>I send a draft itinerary with real price ranges within 24 hours.</li>'
 '<li>We refine it together until the plan and the budget match.</li>'
 '<li>I book and manage it, and stay on call before and during your trip.</li>'
 '</ul>'
 '<h2>What it costs</h2>'
 '<p>Most leisure trips carry no planning fee, since suppliers pay the commission. For complex, custom, multi-country trips, any planning fee is quoted and agreed before work starts, never a surprise.</p>'
 '</div>'
 + plan_fhtml +
 '<div class="ctaband"><h2>Tell me where you want to go.</h2><a class="btn btn-gold" href="/contact/">Start a free planning chat</a></div>')
simple_page("plan","Travel Planning Services | Wonderlocity","Free to start: send your dates and budget and get a draft itinerary in 24 hours, booked through our WorldVia host network. Most leisure trips have no planning fee.","Travel planning services","wl-plan-hero",plan_body,
 {"@type":"Service","serviceType":"Travel planning and advisory","provider":{"@type":"TravelAgency","name":"Wonderlocity"},"areaServed":"US"})
# attach FAQ schema to plan via extra graph is omitted for brevity; FAQ visible on page

contact_body = ('<p class="answer">Tell me where you want to go, your rough dates, and a budget, and I will send a draft itinerary within 24 hours. No fee to start, no obligation.</p>'
 '<form class="prose" action="https://formspree.io/f/your-id" method="POST">'
 '<div class="row2"><div class="field"><label>Your name</label><input name="name" required></div>'
 '<div class="field"><label>Email</label><input type="email" name="email" required></div></div>'
 '<div class="row2"><div class="field"><label>Destination or trip type</label><input name="destination" placeholder="Punta Cana, Maldives, Disney, not sure yet"></div>'
 '<div class="field"><label>Rough budget</label><input name="budget" placeholder="e.g. $5,000 for two"></div></div>'
 '<div class="row2"><div class="field"><label>Approx travel dates</label><input name="dates" placeholder="e.g. early October, 7 nights"></div>'
 '<div class="field"><label>Travelers</label><input name="travelers" placeholder="2 adults, 2 kids"></div></div>'
 '<div class="field"><label>Anything else</label><textarea name="message" rows="4" placeholder="Tell me what matters most for this trip"></textarea></div>'
 '<button class="btn btn-gold" type="submit">Send and get my draft</button>'
 '<p class="disc">This form is a placeholder. We will connect it to your email or a free form service like Formspree during setup.</p>'
 '</form>')
simple_page("contact","Contact Wonderlocity | Free Planning Chat","Send your dates and budget and get a draft itinerary within 24 hours. No fee to start, no obligation.","Contact","wl-contact-hero",contact_body,
 {"@type":"ContactPage","name":"Contact Wonderlocity"})

disclosure_body = ('<p class="answer">Wonderlocity earns money through affiliate links and travel commissions, and it never costs you more.</p>'
 '<div class="prose">'
 '<p>In plain terms required by the US Federal Trade Commission: some links on this site are affiliate links. If you click one and book, Wonderlocity may earn a commission from the hotel, tour operator, insurer, or booking platform. You pay the same price you would pay going direct.</p>'
 '<p>Wonderlocity is also an affiliated travel advisor with the WorldVia Travel Network. When we plan and book a trip for you, we are paid a commission by the travel suppliers, again at no additional cost to you.</p>'
 '<p>We only recommend destinations, resorts, and tools we believe are a genuine fit. Commissions never change the advice. Prices and price ranges shown on this site are estimates for planning and can change at any time.</p>'
 '</div>')
simple_page("disclosure","Affiliate Disclosure | Wonderlocity","How Wonderlocity earns through affiliate links and travel commissions, at no extra cost to you. Our FTC affiliate disclosure.","Affiliate disclosure","wl-disc-hero",disclosure_body)

privacy_body = ('<p class="answer">We collect only what we need to plan your trip and run this site, and we never sell your data.</p>'
 '<div class="prose"><p>This is a starting privacy policy and will be finalized before launch. Wonderlocity collects the details you submit through the contact and newsletter forms, such as your name, email, and trip preferences, to respond to you and send updates you asked for. We use basic analytics to understand which guides are useful. We do not sell your personal information. You can unsubscribe or request deletion at any time by contacting us.</p></div>')
simple_page("privacy","Privacy Policy | Wonderlocity","How Wonderlocity collects and uses your information. We never sell your data.","Privacy policy","wl-priv-hero",privacy_body)

terms_body = ('<p class="answer">Wonderlocity provides travel information and advisory services, and the prices shown are estimates for planning.</p>'
 '<div class="prose"><p>These starter terms will be finalized before launch. The content on Wonderlocity is for general planning and information. Price ranges are estimates and change frequently. Bookings are subject to the terms of the relevant supplier and, where applicable, the WorldVia Travel Network. Wonderlocity is not liable for supplier changes, cancellations, or losses outside our control. Travel insurance is strongly recommended on every trip.</p></div>')
simple_page("terms","Terms | Wonderlocity","Terms of use for Wonderlocity travel information and advisory services.","Terms","wl-terms-hero",terms_body)

# update sitemap
urls = ["/","/about/","/plan/","/contact/","/disclosure/","/privacy/","/terms/",
        "/destinations/punta-cana/","/destinations/maldives/","/destinations/orlando/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    pr = "1.0" if u=="/" else "0.8"
    sm += '  <url><loc>https://wonderlocity.com'+u+'</loc><changefreq>weekly</changefreq><priority>'+pr+'</priority></url>\n'
sm += '</urlset>\n'
with open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8") as f:
    f.write(sm)

print("Generated pages.")

# ===== Phase 1b: trip-type pages, guides, deals, section indexes =====

CARD_CSS = ('<style>.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:30px}'
 '.lcard{background:var(--surface);border:1px solid var(--line);border-radius:12px;overflow:hidden;transition:.2s}'
 '.lcard:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(31,44,40,.1)}'
 '.lcard .ph{height:180px;background-size:cover;background-position:center}'
 '.lcard .b{padding:16px 18px 20px}.lcard h3{font-size:20px;margin:.1em 0 .3em}'
 '.lcard .price{font-size:13.5px;color:var(--green-dark);font-weight:500}'
 '.lcard p{font-size:14.5px;color:var(--muted);margin:.4em 0 .8em}'
 '.lcard a.r{font-size:13.5px;color:var(--gold);font-weight:500}'
 '@media(max-width:860px){.grid3{grid-template-columns:1fr}}</style>')

def phero(seed, crumb_items, h1):
    return ('<section class="phero" style="background-image:url(\''+img_url(seed,1920,900)+'\')">'
        '<div class="wrap inner"><div class="crumb">'+crumbs(crumb_items)+'</div><h1>'+h1+'</h1></div></section>')

def render_tokens(h):
    def fig(m):
        seed,cap=m.group(1),m.group(2)
        return ('<figure class="fig"><img src="'+img_url(seed,1200,600)+'" alt="'+cap+'" loading="lazy" width="1200" height="600">'
                '<figcaption>'+cap+'</figcaption></figure>')
    def tip(m):
        return '<div class="tip"><b>'+m.group(1)+'</b><p>'+m.group(2)+'</p></div>'
    def facts(m):
        items=""
        for part in m.group(1).split(";"):
            k,v=part.split("=",1)
            items+="<li><span>"+k.strip()+"</span>"+v.strip()+"</li>"
        return '<div class="facts"><h3>Quick take</h3><ul>'+items+'</ul></div>'
    h=re.sub(r"\{\{FIG\|([^|}]+)\|([^}]+)\}\}",fig,h)
    h=re.sub(r"\{\{TIP\|([^|}]+)\|([^}]+)\}\}",tip,h)
    h=re.sub(r"\{\{FACTS\|([^}]+)\}\}",facts,h)
    return h

def rich_page(path, canonical, crumb_items, h1, seed, title, desc, answer, prose_html, faqs, extra_nodes, related, affiliate_dest):
    body = phero(seed, crumb_items, h1) + '<section class="section"><div class="narrow">'
    body += '<p class="answer">'+answer+'</p>'
    body += '<div class="prose">'+render_tokens(prose_html)+'</div>'
    if affiliate_dest:
        body += cruise_panel() if 'cruise' in affiliate_dest.lower() else affiliate_panel(affiliate_dest)
    graph = [breadcrumb_schema(crumb_items)]
    if extra_nodes:
        graph += extra_nodes
    if faqs:
        fhtml, fsch = faq_block(faqs)
        body += '<div class="prose">'+fhtml+'</div>'
        graph.append(fsch)
    body += advisory
    if related:
        body += '<p class="eyebrow">Keep exploring</p><div class="related">'
        for rn,ru in related:
            body += '<a href="'+ru+'">'+rn+'</a>'
        body += '</div>'
    body += '</div></section>'
    schema = {"@context":"https://schema.org","@graph":graph}
    return page(path, title, desc, canonical, body, schema)

def listing_page(path, canonical, crumb_items, h1, seed, title, desc, intro, cards):
    body = phero(seed, crumb_items, h1) + '<section class="section"><div class="wrap">'
    body += CARD_CSS + '<p class="sub" style="max-width:60ch;color:var(--muted)">'+intro+'</p>'
    body += '<div class="grid3">'
    for nm,url,cseed,price,blurb in cards:
        body += ('<article class="lcard"><a href="'+url+'"><div class="ph" style="background-image:url(\''+img_url(cseed,800,600)+'\')"></div></a>'
            '<div class="b"><h3>'+nm+'</h3>'+('<div class="price">'+price+'</div>' if price else '')+'<p>'+blurb+'</p>'
            '<a class="r" href="'+url+'">Read more</a></div></article>')
    body += '</div></div></section>'
    schema = {"@context":"https://schema.org","@graph":[breadcrumb_schema(crumb_items)]}
    return page(path, title, desc, canonical, body, schema)

def service_node(name):
    return {"@type":"Service","serviceType":name,"provider":{"@type":"TravelAgency","name":"Wonderlocity"},"areaServed":"US"}
def article_node(headline, desc, url):
    return {"@type":"Article","headline":headline,"description":desc,"author":{"@type":"Organization","name":"Wonderlocity"},"publisher":{"@type":"Organization","name":"Wonderlocity"},"mainEntityOfPage":url}

# ---- trip types ----
rich_page("trip-types/all-inclusive/index.html","https://wonderlocity.com/trip-types/all-inclusive/",
 [("Home","/"),("Trip types","/trip-types/"),("All-inclusive",None)],"All-inclusive vacations","wl-ai-hero",
 "All-Inclusive Vacations 2026: Costs, Best Resorts, Who They Suit | Wonderlocity",
 "What an all-inclusive week costs in 2026, who they suit, and the best-value destinations. Free itinerary draft in 24 hours.",
 "An all-inclusive week bundles flights, hotel, food, and drinks into one price, and in 2026 it runs $1,200 - $3,500 per person depending on the destination and resort tier.",
 "<p>All-inclusive is the simplest way to take a beach week without watching a tab. You pay once, then eat, drink, and relax. It suits couples who want zero decisions, families who like predictable costs, and first-time international travelers who want everything handled.</p>"
 "<h2>Who it is for</h2><p>Anyone who values a fixed budget and an easy week over flexibility. If you plan to eat off-resort most nights or move around a lot, a regular hotel may serve you better.</p>"
 "<h2>How to pick the right resort</h2><p>Match the resort to the trip, not the brand. Adults-only for a romantic week, a strong kids club and pools for families, and a quieter property for rest. The right tier is the one that covers what you will actually use.</p>"
 "<h2>Best-value destinations</h2><p>From the US East Coast, the strongest value is Punta Cana, Cancun and the Riviera Maya, and Jamaica. Short flights, deep all-inclusive markets, and steady competition keep prices reasonable.</p>",
 [("Are all-inclusive resorts cheaper than booking separately?","Usually for a beach week, yes, because the bundled rate beats paying for flights, hotel, meals, and drinks one by one. If you plan to eat out often, the math can flip."),
  ("Which all-inclusive destination is best value from the US?","Punta Cana, Cancun and the Riviera Maya, and Jamaica give the best mix of short flights and strong all-inclusive pricing."),
  ("Do all-inclusives include flights?","Not always. We price both the resort-only rate and a flight-plus-resort package so you can compare.")],
 [service_node("All-inclusive vacation planning")],
 [("Punta Cana","/destinations/punta-cana/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/"),("Plan with me","/plan/")],
 "all-inclusive resorts")

rich_page("trip-types/honeymoon/index.html","https://wonderlocity.com/trip-types/honeymoon/",
 [("Home","/"),("Trip types","/trip-types/"),("Honeymoon",None)],"Honeymoons","wl-hm-hero",
 "Honeymoon Costs 2026: Maldives to the Caribbean | Wonderlocity",
 "What a honeymoon costs in 2026 by destination, where to splurge, and where to save. Free itinerary draft in 24 hours.",
 "A 7-night honeymoon in 2026 ranges from $3,000 to $12,000 per couple, with the Maldives, Bora Bora, and Santorini at the top, and the Caribbean and Mexico offering the best value.",
 "<p>A honeymoon is the one trip worth getting right, and the budget swing is huge. The destination sets the floor, the resort sets the ceiling, and a few smart choices on timing and transfers decide where you land.</p>"
 "<h2>Where to splurge</h2><p>Spend on the room and the view. An overwater villa or a caldera-edge suite is the memory. Skip the extras that photograph well but add little.</p>"
 "<h2>Best value honeymoons</h2><p>The Caribbean and Mexico deliver a luxury feel for far less than the Indian Ocean or the South Pacific. A Riviera Maya or St Lucia honeymoon can feel five-star at a Maldives-adjacent dream for half the price.</p>"
 "<h2>Timing matters</h2><p>Shoulder season trims hundreds to thousands off the same trip. We build the plan around the cheapest good-weather window for your destination.</p>",
 [("How much should I budget for a honeymoon?","Plan $3,000 to $12,000 per couple for a week in 2026. The Maldives, Bora Bora, and Santorini sit at the top, the Caribbean and Mexico offer the best value."),
  ("When should we book a honeymoon?","Six to nine months out for peak destinations, both to lock rates and to access honeymoon perks. We watch for price drops after booking."),
  ("What is the most romantic affordable honeymoon?","St Lucia, the Riviera Maya, and Santorini in shoulder season give a luxury feel without Maldives-level prices.")],
 [service_node("Honeymoon planning")],
 [("Maldives","/destinations/maldives/"),("All-inclusive","/trip-types/all-inclusive/"),("Plan with me","/plan/")],
 "honeymoon resorts")

rich_page("trip-types/cruise/index.html","https://wonderlocity.com/trip-types/cruise/",
 [("Home","/"),("Trip types","/trip-types/"),("Cruises",None)],"Cruises","wl-cr-hero",
 "Caribbean Cruise Cost 2026: What a Week Really Costs | Wonderlocity",
 "What a 7-night Caribbean cruise costs in 2026, plus the extras first-timers miss. Free planning help in 24 hours.",
 "A 7-night Caribbean cruise in 2026 starts from about $700 per person, covering the cabin, meals, and entertainment, before flights, excursions, gratuities, and drinks.",
 "<p>A cruise is the most all-in-one trip there is, but the sticker price is only part of the story. The cabin fare is the start, and the extras decide what you really spend.</p>"
 "<h2>What is included</h2><p>Your cabin, main dining, most entertainment, and getting between ports. That alone is strong value, especially for first-timers and multi-generation groups.</p>"
 "{{TIP|About &ldquo;from&rdquo; prices|Cruise fares change by the day. A &ldquo;from&rdquo; price is a starting point for an inside cabin, and your real fare depends on the ship, the week you sail, and how early you book.}}<h2>What is extra</h2><p>Flights to the port, shore excursions, gratuities, drink packages, specialty dining, and wifi. These can add 30 to 60 percent on top of the fare, so we budget them up front.</p>"
 "<h2>Picking the right line</h2><p>Mass-market lines suit families and value seekers, premium lines suit couples who want calmer ships, and the cabin type matters more than most people expect.</p>",
 [("How much does a Caribbean cruise cost?","The cabin fare starts from about $700 per person for a week in 2026 and climbs with cabin, ship, and dates. Add flights, excursions, gratuities, and drinks, which can lift the total by 30 to 60 percent."),
  ("Are drinks and tips included on a cruise?","Usually not. Gratuities and drink packages are typically extra, though some fares bundle them. We confirm what is included before you book."),
  ("Is a cruise good for first-time travelers?","Yes. One price covers your room, meals, and entertainment, and you unpack once while visiting several places.")],
 [service_node("Cruise planning")],
 [("All cruise guides","/cruises/"),("Carnival cost review","/cruises/carnival-cruise-line-review/"),("All-inclusive","/trip-types/all-inclusive/"),("Family trips","/trip-types/family/"),("Plan with me","/plan/")],
 "cruises")

rich_page("trip-types/family/index.html","https://wonderlocity.com/trip-types/family/",
 [("Home","/"),("Trip types","/trip-types/"),("Family",None)],"Family vacations","wl-fm-hero",
 "Family Vacation Costs 2026: Beaches and Disney | Wonderlocity",
 "What a family vacation costs in 2026, from all-inclusive beaches to Disney, and where families actually save. Free itinerary draft in 24 hours.",
 "A week-long family vacation in 2026 typically costs $3,500 - $8,000 for a family of four, with all-inclusive beaches and Orlando the most popular picks.",
 "<p>Family trips live or die on logistics, and the budget hinges on a few big choices: drive or fly, all-inclusive or theme park, and how many paid days you really need.</p>"
 "<h2>All-inclusive beaches</h2><p>The lowest-stress family week. Kids clubs, pools, and food included means fewer decisions and a known total. Punta Cana, Cancun, and the Riviera Maya lead for value.</p>"
 "<h2>Orlando and Disney</h2><p>The classic, and the easiest place to overspend. Matching the ticket to the right number of park days is the single biggest saver.</p>"
 "<h2>Where families save</h2><p>Travel in shoulder weeks, stay near the action rather than on it, and skip the add-ons kids will not remember. We build the plan so you pay for what you will use.</p>",
 [("How much does a family vacation cost?","Plan $3,500 to $8,000 for a family of four for a week in 2026. All-inclusive beaches and Orlando are the most popular, and park-day count drives the Orlando total."),
  ("Is all-inclusive or Disney better for families?","All-inclusive is lower stress and easier to budget, Disney is the bucket-list experience. We can price both for your dates."),
  ("When is the cheapest time for a family trip?","Outside school holidays. Late spring, early fall, and early December bring lower crowds and rates.")],
 [service_node("Family vacation planning")],
 [("Orlando and Disney","/destinations/orlando/"),("All-inclusive","/trip-types/all-inclusive/"),("Plan with me","/plan/")],
 "family resorts")

# ---- guides ----
rich_page("guides/all-inclusive-caribbean-cost/index.html","https://wonderlocity.com/guides/all-inclusive-caribbean-cost/",
 [("Home","/"),("Travel guides","/guides/"),("All-inclusive Caribbean cost",None)],"What a week all-inclusive in the Caribbean really costs in 2026","wl-g1-hero",
 "All-Inclusive Caribbean Cost 2026: Real Prices by Destination | Wonderlocity",
 "A week all-inclusive in the Caribbean costs $1,200 to $3,500 per person in 2026. See the real breakdown by destination and what changes the price.",
 "A week all-inclusive in the Caribbean costs $1,200 - $3,500 per person in 2026, including round-trip US flights, a beachfront resort, and all food and drinks.",
 "<p>That range is wide because three things move the number: which island you fly to, the resort tier you pick, and the week you travel. Here is how it breaks down so you can plan with real figures.</p>"
 "<h2>What the price includes</h2><p>A true all-inclusive covers your room, all meals, snacks, most drinks, and resort activities. Flights and transfers are sometimes bundled and sometimes separate, which is the first thing to check.</p>"
 "<h2>Cost by destination</h2><table class='costtable'>"
 "<tr><td>Punta Cana, Dominican Republic</td><td>$1,200 - $2,800 per person</td></tr>"
 "<tr><td>Cancun and Riviera Maya, Mexico</td><td>$1,400 - $3,200 per person</td></tr>"
 "<tr><td>Montego Bay, Jamaica</td><td>$1,500 - $3,400 per person</td></tr>"
 "<tr><td>Punta Cana adults-only upgrade</td><td>add $400 - $1,200 per person</td></tr></table>"
 "<h2>What changes the price most</h2><p>Season is the biggest lever, followed by resort tier and how early you book. The same resort in early November can cost a third less than the same week at New Year.</p>"
 "<h2>Cheapest months to go</h2><p>Late April to early June and the first half of November offer the best mix of low rates and good weather. The December holidays and spring break are the priciest weeks.</p>"
 "<h2>Is all-inclusive worth it in the Caribbean?</h2><p>For a beach-focused week, almost always. The bundled rate usually beats paying separately, and you never think about money once you arrive.</p>",
 [("How much is a week all-inclusive in the Caribbean?","$1,200 to $3,500 per person in 2026, including US flights, a beachfront resort, and all food and drinks. Punta Cana is typically the lowest, Mexico and Jamaica a touch higher."),
  ("What is the cheapest Caribbean all-inclusive?","Punta Cana usually has the lowest all-inclusive pricing from the US East Coast, thanks to short flights and a deep, competitive resort market."),
  ("Which months are cheapest for the Caribbean?","Late April to early June and the first half of November, when good weather meets post-peak pricing.")],
 [article_node("What a week all-inclusive in the Caribbean really costs in 2026","Real 2026 Caribbean all-inclusive prices by destination.","https://wonderlocity.com/guides/all-inclusive-caribbean-cost/")],
 [("Punta Cana","/destinations/punta-cana/"),("All-inclusive trips","/trip-types/all-inclusive/"),("Plan with me","/plan/")],
 "Caribbean all-inclusive resorts")

rich_page("guides/best-time-to-visit-italy/index.html","https://wonderlocity.com/guides/best-time-to-visit-italy/",
 [("Home","/"),("Travel guides","/guides/"),("Best time to visit Italy",None)],"The best time to visit Italy, by region and budget","wl-g2-hero",
 "Best Time to Visit Italy 2026: By Region and Budget | Wonderlocity",
 "The best time to visit Italy is mid-April to early June and mid-September to October. See the trade-offs by season, region, and budget.",
 "The best time to visit Italy is mid-April to early June and mid-September to October, when the weather is warm, crowds thin, and prices sit below the summer peak.",
 "<p>Italy rewards shoulder-season travel more than almost anywhere in Europe. You get long, mild days, lighter crowds at the big sights, and hotel rates well under July and August. Here is how to choose your window.</p>"
 "<h2>Spring, April to June</h2><p>The sweet spot. Comfortable temperatures, blooming countryside, and manageable crowds before the summer rush. Book ahead for the late-May long weekends.</p>"
 "<h2>Summer, July and August</h2><p>Hot, busy, and most expensive, and many locals leave the cities in August. Great for the coast and lakes, harder for sightseeing in Rome and Florence.</p>"
 "<h2>Fall, September and October</h2><p>The other sweet spot. Warm seas into September, harvest season inland, and softening prices. October is ideal for cities and food regions.</p>"
 "<h2>By region</h2><p>For the Amalfi Coast and the islands, May to early October. For Rome, Florence, and Venice, spring and fall. For the Dolomites, summer hiking or winter skiing.</p>",
 [("What is the cheapest time to visit Italy?","November to March outside the holidays is cheapest, but the value-with-good-weather window is mid-April to early June and mid-September to October."),
  ("When is the best weather in Italy?","Late spring and early fall give warm, settled days without the August heat. The coast stays swimmable into September."),
  ("When should I avoid visiting Italy?","August is hottest, busiest on the coast, and quietest in the cities, since many businesses close while locals take holidays.")],
 [article_node("The best time to visit Italy, by region and budget","Season-by-season guide to the best time to visit Italy.","https://wonderlocity.com/guides/best-time-to-visit-italy/")],
 [("Honeymoon ideas","/trip-types/honeymoon/"),("Destinations","/destinations/"),("Plan with me","/plan/")],
 None)

rich_page("guides/weekend-getaways-from-virginia-beach/index.html","https://wonderlocity.com/guides/weekend-getaways-from-virginia-beach/",
 [("Home","/"),("Travel guides","/guides/"),("Weekend getaways from Virginia Beach",None)],"12 weekend getaways from Virginia Beach worth the drive","wl-g3-hero",
 "Weekend Getaways from Virginia Beach 2026: 12 Best Trips | Wonderlocity",
 "The best weekend getaways from Virginia Beach, from the Outer Banks to the Blue Ridge, all within a 1 to 4 hour drive. Distances and what to do.",
 "The best weekend getaways from Virginia Beach are the Outer Banks, Williamsburg, Richmond, Washington DC, Charlottesville, and the Blue Ridge, all within a 1 to 4 hour drive.",
 "<p>You do not need a flight for a great long weekend out of Virginia Beach. Within a four-hour drive you can hit beaches, mountains, history, and a capital city. Here are twelve worth the gas.</p>"
 "<h2>Under 2 hours</h2><p>Outer Banks, North Carolina, about 1.5 hours, for wild beaches and lighthouses. Williamsburg, under an hour, for colonial history and Busch Gardens. Norfolk and the Eastern Shore for low-key waterfront.</p>"
 "<h2>2 to 3 hours</h2><p>Richmond for food and murals, Washington DC for museums and monuments, and the Northern Neck for quiet rivers and wineries.</p>"
 "<h2>3 to 4 hours</h2><p>Charlottesville and the Monticello wine country, the Blue Ridge Parkway and Shenandoah for fall color and hikes, and the Outer Banks south to Ocracoke for a slower pace.</p>"
 "<h2>How to pick</h2><p>Beach lovers go south to the Outer Banks, history buffs go to Williamsburg and DC, and leaf peepers head west to the Blue Ridge in October.</p>",
 [("What is the closest weekend getaway to Virginia Beach?","Williamsburg is under an hour, and the Outer Banks are about 1.5 hours, making both easy one-tank trips."),
  ("Where can you go for a weekend within 3 hours of Virginia Beach?","Richmond, Washington DC, and the Northern Neck are all roughly 2 to 3 hours by car."),
  ("Best fall weekend trip from Virginia Beach?","The Blue Ridge Parkway and Shenandoah National Park, about 3 to 4 hours west, peak for color in October.")],
 [article_node("12 weekend getaways from Virginia Beach worth the drive","The best drivable weekend trips from Virginia Beach.","https://wonderlocity.com/guides/weekend-getaways-from-virginia-beach/")],
 [("Destinations","/destinations/"),("Travel guides","/guides/"),("Plan with me","/plan/")],
 None)

rich_page("guides/cancun-travel-cost/index.html","https://wonderlocity.com/guides/cancun-travel-cost/",
 [("Home","/"),("Travel guides","/guides/"),("Cancun vs Riviera Maya",None)],"Cancun vs Riviera Maya: which is better value in 2026","wl-g4-hero",
 "Cancun vs Riviera Maya 2026: Which Is Better Value | Wonderlocity",
 "Cancun and the Riviera Maya cost about $1,400 to $3,200 per person for an all-inclusive week in 2026. See which is better value for couples, families, and budget.",
 "Cancun and the Riviera Maya cost about the same for an all-inclusive week in 2026, roughly $1,400 - $3,200 per person, so the better value comes down to fit, with Cancun winning on nightlife, short transfers, and budget resorts, and the Riviera Maya winning on calmer, more upscale stays and cenotes.",
 "<p>Cancun and the Riviera Maya share one airport and the same stretch of Caribbean coast, so the headline price is nearly identical. The real question is which place matches your trip. Here is the honest comparison, with numbers up front.</p>"
 "<h2>How the two compare on price</h2><p>For a 7-night all-inclusive week with US flights, the two areas sit within a few hundred dollars of each other. Resort tier and travel week move the number far more than the choice between them.</p><table class='costtable'>"
 "<tr><td>Cancun Hotel Zone, all-inclusive week</td><td>$1,400 - $3,000 per person</td></tr>"
 "<tr><td>Riviera Maya, Playa del Carmen to Tulum</td><td>$1,500 - $3,200 per person</td></tr>"
 "<tr><td>Adults-only upgrade, either area</td><td>add $400 - $1,200 per person</td></tr>"
 "<tr><td>Family suite upgrade, either area</td><td>add $300 - $900 per person</td></tr></table>"
 "<h2>What Cancun does best</h2><p>Cancun packs resorts, restaurants, and nightlife into a compact Hotel Zone just minutes from the airport. Transfers are short and cheap, the beaches are wide and white, and the budget end of the resort market is deeper, so value seekers find more options. It suits first-timers, groups, and anyone who wants energy and convenience close at hand.</p>"
 "<h2>What the Riviera Maya does best</h2><p>The Riviera Maya spreads south from the airport along quieter coastline, from Playa del Carmen down to Tulum. Resorts tend to be newer, larger, and more design-led, the pace is calmer, and you are closer to cenotes, Mayan ruins, and the Sian Kaan reserve. It suits couples, families who want space, and travelers who care about scenery over a late-night scene. The trade-off is a longer transfer.</p>"
 "<h2>Which is better for couples</h2><p>For a romantic week, the Riviera Maya edges ahead. Adults-only resorts around Playa del Carmen and Tulum feel more secluded and upscale at a similar price. Cancun still has excellent adults-only properties, but the Hotel Zone is busier and louder, which some couples love and others do not.</p>"
 "<h2>Which is better for families</h2><p>It is close. Cancun shortens the transfer with tired kids and keeps everything nearby, while the Riviera Maya offers bigger family resorts with more pools and water parks. With young children, the quick airport run is a real advantage. With older kids who want excursions, the Riviera Maya space and day trips win.</p>"
 "<h2>Getting there and getting around</h2><p>Both use Cancun International Airport. The Cancun Hotel Zone is a 20 to 30 minute transfer, while the Riviera Maya runs about 45 minutes to Playa del Carmen and up to 90 minutes to Tulum. Neither needs a rental car for an all-inclusive week, though the Riviera Maya rewards a day trip or two to cenotes and ruins.</p>"
 "<h2>Cheapest time to go</h2><p>Prices in both areas drop in late April to early June and the first half of November, when the weather is still good and the holiday peaks have passed. The December holidays, spring break, and July are the priciest weeks in either place.</p>"
 "<h2>The verdict</h2><p>Choose Cancun for value, lively evenings, the shortest transfers, and the deepest pool of budget resorts. Choose the Riviera Maya for calmer, more stylish stays and easy access to cenotes and ruins for a little more. At the same budget, most couples lean Riviera Maya, while first-time or short-trip travelers often lean Cancun.</p>",
 [("Is Cancun or the Riviera Maya cheaper?","They are close, about $1,400 to $3,200 per person for an all-inclusive week in 2026. Cancun has slightly more budget resorts, while the Riviera Maya skews a touch higher for its newer, larger properties."),
  ("Is the Riviera Maya better than Cancun for a honeymoon?","For most couples, yes. Its adults-only resorts feel more secluded and upscale at a similar price, though Cancun has strong adults-only options too."),
  ("How far is the Riviera Maya from Cancun airport?","Playa del Carmen is about 45 minutes and Tulum can be 90 minutes, versus 20 to 30 minutes to the Cancun Hotel Zone.")],
 [article_node("Cancun vs Riviera Maya: which is better value in 2026","An honest 2026 comparison of cost, vibe, and who each area suits.","https://wonderlocity.com/guides/cancun-travel-cost/")],
 [("All-inclusive trips","/trip-types/all-inclusive/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/"),("Plan with me","/plan/")],
 "Cancun and Riviera Maya all-inclusive resorts")

rich_page("guides/punta-cana-best-resorts/index.html","https://wonderlocity.com/guides/punta-cana-best-resorts/",
 [("Home","/"),("Travel guides","/guides/"),("Punta Cana adults-only resorts",None)],"The best adults-only all-inclusive resorts in Punta Cana for 2026","wl-g5-hero",
 "Best Adults-Only All-Inclusive Resorts in Punta Cana 2026 | Wonderlocity",
 "The best adults-only all-inclusive resorts in Punta Cana by area, with real 2026 prices. An adults-only week runs $1,800 to $4,000 per person. Free itinerary draft in 24 hours.",
 "The best adults-only all-inclusive resorts in Punta Cana sit in three areas, Bavaro for lively value, Cap Cana for upscale calm, and Uvero Alto for secluded luxury, and an adults-only week runs $1,800 - $4,000 per person in 2026 including round-trip US flights, the resort, and all food and drinks.",
 "<p>Punta Cana has one of the deepest adults-only markets in the Caribbean, so the hard part is not finding a good resort, it is matching the right one to the trip you want. The honest way to choose is by area and by vibe, since that shapes your week far more than the brand on the gate. Here is how the adults-only scene breaks down, with prices up front.</p>"
 "<h2>How much an adults-only week costs</h2><p>Adults-only resorts in Punta Cana command a premium over the family all-inclusive rate, usually a few hundred dollars per person for the same week, in exchange for quieter pools, better restaurants, and a calmer feel. For a 7-night week with round-trip US flights, here is the 2026 range by area.</p><table class='costtable'>"
 "<tr><td>Bavaro, lively adults-only</td><td>$1,800 - $3,200 per person</td></tr>"
 "<tr><td>Cap Cana, upscale adults-only</td><td>$2,400 - $4,000 per person</td></tr>"
 "<tr><td>Uvero Alto, secluded luxury</td><td>$2,200 - $4,000 per person</td></tr>"
 "<tr><td>Swim-up or ocean-view suite upgrade</td><td>add $300 - $900 per person</td></tr></table>"
 "<h2>The best areas for adults-only</h2><p>Punta Cana is really a string of beaches. Bavaro is the busy heart, with the widest choice of resorts, the most restaurants and bars within reach, and the shortest transfers from the airport. Cap Cana sits to the south, a gated enclave of newer, polished resorts, a marina, and championship golf, with a calmer and more upmarket feel. Uvero Alto lies to the north, about an hour from the airport, where the resorts are large, modern, and spread along quiet sand, ideal if you want to disappear for a week.</p>"
 "<h2>Best for a romantic week or honeymoon</h2><p>For couples who want seclusion and polish, Cap Cana and Uvero Alto lead. The resorts there skew newer and more design-led, the beaches feel private, and the dining is a step up, all at a price that still beats an equivalent honeymoon in Mexico or the islands. Look for properties with swim-up suites, butler service, and a standout rooftop or beachfront restaurant if you want the splurge to feel special.</p>"
 "<h2>Best for a lively, social trip</h2><p>If you want a pool with a scene, swim-up bars, and an easy ride to more nightlife, Bavaro is the pick. The adults-only resorts here range from party-leaning to simply grown-up and quiet, so read recent reviews before you book. Bavaro also puts you closest to the airport, which means more of your week is spent on the beach and less in a transfer van.</p>"
 "<h2>Best for value</h2><p>The strongest adults-only value is in Bavaro, where the sheer number of resorts keeps prices competitive and shoulder-season deals are common. You can often book a solid 4-star adults-only week here for close to what a family resort costs, especially if you travel in late spring or early November and book a few months ahead.</p>"
 "<h2>What to look for when you book</h2><p>Match the resort to the trip, not the star rating. Confirm that adults-only covers the whole property and not just one section, check whether premium dining and top-shelf drinks are included or cost extra, and look at how far the resort sits from the airport if a long transfer would sour the start. Recent guest photos tell you more about the beach and the crowd than the brochure does.</p>"
 "<h2>Cheapest time to go</h2><p>Prices drop in late April to early June and the first half of November, when the weather is still good and the holiday peaks have passed. The December holidays, spring break, and the July to August stretch are the priciest weeks, and the late-summer hurricane window trades some weather risk for a lower rate.</p>"
 "<h2>The verdict</h2><p>Choose Bavaro for value, energy, and short transfers, Cap Cana for upscale calm and golf, and Uvero Alto for a secluded luxury week away from the crowds. For most couples the sweet spot is a newer Cap Cana or Uvero Alto resort in shoulder season, which buys a genuinely upscale week at a mid-range price.</p>",
 [("How much does an adults-only all-inclusive in Punta Cana cost?","About $1,800 to $4,000 per person for a week in 2026, including US flights, the resort, and all food and drinks. Bavaro is the value end, while Cap Cana and Uvero Alto sit higher for their newer, more upscale properties."),
  ("Which area of Punta Cana is best for adults-only?","Bavaro for value and a lively beach, Cap Cana for upscale calm and golf, and Uvero Alto for secluded luxury a bit farther from the airport."),
  ("When is the cheapest time for an adults-only Punta Cana trip?","Late April to early June and the first half of November, when good weather meets post-peak pricing. The December holidays and spring break are the most expensive weeks.")],
 [article_node("The best adults-only all-inclusive resorts in Punta Cana for 2026","The best adults-only resorts in Punta Cana by area, with real 2026 prices.","https://wonderlocity.com/guides/punta-cana-best-resorts/")],
 [("Punta Cana guide","/destinations/punta-cana/"),("Honeymoon ideas","/trip-types/honeymoon/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/")],
 "Punta Cana adults-only resorts")

rich_page("guides/maldives-vs-bora-bora/index.html","https://wonderlocity.com/guides/maldives-vs-bora-bora/",
 [("Home","/"),("Travel guides","/guides/"),("Maldives vs Bora Bora",None)],"Maldives vs Bora Bora for a honeymoon: cost and feel","wl-g6-hero",
 "Maldives vs Bora Bora Honeymoon 2026: Cost and Feel | Wonderlocity",
 "A 7-night honeymoon in the Maldives or Bora Bora costs $4,500 to $14,000 per couple in 2026. See how the two compare on price, scenery, and the trip each one suits.",
 "A 7-night honeymoon costs $4,500 - $14,000 per couple in 2026 in either the Maldives or Bora Bora, with the Maldives offering deeper resort choice and lower entry prices, and Bora Bora delivering its iconic turquoise lagoon and Mount Otemanu views in a more compact, single-island setting.",
 "<p>Both are bucket-list overwater honeymoons, and both photograph like a dream, so the real decision comes down to budget, how far you want to fly, and the kind of feel you are after. Here is the honest comparison, with the numbers up front.</p>"
 "<h2>How the two compare on price</h2><p>The Maldives spans a wider price range because it has everything from value 4-star resorts to ultra-luxury private islands, so the entry point is lower. Bora Bora has fewer resorts and pricier flights from the US, which pushes the floor higher. For a 7-night overwater honeymoon with round-trip US flights, here is the 2026 range.</p><table class='costtable'>"
 "<tr><td>Maldives, 7-night overwater honeymoon</td><td>$4,500 - $11,000 per couple</td></tr>"
 "<tr><td>Bora Bora, 7-night overwater honeymoon</td><td>$7,000 - $14,000 per couple</td></tr>"
 "<tr><td>Round-trip US flights, Maldives</td><td>$1,400 - $2,600 per couple</td></tr>"
 "<tr><td>Round-trip US flights, Bora Bora via Tahiti</td><td>$2,000 - $3,400 per couple</td></tr></table>"
 "<h2>What the Maldives does best</h2><p>The Maldives is a scattering of more than a hundred resort islands, each one its own private world, so you can match the trip to your budget without giving up the overwater villa. The water is a luminous, glassy blue, the house reefs are excellent for snorkeling straight off your deck, and the sheer choice means strong shoulder-season deals. It suits couples who want the overwater dream at the widest range of prices, and who like the idea of having an entire small island to themselves.</p>"
 "<h2>What Bora Bora does best</h2><p>Bora Bora is a single dramatic island ringed by a vivid lagoon, with the green peak of Mount Otemanu rising at its center, so the scenery has a grandeur the flat Maldives atolls do not. The overwater bungalow was effectively born here, the lagoon is calm and swimmable, and French Polynesian culture, food, and warmth give the trip a distinct character. It suits couples who want that one unmistakable view, a mountain-and-lagoon backdrop, and a more concentrated sense of place.</p>"
 "<h2>Getting there from the US</h2><p>The Maldives is a long haul east, usually one stop through the Middle East or Asia, then a seaplane or speedboat to your island, with total travel often 22 to 30 hours from the East Coast. Bora Bora is reached by flying to Tahiti, most easily from Los Angeles in about 8 hours, then a short 50-minute hop to Bora Bora, which is far simpler from the US West Coast. If you live in the West, Bora Bora is the easier journey, while the Maldives can be the same effort from either coast.</p>"
 "<h2>Which feels more romantic</h2><p>This is genuinely close and personal. The Maldives wins on seclusion and water clarity, since your villa often sits over an empty turquoise flat with no one in sight. Bora Bora wins on the postcard view, with bungalows framed against the lagoon and Mount Otemanu, and on a livelier sense of being somewhere with culture and a small town nearby. For pure barefoot privacy, lean Maldives. For drama and an iconic backdrop, lean Bora Bora.</p>"
 "<h2>Cheapest time to go</h2><p>The Maldives is cheapest and quieter from May to early November, the off-peak season, with a higher chance of short rain, while December to April is the dry, peak, and priciest stretch. Bora Bora flips this slightly: its dry season runs May to October, which is also high season for weather, so the best value windows are the shoulder weeks of April, May, and late October before and after the peak. For both, booking six to nine months ahead matters more than the exact month.</p>"
 "<h2>The verdict</h2><p>Choose the Maldives for the widest price range, the clearest water, and the most private overwater feel, especially if you are flying from the East Coast where the journey is similar either way. Choose Bora Bora for the single most recognizable honeymoon view, an easier trip from the West Coast, and a stronger sense of local culture, accepting a higher starting price. At a matched budget the Maldives usually buys a more luxurious villa, while Bora Bora buys a backdrop nothing else replicates.</p>",
 [("Is the Maldives or Bora Bora cheaper for a honeymoon?","The Maldives is usually cheaper to start, from about $4,500 per couple for a week versus roughly $7,000 for Bora Bora, mainly because it has more value resorts and cheaper flights. At the top end both reach $11,000 to $14,000 for ultra-luxury stays."),
  ("Is the Maldives or Bora Bora better for a honeymoon?","Both are world-class. The Maldives offers more seclusion, clearer water, and a wider range of prices, while Bora Bora offers the iconic lagoon and Mount Otemanu view and an easier trip from the US West Coast."),
  ("How long is the flight to the Maldives versus Bora Bora?","From the US East Coast the Maldives is often 22 to 30 hours with one stop, while Bora Bora is about 8 hours from Los Angeles to Tahiti plus a 50-minute hop, making it far quicker from the West Coast.")],
 [article_node("Maldives vs Bora Bora for a honeymoon: cost and feel","An honest 2026 comparison of cost, scenery, and the trip each one suits.","https://wonderlocity.com/guides/maldives-vs-bora-bora/")],
 [("Maldives guide","/destinations/maldives/"),("Honeymoon ideas","/trip-types/honeymoon/"),("Plan with me","/plan/")],
 "Maldives and Bora Bora honeymoon resorts")

rich_page("guides/santorini-honeymoon-cost/index.html","https://wonderlocity.com/guides/santorini-honeymoon-cost/",
 [("Home","/"),("Travel guides","/guides/"),("Santorini honeymoon cost",None)],"What a Santorini honeymoon costs in 2026","wl-g7-hero",
 "Santorini Honeymoon Cost 2026: Real Prices by Style | Wonderlocity",
 "A 7-night Santorini honeymoon costs $4,000 to $11,000 per couple in 2026. See the real breakdown by hotel style, where to stay for the view, and how to save.",
 "A 7-night Santorini honeymoon costs $4,000 - $11,000 per couple in 2026, covering round-trip US flights, a caldera-view or value hotel with breakfast, and the transfers and ferries that get you there.",
 "<p>Santorini is the rare honeymoon where the view is the whole point, and that view is exactly what moves the budget. A suite hanging over the caldera in Oia at sunset costs a different world from a lovely room a few streets back, yet both sit on the same island. Here is the honest breakdown, with the numbers up front, so you can spend where it matters and save where it does not.</p>"
 "<h2>How much a Santorini honeymoon costs</h2><p>The single biggest lever is where your hotel sits. A room hung over the caldera in Oia or Imerovigli is the postcard, and it carries a premium of hundreds of dollars a night over an equally nice room in Fira or inland. For a 7-night honeymoon with round-trip US flights, here is the 2026 range by style.</p><table class='costtable'>"
 "<tr><td>Caldera-view week, Oia or Imerovigli</td><td>$6,000 - $11,000 per couple</td></tr>"
 "<tr><td>Value week, Fira or inland Santorini</td><td>$4,000 - $6,500 per couple</td></tr>"
 "<tr><td>Round-trip US flights via Athens</td><td>$1,400 - $2,600 per couple</td></tr>"
 "<tr><td>Private cave-pool suite upgrade</td><td>add $1,000 - $3,000 per couple</td></tr></table>"
 "<h2>Where to stay for the view</h2><p>Santorini's caldera villages climb the cliff along the island's west side, and each has its own feel. Oia is the famous one, all whitewashed lanes and blue domes, with the most romantic sunset and the highest prices. Imerovigli sits a little south on the highest point of the rim, quieter and just as scenic, and it is the pick for couples who want the view without Oia's crowds. Firostefani and Fira look out on the same caldera but bring more dining and a livelier evening, and Fira is where the best value caldera rooms hide. Choose Oia or Imerovigli for the splurge, Firostefani or Fira for the balance.</p>"
 "<h2>Best time to go for a honeymoon</h2><p>The sweet spots are late April to June and September to October, when the weather is warm, the sea is swimmable, and rates and crowds sit below the July and August peak. June and September are the prettiest, with long golden evenings and full restaurant and ferry schedules. July and August are hot, busy, and most expensive, and the sunset spots in Oia get shoulder to shoulder. Winter is cheap and quiet, but many cliffside hotels close, so for a honeymoon the shoulder months win on every count.</p>"
 "<h2>Getting there and getting around</h2><p>Most US couples connect through a European hub to Athens, then take a 45-minute flight or a high-speed ferry across to Santorini. The flight saves half a day, the ferry is cheaper and scenic. On the island you do not need a car if you stay in a caldera village, since the sights, restaurants, and sunsets are walkable, though the lanes carry a lot of steps. For the beaches and wineries on the far side, a rented car or ATV for a day, or a private driver, opens things up. A pre-booked transfer from the airport or port spares you the taxi scramble on arrival.</p>"
 "<h2>What to do on a Santorini honeymoon</h2><p>The classic week is unhurried. Watch the Oia sunset at least once, then find your own quieter stretch of rim each evening. Book a half-day catamaran cruise around the caldera with a swim at the hot springs and dinner aboard, the one excursion almost every couple loves. Spend an afternoon tasting the island's distinctive volcanic wines at a cliffside winery, wander the ruins at Akrotiri, and trade an afternoon for the black-sand beaches at Perissa or the red beach in the south. Most of all, leave room to do nothing but sit on your terrace with the view you came for.</p>"
 "<h2>How to save without losing the magic</h2><p>You can keep the view and trim the cost with a few moves. Stay in Fira or Firostefani rather than Oia for a similar caldera at a lower rate, and walk the 30 minutes to Oia for sunset. Travel in the shoulder weeks of late April, May, or October. Book six to nine months ahead, since the best caldera rooms sell out first. Split the week, a few nights cliffside for the wow and a few in a value room, to stretch the budget. And swap the priciest sunset-view dinner reservation for a terrace picnic, which is often more romantic anyway.</p>"
 "<h2>The verdict</h2><p>A Santorini honeymoon is worth planning around the view, because the view is the experience. If the budget allows, spend on a caldera-edge suite in Oia or Imerovigli for at least part of the week and you will not forget it. If it does not, a value room in Fira plus a sunset stroll to Oia delivers most of the magic for thousands less. Either way, go in shoulder season, book early, and let the island set the pace.</p>",
 [("How much does a Santorini honeymoon cost?","About $4,000 to $11,000 per couple for a week in 2026, including US flights and breakfasts. A value room in Fira sits at the low end, while a caldera-view suite in Oia or Imerovigli pushes toward the top."),
  ("Where should you stay in Santorini for a honeymoon?","Oia and Imerovigli for the most romantic caldera views and sunsets, Firostefani and Fira for the same view with more dining and better value. A caldera-side room is the splurge worth making."),
  ("When is the best time for a Santorini honeymoon?","Late April to June and September to October, when warm weather and swimmable seas meet lower crowds and rates than the July and August peak.")],
 [article_node("What a Santorini honeymoon costs in 2026","Real 2026 Santorini honeymoon prices by hotel style, with where to stay and how to save.","https://wonderlocity.com/guides/santorini-honeymoon-cost/")],
 [("Honeymoon ideas","/trip-types/honeymoon/"),("Maldives vs Bora Bora","/guides/maldives-vs-bora-bora/"),("Plan with me","/plan/")],
 "Santorini honeymoon hotels")

rich_page("guides/caribbean-cruise-first-timer/index.html","https://wonderlocity.com/guides/caribbean-cruise-first-timer/",
 [("Home","/"),("Travel guides","/guides/"),("First Caribbean cruise",None)],"First Caribbean cruise: a complete 2026 cost and tips guide","wl-g8-hero",
 "First Caribbean Cruise 2026: Costs, Tips, and What to Know | Wonderlocity",
 "A first Caribbean cruise starts from about $700 per person for a 7-night sailing in 2026. See what is included, what costs extra, which line to pick, and the tips first-timers wish they knew.",
 "A first Caribbean cruise starts from about $700 per person for a 7-night sailing in 2026, covering your cabin, meals, and entertainment, before you add flights to the port, shore excursions, gratuities, and drinks that typically lift the total by 30 to 60 percent.",
 "<p>A cruise is the easiest big trip to take for the first time, since one price covers your room, your meals, and most of the entertainment, and you unpack once while the ship carries you between islands. The catch is that the fare you see advertised is only the starting point, and the extras decide what you actually spend. Here is the honest breakdown, with the numbers up front, so you board knowing what a week really costs.</p>"
 "<h2>What a first Caribbean cruise costs</h2><p>The fare depends most on your cabin type, the line, and the week you sail. An inside cabin on a mass-market ship is the value entry point, while a balcony costs more but transforms the trip with your own view and fresh air. For a 7-night Caribbean sailing in 2026, here is the range, along with the two extras almost every first-timer forgets to budget.</p><table class='costtable'>"
 "<tr><td>Inside cabin, 7-night sailing</td><td>from $700 per person</td></tr>"
 "<tr><td>Balcony cabin, 7-night sailing</td><td>from $1,100 per person</td></tr>"
 "<tr><td>Gratuities for the week</td><td>$120 - $170 per person</td></tr>"
 "<tr><td>Drink package</td><td>add $65 - $95 per person per day</td></tr></table>"
 "<h2>What is included in the fare</h2><p>Your cabin, all your main dining room and buffet meals, most daytime activities, the pools, the evening shows, and the transport between ports are built into the price. That is why a cruise feels like such strong value, especially for first-timers and families, since you can eat well and stay entertained without opening your wallet once you are aboard. Room service is often included or carries a small fee, and the kids clubs on the big family lines are free.</p>"
 "{{TIP|About &ldquo;from&rdquo; prices|Cruise fares change by the day. A &ldquo;from&rdquo; price is a starting point for an inside cabin, and your real fare depends on the ship, the line, the week you sail, and how early you book.}}<h2>What costs extra</h2><p>The line makes its money on the add-ons, so plan for them. Flights to the departure port, shore excursions at each island, daily gratuities, drink packages, specialty restaurants, wifi, spa treatments, and the casino all sit on top of the fare. Together they commonly add 30 to 60 percent to the base price, which is how a $900 fare becomes a $1,400 trip. The three that matter most are gratuities, which are close to mandatory, excursions, which you can often book independently for less, and drinks, where a package only pays off if you drink several a day.</p>"
 "<h2>Which cruise line to pick for your first time</h2><p>Match the line to your group, not the brochure. Royal Caribbean and Norwegian suit first-timers who want big, activity-packed ships with plenty for all ages, Carnival leans fun, casual, and budget-friendly, and Princess or Celebrity feel calmer and a touch more refined for couples. The ship matters as much as the line, since a newer, larger vessel carries more dining, pools, and entertainment. For a first cruise, a well-reviewed big ship on a major line is the safest way to find out if cruising is for you.</p>"
 "<h2>Eastern, Western, or Southern Caribbean</h2><p>Most first-timers sail one of three routes. The Eastern Caribbean visits beach-and-shopping ports like St Thomas and St Maarten plus the cruise line's private island, and it is the classic easy first cruise. The Western Caribbean leans toward Cozumel, Grand Cayman, and Jamaica, with more snorkeling, ruins, and adventure excursions. The Southern Caribbean, often out of San Juan, reaches further-flung islands like Aruba and Barbados with warmer, drier weather, though it usually means flying to the port. For a first sailing, an Eastern or Western route from Florida keeps flights short and the pace relaxed.</p>"
 "<h2>When to go and hurricane season</h2><p>The cheapest fares fall in the shoulder weeks of late April to early June and September to early December, outside school holidays and the winter peak. The Atlantic hurricane season runs June through November, with the highest risk from August to October. A cruise is actually a reasonable way to travel then, since ships can and do reroute around storms, and fares and crowds drop. The trade-off is a small chance of a changed itinerary, so travel insurance is worth the modest cost in those months. For the calmest seas and best weather, the December to April window is ideal, and also the priciest.</p>"
 "<h2>What first-timers wish they knew</h2><p>A few habits make the first cruise smoother. Pack a carry-on with swimwear and any medicine, since your checked bags may not reach the cabin until dinnertime. Book popular excursions and specialty dinners before you sail, because the best ones fill up. Download the ship's app to see the daily schedule, and bring a lanyard for your key card. Budget cash for port taxis and tips. Do the drink-package math, since it only saves money at four or more drinks a day. And if you are flying, arrive in the port city the night before, so a delayed flight never costs you the ship.</p>"
 "<h2>The verdict</h2><p>A Caribbean cruise is one of the best-value first big trips you can take, and the way to enjoy it is to budget the extras up front rather than be surprised by them. Pick a big, well-reviewed ship on a major line, choose an Eastern or Western route from Florida to keep flights short, sail in shoulder season if you can, and add insurance if you go during hurricane months. Do that and the week delivers several islands, all your meals, and nightly entertainment for a price that is hard to beat any other way.</p>",
 [("How much does a first Caribbean cruise cost?","From about $700 per person for a 7-night sailing in 2026, and more for balconies, newer ships, and holiday weeks. Add flights, gratuities, excursions, and drinks, which typically lift the total by 30 to 60 percent."),
  ("What is the best cruise line for first-timers?","Royal Caribbean and Norwegian for big, activity-packed ships, Carnival for a fun budget-friendly trip, and Princess or Celebrity for a calmer, more refined feel. A newer, larger ship on a major line is the safest first choice."),
  ("Is it safe to cruise the Caribbean during hurricane season?","Generally yes. Ships reroute around storms, and fares and crowds are lower from June to November. The main risk is a changed itinerary, so travel insurance is worth it in those months.")],
 [article_node("First Caribbean cruise: a complete 2026 cost and tips guide","Real 2026 costs, what is included, which line to pick, and first-timer tips for a Caribbean cruise.","https://wonderlocity.com/guides/caribbean-cruise-first-timer/")],
 [("All cruise guides","/cruises/"),("Cruise cost guide","/trip-types/cruise/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/"),("Plan with me","/plan/")],
 "Caribbean cruises")

rich_page("guides/royal-caribbean-vs-carnival/index.html","https://wonderlocity.com/guides/royal-caribbean-vs-carnival/",
 [("Home","/"),("Travel guides","/guides/"),("Royal Caribbean vs Carnival vs Norwegian",None)],"Royal Caribbean vs Carnival vs Norwegian: which to pick","wl-g9-hero",
 "Royal Caribbean vs Carnival vs Norwegian 2026: Which to Pick | Wonderlocity",
 "Royal Caribbean, Carnival, and Norwegian all run 7-night Caribbean cruises from about $700 per person in 2026. See which line fits your group, budget, and style.",
 "For a 7-night Caribbean sailing in 2026 all three lines start from roughly $700 per person, so the right pick comes down to style, with Carnival cheapest and most casual, Royal Caribbean the biggest ships and best kids programs, and Norwegian the most flexible dining and adult-friendly freestyle feel.",
 "<p>Royal Caribbean, Carnival, and Norwegian are the three lines almost every first-time and family cruiser ends up comparing, and on price they overlap far more than their reputations suggest. The same week, the same route, and the same cabin category usually land within a few hundred dollars of each other. What actually differs is the onboard experience, so the smart way to choose is by trip style, not by fare alone. Here is how the three compare, with the numbers up front.</p>"
 "<h2>How the three compare on price</h2><p>For a 7-night Caribbean sailing in 2026, Carnival is usually the cheapest entry point, Royal Caribbean sits in the middle but climbs fast on its newest ships, and Norwegian prices close to Royal Caribbean once you add its dining and drink bundles. Sale weeks shuffle the order constantly, which is why we price all three for your dates before booking.</p><table class='costtable'>"
 "<tr><td>Carnival, inside to balcony</td><td>from $700 per person</td></tr>"
 "<tr><td>Royal Caribbean, inside to balcony</td><td>from $800 per person</td></tr>"
 "<tr><td>Norwegian, inside to balcony</td><td>from $800 per person</td></tr>"
 "<tr><td>Drink package, any line</td><td>add $65 - $110 per person per day</td></tr></table>"
 "<h2>Royal Caribbean: the biggest ships and best for kids</h2><p>Royal Caribbean's calling card is scale. Its Oasis and Icon class ships are floating resorts with water parks, ice rinks, surf simulators, and whole neighborhoods to explore, and the Adventure Ocean kids program is the strongest of the three. Families with children who want to be busy from breakfast to bedtime get the most here. The trade-off is that the newest ships command the highest fares of the three lines, and the biggest ships can feel crowded at peak times.</p>"
 "<h2>Carnival: the budget-friendly fun ship</h2><p>Carnival leans casual, social, and affordable. The atmosphere is lively, the comedy clubs and deck parties are the identity, and food highlights like Guy's Burger Joint are free. Fares run lowest of the three, drink packages are cheapest, and short 3 to 5 night sailings from many US ports make it the easiest low-cost trial run. It suits budget-minded groups, younger crowds, and anyone who wants fun over polish. If you prefer a quieter, more refined ship, this is not the pick.</p>"
 "<h2>Norwegian: freestyle dining and adult flexibility</h2><p>Norwegian built its brand on freestyle cruising, which means no fixed dinner times, no assigned tables, and no formal nights unless you want them. It carries the widest range of included and specialty dining venues, solo cabins with their own lounge, and a more adult overall feel. Couples and groups who hate schedules like it best. The catch is that the headline fare often excludes things you will want, so the Free at Sea bundle math matters more here than on the other two lines.</p>"
 "<h2>Which line for families</h2><p>Royal Caribbean wins for most families, on the strength of its kids clubs, teen spaces, and the sheer volume of onboard activities. Carnival is the value alternative and its Camp Ocean program is solid, especially for younger kids on a budget. Norwegian works for families too, but its edge is flexibility rather than kid infrastructure, so it ranks third for most crews with children.</p>"
 "<h2>Which line for couples and adults</h2><p>Norwegian takes this one for most couples, with open dining, a more grown-up ship feel, and adults-only areas like Vibe Beach Club. Royal Caribbean's newest ships offer plenty for adults as well, especially the private-island days at Perfect Day at CocoCay. Carnival can absolutely work for a couples trip, just expect a livelier, more social ship than a quiet romantic one.</p>"
 "<h2>The verdict</h2><p>Pick Royal Caribbean if you want the biggest ships and the best kids programs, pick Carnival if budget and a fun, casual vibe come first, and pick Norwegian if flexible dining and an adult-friendly feel matter most. Price all three for your exact week, because sales change the order often, and the same cabin can swing by hundreds of dollars between lines. That is exactly the comparison we run for you, free, before you book.</p>",
 [("Which is cheaper, Royal Caribbean or Carnival?","Carnival is usually cheaper, with 7-night Caribbean fares starting around $700 per person in 2026 versus $800 or more on Royal Caribbean. Sales shuffle the order weekly, so compare both for your exact dates."),
  ("Which cruise line is best for families?","Royal Caribbean for most families, thanks to the strongest kids clubs and the most onboard activities. Carnival is the best value pick for families on a budget."),
  ("Is Norwegian better than Royal Caribbean?","Neither is better across the board. Norwegian wins on flexible dining and an adult-friendly feel, Royal Caribbean wins on ship scale and kids programs. The right pick depends on your group.")],
 [article_node("Royal Caribbean vs Carnival vs Norwegian: which to pick","An honest 2026 comparison of Royal Caribbean, Carnival, and Norwegian on price, families, couples, and ship style.","https://wonderlocity.com/guides/royal-caribbean-vs-carnival/")],
 [("All cruise guides","/cruises/"),("Cruise cost guide","/trip-types/cruise/"),("First Caribbean cruise guide","/guides/caribbean-cruise-first-timer/"),("Carnival cost review","/cruises/carnival-cruise-line-review/"),("Plan with me","/plan/")],
 "Caribbean cruises")

rich_page("guides/disney-or-universal-toddlers/index.html","https://wonderlocity.com/guides/disney-or-universal-toddlers/",
 [("Home","/"),("Travel guides","/guides/"),("Disney or Universal for toddlers",None)],"Disney or Universal for toddlers: which is better in 2026","wl-g10-hero",
 "Disney or Universal for Toddlers 2026: Which Is Better | Wonderlocity",
 "Disney is the better park for toddlers in 2026, and here is why. Real trip costs for a family of four, what toddlers can actually ride, and when Universal makes sense.",
 "Disney is the better choice for toddlers in 2026 because Magic Kingdom has far more rides with no height requirement, and a 4-night trip for a family of four runs $3,200 - $6,500 at Disney versus $2,900 - $6,000 at Universal.",
 "<p>Parents ask this one constantly, and with a toddler the answer is clearer than almost any other Orlando question. Both resorts are world class, but they are built for different ages. Disney, and Magic Kingdom in particular, was designed with small children at the center. Universal skews older, faster, and taller, even after its recent family additions. Here is the full picture, with the numbers and the ride reality up front.</p>"
 "<h2>Why Disney wins for toddlers</h2><p>The short version is ride access and atmosphere. Magic Kingdom alone has more than a dozen attractions with no height requirement, so a 2 or 3 year old can ride nearly everything in Fantasyland alongside you. Character meets are everywhere, parades and fireworks are built into the day, and the whole park runs at toddler pace. At Universal, most of the marquee rides carry height minimums of 40 inches or more, which locks a toddler out of the headline experiences and turns the day into a rider-swap exercise for the adults.</p>"
 "<h2>What toddlers can actually do at Disney</h2><p>At Magic Kingdom a toddler can ride Dumbo, It's a Small World, the Carrousel, Peter Pan's Flight, the Winnie the Pooh ride, the PeopleMover, the Jungle Cruise, Pirates of the Caribbean, and the Mad Tea Party, and that is not the full list. Add Fantasyland character spots, the castle shows, and the afternoon parade, and you can fill two full days without hitting a single height check. Animal Kingdom is the strong second park for this age, with the safari, the Nemo show, and the Boneyard playground.</p>"
 "<h2>What Universal offers toddlers</h2><p>Universal is not empty for small kids, it is just thinner. Seuss Landing at Islands of Adventure is a legitimately great toddler zone, DreamWorks Land at Universal Studios added a Shrek-themed play area and a small coaster in 2024, and Epic Universe, which opened in 2025, has some family-friendly corners. The catch is that these pockets are surrounded by parks whose identity is thrill rides, so a toddler family pays full price to use a fraction of the lineup.</p>"
 "<h2>What each trip costs in 2026</h2><p>For a family of four with a toddler, on a 4-night trip with park tickets, a mid-tier on-site or near-park hotel, and food, expect these ranges.</p><table class='costtable'>"
 "<tr><td>Disney World, 4 nights, family of four</td><td>$3,200 - $6,500</td></tr>"
 "<tr><td>Universal Orlando, 4 nights, family of four</td><td>$2,900 - $6,000</td></tr>"
 "<tr><td>Ticket savings with a child under 3</td><td>$400 - $700</td></tr>"
 "<tr><td>Stroller rental for the week</td><td>$60 - $130</td></tr></table>"
 "<h2>The under-3 advantage</h2><p>Both resorts let children under 3 into the parks free, and at buffets and family-style meals they eat free from your plate. That makes ages 2 and under the cheapest window your family will ever have for an Orlando trip, and it is a real argument for going now rather than waiting. Once your child turns 3, tickets alone add several hundred dollars to the trip.</p>"
 "<h2>When Universal makes sense instead</h2><p>Pick Universal if your toddler has older siblings in the 8-plus range who want coasters and Harry Potter, because rider swap lets the adults trade off while the big kids ride. It also makes sense if you have visited Disney recently and want variety, or if a Universal hotel deal brings the price well under the Disney equivalent. For a family whose youngest sets the pace, though, Disney simply fills more hours.</p>"
 "<h2>Tips for a toddler park day</h2><p>Book the park for the morning, not the whole day. Toddlers peak early, so arrive at opening, ride the low-wait headliners first, and plan to be back at the pool by early afternoon. Bring your own stroller or rent one for the trip rather than daily, use the baby care centers, which both resorts run and Disney does especially well, and do not buy more park days than your child can use. Three park days on a 4-night trip is plenty at this age.</p>",
 [("Is Disney or Universal better for a 2 year old?","Disney, and it is not close at this age. Magic Kingdom has more than a dozen rides with no height requirement, while most of Universal's headline rides require 40 inches or more."),
  ("Do toddlers need tickets at Disney or Universal?","No. Both Disney World and Universal Orlando admit children under 3 free, and under-3s eat free from an adult's plate at buffets and family-style meals."),
  ("How many park days do you need with a toddler?","Three park days on a 4-night trip is the sweet spot. Toddlers do best with morning park time and afternoon breaks, so more days at a slower pace beats cramming.")],
 [article_node("Disney or Universal for toddlers: which is better in 2026","Why Disney beats Universal for toddlers in 2026, with real family-of-four costs and the rides toddlers can actually go on.","https://wonderlocity.com/guides/disney-or-universal-toddlers/")],
 [("Orlando and Disney","/destinations/orlando/"),("Family trips","/trip-types/family/"),("Plan with me","/plan/")],
 "Orlando family trips")

rich_page("guides/orlando-on-a-budget/index.html","https://wonderlocity.com/guides/orlando-on-a-budget/",
 [("Home","/"),("Travel guides","/guides/"),("Orlando on a budget",None)],"How to do Orlando on a budget in 2026","wl-g11-hero",
 "Orlando on a Budget 2026: Real Costs and Where Families Save | Wonderlocity",
 "A budget Orlando trip costs $2,400 to $4,000 for a family of four in 2026. See where the money goes and the savings that actually move the number.",
 "A budget Orlando trip for a family of four costs $2,400 - $4,000 for 5 nights in 2026, covering park tickets, an off-site hotel or condo, food, and a rental car, which is roughly half the cost of the same week done the default on-site way.",
 "<p>Orlando has a reputation as a budget-killer, and it earns it if you book the default package: on-site deluxe hotel, maximum park days, and every meal inside the gates. But the parks themselves are only part of the bill, and almost everything around them is negotiable. Families that make four or five deliberate choices routinely do the same trip for half the price. Here is where the money actually goes, and the savings that are worth the effort.</p>"
 "<h2>What a budget Orlando trip costs in 2026</h2><p>For a family of four on a 5-night trip with three park days, a well-reviewed off-site hotel or vacation condo, groceries plus a few restaurant meals, and a rental car, these are realistic 2026 ranges.</p><table class='costtable'>"
 "<tr><td>Off-site hotel or condo, 5 nights</td><td>$450 - $950</td></tr>"
 "<tr><td>3-day base park tickets, family of four</td><td>$1,200 - $1,700</td></tr>"
 "<tr><td>Food, groceries plus some meals out</td><td>$400 - $700</td></tr>"
 "<tr><td>Rental car, gas, and parking</td><td>$300 - $550</td></tr></table>"
 "<p>Flights sit on top of that and vary hugely by city, which is why driving families and travelers within a cheap-flight radius of MCO have a built-in head start.</p>"
 "<h2>Tickets: the biggest line, and the hardest to discount</h2><p>Park tickets are the one Orlando cost with almost no true discounts, so the savings come from buying smart rather than hunting coupons. Buy multi-day base tickets, since the per-day price drops sharply after day two. Skip park hopper unless you know you will use it, because it adds roughly a hundred dollars per person for flexibility most families never touch. Skip the paid line-skipping add-ons on a budget trip and use early mornings instead. And only buy from official sources or major authorized resellers, never from resale sites, since Orlando ticket fraud is rampant.</p>"
 "<h2>Fewer park days beats cheaper everything else</h2><p>The single biggest saver in Orlando is buying three park days instead of five. A day at Disney or Universal for a family of four costs $400 to $600 in tickets alone before food and parking, while a pool day, a springs day, or a free-activity day costs almost nothing. Alternating park days with rest days also happens to be how young kids enjoy the trip most, so the cheapest structure and the most pleasant one are the same structure.</p>"
 "<h2>Where to stay for less</h2><p>Off-site is where the budget math swings hardest. The area around Disney, especially Kissimmee and Lake Buena Vista, is saturated with well-reviewed hotels for $90 to $150 a night and vacation condos and townhomes that sleep six for similar money. A condo with a kitchen also unlocks the food savings below. If you want on-site perks, Disney's value resorts and Universal's endless-summer tier are the compromise, usually $150 - $250 a night, and worth it mainly when a family wants early park entry more than space.</p>"
 "<h2>Eat well without park prices</h2><p>Food is the sneaky budget-wrecker, since in-park meals run $15 to $25 per person even for counter service. The fix is structural, not willpower. Eat breakfast at the condo, carry snacks and refillable water bottles into the parks, which both Disney and Universal explicitly allow, plan one counter-service meal inside the park, and do dinners at grocery-stocked home base or the endless mid-priced restaurants on US 192 and International Drive. A family that grocery-shops on arrival day typically cuts the food bill nearly in half.</p>"
 "<h2>When to go for the lowest prices</h2><p>Crowd calendars and price calendars track each other closely. The cheapest good windows in 2026 are mid-January through early February, the weeks after spring break through late May, late August through September, and the first two weeks of December. Those windows bring lower ticket prices on date-based pricing, hotel rates 20 to 40 percent under peak, and shorter lines, which makes three park days feel like five. Avoid Christmas week, spring break, and summer holiday weeks if the budget matters.</p>"
 "<h2>Free and cheap things beyond the parks</h2><p>Orlando has a deep bench of low-cost days that keep the trip fun between park days. Disney Springs and Universal CityWalk are free to walk, with fountains, entertainment, and people-watching. Hotel and condo pools soak up an afternoon. Lakefront parks, gator-spotting airboat rides, and the Kennedy Space Center within day-trip range round it out, and a springs day at somewhere like Wekiwa costs a few dollars per car. None of these need tickets bought months ahead, so they flex around your family's energy.</p>"
 "<h2>The verdict</h2><p>Orlando on a budget is not about deprivation, it is about refusing the defaults. Go in a value week, buy three base-ticket days instead of five, sleep off-site in a condo with a kitchen, grocery-shop on day one, and fill the gaps with pools and free evenings. Do those five things and a family of four lands in the $2,400 - $4,000 range for a trip that feels every bit as full as the version costing twice as much. We price the whole thing for your dates free, including the ticket configuration, before you book anything.</p>",
 [("How much does a budget Orlando trip cost for a family of four?","About $2,400 to $4,000 for 5 nights in 2026 with three park days, an off-site hotel or condo, groceries plus some meals out, and a rental car, before flights."),
  ("What is the cheapest time to visit Orlando?","Mid-January to early February, late April through May, late August through September, and early December. Those weeks combine the lowest date-based ticket prices with hotel rates 20 to 40 percent under peak."),
  ("How can I save money on Disney and Universal tickets?","Buy multi-day base tickets from official sources, skip park hopper and paid line-skipping, and use date-based pricing by traveling in value weeks. The per-day price drops sharply after day two, and children under 3 are free.")],
 [article_node("How to do Orlando on a budget in 2026","Real 2026 budget Orlando costs for a family of four, with the five choices that cut the trip price in half.","https://wonderlocity.com/guides/orlando-on-a-budget/")],
 [("Orlando and Disney","/destinations/orlando/"),("Family trips","/trip-types/family/"),("Disney or Universal for toddlers","/guides/disney-or-universal-toddlers/")],
 "Orlando family trips")

rich_page("guides/best-time-to-visit-greece/index.html","https://wonderlocity.com/guides/best-time-to-visit-greece/",
 [("Home","/"),("Travel guides","/guides/"),("Best time to visit Greece",None)],"The best time to visit Greece by island and budget","wl-g12-hero",
 "Best Time to Visit Greece 2026: By Island and Budget | Wonderlocity",
 "The best time to visit Greece is mid-May to mid-June and September to early October. See the best window by island and budget, with real 2026 prices.",
 "The best time to visit Greece is mid-May to mid-June and September to early October, when the sea is warm, the islands are fully open but not packed, and good hotels run $90 - $180 a night instead of the $200 - $400 they charge in peak summer.",
 "<p>Greece is really two destinations wearing one name: the whitewashed islands everyone pictures, and the mainland of Athens, Delphi, and the Peloponnese. They peak at different times, and the price gap between a June week and an August week on the same island is bigger than almost anywhere in Europe. Here is how to pick your window by season, by island, and by budget.</p>"
 "<h2>Late spring, mid-May to mid-June</h2><p>The first sweet spot. The sea has warmed enough to swim, every ferry route and taverna is open, wildflowers are still on the hillsides, and the crowds that swamp Santorini and Mykonos in July have not arrived. Hotel rates sit 30 to 50 percent under peak, and you can still book a caldera-view room weeks out rather than months. If you only get one recommendation, this is it.</p>"
 "<h2>Peak summer, July and August</h2><p>Hot, windy in the Cyclades thanks to the meltemi, and as expensive as Greece gets. The famous islands are shoulder to shoulder, sunset spots in Oia require staking out a place an hour ahead, and the same room that cost $150 in May lists for $350. That said, peak has its case: the longest days, the warmest sea, every beach club and boat trip running, and the best nightlife on Mykonos and Ios. If you go, book four to six months ahead and lean toward quieter islands.</p>"
 "<h2>September and early October</h2><p>The other sweet spot, and the better one for swimmers. The Aegean holds its summer heat, so the sea in late September is warmer than in June, while the August crowds vanish almost overnight after the first week of September. Prices drop back to shoulder rates, the light turns golden, and restaurant owners have time to talk again. By mid-October, island hotels start closing for the season, so aim for the front half of the window.</p>"
 "<h2>Winter and early spring, November to April</h2><p>The cheapest time by far, and the wrong time for an island trip. Most island hotels and restaurants close, ferry schedules thin to a trickle, and the sea is cold. But it is a genuinely good window for the mainland: Athens sightseeing without lines, Delphi and Meteora in crisp quiet air, and city hotel rates at $60 - $120 a night. If your Greece trip is museums and ruins rather than beaches, February to April is an underrated bargain.</p>"
 "<h2>The best time by island</h2><p>Santorini is best in May, early June, and late September, when the caldera views come without the cruise-ship crush. Mykonos wants June through early September if nightlife is the point, and shoulder weeks if it is not. Crete has the longest season, swimmable from May into late October, and its size absorbs crowds better than the small Cyclades. Rhodes and the Dodecanese run warm and busy all summer and stay pleasant into October. Corfu and the Ionians are greener, milder, and best May through September. Naxos, Paros, and Milos follow the Santorini calendar at half the price.</p>"
 "<h2>The best time by budget</h2><p>For a 7-night trip for two, covering mid-range hotels, ferries or short flights, food, and sightseeing, these are realistic 2026 ranges by season.</p><table class='costtable'>"
 "<tr><td>Peak, July and August</td><td>$3,500 - $6,500 per couple</td></tr>"
 "<tr><td>Shoulder, mid-May to mid-June and September</td><td>$2,200 - $4,000 per couple</td></tr>"
 "<tr><td>Off-season mainland trip, November to April</td><td>$1,400 - $2,500 per couple</td></tr></table>"
 "<p>Flights from the US follow the same curve. A New York to Athens round trip that costs $1,100 in late July routinely drops to $650 - $850 in shoulder months and under $600 in winter.</p>"
 "<h2>When to book</h2><p>For peak summer on Santorini or Mykonos, book flights and hotels four to six months out, since the best-located rooms sell first and never discount. For shoulder season, two to three months is usually enough, and last-minute deals appear in May and late September. We watch fares and rates for your dates free and tell you when to pull the trigger.</p>",
 [("What is the cheapest time to visit Greece?","November to April is cheapest, with mainland trips running $1,400 - $2,500 per couple for a week, but most island hotels close. The best value with the islands open is mid-May to mid-June and September, at $2,200 - $4,000 per couple."),
  ("When is the sea warm enough to swim in Greece?","From roughly mid-May through late October. September is the warmest-water month because the Aegean holds its summer heat, which is why it beats June for swimmers."),
  ("When should I avoid Santorini and Mykonos?","Late July and August, when cruise crowds, the meltemi wind, and peak prices all hit at once. The same trip in early June or late September costs 30 to 50 percent less and feels far calmer.")],
 [article_node("The best time to visit Greece by island and budget","Month-by-month and island-by-island guide to the best time to visit Greece, with real 2026 costs by season.","https://wonderlocity.com/guides/best-time-to-visit-greece/")],
 [("Santorini honeymoon cost","/guides/santorini-honeymoon-cost/"),("Best time to visit Italy","/guides/best-time-to-visit-italy/"),("Honeymoon ideas","/trip-types/honeymoon/")],
 None)

rich_page("guides/italy-10-day-itinerary/index.html","https://wonderlocity.com/guides/italy-10-day-itinerary/",
 [("Home","/"),("Travel guides","/guides/"),("10-day Italy itinerary",None)],"A 10-day Italy itinerary for first-timers, with costs","wl-g13-hero",
 "10-Day Italy Itinerary for First-Timers 2026: Route and Real Costs | Wonderlocity",
 "The classic 10-day Italy itinerary for first-timers: Rome, Florence, and Venice by train, with a day-by-day plan and real 2026 costs of $4,000 - $7,500 per couple.",
 "The best 10-day Italy itinerary for first-timers is 4 nights in Rome, 3 in Florence, and 3 in Venice, connected by fast trains, and it costs $4,000 - $7,500 per couple in 2026 including round-trip US flights, mid-range hotels, trains, food, and the big sights.",
 "<p>Ten days is the sweet spot for a first Italy trip. It is long enough to do the three headline cities properly without the trip turning into a checklist sprint, and the fast trains between them mean you never lose a day to travel. Here is the route, the day-by-day plan, and what it actually costs.</p>"
 "<h2>The route at a glance</h2><p>Fly into Rome, out of Venice, and move north in one direction: Rome for 4 nights, Florence for 3, Venice for 3. Open-jaw flights cost about the same as a round trip to one city and save you a half-day backtrack at the end. The Rome to Florence train takes about 90 minutes and Florence to Venice just over 2 hours, so every transfer is a morning, not a lost day.</p>"
 "<h2>Days 1 to 4, Rome</h2><p>Give Rome your longest stay because it has the most ground to cover and you will land jet-lagged. Day 1 is arrival, a walk through the centro storico, and an early night. Day 2 is the ancient core: Colosseum, Forum, and Palatine Hill on one timed ticket booked weeks ahead. Day 3 is the Vatican, with an early-entry museum slot to beat the crush at the Sistine Chapel, then St. Peter's. Day 4 is the joy of Rome without a schedule: Trastevere, the Pantheon, the fountains, and the best carbonara of your life.</p>"
 "<h2>Days 5 to 7, Florence and Tuscany</h2><p>Take a morning train on day 5 and be at your Florence hotel by lunch. That afternoon is the Duomo complex and a climb of either the dome or the bell tower. Day 6 is art day: the Uffizi in the morning and the Accademia for David in the late afternoon, both on timed reservations. Day 7 is a Tuscany day trip, either a small-group Chianti wine tour or the bus to Siena, which many first-timers end up calling their favorite day of the trip.</p>"
 "<h2>Days 8 to 10, Venice</h2><p>Arrive day 8 by late morning and spend the afternoon getting purposely lost, since being lost in Venice is the attraction. Day 9 is St. Mark's Basilica and the Doge's Palace early, then the quiet Dorsoduro and Cannaregio neighborhoods once the day-trippers flood in. Day 10 is a morning vaporetto ride down the Grand Canal or a quick hop to Murano and Burano before an evening flight home, or a last spritz if you fly the next morning.</p>"
 "<h2>What it costs in 2026</h2><p>These ranges cover two people for the full 10 days in shoulder season, with the low end for careful mid-range travel and the high end for four-star comfort in peak months.</p><table class='costtable'>"
 "<tr><td>Round-trip US flights, open-jaw</td><td>$1,300 - $2,400 per couple</td></tr>"
 "<tr><td>Hotels, 10 nights mid-range</td><td>$1,500 - $3,000 per couple</td></tr>"
 "<tr><td>Trains between cities</td><td>$100 - $200 per couple</td></tr>"
 "<tr><td>Food, sights, and local transit</td><td>$1,100 - $1,900 per couple</td></tr></table>"
 "<p>Add roughly 20 to 30 percent for June through August travel, and subtract about 15 percent for November through March city trips.</p>"
 "<h2>Getting between cities</h2><p>The Frecciarossa and Italo high-speed trains are the whole reason this route works. Book 2 to 4 weeks ahead on either operator's site and a Rome to Florence seat costs $25 - $50 per person instead of the $80 walk-up fare. There is no security line, stations are in the city centers, and luggage just goes on the rack, so a transfer door to door is usually under three hours.</p>"
 "<h2>When to go and when to book</h2><p>April, May, September, and October are the sweet spots, with warm weather and prices below the summer peak. Book flights 3 to 5 months out, hotels 2 to 4 months out, and the timed tickets for the Colosseum, Vatican, and Uffizi as soon as your dates are fixed, since the best entry slots sell out weeks ahead in high season. We watch fares and entry-slot releases for your dates free and tell you when to book.</p>",
 [("Is 10 days enough for Italy?","Yes, for a first trip. Ten days covers Rome, Florence, and Venice properly with a Tuscany day trip included. Trying to add the Amalfi Coast or Cinque Terre in the same 10 days usually means enjoying all of it less."),
  ("How much does 10 days in Italy cost for two people?","$4,000 - $7,500 per couple in 2026, including round-trip US flights, mid-range hotels, trains, food, and major sights. Summer peak adds 20 to 30 percent, and winter city trips run about 15 percent less."),
  ("Do I need to rent a car in Italy?","Not for this itinerary. High-speed trains connect Rome, Florence, and Venice faster than driving, and cars are a liability in all three cities. Rent one only if you add a countryside stay in Tuscany.")],
 [article_node("A 10-day Italy itinerary for first-timers, with costs","Day-by-day 10-day Italy itinerary covering Rome, Florence, and Venice, with real 2026 costs.","https://wonderlocity.com/guides/italy-10-day-itinerary/")],
 [("Best time to visit Italy","/guides/best-time-to-visit-italy/"),("Best time to visit Greece","/guides/best-time-to-visit-greece/"),("Plan with me","/plan/")],
 "Italy hotels and tours")

rich_page("guides/outer-banks-weekend/index.html","https://wonderlocity.com/guides/outer-banks-weekend/",
 [("Home","/"),("Travel guides","/guides/"),("Outer Banks weekend",None)],"An Outer Banks weekend from Virginia Beach: costs and plan","wl-g14-hero",
 "Outer Banks Weekend from Virginia Beach 2026: Costs and a 2-Day Plan | Wonderlocity",
 "An Outer Banks weekend from Virginia Beach costs $350 - $900 for two in 2026. The 90-minute route, where to base yourself, and a two-day plan that works.",
 "An Outer Banks weekend from Virginia Beach costs $350 - $900 for two people in 2026, covering two nights in a hotel or small rental, gas for the roughly 90-minute drive, meals out, and a couple of paid attractions.",
 "<p>The Outer Banks is the easiest great weekend you can take from Virginia Beach. It is close enough to leave after breakfast on Saturday and still have a full beach day, far enough to feel like a real trip, and cheap enough outside peak summer that a spontaneous weekend does not need a budget meeting. Here is the route, the costs, and a two-day plan that fits it all in without rushing.</p>"
 "<h2>Getting there from Virginia Beach</h2><p>The drive is about 90 minutes to Kitty Hawk on the most direct route, south on US-168 through Chesapeake, across the state line, then NC-158 to the Wright Memorial Bridge. It is a two-lane highway for long stretches, so summer Saturday traffic can push it past two hours. Leave before 8 am on summer weekends and you will roll onto the beach road while everyone else is still queued at the bridge. Off season, the drive is genuinely easy at any hour.</p>"
 "<h2>Where to base yourself</h2><p>For a two-night trip, stay in the central towns: Kitty Hawk, Kill Devil Hills, or Nags Head. They put you within ten minutes of the Wright Brothers Memorial, Jockey's Ridge, the fishing piers, and the widest choice of restaurants, and they have the deepest supply of hotels and small rentals. Duck and Corolla to the north are prettier and quieter but add 30 to 45 minutes each way and skew toward week-long house rentals. Hatteras and points south are wilder and wonderful, but they are better saved for a three-night trip, since the extra hour of driving eats a weekend.</p>"
 "<h2>What a weekend costs in 2026</h2><p>These ranges cover two people for two nights, with the low end for an off-season hotel weekend and the high end for a summer weekend in a nicer oceanfront room.</p><table class='costtable'>"
 "<tr><td>Hotel or small rental, 2 nights</td><td>$180 - $550</td></tr>"
 "<tr><td>Gas from Virginia Beach, round trip</td><td>$25 - $40</td></tr>"
 "<tr><td>Food, two days of casual meals out</td><td>$100 - $220</td></tr>"
 "<tr><td>Attractions and parking</td><td>$20 - $90</td></tr></table>"
 "<p>The swing is almost entirely the room. The same oceanfront hotel that asks $260 a night on a July Saturday lists for $90 - $120 in April or late October, which is why shoulder season is the local's move.</p>"
 "<h2>A two-day plan that works</h2><p>Day one: arrive by mid-morning, drop bags, and take the beach while the light is good. In the late afternoon climb the dunes at Jockey's Ridge State Park, which is free, for the best sunset on the northern beaches, then eat in Nags Head or Kill Devil Hills. Day two: start at the Wright Brothers National Memorial when it opens, walk the first-flight line before the tour buses, then either browse the shops and duck donuts in Duck or drive south past Oregon Inlet to Pea Island for empty-beach walking and birdlife. Lunch on the water, one last beach hour, and you are home by dinner.</p>"
 "<h2>The best time of year to go</h2><p>May, early June, September, and October are the sweet spots. The ocean is swimmable from late May through October, the crowds and rates peak from mid-June to mid-August, and September in particular gives warm water, open restaurants, and hotel prices a third below July. Winter weekends are the bargain, with $80 - $120 oceanfront rooms and empty beaches, as long as a windswept walk sounds better to you than a swim.</p>"
 "<h2>Worth knowing before you go</h2><p>Book summer Saturdays two to three months out, since the central-beach hotels fill first, while off-season trips can be booked the same week. Beach parking is free at most public accesses in Kitty Hawk and Kill Devil Hills but fills by 10 am in summer. And check the events calendar before you pick your weekend, because fishing tournaments and the marathon in November can quietly double room rates.</p>",
 [("How far is the Outer Banks from Virginia Beach?","About 60 miles and 90 minutes to Kitty Hawk on US-168 and NC-158, though summer Saturday bridge traffic can stretch it past two hours. Leaving before 8 am avoids the worst of it."),
  ("How much does an Outer Banks weekend cost?","$350 - $900 for two people for two nights in 2026, covering the room, gas, meals, and attractions. The room drives the range, with off-season rates at less than half of July prices."),
  ("What is the best time for an Outer Banks weekend?","May, early June, September, and October. September is the standout, with warm ocean water, thinner crowds, and hotel rates roughly a third below peak summer.")],
 [article_node("An Outer Banks weekend from Virginia Beach: costs and plan","What an Outer Banks weekend from Virginia Beach costs in 2026, with the route, where to stay, and a two-day plan.","https://wonderlocity.com/guides/outer-banks-weekend/")],
 [("Weekend getaways from Virginia Beach","/guides/weekend-getaways-from-virginia-beach/"),("Travel guides","/guides/"),("Plan with me","/plan/")],
 "Outer Banks hotels and rentals")

rich_page("guides/williamsburg-weekend/index.html","https://wonderlocity.com/guides/williamsburg-weekend/",
 [("Home","/"),("Travel guides","/guides/"),("Williamsburg weekend",None)],"A Williamsburg weekend from Virginia Beach: what to do","wl-g15-hero",
 "Williamsburg Weekend from Virginia Beach 2026: What to Do and Real Costs | Wonderlocity",
 "A Williamsburg weekend from Virginia Beach costs $400 - $1,000 for two in 2026. The one-hour drive, Colonial Williamsburg tips, Busch Gardens, and a two-day plan.",
 "A Williamsburg weekend from Virginia Beach costs $400 - $1,000 for two people in 2026, covering two nights in a hotel, gas for the roughly one-hour drive, meals out, and tickets to Colonial Williamsburg or a day at Busch Gardens.",
 "<p>Williamsburg is the closest real getaway Virginia Beach has. It is under an hour away, yet it swaps the boardwalk for brick sidewalks, fife and drum corps, and one of the best theme parks on the East Coast. It works as a history weekend, a roller coaster weekend, or an eat-and-wander weekend, and it is cheap enough that you can decide on Thursday and go on Saturday. Here is how to do it well.</p>"
 "<h2>Getting there from Virginia Beach</h2><p>The drive is about 60 miles and an hour on a clear day: I-264 west to I-64 west, through the Hampton Roads Bridge-Tunnel, then straight up the Peninsula to the Colonial Williamsburg exits. The tunnel is the variable. On summer Fridays and holiday weekends an HRBT backup can add 30 to 60 minutes, so leave before 9 am or after 7 pm and you will glide through. No flights, no ferries, one tank of gas covers the whole trip both ways.</p>"
 "<h2>What a weekend costs in 2026</h2><p>These ranges cover two people for two nights, with the low end for an off-season trip built around free strolling and one paid attraction, and the high end for a peak-season weekend with a nicer hotel and a full day at Busch Gardens.</p><table class='costtable'>"
 "<tr><td>Hotel, 2 nights</td><td>$150 - $450</td></tr>"
 "<tr><td>Gas from Virginia Beach, round trip</td><td>$15 - $25</td></tr>"
 "<tr><td>Food, two days of meals out</td><td>$120 - $260</td></tr>"
 "<tr><td>Attractions for two</td><td>$100 - $330</td></tr></table>"
 "<p>Williamsburg hotels are a quiet bargain. The town has far more rooms than a normal town its size because of the tourism base, so outside graduation weekends and the December holidays, $75 - $120 a night buys a solid stay and $180 - $220 puts you in the historic-area inns.</p>"
 "<h2>Colonial Williamsburg without overpaying</h2><p>Here is the part first-timers miss: walking the historic area is free. Duke of Gloucester Street, the gardens, the taverns from the outside, the costumed interpreters going about their day, all of it is open to anyone. The admission ticket, about $50 per adult for a single day in 2026, is what gets you inside the buildings: the Governor's Palace, the Capitol, the trade shops where smiths and printers actually work. If you have never been, one ticketed day is worth it, and the trades demonstrations are the highlight. If you mostly want the atmosphere, budget your money for a tavern dinner instead and stroll for free.</p>"
 "<h2>Busch Gardens, history, or both</h2><p>Busch Gardens Williamsburg runs about $60 - $90 per person for single-day tickets bought online in 2026, and it is regularly voted the most beautiful theme park in the country. The coasters are legitimate, the food is better than theme park average, and the park sits ten minutes from the historic area. A weekend gives you room for one full Busch Gardens day and one historic-area day, which is the classic split. With toddlers or grandparents in tow, swap the park day for Jamestown and an afternoon at the free Yorktown beach.</p>"
 "<h2>Do not skip Jamestown and Yorktown</h2><p>Williamsburg is one corner of the Historic Triangle, and the Colonial Parkway that links all three is the prettiest drive in the region. Historic Jamestowne, the actual 1607 site, and the Yorktown battlefield are both run by the National Park Service and cost far less than the big attractions, roughly $15 - $30 per adult depending on passes. Yorktown also has a small riverfront beach and a walkable main street that makes a perfect low-key Sunday morning before the drive home.</p>"
 "<h2>A two-day plan that works</h2><p>Day one: leave Virginia Beach by 8 am, beat the tunnel, and be walking Duke of Gloucester Street by 9:30. Do the ticketed buildings in the morning while the tour groups are thin, lunch at a tavern or in Merchants Square, then spend the afternoon on the trades shops and the Palace gardens. Dinner in Merchants Square, and if it is summer, catch the evening fife and drum march. Day two: Busch Gardens from opening until mid-afternoon, or the Jamestown and Yorktown loop via the Colonial Parkway, then roll home against light Sunday traffic and be back for dinner.</p>"
 "<h2>When to go</h2><p>April, May, September, and October are the sweet spots, with warm walking weather and full operating schedules. Summer works but is hot and holds the biggest Busch Gardens crowds. December is a special case: Grand Illumination and the holiday decorations make it the most atmospheric month, and Christmas Town at Busch Gardens turns the park into a lights festival, so it is worth braving the cold at least once. January and February are the true bargain months, with $75 hotel nights, though some attractions run shorter hours.</p>",
 [("How far is Williamsburg from Virginia Beach?","About 60 miles, roughly an hour up I-64 through the Hampton Roads Bridge-Tunnel. Summer Friday tunnel backups can add 30 to 60 minutes, so leave early or after dinner."),
  ("How much does a Williamsburg weekend cost?","$400 - $1,000 for two people for two nights in 2026, covering the hotel, gas, meals, and tickets. The swing comes from the hotel tier and whether you add a Busch Gardens day."),
  ("Is Colonial Williamsburg worth the ticket price?","For a first visit, yes. About $50 per adult opens the Governor's Palace, the Capitol, and the working trade shops. Walking the historic streets themselves is free, so repeat visitors can enjoy the town without a ticket.")],
 [article_node("A Williamsburg weekend from Virginia Beach: what to do","What a Williamsburg weekend from Virginia Beach costs in 2026, with Colonial Williamsburg tips, Busch Gardens, and a two-day plan.","https://wonderlocity.com/guides/williamsburg-weekend/")],
 [("Weekend getaways from Virginia Beach","/guides/weekend-getaways-from-virginia-beach/"),("Outer Banks weekend","/guides/outer-banks-weekend/"),("Travel guides","/guides/")],
 "Williamsburg hotels")

# ---- deals page ----
deals_body = ('<p class="answer">These are the booking partners Wonderlocity uses for hotels, tours, and travel insurance, all at the same price you would pay direct.</p>'
 '<div class="prose">'
 '<p>Booking through these links is how the free guides stay free. We only list partners we would use ourselves. During setup we connect your live Expedia TAAP and Travelpayouts widgets here, filtered by destination.</p>'
 '<h2>Hotels and resorts</h2><p>Compare beachfront and city stays across the Caribbean, Mexico, and Europe.</p>'
 '<h2>Tours and activities</h2><p>Skip-the-line tickets, day trips, and excursions through trusted operators.</p>'
 '<h2>Travel insurance</h2><p>Coverage we recommend on every trip, quoted in a couple of minutes.</p>'
 '</div>'
 + affiliate_panel("your trip") )
simple_page("deals","Travel Deals | Hotels, Tours, Insurance | Wonderlocity","The hotel, tour, and travel insurance partners Wonderlocity uses, at the same price you pay direct. Booking here keeps our guides free.","Travel deals","wl-deals-hero",deals_body,
 {"@type":"CollectionPage","name":"Travel deals"})

# ---- resources / lead magnet ----
resources_body = ('<p class="answer">Get the free guide: what a week all-inclusive in the Caribbean really costs in 2026, plus the resorts worth the money.</p>'
 '<div class="prose"><p>Join the Wonderlocity list and we will send the cost breakdown straight to your inbox, then a short, useful email every couple of weeks. No spam, unsubscribe anytime.</p>'
 '<form action="#" method="post" onsubmit="return false" style="display:flex;gap:10px;flex-wrap:wrap;max-width:460px">'
 '<input type="email" placeholder="Your email" aria-label="Your email" required style="flex:1;min-width:220px;border:1px solid var(--line);border-radius:40px;padding:13px 18px;font:inherit">'
 '<button class="btn btn-gold" type="submit">Send me the guide</button></form>'
 '<p class="disc">We will connect this to MailerLite free during setup.</p></div>')
simple_page("resources","Free Travel Resources | Wonderlocity","Free Wonderlocity guides, starting with the real cost of a week all-inclusive in the Caribbean in 2026.","Free resources","wl-res-hero",resources_body,
 {"@type":"CollectionPage","name":"Free resources"})

rich_page("guides/caribbean-family-resorts/index.html","https://wonderlocity.com/guides/caribbean-family-resorts/",
 [("Home","/"),("Travel guides","/guides/"),("Caribbean family resorts",None)],"The best family all-inclusive resorts in the Caribbean for 2026","wl-g16-hero",
 "Best Family All-Inclusive Resorts in the Caribbean 2026 | Wonderlocity",
 "The best family all-inclusive resorts in the Caribbean for 2026, by budget and kid age, with real per-person prices and which ones have the strongest kids clubs.",
 "The best family all-inclusive resorts in the Caribbean for 2026 run $1,400 - $4,500 per person for a week, with RIU and Grand Palladium properties leading on value, Beaches Turks and Caicos leading on kids activities, and Atlantis Paradise Island leading on the splurge trip.",
 "<p>Family resorts live and die on one thing, whether the kids stay busy enough that the adults get any actual vacation. Price matters too, but a cheap resort with a bored eight year old is not a deal. Here is how the Caribbean family market breaks down, with the numbers up front.</p>"
 "<h2>How much a family week costs</h2><p>Family all-inclusive pricing depends heavily on how many kids clubs, water features, and suite configurations a resort offers, since family suites and connecting rooms cost more than a standard couples room. For a 7-night week with round-trip US flights, here is the 2026 range by tier.</p><table class='costtable'>"
 "<tr><td>Value tier, RIU and similar</td><td>$1,400 - $2,600 per person</td></tr>"
 "<tr><td>Mid tier, Grand Palladium and similar</td><td>$2,200 - $3,400 per person</td></tr>"
 "<tr><td>Splurge tier, Atlantis Paradise Island</td><td>$3,200 - $4,500 per person</td></tr>"
 "<tr><td>Family suite or connecting rooms upgrade</td><td>add $200 - $700 per person</td></tr></table>"
 "<h2>Best for value</h2><p>RIU's family properties across Aruba, Jamaica, and the Dominican Republic keep the format simple: buffet dining that works for picky eaters, a dedicated kids pool, and beachfront access without extra frills. Prices stay predictable because there is little room variation, which makes RIU the easiest resort to budget for down to the dollar.</p>"
 "<h2>Best for a strong kids club</h2><p>Beaches Turks and Caicos runs one of the largest water park setups of any family resort in the Caribbean, with a supervised kids camp that genuinely frees up adult pool time. This is the pick when the trip needs to entertain kids ages 5 to 12 for a full week without repeat activities.</p>"
 "<h2>Best mid-range step up</h2><p>Grand Palladium properties in the Riviera Maya and Jamaica sit a notch above value resorts in polish and grounds, with kids club programs strong enough to handle siblings of different ages who want different things during the day.</p>"
 "<h2>Best for a milestone trip</h2><p>Atlantis Paradise Island in the Bahamas functions less like a resort and more like a full destination, built around the Aquaventure water park and a marine habitat kids can walk through. It costs more, but for a big family trip it delivers an experience kids remember for years.</p>"
 "<h2>Cheapest time to go</h2><p>Family resort prices peak hardest around the December holidays and spring break, when school schedules force demand into a few weeks. Late April through early June, and again in September through early November outside hurricane peak, both bring meaningfully lower rates at every tier.</p>"
 "<h2>The verdict</h2><p>Choose RIU for predictable value, Beaches Turks and Caicos for the strongest kids club and water park, Grand Palladium for a mid-range step up, and Atlantis for a milestone trip worth the splurge. For most families the sweet spot is a mid-tier resort booked in shoulder season, which buys noticeably nicer grounds for close to value-tier pricing.</p>",
 [("How much does a Caribbean family resort cost per person?","About $1,400 to $4,500 per person for a week in 2026, depending on tier. Value resorts like RIU sit at the low end, while Atlantis Paradise Island sits at the top for its water park and marine habitat."),
  ("Which Caribbean resort is best for young kids?","Beaches Turks and Caicos, thanks to its large water park and supervised kids camp built for ages 5 to 12."),
  ("When is the cheapest time to book a Caribbean family trip?","Late April through early June, and September through early November outside hurricane peak, both bring lower rates than the December holidays or spring break.")],
 [article_node("The best family all-inclusive resorts in the Caribbean for 2026","Family resorts in the Caribbean by budget and kid age, with real 2026 prices.","https://wonderlocity.com/guides/caribbean-family-resorts/")],
 [("Trip types: family","/trip-types/family/"),("Orlando on a budget","/guides/orlando-on-a-budget/"),("Punta Cana guide","/destinations/punta-cana/")],
 "Caribbean family all-inclusive resorts")

rich_page("guides/cancun-vs-punta-cana-vs-nassau/index.html","https://wonderlocity.com/guides/cancun-vs-punta-cana-vs-nassau/",
 [("Home","/"),("Travel guides","/guides/"),("Cancun vs Punta Cana vs Nassau",None)],"Cancun vs Punta Cana vs Nassau: which fits your trip","wl-g17-hero",
 "Cancun vs Punta Cana vs Nassau 2026: Which Fits Your Trip | Wonderlocity",
 "Cancun, Punta Cana, and Nassau compared for flight time, price, and vibe in 2026, so you can pick the right warm-weather trip instead of guessing.",
 "Cancun wins on flight access and resort variety, Punta Cana wins on value at the luxury tier, and Nassau wins on flight time from the East Coast and the Atlantis resort experience, and all three sit in the same December to April dry season.",
 "<p>These three are consistently the most searched beach destinations for US travelers, and each one is genuinely different once you get past 'tropical beach vacation.' Here is how to actually choose.</p>"
 "<h2>Flight time and price snapshot</h2><table class='costtable'>"
 "<tr><td>Cancun, flight time from most US cities</td><td>2.5 - 4 hours</td></tr>"
 "<tr><td>Punta Cana, flight time from most US cities</td><td>3.5 - 5 hours</td></tr>"
 "<tr><td>Nassau, flight time from most US East Coast cities</td><td>2 - 3.5 hours</td></tr>"
 "<tr><td>Typical 7-night all-inclusive, per person, 2026</td><td>$1,400 - $3,400 across all three</td></tr></table>"
 "<h2>Cancun, Mexico</h2><p>Cancun offers the widest resort inventory of the three at every price point, plus direct flights from dozens of US cities and easy access to extras like Mayan ruins and cenotes if you want to leave the resort. The tradeoff is a busier Hotel Zone, especially during winter peak months.</p>"
 "<h2>Punta Cana, Dominican Republic</h2><p>Punta Cana tends to offer more beach space per resort than Cancun's tighter Hotel Zone, and better value at the luxury tier, so higher-end adults-only resorts often cost less here than comparable Cancun properties. It has fewer off-resort activities, making it more of a stay-and-relax destination than an explore one.</p>"
 "<h2>Nassau, Bahamas</h2><p>Nassau's biggest draw is Atlantis Paradise Island, which functions almost as its own theme park with a large water park and marine exhibits. It is also the shortest flight for most East Coast travelers, which makes it a strong pick for a long weekend rather than a full week, though it runs pricier than Cancun or Punta Cana for comparable resort quality.</p>"
 "<h2>Quick decision guide</h2><p>Want the shortest flight and do not mind paying a bit more, choose Nassau. Want the best luxury to price ratio and quieter beaches, choose Punta Cana. Want the most resort options, easiest flights, and extra activities off resort, choose Cancun.</p>"
 "<h2>The verdict</h2><p>All three sit within the Caribbean and Gulf dry season window of December through April, so weather-wise the decision comes down to vibe, budget, and how far you are willing to fly rather than the calendar.</p>",
 [("Which is cheaper, Cancun, Punta Cana, or Nassau?","Cancun usually has the lowest entry price thanks to the largest resort inventory, Punta Cana offers the best value at the luxury tier, and Nassau tends to run priciest for comparable resort quality."),
  ("Which has the shortest flight from the US?","Nassau, for most East Coast departure cities, at 2 to 3.5 hours."),
  ("Which is better for a first-time all-inclusive trip?","Cancun, because of its resort variety, easy direct flights, and off-resort activities if you want a break from the beach.")],
 [article_node("Cancun vs Punta Cana vs Nassau: which fits your trip","A 2026 comparison of flight time, price, and vibe across all three.","https://wonderlocity.com/guides/cancun-vs-punta-cana-vs-nassau/")],
 [("Cancun vs Riviera Maya","/guides/cancun-travel-cost/"),("Punta Cana adults-only resorts","/guides/punta-cana-best-resorts/"),("Punta Cana guide","/destinations/punta-cana/")],
 "Cancun, Punta Cana, and Nassau trip planning")

rich_page("essentials/caribbean-packing-list/index.html","https://wonderlocity.com/essentials/caribbean-packing-list/",
 [("Home","/"),("Travel essentials","/essentials/"),("Caribbean packing list",None)],"What to pack for a Caribbean all-inclusive resort","wl-ess1-hero",
 "Caribbean All-Inclusive Packing List 2026 | Wonderlocity",
 "The exact packing list for a Caribbean all-inclusive resort, with what to put in your carry-on, what the resort already provides, and what people forget most.",
 "Pack light for a Caribbean all-inclusive: two swimsuits, reef-safe sunscreen, a light cover-up, sandals, one nice outfit for dinner, and your travel documents in the carry-on, since the resort supplies towels, most toiletries, and pool floats.",
 "<p>All-inclusive resorts remove most of the guesswork, since food, drinks, and often basic toiletries are covered. The packing mistakes people actually make are less about forgetting items and more about overpacking for a trip where the resort already has you covered.</p>"
 "<h2>What to put in your carry-on</h2><p>Keep the essentials with you in case checked luggage is delayed, which matters more on island routes with tighter connections. Pack one swimsuit, sunscreen, sunglasses, any medication, phone and charger, and your passport or ID plus hotel confirmation in your carry-on.</p>"
 "<h2>What the resort almost always provides</h2><p>Most Caribbean all-inclusives supply pool towels, basic shampoo and soap, beach umbrellas or cabana access, and often snorkel gear at the water sports desk. Check your specific resort's site before packing your own, since bringing duplicates just adds weight.</p>"
 "<h2>Clothing that actually gets worn</h2><p>Two swimsuits let one dry while you wear the other, which matters in humid climates where things do not dry overnight. Add a light cover-up, breathable shorts or a sundress, one slightly nicer outfit for a specialty dinner, and comfortable sandals. Skip the extra shoes, most trips only use two pairs the whole week.</p>"
 "<h2>What people forget most</h2><p>Reef-safe sunscreen matters both for your skin and because some Caribbean destinations now require it by law. A dry bag protects your phone at the pool or beach, and a portable charger covers a full excursion day without hunting for an outlet. A light rain jacket or umbrella is worth the space, since Caribbean showers are brief but common even in dry season.</p>"
 "<h2>What to skip</h2><p>Leave the beach towel at home, the resort provides one, and skip a full toiletry kit since most all-inclusives stock the basics. Formal wear is rarely needed outside one specialty dinner, and heavy guidebooks are better replaced with a phone and a saved guide.</p>",
 [("Do I need to bring my own towels to a Caribbean all-inclusive?","No, pool and beach towels are included at nearly every Caribbean all-inclusive resort, usually through a towel card system at the pool desk."),
  ("Is reef-safe sunscreen actually required?","Some Caribbean destinations, including parts of Mexico and the US Virgin Islands, restrict sunscreens with oxybenzone and octinoxate to protect coral reefs, so reef-safe is the safer default everywhere in the region."),
  ("How many swimsuits should I pack for a week?","Two is the practical number, so one can dry while the other is in use, which matters in humid Caribbean climates.")],
 [article_node("What to pack for a Caribbean all-inclusive resort","The exact 2026 packing list for a Caribbean all-inclusive week.","https://wonderlocity.com/essentials/caribbean-packing-list/")],
 [("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/"),("Punta Cana guide","/destinations/punta-cana/"),("First Caribbean cruise","/guides/caribbean-cruise-first-timer/")],
 None)

rich_page("essentials/cruise-packing-list/index.html","https://wonderlocity.com/essentials/cruise-packing-list/",
 [("Home","/"),("Travel essentials","/essentials/"),("Cruise packing list",None)],"Cruise packing list: what first-timers forget","wl-ess2-hero",
 "Cruise Packing List 2026: What First-Timers Forget | Wonderlocity",
 "A first-timer's cruise packing list covering what to bring, what cabins lack, and the small items that make the first day much easier.",
 "Pack a magnetic power strip, a small day bag, motion sickness remedies even if you rarely get seasick, and a lanyard for your ship card, since cabins have limited outlets and the first sea day catches most first-timers off guard.",
 "<p>Cruise ships pack a lot into a small cabin, which means a few specific items solve problems that only show up once you are on board. Here is what actually earns space in a first-timer's suitcase.</p>"
 "<h2>Cabin essentials cruise lines do not mention</h2><p>Most cabins have very few outlets, so a magnetic power strip, not a surge-protected one which most lines ban, keeps phones, cameras, and CPAP machines charged without a nightly outlet standoff. A door magnet organizer holds daily schedules and small items on the metal cabin door, which is genuinely useful in a small space.</p>"
 "<h2>For getting on and off the ship</h2><p>A small day bag or backpack matters more than it sounds, since you carry it through embarkation lines, port excursions, and back on board through security. A lanyard or card holder for your ship key card saves you patting down pockets at every door and the bar.</p>"
 "<h2>For the first sea day</h2><p>Motion sickness remedies are worth packing even if you rarely feel seasick, since the first day out can catch anyone off guard in open water before the ship settles into its route. Ginger chews, wristbands, or over-the-counter medication all work, pick before you need it rather than searching the ship's small shop mid-crossing.</p>"
 "<h2>Clothing by day type</h2><p>Pack layers for the ship's strong air conditioning, swimwear for pool and port days, and one or two slightly dressier outfits if your line has a formal or elegant night. Comfortable walking shoes matter more than cruise-specific gear, since port days often mean several hours on foot.</p>"
 "<h2>What people forget most</h2><p>A printed copy of your booking confirmation and ID, in case a phone battery dies at exactly the wrong moment during embarkation. Cash in small bills for ports where cards are not always accepted. Reusable water bottle, since most ships let you fill it at stations around the ship, saving both money and trips to the bar for water.</p>",
 [("Do cruise cabins have enough outlets?","Rarely more than one or two, which is why a magnetic power strip (not a surge-protected one, which most lines prohibit) is one of the most useful items to pack."),
  ("Should I pack seasickness medication even if I don't usually get seasick?","Yes, the first sea day catches many first-timers off guard before the ship settles into its route, and it is easier to have it on hand than to search a small ship shop mid-crossing."),
  ("What should I bring for getting on and off the ship at ports?","A small day bag for essentials, your ship key card on a lanyard, and comfortable walking shoes, since port days often involve several hours on foot.")],
 [article_node("Cruise packing list: what first-timers forget","What to pack for a first cruise, and what cabins lack.","https://wonderlocity.com/essentials/cruise-packing-list/")],
 [("First Caribbean cruise","/guides/caribbean-cruise-first-timer/"),("Royal Caribbean vs Carnival","/guides/royal-caribbean-vs-carnival/"),("Trip types: cruise","/trip-types/cruise/")],
 None)

# ---- section index pages ----
listing_page("destinations/index.html","https://wonderlocity.com/destinations/",
 [("Home","/"),("Destinations",None)],"Destinations","wl-dest-hero",
 "Destination Guides with Real 2026 Costs | Wonderlocity",
 "Honest destination guides with real 2026 price ranges, from the Caribbean to the Maldives to Disney.",
 "Every destination guide opens with a real 2026 price range, so you know the cost before you fall in love with the place. More destinations are added every week.",
 [("Punta Cana","/destinations/punta-cana/","puntacana","From $1,400 - $3,200 pp, week","Easy all-inclusive beach value from the East Coast."),
  ("Maldives","/destinations/maldives/","maldivesod","From $4,500 - $11,000 per couple","The honeymoon benchmark, and where to splurge."),
  ("Orlando and Disney","/destinations/orlando/","orlandofl","From $3,800 - $7,500 for four","Tickets, park days, and where families save.")])

listing_page("trip-types/index.html","https://wonderlocity.com/trip-types/",
 [("Home","/"),("Trip types",None)],"Trip types","wl-tt-hero",
 "Plan by Trip Type: All-Inclusive, Honeymoon, Cruise, Family | Wonderlocity",
 "Plan by the kind of trip you want, with real 2026 cost ranges for each.",
 "Not sure where, but you know the kind of trip? Start here. Each guide gives a real 2026 cost range and how to get the most for it.",
 [("All-inclusive","/trip-types/all-inclusive/","wl-ai-hero","$1,200 - $3,500 per person, week","One price, zero decisions, easy beach weeks."),
  ("Honeymoon","/trip-types/honeymoon/","wl-hm-hero","$3,000 - $12,000 per couple","Where to splurge and where to save."),
  ("Cruises","/trip-types/cruise/","wl-cr-hero","From about $700 per person, week","All-in-one, plus the extras to budget for."),
  ("Family","/trip-types/family/","wl-fm-hero","$3,500 - $8,000 for four","Beaches and Disney, and where families save.")])

listing_page("guides/index.html","https://wonderlocity.com/guides/",
 [("Home","/"),("Travel guides",None)],"Travel guides","wl-guides-hero",
 "Travel Guides: Honest Costs and Best-Time Answers | Wonderlocity",
 "Answer-first travel guides on costs, timing, and getaways. Written to actually answer the question.",
 "Straight answers, written first. Costs, best times to go, and trips worth taking, with the numbers up front.",
 [("All-inclusive Caribbean cost","/guides/all-inclusive-caribbean-cost/","wlguide1","","What a week really costs in 2026, by destination."),
  ("Best time to visit Italy","/guides/best-time-to-visit-italy/","wlguide2","","Season by season, region by region."),
  ("Weekend getaways from Virginia Beach","/guides/weekend-getaways-from-virginia-beach/","wlguide3","","12 drivable trips within 4 hours."),
  ("Cancun vs Riviera Maya","/guides/cancun-travel-cost/","wlguide4","","Which is better value in 2026, compared."),
  ("Punta Cana adults-only resorts","/guides/punta-cana-best-resorts/","wlguide5","","The best adults-only all-inclusive resorts, by area."),
  ("Maldives vs Bora Bora","/guides/maldives-vs-bora-bora/","wlguide6","","Cost and feel, compared for honeymooners."),
  ("Santorini honeymoon cost","/guides/santorini-honeymoon-cost/","wlguide7","","What a week in Santorini really runs in 2026."),
  ("First Caribbean cruise","/guides/caribbean-cruise-first-timer/","wlguide8","","A complete cost and tips guide for beginners."),
  ("Royal Caribbean vs Carnival vs Norwegian","/guides/royal-caribbean-vs-carnival/","wlguide9","","Which cruise line to pick, compared."),
  ("Disney or Universal for toddlers","/guides/disney-or-universal-toddlers/","wlguide10","","Which park actually suits little kids better."),
  ("Orlando on a budget","/guides/orlando-on-a-budget/","wlguide11","","How to do Orlando without overspending."),
  ("Best time to visit Greece","/guides/best-time-to-visit-greece/","wlguide12","","By island and by budget."),
  ("10-day Italy itinerary","/guides/italy-10-day-itinerary/","wlguide13","","A first-timer route, with costs."),
  ("Outer Banks weekend","/guides/outer-banks-weekend/","wlguide14","","Costs and a plan, from Virginia Beach."),
  ("Williamsburg weekend","/guides/williamsburg-weekend/","wlguide15","","What to do, from Virginia Beach."),
  ("Best family resorts in the Caribbean","/guides/caribbean-family-resorts/","wlguide16","","By budget and kid age, with real prices."),
  ("Cancun vs Punta Cana vs Nassau","/guides/cancun-vs-punta-cana-vs-nassau/","wlguide17","","Flight time, price, and vibe, compared.")])

listing_page("essentials/index.html","https://wonderlocity.com/essentials/",
 [("Home","/"),("Travel essentials",None)],"Travel essentials","wl-ess-hero",
 "Travel Essentials: Packing Lists and Gear That Actually Helps | Wonderlocity",
 "Real packing lists for Caribbean resorts and cruises, covering what to bring, what to skip, and what most people forget.",
 "No generic packing filler, just what actually earns space in your suitcase for the trip you are taking.",
 [("Caribbean all-inclusive packing list","/essentials/caribbean-packing-list/","wlessguide1","","What to pack, what to skip, what the resort provides."),
  ("Cruise packing list","/essentials/cruise-packing-list/","wlessguide2","","What first-timers forget most.")])

# ===== Cruises section: hub + 3 Carnival articles (added Nov 2026) =====
CRUISE_SEED = "wl-caribbean"

# ---- Article 1: Carnival review and costs ----
rich_page("cruises/carnival-cruise-line-review/index.html","https://wonderlocity.com/cruises/carnival-cruise-line-review/",
 [("Home","/"),("Cruises","/cruises/"),("Carnival Cruise Line",None)],"Carnival Cruise Line: is it right for you?","cr-review",
 "Carnival Cruise Review 2027: Costs, Cabins, Who It Fits | Wonderlocity",
 "A Carnival cruise starts from about $105 per person per night in late 2026. See what the fare includes, what costs extra, and who it fits.",
 "A Carnival cruise starts from about $105 per person per night for an inside cabin and from about $165 for a balcony in late 2026, so a week starts from roughly $735 for an inside cabin and $1,155 for a balcony, per person, before gratuities, drinks, and excursions. It is the best-value big-ship line for families, groups, and first-timers who want plenty to do and do not need a quiet, formal ship.",
 """{{FACTS|Starts from=about $105 per person, per night;Best for=Families, groups, first-timers;Watch the extras=Gratuities, drinks, wifi;Easiest first sail=4 to 5 nights}}<p>Carnival is the line most Americans picture when they think of a cruise: big, lively ships, a casual dress code, a water slide on deck, and a price that undercuts most of the competition. It is also the line people are most likely to be surprised by on the bill, because the low fare leaves out several things that most guests end up buying. Here is what you actually get, what it really costs, and who should book it.</p>
<h2>What a week on Carnival actually feels like</h2><p>Carnival calls its ships Fun Ships, and the name is honest. Expect a busy pool deck, music, trivia, comedy, and a nightly theater show, with a crowd that skews toward families, friend groups, and multi-generation trips. The mood is relaxed and the dress is shorts and flip-flops by day, with an optional dressier night or two. Food leans casual and generous, with a main dining room, a buffet, and free counters like Guy's Burger Joint, BlueIguana Cantina, and a pizzeria. If you picture a quiet, polished, adults-only sailing, this is not it. If you picture a good-value week where everyone in your group finds something to do, it is.</p>
{{FIG|cr-beachship|A beach stop is part of many Caribbean and Bahamas sailings.}}<h2>What it costs: starting prices</h2><p>Cabin type drives the price more than anything else. These are late-2026 averages per person, drawn from a price tracker that follows Carnival sailings, and they are a guide rather than a quote, since a school-holiday week or a brand-new ship can cost well above them.</p>
<table class='costtable'><tr><td>Inside cabin</td><td>from $105 a night, about $735 a week</td></tr>
<tr><td>Ocean view cabin</td><td>from $130 a night, about $910 a week</td></tr>
<tr><td>Balcony cabin</td><td>from $165 a night, about $1,155 a week</td></tr>
<tr><td>Suite</td><td>from $265 a night, about $1,860 a week</td></tr></table>
<p>Shorter sailings are where Carnival is cheapest to try. In sample fares priced in 2025 and 2026, a 4-night Baja cruise from Long Beach started near $390 for an inside cabin, and a 5-night Western Caribbean sailing from Miami started near $525. Always compare the final price with taxes and port fees included, because that is the number you will pay.</p>
<h2>What is included in the fare</h2><p>Your cabin with daily steward service, meals in the main dining room and buffet, the free casual counters, and a handful of free drinks: water, iced tea, lemonade, milk, hot chocolate, select juices, and basic coffee. You also get the pools, the WaterWorks slides, the SportSquare activities, the fitness center, the nightly shows, and the kids clubs, which are Camp Ocean for ages 2 to 11, Circle C for 12 to 14, and Club O2 for 15 to 17. Visits to Carnival's own Bahamas destinations, such as Celebration Key and Half Moon Cay, cost nothing extra.</p>
{{TIP|How to read a &ldquo;from&rdquo; price|A &ldquo;from&rdquo; fare is the starting price for an inside cabin. Your sailing can cost more depending on the ship, the week, and how close you book, so treat these numbers as a starting point and ask for a quote on your exact dates.}}<h2>Where the extra money goes</h2><p>This is the part to budget for before you book. The big four are gratuities, drinks, wifi, and excursions.</p>
<table class='costtable'><tr><td>Gratuities, standard cabin</td><td>$17 per person, per day</td></tr>
<tr><td>Gratuities, suite</td><td>$19 per person, per day</td></tr>
<tr><td>Bottomless Bubbles soda package</td><td>$11.99 adult, $6.95 child, per day</td></tr>
<tr><td>Cheers alcohol package</td><td>about $80 to $95 per adult, per day</td></tr>
<tr><td>Wifi</td><td>about $19 to $24 per day</td></tr>
<tr><td>Specialty dinner</td><td>about $25 to $50 per adult</td></tr>
<tr><td>Shore excursions</td><td>varies by port</td></tr></table>
<p>Gratuities are added automatically, so a week costs about $119 per person in a standard cabin. Drink packages carry a 20 percent service charge on top of the listed price, and if one adult in a cabin buys the Cheers package, Carnival requires every adult 21 and over in that cabin to buy it too. Prices move, so confirm each figure on Carnival's site when you book.</p>
{{TIP|Do this before you compare fares|Add about $119 per person for gratuities on a 7-night sailing in a standard cabin, then compare ships. That one step makes cheap-looking fares much easier to judge.}}<h2>What you will really spend</h2><p>A useful rule of thumb is from about $150 per person per day for an inside cabin with light spending, and from about $200 per day for a typical guest who adds drinks, wifi, and a couple of excursions. A couple on a 7-night balcony cruise who drink at dinner and book two excursions should plan for well over the fare alone, and the extras can add 30 to 60 percent on top.</p>
<h2>Is Carnival your kind of cruise?</h2><p>Carnival is a strong pick for families with kids, because the clubs and water attractions are some of the best at sea. It suits groups and celebrations, first-timers on a short sailing, and anyone who wants the lowest entry price on a big ship. It is a weaker fit for travelers who want quiet, a formal atmosphere, or a ship that feels exclusive. For those, our <a href='/guides/royal-caribbean-vs-carnival/'>Royal Caribbean vs Carnival vs Norwegian comparison</a> shows where the other lines pull ahead.</p>
<h2>Tips before you book</h2><p>The ship matters as much as the cabin, since the newest ships have far bigger attractions than the oldest, and our <a href='/cruises/carnival-ships-guide/'>Carnival ships guide</a> explains the difference. Pick your sailing port first, because a drive-to port saves airfare, which we cover in the <a href='/cruises/carnival-caribbean-itineraries/'>Carnival Caribbean itineraries guide</a>. Decide on drinks before you sail, since the pre-cruise price is usually lower than the onboard price. And if this is your first cruise, read the <a href='/guides/caribbean-cruise-first-timer/'>first Caribbean cruise guide</a> and the <a href='/essentials/cruise-packing-list/'>cruise packing list</a> before you pack.</p>
{{TIP|Pick the ship first|The newest ships have far bigger attractions than the oldest, so choose the ship before you choose the cabin. Our <a href='/cruises/carnival-ships-guide/'>Carnival ships guide</a> explains the classes.}}<h2>Our take</h2><p>Carnival delivers the most ship for the least money, and it is hard to beat for a family or a group on a budget. Go in knowing the fare is the starting point, add gratuities and drinks to your math, and pick a newer ship if the attractions matter to you.</p>"""
 + cruise_panel(),
 [("How much does a Carnival cruise cost?","From about $105 per person per night for an inside cabin and from about $165 for a balcony in late 2026, or roughly $735 and $1,155 per person for a week, before gratuities, drinks, and excursions."),
  ("Are drinks included on Carnival?","Only basic ones such as water, iced tea, lemonade, and drip coffee. Soda, alcohol, specialty coffee, and bottled water cost extra, though you can buy a package. Bottomless Bubbles is the soda package and Cheers is the alcohol package."),
  ("Do I have to pay gratuities on Carnival?","Yes. They are added automatically at $17 per person per day in a standard cabin and $19 in a suite for sailings from April 2026, and they are paid on top of your fare."),
  ("Is Carnival good for first-time cruisers?","Yes. Short 4 and 5 night sailings are an easy, low-cost way to try cruising, and the casual atmosphere and included dining make it simple to learn.")],
 [article_node("Carnival Cruise Line: is it right for you?","What a Carnival cruise costs in 2027, what is included, what costs extra, and who the line fits.","https://wonderlocity.com/cruises/carnival-cruise-line-review/")],
 [("All cruise guides","/cruises/"),("Carnival ships guide","/cruises/carnival-ships-guide/"),("Carnival Caribbean itineraries","/cruises/carnival-caribbean-itineraries/"),("Royal Caribbean vs Carnival","/guides/royal-caribbean-vs-carnival/"),("Plan with me","/plan/")],
 None)

# ---- Article 2: Carnival ships guide ----
rich_page("cruises/carnival-ships-guide/index.html","https://wonderlocity.com/cruises/carnival-ships-guide/",
 [("Home","/"),("Cruises","/cruises/"),("Carnival ships guide",None)],"Carnival ships explained: which class fits your trip","cr-ships",
 "Carnival Ships Explained: Every Class and Which to Pick | Wonderlocity",
 "Carnival runs more than two dozen ships. See how Excel, Vista, Dream, Conquest, and older classes compare, and which one fits your trip.",
 "Carnival runs more than two dozen ships in several classes, and the newest Excel-class ships, Mardi Gras, Carnival Celebration, and Carnival Jubilee, carry the biggest attractions in the fleet, while older classes like Conquest and Fantasy cost less and suit shorter, simpler trips.",
 """{{FACTS|Newest ships=Excel class: Mardi Gras, Celebration, Jubilee;Biggest attractions=Excel class;Budget-friendly=Dream and Conquest classes;Lowest prices=Sunshine and Fantasy classes}}<p>Two Carnival cruises can feel like different vacations depending on which ship you board. A 2023 megaship has a roller coaster, a huge water park, and a dozen places to eat. A 1998 ship has a pool, a show lounge, and a lower price. Neither is wrong, but picking blind is the mistake that leaves first-timers disappointed. Here is how the fleet breaks down, from newest to oldest.</p>
<h2>The fleet at a glance</h2><table class='costtable'><tr><td>Excel (2021 to 2023)</td><td>Mardi Gras, Carnival Celebration, Carnival Jubilee</td></tr>
<tr><td>Venice</td><td>Carnival Venezia, Carnival Firenze</td></tr>
<tr><td>Vista (2016 to 2019)</td><td>Carnival Vista, Horizon, Panorama</td></tr>
<tr><td>Dream (2009 to 2012)</td><td>Carnival Dream, Magic, Breeze</td></tr>
<tr><td>Conquest (2002 to 2007)</td><td>Conquest, Glory, Valor, Liberty, Freedom</td></tr>
<tr><td>Spirit (2001 to 2004)</td><td>Spirit, Pride, Legend, Miracle, Luminosa</td></tr>
<tr><td>Sunshine</td><td>Carnival Sunshine, Sunrise, Radiance</td></tr>
<tr><td>Fantasy (1998)</td><td>Carnival Elation, Carnival Paradise</td></tr></table>
<h2>Excel class: the newest and biggest</h2><p>Mardi Gras arrived in 2021, Carnival Celebration in 2022, and Carnival Jubilee in 2023, and they are the largest ships Carnival has built, with Mardi Gras carrying up to about 6,500 guests at full occupancy. Most Excel ships carry the BOLT roller coaster on the top deck, along with the biggest dining and entertainment lineups in the fleet. Two more are coming: Carnival Festivale in spring 2027, which will swap the roller coaster for a larger water park, and Carnival Tropicale in spring 2028. Carnival Celebration is based in Miami on 7-day Caribbean sailings, and Mardi Gras sails from Port Canaveral, moving to shorter Bahamas cruises from late May 2027. Expect the highest fares in the fleet, and book early for school holidays.</p>
<h2>Venice class: a different feel</h2><p>Carnival Venezia and Carnival Firenze joined the fleet from sister brand Costa, so they feel a little different from a classic Carnival ship. Read recent reviews for the exact ship and sailing before you book.</p>
{{FIG|cr-bigship|Ship size and age change the whole trip, from pool decks to dining.}}<h2>Vista class: the sweet spot</h2><p>Carnival Vista (2016), Carnival Horizon (2018), and Carnival Panorama (2019) carry about 4,000 guests each, with Panorama at 4,008 and Horizon at 3,960. They are big, modern, and full of attractions, yet they usually cost less than the Excel ships, which makes Vista class the best value for a family that wants a lot of ship without the top price.</p>
<h2>Dream class: solid and mid-sized</h2><p>Carnival Dream (2009), Carnival Magic (2011), and Carnival Breeze (2012) are popular mid-sized ships. Magic and Breeze carry about 3,690 guests. They are comfortable, well-proven ships with good pool decks and dining, and they are a safe middle choice on both price and features.</p>
<h2>Conquest and Spirit classes: older and cheaper</h2><p>The five Conquest-class ships, built between 2002 and 2007, carry roughly 3,000 guests each, and Carnival Freedom (2007, about 2,980 guests) will take over the Norfolk homeport in May 2027. The Spirit-class ships, Spirit, Pride, Legend, and Miracle, are smaller still, with Pride and Legend at about 2,124 guests, plus Carnival Luminosa, which came from Costa. These ships have fewer attractions and a more traditional layout, and that shows up as lower fares and a calmer feel.</p>
{{FIG|cr-day|Older ships trade the biggest attractions for a lower fare.}}<h2>Sunshine and Fantasy classes: the lowest prices</h2><p>The Sunshine class is made up of older ships that were renovated and renamed: Carnival Sunshine was originally Carnival Destiny, launched in 1996, Carnival Sunrise was Carnival Triumph, and Carnival Radiance was Carnival Victory. Carnival Sunshine spent a month in dry dock before it began sailing from Norfolk, Virginia in February 2025. The Fantasy class, Carnival Elation and Carnival Paradise from 1998, is among the oldest and most compact in the fleet, with Elation carrying about 2,130 guests. These suit short getaways and shoppers who put price first.</p>
{{TIP|Check the exact ship|Class is a good guide, but each ship has its own refits and sailings, so read recent reviews for the exact ship and sailing before you book.}}<h2>So which ship should you pick?</h2><p>Match the ship to your group. Families with older kids and teens should lean toward Excel and Vista, where the attractions keep everyone busy. Couples and groups watching their budget do well on Dream and Conquest. First-timers testing a 4 or 5 night sailing can start on an older ship and upgrade later. Whatever the class, check the homeport first, because a ship you can drive to saves a flight, and our <a href='/cruises/carnival-caribbean-itineraries/'>Carnival Caribbean itineraries guide</a> shows where each ship sails. For what a cruise costs once you add extras, see the <a href='/cruises/carnival-cruise-line-review/'>Carnival cost review</a>.</p>"""
 + cruise_panel(),
 [("What is the newest Carnival ship?","Carnival Jubilee, built in 2023, is the newest Excel-class ship in service. Carnival Festivale is due in spring 2027 and Carnival Tropicale in spring 2028."),
  ("Which Carnival ships are the biggest?","The Excel-class ships, Mardi Gras, Carnival Celebration, and Carnival Jubilee. Mardi Gras holds up to about 6,500 guests at full occupancy."),
  ("Does the ship really matter on Carnival?","Yes. Newer ships have far larger attractions and more dining choices, and older ships cost less. Pick the ship before the cabin."),
  ("Which Carnival ship sails from Norfolk?","Carnival Sunshine sails from Norfolk, Virginia through mid-May 2027, and Carnival Freedom replaces it from May 15, 2027.")],
 [article_node("Carnival ships explained: which class fits your trip","Every Carnival ship class, from the newest Excel ships to the older Fantasy class, and which fits your trip.","https://wonderlocity.com/cruises/carnival-ships-guide/")],
 [("All cruise guides","/cruises/"),("Carnival cost review","/cruises/carnival-cruise-line-review/"),("Carnival Caribbean itineraries","/cruises/carnival-caribbean-itineraries/"),("First Caribbean cruise","/guides/caribbean-cruise-first-timer/"),("Plan with me","/plan/")],
 None)

# ---- Article 3: Carnival Caribbean itineraries ----
rich_page("cruises/carnival-caribbean-itineraries/index.html","https://wonderlocity.com/cruises/carnival-caribbean-itineraries/",
 [("Home","/"),("Cruises","/cruises/"),("Carnival Caribbean itineraries",None)],"Carnival Caribbean cruises: itineraries, ports, and where to sail from","cr-itin",
 "Carnival Caribbean Cruises: Itineraries and Ports | Wonderlocity",
 "Carnival sails the Caribbean and Bahamas from Miami, Port Canaveral, and Norfolk. See itineraries, private destinations, and which port saves airfare.",
 "Carnival sails the Caribbean and Bahamas from ports including Miami, Port Canaveral, and Norfolk, Virginia, on 4 to 7 night itineraries that stop at ports like Nassau, Cozumel, St. Thomas, and Carnival's own Celebration Key, and the best choice is usually the port you can drive to.",
 """{{FACTS|Shortest first cruise=4 to 5 night Bahamas;Beach days=Western Caribbean via Cozumel;Closest to Orlando=Port Canaveral;Drive from Virginia=Norfolk}}<p>The itinerary decides what your cruise feels like, and the departure port decides what it costs to get there. Carnival covers the Caribbean from several US ports, so the useful question is not which island is best but which sailing fits your time, your budget, and your drive. Here is how the main options work.</p>
<h2>Bahamas, Eastern, and Western Caribbean</h2><p>Carnival's Caribbean sailings fall into three groups. Bahamas cruises are the shortest, usually 4 or 5 nights, with stops like Nassau and Carnival's own beach destinations, which makes them the easiest first cruise. Eastern Caribbean sailings run about a week and call at ports such as St. Thomas, St. Maarten, San Juan, Grand Turk, and Amber Cove in the Dominican Republic, which suits travelers who like shopping and variety. Western Caribbean sailings call at places like Cozumel in Mexico, and they suit snorkeling, ruins, and beach days.</p>
{{FIG|cr-beach|Beach time is the reason many people pick a short Bahamas sailing.}}<h2>Carnival's private Bahamas destinations</h2><p>Two stops are worth knowing by name. Celebration Key is Carnival's newer exclusive destination on Grand Bahama, and Half Moon Cay, which Carnival now brands as RelaxAway, Half Moon Cay, is its long-running private island. Visits to both are part of your fare with no extra charge to go ashore, though some activities, food, and drinks there may cost extra. They are the reason a short Bahamas sailing can feel like a full beach vacation.</p>
{{FIG|cr-port|Nassau, Bahamas, is a port on many Caribbean itineraries.}}<h2>Sailing from Miami</h2><p>Carnival Celebration is based in PortMiami on 7-day Eastern and Western Caribbean itineraries, according to Carnival's published 2027 and 2028 schedule. Eastern routes include Celebration Key, Amber Cove, Grand Turk, St. Thomas, St. Maarten, San Juan, RelaxAway, Half Moon Cay, and Nassau, and Western routes include Celebration Key and Cozumel. Miami has the most flights and the widest choice of sailings, so it is the best port if you are flying in.</p>
<h2>Sailing from Port Canaveral</h2><p>Port Canaveral, on Florida's east coast, is the cruise port closest to Orlando, which makes it easy to pair a cruise with theme parks. Mardi Gras sails from here, and from late May 2027 it moves to 4 and 5 day Bahamas cruises calling at Celebration Key, RelaxAway, Half Moon Cay, and Nassau depending on the length. If you are building a Disney or Universal trip too, see our <a href='/guides/orlando-on-a-budget/'>Orlando on a budget guide</a>.</p>
<h2>Sailing from Norfolk, Virginia</h2><p>For anyone in Virginia, the Carolinas, or the Mid-Atlantic, Norfolk is the shortcut, because you drive to the ship and skip the airfare. Carnival began year-round sailings from Norfolk's Half Moone Cruise Center in February 2025 with Carnival Sunshine, and its schedule includes the Bahamas, Bermuda, and the Eastern Caribbean. Carnival scheduled Sunshine to add Celebration Key to its calls from September 2025. Carnival Sunshine runs through mid-May 2027, and Carnival Freedom replaces it from May 15, 2027 with 33 cruises that Carnival says will include the Bahamas, Bermuda, the Eastern Caribbean, and Canada. As a price sample, a 6-day Bermuda sailing from Norfolk in September 2025 priced at $782 for an inside cabin and $1,259 for a balcony. Budget for terminal parking on top of the fare.</p>
{{FIG|cr-lagoon|Clear water and easy beach days are what most people picture when they book.}}<h2>Which sailing to pick</h2><table class='costtable'><tr><td>First cruise, short and cheap</td><td>4 to 5 night Bahamas</td></tr>
<tr><td>Beach and snorkeling days</td><td>Western Caribbean via Cozumel</td></tr>
<tr><td>Shopping and island variety</td><td>Eastern Caribbean</td></tr>
<tr><td>Pair with Orlando parks</td><td>Port Canaveral</td></tr>
<tr><td>Skip the flight from Virginia</td><td>Norfolk</td></tr></table>
{{TIP|Drive if you can|If you live within driving distance of Norfolk, a drive-to sailing skips the airfare, which can change which cruise is the better deal.}}<h2>When to go</h2><p>Hurricane season runs from June to November, and fares are often lower then, with itineraries sometimes changed to dodge storms. Winter is peak season with the highest fares. Our <a href='/guides/caribbean-cruise-first-timer/'>first Caribbean cruise guide</a> covers timing in more detail, and the <a href='/cruises/carnival-ships-guide/'>Carnival ships guide</a> helps you pick the ship that sails your route. Schedules and ship assignments change, so confirm the details on Carnival's site before you book.</p>"""
 + cruise_panel(),
 [("Does Carnival sail from Norfolk, Virginia?","Yes. Carnival Sunshine has sailed year-round from Norfolk since February 2025, and Carnival Freedom takes over from May 15, 2027."),
  ("What is the best Carnival itinerary for a first cruise?","A 4 or 5 night Bahamas sailing. It is short, inexpensive, and includes a beach day at a Carnival destination such as Celebration Key."),
  ("Is Celebration Key free to visit?","Going ashore is included in your cruise fare. Some food, drinks, and activities there cost extra."),
  ("Which Carnival port is closest to Orlando?","Port Canaveral, on Florida's east coast, is the cruise port closest to Orlando's theme parks.")],
 [article_node("Carnival Caribbean cruises: itineraries, ports, and where to sail from","Carnival Caribbean and Bahamas itineraries from Miami, Port Canaveral, and Norfolk, with private destinations and port tips.","https://wonderlocity.com/cruises/carnival-caribbean-itineraries/")],
 [("All cruise guides","/cruises/"),("Carnival cost review","/cruises/carnival-cruise-line-review/"),("Carnival ships guide","/cruises/carnival-ships-guide/"),("Cruise packing list","/essentials/cruise-packing-list/"),("Plan with me","/plan/")],
 None)

# ---- Cruises hub page ----
_cr_cards = [
 ("Carnival Cruise Line: is it right for you?","/cruises/carnival-cruise-line-review/","cr-review","From about $105 a night","Cabin prices, what is included, what costs extra, and who Carnival fits."),
 ("Carnival ships explained","/cruises/carnival-ships-guide/","cr-ships","","Every ship class from the newest Excel ships to the oldest, and which to pick."),
 ("Carnival Caribbean itineraries","/cruises/carnival-caribbean-itineraries/","cr-itin","","Bahamas, Eastern, and Western sailings from Miami, Port Canaveral, and Norfolk."),
 ("First Caribbean cruise guide","/guides/caribbean-cruise-first-timer/","wlguide8","From about $700 per person, week","Costs, what is included, and the tips first-timers wish they knew."),
 ("Royal Caribbean vs Carnival vs Norwegian","/guides/royal-caribbean-vs-carnival/","wlguide9","","Which line fits your group, budget, and style."),
 ("Cruise packing list","/essentials/cruise-packing-list/","wlessguide2","","What first-timers forget, and what the cabin lacks."),
 ("What a Caribbean cruise costs","/trip-types/cruise/","wl-cr-hero","From about $700 per person, week","The fare is only part of the bill. See the extras that decide your real total.")]
_cr_crumbs = [("Home","/"),("Cruises",None)]
_cr_body = phero("cr-hub",_cr_crumbs,"Cruises") + '<section class="section"><div class="wrap">' + CARD_CSS
_cr_body += ('<div class="narrow" style="padding:0"><p class="answer">A week on a Caribbean cruise starts from about $700 per person in 2026 before gratuities, drinks, and excursions, and the line, the ship, and the port you sail from decide where in that range you land.</p>'
 '<p>Start with the cost guide, then pick a line, then pick a ship and an itinerary. The Carnival guides below are the first in a growing cruise section built around one question: what will this cruise really cost, and is it worth it for you.</p></div>')
_cr_body += '<div class="grid3">'
for nm,url,cseed,price,blurb in _cr_cards:
    _cr_body += ('<article class="lcard"><a href="'+url+'"><div class="ph" style="background-image:url(\''+img_url(cseed,800,600)+'\')"></div></a>'
        '<div class="b"><h3>'+nm+'</h3>'+('<div class="price">'+price+'</div>' if price else '')+'<p>'+blurb+'</p>'
        '<a class="r" href="'+url+'">Read more</a></div></article>')
_cr_body += '</div><div class="narrow" style="padding:0">' + advisory + '</div></div></section>'
page("cruises/index.html","Cruises: Costs, Lines, Ships, and Itineraries | Wonderlocity",
 "Honest cruise cost guides for Caribbean and Bahamas sailings, with Carnival ship, itinerary, and price breakdowns and tips for first-timers.",
 "https://wonderlocity.com/cruises/", _cr_body,
 {"@context":"https://schema.org","@graph":[breadcrumb_schema(_cr_crumbs)]})


REAL_IMAGES.update({
    "fam-vb-hero": "https://images.unsplash.com/photo-1777138653711-f59e274de4e4?fm=jpg&q=80&fit=crop",
    "fam-vb-umbrella": "https://images.unsplash.com/photo-1531129630896-1744cab0cafd?fm=jpg&q=80&fit=crop",
    "fam-vb-fish": "https://images.unsplash.com/photo-1636045466232-539c7bd7817e?fm=jpg&q=80&fit=crop",
    "fam-vb-trail": "https://images.unsplash.com/photo-1539920951450-2b2d59cff66d?fm=jpg&q=80&fit=crop",
    "fam-vb-water": "https://images.unsplash.com/photo-1739295194212-0602c4d1e797?fm=jpg&q=80&fit=crop",
    "fam-norfolk-hero": "https://images.unsplash.com/photo-1638287527782-56569934c034?fm=jpg&q=80&fit=crop",
    "fam-nf-pier": "https://images.unsplash.com/photo-1721122964936-b0ab03e6dbbd?fm=jpg&q=80&fit=crop",
    "fam-nf-slide": "https://images.unsplash.com/photo-1770330514127-f23131508ebb?fm=jpg&q=80&fit=crop",
    "fam-nf-beach": "https://images.unsplash.com/photo-1475503572774-15a45e5d60b9?fm=jpg&q=80&fit=crop",
    "fam-pack-hero": "https://images.unsplash.com/photo-1555446099-555959e43ecf?fm=jpg&q=80&fit=crop",
    "fam-pack-flat": "https://images.unsplash.com/photo-1541341584401-605c9cf3537e?fm=jpg&q=80&fit=crop",
    "fam-pack-beach": "https://images.unsplash.com/photo-1759559585493-8f3a10cec180?fm=jpg&q=80&fit=crop",
    "fam-road-hero": "https://images.unsplash.com/photo-1761047321481-abbdcfb7ff00?fm=jpg&q=80&fit=crop",
    "fam-road-window": "https://images.unsplash.com/photo-1756142008330-87dc106322a4?fm=jpg&q=80&fit=crop",
    "fam-road-savannah": "https://images.unsplash.com/photo-1780348545647-0498a42c3b38?fm=jpg&q=80&fit=crop",
    "fam-du-hero": "https://images.unsplash.com/photo-1789758612499-dc1ede632152?fm=jpg&q=80&fit=crop",
    "fam-du-carousel": "https://images.unsplash.com/photo-1601930113377-729966035f34?fm=jpg&q=80&fit=crop",
    "fam-du-rides": "https://images.unsplash.com/photo-1761242606389-0a45db29fdee?fm=jpg&q=80&fit=crop",
})

# ===== Five family articles (added Nov 2026) =====
_FAMCR = [("Home","/"),("Family trips","/family/")]
_UPD = "<p><em>Details last checked in November 2026. Prices and hours change, so confirm them before you go.</em></p>"

# ---- 1. Things to do with kids in Virginia Beach ----
rich_page("guides/things-to-do-with-kids-virginia-beach/index.html","https://wonderlocity.com/guides/things-to-do-with-kids-virginia-beach/",
 _FAMCR+[("Things to do with kids in Virginia Beach",None)],"Things to do with kids in Virginia Beach","fam-vb-hero",
 "Things to Do With Kids in Virginia Beach (Beyond the Beach) | Wonderlocity",
 "Kid-tested ideas for Virginia Beach: the aquarium, First Landing State Park, a water park, treetop courses, and rainy-day plans for every age.",
 "Virginia Beach works for kids of every age because the beach is only the start: there is a big aquarium, a state park with 19 miles of trails, a 30-attraction water park, treetop courses, and indoor options for rainy days.",
 """{{FACTS|Best for=Ages 3 to 12, and teens too;Beach and boardwalk=Free to enjoy;Rainy day=Aquarium, Apex, aviation museum;Plan on=2 to 4 days}}<p>Most families come to Virginia Beach for the sand and then discover how much else fits around it. You can swim before lunch, watch sharks after, and be on a forest trail by late afternoon, all without a long drive. Here is how to mix it up so nobody gets bored, and what to save for the days the weather does not cooperate.</p>
<h2>Start with the beach and boardwalk</h2><p>The beach and the Boardwalk cost nothing to enjoy, which makes them the easy anchor for every day. The Boardwalk is good for biking and strolling, so it is an easy evening walk after a beach day. For little ones, Grommet Island Park is an ocean-themed playground steps from the sand, designed for children of all abilities.</p>
{{FIG|fam-vb-umbrella|Plan the beach for mornings, then spend the hot middle of the day somewhere shaded or indoors.}}
<h2>See sharks and rays at the Virginia Aquarium</h2><p>The Virginia Aquarium and Marine Science Center is the classic move for any weather. It has more than a dozen species of shark, ray, eel and reptile, plus live animal encounters, and it suits kids of all ages. Go early on a hot or rainy day, and check current tickets and hours before you head over.</p>
{{FIG|fam-vb-fish|An aquarium visit works for a toddler and a ten-year-old on the same ticket.}}
<h2>Walk it off at First Landing State Park</h2><p>First Landing is called Virginia's most visited state park, with 19 miles of all-ages terrain and 1.25 miles of Chesapeake Bay coastline. It is the right answer when the kids have had enough screens and sand, and you want a flat walk that nobody complains about.</p>
{{FIG|fam-vb-trail|Pick an easy trail first, and let the kids decide if they want a longer one.}}
{{TIP|Pack for the park|Bring bug spray, water, and a snack. A short, easy trail that ends with a beach stop beats a long hike for most kids.}}
<h2>Splash at Ocean Breeze Waterpark</h2><p>Ocean Breeze has more than 30 attractions, including water slides, aquatic playgrounds, a wave pool, and a lazy river called Adventure River. It is a good day for mixed ages, because there is shallow play for the small ones and bigger slides for everyone else.</p>
{{FIG|fam-vb-water|A water park day covers kids who are tired of waves and want slides.}}
<h2>Rainy days and big-kid energy</h2><p>When it pours, Apex Entertainment brings indoor ropes courses and go-karts. The Military Aviation Museum shows off about 70 planes restored to flying condition, which is a hit with plane fans of any age. The Cape Henry Lighthouse, built in 1792, has 191 narrow, winding steps, so decide if your kids are ready for the climb.</p>
<h2>Farms, treetops, and wildlife</h2><p>Hunt Club Farm is a family-run 50 acres with a petting farm and a TreeWalk Adventure. The Adventure Park at Virginia Beach is another treetop option for kids who like climbing. Back Bay National Wildlife Refuge is a quieter pick for wildlife viewing.</p>
<h2>A simple three-day plan</h2><table class='costtable'><tr><td>Day 1</td><td>Beach morning, Boardwalk walk in the evening</td></tr>
<tr><td>Day 2</td><td>Virginia Aquarium, then Grommet Island Park</td></tr>
<tr><td>Day 3</td><td>First Landing State Park or Ocean Breeze, depending on the weather</td></tr></table>
<p>Keep one flexible day for rain or tired kids, and book the aquarium or water park for the day with the best forecast.</p>
<h2>Where to stay</h2><p>Staying near the oceanfront means you can walk to the beach and the Boardwalk and skip the car on most evenings. If you want a bigger space for the family, look for a suite or condo with a kitchenette, since breakfasts and snacks add up fast.</p>"""+_UPD+"""""",
 [("What is the best thing to do with kids in Virginia Beach?","Start with the beach and Boardwalk, which are free to enjoy, and add the Virginia Aquarium and First Landing State Park. Together they cover water, animals, and an easy walk."),
  ("What can we do in Virginia Beach when it rains?","Try the Virginia Aquarium, Apex Entertainment for indoor ropes and go-karts, or the Military Aviation Museum, which has about 70 planes restored to flying condition."),
  ("Is Virginia Beach good for toddlers?","Yes. Grommet Island Park is an ocean-themed playground by the sand, and the aquarium and the beach both work well for small children.")],
 [article_node("Things to do with kids in Virginia Beach","Beach, aquarium, parks, a water park, and rainy-day plans for families in Virginia Beach.","https://wonderlocity.com/guides/things-to-do-with-kids-virginia-beach/")],
 [("All family trips","/family/"),("Weekend getaways from Virginia Beach","/guides/weekend-getaways-from-virginia-beach/"),("Williamsburg weekend","/guides/williamsburg-weekend/"),("Outer Banks weekend","/guides/outer-banks-weekend/"),("Free planning chat","/contact/")],
 "Virginia Beach")

# ---- 2. Carnival from Norfolk with kids ----
rich_page("cruises/carnival-from-norfolk-with-kids/index.html","https://wonderlocity.com/cruises/carnival-from-norfolk-with-kids/",
 [("Home","/"),("Cruises","/cruises/"),("Carnival from Norfolk with kids",None)],"Carnival from Norfolk with kids: a cruise with no flight","fam-norfolk-hero",
 "Carnival From Norfolk With Kids: Cruise Without Flying | Wonderlocity",
 "Drive to a Carnival cruise from Norfolk, Virginia. Parking costs, which ship sails, kids clubs, and a packing plan for families.",
 "Carnival sails year-round from Norfolk, Virginia, so a Virginia Beach family can drive to the ship, skip the airfares, and park for $15 a day, with Carnival Sunshine through mid-May 2027 and Carnival Freedom after that.",
 """{{FACTS|Ship now=Carnival Sunshine until mid-May 2027;Ship after=Carnival Freedom from May 15, 2027;Parking=$15 per day, free shuttle;Kids club=Camp Ocean, ages 2 to 11}}<p>The best part of cruising from Norfolk is what you leave out: no flights, no checked-bag fees, no rental car at the other end. You pack the car, drive to the ship, and walk on. For a family of four, that can change which cruise is the better deal, and it makes a short Bahamas or Eastern Caribbean sailing much easier to try.</p>
<h2>Which ship you will sail on</h2><p>Carnival Sunshine has been Norfolk's ship and stays through mid-May 2027, finishing 21 cruises before it moves on. It entered service in 1996 as Carnival Destiny and was rebuilt and renamed in 2013. Carnival Freedom arrives on May 15, 2027 and runs 33 cruises from Norfolk for the rest of that year. It carries about 3,000 guests and entered service in 2006. For 2027, Carnival lists Bahamas, Bermuda, Eastern Caribbean, and Canada sailings from Norfolk, so check which itinerary and length fits your school break.</p>
{{FIG|fam-nf-pier|Ships dock at the Half Moone Cruise Terminal in downtown Norfolk, a short drive from Virginia Beach.}}
<h2>Parking, step by step</h2><p>The Half Moone Cruise Terminal is at 1 Waterside Drive in downtown Norfolk. The City of Norfolk lists Cedar Grove parking at 1000 Monticello Avenue, about 1.5 miles away, at $15 per day, and you can pre-pay or pay on entry by cash or card. A free shuttle takes you to the terminal, and you can check your luggage at the lot so it goes straight to the ship. On cruise days the lot opens at 9:30 a.m., shuttles start around 9:45 a.m., and the last shuttle runs at 2:30 p.m. If you would rather skip parking, drop-off is on Waterside Drive.</p>
<table class='costtable'><tr><td>Parking, 7-night cruise</td><td>about $105 to $120</td></tr>
<tr><td>Gratuities</td><td>about $119 per person for a week</td></tr>
<tr><td>Flights for the family</td><td>$0, you drive</td></tr></table>
{{TIP|Do the real math|Parking runs $15 a day, so a week costs about $105 to $120. Compare that with four airfares plus bags to a Florida port. Add gratuities to any fare you compare.}}
<h2>What kids do on board</h2><p>Carnival's kids program, Camp Ocean, is included in the cruise fare and starts at age 2. It splits kids into Penguins (2 to 5), Stingrays (6 to 8), and Sharks (9 to 11). A late-evening option called Night Owls has a fee. Our <a href='/cruises/carnival-ships-guide/'>Carnival ships guide</a> explains how older and newer ships differ, which matters when you choose between Sunshine and Freedom.</p>
{{FIG|fam-nf-slide|Pool and slide time is the main event for most kids at sea.}}
<h2>Before you go</h2><p>Every traveler, kids included, needs proper travel documents at embarkation, and guests without them cannot board, so confirm Carnival's current rules for your group. Carnival also prohibits all speakers, including Bluetooth, and holds them until the cruise ends, so leave the kids' speakers at home. Our <a href='/essentials/family-cruise-packing-list/'>family cruise packing list</a> has a printable checklist.</p>
<h2>Make a day of Norfolk</h2><p>Nauticus, the maritime museum on the terminal campus beside the USS Wisconsin, offers cruise passengers buy-one-get-one-free admission. It is a good use of an early arrival or a post-cruise afternoon.</p>
{{FIG|fam-nf-beach|Bahamas and Eastern Caribbean itineraries bring beach days within a short sail from the Mid-Atlantic.}}"""+_UPD+"""""",
 [("Does Carnival sail from Norfolk, Virginia?","Yes. Carnival Sunshine sails from Norfolk through mid-May 2027, and Carnival Freedom takes over from May 15, 2027."),
  ("How much is parking at the Norfolk cruise terminal?","The city lists Cedar Grove parking at $15 per day, with a free shuttle to the terminal. Confirm current rates and shuttle times before your cruise."),
  ("What is the kids club on Carnival?","Camp Ocean, included in the fare, for ages 2 to 11: Penguins (2 to 5), Stingrays (6 to 8), and Sharks (9 to 11).")],
 [article_node("Carnival from Norfolk with kids","Carnival cruises from Norfolk for families: ships, parking, kids clubs, and what to pack.","https://wonderlocity.com/cruises/carnival-from-norfolk-with-kids/")],
 [("All cruise guides","/cruises/"),("All family trips","/family/"),("Carnival Caribbean itineraries","/cruises/carnival-caribbean-itineraries/"),("Carnival cost review","/cruises/carnival-cruise-line-review/"),("Family cruise packing list","/essentials/family-cruise-packing-list/"),("Free planning chat","/contact/")],
 "Caribbean cruises")

# ---- 3. Family cruise packing list (printable) ----
rich_page("essentials/family-cruise-packing-list/index.html","https://wonderlocity.com/essentials/family-cruise-packing-list/",
 [("Home","/"),("Family trips","/family/"),("Family cruise packing list",None)],"Family cruise packing list (with printable checklist)","fam-pack-hero",
 "Family Cruise Packing List: Printable Checklist for Kids | Wonderlocity",
 "A printable family cruise packing checklist: documents, carry-on, kids' items, cabin helpers, and what to leave at home.",
 "A family cruise packing list should cover documents, a first-day carry-on, kids' items, and a few cabin helpers, and it should leave out speakers and anything the cruise line prohibits.",
 """<style>.check ul{list-style:none;padding-left:0}.check li{padding:7px 0 7px 32px;position:relative;border-bottom:1px solid var(--line)}.check li:before{content:'';position:absolute;left:0;top:10px;width:16px;height:16px;border:2px solid var(--green);border-radius:4px}@media print{header.site,footer.site,.phero,.panel,.related,.ctaband,.faq,.fig,.noprint,.answer,.tip,.facts{display:none!important}.check li{break-inside:avoid}}</style>{{FACTS|Use it for=Any family cruise;Print it=Button below;Pack first=Documents and carry-on;Leave home=Speakers and prohibited items}}<p>Packing for a cruise with kids is mostly about three bags: the one you carry, the ones that arrive at the cabin later, and the little one with everything the kids will ask for in the first hour. Use this list, print it, and tick items off as they go in.</p>
<p class='noprint'><button class='btn btn-green' type='button' onclick='window.print()'>Print this checklist</button></p>
{{FIG|fam-pack-flat|Lay everything out first, then pack the carry-on before anything else.}}
<div class='check'>
<h2>Documents and money</h2><ul><li>Passports or travel documents for every traveler, kids included</li><li>Boarding documents and luggage tags from online check-in</li><li>A card and a little cash for tips and small purchases</li><li>Copies of key documents, kept separate from the originals</li></ul>
<h2>Carry-on for day one</h2><ul><li>Swimsuits and cover-ups for everyone</li><li>Sunscreen and hats</li><li>One change of clothes per person</li><li>Any medicine, in its original packaging</li><li>Phone chargers and a portable battery</li><li>Snacks and a refillable water bottle for the walk to the ship</li></ul>
<h2>For the kids</h2><ul><li>Swim gear, goggles, and a quick-dry towel</li><li>A small backpack for pool and shore days</li><li>Cards, a travel game, or a small toy for dining room waits</li><li>A comfort item for bedtime</li><li>Swim diapers if you have a baby or toddler (check the pool rules)</li></ul>
<h2>Clothes</h2><ul><li>Shorts, t-shirts, and flip-flops for most days</li><li>One or two dressier outfits for the optional dressy nights</li><li>A light jacket or sweater for cool evenings and strong air conditioning</li><li>Comfortable shoes for shore days</li></ul>
<h2>Cabin helpers</h2><ul><li>A small laundry bag</li><li>A few clips or hooks for towels and swimsuits</li><li>Wet wipes and hand sanitizer</li><li>A night light for the cabin</li></ul>
<h2>Before you go</h2><ul><li>Download the cruise line app and book excursions and dinners early</li><li>Check the prohibited items list for anything with a plug, such as power strips</li><li>Leave speakers at home</li><li>Charge devices the night before</li></ul>
</div>
{{TIP|Why the carry-on matters|Checked bags can reach the cabin late in the day. A carry-on with swimsuits and sunscreen lets the kids hit the pool right away.}}
<h2>Leave at home</h2><p>Carnival prohibits all speakers, including Bluetooth, and holds them until the cruise ends. The line also publishes a prohibited items list, so check it before you pack anything plug-in. Leave valuables at home too.</p>
{{FIG|fam-pack-beach|Pack for pool days and shore days, and let the kids carry their own small bag.}}
<p>For a longer, general list, see our <a href='/essentials/cruise-packing-list/'>cruise packing list</a>, and for itinerary ideas see <a href='/cruises/carnival-from-norfolk-with-kids/'>Carnival from Norfolk with kids</a>.</p>"""+_UPD+"""""",
 [("What should families pack in a cruise carry-on?","Swimsuits, sunscreen, one change of clothes, medicine, chargers, and snacks, so everyone can start vacation before the bags arrive."),
  ("What can you not bring on a Carnival cruise?","Carnival prohibits all speakers, including Bluetooth, and holds them until the cruise ends. The line also publishes a prohibited items list, so check it before you pack."),
  ("Do kids need passports for a cruise?","Every traveler needs proper travel documents at embarkation, and guests without them cannot board. Confirm the cruise line's current rules for each traveler.")],
 [article_node("Family cruise packing list","A printable packing checklist for families going on a cruise.","https://wonderlocity.com/essentials/family-cruise-packing-list/")],
 [("All family trips","/family/"),("Cruise packing list","/essentials/cruise-packing-list/"),("Carnival from Norfolk with kids","/cruises/carnival-from-norfolk-with-kids/"),("First Caribbean cruise","/guides/caribbean-cruise-first-timer/"),("Free planning chat","/contact/")],
 "Caribbean cruises")

# ---- 4. Road trip Virginia Beach to Orlando ----
rich_page("guides/road-trip-virginia-beach-to-orlando-with-kids/index.html","https://wonderlocity.com/guides/road-trip-virginia-beach-to-orlando-with-kids/",
 _FAMCR+[("Virginia Beach to Orlando road trip",None)],"Road trip from Virginia Beach to Orlando with kids","fam-road-hero",
 "Virginia Beach to Orlando Road Trip With Kids: Stops and Plan | Wonderlocity",
 "A family road trip from Virginia Beach to Orlando: about 769 miles, where to break the drive, kid-friendly stops, and how to keep the car calm.",
 "Virginia Beach to Orlando is about 769 miles and roughly 14.5 hours of driving, so most families split it into two days with an overnight in South Carolina or Georgia and add one or two kid-friendly stops.",
 """{{FACTS|Distance=About 769 miles;Drive time=About 14.5 hours, no stops;Best plan=Two days with one overnight;Good stops=Savannah, Walterboro, Fayetteville}}<p>Driving to Orlando from the Virginia Beach area is a long day, but it has real upsides for a family: you bring everything, you have a car when you get there, and you can turn the trip into a vacation of its own. The key is to treat it as two easy days rather than one hard one.</p>
<h2>The numbers</h2><p>The drive is about 769 miles and roughly 14.5 hours without stops, which is why a stop for the night makes the trip so much calmer. Most families take I-64 to I-95 south. Plan around meals, gas, and restroom breaks with kids, and add time for traffic near big cities.</p>
<h2>Where to break the drive</h2><p>Think of the trip in three chunks: a first leg through Virginia and North Carolina, a middle leg through South Carolina and Georgia, and a short last day into Florida. Families who prefer a shorter day two often sleep in Georgia or South Carolina, so the Orlando arrival comes before dinner.</p>
<h2>Kid-friendly stops along I-95</h2><table class='costtable'><tr><td>Fayetteville, NC</td><td>U.S. Army Airborne and Special Operations Museum, indoors</td></tr>
<tr><td>Walterboro, SC</td><td>Walterboro Wildlife Sanctuary, boardwalks and trails</td></tr>
<tr><td>Savannah, GA</td><td>Riverfront walk and The Pirates' House</td></tr>
<tr><td>Cape Canaveral, FL</td><td>Kennedy Space Center and Canaveral National Seashore</td></tr></table>
<p>In Fayetteville, the Army Airborne and Special Operations Museum is indoors, so it works in any weather. In Walterboro, the wildlife sanctuary has boardwalks and trails, which is a good way to stretch legs. In Savannah, walk the historic riverfront, and kids can climb the spiral staircase at The Pirates' House up to a pirate gift shop and restaurant. Near Cape Canaveral, Kennedy Space Center and Canaveral National Seashore, with 24 miles of undeveloped beach, are worth a detour if you have time.</p>
{{FIG|fam-road-savannah|Savannah's moss-draped oaks make a calm stop for a family that has spent hours in the car.}}
{{TIP|Make the first stop short|Pick a stop within two or three hours. It sets a relaxed pace and gives the kids a first win before the long middle stretch.}}
<h2>Keeping the car calm</h2><p>Pack snacks in a reachable bag, download shows and music before you leave, and bring a few games that need no screen. Give older kids a job, like tracking the map or choosing the next stop, and give younger ones a small surprise for each leg.</p>
{{FIG|fam-road-window|Window seats, snacks, and a plan for the next stop keep most road trips cheerful.}}
<h2>Drive or fly?</h2><p>Driving makes the most sense for a bigger family, for anyone who wants a car in Orlando, and for people who like a slower start to the vacation. Flying saves a day each way, so it fits a short trip better. Either way, read our <a href='/guides/orlando-on-a-budget/'>Orlando on a budget</a> guide before you book hotels and tickets.</p>"""+_UPD+"""""",
 [("How far is Virginia Beach from Orlando by car?","About 769 miles, or roughly 14.5 hours of driving without stops."),
  ("Can you drive from Virginia Beach to Orlando in one day?","It is possible, but it is a very long day with kids. Most families split it into two days with an overnight in South Carolina or Georgia."),
  ("What are good kid-friendly stops on the way to Orlando?","Fayetteville, North Carolina for the Army Airborne museum, Walterboro, South Carolina for the wildlife sanctuary, and Savannah, Georgia for the riverfront and The Pirates' House.")],
 [article_node("Road trip from Virginia Beach to Orlando with kids","Distance, stops, and a two-day plan for driving from Virginia Beach to Orlando with kids.","https://wonderlocity.com/guides/road-trip-virginia-beach-to-orlando-with-kids/")],
 [("All family trips","/family/"),("Orlando on a budget","/guides/orlando-on-a-budget/"),("Disney or Universal for ages 6 to 12","/guides/disney-vs-universal-kids-6-12/"),("Orlando guide","/destinations/orlando/"),("Free planning chat","/contact/")],
 "Orlando")

# ---- 5. Disney vs Universal for kids 6-12 ----
rich_page("guides/disney-vs-universal-kids-6-12/index.html","https://wonderlocity.com/guides/disney-vs-universal-kids-6-12/",
 _FAMCR+[("Disney or Universal for ages 6 to 12",None)],"Disney or Universal for kids ages 6 to 12","fam-du-hero",
 "Disney vs Universal for Kids 6 to 12: Which Fits Your Family | Wonderlocity",
 "Disney World or Universal Orlando for ages 6 to 12? A plain comparison of rides, height limits, crowds, and ticket prices from about $119.",
 "For ages 6 to 8, Disney World is usually the easier fit, and for ages 9 to 12 who like coasters, Universal Orlando is a serious contender, with one-day tickets starting from about $119 per person at both.",
 """{{FACTS|Ages 6 to 8=Disney is usually easier;Ages 9 to 12=Either works, Universal for thrill fans;Tickets=From about $119 per day;Days needed=8 to 10 for both resorts}}<p>If your kids are somewhere between 6 and 12, you are in the sweet spot: old enough for real rides, young enough that the magic still works. The better resort depends less on the age number and more on what your kids actually like.</p>
<h2>The short answer</h2><p>Younger kids in this range, around 6 to 8, usually do best at Disney, which has a lot of rides without height limits and many gentle attractions. Kids who are 9 and up are ready for Universal, especially if they love coasters, Harry Potter, or Nintendo. If your group is mixed, Disney is the safer first trip and Universal is the one to add later.</p>
{{FIG|fam-du-carousel|Classic carousel and gentle rides are where Disney tends to shine for younger kids.}}
<h2>Rides and height limits</h2><p>Disney skews toward all ages and all comfort levels. Universal skews toward intensity, and many headline rides have minimum heights or intense motion. One example is Harry Potter and the Battle at the Ministry at Epic Universe, which has a 48-inch minimum. Always check each ride's current height rule before you promise anything, and remember that both parks offer a rider switch, so one adult can stay with a smaller child.</p>
<h2>What it costs</h2><table class='costtable'><tr><td>Disney, one-day ticket</td><td>from about $119 per adult</td></tr>
<tr><td>Disney, one-day child ticket</td><td>from about $113</td></tr>
<tr><td>Universal Epic Universe, one day</td><td>from about $135 per adult</td></tr>
<tr><td>Universal, 3+ days, all four parks</td><td>from about $73 per day</td></tr></table>
{{TIP|How to read these prices|Theme park tickets change by date. A Tuesday in mid-September costs far less than a Saturday in late December, so price your exact dates before you decide.}}
<p>Child pricing generally covers ages 3 to 9 at both resorts, so a 10 to 12 year old is usually priced as an adult. Check the current ticket rules at checkout. Neither resort includes line-skipping in a standard ticket: Disney sells Lightning Lane separately, and Universal sells Express separately.</p>
{{FIG|fam-du-rides|Bigger rides and bigger crowds mean planning your day around a few must-do attractions.}}
<h2>Crowds and line-skipping</h2><p>Disney's Lightning Lane Multi Pass can help on busy days, especially at Magic Kingdom. Universal Express is worth considering at Epic Universe while crowds remain high. For both, weekdays in late August or early September are usually the easiest, and arriving early helps.</p>
<h2>How many days do you need?</h2><p>Disney has four parks and Universal has four, including Epic Universe and Volcano Bay. Doing both well takes about 8 to 10 days, with 4 to 5 at Disney and 2 to 3 at Universal, and Epic Universe needs at least one full day. If you have only a week, pick one resort and save the other for another year.</p>
<h2>Skip these for this age</h2><p>Universal's Halloween Horror Nights is not for kids under 12 or 13. If you visit in the fall, ask yourself honestly how your kids handle scary scenes.</p>
<h2>So which one?</h2><p>Choose Disney if your kids love characters, gentler rides, and shows. Choose Universal if they chase thrills and big worlds. Choose both if you can give the trip at least a week and a half. For a closer look at the younger end, see our <a href='/guides/disney-or-universal-toddlers/'>toddlers guide</a>, and for budget planning, see <a href='/guides/orlando-on-a-budget/'>Orlando on a budget</a>.</p>"""+_UPD+"""""",
 [("Is Disney or Universal better for a 7 year old?","Disney is usually the easier fit, with more rides without height limits and many gentle attractions."),
  ("Is Universal good for a 10 year old?","Yes, especially for kids who like coasters, Harry Potter, or Nintendo. Check each ride's height rule before you go."),
  ("How much do Disney and Universal tickets cost?","One-day tickets start from about $119 per person at both, and Epic Universe starts from about $135. Prices change by date, so check your exact days.")],
 [article_node("Disney or Universal for kids ages 6 to 12","Rides, height limits, crowds, and prices for choosing between Disney World and Universal Orlando with kids 6 to 12.","https://wonderlocity.com/guides/disney-vs-universal-kids-6-12/")],
 [("All family trips","/family/"),("Disney or Universal for toddlers","/guides/disney-or-universal-toddlers/"),("Orlando on a budget","/guides/orlando-on-a-budget/"),("Road trip to Orlando","/guides/road-trip-virginia-beach-to-orlando-with-kids/"),("Orlando guide","/destinations/orlando/"),("Free planning chat","/contact/")],
 "Orlando")


# ===== Florida and cruise articles, batch 2 (added Nov 2026) =====
_FLIM = {
"fl-pc-hero":"1719423324139-04edfa77ea0d","fl-pc-ship":"1717465760671-c47cb5f8b56f","fl-pc-launch":"1457364887197-9150188c107b","fl-pc-beach":"1745261394475-1ec45d960f7b",
"fl-mia-hero":"1535498730771-e735b998cd64","fl-mia-beach":"1589083130544-0d6a2926e519","fl-mia-ship":"1764609287343-7cb772b75c55","fl-mia-sea":"1724597402406-f2904a5bee40",
"fl-cmp-hero":"1707342617132-582a6bda20ff","fl-cmp-a":"1628503172677-7177af7aea9e","fl-cmp-b":"1596618452407-4a44d426717c",
"fl-fam-hero":"1685101260406-5c7ad28ca00b","fl-fam-pool":"1768270181731-b4234ef5c673","fl-fam-deck":"1667604963377-93dda0e11b1b","fl-fam-sunset":"1676407118683-f0060c12b94f",
"fl-orl-hero":"1758464642801-14bd789db153","fl-orl-gator":"1523917631658-047ed87b47fa","fl-orl-space":"1551871812-10ecc21ffa2f","fl-orl-green":"1609184889514-656548112551",
"fl-bch-hero":"1658157799932-eef5dee4118c","fl-bch-guard":"1512936702668-1ab037aced2a","fl-bch-light":"1708009241983-8ea0dc90c5d9","fl-bch-walk":"1654206700775-1c6257fb12e9",
"fl-dis-hero":"1570613141985-aefb384a573b","fl-dis-ship":"1707342616937-c30b896b7c27","fl-dis-deck":"1775145408468-ec55b208f645"}
REAL_IMAGES.update({k:"https://images.unsplash.com/photo-"+v+"?fm=jpg&q=80&fit=crop" for k,v in _FLIM.items()})
_CRCR = [("Home","/"),("Cruises","/cruises/")]
_RELX = [("Free planning chat","/contact/")]

# ---- Cruises from Orlando (Port Canaveral) ----
rich_page("cruises/cruises-from-orlando-port-canaveral/index.html","https://wonderlocity.com/cruises/cruises-from-orlando-port-canaveral/",
 _CRCR+[("Cruises from Orlando",None)],"Cruises from Orlando: the Port Canaveral guide","fl-pc-hero",
 "Cruises From Orlando (Port Canaveral): Lines, Parking, Transfers | Wonderlocity",
 "Orlando cruises sail from Port Canaveral, about 45 minutes away. Which lines go, Bahamas and Caribbean options, parking from $20 a day, and how to pair it with a park trip.",
 "Orlando does not have its own cruise port: ships leave from Port Canaveral, about 45 minutes east of Orlando International Airport, with Royal Caribbean, Norwegian, MSC, Carnival, Celebrity and Disney all sailing from there.",
 """{{FACTS|Port=Port Canaveral on the Space Coast;From Orlando airport=About 45 minutes;Parking=From $20 per day plus tax;Trips=3 to 14 nights}}<p>Port Canaveral is the easy way to combine a theme park trip with a cruise. You fly into Orlando, spend a few days at the parks, then ride east to the ship. Here is how it works and what to plan before you book.</p>
<h2>Which lines sail from Port Canaveral</h2><p>Cruise Critic lists Royal Caribbean (including Utopia of the Seas and Star of the Seas), Norwegian, MSC, Carnival, Celebrity and Disney, and Cunard also appears in the lineup. Disney has its own dedicated terminal, which makes the port a favorite for families. Ships and terminals change by season, so confirm yours with your travel advisor or the cruise line.</p>
{{FIG|fl-pc-ship|Several lines share the port, and each ship is assigned a terminal for its sailing day.}}
<h2>Where you can go</h2><table class='costtable'><tr><td>3 to 4 nights</td><td>Bahamas, with stops like Nassau, Perfect Day at CocoCay, and Great Stirrup Cay</td></tr>
<tr><td>7 nights</td><td>Eastern or Western Caribbean, such as St. Thomas, St. Maarten, Cozumel, Grand Cayman, and Ocho Rios</td></tr>
<tr><td>9 nights</td><td>Southern Caribbean, such as Antigua, Barbados, and St. Lucia</td></tr></table>
<p>Most sailings are seven nights. A short Bahamas cruise is the gentlest first try if you are adding it onto a Florida vacation.</p>
<h2>Getting to the port from Orlando</h2><p>The port says Orlando International Airport is about 45 minutes west of it, via the S.R. 528 toll road. Orlando Melbourne International is about 40 minutes south, and Orlando Sanford is about an hour northwest. Options for the ride include a rental car, a shuttle, a rideshare, a private car, and ground transfers some lines sell. Norwegian, for example, offers airport transfers on select sailings that must be booked at least four days ahead.</p>
<h2>Parking, if you drive</h2><p>The port charges $20 per day plus tax, covering the day you arrive and the day you leave. It does not take parking reservations, you pay on arrival, and cash is not accepted. Garages and lots sit next to the terminals, and parking opens at 10 a.m. on embarkation day. Rates can change, so check the port's page before you go.</p>
{{TIP|Arrive the day before|Flying in the morning of your cruise leaves no room for delays. A hotel night near the port or in Cocoa Beach is cheap insurance, and many hotels there offer shuttles.}}
<h2>Fun things before or after the ship</h2><p>Kennedy Space Center is about 20 minutes from the port. It has a Rocket Garden of full-size rockets, the Atlantis orbiter, and more than 60 interactive simulators. Cocoa Beach is about 15 minutes south, which makes it an easy beach day.</p>
{{FIG|fl-pc-launch|The Space Coast is rocket country, so a launch day can be part of your trip.}}
{{FIG|fl-pc-beach|Cocoa Beach is a short drive from the terminals.}}
<h2>Combining parks and a cruise</h2><p>A common plan is four or five days at the parks, a night near the coast, then a short Bahamas cruise. Read our <a href='/guides/disney-vs-universal-kids-6-12/'>Disney vs Universal guide</a> to choose the parks, and our <a href='/cruises/disney-cruise-from-port-canaveral/'>Disney cruise guide</a> if you want a Disney land and sea trip.</p>"""+_UPD,
 [("Can you cruise from Orlando?","Not directly. Ships sail from Port Canaveral, about 45 minutes east of Orlando International Airport."),
  ("How much is parking at Port Canaveral?","$20 per day plus tax, paid on arrival by card. The port does not take reservations or cash."),
  ("Which cruise lines sail from Port Canaveral?","Royal Caribbean, Norwegian, MSC, Carnival, Celebrity and Disney all sail from the port, and Cunard also appears in the lineup.")],
 [article_node("Cruises from Orlando: the Port Canaveral guide","Lines, itineraries, parking, and transfers for cruising from Port Canaveral near Orlando.","https://wonderlocity.com/cruises/cruises-from-orlando-port-canaveral/")],
 [("All cruise guides","/cruises/"),("Cruises from Miami","/cruises/cruises-from-miami/"),("Port Canaveral or Miami","/cruises/port-canaveral-vs-miami/"),("Disney cruise from Port Canaveral","/cruises/disney-cruise-from-port-canaveral/"),("Orlando on a budget","/guides/orlando-on-a-budget/")]+_RELX,
 "Caribbean cruises")

# ---- Cruises from Miami ----
rich_page("cruises/cruises-from-miami/index.html","https://wonderlocity.com/cruises/cruises-from-miami/",
 _CRCR+[("Cruises from Miami",None)],"Cruises from Miami: lines, ships, and where they go","fl-mia-hero",
 "Cruises From Miami: Cruise Lines, Ships, Caribbean and Bahamas | Wonderlocity",
 "Miami is one of the biggest cruise ports in the world. Which lines sail from PortMiami, what the ships are like, and who each one suits.",
 "PortMiami has ten passenger terminals and serves lines from Carnival, Royal Caribbean, Norwegian and MSC to Virgin Voyages and luxury brands, with Bahamas and Caribbean sailings of every length.",
 """{{FACTS|Port=PortMiami, 10 terminals;Lines=14 listed by Miami tourism;Typical trips=Bahamas and Caribbean;Good for=First cruises and big ships}}<p>Miami has the widest choice of any Florida port. You can pick a giant family ship, a short Bahamas getaway, or a long luxury sailing, and flights into Miami are easy from most of the country.</p>
<h2>Who sails from Miami</h2><p>The Greater Miami tourism site lists Azamara, Carnival, Celebrity, Cunard, Holland America, MSC, Norwegian, Oceania, Princess, Regent Seven Seas, Royal Caribbean, Seabourn, Silversea and Virgin Voyages. That is a lot of range, from mass-market to ultra-luxury.</p>
{{FIG|fl-mia-ship|Large ships and many lines share the port, so compare carefully before you choose.}}
<h2>Big ships and families</h2><table class='costtable'><tr><td>Royal Caribbean</td><td>Icon of the Seas (1,198 ft), Utopia, Wonder, Allure, Oasis</td></tr>
<tr><td>Carnival</td><td>Carnival Celebration, Horizon, Sunrise, Imagination</td></tr>
<tr><td>MSC</td><td>MSC World America, Seaside, Seashore, Meraviglia</td></tr>
<tr><td>Norwegian</td><td>Norwegian Luna, Viva, Prima, Encore, Breakaway</td></tr></table>
<p>These are the ships most families look at first. They have the most pools, slides, and clubs for kids, so compare the kids programs and age groups on each line's site before you book.</p>
<h2>Adults only and quieter options</h2><p>Virgin Voyages ships sail from Miami, often with a stop at its Beach Club at Bimini, but Virgin sails for adults only, so it is not an option for a family trip. Luxury brands such as Oceania, Seabourn, Silversea and Regent suit couples and travelers who want smaller ships.</p>
<h2>Where the ships go</h2><p>Miami sailings include Bahamas trips year-round, Caribbean cruises of seven nights and longer, some one-way voyages to Europe, and longer luxury itineraries. Cunard sails roundtrip Caribbean cruises of 9 to 21 nights.</p>
{{FIG|fl-mia-beach|Add a beach day on Miami Beach before or after your cruise.}}
{{TIP|Plan a night in Miami|Arrive the day before, and use the evening for a beach walk. It is easier than racing to the terminal after a morning flight.}}
<h2>Before you book</h2><p>Look at the embarkation day and terminal, and ask how far your hotel is from the port. Compare total cost with gratuities and drinks, not only the fare, and read our <a href='/cruises/carnival-cruise-line-review/'>Carnival review</a> for a plain look at what a week really costs.</p>"""+_UPD,
 [("What cruise lines sail from Miami?","Miami tourism lists 14, including Carnival, Royal Caribbean, Norwegian, MSC, Celebrity, Princess, Holland America and Virgin Voyages."),
  ("Is Miami good for a family cruise?","Yes, because it has many large family ships from Royal Caribbean, Carnival, MSC and Norwegian. Check each line's kids program before you book."),
  ("Can kids go on Virgin Voyages?","No. Virgin Voyages is adults only, so families should choose another line.")],
 [article_node("Cruises from Miami","Cruise lines, ships and itineraries sailing from PortMiami.","https://wonderlocity.com/cruises/cruises-from-miami/")],
 [("All cruise guides","/cruises/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/"),("Port Canaveral or Miami","/cruises/port-canaveral-vs-miami/"),("Best Florida cruises for families","/cruises/best-cruises-from-florida-for-families/"),("Royal Caribbean vs Carnival","/guides/royal-caribbean-vs-carnival/")]+_RELX,
 "Caribbean cruises")

# ---- Port Canaveral vs Miami ----
rich_page("cruises/port-canaveral-vs-miami/index.html","https://wonderlocity.com/cruises/port-canaveral-vs-miami/",
 _CRCR+[("Port Canaveral or Miami",None)],"Port Canaveral or Miami: which port should you pick?","fl-cmp-hero",
 "Port Canaveral vs Miami Cruise Port: Which Is Better? | Wonderlocity",
 "Port Canaveral or Miami for your cruise? A plain comparison of location, cruise lines, parking, and what to do before sailing.",
 "Pick Port Canaveral if you are pairing a cruise with Orlando's theme parks, and pick Miami if you want the biggest choice of lines and ships and a city to explore.",
 """{{FACTS|Orlando parks=Port Canaveral;Most choice=Miami;Distance between=A little over 3 hours;Parking at Canaveral=$20 per day plus tax}}<p>Both ports are good, and which one wins depends on the rest of your trip. Start with where you are flying and what you want to do before or after the ship.</p>
<h2>Side by side</h2><table class='costtable'><tr><td>Best for</td><td>Canaveral: parks and the Space Coast. Miami: city and beach days</td></tr>
<tr><td>Cruise lines</td><td>Canaveral: six main lines plus Cunard. Miami: 14 lines listed</td></tr>
<tr><td>From the airport</td><td>Canaveral: about 45 minutes from Orlando airport. Miami: check your transfer time</td></tr>
<tr><td>Before or after</td><td>Canaveral: Kennedy Space Center, Cocoa Beach. Miami: Miami Beach</td></tr></table>
{{FIG|fl-cmp-a|Many ships look alike from the dock, so compare itineraries and what is on board.}}
<h2>Choose Port Canaveral if</h2><p>You are adding a short cruise to a Disney or Universal week, you like a smaller port with terminals close to parking, or you want a Disney cruise, since Disney has a dedicated terminal there. Kennedy Space Center is about 20 minutes away, and Cocoa Beach is about 15 minutes south.</p>
<h2>Choose Miami if</h2><p>You want the largest choice of lines, you are chasing a specific big ship, or you want a city stay as part of the trip. Miami also has lines that do not sail from Canaveral, including Holland America, Princess and Virgin Voyages.</p>
<h2>Can you do both?</h2><p>Miami is a little over three hours south of Port Canaveral by car, so some travelers fly into one and out of the other, or drive between them. A one-way cruise can end at a different port, so ask your advisor.</p>
{{FIG|fl-cmp-b|Check your ship, your terminal, and your embarkation day before you book flights.}}
<h2>Our rule of thumb</h2><p>Orlando parks first, Canaveral. Maximum choice, Miami. Read both guides: <a href='/cruises/cruises-from-orlando-port-canaveral/'>Port Canaveral</a> and <a href='/cruises/cruises-from-miami/'>Miami</a>.</p>"""+_UPD,
 [("Is Port Canaveral or Miami better for a cruise?","Port Canaveral is better for pairing a cruise with Orlando's parks, and Miami is better for the widest choice of ships and a city stay."),
  ("How far is Port Canaveral from Miami?","A little over three hours by car, per Norwegian's guide."),
  ("Which port is cheaper for parking?","Port Canaveral charges $20 per day plus tax. Check Miami's current rates on the port's own page.")],
 [article_node("Port Canaveral or Miami","A comparison of Port Canaveral and Miami as cruise ports.","https://wonderlocity.com/cruises/port-canaveral-vs-miami/")],
 [("All cruise guides","/cruises/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/"),("Cruises from Miami","/cruises/cruises-from-miami/"),("Carnival from Norfolk","/cruises/carnival-from-norfolk-with-kids/")]+_RELX,
 "Caribbean cruises")

# ---- Best Florida cruises for families ----
rich_page("cruises/best-cruises-from-florida-for-families/index.html","https://wonderlocity.com/cruises/best-cruises-from-florida-for-families/",
 _CRCR+[("Florida cruises for families",None)],"Best cruises from Florida for families","fl-fam-hero",
 "Best Cruises From Florida for Families: Orlando and Miami | Wonderlocity",
 "Family cruises from Port Canaveral and Miami: which lines and ships suit kids, how long to sail, and what to check before you book.",
 "For a family cruise from Florida, start with short Bahamas sailings of three to four nights from Port Canaveral or Miami, then choose the line whose kids program and ship fit your children's ages.",
 """{{FACTS|Start with=3 to 4 nights;Ports=Port Canaveral or Miami;Kids club (Carnival)=Camp Ocean, ages 2 to 11;Check=Kids program ages}}<p>Florida is the easiest place in the country to start cruising with kids. Short sailings leave all week, ships are big, and you can pick a port that fits your flights.</p>
<h2>Start short</h2><p>A 3 or 4 night Bahamas cruise is a good test. You see how your kids handle the ship and the pool without committing to a week. From Port Canaveral those sailings stop at places like Nassau, Perfect Day at CocoCay, and Great Stirrup Cay.</p>
{{FIG|fl-fam-pool|Pool time is the main event for most kids on any ship.}}
<h2>Lines to compare</h2><table class='costtable'><tr><td>Disney Cruise Line</td><td>Port Canaveral, 3 to 7 nights, dedicated terminal</td></tr>
<tr><td>Royal Caribbean</td><td>Port Canaveral and Miami, big ships including Icon of the Seas</td></tr>
<tr><td>Carnival</td><td>Both ports, Camp Ocean included in the fare, ages 2 to 11</td></tr>
<tr><td>MSC and Norwegian</td><td>Both ports, large ships with many pools</td></tr></table>
<p>Kids programs, age groups, and any extra fees differ by line, so check each one's current rules for your children's ages. Avoid Virgin Voyages, which is adults only.</p>
<h2>What to check</h2><ul><li>The kids club age groups and hours</li><li>Whether your children need a minimum age for particular activities</li><li>Gratuities, which add to the fare</li><li>Where the ship docks and how you will get there</li></ul>
{{FIG|fl-fam-deck|Shaded deck space helps when the kids need a break from the sun.}}
{{TIP|Book the room, not just the fare|Families often need a bigger cabin or connecting rooms. Ask your advisor to price a few cabin types side by side.}}
<h2>Plan the parts around the ship</h2><p>Pair the cruise with the parks using our <a href='/cruises/cruises-from-orlando-port-canaveral/'>Port Canaveral guide</a>, or compare ports in <a href='/cruises/port-canaveral-vs-miami/'>Port Canaveral or Miami</a>. For packing, see the <a href='/essentials/family-cruise-packing-list/'>family cruise packing list</a>.</p>
{{FIG|fl-fam-sunset|An evening on deck is often the calmest part of the day.}}"""+_UPD,
 [("What is the best cruise from Florida for families?","It depends on your kids' ages, but a 3 or 4 night Bahamas sailing from Port Canaveral or Miami is a good first choice."),
  ("What age is the Carnival kids club?","Camp Ocean starts at age 2 and covers 2 to 11, included in the fare."),
  ("Is Virgin Voyages good for kids?","No. It is adults only.")],
 [article_node("Best cruises from Florida for families","How to pick a family cruise from Port Canaveral or Miami.","https://wonderlocity.com/cruises/best-cruises-from-florida-for-families/")],
 [("All cruise guides","/cruises/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/"),("Cruises from Miami","/cruises/cruises-from-miami/"),("Disney cruise from Port Canaveral","/cruises/disney-cruise-from-port-canaveral/"),("Family cruise packing list","/essentials/family-cruise-packing-list/")]+_RELX,
 "Caribbean cruises")

# ---- Disney cruise from Port Canaveral ----
rich_page("cruises/disney-cruise-from-port-canaveral/index.html","https://wonderlocity.com/cruises/disney-cruise-from-port-canaveral/",
 _CRCR+[("Disney cruise from Port Canaveral",None)],"Disney cruise from Port Canaveral: a land and sea trip","fl-dis-hero",
 "Disney Cruise From Port Canaveral: Ships, Lengths, Getting There | Wonderlocity",
 "Disney Cruise Line sails from Port Canaveral near Orlando. Which ships, how long, and how to combine it with a Disney World week.",
 "Disney Fantasy, Disney Wish and Disney Treasure are based at Port Canaveral, about 45 to 60 minutes from Walt Disney World, so one trip can include both the parks and a Bahamas or Caribbean cruise.",
 """{{FACTS|Ships based=Fantasy, Wish, Treasure;Lengths=3 to 7 nights;From Disney World=About 45 to 60 minutes;Parking=About $20 per day}}<p>For many families, a Disney trip ends with a cruise. Port Canaveral makes that practical, since Disney has a terminal built just for its ships.</p>
<h2>The ships</h2><p>Disney Fantasy, Disney Wish and Disney Treasure are based at Port Canaveral, and Disney Dream and Disney Magic sail from the port on some dates. Fantasy runs 4 and 5 night Bahamas and Western Caribbean cruises. Wish runs 3 and 4 night Bahamas cruises year-round, and Treasure runs 7 night Eastern and Western Caribbean sailings. Check the current schedule, because it changes by year.</p>
{{FIG|fl-dis-ship|Short sailings are a gentle way to add the sea to a park trip.}}
<h2>Getting there from Disney World</h2><p>Port Canaveral is about 45 miles east of Orlando. It is roughly a 45-minute to one-hour drive from Disney World. Options include a rental car, a shuttle, a rideshare, and Disney Cruise Line ground transfers. If you drive, parking by the terminal is about $20 per day, paid on arrival.</p>
<h2>How to plan the days</h2><table class='costtable'><tr><td>Park days</td><td>Four to five days at the parks first</td></tr>
<tr><td>Transition</td><td>One easy night or a morning drive to the port</td></tr>
<tr><td>Cruise</td><td>3 to 4 nights is easiest for a first try</td></tr></table>
{{FIG|fl-dis-deck|A few nights at sea is a calm contrast to busy park days.}}
{{TIP|Book the cruise early|Disney sailings sell out for school breaks. Hold your dates early, and ask what fits your family's budget.}}
<h2>Is it worth it?</h2><p>A Disney cruise costs more than most mainstream lines. If your kids love Disney, a short sailing can feel like another park day with a beach stop. If budget matters most, compare it with a Carnival or Royal Caribbean cruise from the same port using <a href='/cruises/best-cruises-from-florida-for-families/'>our family cruise guide</a>.</p>"""+_UPD,
 [("Does Disney Cruise Line sail from Port Canaveral?","Yes. Disney Fantasy, Disney Wish and Disney Treasure are based there."),
  ("How far is Port Canaveral from Disney World?","About 45 to 60 minutes by car."),
  ("How long are Disney cruises from Port Canaveral?","From 3 nights on Disney Wish up to 7 nights on Disney Treasure.")],
 [article_node("Disney cruise from Port Canaveral","Ships, itineraries and logistics for a Disney cruise from Port Canaveral.","https://wonderlocity.com/cruises/disney-cruise-from-port-canaveral/")],
 [("All cruise guides","/cruises/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/"),("Best Florida cruises for families","/cruises/best-cruises-from-florida-for-families/"),("Disney or Universal for 6 to 12","/guides/disney-vs-universal-kids-6-12/")]+_RELX,
 "Caribbean cruises")

# ---- Orlando with kids without theme parks ----
rich_page("guides/orlando-with-kids-without-theme-parks/index.html","https://wonderlocity.com/guides/orlando-with-kids-without-theme-parks/",
 _FAMCR+[("Orlando without theme parks",None)],"Orlando with kids: what to do besides theme parks","fl-orl-hero",
 "Orlando With Kids Without Theme Parks: Gators, Space, Science | Wonderlocity",
 "Rest days in Orlando: Gatorland, an aquarium, a science museum, Kennedy Space Center, and gardens that kids actually enjoy.",
 "Orlando has plenty for kids beyond the parks, including a 110-acre gator park, a four-floor science center, an aquarium with 250 species, and Kennedy Space Center about an hour away.",
 """{{FACTS|Best for=Rest days between parks;Day trip=Kennedy Space Center, about 1 hour;Animals=Gatorland and SEA LIFE;Indoor=Science Center and aquarium}}<p>A week of theme parks wears kids out, and it wears out budgets too. These are the places families use for the in-between days.</p>
{{FIG|fl-orl-hero|A lake and a walk are a good reset after a big park day.}}
<h2>Animals and wildlife</h2><p>Gatorland is a 110-acre wildlife preserve with a zipline over the alligator breeding marsh. SEA LIFE Orlando Aquarium has 250 species across nine exhibits. Giraffe Ranch runs a guided safari that ends with a chance to feed a giraffe.</p>
{{FIG|fl-orl-gator|Alligators are a Florida must-see for most kids.}}
<h2>Science and space</h2><p>The Orlando Science Center has four floors of interactive exhibits, along with live fish and alligators. Kennedy Space Center is about an hour from Orlando, and its bus tour drives past the launch pad and shows a real rocket.</p>
{{FIG|fl-orl-space|Space Coast days are good for kids who love rockets.}}
<h2>Gardens and quiet time</h2><p>Leu Gardens offers kid-friendly scavenger hunts, plus holiday light displays and rotating exhibits through the year. It is a calm choice for a break day.</p>
{{FIG|fl-orl-green|A garden walk gives everyone a rest.}}
{{TIP|Mix it up|Plan one non-park day for every two park days. Kids stay happier, and you spend less on tickets.}}
<h2>A sample rest day</h2><table class='costtable'><tr><td>Morning</td><td>Orlando Science Center or SEA LIFE</td></tr>
<tr><td>Afternoon</td><td>Pool time at the hotel</td></tr>
<tr><td>Evening</td><td>Gardens or an easy dinner</td></tr></table>
<p>For the parks, see <a href='/guides/disney-vs-universal-kids-6-12/'>Disney vs Universal for ages 6 to 12</a> and <a href='/guides/orlando-on-a-budget/'>Orlando on a budget</a>.</p>"""+_UPD,
 [("What can kids do in Orlando besides theme parks?","Try Gatorland, SEA LIFE Orlando Aquarium, the Orlando Science Center, Leu Gardens, or a day at Kennedy Space Center."),
  ("How far is Kennedy Space Center from Orlando?","About an hour by car."),
  ("Is the Orlando Science Center good for kids?","Yes. It has four floors of hands-on exhibits and live fish and alligators.")],
 [article_node("Orlando with kids: what to do besides theme parks","Rest-day ideas for families in Orlando.","https://wonderlocity.com/guides/orlando-with-kids-without-theme-parks/")],
 [("All family trips","/family/"),("Orlando on a budget","/guides/orlando-on-a-budget/"),("Best beaches near Orlando","/guides/best-beaches-near-orlando-for-families/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/")]+_RELX,
 "Orlando")

# ---- Best beaches near Orlando ----
rich_page("guides/best-beaches-near-orlando-for-families/index.html","https://wonderlocity.com/guides/best-beaches-near-orlando-for-families/",
 _FAMCR+[("Beaches near Orlando",None)],"Best beaches near Orlando for families","fl-bch-hero",
 "Best Beaches Near Orlando for Families: Cocoa Beach and More | Wonderlocity",
 "Beach day from Orlando: Cocoa Beach, New Smyrna, Daytona, Canaveral National Seashore, and how long each drive takes.",
 "The closest family beaches to Orlando are about an hour away: Daytona Beach, New Smyrna Beach and Cocoa Beach, with Canaveral National Seashore for quiet sand.",
 """{{FACTS|Closest=Daytona, New Smyrna, Cocoa;Drive=About 1 hour to 1 hour 15;Calm water=New Smyrna Beach;Quiet sand=Canaveral National Seashore}}<p>Orlando is inland, but the Atlantic coast is only about an hour away. A beach day fits easily between park days.</p>
<h2>Beaches and drive times</h2><table class='costtable'><tr><td>Daytona Beach</td><td>About 58 minutes, boardwalk and family entertainment</td></tr>
<tr><td>New Smyrna Beach</td><td>About 1 hour 3 minutes, gentle waves</td></tr>
<tr><td>Cocoa Beach</td><td>About 1 hour 9 minutes, pier with restaurants and free live music</td></tr>
<tr><td>Canaveral National Seashore</td><td>About 1 hour 15 minutes, wide quiet sands</td></tr></table>
{{FIG|fl-bch-guard|Cocoa Beach has a pier, shops, and a relaxed family feel.}}
<h2>Best pick by kids</h2><p>New Smyrna Beach has gentle waves that suit young kids. Cocoa Beach works for a mix of ages thanks to the pier and live music. Daytona Beach is the choice if you want a boardwalk and entertainment.</p>
{{FIG|fl-bch-light|Ponce Inlet is home to Florida's tallest lighthouse, which visitors can climb.}}
<h2>Go quiet</h2><p>Canaveral National Seashore has wide quiet sands for swimming and hiking, but the park does not sell snacks, water, sunscreen or bug spray, so bring your own. Satellite Beach has a sea turtle walk with the Sea Turtle Preservation Society.</p>
{{FIG|fl-bch-walk|Pack a cooler and let the kids set the pace.}}
{{TIP|Leave early|Leaving by 8 or 9 a.m. gives you a long beach day and an easier drive home before evening traffic.}}
<p>Combine a beach day with a cruise from <a href='/cruises/cruises-from-orlando-port-canaveral/'>Port Canaveral</a>, or add rest days from our <a href='/guides/orlando-with-kids-without-theme-parks/'>Orlando without theme parks</a> guide.</p>"""+_UPD,
 [("What is the closest beach to Orlando?","Daytona Beach is about 58 minutes away, followed by New Smyrna Beach at about an hour."),
  ("Which beach near Orlando is best for young kids?","New Smyrna Beach has gentle waves that suit kids, and Cocoa Beach has a pier with live music."),
  ("Can you bring food to Canaveral National Seashore?","You need to. The park does not sell snacks, water, sunscreen or bug spray.")],
 [article_node("Best beaches near Orlando for families","Family beaches within about an hour and a quarter of Orlando.","https://wonderlocity.com/guides/best-beaches-near-orlando-for-families/")],
 [("All family trips","/family/"),("Orlando without theme parks","/guides/orlando-with-kids-without-theme-parks/"),("Cruises from Orlando","/cruises/cruises-from-orlando-port-canaveral/"),("Orlando guide","/destinations/orlando/")]+_RELX,
 "Orlando")


# ===== Family hub + homepage story feed (added Nov 2026) =====
import glob as _g2, re as _r2, html as _h2

FEED_META = {
 "cruises/cruises-from-orlando-port-canaveral":("Cruises","cruises family"),
 "cruises/cruises-from-miami":("Cruises","cruises family"),
 "cruises/port-canaveral-vs-miami":("Cruises","cruises"),
 "cruises/best-cruises-from-florida-for-families":("Cruises","cruises family"),
 "cruises/disney-cruise-from-port-canaveral":("Cruises","cruises family"),
 "guides/orlando-with-kids-without-theme-parks":("Family","family"),
 "guides/best-beaches-near-orlando-for-families":("Family","family beach"),
 "guides/things-to-do-with-kids-virginia-beach":("Family","family weekend"),
 "cruises/carnival-from-norfolk-with-kids":("Cruises","cruises family"),
 "essentials/family-cruise-packing-list":("Packing list","cruises family"),
 "guides/road-trip-virginia-beach-to-orlando-with-kids":("Family","family"),
 "guides/disney-vs-universal-kids-6-12":("Family","family"),
 "guides/disney-or-universal-toddlers":("Family","family"),
 "guides/orlando-on-a-budget":("Family","family"),
 "guides/caribbean-family-resorts":("Family","family beach"),
 "guides/williamsburg-weekend":("Weekend trip","family weekend"),
 "guides/outer-banks-weekend":("Weekend trip","family weekend"),
 "guides/weekend-getaways-from-virginia-beach":("Weekend trip","family weekend"),
 "guides/caribbean-cruise-first-timer":("Cruises","cruises"),
 "guides/royal-caribbean-vs-carnival":("Cruises","cruises family"),
 "essentials/cruise-packing-list":("Packing list","cruises family"),
 "essentials/caribbean-packing-list":("Packing list","beach family"),
 "guides/all-inclusive-caribbean-cost":("Beach and resorts","beach"),
 "guides/cancun-travel-cost":("Beach and resorts","beach"),
 "guides/punta-cana-best-resorts":("Beach and resorts","beach"),
 "guides/cancun-vs-punta-cana-vs-nassau":("Beach and resorts","beach"),
 "guides/maldives-vs-bora-bora":("Honeymoon","beach"),
 "guides/santorini-honeymoon-cost":("Europe","europe"),
 "guides/best-time-to-visit-italy":("Europe","europe"),
 "guides/italy-10-day-itinerary":("Europe","europe"),
 "guides/best-time-to-visit-greece":("Europe","europe"),
 "destinations/maldives":("Destination","beach"),
 "destinations/punta-cana":("Destination","beach family"),
 "destinations/orlando":("Destination","family"),
}
FEED_ORDER = ["cruises/cruises-from-orlando-port-canaveral","cruises/cruises-from-miami","cruises/port-canaveral-vs-miami","cruises/best-cruises-from-florida-for-families","cruises/disney-cruise-from-port-canaveral","guides/orlando-with-kids-without-theme-parks","guides/best-beaches-near-orlando-for-families",
 "guides/things-to-do-with-kids-virginia-beach","cruises/carnival-from-norfolk-with-kids","essentials/family-cruise-packing-list","guides/road-trip-virginia-beach-to-orlando-with-kids","guides/disney-vs-universal-kids-6-12",
 "cruises/carnival-cruise-line-review","guides/disney-or-universal-toddlers","guides/caribbean-family-resorts",
 "cruises/carnival-caribbean-itineraries","guides/williamsburg-weekend","guides/italy-10-day-itinerary","guides/orlando-on-a-budget",
 "cruises/carnival-ships-guide","guides/outer-banks-weekend","guides/punta-cana-best-resorts","guides/santorini-honeymoon-cost",
 "guides/caribbean-cruise-first-timer","guides/weekend-getaways-from-virginia-beach","guides/royal-caribbean-vs-carnival",
 "guides/all-inclusive-caribbean-cost","essentials/cruise-packing-list"]

def _scan_articles():
    out = {}
    pats = ["guides/*/index.html","cruises/*/index.html","essentials/*/index.html","destinations/*/index.html"]
    for pat in pats:
        for f in sorted(_g2.glob(os.path.join(ROOT,pat))):
            key = os.path.relpath(os.path.dirname(f),ROOT).replace(os.sep,"/")
            h = open(f,encoding="utf-8").read()
            m1 = _r2.search(r"<h1>(.*?)</h1>",h,_r2.S); m2 = _r2.search(r'<meta name="description" content="([^"]*)"',h)
            m3 = _r2.search(r"phero\" style=\"background-image:url\('([^']+)'\)",h)
            if not (m1 and m3): continue
            img = m3.group(1).replace("w=1920&h=900","w=900&h=600").replace("/1920/900","/900/600")
            label,cats = FEED_META.get(key,("Cruises","cruises") if key.startswith("cruises/") else ("Guide",""))
            out[key] = {"url":"/"+key+"/","title":m1.group(1).strip(),"desc":(m2.group(1) if m2 else ""),"img":img,"label":label,"cats":cats}
    return out

def _story_card(a, cls="sc"):
    return ('<article class="'+cls+'" data-cat="'+a["cats"]+'"><a class="sc-img" href="'+a["url"]+'"><img src="'+a["img"]+'" alt="" loading="lazy" width="900" height="600" onerror="this.style.display=\'none\'"></a>'
        '<div class="sc-b"><p class="sc-k">'+a["label"]+'</p><h3><a href="'+a["url"]+'">'+a["title"]+'</a></h3><p class="sc-d">'+a["desc"]+'</p>'
        '<a class="sc-r" href="'+a["url"]+'">Read the story</a></div></article>')

STORY_CSS = """<style>
#stories{scroll-margin-top:90px}
.fchips{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0 8px}
.fchips button{font:inherit;font-size:14.5px;border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:8px 16px;border-radius:30px;cursor:pointer;transition:.2s}
.fchips button:hover{border-color:var(--green)}.fchips button.on{background:var(--green);border-color:var(--green);color:#fff}
.fgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:30px 24px;margin-top:26px}
.sc{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.sc.in{opacity:1;transform:none}
.sc[hidden]{display:none}
.sc-img{display:block;aspect-ratio:3/2;overflow:hidden;border-radius:var(--radius);background:var(--sand)}
.sc-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s ease}
.sc:hover .sc-img img{transform:scale(1.04)}
.sc-b{padding-top:14px}
.sc-k{font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);font-weight:500;margin:0 0 6px}
.sc h3{font-family:Fraunces,Georgia,serif;font-weight:400;font-size:23px;line-height:1.22;margin:0 0 8px}
.sc h3 a:hover{color:var(--green-dark)}
.sc-d{font-size:15px;color:var(--muted);margin:0 0 10px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.sc-r{font-size:14px;color:var(--gold);font-weight:500}
.fmore{text-align:center;margin-top:38px}
@media(max-width:900px){.fgrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.fgrid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){.sc{opacity:1;transform:none;transition:none}}
</style><noscript><style>.sc{opacity:1!important;transform:none!important}</style></noscript>"""

STORY_JS = """<script>
(function(){
var grid=document.getElementById('fgrid');if(!grid)return;
var cards=[].slice.call(grid.children),btn=document.getElementById('fmore'),chips=[].slice.call(document.querySelectorAll('.fchips button'));
var filter='all',limit=9,STEP=9;
var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'}):null;
function match(c){return filter==='all'||(' '+c.getAttribute('data-cat')+' ').indexOf(' '+filter+' ')>-1;}
function render(){var shown=0,total=0,delay=0;
cards.forEach(function(c){if(match(c)){total++;if(shown<limit){c.hidden=false;shown++;
if(io&&!c.classList.contains('in')){c.style.transitionDelay=(delay%3)*90+'ms';delay++;io.observe(c);}else{c.classList.add('in');}}else{c.hidden=true;}}else{c.hidden=true;}});
btn.style.display=(shown<total)?'':'none';}
chips.forEach(function(b){b.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on');});b.classList.add('on');filter=b.getAttribute('data-f');limit=9;render();});});
btn.addEventListener('click',function(){limit+=STEP;render();});
render();
})();
</script>"""

def _build_feed_html(arts):
    keys = [k for k in FEED_ORDER if k in arts]
    new = sorted(k for k in arts if k not in FEED_ORDER and k not in FEED_META and not k.startswith("destinations/"))
    rest = sorted(k for k in arts if k not in keys and k not in new)
    ordered = new + keys + rest
    cards = "".join(_story_card(arts[k]) for k in ordered)
    chips = ('<button class="on" data-f="all">All stories</button><button data-f="family">Family trips</button>'
             '<button data-f="cruises">Cruises</button><button data-f="beach">Beach and resorts</button>'
             '<button data-f="europe">Europe</button><button data-f="weekend">Weekend trips</button>')
    return ('<!--FEED--><section class="section tight" id="stories"><div class="wrap">'+STORY_CSS+
        '<p class="eyebrow">Latest stories</p><h2 style="font-size:34px;margin-bottom:0">Real costs, honest picks, and trips worth taking</h2>'
        '<div class="fchips">'+chips+'</div><div class="fgrid" id="fgrid">'+cards+'</div>'
        '<div class="fmore"><button class="btn btn-green" id="fmore" type="button">Show more stories</button></div></div>'+STORY_JS+'</section><!--/FEED-->')

_ARTS = _scan_articles()

# ---- inject feed into the homepage (between markers; first run inserts after the hero) ----
_hp = os.path.join(ROOT,"index.html"); _hh = open(_hp,encoding="utf-8").read()
_feed = _build_feed_html(_ARTS)
if "<!--FEED-->" in _hh:
    _hh = _r2.sub(r"<!--FEED-->.*?<!--/FEED-->",lambda m:_feed,_hh,flags=_r2.S)
else:
    _i = _hh.index("</section>",_hh.index('class="hero"'))+len("</section>")
    _hh = _hh[:_i]+"\n\n"+_feed+_hh[_i:]
open(_hp,"w",encoding="utf-8").write(_hh)

# ---- Family hub ----
_FAM = [
 ("theme-parks","Theme parks and Orlando","Disney, Universal, and how to do Orlando without the sticker shock.",
   ["guides/orlando-with-kids-without-theme-parks","guides/disney-vs-universal-kids-6-12","guides/road-trip-virginia-beach-to-orlando-with-kids","guides/disney-or-universal-toddlers","guides/orlando-on-a-budget","destinations/orlando"]),
 ("beach","Beach and all-inclusive resorts","Resorts where the kids are busy and the bill is clear before you book.",
   ["guides/best-beaches-near-orlando-for-families","guides/caribbean-family-resorts","guides/all-inclusive-caribbean-cost","guides/cancun-vs-punta-cana-vs-nassau","guides/punta-cana-best-resorts"]),
 ("cruises","Cruises with kids","One price, one unpack, and a different island most days.",
   ["cruises/best-cruises-from-florida-for-families","cruises/cruises-from-orlando-port-canaveral","cruises/cruises-from-miami","cruises/disney-cruise-from-port-canaveral","cruises/port-canaveral-vs-miami","cruises/carnival-from-norfolk-with-kids","guides/royal-caribbean-vs-carnival","cruises/carnival-cruise-line-review","guides/caribbean-cruise-first-timer","cruises/carnival-ships-guide"]),
 ("weekends","Weekend trips from Virginia Beach","Short drives, no flights, and easy to fit around school and work.",
   ["guides/things-to-do-with-kids-virginia-beach","guides/williamsburg-weekend","guides/outer-banks-weekend","guides/weekend-getaways-from-virginia-beach"]),
 ("plan","Plan and pack","Packing lists and planning help so nothing gets forgotten.",
   ["essentials/family-cruise-packing-list","essentials/cruise-packing-list","essentials/caribbean-packing-list"]),
]
_fam_crumbs = [("Home","/"),("Family trips",None)]
_fb = phero("wl-fm-hero",_fam_crumbs,"Family trips")
_fb += '<section class="section"><div class="wrap">' + CARD_CSS
_fb += ('<div class="narrow" style="padding:0"><p class="answer">Family trips go well when the plan fits the kids, and the budget is clear before you book.</p>'
        '<p>Pick a direction below. Each guide starts with what the trip really costs, then covers what to do, where to stay, and what to skip with children along.</p></div>')
_fb += '<div class="fchips" style="margin:22px 0 4px">' + "".join('<a class="btn" style="border:1px solid var(--line);background:var(--surface);padding:8px 16px;font-size:14.5px" href="#'+i+'">'+t+'</a>' for i,t,d,k in _FAM) + '</div>'
for _id,_t,_d,_keys in _FAM:
    _items = [_ARTS[k] for k in _keys if k in _ARTS]
    if not _items: continue
    _fb += '<h2 id="'+_id+'" style="font-size:30px;margin:54px 0 4px">'+_t+'</h2><p style="color:var(--muted);margin:0 0 6px">'+_d+'</p><div class="grid3" style="margin-top:20px">'
    for a in _items:
        _fb += ('<article class="lcard"><a href="'+a["url"]+'"><div class="ph" style="background-image:url(\''+a["img"]+'\')"></div></a>'
                '<div class="b"><h3>'+a["title"]+'</h3><p>'+a["desc"]+'</p><a class="r" href="'+a["url"]+'">Read more</a></div></article>')
    _fb += '</div>'
_fb += '<div class="narrow" style="padding:0;margin-top:56px">' + advisory + '</div></div></section>'
page("family/index.html","Family Trips: Theme Parks, Beaches, Cruises and Weekends | Wonderlocity",
 "Family trip guides with real costs: Orlando with kids, beach resorts, cruises, and weekend trips from Virginia Beach.",
 "https://wonderlocity.com/family/", _fb,
 {"@context":"https://schema.org","@graph":[breadcrumb_schema(_fam_crumbs)]})


# ---- rebuild full sitemap ----
all_urls = ["/","/about/","/plan/","/contact/","/disclosure/","/privacy/","/terms/","/deals/","/resources/",
 "/destinations/","/destinations/punta-cana/","/destinations/maldives/","/destinations/orlando/",
 "/trip-types/","/trip-types/all-inclusive/","/trip-types/honeymoon/","/trip-types/cruise/","/trip-types/family/",
 "/guides/","/guides/all-inclusive-caribbean-cost/","/guides/best-time-to-visit-italy/","/guides/weekend-getaways-from-virginia-beach/","/guides/cancun-travel-cost/","/guides/punta-cana-best-resorts/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in all_urls:
    pr = "1.0" if u=="/" else "0.8"
    sm += '  <url><loc>https://wonderlocity.com'+u+'</loc><changefreq>weekly</changefreq><priority>'+pr+'</priority></url>\n'
sm += '</urlset>\n'
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
print("Phase 1b complete:", len(all_urls), "urls in sitemap.")

# ===== Phase 2: filesystem-driven sitemap + RSS feed =====
import glob as _glob, re as _re, datetime as _dt
def _scan_pages():
    out=[]
    for f in _glob.glob(os.path.join(ROOT,"**","index.html"),recursive=True):
        rel=os.path.relpath(f,ROOT).replace("\\","/")
        d=os.path.dirname(rel)
        url="/"+(d+"/" if d else "")
        html=open(f,encoding="utf-8").read()
        t=_re.search(r"<title>(.*?)</title>",html,_re.S)
        m=_re.search(r'name="description" content="(.*?)"',html,_re.S)
        out.append((url, t.group(1).strip() if t else "Wonderlocity", m.group(1).strip() if m else ""))
    out.sort(key=lambda x:(x[0]!="/", x[0]))
    return out
_pages=_scan_pages()
_sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u,_,_ in _pages:
    pr="1.0" if u=="/" else ("0.7" if u.count("/")>2 else "0.8")
    _sm+='  <url><loc>https://wonderlocity.com'+u+'</loc><changefreq>weekly</changefreq><priority>'+pr+'</priority></url>\n'
_sm+='</urlset>\n'
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(_sm)

def _esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
_now=_dt.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
_items=""
for u,title,desc in _pages:
    if u.startswith("/guides/") and u!="/guides/":
        link="https://wonderlocity.com"+u
        _items+=("  <item><title>"+_esc(title)+"</title><link>"+link+"</link>"
                 "<guid>"+link+"</guid><pubDate>"+_now+"</pubDate>"
                 "<description>"+_esc(desc)+"</description></item>\n")
_rss=('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>\n'
 '  <title>Wonderlocity Travel Guides</title>\n  <link>https://wonderlocity.com/guides/</link>\n'
 '  <description>Honest travel cost guides and destination advice.</description>\n  <language>en-us</language>\n'
 +_items+'</channel></rss>\n')
open(os.path.join(ROOT,"feed.xml"),"w",encoding="utf-8").write(_rss)
print("Sitemap + RSS rebuilt from disk:", len(_pages), "pages")
