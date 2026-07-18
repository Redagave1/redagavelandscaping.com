# Generate Content Brief from Keyword

Given a target keyword (passed as $ARGUMENTS), generate a complete content brief for a new blog post or service page.

## Steps:

1. **Check existing content** — search the site for pages already targeting this keyword or close variations. List what exists and identify gaps.

2. **Analyze the keyword** — reference `google-profile/keywords.md` for volume estimates and intent. If the keyword isn't listed, estimate intent (informational, commercial, transactional) and approximate Austin-local volume.

3. **Check format-copy.md** — see if `google-profile/format-copy.md` has a content plan for this keyword. If so, follow it. If not, determine the winning format (guide, listicle, comparison, cost breakdown, how-to).

4. **Generate the brief:**
   - **Title options** (3 variations, all under 60 chars)
   - **Meta description** (under 155 chars, front-load value prop)
   - **H1** with slim-gold accent span
   - **Target word count** (based on format)
   - **Key sections** with heading text and 1-sentence description of each
   - **Keywords to include naturally** (primary + 3-5 secondary)
   - **Internal links** to include (which existing pages to link to/from)
   - **Schema type** (Article, FAQPage, HowTo, etc.)
   - **FAQ questions** (5-8 questions with answer summaries)
   - **CTA placement** (where to put contact links)

5. **Brand check** — verify the brief uses correct pricing ($14/sq ft concrete, $20/ft steel edging, mild steel not aluminum) and matches Red Agave's confident, minimal voice.

Output the brief in a format that can be handed directly to a content writer or used as the basis for a /draft-content command.
