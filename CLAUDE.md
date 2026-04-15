# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **GGG Technologies** static website — a UK-based hotel IT support company. It is a flat HTML/CSS site with no build step; all pages are plain `.html` files served directly.

The parent directory (`../`) is an `ai-website-builder` scaffold with Vite + Tailwind. That build system is **not used here**. The `GGGTECH-HTML/` folder is self-contained with pre-bundled assets.

## Development

**Preview locally:** Open any `.html` file directly in a browser, or serve with any static file server:
```bash
npx serve .          # or: python -m http.server 8080
```

If using the parent project's dev server:
```bash
cd .. && npm run dev   # Vite on http://localhost:5173
```

**No build step required** — edits to `.html` files are immediately reflected on reload.

## Asset Structure

```
assets/
  css/
    tailwind.css      # Pre-bundled Tailwind (CDN-style, no compilation needed)
    main.css          # CSS variables + global styles; imports tailwind + fonts
    fonts.css         # Self-hosted font-face declarations
    google-fonts.css  # Fallback Google Fonts import
  fontawesome/
    fontawesome.js    # Bundled FontAwesome (all icons available)
  images/             # Site images (numeric filenames from stock library)
public/               # Mirror of assets/ — used by Vite when running via parent dev server
```

Each HTML page links assets via absolute paths (`/assets/css/...`). Always use absolute paths — not relative — to keep links consistent across nested pages (`/services/`, `/areas/`, etc.).

## Design System

CSS variables are defined in `assets/css/main.css` and re-declared inline in each page's `<style>` block:

| Variable | Value | Role |
|---|---|---|
| `--primary-color` | `#1a3a5c` | Dark navy — headings, brand |
| `--accent-color` | `#2563eb` | Blue — primary CTAs |
| `--accent2-color` | `#10b981` | Green — networks/secondary |
| `--accent3-color` | `#f59e0b` | Amber — security/warnings |
| `--accent4-color` | `#8b5cf6` | Purple — hotel systems |
| `--dark-background-color` | `#0d1b2a` | Footer/dark sections |

Fonts: **Inter** (body) and **Outfit** (headings), self-hosted via `fonts.css`.

Styling is done entirely with **Tailwind utility classes inline in HTML**. Do not add custom CSS unless a utility class cannot achieve the result.

## Page Architecture

All pages share an identical nav and footer copied inline. There is no templating engine — consistency across pages must be maintained manually.

**Nav:** Fixed dark navbar (`bg-[#0f172a]/95`) with hover mega-menus for Services (4 columns), Areas (grid), and dropdown for Industries/Solutions. Mobile: hamburger toggle.

**Footer:** Dark background (`var(--dark-background-color)`) with 4-column grid: company info, services links, areas links, contact details.

When adding or updating nav/footer items, you must update **every** `.html` file that contains that nav/footer.

## Site Map

| Section | Files |
|---|---|
| Top-level | `index.html`, `about.html`, `services.html`, `areas.html`, `industries.html`, `insights.html`, `solutions.html`, `contact.html`, `book-a-visit.html`, `get-a-quote.html`, `404.html` |
| Services (detail) | `services/*.html` — 16 service pages |
| Areas (detail) | `areas/*.html` — 15 area pages |
| Industries (detail) | `industries/*.html` — 6 industry pages |
| Solutions (detail) | `solutions/*.html` — 2 solution pages |
| Blog articles | `insights/*.html` — see template below |

## Blog Article Template

All blog articles live in `insights/` and **must follow the design of `insights/hotel-wifi-problems-guide.html`** exactly. Reference that file as the canonical template.

### URL convention
`/insights/[kebab-case-slug].html`

### Required `<head>` tags
```html
<title>[Article Title] | GGG Technologies</title>  <!-- ≤60 chars -->
<meta name="description" content="...">            <!-- 150-160 chars -->
<meta property="og:type" content="article">        <!-- not "website" -->
<link rel="canonical" href="https://gggtech.co.uk/insights/[slug]">
<!-- Article JSON-LD schema (not LocalBusiness) -->
<script type="application/ld+json">
{ "@type": "Article", "headline": "...", "datePublished": "YYYY-MM-DD", ... }
</script>
<!-- BreadcrumbList JSON-LD -->
```

### Page structure (in order)

1. **`<main class="pt-20">`**

2. **Full-bleed hero** — background image + dark gradient overlay + content on top:
   - `min-h-[580px] lg:min-h-[640px]` with `position: relative`
   - Gradient: `bg-gradient-to-t from-[#0a1628] via-[#0a1628]/75 to-[#0f172a]/40`
   - Content: breadcrumb → category badge (coloured, solid fill) + read time + date → H1 → standfirst → author + share buttons row with `border-t border-white/15`

3. **Article body** — `max-w-7xl` container, `py-16`:
   - Grid: `lg:grid lg:grid-cols-[1fr_320px] lg:gap-16`
   - **First column** is a wrapper `<div>` containing:
     - `<div class="prose max-w-none">` — all article text content
     - CTA box **outside** `.prose` (prose CSS overrides Tailwind text colours via `.prose h3` / `.prose p` selectors)
   - **Second column** — `<aside class="toc-sidebar">` with `sticky top-28`

4. **CTA box** (outside `.prose`, inside first column wrapper):
   - Two-tone card: dark navy header strip (`bg-[#1a3a5c]`) + light body (`bg-gray-50`)
   - Header: green icon + title `<p style="font-family:var(--font-family-heading)">` + subtitle
   - Body: description text + two buttons (primary blue, secondary white/bordered)
   - Use `style="font-family:..."` on text elements inside CTA — Tailwind font classes are overridden by `.prose` CSS even outside `.prose` if the element is a descendant

5. **Prose CSS** — define in `<style>` block (not inline):
   - `.prose h2/h3` — Outfit font, `#1a3a5c` colour
   - `.prose p/ul/ol` — Inter font, `#374151` colour, `line-height: 1.8`
   - `.prose ul li::before` — blue dot bullet

6. **Back to Insights link** at bottom: `← Back to All Insights` → `/insights`

### Category colours
| Category | Badge colour |
|---|---|
| WiFi & Networking | `#10b981` (green) |
| Cybersecurity | `#f59e0b` (amber) |
| PMS & Systems | `#8b5cf6` (purple) |
| IT Support | `#2563eb` (blue) |

### TOC sidebar
- `display: none` on mobile (CSS class `.toc-sidebar { @media <1024px { display:none } }`)
- Scroll-spy via `IntersectionObserver` — adds `.active` class to matching `.toc-link`
- Sidebar CTA card below TOC linking to `/book-a-visit`

### After publishing a new article
Update `insights.html` to add the new article card (with correct `data-category` attribute for JS filtering) and update the featured article slot if appropriate.

## Key Rules (from AGENTS.md)

- **Do not edit:** `AGENTS.md`, `CLAUDE.md`, `../setup-guide.html`, `../AGENTS.md`, `../setup.sh`
- **Placeholders:** Before any publish, run a scan for bracket placeholders (`[...]`), `yourwebsite.com`, `placehold.co`, or `lorem ipsum`
- **Images:** Prefer real files from `assets/images/` over placeholders
- **No auto-publish:** Always get explicit user confirmation before any deploy command
- **Publishing commands** (run from parent `../`): `npm run publish:github`, `publish:netlify`, `publish:cloudflare`, `publish:vercel`

## Pre-Publish Audit

```bash
grep -RInE '\[[^]]+\]|yourwebsite\.com|placehold\.co|lorem ipsum' --include='*.html' .
```
