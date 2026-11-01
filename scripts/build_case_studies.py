"""Build /case-studies.html (Hotels We Support) from about.html's shell.

Client list = properties GGG Technologies supports (confirmed by the owner,
Nov 2026). Only name, area and service focus are shown: no invented
outcomes or metrics. Add real project details to CLIENTS to enrich cards.

Usage (repo root): python scripts/build_case_studies.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# slug, name, area, property type, focus, service link, legacy URL
CLIENTS = [
    ('hilton-london-croydon', 'Hilton London Croydon', 'Croydon', 'Branded hotel', '24/7 IT support and operational efficiency', '/solutions/24-7-it-support', 'boosting-operational-efficiency-at-hilton-london-croydon-with-24-7-it-support'),
    ('premier-inn-london-croydon-south', 'Premier Inn London Croydon South (A212)', 'Croydon', 'Branded hotel', 'Full-time cyber security', '/solutions/cyber-security', 'the-value-of-full-time-cyber-security-at-premier-inn-london-croydon-south-a212'),
    ('holiday-inn-london-bexley', 'Holiday Inn London Bexley', 'Bexley', 'Branded hotel', '24/7 IT monitoring', '/solutions/24-7-it-support', 'how-24-7-it-monitoring-improves-guest-experience-at-holiday-inn-london-bexley'),
    ('travelodge-dagenham', 'Travelodge Dagenham', 'Dagenham', 'Branded hotel', 'Proactive monitoring', '/solutions/24-7-it-support', 'eliminating-it-risks-for-travelodge-dagenham-with-proactive-monitoring'),
    ('travelodge-london-belvedere', 'Travelodge London Belvedere', 'Belvedere', 'Branded hotel', 'Round-the-clock IT monitoring', '/solutions/24-7-it-support', 'ensuring-zero-downtime-for-travelodge-london-belvedere-with-round-the-clock-it-monitoring'),
    ('best-western-plus-london-croydon', 'Best Western Plus London Croydon', 'Croydon', 'Branded hotel', 'Guest communication systems', '/services/voice-solutions', 'enhancing-guest-communication-systems-for-best-western-plus-london-croydon'),
    ('hallmark-hotel-croydon', 'Hallmark Hotel Croydon', 'Croydon', 'Hotel', 'Eliminating system interruptions', '/services/it-support-maintenance', 'eliminating-system-interruptions-at-hallmark-hotel-croydon'),
    ('london-croydon-aerodrome-hotel', 'London Croydon Aerodrome Hotel', 'Croydon', 'Hotel', 'Digital operations', '/services/it-support-maintenance', 'enhancing-digital-operations-for-london-croydon-aerodrome-hotel'),
    ('grand-sapphire-banqueting-hotel', 'Grand Sapphire Hotel & Banqueting', 'Croydon', 'Conference & events hotel', 'Events and booking systems', '/industries/conference-hotels', 'keeping-events-bookings-smooth-at-grand-sapphire-banqueting-hotel'),
    ('the-clarendon-hotel', 'The Clarendon Hotel', 'London', 'Independent hotel', 'Check-in and IT automation', '/services/pms-integration', 'ensuring-smooth-check-in-for-the-clarendon-hotel-with-it-automation'),
    ('the-beverley-hotel', 'The Beverley Hotel', 'London', 'Independent hotel', 'Wireless network security', '/services/network-wifi-solutions', 'protecting-wireless-networks-at-the-beverley-hotel-london'),
    ('dukes-head-hotel', 'Dukes Head Hotel', 'South East', 'Independent hotel', 'Managed guest WiFi', '/services/guest-wifi', 'ensuring-stable-guest-wi-fi-at-dukes-head-hotel-through-managed-it'),
    ('the-greyhound-hotel', 'The Greyhound Hotel', 'South East', 'Independent hotel', '24/7 cyber monitoring', '/services/cyber-security', 'protecting-customer-data-for-the-greyhound-hotel-with-24-7-cyber-monitoring'),
    ('berwick-manor-hotel', 'Berwick Manor Hotel', 'South East', 'Independent hotel', 'Booking stability and 24/7 IT support', '/solutions/24-7-it-support', 'strengthening-booking-stability-at-berwick-manor-hotel-through-24-7-it-support'),
    ('staycity-aparthotels-london-croydon', 'Staycity Aparthotels London Croydon', 'Croydon', 'Aparthotel', 'Network reliability', '/services/network-wifi-solutions', 'strengthening-network-reliability-at-staycity-aparthotels-london-croydon'),
    ('flexistay-addiscombe-aparthotel', 'Flexistay Addiscombe Aparthotel', 'Croydon', 'Aparthotel', 'PMS stability', '/services/pms-hotel-systems', 'keeping-pms-systems-stable-at-flexistay-addiscombe-aparthotel'),
    ('westciti-croydon-serviced-apartments', 'Westciti Croydon Serviced Apartments', 'Croydon', 'Serviced apartments', 'Preventing network failures', '/services/network-wifi-solutions', 'preventing-network-failures-at-westciti-croydon-serviced-apartments'),
    ('clarendon-road-apartments', 'Clarendon Road Apartments', 'London', 'Serviced apartments', '24/7 IT monitoring', '/industries/serviced-apartments', 'how-24-7-it-monitoring-benefits-clarendon-road-apartments'),
    ('hazel-residence', 'Hazel Residence', 'London', 'Serviced residence', 'Digital security standards', '/services/cyber-security', 'improving-digital-security-standards-for-hazel-residence'),
    ('croham-park-bb', 'Croham Park B&B', 'Croydon', 'B&B', 'Smart room technology', '/services/smart-room', 'protecting-smart-room-tech-at-croham-park-bb-croydon'),
]

TITLE = 'Hotels We Support: Client Case Studies | GGG Technologies'
DESC = ('Hilton, Premier Inn, Holiday Inn, Travelodge and independent hotels across London and the South East trust '
        'GGG Technologies for 24/7 hotel IT support.')
URL = 'https://gggtech.co.uk/case-studies'

src = open('about.html', encoding='utf-8-sig').read()
head_end = src.index('</head>')
head = src[:head_end]
head = re.sub(r'<title>.*?</title>', f'<title>{TITLE.replace("&", "&amp;")}</title>', head)
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', head)
head = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="hotel it support case studies, hotel it clients, hotel it support croydon, hotel it support london">', head)
for p in ('og:title', 'twitter:title'):
    attr = 'property' if p.startswith('og') else 'name'
    head = re.sub(rf'<meta {attr}="{p}" content="[^"]*">', f'<meta {attr}="{p}" content="{TITLE.replace("&", "&amp;")}">', head)
for p in ('og:description', 'twitter:description'):
    attr = 'property' if p.startswith('og') else 'name'
    head = re.sub(rf'<meta {attr}="{p}" content="[^"]*">', f'<meta {attr}="{p}" content="{DESC}">', head)
head = head.replace('content="https://gggtech.co.uk/about"', f'content="{URL}"')
head = head.replace('<link rel="canonical" href="https://gggtech.co.uk/about">', f'<link rel="canonical" href="{URL}">')
head = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', '', head, flags=re.S)

schema = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type': 'CollectionPage', '@id': URL + '#webpage', 'url': URL, 'name': TITLE, 'description': DESC,
         'inLanguage': 'en-GB', 'isPartOf': {'@id': 'https://gggtech.co.uk/#website'},
         'about': {'@id': 'https://gggtech.co.uk/#organization'},
         'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(CLIENTS), 'itemListElement': [
             {'@type': 'ListItem', 'position': i + 1, 'name': c[1], 'url': f'{URL}#{c[0]}'} for i, c in enumerate(CLIENTS)]}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://gggtech.co.uk/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Case Studies', 'item': URL}]},
    ],
}
head += '    <script type="application/ld+json">\n' + json.dumps(schema, indent=2, ensure_ascii=False) + '\n    </script>\n'

body_start = src.index('<main id="main">')
pre_main = src[head_end:body_start]
post_main = src[src.index('</main>') + len('</main>'):]


def esc(s):
    return s.replace('&', '&amp;')


types = {}
for c in CLIENTS:
    types.setdefault(c[3], []).append(c)

cards = []
for c in CLIENTS:
    slug, name, area, ptype, focus, link, _ = c
    cards.append(f'''                <article id="{slug}" class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col">
                    <div class="flex items-center gap-2 text-sm text-gray-500 mb-3"><i class="fa-solid fa-location-dot text-[#2563eb]" aria-hidden="true"></i><span>{esc(area)}</span><span class="w-1 h-1 rounded-full bg-gray-200"></span><span>{esc(ptype)}</span></div>
                    <h3 class="text-xl font-bold text-[#1a3a5c] mb-3">{esc(name)}</h3>
                    <p class="text-gray-600 mb-6 grow"><span class="font-semibold text-[#1a3a5c]">Focus:</span> {esc(focus)}</p>
                    <a href="{link}" class="inline-flex items-center gap-2 text-[#2563eb] font-semibold hover:underline">See the service <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                </article>''')

brands = ['Hilton', 'Premier Inn', 'Holiday Inn', 'Travelodge', 'Best Western Plus', 'Staycity', 'Hallmark']

main = f'''<main id="main">

    <!-- Hero Section -->
    <section class="relative pt-32 pb-20 bg-gradient-to-br from-[#0d1b2a] to-[#1a3a5c] overflow-hidden">
        <div class="absolute inset-0 opacity-5" style="background-image: radial-gradient(circle at 1px 1px, white 1px, transparent 0); background-size: 40px 40px;"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
            <nav class="flex justify-center text-white/60 text-sm mb-8 gap-2" aria-label="Breadcrumb"><a href="/" class="hover:text-white">Home</a><span>/</span><span class="text-white font-semibold">Case Studies</span></nav>
            <div class="text-center max-w-3xl mx-auto">
                <div class="inline-flex items-center gap-3 mb-4">
                    <div class="w-12 h-px bg-[#f59e0b]"></div>
                    <span class="text-[#f59e0b] text-sm font-semibold uppercase tracking-widest">Case Studies</span>
                    <div class="w-12 h-px bg-[#f59e0b]"></div>
                </div>
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-6 leading-tight">
                    Hotels We Support <br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#f59e0b] to-[#2563eb]">Across London &amp; the South East</span>
                </h1>
                <p class="text-lg text-white/70 leading-relaxed max-w-2xl mx-auto mb-8">
                    From international brands to family-run B&amp;Bs, these are some of the {len(CLIENTS)} properties that rely on GGG Technologies for 24/7 hotel IT support, guest WiFi, PMS stability and cyber security.
                </p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="/book-a-visit" class="inline-flex items-center justify-center gap-2 px-8 py-4 bg-[#f59e0b] text-[#1a3a5c] font-bold rounded-full hover:bg-[#d97706] transition-all">Book a Free Assessment <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                    <a href="tel:+442036424958" class="inline-flex items-center justify-center gap-2 px-8 py-4 border-2 border-white text-white font-semibold rounded-full hover:bg-white hover:text-[#1a3a5c] transition-all"><i class="fa-solid fa-phone" aria-hidden="true"></i> +44 20 3642 4958</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Brands strip -->
    <section class="bg-white py-12 border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p class="text-sm font-semibold uppercase tracking-widest text-gray-500 mb-6">Trusted by properties operating under</p>
            <div class="flex flex-wrap justify-center gap-8">
{chr(10).join(f'                <span class="text-2xl font-black text-gray-400">{esc(b)}</span>' for b in brands)}
            </div>
        </div>
    </section>

    <!-- Intro -->
    <section class="py-20 bg-[#f5f8fb]" aria-labelledby="clients-heading">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="max-w-3xl mb-12">
                <h2 id="clients-heading" class="text-3xl lg:text-4xl font-black text-[#1a3a5c] mb-6">Hotel IT support in practice</h2>
                <div class="space-y-4 text-gray-600 leading-relaxed">
                    <p>Every property below runs around the clock, and every one has the same problem when technology fails: guests notice first. Our work for these hotels covers the systems that keep a property trading, from the front desk PMS and card terminals to guest WiFi, phones, CCTV and the network that ties it all together.</p>
                    <p>Many of our clients are in Croydon and South London, close to our London base, which is why we can have an engineer on site within one hour across Greater London. Properties further out are covered by remote support straight away and a 4-hour on-site target.</p>
                    <p>Want to hear what it is like to work with us? Ask for a reference from a property similar to yours when you <a href="/book-a-visit" class="text-[#2563eb] font-semibold hover:underline">book your free assessment</a>.</p>
                </div>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
{chr(10).join(cards)}
            </div>
        </div>
    </section>

    <!-- By property type -->
    <section class="py-20 bg-white" aria-labelledby="types-heading">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 id="types-heading" class="text-3xl lg:text-4xl font-black text-[#1a3a5c] mb-10">Experience across every type of property</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="/industries/chain-hotels" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">Branded &amp; chain hotels</h3><p class="text-gray-600 text-sm">{len(types.get('Branded hotel', []))} branded properties, including Hilton, Premier Inn, Holiday Inn, Travelodge and Best Western Plus.</p></a>
                <a href="/industries/boutique-hotels" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">Independent hotels</h3><p class="text-gray-600 text-sm">Owner-run hotels that need an IT department without the overhead of hiring one.</p></a>
                <a href="/industries/serviced-apartments" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">Aparthotels &amp; serviced apartments</h3><p class="text-gray-600 text-sm">Self check-in, keyless entry and reliable WiFi for longer stays, including Staycity, Flexistay and Westciti.</p></a>
                <a href="/industries/conference-hotels" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">Conference &amp; events hotels</h3><p class="text-gray-600 text-sm">Booking systems, AV and high-density WiFi that hold up on the busiest event days.</p></a>
                <a href="/industries/bed-breakfast" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">B&amp;Bs &amp; guesthouses</h3><p class="text-gray-600 text-sm">Simple, affordable support for smaller properties, from WiFi to smart room tech.</p></a>
                <a href="/areas/london" class="group p-6 bg-gray-50 rounded-2xl border border-gray-100 hover:border-[#2563eb] hover:shadow-lg transition-all"><h3 class="text-lg font-bold text-[#1a3a5c] mb-2">London &amp; the South East</h3><p class="text-gray-600 text-sm">Engineers on site within 1 hour across Greater London, 24/7.</p></a>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 lg:py-28 bg-gradient-to-r from-[#1a3a5c] to-[#0d1b2a]">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-white mb-6">Join the hotels that never worry about IT</h2>
            <p class="text-lg text-white/70 mb-8">Book a free, no-obligation IT assessment. We'll review your setup, highlight the risks and give you a fixed monthly quote for supporting your property.</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/get-a-quote" class="inline-flex items-center justify-center gap-2 px-8 py-4 bg-[#f59e0b] text-[#1a3a5c] font-bold rounded-full hover:bg-[#d97706] transition-all">Get a Free Quote <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
                <a href="/book-a-visit" class="inline-flex items-center justify-center gap-2 px-8 py-4 border-2 border-white text-white font-semibold rounded-full hover:bg-white hover:text-[#1a3a5c] transition-all">Book a Visit <i class="fa-regular fa-calendar" aria-hidden="true"></i></a>
            </div>
            <p class="text-white/60 mt-8">Prefer to talk? Call <a href="tel:+442036424958" class="text-white font-semibold hover:underline">+44 20 3642 4958</a>, 24/7.</p>
        </div>
    </section>

    </main>'''

with open('case-studies.html', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write(head + pre_main + main + post_main)

# point the legacy client URLs at their card
redirects_path = 'scripts/legacy-redirects.json'
redirects = json.load(open(redirects_path))
for slug, *_rest, legacy in CLIENTS:
    target = f'/case-studies#{slug}'
    redirects['/' + legacy] = target
    os.makedirs(legacy, exist_ok=True)
    with open(os.path.join(legacy, 'index.html'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Moved | GGG Technologies</title>
<link rel="canonical" href="https://gggtech.co.uk/case-studies">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script>
</head>
<body><p>This page has moved to <a href="{target}">https://gggtech.co.uk{target}</a>.</p></body>
</html>
''')
json.dump(redirects, open(redirects_path, 'w'), indent=1, sort_keys=True)
print('case-studies.html written,', len(CLIENTS), 'clients; legacy stubs updated')
