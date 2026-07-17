# Red Agave Landscape -- Technical SEO Audit

**Audit Date:** July 2026
**Site:** redagaveatx.com
**Pages Audited:** 112 HTML files

---

## Executive Summary

The site has strong technical SEO foundations: every page has schema markup, canonical tags, Open Graph tags, and exactly one H1. The main issues are meta title/description lengths -- nearly all pages exceed Google's display limits, meaning titles and descriptions get truncated in search results. Fixing these is the single highest-impact technical change.

---

## P0 -- Critical

### 1. Meta Titles Over 60 Characters (88 pages)

Google truncates titles at ~60 characters. Nearly every page on the site exceeds this limit, meaning searchers see `...` instead of your full title.

**Worst offenders (90+ chars):**
- `blog/drainage-engineering-austin-tx.html` (118 chars)
- `blog/fire-pit-engineering-austin-tx.html` (117 chars)
- `blog/travertine-vs-flagstone-vs-pavers-austin-tx.html` (114 chars)
- `blog/landscape-consultation-checklist-austin-tx.html` (104 chars)
- `blog/caliche-soil-preparation-austin-tx.html` (97 chars)
- `blog/xeriscape-vs-traditional-lawn-austin-tx.html` (96 chars)

**Pattern:** Most titles follow `[Topic] | Red Agave Landscape` which adds 22 chars of branding. Blog posts are the worst because they add full location qualifiers too.

**Fix strategy:**
- Shorten brand suffix to `| Red Agave` (saves 10 chars)
- Drop "Red Agave Landscape" entirely from blog titles (the URL and schema handle brand attribution)
- Move location to the front: "Austin TX" at start, not end
- Target 50-55 chars to leave room for Google's own formatting

**Example fixes:**
| Current (too long) | Suggested (under 60) |
|---|---|
| How Much Does a Deck Cost in Austin, TX? (2026 Pricing) \| Red Agave Landscape (77) | Deck Cost Austin TX: 2026 Pricing Guide (40) |
| Best Deck Materials for Austin, TX Heat: IPE, Cedar & Composite \| Red Agave Landscape (85) | Best Deck Materials for Austin TX Heat (39) |
| Landscaping Dripping Springs TX \| Hill Country Xeriscape, Decks & Outdoor Living \| Red Agave (92) | Landscaping Dripping Springs TX \| Red Agave (45) |

### 2. Meta Descriptions Over 160 Characters (85 pages)

Google truncates descriptions at ~155-160 characters. Nearly all pages exceed this.

**Worst offenders (200+ chars):**
- `projects/riverview.html` (350 chars)
- `projects/axehandle.html` (311 chars)
- `projects/blazyk.html` (283 chars)
- `projects/flycatcher.html` (273 chars)
- `projects/dormarion.html` (260 chars)
- `blog/landscape-consultation-checklist-austin-tx.html` (236 chars)
- `about.html` (231 chars)
- `projects/hopeland.html` (226 chars)
- `reviews.html` (226 chars)
- `index.html` (222 chars)

**Fix strategy:**
- Cap all descriptions at 150-155 characters
- Front-load the value proposition and call-to-action
- Include primary keyword in first 120 characters (visible on mobile)
- Project pages: summarize the transformation, don't list every material

**Example fixes:**
| Page | Current length | Suggested description |
|---|---|---|
| index.html | 222 | "Austin's top-rated design+build landscaper. Xeriscape, decks, fire pits, lighting & outdoor kitchens. Free consultation. 512-695-7566." (135) |
| reviews.html | 226 | "125+ five-star Google reviews. See why Austin homeowners choose Red Agave for luxury landscaping, hardscape & outdoor living." (124) |

### 3. Short Meta Description

- `media.html` (105 chars) -- too short, should be expanded to 140-155 chars

---

## P1 -- High Priority

### 4. Blog Index Page Missing Proper SEO

`blog/index.html` should have a unique, keyword-rich title and description targeting "Austin landscaping blog" or "landscaping tips Austin TX".

### 5. HTML Entity Encoding in Titles

Several titles use `&amp;` instead of `&` in the `<title>` tag. While browsers render these correctly, it's cleaner to use the literal `&` character inside `<title>` tags (which is valid HTML5).

**Affected files:**
- `blog/drainage-engineering-austin-tx.html` -- `&amp;` in title
- `blog/fire-pit-engineering-austin-tx.html` -- `&amp;` in title
- `blog/gas-vs-wood-fire-pit-austin-tx.html` -- `&amp;` in title
- `blog/landscape-lighting-cost-austin-tx.html` -- `&amp;` in title
- `blog/natural-stone-vs-pavers-austin-tx.html` -- `&amp;` in title
- `blog/xeriscape-vs-traditional-lawn-austin-tx.html` -- `&amp;` in title
- `services/masonry-concrete-austin-tx.html` -- `&amp;` in title
- `services/turf-installation-austin-tx.html` -- `&amp;` in title

---

## P2 -- Medium Priority

### 6. No Favicon or Touch Icons

No `<link rel="icon">` or `<link rel="apple-touch-icon">` found on any page. This affects:
- Browser tab appearance (generic globe icon)
- Mobile bookmark/home screen icon
- Google mobile SERPs favicon display

**Fix:** Create a favicon (agave plant or RA monogram in gold on dark), generate ico + 192px + 512px PNG, add to `<head>` of all pages.

### 7. No `srcset` or Responsive Images

Zero `srcset` attributes found across the site. Mobile users download full-resolution desktop images. This wastes bandwidth and hurts Core Web Vitals (LCP).

**Fix:** Generate 400w, 800w, 1200w variants of key images and add `srcset` + `sizes` attributes.

### 8. Missing `robots.txt` Optimization

Current `robots.txt` exists but should reference the sitemap:
```
Sitemap: https://www.redagaveatx.com/sitemap.xml
```

---

## What's Working Well

- **Schema markup on every page** -- LocalBusiness, BreadcrumbList, FAQPage, Service schemas all present
- **Canonical tags on every page** -- no duplicate content issues
- **Open Graph tags on every page** -- social sharing will render correctly
- **Exactly one H1 per page** -- proper heading hierarchy
- **All CSS inlined** -- no render-blocking stylesheet requests
- **GA4 installed** -- analytics tracking active
- **Sitemap submitted** -- Google Search Console connected
- **HTTPS enabled** -- Let's Encrypt certificate auto-renewing
- **`defer` on all external scripts** -- Three.js, GSAP, ScrollTrigger won't block rendering
- **Non-blocking font loading** -- `media="print"` pattern on Google Fonts
