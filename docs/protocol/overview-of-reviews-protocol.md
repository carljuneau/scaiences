---
title: "Scaiences Overview of Reviews Protocol: Automated certainty-of-evidence assessment in biomedicine"
version: "v0.1"
date: "2026-02-10"
status: "DRAFT (pre-registration)"
authors:
  - name: "Wait for name"
    affiliation: "Scaiences"
    contact: "email"
contributors:
  - "Name (role)"
links:
  repo: "https://github.com/carljuneau/scaiences"
  osf_registration: "<osf url (once registered)>"
---

# Protocol changelog
- v0.1 (2026-02-10): Initial draft (Pivot from Scoping Review to Overview of Reviews).

> Notes on standards:
> - This protocol is written to support **PRIOR** (Preferred Reporting Items for Overviews of Reviews).
> - Critical appraisal of systematic reviews will use **AMSTAR 2**.

---

# 1. Title
**Automated and semi-automated assessment of certainty/quality of biomedical evidence: an overview of reviews**

---

# 2. Background and rationale

## 2.1 Context and Problem
Large language models (LLMs) and tool‑using “agent” systems are increasingly used to support biomedical research workflows, including evidence synthesis, critical appraisal, and related tasks that sit upstream of hypothesis generation and experiment design. At the same time, the evidence base on these uses is expanding quickly and across many publication types (systematic reviews, scoping reviews, narrative reviews, and surveys), with substantial variation in scope, methods, and the specific model generations evaluated.

This creates a practical problem for both researchers and builders: it is difficult to answer basic questions such as (i) where the evidence is strongest, (ii) which findings are stable across reviews, (iii) which outcomes and failure modes are consistently reported, and (iv) where evaluation standards remain weak. In fast‑moving AI settings, conclusions can also become outdated quickly as new model capabilities emerge (e.g., more agentic tool use and longer-horizon execution), making it even more important to separate durable methodological lessons (evaluation design, error types, reproducibility) from time‑bound performance claims tied to a specific model snapshot.

## 2.2 Why an overview of reviews
To address this, we will conduct an overview of reviews (also called an umbrella review or meta‑review), following the approach described by Cochrane: an overview uses explicit, systematic methods to identify and synthesize multiple systematic reviews on related questions, where the unit of inclusion and analysis is the review rather than the primary study.

An overview of reviews is justified here because the topic area has already generated multiple secondary syntheses that partially overlap in coverage and often differ in inclusion criteria, search dates, and evaluation focus. Consolidating this review‑level evidence can provide (1) a clearer map of where consensus exists, (2) a structured inventory of evaluation approaches and limitations, and (3) a defensible basis for deciding what new primary research, benchmarks, or tools are most likely to be additive.

---

# 3. Objectives and review questions

## 3.1 Review questions
RQ1: What review-level evidence exists regarding automated certainty assessment tasks?
RQ2: Which evaluation methods are consistently used across reviews?
RQ3: What failure modes and reporting gaps persist across the synthesis literature?

---

# 4. Methods

## 4.1 Eligibility criteria (PICOS-based)
*   **Population:** Biomedical research literature.
*   **Intervention:** Automated/Semi-automated systems for grading certainty/quality/risk-of-bias.
*   **Comparator:** Manual grading (gold standard) or none.
*   **Outcomes:** Agreement, efficiency, failure rates, calibration.
*   **Study Design:** Systematic reviews, scoping reviews, and meta-analyses. (Excluding primary studies).

## 4.2 Information sources
*   PubMed/MEDLINE
*   Embase
*   Cochrane Library
*   Epistemonikos

## 4.3 Search strategy
[Drafting Needed - Filter for Reviews/Meta-Analysis]

## 4.4 Selection process
Dual independent screening (Title/Abstract → Full Text).

## 4.5 Data collection process
Data will be extracted from included reviews using a standardized form:
*   Review characteristics (Type, Search dates, Number of included studies).
*   Overlap analysis (Citation matrix).
*   Main findings regarding automation performance.
*   Limitations reported by review authors.

## 4.6 Critical appraisal of included reviews
We will appraise the methodological quality of included systematic reviews using **AMSTAR 2** (A MeaSurement Tool to Assess systematic Reviews). This ensures we do not over-weight findings from low-quality syntheses.

## 4.7 Synthesis of results
*   **Overlap Management:** We will map the primary study overlap using a citation matrix (PRIOR guideline recommendation) to avoid double-counting evidence.
*   **Narrative Synthesis:** Summarizing findings by task type (e.g., Risk of Bias assessment vs GRADE assessment).
*   **Gap Map:** Visualizing areas with high/low review coverage.

---

# 5. References
[Include links to PRIOR guideline, AMSTAR 2 tool, etc.]