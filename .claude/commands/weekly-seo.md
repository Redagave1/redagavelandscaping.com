# Weekly SEO Routine

Run the full weekly SEO routine in sequence. This is the one command to trigger the whole workflow.

## Sequence:

### 1. Health Check (run /seo-monitor internally)
Scan all pages for technical issues, content freshness, keyword coverage, and indexability. Save report to `google-profile/seo-report-{date}.md`.

### 2. Technical Fixes
If the health check found P0 or P1 issues:
- Fix meta titles over 60 chars
- Fix meta descriptions over 160 chars
- Add missing schema markup
- Fix broken internal links
- Add missing pages to sitemap.xml

### 3. Content Opportunities
Review keyword coverage gaps:
- List priority keywords that don't have a dedicated page
- List existing pages that could be improved (thin content, missing sections)
- Suggest 1-2 new content pieces for the coming week

### 4. Internal Linking
Quick pass on internal linking:
- Check if any recent blog posts should link to service pages
- Check if service pages should link to recent blog posts
- Add 3-5 natural internal links

### 5. Summary Report
Output a concise summary:
- Pages checked: X
- Issues fixed: X
- Issues remaining: X  
- Content opportunities: X
- Internal links added: X
- Recommended focus for next week

Do NOT push changes automatically. Stage the changes and show a summary for review before committing.
