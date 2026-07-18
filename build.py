#!/usr/bin/env python3
"""Capital Sawmill site generator — builds static pages with shared header/footer."""
import os, pathlib

SITE = pathlib.Path('/root/capital-sawmill/site')

PHONE_DISPLAY = "(518) 479-0729"
PHONE_TEL = "tel:5184790729"
EMAIL = "Steven@CapitalSawmill.com"
ADDRESS = "4119 US HIGHWAY 20. NASSAU, NY 12123"

SVG_PHONE = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M493.4 24.6l-104-24c-11.3-2.6-22.9 3.3-27.5 13.9l-48 112c-4.2 9.8-1.4 21.3 6.9 28l60.6 49.6c-36 76.7-98.9 140.5-177.2 177.2l-49.6-60.6c-6.8-8.3-18.2-11.1-28-6.9l-112 48C3.9 366.5-2 378.1.6 389.4l24 104C27.1 504.2 36.7 512 48 512c256.1 0 464-207.5 464-464 0-11.2-7.7-20.9-18.6-23.4z"/></svg>'
SVG_MARKER = '<svg aria-hidden="true" viewBox="0 0 384 512" fill="currentColor"><path d="M172.268 501.67C26.97 291.031 0 269.413 0 192 0 85.961 85.961 0 192 0s192 85.961 192 192c0 77.413-26.97 99.031-172.268 309.67-9.535 13.774-29.93 13.773-39.464 0zM192 272c44.183 0 80-35.817 80-80s-35.817-80-80-80-80 35.817-80 80 35.817 80 80 80z"/></svg>'
SVG_ENVELOPE = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M502.3 190.8c3.9-3.1 9.7-.2 9.7 4.7V400c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V195.6c0-5 5.7-7.8 9.7-4.7 22.4 17.4 52.1 39.5 154.1 113.6 21.1 15.4 56.7 47.8 92.2 47.6 35.7.3 72-32.8 92.3-47.6 102-74.1 131.6-96.3 154-113.7zM256 320c23.2.4 56.6-29.2 73.4-41.4 132.7-96.3 142.8-104.7 173.4-128.7 5.8-4.5 9.2-11.5 9.2-18.9v-19c0-26.5-21.5-48-48-48H48C21.5 64 0 85.5 0 112v19c0 7.4 3.4 14.3 9.2 18.9 30.6 23.9 40.7 32.4 173.4 128.7 16.8 12.2 50.2 41.8 73.4 41.4z"/></svg>'
SVG_CLOCK = '<svg aria-hidden="true" viewBox="0 0 512 512" fill="currentColor"><path d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm57.1 350.1L224.9 294c-3.1-2.3-4.9-5.9-4.9-9.7V116c0-6.6 5.4-12 12-12h48c6.6 0 12 5.4 12 12v137.7l63.5 46.2c5.4 3.9 6.5 11.4 2.6 16.8l-28.2 38.8c-3.9 5.3-11.4 6.5-16.8 2.6z"/></svg>'
SVG_FB = '<svg aria-hidden="true" viewBox="0 0 320 512" fill="currentColor"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>'
SVG_IG = '<svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>'
SVG_LI = '<svg aria-hidden="true" viewBox="0 0 448 512" fill="currentColor"><path d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"/></svg>'
SVG_TRUCK = '<svg aria-hidden="true" viewBox="0 0 640 512" fill="currentColor"><path d="M624 352h-16V243.9c0-12.7-5.1-24.9-14.1-33.9L494 110.1c-9-9-21.2-14.1-33.9-14.1H416V48c0-26.5-21.5-48-48-48H48C21.5 0 0 21.5 0 48v320c0 26.5 21.5 48 48 48h16c0 53 43 96 96 96s96-43 96-96h128c0 53 43 96 96 96s96-43 96-96h48c8.8 0 16-7.2 16-16v-32c0-8.8-7.2-16-16-16zM160 464c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm320 0c-26.5 0-48-21.5-48-48s21.5-48 48-48 48 21.5 48 48-21.5 48-48 48zm80-208H416V144h44.1l99.9 99.9V256z"/></svg>'

GA_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=swap" rel="stylesheet">'''

def head(title, desc, root='', leaflet=False):
    lf = ''
    if leaflet:
        lf = '''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{root}assets/img/capital-sawmill-logo.png">
{GA_FONTS}
{lf}
<link rel="stylesheet" href="{root}assets/css/main.css">
</head>
<body>'''

