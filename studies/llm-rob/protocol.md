---
title: "Can LLMs assess risk of bias in medical research? A pilot study protocol."
version: "v0.1"
date: "2026-03-22"
status: "DRAFT"
authors:
  - name: "[Author]"
    affiliation: "Scaiences"
---

# Pending questions

- **Primary outcome:** abstract-only or full-text input to the model?
- **Rubric source:** confirm citation for the 8-criterion observational-study RoB tool [CITATION NEEDED]
- **Model temperature:** confirm value (default suggested: 0)
- **Max tokens:** confirm value for model output

---

# Protocol version and date

Version 0.1. March 22, 2026.

# Background and rationale

Risk-of-bias (RoB) assessment is a core step in systematic review of medical research, but is time-intensive and subject to inter-rater variability. Large language models (LLMs) may be able to assist with structured appraisal tasks if given a clear rubric and constrained output format. This pilot tests whether two LLMs of different capability levels can produce criterion-level RoB judgments for observational studies that agree with expert gold labels, using a published 8-criterion rubric [CITATION NEEDED].

# Objective

To compare the accuracy of two LLMs (weak and strong) against expert gold-standard RoB labels for 14 observational studies, using a fixed 8-criterion rubric and abstract-only input [pending: see question above].

# Study sample

- 14 observational studies, single-arm intervention design
- Final study list and expert overall RoB labels are held privately
- Study IDs and PubMed URLs are public
- Abstract text will be collected locally before the run and stored in a gitignored private file

# Rubric

## Criteria

The following 8 criteria are applied to each study. Short keys are used in code; full criterion wording is in the prompt file (`pilot/prompts/rob_obs_prompt.txt`).

| Key | Criterion |
|-----|-----------|
| `study_group_representative` | Described study group consisted of more than 90% of eligible individuals |
| `intervention_and_participants_defined` | Intervention and participants clearly defined |
| `outcome_assessed_for_60pct` | Outcome assessed for at least 60% of the study group |
| `follow_up_length_reported` | Length of follow-up reported |
| `outcome_assessors_blinded` | Outcome assessors blinded to intervention status |
| `outcome_definition_objective_precise` | Outcome definition objective and precise |
| `important_prognostic_factors_accounted_for` | Important prognostic factors or confounders accounted for |
| `analysis_described_and_effect_quantified` | Analysis described and effect size quantified |

## Allowed outputs per criterion

`yes` | `no` | `unclear`

## Missingness rule

- Use `yes` only when the abstract explicitly supports the criterion being met.
- Use `no` only when the abstract gives positive evidence the criterion was not met.
- Use `unclear` when the abstract does not provide enough information to judge.

This rule must appear verbatim in the prompt.

## Overall RoB derivation rule

Overall RoB is derived in Python from the 8 criterion values. The model does not choose the overall label.

```
all yes              → low
any unclear, no no   → moderate
any no               → serious
```

# Models

| Role | Model ID |
|------|----------|
| Weak | `claude-haiku-4-5-20251001` |
| Strong | `claude-opus-4-6` |

Both models receive the identical prompt. Temperature: [PENDING]. Max tokens: [PENDING].

# Run policy

- One call per study per model.
- If the output is invalid JSON or missing any of the 8 criterion fields: retry once with the identical prompt.
- If the second call also fails: record a parse failure for that study; do not impute or manually fix.
- The prompt is frozen before any real-study run. The off-sample smoke test (one study outside the 14) may be used to verify that the pipeline runs end to end, but must not cause any prompt revision.
- No tuning. All 14 studies are scored once and treated as the final test set.

# Inputs

| File | Location | Contents | Privacy |
|------|----------|----------|---------|
| `studies.csv` | `pilot/data/public/` | study ID, first author, PubMed URL, study type | Public |
| `abstracts.csv` | `pilot/data/private/` | study ID, title, abstract text | Gitignored |
| `gold_labels.csv` | `pilot/data/private/` | study ID, expert overall RoB label | Gitignored |

The private directory is listed in `.gitignore`. Abstract text is collected manually from PubMed before the run.

# Output schema

Each model call returns a JSON object with the following structure:

```json
{
  "study_id": "string",
  "criteria": {
    "study_group_representative": "yes|no|unclear",
    "intervention_and_participants_defined": "yes|no|unclear",
    "outcome_assessed_for_60pct": "yes|no|unclear",
    "follow_up_length_reported": "yes|no|unclear",
    "outcome_assessors_blinded": "yes|no|unclear",
    "outcome_definition_objective_precise": "yes|no|unclear",
    "important_prognostic_factors_accounted_for": "yes|no|unclear",
    "analysis_described_and_effect_quantified": "yes|no|unclear"
  },
  "rationale": "string"
}
```

The model does not return an overall RoB label. That field is derived by Python.

# Scoring

**Primary:** exact agreement on overall RoB label (low / moderate / serious) between derived model label and expert gold label.

**Secondary:**
- Confusion matrix (3×3)
- Per-study mismatch list with criterion-level detail
- Majority-class baseline (count of most frequent gold label divided by 14)

No statistical tests are planned for a sample of 14.

# File layout

```
studies/llm-rob/
  protocol.md
  data/
    public/
      studies.csv
    private/              ← gitignored
      abstracts.csv
      gold_labels.csv
  prompts/
    rob_obs_prompt.txt
  src/
    schema.py             ← output schema and validation
    run_models.py         ← prompt building, model calls, raw output saving
    score_results.py      ← parsing, RoB derivation, scoring, reporting
  results/                ← raw outputs, parsed results, scored summaries
```

# Build order

1. Write `studies.csv` (public)
2. Collect abstracts; write `abstracts.csv` (private)
3. Write `gold_labels.csv` (private)
4. Write `rob_obs_prompt.txt`
5. Write `schema.py` and `score_results.py` — test on mocked data
6. Write `run_models.py`
7. Smoke test on one outside observational study
8. Run all 14 with weak model; save raw outputs
9. Run all 14 with strong model; save raw outputs
10. Score both; review mismatches
11. Write memo

# Transparency and reproducibility

Each result row will record: study ID, model name, prompt version, input mode, run timestamp, raw output file reference, 8 parsed criterion values, derived overall RoB, gold overall RoB, correct/incorrect.

Prompt version is a short string (e.g., `v1`) incremented if the prompt changes. Because the run policy forbids mid-run prompt changes, v1 is expected to be the only version.
