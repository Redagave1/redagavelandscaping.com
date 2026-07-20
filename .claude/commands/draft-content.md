# Draft Content Piece from Keyword

Given a target keyword (passed as $ARGUMENTS), write a complete blog post or service page ready to publish.

## Steps:

1. **Run the content-brief process internally** — check existing content, analyze keyword intent, determine format, identify sections needed.

2. **Check format-copy.md** — if `google-profile/format-copy.md` has a plan for this keyword, follow the title, sections, and keyword placement exactly.

3. **Write the full HTML page** using the site's template pattern:
   - GA4 snippet in head
   - Phone click tracking
   - Proper meta title (<60 chars), description (<155 chars), canonical, OG tags
   - Schema markup (Article + FAQPage if applicable)
   - Inline CSS (copy from an existing blog post as template)
   - Page header with background image
   - Content sections using `.sec`, `.s-eye`, `.s-title`, `.content-body` classes
   - Features grid where appropriate
   - Comparison table if the keyword implies comparison
   - FAQ section with 6-10 questions
   - Cross-links to related services/posts
   - Gold CTA section
   - Footer

4. **Brand voice check:**
   - Confident, minimal, no filler
   - Correct pricing (concrete $14/sq ft, steel edging $20/ft)
   - "Mild steel" not "aluminum"
   - Customer quotes verbatim only
   - Bebas Neue headlines, Montserrat body

5. **Save the file** to `blog/` or `services/` as appropriate with the naming pattern: `{topic}-austin-tx.html`

6. **Update sitemap.xml** with the new page.

7. **Add internal links** — find 2-3 existing pages that should link TO this new page and add the links.

8. **Generate a GBP post** — run the `/gbp-post` process on the new page to create a ready-to-publish Google Business Profile update. Output it alongside the report.

9. **Run a local page audit** — run `/local-page-audit` on the new page to verify it scores B or higher before publishing.

10. **Report** the new page URL, word count, target keywords, schema types added, local audit score, and the GBP post.