def header(root=''):
    return f'''
<header id="header">
  <div id="top-info">
    <div class="container">
      <div class="bar-inner">
        <div class="bar-item" id="estimate"><a id="estimate-modal-button" href="{root}contact/">Get A Free Estimate!</a></div>
        <div class="bar-item" id="top-phone"><a href="{PHONE_TEL}">{SVG_PHONE} {PHONE_DISPLAY}</a></div>
        <div class="bar-item" id="top-address"><a href="https://www.google.com/maps/place/Capital+Sawmill+Service,+LLC+Tree+Service+%26+More/@42.5377159,-73.6647907,17z" target="_blank" rel="noopener">{SVG_MARKER} {ADDRESS}</a></div>
      </div>
    </div>
  </div>

  <div id="main-menu">
    <div class="container">
      <div id="main-menu-container">
        <nav id="main-nav">
          <ul>
            <li>
              <a id="main-nav-home" href="{root}">Capital Sawmill&trade;</a>
              <div class="sub-menu">
                <ul>
                  <li><a href="{root}about/">About Us</a></li>
                  <li><a href="{root}#service-area-section">Who We Serve</a></li>
                  <li><a href="{root}firewood/">Firewood</a></li>
                </ul>
              </div>
            </li>
            <li>
              <a href="{root}wood-slabs/">Wood Slabs</a>
              <div id="nav-all-wood-slabs" class="sub-menu">
                <div id="nav-common-woods">
                  <p>Common</p>
                  <ul id="nav-common-woods-col1">
                    <li><a href="{root}wood-slabs/#walnut"><div class="nav-wood-sample ws-walnut"></div><p>Walnut</p></a></li>
                    <li><a href="{root}wood-slabs/#maple"><div class="nav-wood-sample ws-maple"></div><p>Maple</p></a></li>
                    <li><a href="{root}wood-slabs/#oak"><div class="nav-wood-sample ws-oak"></div><p>Oak</p></a></li>
                  </ul>
                  <ul id="nav-common-woods-col2">
                    <li><a href="{root}wood-slabs/#cherry"><div class="nav-wood-sample ws-cherry"></div><p>Cherry</p></a></li>
                    <li><a href="{root}wood-slabs/#pine"><div class="nav-wood-sample ws-pine"></div><p>Pine</p></a></li>
                  </ul>
                </div>
                <div id="nav-specialty-slabs">
                  <p>Specialty Slabs</p>
                  <ul>
                    <li><a href="{root}wood-slabs/#honey-locust">Honey Locust</a></li>
                    <li><a href="{root}wood-slabs/#sycamore">Sycamore</a></li>
                    <li><a href="{root}wood-slabs/#box-elder-maple">Box Elder Maple</a></li>
                    <li><a href="{root}wood-slabs/#catalpa">Catalpa</a></li>
                  </ul>
                </div>
              </div>
            </li>
            <li>
              <a href="{root}wood-products/">Wood Products</a>
              <div class="sub-menu">
                <ul>
                  <li><a href="{root}wood-products/#bartops">Bartops</a></li>
                  <li><a href="{root}wood-products/#table-tops">Table Tops</a></li>
                  <li><a href="{root}wood-products/#mantels">Mantels</a></li>
                  <li><a href="{root}wood-products/#deer-plaques">Deer Plaque Mounts</a></li>
                  <li><a href="{root}firewood/">Firewood</a></li>
                </ul>
              </div>
            </li>
            <li>
              <a href="{root}tree-removal/">Tree Removal</a>
            </li>
            <li id="header-contact-button"><a href="{root}contact/">Contact</a></li>
          </ul>
        </nav>
        <div id="capital-sawmill-logo"><a href="{root}"><img src="{root}assets/img/capital-sawmill-logo.png" width="144" height="80" alt="Capital Sawmill Service, LLC"></a></div>
      </div>
      <div class="clear-float"></div>
    </div>
  </div>
</header>'''

def plank(text, small=False, alt=False, tag='h2', anchor=''):
    cls = 'plank small' if small else 'plank'
    if alt: cls += ' alt'
    a = f' id="{anchor}"' if anchor else ''
    return f'<div class="plank-wrap"{a}><div class="{cls}"><{tag}>{text}</{tag}></div></div>'

def footer(root=''):
    return f'''
<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="{root}assets/img/capital-sawmill-logo.png" width="144" height="80" alt="Capital Sawmill logo" style="margin-bottom:12px">
        <ul class="contact-info-list">
          <li><a href="{PHONE_TEL}">{SVG_PHONE} {PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{SVG_ENVELOPE} {EMAIL}</a></li>
          <li>{SVG_MARKER} 4119 US Highway 20, Nassau, NY 12123</li>
        </ul>
        <ul id="footer-social-links">
          <li><a href="https://www.facebook.com/CapitalSawmill" target="_blank" rel="noopener" aria-label="Facebook">{SVG_FB}</a></li>
          <li><a href="https://www.instagram.com/capitalsawmillservice" target="_blank" rel="noopener" aria-label="Instagram">{SVG_IG}</a></li>
          <li><a href="https://www.linkedin.com/company/capital-sawmill-service-llc" target="_blank" rel="noopener" aria-label="LinkedIn">{SVG_LI}</a></li>
        </ul>
      </div>
      <div>
        <h3>Come Visit Us</h3>
        <p>{SVG_CLOCK} Monday &ndash; Saturday<br>8AM &ndash; 6PM</p>
        <h3>Explore</h3>
        <p style="line-height:2.1">
          <a href="{root}wood-slabs/">Wood Slabs</a><br>
          <a href="{root}wood-products/">Wood Products</a><br>
          <a href="{root}tree-removal/">Tree Removal</a><br>
          <a href="{root}firewood/">Firewood</a><br>
          <a href="{root}about/">About Us</a><br>
          <a href="{root}contact/">Contact</a>
        </p>
      </div>
      <div id="footer-map">
        <h3>Find the Mill</h3>
        <iframe title="Capital Sawmill location map" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d47035.36349320028!2d-73.69139819585202!3d42.54021004225813!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xd58ee223ea17ec14!2sCapital+Sawmill+Service!5e0" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy;2026 Capital Sawmill Service, LLC. All Rights Reserved.</span>
      <span><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
    </div>
  </div>
</footer>

<div id="sticky-call"><a href="{PHONE_TEL}">{SVG_PHONE} CALL STEVE &mdash; {PHONE_DISPLAY}</a></div>

<script src="{root}assets/js/main.js"></script>
</body>
</html>'''

