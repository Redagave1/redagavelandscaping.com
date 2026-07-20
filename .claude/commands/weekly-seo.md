# Weekly SEO Routine

Run the full weekly SEO routine in sequence. This is the one command to trigger the whole workflow.

## Sequence:

### 1. Health Check (run /seo-monitor internally)
Scan all pages for technical issues, content freshness, keyword coverage, and indexability. Save report to `google-profile/seo-report-{date}.md`.

### 2. Local Page Audits
Run the /local-page-audit checklist on the 5 priority service pages and flag any that score below B:
- `services/xeriscape-austin-tx.html`
- `services/fire-pits-austin-tx.html`
- `services/outdoor-kitchens-austin-tx.html`
- `services/custom-decks-austin-tx.html`
- `services/pergolas-austin-tx.html`

Also audit any location pages that were recently created or modified. For each page, check:
- Keyword targeting (locality + service in title, H1, URL, body)
- Content depth (word count, unique content, FAQs, pricing, comparison tables)
- Schema markup (Service, FAQPage, correct areaServed)
- NAP consistency (Red Agave Landscape, 512-695-7566, redagaveatx.com)
- Internal linking (cross-links, blog links, navigation)
- Images (alt text, WebP format, lazy loading)
- Technical (canonical, GA4, OG tags, sitemap)
- Trust signals (credentials, photos, reviews, CTAs)

Output a summary table: page | score | grade | top issue.

### 3. Technical Fixes
If the health check or audits found P0 or P1 issues:
- Fix meta titles over 60 chars
- Fix meta descriptions over 160 chars
- Add missing schema markup (especially FAQPage where FAQs exist)
- Fix broken internal links
- Add missing pages to sitemap.xml
- Fix any NAP inconsistencies
- Add missing locality signals to underperforming pages

### 4. Content Opportunities
Review keyword coverage gaps:
- List priority keywords from `google-profile/keywords.md` that don't have a dedicated page
- List existing pages that could be improved (thin content, missing sections, low audit scores)
- Suggest 1-2 new content pieces for the coming week
- Check if any pages have outdated year references

### 5. Internal Linking
Quick pass on internal linking:
- Check if any recent blog posts should link to service pages
- Check if service pages should link to recent blog posts
- Check if location pages link to all relevant services
- Add 3-5 natural internal links

### 6. Summary Report
Output a concise summary:
- Pages checked: X
- Local audit scores: [table of service page grades]
- Issues fixed: X
- Issues remaining: X
- Content opportunities: X
- Internal links added: X
- Recommended focus for next week

Do NOT push changes automatically. Stage the changes and show a summary for review before committing.
