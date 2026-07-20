# Generate Google Business Profile Post from Blog

You are writing a Google Business Profile post based on a blog article from this project.

If a blog path is passed as $ARGUMENTS (e.g. `blog/fire-pit-engineering-austin-tx.html`), read that file and extract the body text. If no argument is provided, ask which blog post to use, or list the 10 most recent blog posts by git commit date for the user to pick from.

## Goal

Rewrite the blog post as a single Google Business Profile update that captures the most useful, click-worthy insight from the article.

## Hard Rules

- Output must be UNDER 1400 characters total (including spaces and any CTA). Count carefully.
- Match the EXACT tone of voice of the original blog: same vocabulary, sentence rhythm, level of formality, directness. Do not flatten the voice into generic marketing copy.
- Red Agave's voice: confident, minimal, short declarative lines. No filler. "We build what others won't" energy.
- Write in brand voice (first person plural "we" where appropriate).
- No hashtags. No emojis.
- No links inside the body (the link is added separately in GBP).
- No headings, no markdown, no bullet symbols like "•" or "-". Plain prose only, with line breaks where they aid readability.
- Use "mild steel" not "aluminum" if referencing materials.
- Concrete pricing starts at $14/sq ft if mentioned.

## Structure

1. **Hook line** — mirrors the angle of the blog. The same thing that would make someone click the article.
2. **Core value** — the 1-3 most important takeaways from the post, rewritten (not summarized in a meta way like "this blog explains..."). Deliver the actual insight.
3. **Soft CTA** — natural, in Red Agave's voice, inviting the reader to read the full post or get in touch. Examples: "Full breakdown on the blog." or "Read the full guide on our site." or "Questions? We're at 512-695-7566."

## Process

1. Read the full blog post HTML file.
2. Extract the body text (ignore nav, footer, head).
3. Identify the single most compelling angle — what would make an Austin homeowner stop scrolling?
4. Write the GBP post following the structure above.
5. Count the characters. If over 1400, tighten. Do not truncate — rewrite shorter.
6. Output the final post in a clean code block ready to copy-paste into the GBP composer.
7. Below the post, suggest which project photo from the `images/` directory would pair well with it (if you can determine one from the blog content).

## Example Output Format

```
[The GBP post text here, under 1400 characters, plain prose, no formatting]
```

**Character count:** [X] / 1400
**Suggested image:** `images/projects/axehandle/IMG_8591.webp` — shows the xeriscape + steel edging referenced in the post
**Blog source URL:** `https://www.redagaveatx.com/blog/[slug].html` — add this as the CTA link in GBP
