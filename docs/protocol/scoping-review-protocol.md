# Protocol for a Scoping Review: Automated Certainty of Evidence Grading

**Version:** 0.1 (Draft)
**Date:** 2026-02-09
**Status:** In Development

## Changelog
*   v0.1: Initial draft based on JBI Scoping Review Template.

---

## 1. Title
**Automated Certainty of Evidence Grading in Biomedicine: A Scoping Review**

## 2. Background / Rationale
[Drafting Needed]
*   **Context:** Evidence synthesis is the bottleneck of scientific automation.
*   **Problem:** Current LLMs are confident but not calibrated. We need "certainty" regarding claims.
*   **Gap:** We need to map what methods already exist to grade certainty/quality/risk-of-bias to avoid reinventing the wheel.
*   **Why Scoping?** To map the landscape, definitions, and evaluations (heterogeneous) rather than aggregate effect sizes (systematic).

## 3. Objectives
To map methods and evaluations for automated/semi-automated certainty/quality-of-evidence assessment in biomedicine, and identify evaluation gaps to guide benchmark and tool development.

## 4. Review Questions
*   **Task Definitions:** What tasks exist? (Overall certainty vs. domain downgrades vs. upstream inputs like RoB)
*   **Inputs:** What inputs do systems rely on? (SoF tables, full text, abstracts, structured evidence tables)
*   **Evaluation:** What evaluation methods are used? (Agreement, calibration, traceability, human usefulness)
*   **Failures:** What failure modes are reported? (Rare domains, context dependence, overconfidence)

## 5. Eligibility Criteria (PCC)

### Population
*   **Included:** Biomedical literature (Clinical trials, observational studies, systematic reviews).
*   **Excluded:** General domain text (News, Wikipedia).

### Concept
*   **Included:** Automated/Semi-automated systems grading "certainty," "quality," "strength," "risk of bias," or "trustworthiness."
*   **Excluded:** Pure extraction/summarization without quality judgment.

### Context
*   **Included:** Any (Research, Clinical Decision Support, Guideline Development).

## 6. Information Sources
We will search the following sources:
*   **Biomedical:** PubMed / MEDLINE
*   **Preprints:** medRxiv / bioRxiv
*   **CS/AI:** arXiv, ACL Anthology
*   **Citation Chasing:** Forward/Backward from key benchmarking papers.

## 7. Search Strategy
[Drafting Needed - PRISMA-S compliant]
*   **Draft String (PubMed):** `("certainty of evidence" OR "grade" OR "risk of bias" OR "evidence quality") AND ("automated" OR "machine learning" OR "nlp")`
*   *Note: Strategy will be peered reviewed (PRESS standard).*

## 8. Selection of Sources of Evidence
*   **Screening:** Dual independent screening (Title/Abstract → Full Text).
*   **Resolution:** Consensus or third reviewer.

## 9. Data Charting
*   **Process:** Pilot charting on 5-10 papers first.
*   **Form:** (To be defined in `data-charting-form.md`)

## 10. Data Items (Variables)
*   System/Agent Architecture
*   Level of Automation (Fully vs Semi)
*   Input Data (Abstract, Full Text, Tables)
*   Certainty Dimensions (RoB, Inconsistency, Indirectness, Imprecision, Pub Bias)
*   Evaluation Metrics (Kappa, Accuracy, Calibration Error)
*   Datasets Used

## 11. Synthesis Plan
*   **Evidence Map:** Visual summary of methods vs. certainty dimensions.
*   **Taxonomy:** Classification of approaches.
*   **Gap Analysis:** Where are the missing evaluations?

## 12. Protocol Registration
*   Target: OSF (Open Science Framework)
*   Date Planned: [Date]