# ================= PAGE BODIES =================

def call_cta(center=True, dark=False):
    style = ' style="text-align:center;margin-top:34px"' if center else ''
    return f'''<div{style}>
      <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
      &nbsp; <a class="btn btn-light" href="/contact/">Get a Free Estimate</a>
    </div>'''

INDEX_BODY = f'''
<section id="hero">
  <video autoplay muted loop playsinline poster="assets/img/hero-poster.jpg">
    <source src="assets/vid/header.mp4" type="video/mp4">
  </video>
  <div class="hero-shade"></div>
  <div class="hero-copy">
    <h1>Problem Trees In.<br>Beautiful Lumber Out.</h1>
    <p class="hero-sub">Expert tree removal and custom sawmilling in the Capital Region &mdash; hire us for either, or let us mill the tree in your yard into a slab worth keeping.</p>
    <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
    &nbsp; <a class="btn btn-light" href="contact/">Get a Free Estimate</a>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    {plank('One Crew. Two Trades.')}
    <div class="trades">
      <a class="trade-card" href="tree-removal/">
        <div class="trade-bg" data-parallax="0.06" style="background-image:url(assets/img/07-14-009.jpg)"></div>
        <div class="trade-body">
          <h3>Tree Services</h3>
          <p>Removal, pruning, stump grinding, land clearing &mdash; 30+ years of taking down trees of any size, safely, and leaving the place looking great.</p>
          <span class="btn btn-call">Explore Tree Services</span>
        </div>
      </a>
      <a class="trade-card" href="wood-slabs/">
        <div class="trade-bg" data-parallax="0.06" style="background-image:url(assets/img/wood-slabs-on-forklift.jpg)"></div>
        <div class="trade-body">
          <h3>Sawmill Services</h3>
          <p>Custom lumber, live-edge slabs up to 30&Prime; wide, on-site milling with our portable mill &mdash; and nationwide shipping on slabs and logs.</p>
          <span class="btn btn-maroon">Explore the Sawmill</span>
        </div>
      </a>
    </div>
    <p class="bridge"><strong>Here&rsquo;s what makes us different:</strong> most tree services haul your tree to the chipper. We can haul it to the mill &mdash; and hand it back to you as a bartop, mantel, or heirloom table. One call does both jobs.</p>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-dark">
  <div class="container">
    {plank('From Your Tree to Your Table', alt=True)}
    <div class="process">
      <div class="process-step">
        <img src="assets/img/07-14-009.jpg" alt="Tree removal in progress" loading="lazy">
        <div class="step-body">
          <span class="step-num">1</span>
          <h4>We Take It Down</h4>
          <p>Licensed, insured, and equipped for trees of any size &mdash; problematic or just in the way.</p>
        </div>
      </div>
      <div class="process-step">
        <img src="assets/img/milling-on-site.jpg" alt="Milling a log on site" loading="lazy">
        <div class="step-body">
          <span class="step-num">2</span>
          <h4>We Mill It</h4>
          <p>On location with our portable band sawmill, or on the big stationary mill at our shop in Nassau.</p>
        </div>
      </div>
      <div class="process-step">
        <img src="assets/img/finished-walnut-slab.jpg" alt="Finished walnut slab" loading="lazy">
        <div class="step-body">
          <span class="step-num">3</span>
          <h4>You Keep It</h4>
          <p>Your tree comes back as slabs, beams, or a finished piece &mdash; lumber with a story you already know.</p>
        </div>
      </div>
    </div>
    <div class="split" style="margin-top:56px">
      <div>
        <h3 style="font-family:'Roboto Condensed',sans-serif;text-transform:uppercase;letter-spacing:3px;color:#fff;font-size:24px">Watch How It&rsquo;s Done</h3>
        <p>Whether you have a tree that you want turned into lumber or you&rsquo;re looking for that perfect slab of wood for your next project, Capital Sawmill has you covered. We can mill on location or even ship slabs all across the United States. Our friendly staff makes getting the right slab of wood a hassle-free process that won&rsquo;t break the bank.</p>
        <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Talk It Through With Steve</a>
      </div>
      <div class="video-embed">
        <iframe title="How Problematic Trees are Turned into Custom Lumber" src="https://www.youtube-nocookie.com/embed/0YnnWF1ilhc" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    {plank('Wood Slabs &amp; Milling')}
    <div class="split">
      <div class="split-img"><img src="assets/img/IMG_0446.jpg" alt="Live-edge wood slabs" loading="lazy" data-parallax="0.05"></div>
      <div>
        <p>We create custom lumber used for a variety of applications including bar tops, tables, counters, mantels, and much more. We carry a variety of locally sourced wood and offer both wholesale and finished products &mdash; slabs up to 30&Prime; wide, air-dried under cover for up to two years.</p>
        <p><a class="btn btn-maroon" href="wood-slabs/">Buy Wood Slabs</a> &nbsp; <a class="btn btn-call" href="wood-products/">Browse Wood Products</a></p>
      </div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section">
  <div class="container">
    {plank('Residential &amp; Commercial Tree Services', alt=True)}
    <p style="max-width:860px;margin:0 auto 34px;text-align:center">With over 30 years of experience, our tree experts trim or remove trees of any size that are unwanted or problematic. We handle all facets of tree care &mdash; removal, pruning, stump grinding, lacing, thinning, and crown reduction &mdash; and we get the job done in a timely fashion, leaving the place looking great. Call now for a free consultation and we&rsquo;ll quickly show you why we&rsquo;re the Albany area&rsquo;s favorite tree &amp; sawmill company.</p>
    <div class="service-tiles">
      <a class="service-tile" href="tree-removal/"><img src="assets/img/tree-pruning.jpg" alt="Tree pruning" loading="lazy"><span>Tree Pruning</span></a>
      <a class="service-tile" href="tree-removal/"><img src="assets/img/land-clearing.jpg" alt="Land clearing" loading="lazy"><span>Land Clearing</span></a>
      <a class="service-tile" href="tree-removal/"><img src="assets/img/stump-grinding.jpg" alt="Stump grinding" loading="lazy"><span>Stump Grinding</span></a>
      <a class="service-tile" href="tree-removal/"><img src="assets/img/milling-on-site.jpg" alt="Milling on site" loading="lazy"><span>Milling on Site</span></a>
      <a class="service-tile" href="tree-removal/"><img src="assets/img/wood-chipping.jpg" alt="Wood chipping" loading="lazy"><span>Wood Chipping</span></a>
      <a class="service-tile" href="tree-removal/"><img src="assets/img/debris-removal.jpg" alt="Debris removal" loading="lazy"><span>Debris Removal</span></a>
    </div>
    {call_cta()}
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    {plank('Firewood')}
    <div class="split">
      <div>
        <p>Feed your wood-stove during those cold New York winter nights. Quality seasoned mixed hardwoods, stored clean and dry under our pavilion, available by the face cord &mdash; dumped at your place. Camp wood, kindling kegs, and smoker chunks available too.</p>
        <p><a class="btn btn-call" href="firewood/">Firewood Pricing &amp; Availability</a></p>
      </div>
      <div class="split-img"><img src="assets/img/wp-firewood.jpg" alt="Seasoned firewood" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<section class="section section-dark" id="service-area-section">
  <div class="container">
    {plank('Areas We Service', alt=True)}
    <div class="map-frame"><div id="service-map"></div></div>
    <div class="town-chips">
      <span>Albany</span><span>Chatham</span><span>Rensselaer</span><span>Columbia</span><span>Schenectady</span><span>East Greenbush</span><span>Troy</span><span>Cohoes</span><span>Latham</span><span>Colonie</span><span>Westmere</span><span>Delmar</span><span>Wynantskill</span><span>Westerlo</span><span>Rotterdam</span><span>New Lebanon</span><span>Ghent</span><span>Petersburg</span>
    </div>
    <p class="nationwide-note">{SVG_TRUCK.replace('<svg ', '<svg style="width:20px;height:20px;vertical-align:-3px;margin-right:8px" ')} <strong>Custom lumber ships nationwide.</strong> For the right tree job we&rsquo;ll occasionally travel outside this area, too &mdash; <a href="{PHONE_TEL}">give us a call</a>.</p>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    {plank('What Neighbors Say')}
    <div class="testimonials">
      <blockquote class="testimonial">
        I want to thank you again for your prompt and very professional response to our tree problem. I was home and was able to see the tree removal process and the clean-up as well. All of you are a real credit to your business. Neither my wife nor I will hesitate to call upon you again.
        <cite>John Walden</cite>
      </blockquote>
      <blockquote class="testimonial">
        Capital Sawmill has done tree work for us at 3 different times. We needed tree and stump removal and extensive trimming on very old, large maples. Steve and his crew did a terrific job. The entire team was very pleasant, the price was fair and the crew cleaned the area of all brush. I would recommend Capital Sawmill very highly.
        <cite>Mary LaFleur</cite>
      </blockquote>
      <blockquote class="testimonial">
        I would like to thank you again for the amazing job you did at our house. We appreciate that you were able to come so quickly &mdash; it was comforting to know TRUE professionals were on the job! Thanks again!
        <cite>Billy Lauritsen</cite>
      </blockquote>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {plank('Frequently Asked Questions', alt=True)}
    <div class="faq">
      <details>
        <summary>Do you remove valuable wood in exchange for the lumber?</summary>
        <div class="faq-a">Unfortunately no. The high cost of vehicles, machinery, labor, insurance, and fuel to cut and process the wood versus the value of the wood itself doesn&rsquo;t enable us to do that.</div>
      </details>
      <details>
        <summary>Do you carry common building-supply wood like 2x4&rsquo;s?</summary>
        <div class="faq-a">We cut larger wood specific for custom needs. Common building-supply wood can and should be purchased cheaper through stores like Home Depot and Lowes due to their mass production of it.</div>
      </details>
      <details>
        <summary>Can you turn MY tree into lumber I keep?</summary>
        <div class="faq-a">Yes &mdash; that&rsquo;s our specialty. We can take down your tree and mill it on site with our portable band sawmill, or bring it back to our stationary mill in Nassau. You end up with slabs, beams, or a finished piece from a tree you already own. Call us and tell us about the tree.</div>
      </details>
    </div>
  </div>
</section>

<section class="section section-dark" id="contact-section">
  <div class="container">
    {plank('The Fastest Way to Reach Us? Call.')}
    <div class="call-panel">
      <p style="max-width:640px;margin:0 auto">Steve answers his phone, not his inbox. For estimates, slab availability, or a straight answer about your tree &mdash; call.</p>
      <a class="big-phone" href="{PHONE_TEL}">{SVG_PHONE.replace('<svg ', '<svg style="width:30px;height:30px;margin-right:14px" ')}{PHONE_DISPLAY}</a>
      <p class="call-note">Monday &ndash; Saturday, 8AM &ndash; 6PM &middot; Nassau, NY</p>
    </div>
    <div class="contact-grid">
      <div>
        <h3 style="font-family:'Roboto Condensed',sans-serif;text-transform:uppercase;letter-spacing:2px;color:#fff">Rather write it down?</h3>
        <form id="estimate-form" class="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="New estimate request from capitalsawmill.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Full Name*" required>
          <input type="email" name="email" placeholder="Email*" required>
          <input type="tel" name="phone" placeholder="Phone (so we can call you back)">
          <textarea name="message" placeholder="Tell us about your tree or your project&hellip;"></textarea>
          <button class="btn btn-maroon" type="submit">Send Message</button>
        </form>
      </div>
      <div>
        <h3 style="font-family:'Roboto Condensed',sans-serif;text-transform:uppercase;letter-spacing:2px;color:#fff">Or swing by the mill</h3>
        <ul class="contact-info-list">
          <li>{SVG_MARKER} 4119 US Highway 20, Nassau, NY 12123</li>
          <li>{SVG_CLOCK} Monday &ndash; Saturday, 8AM &ndash; 6PM</li>
          <li>{SVG_ENVELOPE} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p style="margin-top:18px">Come see the slabs in person &mdash; there&rsquo;s nothing like picking your own piece of wood.</p>
      </div>
    </div>
  </div>
</section>
'''

