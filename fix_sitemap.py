import re

# Read the sitemap file
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of www.gggtech.co.uk with gggtech.co.uk
updated_content = re.sub(r'www\.gggtech\.co\.uk', 'gggtech.co.uk', content)

# Write back to the file
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Sitemap URLs updated successfully!")