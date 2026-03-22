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

- **Primary outcome:** abstract-only or full-text input to the model? Abstract-only: public, easier to replicate. Full-text: mirror expert's task, real-world assessment; copywright? Still, I'd favour full-text.
- **Analysis level:** Experts assessed risk of bias as "serious" for all 14 studies. Should we look at agreement with each of the 8 criteria as well? I'd favour yes. criterion rubric to assessment was "serious" abstract-only or full-text input to the model? Abstract-only: public, easier to replicate. Full-text: mirror expert's task, real-world assessment. But copywright? Bottom line, I'd favour full-text.
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
- Public study list: `studies/llm-rob/data/public/studies.csv`
- Abstract text collected locally: `studies/llm-rob/data/private/abstracts.csv` (gitignored)

| ID | First author | Year | DOI | Journal |
|----|-------------|------|-----|---------|
| Bernard Stoecklin | Bernard Stoecklin | 2020 | 10.2807/1560-7917.ES.2020.25.6.2000094 | Euro Surveill |
| Bi | Bi | 2020 | 10.1016/S1473-3099(20)30287-5 | Lancet Infect Dis |
| Burke | Burke | 2020 | 10.15585/mmwr.mm6909e1 | MMWR Morb Mortal Wkly Rep |
| Chen | Chen | 2020 | 10.2196/19540 | J Med Internet Res |
| Choi 2020b | Choi | 2020 | 10.3390/ijerph17113984 | Int J Environ Res Public Health |
| Choi | Choi | 2020 | 10.1136/postgradmedj-2020-137738 | Postgrad Med J |
| Cowling | Cowling | 2020 | 10.1016/S2468-2667(20)30090-6 | Lancet Public Health |
| Davalgi | Davalgi | 2020 | — | Indian J Comm Health |
| Dinh | Dinh | 2020 | 10.1093/jtm/taaa047 | J Travel Med |
| Lam | Lam | 2020 | 10.1016/j.ijid.2020.06.057 | Int J Infect Dis |
| Nachega | Nachega | 2020 | 10.1093/cid/ciaa695 | Clin Infect Dis |
| Ng | Ng | 2020 | 10.15585/mmwr.mm6911e1 | MMWR Morb Mortal Wkly Rep |
| Wilasang | Wilasang | 2020 | 10.1093/jtm/taaa095 | J Travel Med |
| Wong | Wong | 2020 | 10.1503/cmaj.200563 | CMAJ |

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
pilot/
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

# References

Bernard Stoecklin S, Rolland P, Silue Y, et al. First cases of coronavirus disease 2019 (COVID-19) in France: surveillance, investigations and control measures, January 2020. Euro Surveill. 2020;25(6):2000094. doi:10.2807/1560-7917.ES.2020.25.6.2000094

Bi Q, Wu Y, Mei S, et al. Epidemiology and transmission of COVID-19 in 391 cases and 1286 of their close contacts in Shenzhen, China: a retrospective cohort study. Lancet Infect Dis. 2020;S1473-3099(20)30287-5. doi:10.1016/S1473-3099(20)30287-5

Burke RM, Midgley CM, Dratch A, et al. Active Monitoring of Persons Exposed to Patients with Confirmed COVID-19 — United States, January–February 2020. MMWR Morb Mortal Wkly Rep. 2020;69:245–246. doi:10.15585/mmwr.mm6909e1

Chen CM, Jyan HW, Chien SC, et al. Containing COVID-19 Among 627,386 Persons in Contact With the Diamond Princess Cruise Ship Passengers Who Disembarked in Taiwan. J Med Internet Res. 2020;22(5):e19540. doi:10.2196/19540

Choi H, Cho W, Kim MH, Hur JY. Public Health Emergency and Crisis Management: Case Study of SARS-CoV-2 Outbreak. Int J Environ Res Public Health. 2020;17:3984. doi:10.3390/ijerph17113984

Choi JY. COVID-19 in South Korea. Postgrad Med J. 2020;96:399–402. doi:10.1136/postgradmedj-2020-137738

Cowling BJ, Ali ST, Ng TWY, et al. Impact assessment of non-pharmaceutical interventions against coronavirus disease 2019 and influenza in Hong Kong: an observational study. Lancet Public Health. 2020;5(5):e279–e288. doi:10.1016/S2468-2667(20)30090-6

Davalgi S, Malatesh U, Rachana A, et al. Comparison of measures adopted to combat COVID-19 pandemic by different countries in WHO regions. Indian J Comm Health. 2020;32(2). doi:10.47203/IJCH.2020.v32i02SUPP.023

Dinh L, Dinh P, Nguyen PDM, Nguyen DHN, Hoang T. Vietnam's response to COVID-19: prompt and proactive actions. J Travel Med. 2020;27(3):taaa047. doi:10.1093/jtm/taaa047

Lam HY, Lam TS, Wong CH, et al. The epidemiology of COVID-19 cases and the successful containment strategy in Hong Kong-January to May 2020. Int J Infect Dis. 2020;98:51–58. doi:10.1016/j.ijid.2020.06.057

Nachega JB, Grimwood A, Mahomed H, et al. From Easing Lockdowns to Scaling-Up Community-Based COVID-19 Screening, Testing, and Contact Tracing in Africa. Clin Infect Dis. 2020;ciaa695. doi:10.1093/cid/ciaa695

Ng Y, Li Z, Chua YX, et al. Evaluation of the Effectiveness of Surveillance and Containment Measures for the First 100 Patients with COVID-19 in Singapore. MMWR Morb Mortal Wkly Rep. 2020;69(11):307–311. doi:10.15585/mmwr.mm6911e1

Wilasang C, Sararat C, Jitsuk NC, et al. Reduction in effective reproduction number of COVID-19 is higher in countries employing active case detection with prompt isolation. J Travel Med. 2020;taaa095. doi:10.1093/jtm/taaa095

Wong SYS, Kwok KO, Chan FKL. What can countries learn from Hong Kong's response to the COVID-19 pandemic? CMAJ. 2020;192(19):E511–E515. doi:10.1503/cmaj.200563