TREE_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/07-14-009.jpg)">
  <h1>Tree Removal</h1>
  <p>Our licensed and insured arborists remove trees of any size that are unwanted or problematic.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call for a Free Estimate</a>
</section>

<section class="section">
  <div class="container">
    <p style="max-width:860px;margin:0 auto;text-align:center;font-size:19px">The people of Capital Sawmill have been doing tree work for decades, so there truly is no job too big to handle. You can count on us to get the job done in a timely fashion and leave the place looking great. Call now for a free consultation and make us your tree service!</p>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Tree Services')}
    <div class="service-tiles">
      <div class="service-tile"><img src="../assets/img/tree-pruning.jpg" alt="Tree pruning" loading="lazy"><span>Tree Pruning</span></div>
      <div class="service-tile"><img src="../assets/img/land-clearing.jpg" alt="Land clearing" loading="lazy"><span>Land Clearing</span></div>
      <div class="service-tile"><img src="../assets/img/stump-grinding.jpg" alt="Stump grinding" loading="lazy"><span>Stump Grinding</span></div>
      <div class="service-tile"><img src="../assets/img/milling-on-site.jpg" alt="Milling on site" loading="lazy"><span>Milling on Site</span></div>
      <div class="service-tile"><img src="../assets/img/wood-chipping.jpg" alt="Wood chipping" loading="lazy"><span>Wood Chipping</span></div>
      <div class="service-tile"><img src="../assets/img/debris-removal.jpg" alt="Debris removal" loading="lazy"><span>Debris Removal</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {plank('Why Hire an Arborist?', alt=True)}
    <div class="split">
      <div>
        <p>An arborist is a specialist in the care of individual trees. Arborists are knowledgeable about the needs of trees and are trained and equipped to provide proper care. Hiring an arborist is a decision that should not be taken lightly.</p>
        <p>Proper tree care is an investment that can lead to substantial returns. Well-cared-for trees are attractive and can add considerable value to your property. Poorly maintained trees can be a significant liability. Pruning or removing trees, especially large trees, can be dangerous work &mdash; it should be done only by those trained and equipped to work safely in trees.</p>
      </div>
      <div class="split-img"><img src="../assets/img/tree-pruning.jpg" alt="Arborist pruning a tree" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-dark">
  <div class="container">
    {plank("Don&rsquo;t Chip It &mdash; Keep It")}
    <div class="split">
      <div class="split-img"><img src="../assets/img/milling-on-site.jpg" alt="Milling a removed tree on site" loading="lazy"></div>
      <div>
        <p><strong style="color:#fff">Here&rsquo;s the part most tree services can&rsquo;t offer:</strong> before your tree hits the chipper, ask us about milling it. Our portable band sawmill turns take-downs into usable lumber right in your yard &mdash; or we bring the log back to our mill. That maple shading your porch for 40 years could be your dining table for the next 40.</p>
        <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Ask About Milling Your Tree</a>
      </div>
    </div>
  </div>
