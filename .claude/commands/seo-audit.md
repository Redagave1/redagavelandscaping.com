# Weekly Technical SEO Audit

Run a comprehensive technical SEO audit of the site. Check every HTML page for:

## Sitewide Technical Checks

1. **Meta titles** — must be under 60 characters. Flag any over 60.
2. **Meta descriptions** — must be 120-155 characters. Flag any under 100 or over 160.
3. **H1 tags** — every page must have exactly one. Flag pages with 0 or 2+.
4. **Schema markup** — every page should have structured data. Check for Service, Article, FAQPage, LocalBusiness, BreadcrumbList as appropriate. Flag pages with FAQ sections but no FAQPage schema.
5. **Canonical tags** — every page must have one. Flag missing canonicals.
6. **Open Graph tags** — check og:title, og:description, og:image on all pages.
7. **Image alt text** — flag images missing alt attributes.
8. **Internal links** — check for broken internal links (href pointing to files that don't exist).
9. **Sitemap** — verify all pages in the site are listed in sitemap.xml.
10. **GA4** — verify the tracking snippet `G-QTW4E6VSZH` is present on every page.

## Local SEO Checks (on service + location pages)

Run the /local-page-audit checklist on all service pages and location pages. For each page verify:

11. **Keyword targeting** — locality + service keyword in title, meta description, H1, URL slug, first 100 words, and at least one H2/H3.
12. **Content depth** — word count appropriate for the niche, unique content (not boilerplate), pricing info, comparison tables, process sections, 6+ FAQs.
13. **NAP consistency** — business name "Red Agave Landscape" (not "Landscaping"), phone 512-695-7566, website redagaveatx.com — must match exactly across all pages.
14. **Brand accuracy** — "mild steel" not "aluminum", concrete $14/sq ft, steel edging $20/ft.
15. **Service area signals** — nearby cities/neighborhoods mentioned (Cedar Park, Westlake Hills, Round Rock, Bee Cave, Dripping Springs, Lakeway, Pflugerville, Georgetown).
16. **Cross-linking** — each service page links to at least 3 related service/blog pages.
17. **Trust signals** — Licensed & Insured mentioned, project photos present, free consultation CTA.

## Output

Summary table with:
- Total pages checked
- Issues found by category (P0 critical, P1 high, P2 medium)
- Specific files and line numbers for each issue
- Service page audit scores (page | score | grade | top issue)

Compare against the previous audit in `google-profile/tech-audit.md` to track what's been fixed and what's new.
