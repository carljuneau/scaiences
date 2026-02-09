# Scaiences / Certainty
Automated grading of **certainty of evidence** for biomedical claims — open methods, open evals, and reproducible benchmarks.

> Working idea: “synthesize before you hypothesize.”  
> If we can’t reliably grade evidence strength, we can’t safely automate downstream scientific reasoning.

## What this is
This project is an open, research-focused effort to build and evaluate an automated tool that helps **grade certainty of evidence** for biomedical questions.

The goal is not “pretty summaries.” The goal is **evidence-grounded judgments** with:
- explicit reasoning,
- traceability to sources,
- calibrated uncertainty,
- and evaluation against human references.

## Why start with certainty-of-evidence grading
We started from a broad ambition: **LLM agents that accelerate life-science research** (evidence synthesis → hypothesis generation → experiment planning).

We chose to start smaller because:
- Certainty grading is a real bottleneck in evidence synthesis.
- It is slow and expensive for humans.
- It is safety-critical: downstream agents should not act confident on weak evidence.
- It is measurable: we can benchmark agreement, calibration, and failure modes.

This module is designed to become a component in a larger agentic pipeline later.

## What “certainty of evidence” means here
By “certainty,” we mean a structured judgment about how much confidence we should place in a claim, given the evidence.

We will likely operationalize this using familiar domains (inspired by common evidence-grading approaches):
- risk of bias / internal validity
- inconsistency across studies
- indirectness (population, intervention, outcomes)
- imprecision (uncertainty, sample size, wide intervals)
- potential publication bias / selective reporting

**Important:** This tool does not replace expert review. It produces a **transparent, auditable suggestion**.

## Outputs (v1)
Given:
- a research question (or claim),
- a set of studies (or extracted evidence table),
- optional: a draft synthesis statement,

The system produces a structured **Evidence Certainty Card**:
- proposed certainty level (e.g., high / moderate / low / very low) *or* a numeric confidence score
- key reasons (bullet list)
- “cannot assess” flags (what is missing)
- citations / quotes supporting each reason (traceability)
- recommended next steps (what evidence would raise certainty)

## Non-goals (v1)
- Fully automating end-to-end systematic reviews
- Making clinical decisions or medical advice
- Using private patient data (no PHI)
- Claiming “ground truth” certainty for all topics

## Benchmarks and evaluation
This repo will ship a benchmark suite (“CertaintyBench”, working name) to measure:
- **agreement** with human-authored certainty judgments (where available)
- **calibration** (does confidence match accuracy?)
- **overconfidence rate** (confident but wrong)
- **traceability accuracy** (are reasons supported by cited text?)
- **failure modes** (taxonomy + examples)

We will prefer datasets that are:
- derived from published reviews / guidelines where feasible,
- reproducible (clear provenance),
- compatible with licensing constraints.

## Repository layout (proposed)
- `docs/`  
  - `vision.md` — project scope and rationale  
  - `protocol.md` — scoping/protocol notes (living)  
  - `taxonomy.md` — task + failure taxonomy  
- `data/`  
  - `sources.md` — provenance + licensing notes  
  - `v1/` — benchmark samples (or scripts to build them)  
- `benchmarks/`  
  - `certainty/` — tasks + rubrics + scoring code  
- `baselines/`  
  - simple baselines (rules, templates, minimal retrieval)  
- `results/`  
  - versioned reports  
- `scripts/`  
  - dataset build + eval run scripts

## How to run (placeholder)
This section will be updated once v1 lands.

Example target UX:
```bash
# 1) Install
pip install -r requirements.txt

# 2) Run the benchmark
python -m benchmarks.certainty.run --dataset data/v1 --out results/v1.json

# 3) Render report
python -m scripts.render_report --in results/v1.json --out results/v1_report.md
```

## Data and licensing

We will not host copyrighted full-text content that we do not have the right to redistribute.
Where full text is required, we will prefer:

* open-access sources,
* derived features/labels,
* or scripts that users can run locally to fetch permitted content.

## Safety and ethics

This is a research tool.

* Do not use it for clinical decisions.
* Treat outputs as fallible.
* Always keep a human expert in the loop for any real-world use.

## Roadmap (high level)

**Phase 0 (now):** ship a small, defensible benchmark + a baseline grader
**Phase 1:** improve traceability + calibration + abstention behavior
**Phase 2:** connect to evidence synthesis tasks (structured extraction → certainty)
**Phase 3:** extend to hypothesis triage and experiment planning

## Contributing

Contributions welcome:

* benchmark items + gold rationales
* scoring rubrics and adjudication rules
* failure case reports
* baseline methods
* documentation and reproducibility improvements

Open an Issue with:

* what you propose,
* what dataset/source,
* and what license constraints apply.

## Contact

* Maintainer: <Name / handle>
* Discussion: <GitHub Discussions / Discord / email>
