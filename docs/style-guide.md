# Scaiences Style Guide

**Goal:** Write like a scientist, but accessible. Rigorous, clear, and unpretentious.

## Principles

### 1. Clarity beats cleverness
*   Prefer simple words.
*   One idea per sentence.

### 2. Separate evidence from interpretation
*   **Evidence:** What a paper/report shows.
*   **Interpretation:** What we think it implies.
*   **Hypothesis:** What we think might be true, but isn’t shown yet.

### 3. Make uncertainty explicit
*   Use calibrated terms (“may,” “likely,” “insufficient evidence”) only when justified.
*   If you don’t know, say what you don’t know.

### 4. Make claims traceable
*   For every non-obvious factual claim, include a citation.
*   For key decisions, cite both “why” and “how”.

## Structure Rules
*   **Start every major doc with:**
    *   **Goal** (1–2 sentences)
    *   **What we decided** (3–5 bullets)
    *   **What’s next** (1–3 bullets)
*   **Use consistent headings:**
    *   Background → Objective → Methods → Outputs → Limits
*   **Every article must include a Limitations section** placed immediately before the conclusion.
    *   Describe scope constraints and what the article does not cover.
    *   Distinguish recommendations by evidential status: "best practice" (convergence across sources) vs. "rule of thumb" (practical synthesis where consensus is limited).
*   **Conclusion heading should be a short declarative claim**, not the word "Conclusion".

## Sentence-Level Rules
*   **Length:** Target 12–20 words per sentence when possible.
*   **Voice:** Use **active voice** unless passive is clearer.
    *   *Good:* “We screened abstracts…”
    *   *Bad:* “Abstracts were screened…”
*   **Concrete actor in the subject.** Name who does the action. Avoid using abstractions (approaches, systems, methods, frameworks) as the grammatical subject.
    *   *Good:* “We screened abstracts…” / “The team queues the next run…”
    *   *Bad:* “Abstracts were screened…” / “This approach enables screening…”
*   **Avoid stacked nouns:**
    *   *Good:* “dataset to evaluate certainty grading”
    *   *Bad:* “certainty grading evaluation dataset”

## Terminology
*   **Acronyms:** Define on first use, then reuse consistently (e.g., “large language model (LLM)”).
*   **Consistency:** Avoid synonyms. Pick one term (e.g., “certainty of evidence”) and stick to it.

## Numbers and Results
*   **Denominators:** Always include them. “12/30 papers…” not “12 papers…”
*   **Absolute counts:** “12/30 (40%)”
*   **Metrics:** If reporting agreement, specify the measure (e.g., Cohen's κ) and context.

## Citations
*   Cite primary sources (papers, guidelines).
*   For methods claims, cite the guideline (PRISMA/JBI/PRESS).
*   In prose, use **Author (year)** format — e.g., “Smith et al. (2024) found…” — never “Smith et al., 2024”.
*   When the citation is already inside parentheses, drop the inner parentheses: `(Smith et al. 2024)` not `(Smith et al. (2024))`.
*   Do **not** use journal names or article titles as a substitute for the authors in narrative citations.

## Tone
*   **No Hype:** Avoid “revolutionary,” “game-changing,” “solves.”
*   **Precision:** “improves reproducibility” rather than “makes it better.”
*   Prefer **plain positive statements** over contrastive phrasing like “it is not X, it is Y.” State what the evidence shows directly.

## Pre-publish Checklist
Before publishing any article, verify:
- [ ] File is at repo root (not in a subfolder)
- [ ] `<title>` matches `<h1>` and ends with `| Scaiences`
- [ ] `<meta name="description">` is filled in (1–2 sentences)
- [ ] Label is one of: `Science Spotlight`, `Brief Review`, `Commentary`
- [ ] Hook sentence(s) appear before the first `<h2>`
- [ ] Byline uses comma-separated authors, AI model first if applicable
- [ ] Date uses `Month D, YYYY` format
- [ ] Back-link points to `index.html`
- [ ] Stylesheet points to `style.css` (root-relative)
- [ ] All external links use `target="_blank" rel="noopener"`
- [ ] New article card added to `index.html`
- [ ] Limitations section present, placed just before the conclusion
- [ ] Conclusion heading is a declarative claim (not the word "Conclusion")

## Article Formatting
*   **Dates:** Use full written format: `Month D, YYYY` (e.g., "March 12, 2026"). Never use ISO format (`2026-03-12`) in article bylines.
*   **Multiple authors:** Separate with a comma, not "&" or "and". e.g., `Claude Sonnet 4.6, Carl Juneau, PhD`
*   **autoresearch (and similar project names):** Lowercase mid-sentence; capitalize at the start of a sentence.

## Build-in-Public Norms
*   **Versioning:** Use versions and dates. e.g., `Protocol v0.1 (2026-02-09)`
*   **Changelogs:** Keep a short changelog at the top of protocol files.
