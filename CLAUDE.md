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
