# SEO Rankings & Traffic Monitor

Pull current site health metrics and flag any pages that may have dropped.

## Steps:

### 1. Site Health Snapshot
Scan all HTML pages and generate a health report:
- Total page count
- Pages with meta titles over 60 chars
- Pages with meta descriptions over 160 chars or under 100 chars
- Pages missing FAQPage schema (that have FAQ sections)
- Pages missing canonical tags
- Pages not in sitemap.xml
- Pages missing GA4 snippet
- Broken internal links (hrefs to pages that don't exist)

### 2. Content Freshness
- List pages by last-modified date (from git log)
- Flag pages not updated in 90+ days that are targeting competitive keywords
- Flag blog posts with outdated year references (e.g., "2025" when it's 2026)

### 3. Keyword Coverage Check
Cross-reference `google-profile/keywords.md` against existing pages:
- For each priority keyword, which page targets it?
- Are there priority keywords with no dedicated page?
- Are there pages targeting the same keyword (cannibalization risk)?

### 4. Indexability Check
Use `curl` to check HTTP status codes for key pages:
```
curl -s -o /dev/null -w "%{http_code}" https://www.redagaveatx.com/services/xeriscape-austin-tx.html
```
Check the top 20 most important pages (homepage, service pages, top blog posts).

### 5. Page Speed Indicators
For each service page, report:
- File size (HTML only, since CSS is inline)
- Number of images (potential LCP bottleneck)
- Whether images use `loading="lazy"`
- Whether scripts use `defer`

### 6. Competitive Positioning
Search Google for the top 5 priority keywords and note:
- Where Red Agave appears (if visible in top 20)
- Who ranks #1-3 for each keyword
- Any featured snippets or People Also Ask that Red Agave could target

### 7. Output
Generate a dashboard-style report saved to `google-profile/seo-report-{date}.md` with:
- Overall health score (% of pages passing all checks)
- Critical issues (must fix)
- Opportunities (could improve rankings)
- Content gaps (keywords without pages)
- Recommended next actions (prioritized)

Compare against the most recent previous report if one exists.
