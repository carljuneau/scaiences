---
title: "Scaiences Scoping Review Protocol: Automated certainty-of-evidence assessment in biomedicine"
version: "v0.1"
date: "2026-02-09"
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
- v0.1 (2026-02-09): Initial draft.

> Notes on standards:
> - This protocol is written to support PRISMA-ScR reporting later (especially Methods items 5–13).  
> - Search reporting will follow PRISMA-S / PRISMA-Search.  
> - Optional search peer review using PRESS 2015.

---

# 1. Title
(Ensure the final report clearly identifies this as a *scoping review*.)  
**PRISMA-ScR item:** 1

**Working title:** Automated and semi-automated assessment of certainty/quality of biomedical evidence: a scoping review

---

# 2. Background and rationale
**PRISMA-ScR item:** 3

## 2.1 Context
Evidence synthesis is a critical bottleneck in biomedical decision-making. Currently, "certainty of evidence" (or quality of evidence) is assessed manually by experts using frameworks like GRADE. This process is slow, expensive, and limits the scalability of evidence-based medicine.

With the rise of Large Language Models (LLMs) and agentic workflows, there is a push to automate synthesis. However, LLMs are often confident but not calibrated. Without a reliable, traceable, and calibrated way to grade the *certainty* of evidence, automated synthesis is unsafe for downstream reasoning (hypothesis generation, experiment planning).

## 2.2 Why a scoping review (not a systematic review)
The literature on this topic is highly heterogeneous. Approaches vary from simple risk-of-bias classifiers (text classification) to complex agentic workflows generating structured evidence profiles. The terminology is also diverse ("certainty," "quality," "trustworthiness," "strength").

A systematic review (aggregating effect sizes) is not yet feasible. The goal of this scoping review is to **map key concepts**, **catalog existing methods**, and **identify evaluation gaps** to guide the development of future benchmarks and tools.

---

# 3. Objectives and review questions
**PRISMA-ScR item:** 4

## 3.1 Objectives
Primary objective:
- Map existing approaches for automated or semi-automated certainty/quality-of-evidence assessment in biomedicine and how they are evaluated.

Secondary objectives:
- Identify evaluation gaps (e.g., calibration, traceability, overconfidence, context dependence).
- Identify opportunities for new benchmarks/tools.

## 3.2 Review questions
RQ1: What tasks are covered (overall certainty grade vs domain-level reasons vs upstream inputs like RoB)?
RQ2: What inputs are used (full text, abstracts, extracted tables, Summary-of-Findings tables, guidelines, registries)?
RQ3: What methods are used (rules/ML/LLMs/RAG/agentic workflows; human-in-the-loop)?
RQ4: How are systems evaluated (agreement metrics, error taxonomies, human studies, calibration, traceability)?
RQ5: What limitations and failure modes are reported, and what is not yet addressed?

---

# 4. Protocol and registration
**PRISMA-ScR item:** 5

## 4.1 Where this protocol will be registered
- Planned registry/platform: OSF (or other)
- Registration link: <to be added>
- Registration date: <to be added>

## 4.2 Amendments
Any protocol changes after registration will be:
- logged in the changelog at the top of this document,
- dated,
- and described with rationale.
Major amendments will also be reflected in the OSF record.

---

# 5. Eligibility criteria
**PRISMA-ScR item:** 6

We will use PCC (Population–Concept–Context).

## 5.1 Population
- Biomedical and health research evidence and workflows (e.g., evidence syntheses, guideline development, clinical research decision support).

## 5.2 Concept
Include sources that describe or evaluate systems that:
- output an explicit certainty/quality-of-evidence judgment (e.g., “high/moderate/low/very low” or analogous),
  OR
- output domain-level reasons/components that are used to grade certainty (e.g., risk of bias, inconsistency, indirectness, imprecision, publication bias),
  OR
- generate structured evidence profiles intended to support certainty grading.

We will include both:
- fully automated systems, and
- semi-automated workflows with explicit human-in-the-loop components.

## 5.3 Context
- Any biomedical/clinical domain.
- Any setting (academic, industry, public sector).
- Any geography.

## 5.4 Types of sources of evidence
Include:
- peer-reviewed journal articles
- conference papers
- preprints
- technical reports with sufficient methodological detail

Exclude:
- opinion/editorials without a described method or system
- sources not focused on biomedicine/health
- tools with no description of how certainty/quality is produced

## 5.5 Limits
- Date range: [e.g., 2018–present] OR [no limit], with justification.
- Language: [e.g., English only], with rationale.
- Publication status: include preprints? (yes/no)

---

# 6. Information sources
**PRISMA-ScR item:** 7

We will search the following sources (list all that apply):
- PubMed/MEDLINE
- Embase (if available)
- Web of Science / Scopus (if available)
- arXiv
- bioRxiv / medRxiv
- IEEE Xplore (optional)
- ACL Anthology (optional)
- Backward citation chasing (reference lists)
- Forward citation chasing (via Google Scholar / Scopus, specify tool)

## 6.1 Search dates
- Initial search executed on: YYYY-MM-DD
- Most recent search executed on: YYYY-MM-DD (to be completed at end)

---

# 7. Search strategy
**PRISMA-ScR item:** 8  
**PRISMA-S / PRISMA-Search:** will be used to report full search details.

