#!/usr/bin/env python3
import os
import re

# Directory containing the HTML files
base_dir = r"c:\Users\Administrator\Desktop\GGGTECH-HTML\gggtech.co.uk-1"

# Pattern to match the social media links without aria-labels
pattern = r'(<a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-\[#2563eb\] transition-colors"><i class="fa-brands fa-linkedin-in"></i></a><a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-\[#2563eb\] transition-colors"><i class="fa-brands fa-twitter"></i></a><a href="#" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-\[#2563eb\] transition-colors"><i class="fa-brands fa-facebook-f"></i></a>)'

# Replacement with aria-labels
replacement = r'<a href="#" aria-label="Follow us on LinkedIn" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-[#2563eb] transition-colors"><i class="fa-brands fa-linkedin-in"></i></a><a href="#" aria-label="Follow us on Twitter" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-[#2563eb] transition-colors"><i class="fa-brands fa-twitter"></i></a><a href="#" aria-label="Follow us on Facebook" class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-[#2563eb] transition-colors"><i class="fa-brands fa-facebook-f"></i></a>'

# Files to process (excluding about.html which we already did)
files_to_process = [
    "404.html",
    "areas.html",
    "contact.html",
    "book-a-visit.html",
    "faq.html",
    "solutions.html",
    os.path.join("areas", "bloomsbury.html"),
    os.path.join("areas", "east-anglia.html"),
    os.path.join("areas", "mayfair.html"),
    os.path.join("areas", "kensington.html"),
    os.path.join("areas", "london.html"),
    os.path.join("areas", "covent-garden.html"),
]

for filename in files_to_process:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace the pattern
        new_content = re.sub(re.escape(pattern), replacement, content)

        # Only write if there was a change
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes needed for {filename}")
    else:
        print(f"File not found: {filename}")

print("Social media aria-label update complete!")