#!/usr/bin/env bash
# Auto-generate sitemap.xml from all HTML files in the site

SITE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOMAIN="https://gggtech.co.uk"
TODAY=$(date +%Y-%m-%d)
OUTPUT="$SITE_ROOT/sitemap.xml"

get_url_entry() {
  local file="$1"
  local rel="${file#$SITE_ROOT/}"
  local slug="${rel%.html}"
  local loc priority changefreq

  if [ "$slug" = "index" ]; then
    loc="${DOMAIN}/"
  else
    loc="${DOMAIN}/${slug}"
  fi

  case "$slug" in
    "index")
      priority="1.0"; changefreq="weekly" ;;
    "book-a-visit"|"get-a-quote")
      priority="0.9"; changefreq="monthly" ;;
    "about"|"services"|"areas"|"industries"|"insights"|"solutions"|"contact"|"faq")
      priority="0.8"; changefreq="monthly" ;;
    services/*|solutions/*)
      priority="0.8"; changefreq="monthly" ;;
    areas/*|industries/*|insights/*)
      priority="0.7"; changefreq="monthly" ;;
    *)
      priority="0.7"; changefreq="monthly" ;;
  esac

  echo "  <url><loc>${loc}</loc><changefreq>${changefreq}</changefreq><priority>${priority}</priority><lastmod>${TODAY}</lastmod></url>"
}

{
  echo "<?xml version='1.0' encoding='utf-8'?>"
  echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
  echo ""

  # Top-level pages (index first, then alphabetical)
  for f in "$SITE_ROOT/index.html" "$SITE_ROOT/about.html" "$SITE_ROOT/services.html" \
            "$SITE_ROOT/areas.html" "$SITE_ROOT/industries.html" "$SITE_ROOT/insights.html" \
            "$SITE_ROOT/solutions.html" "$SITE_ROOT/contact.html" "$SITE_ROOT/book-a-visit.html" \
            "$SITE_ROOT/get-a-quote.html" "$SITE_ROOT/faq.html"; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""

  # Services
  for f in "$SITE_ROOT/services"/*.html; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""

  # Areas
  for f in "$SITE_ROOT/areas"/*.html; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""

  # Industries
  for f in "$SITE_ROOT/industries"/*.html; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""

  # Solutions
  for f in "$SITE_ROOT/solutions"/*.html; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""

  # Insights / Blog
  for f in "$SITE_ROOT/insights"/*.html; do
    [ -f "$f" ] && get_url_entry "$f"
  done

  echo ""
  echo "</urlset>"
} > "$OUTPUT"

echo "Sitemap regenerated: $OUTPUT ($(grep -c '<url>' "$OUTPUT") URLs)"
