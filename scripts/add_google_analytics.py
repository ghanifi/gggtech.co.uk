#!/usr/bin/env python3
"""Inserts the Google Analytics (gtag.js) snippet into every HTML page's <head>.

Idempotent: skips any file that already contains the measurement ID.
"""
import glob
import os

MEASUREMENT_ID = "G-XHSTKJKDQ9"

SNIPPET = f"""<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{MEASUREMENT_ID}');
    </script>
"""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def process(path):
    with open(path, "rb") as f:
        raw = f.read()

    bom = b""
    if raw.startswith(b"\xef\xbb\xbf"):
        bom = raw[:3]
        raw = raw[3:]

    text = raw.decode("utf-8")

    if MEASUREMENT_ID in text:
        return "skipped (already present)"

    if "<head>" not in text:
        return "SKIPPED - no <head> tag found"

    text = text.replace("<head>", SNIPPET, 1)

    with open(path, "wb") as f:
        f.write(bom + text.encode("utf-8"))

    return "updated"


def main():
    html_files = sorted(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True))
    html_files = [p for p in html_files if os.sep + ".git" + os.sep not in p]

    for path in html_files:
        rel = os.path.relpath(path, ROOT)
        result = process(path)
        print(f"{result}: {rel}")


if __name__ == "__main__":
    main()
