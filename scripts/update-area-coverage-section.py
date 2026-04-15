import glob, re, os

NEW_SECTION = """        <div class="py-20 bg-[#0f172a]">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12">
                    <span class="inline-block px-4 py-1 bg-white/10 text-cyan-400 text-xs font-bold rounded-full mb-4 uppercase tracking-widest">UK-Wide Coverage</span>
                    <h2 class="text-3xl lg:text-4xl font-black text-white mb-3">Explore All Coverage Areas</h2>
                    <p class="text-white/50 max-w-lg mx-auto text-sm">Dedicated on-site hotel IT support across London's key districts and major UK regions.</p>
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
                    <a href="/areas/london" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#2563eb]/10 hover:border-[#2563eb]/40 transition-all">
                        <i class="fa-solid fa-city text-[#2563eb] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">London</div><div class="text-xs text-white/40 mt-0.5">Greater London</div></div>
                    </a>
                    <a href="/areas/central-london" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#2563eb]/10 hover:border-[#2563eb]/40 transition-all">
                        <i class="fa-solid fa-building-columns text-[#1d4ed8] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Central London</div><div class="text-xs text-white/40 mt-0.5">West End &amp; City</div></div>
                    </a>
                    <a href="/areas/mayfair" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#8b5cf6]/10 hover:border-[#8b5cf6]/40 transition-all">
                        <i class="fa-solid fa-gem text-[#8b5cf6] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Mayfair</div><div class="text-xs text-white/40 mt-0.5">Luxury Hotels</div></div>
                    </a>
                    <a href="/areas/kensington" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#0ea5e9]/10 hover:border-[#0ea5e9]/40 transition-all">
                        <i class="fa-solid fa-landmark text-[#0ea5e9] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Kensington</div><div class="text-xs text-white/40 mt-0.5">Museums &amp; Hotels</div></div>
                    </a>
                    <a href="/areas/chelsea" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#ec4899]/10 hover:border-[#ec4899]/40 transition-all">
                        <i class="fa-solid fa-hotel text-[#ec4899] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Chelsea</div><div class="text-xs text-white/40 mt-0.5">Boutique Hotels</div></div>
                    </a>
                    <a href="/areas/canary-wharf" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#06b6d4]/10 hover:border-[#06b6d4]/40 transition-all">
                        <i class="fa-solid fa-building text-[#06b6d4] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Canary Wharf</div><div class="text-xs text-white/40 mt-0.5">Financial District</div></div>
                    </a>
                    <a href="/areas/westminster" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#3b82f6]/10 hover:border-[#3b82f6]/40 transition-all">
                        <i class="fa-solid fa-landmark-dome text-[#3b82f6] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Westminster</div><div class="text-xs text-white/40 mt-0.5">Government District</div></div>
                    </a>
                    <a href="/areas/soho" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#f59e0b]/10 hover:border-[#f59e0b]/40 transition-all">
                        <i class="fa-solid fa-music text-[#f59e0b] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Soho</div><div class="text-xs text-white/40 mt-0.5">Entertainment Hub</div></div>
                    </a>
                    <a href="/areas/covent-garden" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#ef4444]/10 hover:border-[#ef4444]/40 transition-all">
                        <i class="fa-solid fa-store text-[#ef4444] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Covent Garden</div><div class="text-xs text-white/40 mt-0.5">Theatre District</div></div>
                    </a>
                    <a href="/areas/shoreditch" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#14b8a6]/10 hover:border-[#14b8a6]/40 transition-all">
                        <i class="fa-solid fa-microchip text-[#14b8a6] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Shoreditch</div><div class="text-xs text-white/40 mt-0.5">Tech &amp; Lifestyle</div></div>
                    </a>
                    <a href="/areas/south-bank" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#22c55e]/10 hover:border-[#22c55e]/40 transition-all">
                        <i class="fa-solid fa-water text-[#22c55e] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">South Bank</div><div class="text-xs text-white/40 mt-0.5">Riverside Hotels</div></div>
                    </a>
                    <a href="/areas/bloomsbury" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#a855f7]/10 hover:border-[#a855f7]/40 transition-all">
                        <i class="fa-solid fa-book text-[#a855f7] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Bloomsbury</div><div class="text-xs text-white/40 mt-0.5">Academic Quarter</div></div>
                    </a>
                    <a href="/areas/paddington" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#0ea5e9]/10 hover:border-[#0ea5e9]/40 transition-all">
                        <i class="fa-solid fa-train-subway text-[#0ea5e9] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Paddington</div><div class="text-xs text-white/40 mt-0.5">Transport Hub</div></div>
                    </a>
                    <a href="/areas/south-east" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#10b981]/10 hover:border-[#10b981]/40 transition-all">
                        <i class="fa-solid fa-map text-[#10b981] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">South East</div><div class="text-xs text-white/40 mt-0.5">Kent, Sussex, Surrey</div></div>
                    </a>
                    <a href="/areas/midlands" class="flex items-center gap-3 p-4 bg-white/5 border border-white/10 rounded-2xl hover:bg-[#8b5cf6]/10 hover:border-[#8b5cf6]/40 transition-all">
                        <i class="fa-solid fa-industry text-[#8b5cf6] text-lg flex-shrink-0" aria-hidden="true"></i>
                        <div><div class="font-semibold text-white text-sm leading-tight">Midlands</div><div class="text-xs text-white/40 mt-0.5">Birmingham &amp; Beyond</div></div>
                    </a>
                </div>
                <div class="text-center mt-10">
                    <a href="/areas" class="inline-flex items-center gap-2 px-7 py-3 bg-[#2563eb] text-white font-semibold rounded-full hover:bg-[#1d4ed8] transition-colors text-sm">
                        View All Coverage Areas <i class="fa-solid fa-arrow-right text-xs" aria-hidden="true"></i>
                    </a>
                </div>
            </div>
        </div>
    </main>"""

files = glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/areas/*.html')
count = 0
for f in files:
    content = open(f, encoding='utf-8').read()
    new_content = re.sub(
        r'        <div class="py-12 border-t border-gray-100">.*?</div>\s*</div>\s*</div>\s*</main>',
        NEW_SECTION,
        content,
        flags=re.DOTALL
    )
    if new_content != content:
        open(f, 'w', encoding='utf-8').write(new_content)
        count += 1
        print(f"  Updated: {os.path.basename(f)}")

print(f"\nTotal: {count} files updated")
