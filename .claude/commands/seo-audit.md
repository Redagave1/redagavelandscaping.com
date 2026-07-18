# Weekly Technical SEO Audit

Run a comprehensive technical SEO audit of the site. Check every HTML page for:

1. **Meta titles** — must be under 60 characters. Flag any over 60.
2. **Meta descriptions** — must be 120-155 characters. Flag any under 100 or over 160.
3. **H1 tags** — every page must have exactly one. Flag pages with 0 or 2+.
4. **Schema markup** — every page should have structured data. Check for Service, Article, FAQPage, LocalBusiness, BreadcrumbList as appropriate.
5. **Canonical tags** — every page must have one. Flag missing canonicals.
6. **Open Graph tags** — check og:title, og:description, og:image on all pages.
7. **Image alt text** — flag images missing alt attributes.
8. **Internal links** — check for broken internal links (href pointing to files that don't exist).
9. **Sitemap** — verify all pages in the site are listed in sitemap.xml.
10. **GA4** — verify the tracking snippet `G-QTW4E6VSZH` is present on every page.

Output a summary table with:
- Total pages checked
- Issues found by category (P0 critical, P1 high, P2 medium)
- Specific files and line numbers for each issue

Compare against the previous audit in `google-profile/tech-audit.md` to track what's been fixed and what's new.