## 7.1 Approach
- Build a high-sensitivity strategy, then refine during a pilot.
- Record all iterations and the final strings.

## 7.2 Core concepts (keywords)
Concept A: LLMs / agents / AI-assisted research  
Concept B: certainty of evidence / quality of evidence / GRADE-like assessment / evidence profiles  
Concept C (optional): systematic reviews / guidelines / evidence synthesis contexts

## 7.3 Full electronic search strategy (at least one database)
Provide the complete strategy for at least one database (repeatable), including limits.

### Example (PubMed) — DRAFT
[Insert final PubMed search string here.]

## 7.4 Search strategy peer review (optional, recommended)
- We will use PRESS 2015 to peer review at least the PubMed/MEDLINE strategy.
- Reviewer: [Name / role]
- Date completed: YYYY-MM-DD

---

# 8. Selection of sources of evidence
**PRISMA-ScR item:** 9

## 8.1 Screening workflow
- Deduplicate records using: [tool/process]
- Stage 1: title/abstract screening
- Stage 2: full-text screening

## 8.2 Reviewers and conflict resolution
- Number of screeners per record: [1 or 2]
- Disagreement resolution: [discussion / third reviewer]
- Pilot screening of N records to calibrate criteria: [N]

## 8.3 Recording exclusions
- Full-text exclusions will be documented with reasons.

---

# 9. Data charting process
**PRISMA-ScR item:** 10

## 9.1 Charting approach
- We will chart data using a structured form (see Section 10).
- The form will be piloted on N studies and then finalized.
- Charting will be performed by: [1 reviewer + audit / 2 reviewers], with rationale.

## 9.2 Data integrity checks
- Spot checks on a random sample of N%.
- Any author contact for missing details: [yes/no], and how.

---

# 10. Data items
**PRISMA-ScR item:** 11

We will extract the following fields (draft; will be finalized after pilot):

## 10.1 Bibliographic
- Year
- Venue type (journal / conference / preprint / report)
- Domain area (e.g., clinical, preclinical, omics, etc.)

## 10.2 Task definition
- Output type:
  - overall certainty grade (ordinal)
  - domain-level downgrades/justifications
  - evidence profile generation
  - other (specify)
- Unit of assessment:
  - single study
  - outcome within a review
  - body of evidence across studies
  - guideline recommendation evidence set

## 10.3 Inputs and evidence substrate
- Inputs used:
  - full text / abstract / extracted tables / SoF tables / guidelines / registries / knowledge graphs
- Retrieval:
  - none / keyword / RAG / structured retrieval / other

## 10.4 Method / system design
- System type: rules / classical ML / LLM / LLM+RAG / agentic
- Human-in-the-loop: none / screening / adjudication / final rating / other
- Traceability approach: citations / quotes / provenance log / none

## 10.5 Evaluation
- Reference standard (human ratings? which population?)
- Metrics used (accuracy, F1, κ, calibration, etc.)
- Study design (retrospective benchmark, prospective, user study)
- Reported failure modes / limitations

## 10.6 Reproducibility
- Code available (Y/N)
- Data available (Y/N)
- Prompts/config available (Y/N)

---

# 11. Critical appraisal of individual sources of evidence
**PRISMA-ScR item:** 12

- We [will / will not] conduct critical appraisal.
- Rationale:
  - Scoping reviews typically aim to map evidence rather than judge quality; however, we may capture “rigor signals” (code availability, evaluation design, etc.) descriptively.

If we do any appraisal or “rigor signals,” specify:
- tool/criteria
- how it will be used in synthesis (descriptive only vs weighting)

---

# 12. Synthesis of results
**PRISMA-ScR item:** 13

## 12.1 Planned outputs
- Evidence map of tasks and methods (tables + counts)
- Taxonomy of approaches (inputs → method → outputs)
- Evaluation map (what is measured, how, and where gaps are)
- Gap analysis: “highest-leverage next steps” for benchmarks/tools

## 12.2 How we will summarize
- Descriptive statistics (counts, timelines)
- Narrative synthesis organized by task family and evaluation approach
- No meta-analysis planned (unless a narrow, homogeneous subset emerges, which would be treated as a separate study)

---

# 13. Funding and conflicts of interest
**PRISMA-ScR item:** 22 (final report)

- Funding for the scoping review: [None / source]
- Role of funders: [None / specify]
- Conflicts of interest: [declare]

---

# Appendix A — Draft charting form (copy/paste table)
[Include your structured extraction form here once stable.]

# Appendix B — Full search strategies (final)
- PubMed/MEDLINE: <full strategy>
- arXiv: <full strategy>
- bioRxiv/medRxiv: <full strategy>
- etc.

# Appendix C — PRISMA-ScR checklist (tracking)
[Link or embed the PRISMA-ScR fillable checklist and track “where we cover each item”.]

# Appendix D — PRISMA-S / PRISMA-Search checklist (tracking)
[Link or embed PRISMA-S/PRISMA-Search checklist and track search reporting completeness.]

## References
https://jbi-global-wiki.refined.site/space/MANUAL/355862497/10.+Scoping+reviews

https://www.prisma-statement.org/scoping?utm_source=chatgpt.com

https://www.prisma-statement.org/prisma-search?utm_source=chatgpt.com

https://pubmed.ncbi.nlm.nih.gov/27005575/