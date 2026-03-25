# Can LLMs assess risk of bias in medical research? A pilot study protocol
Juneau CE*, Siegel N
*Corresponding author: carl-etienne.juneau@umontreal.ca

# Pending questions

## Potentials research questions

### Prompt/protocol evaluation

- How does RoB agreement change as prompt quality increases: minimal instruction → reviewer documentation → documentation + worked example?
- How does agreement scale with the number of in-context worked examples (0, 1, 2, 3, etc.)?

### Direct capability baseline

- Does a strong model agree more with expert RoB labels than a weak model when both use the same rubric?

### Scalable oversight

- Does a strong model's RoB agreement improve when it first receives the weak model's assessments?
- Do strong models improve their RoB agreement more when they receive weak labels with rationales than with labels alone?

### Others
- **Weak labels:** Should we use a single human investigator as the weak baseline instead of a weak LLM? More external validity, according to Pavel Izmailov: "I think it would be even more interesting if you could generate more realistic weak labels, as in not use weak models, but instead use some biased human signal as labels. To clarify, in weak-to-strong generalization we are interested in whether strong models can generalize biased and imperfect signal coming from supervisors (humans). We don't know if using weak models is a meaningful model of the type of errors and biases that would be coming from humans. If you have more realistic weak labels, that would be better."
- **Analysis level:** Experts assessed risk of bias as "serious" for all 14 studies. I'm afraid this may artifically boost model performance. Should we look at agreement with each of the 8 subcriteria as well? I think yes.
- **Sources of worked examples:** Should the prompt include a worked example of RoB assessment (one-shot) to guide the model, or rely on the rubric alone (zero-shot)? Candidate examples: Mulder et al. 2019 (different domain, lower contamination) or a COVID-19 quarantine Cochrane review (closer domain, higher contamination risk).

---

# Introduction

In medical research, we assess risk of bias to determine how much we can trust the findings of a given study. We do this because we know that flawed study design can systematically push results in a particular direction, leading to incorrect conclusions about the safety or effectiveness of interventions (Higgins et al. 2024). 

To assess risk of bias, subject matter experts typically use a checklist of criteria covering domains such as selection of participants, measurement of outcomes, handling of missing data, and control for confounding. Criteria are then tallied up and aggregated into an overall rating.

This exercise can be time-intensive and error-prone, especially in comprehensive literature reviews. Large language models (LLMs) could reduce this burden, potentially making reviews faster and more consistent. However, there is little research on how well they actually perform at this task.

In this pilot study, we aim to compare the accuracy of two LLMs (weak and strong) against expert bias labels we generated during the Covid-19 pandemic (Juneau et al. 2023). We hypothesise that strong models will perform as well as human expert raters on this task, especially when given worked examples. 

# Methods

This pilot uses risk of bias assessments of 14 observational studies from our systematic review of Covid-19 contact tracing as a test set (Juneau et al. 2023). It asks whether two LLMs of different capability levels can produce criterion-level RoB judgments that agree with expert gold labels, using a published, established 8-criterion rubric (Mulder et al., 2019).

## Study sample
- 14 observational studies, single-arm intervention design
- Final study list and expert overall RoB labels are held privately
- Public study list: [Table - RoB_observational_studies.csv](data/public/Table%20-%20RoB_observational_studies.csv)
- Full-text PDFs collected locally: `studies/llm-rob/data/private/observational/` (gitignored)


## Rubric

### Criteria

See [Table 2 - RoB_criteria.csv](data/public/Table%202%20-%20RoB_criteria.csv) (SST). Allowed outputs per criterion: `yes` | `no` | `unclear`.

### Missingness rule

- Use `yes` only when the full text explicitly supports the criterion being met.
- Use `no` only when the full text gives positive evidence the criterion was not met.
- Use `unclear` when the full text does not provide enough information to judge.

This rule must appear verbatim in the prompt.

### Overall RoB derivation rule

Overall RoB is derived in Python from the 8 criterion values. The model does not choose the overall label.

```
all yes              → low
any unclear, no no   → moderate
any no               → serious
```

## Models

