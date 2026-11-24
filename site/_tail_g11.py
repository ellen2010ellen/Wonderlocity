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
