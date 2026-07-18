# Red Agave Landscape — Project Context

## Business
Red Agave Landscape is a luxury design+build landscaping company in Austin, TX.
- **Owner:** Jensen Mehrens
- **Phone:** 512-695-7566
- **Email:** redagaveatx@gmail.com
- **Site:** redagaveatx.com (hosted on Netlify)
- **ICP:** Homeowners in Austin metro (Cedar Park, Westlake Hills, Round Rock, Bee Cave, Dripping Springs, Lakeway, Pflugerville, Georgetown) with $15K-$100K+ outdoor living budgets

## Core Services (priority order)
1. Xeriscaping & native plant design
2. Custom fire pits (steel, stone, gas)
3. Outdoor kitchens
4. Custom decks (IPE, cedar, composite)
5. Pergolas & pavilions (steel + cedar)
6. Landscape lighting (WLED/FCOB)
7. Patios (concrete, pavers, flagstone)
8. Masonry & concrete
9. Pools
10. Artificial turf
11. Steel planters
12. Full yard design+build

## Material Facts (enforce in all content)
- **Mild steel only** — never say "aluminum" as a Red Agave material. We fabricate mild steel in-house.
- **Concrete starts at $14/sq ft** (not $6 or $12)
- **Steel edging starts at $20/ft** (1/4-inch, bent and welded on-site)
- **Decomposed granite: $6-$9/sq ft installed**
- **Limestone comes in 2x4 ft slabs** — don't call it "pavers"
- Customer review quotes must NEVER be altered — verbatim only

## Brand Voice
Confident and minimal. Short declarative lines. No filler, no fluff.
"We build what others won't" energy — never "we provide quality services."
Headings are statements, not descriptions.

## Design System
- **Palette:** `--dark:#080b06`, `--dark2:#0d120a`, `--dark3:#0a1208`, `--gold:#c9a84c`, `--gold-light:#e8c96a`, `--cream:#f0ead6`
- **Fonts:** Bebas Neue (headlines), Montserrat (body/buttons). No other fonts ever.
- **No purple, pink, teal, white backgrounds, Bootstrap/Tailwind aesthetics**
- All CSS inlined, all JS deferred, Google Fonts loaded via print/onload pattern
- `.rev` class for scroll reveal animation on all content elements
- Section backgrounds alternate: `var(--dark)`, `var(--dark2)`, `var(--dark3)`

## Tech Stack
- Static HTML site, no build system
- Inline CSS, CDN-loaded JS (GSAP, Three.js) with `defer`
- Hosted on Netlify (remote: `netlify`), GitHub backup (remote: `origin`)
- **Push command:** `TMPDIR=/tmp git push netlify main && TMPDIR=/tmp git push origin main`
- GA4: `G-QTW4E6VSZH` (installed on all pages)
- Phone click tracking: `phone_click` event
- Contact form: `form_submission` event

## Site Structure (112 pages)
- `/index.html` — homepage
- `/services.html` — services hub
- `/services/*.html` — 13 individual service pages
- `/blog/*.html` — 65+ blog posts (SEO content)
- `/locations/*.html` — 15 location pages
- `/projects/*.html` — 8 signature project case studies
- `/gallery.html`, `/featured.html`, `/reviews.html`, `/about.html`, `/contact.html`, `/media.html`, `/service-area.html`, `/before-after.html`
- `/sitemap.xml` — update when adding new pages
- `/robots.txt`, `/llms.txt`

## SEO Reference Files
All in `google-profile/`:
- `keywords.md` — priority keywords with Austin volume estimates and AI prompt variations
- `serp-analysis.md` — SERP analysis for top keywords
- `format-copy.md` — content format & copy plan for 10 keywords (titles, sections, publishing calendar)
- `tech-audit.md` — technical SEO audit findings
- `ux-audit.md` — UX audit findings
- `link-prospects.md` — link building opportunities

## SEO Workflow (Weeks 1-3 completed)
**Week 1:** Keyword research, SERP analysis, content format planning
**Week 2:** Technical audit fixes (meta titles <60 chars, descriptions <155 chars, GA4 sitewide, UX fixes)
**Week 3:** Service page optimization (5 priority pages with FAQPage schema, pricing tables, comparison tables, expanded FAQs, process sections)
**Week 4:** Automation (this CLAUDE.md, reusable commands, monitoring)

## Page Template Pattern
Service/blog pages follow this structure:
```
page-header (background image + overlay + h1)
sec (content-body with intro paragraphs)
sec (features-grid with 6 items)
sec (comparison table)
sec (pricing tiers)
sec (process grid — 4 columns)
sec (photo-grid with 3 project images)
sec (features-grid — "What's Included")
sec (faq-list with 6-10 details/summary items)
cross-links
CTA section (gold background)
footer
```

## CSS Classes Reference
- `.sec` — section wrapper
- `.s-eye.rev` — eyebrow text above heading
- `.s-title.rev` — section heading (Bebas Neue)
- `.content-body.rev` — text block wrapper
- `.features-grid` — 3-column card grid
- `.feature-item.rev` — card with `.feature-num`, `.feature-name`, `.feature-desc`
- `.faq-list` — FAQ container
- `.faq-item.rev` — `<details>` element with `.faq-q` (summary) and `.faq-a` (answer)
- `.photo-grid` — 3-column image grid
- `.cross-links.rev` — pill-shaped links to related services
- `.page-header` — hero section with `.page-header-bg`, `.page-header-ov`, `.page-header-inner`

## Schema Markup
Every page should have:
- `Service` or `Article` schema (depending on page type)
- `FAQPage` schema (separate script tag) if page has FAQ section
- `LocalBusiness` reference via `"provider":{"@id":"https://www.redagaveatx.com/#business"}`
- `BreadcrumbList` schema on blog posts
