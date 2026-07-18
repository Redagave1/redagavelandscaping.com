# Generate Schema Markup for a Page

Given a page path (passed as $ARGUMENTS), analyze the page content and generate or update its structured data markup.

## Steps:

1. **Read the page** and identify its type (service page, blog post, location page, project page).

2. **Check existing schema** — see what structured data is already present.

3. **Generate/update schema** based on page type:
   - **Service pages:** `Service` schema + `FAQPage` if FAQs exist
   - **Blog posts:** `Article` schema + `BreadcrumbList` + `FAQPage` if FAQs exist + `HowTo` if step-by-step content
   - **Location pages:** `LocalBusiness` with `areaServed`
   - **Project pages:** `CreativeWork` or `Service` with project details
   - **Review page:** `AggregateRating` + individual `Review` schemas

4. **Validate:**
   - All FAQ questions in schema must match FAQ questions on the page exactly
   - Provider references `{"@id":"https://www.redagaveatx.com/#business"}`
   - Area served includes Austin, TX
   - No duplicate schema types

5. **Insert the schema** as `<script type="application/ld+json">` tags in the page `<head>`, after existing schema blocks.

6. **Report** what schemas were added/updated.