| Role | Model ID |
|------|----------|
| Weak | `claude-haiku-4-5-20251001` |
| Strong | `claude-opus-4-6` |

Both models receive the identical prompt. Temperature: 0. Max tokens: 1024.

## Run policy

- One call per study per model.
- If the output is invalid JSON or missing any of the 8 criterion fields: retry once with the identical prompt.
- If the second call also fails: record a parse failure for that study; do not impute or manually fix.
- The prompt is frozen before any real-study run. The off-sample smoke test (one study outside the 14) may be used to verify that the pipeline runs end to end, but must not cause any prompt revision.
- No tuning. All 14 studies are scored once and treated as the final test set.

## Inputs

| File | Location | Contents | Privacy |
|------|----------|----------|---------|
| `Table - RoB_observational_studies.csv` | `data/public/` | study ID, year, DOI, 8 RoB criteria, overall RoB | Public |
| `observational/` | `data/private/` | full-text PDFs, one per study | Gitignored |
| `gold_labels.csv` | `data/private/` | study ID, expert overall RoB label | Gitignored |

The private directory is listed in `.gitignore`.

## Output schema

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

## Scoring

**Primary:** exact agreement on overall RoB label (low / moderate / serious) between derived model label and expert gold label.

**Secondary:**
- Confusion matrix (3×3)
- Per-study mismatch list with criterion-level detail
- Majority-class baseline (count of most frequent gold label divided by 14)

No statistical tests are planned for a sample of 14.

## File layout

```
studies/llm-rob/
  data/
    public/
      Table - RoB_observational_studies.csv
      Table 2 - RoB_criteria.csv
    private/              ← gitignored
      observational/      ← full-text PDFs
      gold_labels.csv
  prompts/
    rob_obs_prompt.txt
  src/
    schema.py             ← output schema and validation
    run_models.py         ← prompt building, model calls, raw output saving
    score_results.py      ← parsing, RoB derivation, scoring, reporting
  results/                ← raw outputs, parsed results, scored summaries
```

## Build order

1. Prepare `Table - RoB_observational_studies.csv` (public) ✓
2. Collect full-text PDFs (private)
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

Higgins JPT, Thomas J, Chandler J, et al. (eds). Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane, 2024. www.cochrane.org/authors/handbooks-and-manuals/handbook/current

Juneau CE, Briand AS, Collazzo P, Siebert U, Pueyo T. Effective contact tracing for COVID-19: A systematic review. Glob Epidemiol. 2023;5:100103. doi:10.1016/j.gloepi.2023.100103

Mulder RL, Bresters D, Van den Hof M, et al. Hepatic late adverse effects after antineoplastic treatment for childhood cancer. Cochrane Database Syst Rev. 2019;4:CD008205. doi:10.1002/14651858.CD008205.pub3

Lam HY, Lam TS, Wong CH, et al. The epidemiology of COVID-19 cases and the successful containment strategy in Hong Kong-January to May 2020. Int J Infect Dis. 2020;98:51–58. doi:10.1016/j.ijid.2020.06.057

Nachega JB, Grimwood A, Mahomed H, et al. From Easing Lockdowns to Scaling-Up Community-Based COVID-19 Screening, Testing, and Contact Tracing in Africa. Clin Infect Dis. 2020;ciaa695. doi:10.1093/cid/ciaa695

Ng Y, Li Z, Chua YX, et al. Evaluation of the Effectiveness of Surveillance and Containment Measures for the First 100 Patients with COVID-19 in Singapore. MMWR Morb Mortal Wkly Rep. 2020;69(11):307–311. doi:10.15585/mmwr.mm6911e1

Wilasang C, Sararat C, Jitsuk NC, et al. Reduction in effective reproduction number of COVID-19 is higher in countries employing active case detection with prompt isolation. J Travel Med. 2020;taaa095. doi:10.1093/jtm/taaa095

Wong SYS, Kwok KO, Chan FKL. What can countries learn from Hong Kong's response to the COVID-19 pandemic? CMAJ. 2020;192(19):E511–E515. doi:10.1503/cmaj.200563
