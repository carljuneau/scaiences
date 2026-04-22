# Scaiences Article Writer

Write a new article for scaiences.com based on a topic, URL, or brief provided by the user.

## Workflow

### 1. Research
- If a URL or external resource is provided, fetch and summarize it
- Read `docs/style-guide.md` for tone, formatting, and checklist rules
- Read one existing article (`autoresearch-meets-biology.html` or `age-reversal.html`) to match structure and voice

### 2. Plan (ask before writing)
- Propose: title options (5–10), label (`Science Spotlight` / `Brief Review` / `Commentary`), filename, section outline
- Title style: titles should sound like journal papers or letters — precise, declarative, scientific (e.g., "Reporting standards for LLM evaluations: a gap analysis" not "AI evals need better standards")
- Confirm with user before writing

### 3. Write (then humanize)
- Copy structure from `docs/article-template.html`
- File goes at repo root (e.g., `my-article.html`), never in a subfolder
- Byline: `<a href="about.html">Carl Juneau, PhD</a>` only — do not include the AI model name
- Date: `Month D, YYYY` format using today's date
- Open with 1–3 hook sentences before the first `<h2>`
- Sections use `<h2>` headings, `<h3>` for subsections
- Inline citations: `<a href="URL" target="_blank" rel="noopener">Author et al. (YEAR)</a>` — always Author (year), never "Author, year"
- When a citation appears inside existing parentheses, drop the inner parens: `(Author et al. YEAR)` not `(Author et al. (YEAR))`
- Keep language plain and direct. No hype words ("revolutionary", "game-changing")
- Epistemic humility is mandatory: we are not domain experts and have not done deep primary research. Use hedging language throughout — "it appears," "to our knowledge," "it seems," "as far as we are aware," "this suggests" — wherever a claim goes beyond what the cited source directly states. Do not hedge things the source explicitly says; do hedge interpretations, comparisons, and conclusions.
- Section headings must be plain and declarative — like a journal paper (e.g., "Reporting standards in medicine", "Implications for oversight"). Never hedge in headings ("What medicine appears to have built", "Why the gap may matter").
- Be honest about limits and unknowns
- Avoid over-explaining technical details for a life sciences audience
- After writing, run the `/humanizer` skill on all body `<p>` text before saving. Do not humanize headings, labels, byline, date, or HTML structure. Overwrite the file with the humanized version — do not create a separate copy.

### 4. Update index.html
- Add a new `<a class="spotlight-card">` entry at the top of the article list (above existing cards, below the roadmap)

### 5. Pre-publish check
Run through `docs/style-guide.md` Pre-publish Checklist before finishing.

### 6. Commit and push
- Commit both the new article and updated `index.html`
- Ask user before pushing unless they said to push

## Style Rules (summary)
- Tone: scientist writing for scientists, but accessible. Rigorous, not pompous.
- Voice: active. "We found" not "it was found"
- Sentences: 12–20 words target
- Uncertainty: use "may", "likely", "insufficient evidence" only when justified
- Citations: inline author-year, primary sources only
- Project names (e.g., autoresearch): lowercase mid-sentence, capitalize at sentence start
- Multiple authors: comma, not "&"
- Dates: `Month D, YYYY` — never ISO format

## Label Definitions
- **Science Spotlight** — evidence review of a biological/medical topic
- **Brief Review** — structured review of a research area with findings table or summary
- **Commentary** — opinion or analysis piece extrapolating beyond current evidence
