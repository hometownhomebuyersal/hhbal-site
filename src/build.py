import os
OUT='/workspace/hhbal-site'
PHONE='205-914-4215'; TEL='tel:+12059144215'; SMS='sms:+12059144215'
EMAIL='joshua@hhbal.com'
LEAD_EMAIL='hometownhomebuyersal@gmail.com'
GREVIEWS='https://search.google.com/local/reviews?placeid=ChIJfT1eZ8mdiYgRRodK3oOmLRw'
GWRITE='https://search.google.com/local/writereview?placeid=ChIJfT1eZ8mdiYgRRodK3oOmLRw'
GMAPS='https://www.google.com/maps/place/?q=place_id:ChIJfT1eZ8mdiYgRRodK3oOmLRw'
FORM_ENDPOINT='https://formsubmit.co/ajax/'+LEAD_EMAIL
G_ICON='<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-7.9l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>'
ROOF='<svg class="roof" viewBox="0 0 500 120" aria-hidden="true"><path d="M10 110 L170 20 L330 110" fill="none" stroke="#fff" stroke-width="16"/><rect x="200" y="75" width="40" height="30" fill="#fff"/><rect x="360" y="75" width="40" height="30" fill="#fff"/><path d="M300 110 L400 50 L500 110" fill="none" stroke="#fff" stroke-width="16"/></svg>'

def icon(paths): return f'<svg viewBox="0 0 64 64" fill="none" stroke="#375875" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
ICONS=[
 ('Downsizing',icon('<path d="M6 30 L22 16 L38 30"/><path d="M10 27v24h24V27"/><path d="M34 40 L46 30 L58 40"/><path d="M38 37v14h16V37"/><path d="M28 10h10M34 6l4 4-4 4"/>')),
 ('Foreclosure',icon('<path d="M8 30 L32 10 L56 30"/><path d="M14 25v29h36V25"/><rect x="24" y="30" width="16" height="12"/><path d="M28 30v-3a4 4 0 0 1 8 0v3"/><path d="M32 35v3"/>')),
 ('Bankruptcy',icon('<rect x="8" y="12" width="20" height="40"/><path d="M14 20h8M14 28h8M14 36h8"/><path d="M36 20 L56 44"/><path d="M36 44 L44 34 50 40 56 30"/><path d="M34 52h24"/>')),
 ('No Equity',icon('<circle cx="32" cy="28" r="14"/><path d="M36 22c-1-2-3-3-5-3-3 0-5 2-5 4 0 6 11 3 11 9 0 2-2 4-6 4-2 0-4-1-5-3M31 17v3M31 36v3"/><path d="M14 50h36M20 56h24"/>')),
 ('Retirement',icon('<path d="M10 54 L10 30 L22 22 L34 30 L34 54Z"/><path d="M18 54V40h8v14"/><circle cx="46" cy="18" r="6"/><path d="M46 24v14l-6 16M46 38l6 16M40 30h12"/>')),
 ('Damaged',icon('<path d="M8 30 L32 10 L56 30"/><path d="M14 25v29h36V25"/><path d="M30 10 L26 22 L34 28 L28 40"/><path d="M38 54v-12h-8"/><path d="M4 58h56"/>')),
 ('Needs Repairs',icon('<path d="M8 30 L32 10 L56 30"/><path d="M14 25v29h36V25"/><path d="M24 48 L38 34"/><path d="M36 30a6 6 0 1 0 6 6l-3-3"/><path d="M22 46l-2 4 4-2"/>')),
 ('Divorce',icon('<path d="M8 30 L22 18 L30 25"/><path d="M12 27v25h14"/><path d="M34 25 L42 18 L56 30"/><path d="M52 27v25H38"/><path d="M32 14 L29 26 L35 34 L30 54" stroke-dasharray="4 3"/>')),
]

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=Source+Sans+3:wght@400;700&display=swap" rel="stylesheet">'

