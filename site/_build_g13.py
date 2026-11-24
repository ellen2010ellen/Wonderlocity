import os, json
ROOT = os.path.dirname(os.path.abspath(__file__))

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
.brand{font-family:Fraunces,serif;font-size:25px;color:var(--green-dark)}.brand b{font-weight:500}
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
"""

HEADER = """<header class="site"><div class="wrap nav">
<a class="brand" href="/"><b>Wonderlocity</b></a>
<nav><ul id="menu">
<li><a href="/destinations/">Destinations</a></li>
<li><a href="/guides/">Travel Guides</a></li>
<li><a href="/deals/">Deals</a></li>
<li><a href="/plan/">Plan with me</a></li>
<li><a href="/about/">About</a></li>
<li><a href="/contact/">Contact</a></li>
</ul></nav>
<div class="cta"><span class="lang" title="Russian version coming later">EN</span>
<a class="btn btn-green" href="/contact/">Free planning chat</a>
<button class="burger" aria-label="Open menu" id="burger">&#9776;</button></div>
</div></header>"""

FOOTER = """<footer class="site"><div class="wrap">
<div class="fcols">
<div><a class="brand" href="/">Wonderlocity</a><p>An independent travel advisory and resource based in Virginia Beach, Virginia, affiliated with the WorldVia Travel Network.</p></div>
<div><h4>Explore</h4><ul><li><a href="/destinations/">Destinations</a></li><li><a href="/guides/">Travel Guides</a></li><li><a href="/deals/">Deals</a></li><li><a href="/trip-types/all-inclusive/">All-inclusive</a></li></ul></div>
<div><h4>Work with me</h4><ul><li><a href="/plan/">Planning services</a></li><li><a href="/contact/">Free planning chat</a></li><li><a href="/about/">About Wonderlocity</a></li><li><a href="/resources/">Free resources</a></li></ul></div>
<div><h4>Follow</h4><ul><li><a href="#">Pinterest</a></li><li><a href="#">Facebook</a></li><li><a href="#">Instagram</a></li></ul></div>
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