</section>
'''

def species_card(anchor, name, img, body, sprite=None, strip=False):
    if img:
        thumb = f'<img src="../assets/img/{img}" alt="{name} wood" loading="lazy">'
    elif sprite:
        thumb = f'<img src="../assets/img/{sprite}" alt="{name} wood sample" loading="lazy" style="height:130px">'
    else:
        thumb = '<div style="height:26px;background:url(../assets/tex/h2-bg.jpg);background-size:600px 120px;box-shadow:inset 0 -3px 6px rgba(0,0,0,.25)"></div>'
    return f'''<div class="card" id="{anchor}">
      {thumb}
      <div class="card-body">
        <h3>{name}</h3>
        {body}
      </div>
    </div>'''

SLABS_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wood-slabs-on-forklift.jpg)">
  <h1>Custom Wood Slabs</h1>
  <p>One of a kind. Unfinished or finished, up to 30&Prime; wide &mdash; for whatever project you&rsquo;re working on.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Tell Us About Your Project</a>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p>We can mill trees at your site or ours with our portable band sawmill. We can take down your trees and mill them, or mill trees that have already been felled. Although we don&rsquo;t stock dimensional lumber, we can custom cut logs into planks of many widths and lengths, suited to fit your project &mdash; boards, beams, planks, posts, timbers, you name it.</p>
        <p>At our shop we have many woods available: free-form mantel pieces and bar tops in stock or cut to order, fireplace mantels in cherry, walnut, maple, oak, pine and more &mdash; with the natural wane of the wood or cut with square or rounded edges. Custom designed, hand-built furniture too. Call for rates, local or out-of-state.</p>
      </div>
      <div class="split-img"><img src="../assets/img/IMG_0446.jpg" alt="Stacked live-edge slabs" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Which Wood Is Right for You?')}
    <div class="species-grid">
      {species_card('walnut', 'Walnut', 'finished-walnut-slab.jpg',
        '<p>A straight-grained hardwood ranging from chocolate brown to blond. A top pick for headboards, antique-style dining tables, and mantels &mdash; typically clear-coated or oiled to bring out its color.</p><p class="pros"><strong>Pros:</strong> Very strong and stable; takes intricate carving; beautiful color.</p><p class="cons"><strong>Cons:</strong> One of the more costly woods; color varies board to board.</p>')}
      {species_card('cherry', 'Cherry', 'cherry-finished2.jpg',
        '<p>A fine, straight-grained hardwood from reddish brown to blond. Seen in carved chairs and clean-lined Shaker tables and cabinets alike.</p><p class="pros"><strong>Pros:</strong> Easily shaped, polishes well, rich unstained color.</p><p class="cons"><strong>Cons:</strong> Pricier; color can darken with age.</p>')}
      {species_card('maple', 'Maple', None,
        '<p>A creamy white hardwood, sometimes with a reddish tinge. One of the hardest species &mdash; the pick for heavy-use pieces like dressers and kitchen cabinets.</p><p class="pros"><strong>Pros:</strong> Affordable, ultra-durable, takes dark stains well.</p><p class="cons"><strong>Cons:</strong> Needs proper sealing before staining or it can blotch.</p>', sprite='sample-maple.jpg')}
      {species_card('oak', 'Oak', None,
        '<p>A very grainy hardwood in red and white varieties &mdash; the classic Arts &amp; Crafts and Mission-style wood with a distinctive wavy grain.</p><p class="pros"><strong>Pros:</strong> Very durable, resists warping, a clear finish highlights the grain beautifully.</p><p class="cons"><strong>Cons:</strong> Heavy stain can exaggerate the grain into a two-toned look.</p>', sprite='sample-oak.jpg')}
      {species_card('pine', 'Pine', None,
        '<p>An inexpensive, lightweight wood, yellowish or whitish with brown knots &mdash; the farmhouse-table classic.</p><p class="pros"><strong>Pros:</strong> Low cost, takes paint well, develops a rustic patina, resists shrinking and swelling.</p><p class="cons"><strong>Cons:</strong> Softwood &mdash; prone to scratches and dents.</p>', sprite='sample-pine.jpg')}
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="container">
    {plank('Specialty Slabs', alt=True)}
    <p style="text-align:center;max-width:800px;margin:0 auto 34px">We start with carefully selected logs from upstate New York. Lumber is stored under cover as it slowly air dries for up to two years &mdash; besides good logs, proper drying is the most important step in quality control.</p>
    <div class="species-grid">
      {species_card('honey-locust', 'Honey Locust', None,
        '<p>High quality, durable wood that polishes beautifully. Honey locust doesn&rsquo;t grow in numbers that support bulk industry &mdash; which is exactly why a slab of it is special. Also prized for posts and rails thanks to its dense, rot-resistant nature.</p>')}
      {species_card('sycamore', 'Sycamore', None,
        '<p>American Sycamore is the largest hardwood species in North America, yielding lumber with very respectable dimensions. Properly seasoned, it shows up in cabinets, butcher blocks, and barrels &mdash; quarter and rift sawn boards are especially stable and figured.</p>')}
      {species_card('box-elder-maple', 'Box Elder Maple', 'box-elder-unfinished.jpg',
        '<p>A light wood that lends itself well to furniture projects. Spalted boxelder, with its raspberry streaks, is highly prized for accent work and turnings.</p>')}
      {species_card('catalpa', 'Catalpa', 'catalpa-finished.jpg',
        '<p>Heartwood ranges from grayish tan to a rich golden brown with a straight, open grain that resembles ash. Rated durable for decay resistance &mdash; a great choice that&rsquo;s hard to find at a lumber yard.</p>')}
    </div>
    {call_cta()}
  </div>
</section>
'''