def head(title,desc,canon,extra=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="https://hhbal.com{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://hhbal.com/img/hero.webp"><meta name="theme-color" content="#375875">
<link rel="icon" href="/favicon.png">{FONTS}<link rel="stylesheet" href="/styles.css">{extra}</head><body>'''

HEADER=f'''<header class="hdr"><div class="wrap"><a class="logo" href="/" aria-label="Hometown Home Buyers home"><img src="/img/logo.webp" width="453" height="120" alt="Hometown Home Buyers – Real Estate Investments"></a>
<button class="menu-btn" aria-label="Menu" onclick="document.querySelector('.nav').classList.toggle('open')"><span></span><span></span><span></span></button>
<nav class="nav"><a href="/">Home</a><a href="/#reviews">Success Stories</a><a href="/#offer">Get A Cash Offer</a><a class="btn" href="{TEL}">{PHONE}</a></nav></div></header>'''

CONSENT_TXT=f'I agree to receive text messages from Hometown Home Buyers about my property, appointment scheduling, updates, and general questions. Reply STOP to opt out or HELP for help. Message frequency varies. Message and data rates may apply. See our <a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms of Use</a> to learn how your information is used.'

def form(fid, comments=False):
    c=f'<label for="{fid}-c">Anything else we should know?</label><input type="text" id="{fid}-c" name="comments" autocomplete="off">' if comments else ''
    return f'''<form class="lead" id="{fid}" action="{FORM_ENDPOINT}" method="POST" novalidate>
<input type="hidden" name="_subject" value="New cash offer request – hhbal.com"><input type="hidden" name="_template" value="table"><input type="hidden" name="form" value="{fid}">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<label for="{fid}-a">Property Address <span class="req">*</span></label><input type="text" id="{fid}-a" name="property_address" placeholder="Enter Your Address" autocomplete="street-address" required>
<div class="row2"><div><label for="{fid}-p">Phone <span class="req">*</span></label><input type="tel" id="{fid}-p" name="phone" autocomplete="tel" inputmode="tel" required></div>
<div><label for="{fid}-e">Email</label><input type="email" id="{fid}-e" name="email" autocomplete="email"></div></div>{c}
<label>SMS Consent</label><div class="consent"><input type="checkbox" id="{fid}-s" name="sms_consent" value="Yes"><label for="{fid}-s" style="margin:0;font-size:inherit">{CONSENT_TXT}</label></div>
<button class="btn btn-block" type="submit">Get Your Offer</button><div class="msg" role="status" aria-live="polite"></div></form>'''

def gbadge(): return f'<a class="gbadge" href="{GREVIEWS}" target="_blank" rel="noopener">{G_ICON}<div><b>5.0</b> <span class="stars">★★★★★</span><small>32 Google reviews</small></div></a>'

FOOTER=f'''<footer class="ftr"><div class="wrap"><div class="cols">
<div class="flogo"><img src="/img/logo.webp" width="453" height="120" alt="Hometown Home Buyers" loading="lazy">{gbadge()}</div>
<div><h4>Quick Links</h4><ul><li><a href="/#reviews">Success Stories</a></li><li><a href="/#offer">Get An Offer</a></li><li><a href="/faq.html">FAQ</a></li><li><a href="/#contact">Contact Us</a></li></ul></div>
<div id="contact"><h4>Contact Us</h4><ul><li><a href="{TEL}" style="color:var(--accent-d);text-decoration:underline">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>7050 Gadsden Hwy<br>Trussville, AL 35173</li><li>8195 US-11<br>Springville, AL 35146</li><li>Servicing the Southeast</li></ul></div>
</div><p class="legal">{CONSENT_TXT.replace(" and <a href=\"/terms.html\">Terms of Use</a>","")}</p><p class="copy">© 2026 Hometown Home Buyers LLC · hhbal.com</p></div></footer>
<div class="callbar"><a href="{TEL}">📞 Call {PHONE}</a><a href="{SMS}">💬 Text Us</a></div>
<script src="/main.js" defer></script></body></html>'''

REVIEWS=[  # real Google review snippets (Google Maps place data, Nov 6 2026); full text and reviewer names not publicly retrievable without sign-in
 ("Josh gave us the best offer for our house in Georgia with CASH OFFER.",'G'),
 ("Great company to work with.",'G'),
]
def rcards():
    out=[]
    for txt,_ in REVIEWS:
        out.append(f'''<div class="rcard"><div class="bubble"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><p>“{txt}”</p></div>
<div class="who"><div class="av">G{G_ICON}</div><div><b>Google reviewer</b><small>5-star review · excerpt</small></div></div></div>''')
    out.append(f'''<div class="rcard summary"><div class="bubble"><div class="big">5.0</div><div class="stars">★★★★★</div><p>Average from <b>32</b> Google reviews</p><p style="margin-top:8px"><a href="{GREVIEWS}" target="_blank" rel="noopener">Read them all on Google →</a></p></div>
<div class="who"><div class="av" style="background:var(--brand)">H</div><div><b>Hometown Home Buyers LLC</b><small>Springville, AL</small></div></div></div>''')
    return '\n'.join(out)

index=head('Sell My House Fast for Cash in Alabama | Hometown Home Buyers','Sell your house fast for cash in Springville, St. Clair County, and the Birmingham area. No commissions, no fees, no repairs. Call 205-914-4215 for a fair cash offer.','/',
 '<link rel="preload" as="image" href="/img/hero-m.webp" media="(max-width:900px)"><link rel="preload" as="image" href="/img/hero.webp" media="(min-width:901px)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"RealEstateAgent","name":"Hometown Home Buyers LLC","url":"https://hhbal.com","telephone":"+1-205-914-4215","email":"joshua@hhbal.com","address":{"@type":"PostalAddress","addressLocality":"Springville","addressRegion":"AL","postalCode":"35146","addressCountry":"US"},"areaServed":"Southeastern United States"}</script>')+HEADER+f'''
<main>
<section class="hero" id="offer"><div class="wrap"><div><h1>Sell Your House Fast With Hometown Home Buyers</h1><p>Selling your Alabama home just got simple. No commissions. No fees.<br>We buy AS-IS, and there's no realtor needed.</p></div>
<div>{form('lead-top')}</div></div></section>

<section class="why"><div class="wrap"><h2>Why Should You Choose Hometown Home Buyers?</h2>
<div class="grid"><div class="ph"><img src="/img/why.webp" width="800" height="600" alt="Brick ranch home in St. Clair County, Alabama" loading="lazy"><div class="tag"><img src="/img/logo.webp" width="113" height="30" alt=""></div></div>
<div class="txt"><p>We're a family-owned, Springville-based home buying company that finds win-win solutions for Alabama homeowners in tough spots.</p>
<p>Selling to us skips the headaches of a traditional listing. Our process is quick and straightforward, and you choose the move-out date that works for you. The cash price we agree on is the cash you walk away with: no agent commissions and no closing costs.</p>
<p>We buy houses AS-IS and close on your schedule. No repairs, no clean-out, no showings. Leave it exactly the way it is and we'll still make you a fair offer. Want to know what your home is worth in cash? Call or text <a href="{TEL}">{PHONE}</a> or fill out the form.</p></div></div>
<div class="stats"><div class="stat"><b data-count="2295">2,295</b><span>Cash Offers Made &amp; Counting</span></div><div class="stat"><b data-count="100" data-suffix="%">100%</b><span>Satisfied Customers</span></div><div class="stat"><b data-count="153">153</b><span>Houses Bought</span></div></div>
<div class="center"><a class="btn" href="#offer">Get An Offer</a></div></div></section>

<section class="how"><div class="wrap"><h2>How It Works</h2><div class="cards">
<div class="step"><div class="num">01</div><div class="card"><img src="/img/step1.webp" width="800" height="600" alt="Homeowner calling on a phone" loading="lazy"><h3>Request Your Offer</h3><p>Call or text us at <a href="{TEL}">{PHONE}</a> or fill out the form on this page. We'll ask a few quick questions so we understand your home's condition and your goals.</p></div></div>
<div class="step"><div class="num">02</div><div class="card"><img src="/img/step2.webp" width="800" height="600" alt="Happy couple reviewing their cash offer" loading="lazy"><h3>Get Your Cash Offer</h3><p>Once we've looked at your property, we'll give you a no-obligation, all-cash offer, often the same day. Say yes or no. There are no fees and no pressure.</p></div></div>
<div class="step"><div class="num">03</div><div class="card"><img src="/img/step3.webp" width="800" height="600" alt="Couple carrying moving boxes" loading="lazy"><h3>Sign &amp; Close</h3><p>When we agree on a price, you pick the closing date. We close with a local title company and you get paid. We work around your schedule, not ours!</p></div></div>
</div></div>{ROOF}</section>

<section class="band"><div class="wrap"><img class="lg" src="/img/logo.webp" width="453" height="120" alt="Hometown Home Buyers" loading="lazy"><ul><li>We Can Buy Your House Fast</li><li>We Keep The Process Easy</li><li>You Won't Pay Hidden Fees</li></ul></div></section>

<section class="sit"><div class="wrap"><h2 class="center">We Buy Alabama Houses For Cash “As-Is”, Whatever The Condition!</h2>
<p class="lead-p">At Hometown Home Buyers, a house never has to be perfect. We buy every kind of property, from Springville and St. Clair County to Birmingham, so you can close fast and keep more money in your pocket!</p>
<div class="icons">{''.join(f'<div>{s}<span>{n}</span></div>' for n,s in ICONS)}</div>
<div class="center"><a class="btn" href="{TEL}">Call {PHONE}</a></div></div></section>

<section class="stories" id="reviews"><div class="wrap"><h2>Customer Success Stories</h2>
<div class="rbox"><h3>What our customers say</h3>
<div class="rhead"><div><div class="gname">{G_ICON}<span>Google Reviews</span></div><div class="rscore"><b>5.0</b><span class="stars">★★★★★</span><small>(32)</small></div></div><a class="rbtn" href="{GWRITE}" target="_blank" rel="noopener">Review us on Google</a></div>
<div class="rgrid">{rcards()}</div>
<div class="rmore"><a href="{GREVIEWS}" target="_blank" rel="noopener">See All 32 Reviews</a></div></div>
<div class="center"><a class="btn" href="#offer">Get Offer</a></div></div>{ROOF}</section>

<section class="cta-final" id="get-offer"><div class="wrap"><h2>We Buy Houses At Any Price and In Any Condition!</h2>{form('lead-bottom')}</div></section>
</main>'''+FOOTER

def sub(fn,title,desc,body):
    open(f'{OUT}/{fn}','w').write(head(title,desc,'/'+fn)+HEADER+f'<main class="wrap page">{body}</main>'+FOOTER)

open(f'{OUT}/index.html','w').write(index)
FAQ=[
("How fast can you close?","Usually in as little as 7–14 days, depending on title work. If you need more time, you pick the date that works for you."),
("Do I have to make repairs or clean out the house?","No. We buy as-is. Take what you want and leave the rest. We'll handle it."),
("Are there any fees or commissions?","No. There are no agent commissions and no hidden fees, and in most cases we cover the normal closing costs."),
("How do you decide on my offer?","We look at your home's location, condition, needed repairs, and recent nearby sales. Then we give you a fair, no-obligation cash offer."),
("What areas do you buy in?","We're servicing the Southeast. Call and ask about your area."),
("Is there any obligation?","None. If our offer doesn't work for you, just say no thanks."),
]
sub('faq.html','FAQ | Hometown Home Buyers','Common questions about selling your Alabama house for cash to Hometown Home Buyers.',
 '<h1>Frequently Asked Questions</h1><div class="faq">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)+f'</div><p style="margin-top:30px"><a class="btn" href="/#offer">Get Your Cash Offer</a> &nbsp; or call <a href="{TEL}">{PHONE}</a></p>')
sub('privacy.html','Privacy Policy | Hometown Home Buyers','Privacy policy for hhbal.com.',f'''<h1>Privacy Policy</h1><p>Hometown Home Buyers LLC ("we") collects the information you submit on this website, such as your property address, phone number, email, and comments, only so we can respond to your request and discuss buying your property.</p>
<p><b>Text messages:</b> If you check the SMS consent box, we may text you about your property, appointments, and updates. Message frequency varies and message and data rates may apply. Reply STOP to opt out or HELP for help. We do not sell or share your mobile number or SMS consent with third parties or affiliates for their marketing.</p>
<p>We do not sell your personal information. Form submissions go through a third-party form service (FormSubmit) and are delivered to our email. Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="{TEL}">{PHONE}</a>.</p>''')
sub('terms.html','Terms of Use | Hometown Home Buyers','Terms of use for hhbal.com.',f'''<h1>Terms of Use</h1><p>Information on this website is for general purposes only. Submitting a form does not create any obligation to sell or buy. Any offer from Hometown Home Buyers LLC is subject to a property review and a signed written agreement.</p><p>Hometown Home Buyers LLC buys property as a principal and is not acting as your real estate agent. You may wish to consult a licensed agent or attorney before you sell.</p><p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{TEL}">{PHONE}</a></p>''')
sub('thank-you.html','Thank You | Hometown Home Buyers','Thanks for your request.',f'<h1>Thank you!</h1><p>We got your info and will reach out shortly. Need us sooner? Call or text <a href="{TEL}">{PHONE}</a>.</p>')
print('built')
