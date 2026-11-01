"""Generate sitemap.xml from the site's real HTML pages.

Skips 404.html and legacy redirect stubs (folders with index.html that only
meta-refresh to a new URL). lastmod = last git commit date of the file, or
today if the file has uncommitted changes.

Usage (from repo root):  python scripts/generate_sitemap.py
"""
import datetime
import glob
import os
import subprocess

DOMAIN = 'https://gggtech.co.uk'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
today = datetime.date.today().isoformat()
dirty = set(
    l[3:].strip() for l in subprocess.run(
        ['git', 'status', '--porcelain', '-uall'], capture_output=True, text=True
    ).stdout.splitlines()
)


def lastmod(path):
    if path in dirty:
        return today
    d = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', path],
                       capture_output=True, text=True).stdout.strip()
    return d or today


def priority(slug):
    if slug == 'index':
        return '1.0'
    if slug in ('get-a-quote', 'book-a-visit', 'services', 'solutions', 'areas/london'):
        return '0.9'
    if '/' not in slug or slug.startswith(('services/', 'solutions/')):
        return '0.8'
    return '0.7'


files = sorted(glob.glob('*.html') + glob.glob('*/*.html'))
rows = []
for f in files:
    f = f.replace(os.sep, '/')
    if f == '404.html' or f.endswith('/index.html'):
        continue
    with open(f, encoding='utf-8-sig') as fh:
        head = fh.read(4000)
    if 'http-equiv="refresh"' in head or 'noindex' in head:
        continue
    slug = f[:-5]
    loc = DOMAIN + '/' if slug == 'index' else f'{DOMAIN}/{slug}'
    rows.append(f'  <url><loc>{loc}</loc><lastmod>{lastmod(f)}</lastmod><priority>{priority(slug)}</priority></url>')

with open('sitemap.xml', 'w', encoding='utf-8', newline='\n') as out:
    out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    out.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    out.write('\n'.join(rows) + '\n</urlset>\n')
print(f'{len(rows)} URLs written to sitemap.xml')
