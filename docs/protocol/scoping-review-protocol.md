# Protocol for a Scoping Review

**Title:** Automated Certainty of Evidence Grading in Biomedicine: A Scoping Review

**Protocol Version:** 0.1 (Draft)
**Date:** [Current Date]

## 1. Introduction

### Background
[Explain why this review is needed. Briefly: automated evidence synthesis is growing, but "certainty" (quality of evidence) is the bottleneck for safe downstream reasoning. We need to map what exists.]

### Review Question(s)
*   **Primary Question:** What methods and evaluations exist for the automated or semi-automated grading of certainty of evidence in biomedical literature?
*   **Sub-questions:**
    *   What inputs do these systems rely on (full text, abstracts, structured data)?
    *   What evaluation metrics are used (agreement, calibration, traceability)?
    *   What failure modes are reported?

## 2. Inclusion Criteria (PCC)

### Population / Participants
*   **Included:** Biomedical literature (clinical trials, observational studies, systematic reviews).
*   **Excluded:** General domain text (news, Wikipedia) unless specifically applied to biomedical claims.

### Concept
*   **Included:** Automated or semi-automated systems that assess "certainty," "quality," "strength," "risk of bias," or "trustworthiness" of evidence/claims.
*   **Excluded:** Systems that only do information retrieval or summarization without a quality judgment.

### Context
*   **Included:** Any setting (academic research, clinical decision support, guideline development).

## 3. Methods

### Search Strategy
We will search the following databases:
*   [ ] PubMed / MEDLINE
*   [ ] Embase
*   [ ] ACL Anthology (for NLP methods)
*   [ ] arXiv / biorXiv / medRxiv (preprints)

**Draft Search String (PubMed):**
`("certainty of evidence" OR "grade" OR "risk of bias" OR "evidence quality" OR "strength of evidence") AND ("automated" OR "machine learning" OR "artificial intelligence" OR "nlp" OR "text mining")`

### Source Selection (Screening)
1.  **Level 1:** Title and Abstract screening (Independent dual screening).
2.  **Level 2:** Full-text screening against inclusion criteria.
    *   Disagreements resolved by consensus or third reviewer.

### Data Extraction (Charting)
We will extract data using a structured form, capturing:
*   Study details (Author, Year, Source)
*   Task definition (Input -> Output)
*   Specific "certainty" dimensions assessed (e.g., Risk of Bias, Inconsistency, Indirectness)
*   Datasets used for training/eval
*   Evaluation metrics (e.g., Kappa, F1, Calibration Error)
*   Reported limitations

### Data Analysis and Presentation
Results will be presented in tabular form (evidence map) and a narrative summary describing the state of the art and identifying research gaps.

## 4. References
[Placeholder for references]
