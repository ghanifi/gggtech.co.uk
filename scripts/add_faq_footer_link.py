from pathlib import Path
import re

root = Path('.')
pattern = re.compile(
    r'(<li><a href="/about" class="text-white/70 hover:text-white transition-colors">About Us</a></li><li><a href="/industries" class="text-white/70 hover:text-white transition-colors">Industries</a></li>)(<li><a href="/insights" class="text-white/70 hover:text-white transition-colors">Insights</a></li>)'
)
replacement = r'\1<li><a href="/faq" class="text-white/70 hover:text-white transition-colors">FAQ</a></li>\2'
updated = []

for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8')
    if '/faq" class="text-white/70 hover:text-white transition-colors">FAQ' in text:
        continue
    new_text, count = pattern.subn(replacement, text)
    if count:
        path.write_text(new_text, encoding='utf-8')
        updated.append(path.relative_to(root).as_posix())

print('Updated', len(updated), 'files')
for p in updated:
    print(p)