def dest_page(slug, name, seed, title, desc, answer, expand, besttime, includes, costs, faqs, related):
    canonical = "https://wonderlocity.com/destinations/"+slug+"/"
    cr = [("Home","/"),("Destinations","/destinations/"),(name,None)]
    body = ('<section class="phero" style="background-image:url(\'https://picsum.photos/seed/'+seed+'/1920/900\')">'
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
    return ('<section class="phero" style="background-image:url(\'https://picsum.photos/seed/'+seed+'/1920/900\')">'
        '<div class="wrap inner"><div class="crumb">'+crumbs(crumb_items)+'</div><h1>'+h1+'</h1></div></section>')

def rich_page(path, canonical, crumb_items, h1, seed, title, desc, answer, prose_html, faqs, extra_nodes, related, affiliate_dest):
    body = phero(seed, crumb_items, h1) + '<section class="section"><div class="narrow">'
    body += '<p class="answer">'+answer+'</p>'
    body += '<div class="prose">'+prose_html+'</div>'
    if affiliate_dest:
        body += affiliate_panel(affiliate_dest)
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
        body += ('<article class="lcard"><a href="'+url+'"><div class="ph" style="background-image:url(\'https://picsum.photos/seed/'+cseed+'/800/600\')"></div></a>'
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
 "A 7-night Caribbean cruise in 2026 costs $700 - $2,500 per person, covering the cabin, meals, and entertainment, before flights, excursions, gratuities, and drinks.",
 "<p>A cruise is the most all-in-one trip there is, but the sticker price is only part of the story. The cabin fare is the start, and the extras decide what you really spend.</p>"
 "<h2>What is included</h2><p>Your cabin, main dining, most entertainment, and getting between ports. That alone is strong value, especially for first-timers and multi-generation groups.</p>"
 "<h2>What is extra</h2><p>Flights to the port, shore excursions, gratuities, drink packages, specialty dining, and wifi. These can add 30 to 60 percent on top of the fare, so we budget them up front.</p>"
 "<h2>Picking the right line</h2><p>Mass-market lines suit families and value seekers, premium lines suit couples who want calmer ships, and the cabin type matters more than most people expect.</p>",
 [("How much does a Caribbean cruise cost?","The cabin fare runs $700 to $2,500 per person for a week in 2026. Add flights, excursions, gratuities, and drinks, which can lift the total by 30 to 60 percent."),
  ("Are drinks and tips included on a cruise?","Usually not. Gratuities and drink packages are typically extra, though some fares bundle them. We confirm what is included before you book."),
  ("Is a cruise good for first-time travelers?","Yes. One price covers your room, meals, and entertainment, and you unpack once while visiting several places.")],
 [service_node("Cruise planning")],
 [("All-inclusive","/trip-types/all-inclusive/"),("Family trips","/trip-types/family/"),("Plan with me","/plan/")],
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
 "A first Caribbean cruise costs $700 to $2,500 per person for a 7-night sailing in 2026. See what is included, what costs extra, which line to pick, and the tips first-timers wish they knew.",
 "A first Caribbean cruise costs $700 - $2,500 per person for a 7-night sailing in 2026, covering your cabin, meals, and entertainment, before you add flights to the port, shore excursions, gratuities, and drinks that typically lift the total by 30 to 60 percent.",
 "<p>A cruise is the easiest big trip to take for the first time, since one price covers your room, your meals, and most of the entertainment, and you unpack once while the ship carries you between islands. The catch is that the fare you see advertised is only the starting point, and the extras decide what you actually spend. Here is the honest breakdown, with the numbers up front, so you board knowing what a week really costs.</p>"
 "<h2>What a first Caribbean cruise costs</h2><p>The fare depends most on your cabin type, the line, and the week you sail. An inside cabin on a mass-market ship is the value entry point, while a balcony costs more but transforms the trip with your own view and fresh air. For a 7-night Caribbean sailing in 2026, here is the range, along with the two extras almost every first-timer forgets to budget.</p><table class='costtable'>"
 "<tr><td>Inside cabin, 7-night sailing</td><td>$700 - $1,300 per person</td></tr>"
 "<tr><td>Balcony cabin, 7-night sailing</td><td>$1,100 - $2,500 per person</td></tr>"
 "<tr><td>Gratuities for the week</td><td>$120 - $170 per person</td></tr>"
 "<tr><td>Drink package</td><td>add $65 - $95 per person per day</td></tr></table>"
 "<h2>What is included in the fare</h2><p>Your cabin, all your main dining room and buffet meals, most daytime activities, the pools, the evening shows, and the transport between ports are built into the price. That is why a cruise feels like such strong value, especially for first-timers and families, since you can eat well and stay entertained without opening your wallet once you are aboard. Room service is often included or carries a small fee, and the kids clubs on the big family lines are free.</p>"
 "<h2>What costs extra</h2><p>The line makes its money on the add-ons, so plan for them. Flights to the departure port, shore excursions at each island, daily gratuities, drink packages, specialty restaurants, wifi, spa treatments, and the casino all sit on top of the fare. Together they commonly add 30 to 60 percent to the base price, which is how a $900 fare becomes a $1,400 trip. The three that matter most are gratuities, which are close to mandatory, excursions, which you can often book independently for less, and drinks, where a package only pays off if you drink several a day.</p>"
 "<h2>Which cruise line to pick for your first time</h2><p>Match the line to your group, not the brochure. Royal Caribbean and Norwegian suit first-timers who want big, activity-packed ships with plenty for all ages, Carnival leans fun, casual, and budget-friendly, and Princess or Celebrity feel calmer and a touch more refined for couples. The ship matters as much as the line, since a newer, larger vessel carries more dining, pools, and entertainment. For a first cruise, a well-reviewed big ship on a major line is the safest way to find out if cruising is for you.</p>"
 "<h2>Eastern, Western, or Southern Caribbean</h2><p>Most first-timers sail one of three routes. The Eastern Caribbean visits beach-and-shopping ports like St Thomas and St Maarten plus the cruise line's private island, and it is the classic easy first cruise. The Western Caribbean leans toward Cozumel, Grand Cayman, and Jamaica, with more snorkeling, ruins, and adventure excursions. The Southern Caribbean, often out of San Juan, reaches further-flung islands like Aruba and Barbados with warmer, drier weather, though it usually means flying to the port. For a first sailing, an Eastern or Western route from Florida keeps flights short and the pace relaxed.</p>"
 "<h2>When to go and hurricane season</h2><p>The cheapest fares fall in the shoulder weeks of late April to early June and September to early December, outside school holidays and the winter peak. The Atlantic hurricane season runs June through November, with the highest risk from August to October. A cruise is actually a reasonable way to travel then, since ships can and do reroute around storms, and fares and crowds drop. The trade-off is a small chance of a changed itinerary, so travel insurance is worth the modest cost in those months. For the calmest seas and best weather, the December to April window is ideal, and also the priciest.</p>"
 "<h2>What first-timers wish they knew</h2><p>A few habits make the first cruise smoother. Pack a carry-on with swimwear and any medicine, since your checked bags may not reach the cabin until dinnertime. Book popular excursions and specialty dinners before you sail, because the best ones fill up. Download the ship's app to see the daily schedule, and bring a lanyard for your key card. Budget cash for port taxis and tips. Do the drink-package math, since it only saves money at four or more drinks a day. And if you are flying, arrive in the port city the night before, so a delayed flight never costs you the ship.</p>"
 "<h2>The verdict</h2><p>A Caribbean cruise is one of the best-value first big trips you can take, and the way to enjoy it is to budget the extras up front rather than be surprised by them. Pick a big, well-reviewed ship on a major line, choose an Eastern or Western route from Florida to keep flights short, sail in shoulder season if you can, and add insurance if you go during hurricane months. Do that and the week delivers several islands, all your meals, and nightly entertainment for a price that is hard to beat any other way.</p>",
 [("How much does a first Caribbean cruise cost?","About $700 to $2,500 per person for a 7-night sailing in 2026, depending on cabin and line. Add flights, gratuities, excursions, and drinks, which typically lift the total by 30 to 60 percent."),
  ("What is the best cruise line for first-timers?","Royal Caribbean and Norwegian for big, activity-packed ships, Carnival for a fun budget-friendly trip, and Princess or Celebrity for a calmer, more refined feel. A newer, larger ship on a major line is the safest first choice."),
  ("Is it safe to cruise the Caribbean during hurricane season?","Generally yes. Ships reroute around storms, and fares and crowds are lower from June to November. The main risk is a changed itinerary, so travel insurance is worth it in those months.")],
 [article_node("First Caribbean cruise: a complete 2026 cost and tips guide","Real 2026 costs, what is included, which line to pick, and first-timer tips for a Caribbean cruise.","https://wonderlocity.com/guides/caribbean-cruise-first-timer/")],
 [("Cruises","/trip-types/cruise/"),("Caribbean cost guide","/guides/all-inclusive-caribbean-cost/"),("Plan with me","/plan/")],
 "Caribbean cruises")

rich_page("guides/royal-caribbean-vs-carnival/index.html","https://wonderlocity.com/guides/royal-caribbean-vs-carnival/",
 [("Home","/"),("Travel guides","/guides/"),("Royal Caribbean vs Carnival vs Norwegian",None)],"Royal Caribbean vs Carnival vs Norwegian: which to pick","wl-g9-hero",
 "Royal Caribbean vs Carnival vs Norwegian 2026: Which to Pick | Wonderlocity",
 "Royal Caribbean, Carnival, and Norwegian all run 7-night Caribbean cruises for $700 to $2,500 per person in 2026. See which line fits your group, budget, and style.",
 "For a 7-night Caribbean sailing in 2026 all three lines cost roughly $700 - $2,500 per person, so the right pick comes down to style, with Carnival cheapest and most casual, Royal Caribbean the biggest ships and best kids programs, and Norwegian the most flexible dining and adult-friendly freestyle feel.",
 "<p>Royal Caribbean, Carnival, and Norwegian are the three lines almost every first-time and family cruiser ends up comparing, and on price they overlap far more than their reputations suggest. The same week, the same route, and the same cabin category usually land within a few hundred dollars of each other. What actually differs is the onboard experience, so the smart way to choose is by trip style, not by fare alone. Here is how the three compare, with the numbers up front.</p>"
 "<h2>How the three compare on price</h2><p>For a 7-night Caribbean sailing in 2026, Carnival is usually the cheapest entry point, Royal Caribbean sits in the middle but climbs fast on its newest ships, and Norwegian prices close to Royal Caribbean once you add its dining and drink bundles. Sale weeks shuffle the order constantly, which is why we price all three for your dates before booking.</p><table class='costtable'>"
 "<tr><td>Carnival, inside to balcony</td><td>$700 - $1,900 per person</td></tr>"
 "<tr><td>Royal Caribbean, inside to balcony</td><td>$800 - $2,500 per person</td></tr>"
 "<tr><td>Norwegian, inside to balcony</td><td>$800 - $2,400 per person</td></tr>"
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
 [("Cruises","/trip-types/cruise/"),("First Caribbean cruise guide","/guides/caribbean-cruise-first-timer/"),("Plan with me","/plan/")],
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
  ("Cruises","/trip-types/cruise/","wl-cr-hero","$700 - $2,500 per person, week","All-in-one, plus the extras to budget for."),
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
  ("Punta Cana adults-only resorts","/guides/punta-cana-best-resorts/","wlguide5","","The best adults-only all-inclusive resorts, by area.")])

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
