import os
import re

def replace_colors(root_dir):
    patterns = [
        (r'--accent3-color: #f59e0b;', '--accent3-color: #92400e;'),  # CSS variable
        (r'bg-\[#f59e0b\]', 'bg-[#92400e]'),  # Background colors
        (r'hover:bg-\[#f59e0b\]', 'hover:bg-[#92400e]'),  # Hover backgrounds
        (r'hover:border-\[#f59e0b\]', 'hover:border-[#92400e]'),  # Hover borders
        (r'hover:shadow-\[#f59e0b\]', 'hover:shadow-[#92400e]'),  # Hover shadows
        (r'from-\[#f59e0b\]', 'from-[#92400e]'),  # Gradient starts
        (r'to-\[#d97706\]', 'to-[#92400e]'),  # Gradient ends (darker amber)
    ]

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.css'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content
                    for pattern, replacement in patterns:
                        content = re.sub(pattern, replacement, content)

                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Updated: {filepath}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    replace_colors(".")