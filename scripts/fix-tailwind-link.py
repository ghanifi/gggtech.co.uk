import glob, re

files = (
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/*.html') +
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/services/*.html') +
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/areas/*.html') +
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/industries/*.html') +
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/solutions/*.html') +
    glob.glob('C:/Users/Administrator/Desktop/GGGTECH-HTML/gggtech.co.uk-1/insights/*.html')
)

count = 0
for f in files:
    content = open(f, encoding='utf-8').read()
    # Replace both script tags (defer and non-defer) with a single link tag
    new_content = re.sub(
        r'\s*<script src="/assets/css/tailwind\.css" defer></script>\s*\n\s*<script src="/assets/css/tailwind\.css"></script>',
        '\n    <link rel="stylesheet" href="/assets/css/tailwind.css">',
        content
    )
    if new_content == content:
        # Try alternate orderings
        new_content = re.sub(
            r'<script src="/assets/css/tailwind\.css"[^>]*></script>',
            '',
            content
        )
        if new_content != content:
            # Add link tag after main.css noscript or before </head>
            new_content = new_content.replace(
                '</head>',
                '    <link rel="stylesheet" href="/assets/css/tailwind.css">\n</head>',
                1
            )
    if new_content != content:
        open(f, 'w', encoding='utf-8').write(new_content)
        count += 1
        print(f"  Updated: {f.split('/')[-1]}")

print(f"\nTotal: {count} files updated")
