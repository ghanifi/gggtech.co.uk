import os
import re

def update_html_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Skip index.html as it's already optimized
                    if 'index.html' in filepath:
                        continue

                    # Update main.css to preload pattern
                    content = re.sub(
                        r'<link href="/assets/css/main\.css" rel="stylesheet">',
                        r'<link rel="preload" href="/assets/css/main.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">',
                        content
                    )

                    # Add defer to fontawesome script
                    content = re.sub(
                        r'<script src="/assets/fontawesome/fontawesome\.js" crossorigin="anonymous"></script>',
                        r'<script src="/assets/fontawesome/fontawesome.js" crossorigin="anonymous" defer></script>',
                        content
                    )

                    # Add defer to tailwind script
                    content = re.sub(
                        r'<script src="/assets/css/tailwind\.css"></script>',
                        r'<script src="/assets/css/tailwind.css" defer></script>',
                        content
                    )

                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {filepath}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    update_html_files(".")