def product_section(anchor, title, img, body, dark=False, flip=False):
    cls = 'section section-dark' if dark else 'section section-cream'
    img_html = f'<div class="split-img"><img src="../assets/img/{img}" alt="{title}" loading="lazy" data-parallax="0.04"></div>'
    text_html = f'<div>{body}<p><a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Ask About Our Current Selection</a></p></div>'
    inner = (img_html + text_html) if not flip else (text_html + img_html)
    return f'''<section class="{cls}" id="{anchor}">
  <div class="container">
    {plank(title, alt=dark)}
    <div class="split">{inner}</div>
  </div>
</section>'''

PRODUCTS_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wp-bartops.jpg)">
  <h1>Wood Products</h1>
  <p>Besides wood slabs and lumber, we build and sell a variety of wood products for your project needs.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call About a Custom Piece</a>
</section>

{product_section('bartops', 'Bar Tops', 'wp-bartops.jpg',
  '<p>High quality bar tops for bars, restaurants and homes &mdash; finished, or unfinished slabs for builders and woodworkers. We specialize in customization and build to standards that stand up to the passage of time and excessive use. Our unique, durable bar tops ship to customers across the United States.</p>')}

{product_section('table-tops', 'Table Tops', 'wp-table-tops.jpg',
  '<p>Choose the type and shape of wood from the many we have available &mdash; durable table tops made your way, at an affordable price. Compatible with all kinds of bases: stylish metal brackets, A-racks, legs with rollers, whatever your build calls for. Finished or unfinished.</p>', dark=True, flip=True)}

