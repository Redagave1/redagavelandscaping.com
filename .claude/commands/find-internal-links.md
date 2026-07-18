# Find Internal Linking Opportunities

Scan the site for internal linking opportunities. This helps distribute page authority and improve crawlability.

## Steps:

1. **Build a page inventory** — list all HTML pages with their H1, title, and primary keyword.

2. **For each service page**, check:
   - Which blog posts mention this service but don't link to the service page?
   - Which location pages should link to this service?
   - Which project pages feature this service but don't link to it?

3. **For each blog post**, check:
   - Does it mention services without linking to the service page? (e.g., mentions "fire pit" but doesn't link to `services/fire-pits-austin-tx.html`)
   - Does it mention other blog topics without cross-linking?
   - Does it have cross-links in the footer section?

4. **For each location page**, check:
   - Does it link to all relevant service pages?
   - Does it link to relevant blog posts?

5. **Check orphan pages** — pages with zero internal links pointing to them.

6. **Output a prioritized list:**
   - High priority: service pages with few inbound links
   - Medium priority: blog posts that should cross-link
   - Low priority: location pages missing service links

Format: `[source page] → [target page] — [anchor text suggestion]`

Only suggest links where the context is natural. Don't force links where the topic doesn't fit.