{product_section('mantels', 'Fireplace Mantels', 'wp-mantels.jpg',
  '<p>Beautiful wooden fireplace mantels, made to your taste &mdash; plain or extravagant, classic, modern, Victorian or colonial. Available in cherry, walnut, maple, oak, pine and more, with the natural live edge of the wood or cut square. Easy to mount and assemble, shipped across the United States.</p>')}

{product_section('deer-plaques', 'Deer Plaque Mounts', 'wp-dpm.jpg',
  '<p>Looking for a befitting mount for your trophy? We specialize in deer mount plaques with lots of selection &mdash; cedar, walnut, oak, pine, and many more. Customized plaques at a very reasonable price. It will look great on any wall.</p>', dark=True, flip=True)}

{product_section('chainsaw-signs', 'Chainsaw Signs', 'wp-chainsaw-signs.jpg',
  '<p>Hand-carved chainsaw signs, custom made from our own lumber &mdash; a one-of-a-kind marker for your camp, home, or business.</p>')}

<section class="section section-dark" id="firewood-link">
  <div class="container" style="text-align:center">
    {plank('Firewood', alt=True)}
    <p style="max-width:700px;margin:0 auto 24px">Seasoned mixed hardwoods by the face cord, kindling kegs, and smoker chunks in pear, apple, hickory and cherry.</p>
    <a class="btn btn-call" href="../firewood/">Firewood Pricing &amp; Availability</a>
  </div>
</section>
'''

FIREWOOD_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/wp-firewood.jpg)">
  <h1>Firewood For Sale</h1>
  <p>We know first-hand that New York gets COLD. Keep your home nice and cozy by stocking up on firewood.</p>
  <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call to Order</a>
</section>

<section class="section">
  <div class="container">
    {plank('Firewood Prices')}
    <div class="split">
      <div>
        <p>Seasoned mixed hardwoods, cut to stove lengths of 14&Prime; to 16&Prime; and stored under a pavilion so your wood stays clean and dry. Sold in face cord increments, priced for local delivery:</p>
        <ul style="line-height:2.2;font-size:18px">
          <li><strong>$230</strong> &mdash; face cord (4x8, one tier), dumped</li>
          <li><strong>$385</strong> &mdash; double face cord (4x8, two tiers), dumped</li>
          <li><strong>$540</strong> &mdash; triple face cord (4x8, three tiers), dumped</li>
        </ul>
        <p><strong>Kindling kegs</strong> &mdash; 11&Prime; diameter, 14&Prime; long, with a convenient carrying handle &mdash; are <strong>$15</strong> and make starting a fire a snap.</p>
      </div>
      <div class="split-img"><img src="../assets/img/FW-pavillion-3.jpg" alt="Firewood stored under the pavilion" loading="lazy" data-parallax="0.04"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Smoker Wood &amp; Camp Wood', alt=True)}
    <p style="max-width:800px;margin:0 auto;text-align:center">Smoker chunks in <strong>pear, apple, hickory and cherry</strong> for $14.95 a bag (about 14&Prime; x 14&Prime;), and smoker shavings in cherry and cherry/maple for $4.95 (14&Prime; x 20&Prime;). Camp wood available too &mdash; call ahead and we&rsquo;ll have it ready.</p>
    {call_cta()}
  </div>
</section>
'''

ABOUT_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/img/history-pics.jpg);background-position:center">
  <h1>About Capital Sawmill</h1>
  <p>Three generations of tree work &mdash; and a sawmill that gives good trees a second life.</p>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p>Capital Sawmill can take down your unwanted trees, prune for more light and healthier trees, and mill take-downs into lumber on site. Owner and arborist <strong>Steven Daniels</strong> has been providing tree service for over 30 years. In 1995 he added a portable sawmill to the company to better utilize the trees removed &mdash; and the rest is history.</p>
        <p>Capital Sawmill is located southeast of Albany at 4119 US Route 20 in Nassau, and previously operated as Steven Daniels Tree Service in Westchester, New York.</p>
        {call_cta(center=False)}
      </div>
      <div class="split-img"><img src="../assets/img/100_0254-1.jpg" alt="Capital Sawmill at work" loading="lazy" data-parallax="0.05"></div>
    </div>
  </div>
</section>

<div class="grain-divider"></div>

<section class="section section-cream">
  <div class="container">
    {plank('Company History')}
    <p style="max-width:800px;margin:0 auto 26px;text-align:center">It started with <strong>Frank Daniels</strong>, Steven&rsquo;s father, running his log truck in 1981. Steven grew up in the trade &mdash; pictured in front of his own log truck in 1991, and quite the climber, going out on a limb in 1992.</p>
    <img src="../assets/img/history-pics.jpg" alt="Daniels family tree service history photos, 1981-1992" style="display:block;margin:0 auto;border-radius:6px;box-shadow:0 10px 26px rgba(0,0,0,.35)" loading="lazy">
  </div>
</section>
'''

CONTACT_BODY = f'''
<section class="page-banner" style="background-image:url(../assets/tex/footer-bg.jpg)">
  <h1>Contact Capital Sawmill</h1>
  <p>Estimates are free. Answers are fast &mdash; especially by phone.</p>
</section>

<section class="section section-dark">
  <div class="container">
    {plank('Call First. Seriously.')}
    <div class="call-panel">
      <p style="max-width:640px;margin:0 auto">Steve runs the mill and the crew from his truck, not a desk. A two-minute call gets you an answer that three emails won&rsquo;t.</p>
      <a class="big-phone" href="{PHONE_TEL}">{SVG_PHONE.replace('<svg ', '<svg style="width:30px;height:30px;margin-right:14px" ')}{PHONE_DISPLAY}</a>
      <p class="call-note">Monday &ndash; Saturday, 8AM &ndash; 6PM &middot; Nassau, NY</p>
    </div>
    <div class="contact-grid">
      <div>
        <h3 style="font-family:'Roboto Condensed',sans-serif;text-transform:uppercase;letter-spacing:2px;color:#fff">Rather write it down?</h3>
        <form id="estimate-form" class="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST">
          <input type="hidden" name="_subject" value="New estimate request from capitalsawmill.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder="Full Name*" required>
          <input type="email" name="email" placeholder="Email*" required>
          <input type="tel" name="phone" placeholder="Phone (so we can call you back)">
          <textarea name="message" placeholder="Tell us about your tree or your project&hellip;"></textarea>
          <button class="btn btn-maroon" type="submit">Send Message</button>
        </form>
      </div>
      <div>
        <h3 style="font-family:'Roboto Condensed',sans-serif;text-transform:uppercase;letter-spacing:2px;color:#fff">Visit the mill</h3>
        <ul class="contact-info-list">
          <li>{SVG_MARKER} 4119 US Highway 20, Nassau, NY 12123</li>
          <li>{SVG_CLOCK} Monday &ndash; Saturday, 8AM &ndash; 6PM</li>
          <li>{SVG_ENVELOPE} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p style="margin-top:18px">Slabs are best picked in person &mdash; come walk the racks and find yours.</p>
      </div>
    </div>
  </div>
</section>
'''

THANKS_BODY = f'''
<section class="section" style="min-height:50vh;display:flex;align-items:center">
  <div class="container" style="text-align:center">
    {plank('Message Sent!')}
    <p style="max-width:600px;margin:0 auto 26px">Thanks &mdash; your message is on its way to Steve. Want an answer faster? You know what to do:</p>
    <a class="btn btn-call" href="{PHONE_TEL}">{SVG_PHONE} Call {PHONE_DISPLAY}</a>
  </div>
</section>
'''

PAGES = [
    # (path, title, description, body, root, leaflet)
    ('index.html',
     'Albany NY Custom Lumber, Wood Slabs, and Tree Removal | Capital Sawmill',
     'Capital Sawmill Service: expert tree removal and custom sawmilling in the Capital Region. We turn problem trees into beautiful lumber. Call (518) 479-0729.',
     INDEX_BODY, '', True),
    ('tree-removal/index.html',
     'Tree Removal & Tree Services | Capital Sawmill, Albany NY',
     'Licensed, insured tree removal, pruning, stump grinding and land clearing in the Albany Capital Region. 30+ years of experience. Call (518) 479-0729.',
     TREE_BODY, '../', False),
    ('wood-slabs/index.html',
     'Custom Wood Slabs — Walnut, Cherry, Maple, Oak & More | Capital Sawmill',
     'One-of-a-kind live-edge wood slabs up to 30" wide, air dried and milled in Nassau NY. Walnut, cherry, maple, oak, pine and specialty species. Ships nationwide.',
     SLABS_BODY, '../', False),
    ('wood-products/index.html',
     'Wood Products — Bar Tops, Table Tops, Mantels | Capital Sawmill',
     'Custom bar tops, table tops, fireplace mantels, deer plaque mounts and chainsaw signs, handmade from our own lumber in Nassau NY. Ships nationwide.',
     PRODUCTS_BODY, '../', False),
    ('firewood/index.html',
     'Firewood For Sale — Seasoned Hardwood | Capital Sawmill, Nassau NY',
     'Seasoned mixed hardwood firewood by the face cord, kindling kegs, and smoker chunks. Local delivery in the Capital Region. Call (518) 479-0729 to order.',
     FIREWOOD_BODY, '../', False),
    ('about/index.html',
     'About Us — Three Generations of Tree Work | Capital Sawmill',
     'Owner and arborist Steven Daniels has provided tree service for over 30 years, adding a sawmill in 1995 to give removed trees a second life as custom lumber.',
     ABOUT_BODY, '../', False),
    ('contact/index.html',
     'Contact Capital Sawmill — Call (518) 479-0729',
     'Free estimates for tree removal and custom milling. Call (518) 479-0729, Monday-Saturday 8AM-6PM, or visit the mill at 4119 US Highway 20, Nassau NY.',
     CONTACT_BODY, '../', False),
    ('thanks/index.html',
     'Thanks! | Capital Sawmill',
     'Your message is on its way to Capital Sawmill.',
     THANKS_BODY, '../', False),
]

for path, title, desc, body, root, leaflet in PAGES:
    out = SITE / path
    out.parent.mkdir(parents=True, exist_ok=True)
    html = head(title, desc, root, leaflet) + header(root) + '<main>' + body + '</main>' + footer(root)
    out.write_text(html)
    print(f'built {path} ({len(html)} bytes)')

print('done')
