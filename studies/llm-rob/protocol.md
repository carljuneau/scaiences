# Can LLMs assess risk of bias in medical research? A pilot study protocol
Juneau CE*, Siegel N
*Corresponding author: carl-etienne.juneau@umontreal.ca

# Research questions

1. **Prompt quality:** How does RoB agreement change as prompt support increases from a minimal instruction, to reviewer documentation, to documentation plus worked examples?
2. **Shot count:** How does agreement scale with the number of in-context worked examples (0, 1, 2, 3, 4, ...)?

Both questions are tested on two models (weak and strong), yielding a secondary comparison of model capability across prompt conditions.

## Future work (scalable oversight)

- Does a strong model's RoB agreement improve when it first receives the weak model's assessments?
- Do strong models benefit more from weak labels with rationales than labels alone?
- Sources of worked examples: Mulder et al. 2019 (different domain, lower contamination) vs. a COVID-19 Cochrane review (closer domain, higher contamination risk)

---

# Introduction

In medical research, we assess risk of bias to judge how much confidence to place in a study's findings. We do this because flaws in study design, conduct, analysis, and reporting can systematically overestimate or underestimate effects (Higgins et al., 2024). To make these judgments, reviewers use structured tools that cover domains such as participant selection, outcome measurement, missing data, and confounding.

This work is important, but it is also time-intensive and can be difficult to do efficiently across large reviews. Large language models (LLMs) could help reduce this burden. Recent reviews suggest that LLMs are being tested across many parts of evidence synthesis, especially search, screening, and data extraction, but validated applications remain limited and fully autonomous use is not yet supported (Lieberum et al., 2025). Risk-of-bias assessment is a particularly open question. Early studies have reported mixed results, with performance varying by tool, domain, and study type, and related appraisal work suggests that more explicit instructions may improve agreement (Hasan et al., 2024).

In this pilot study, we evaluate how well two LLMs, a weaker model and a stronger model, reproduce expert risk-of-bias labels from our prior review (Juneau et al., 2023). We also examine whether agreement improves as the prompting protocol becomes more explicit, moving from a basic instruction to reviewer documentation and worked examples. Rather than asking whether LLMs can replace expert reviewers, we ask how much performance depends on the evaluation protocol itself. We hypothesize that the stronger model will outperform the weaker model, and that agreement with expert labels will improve as prompts become more explicit. Current guidance supports studying AI in this assistive role, with human oversight and transparent reporting (Flemyng et al., 2025).

# Methods

This pilot uses risk-of-bias assessments of 14 observational studies from our systematic review of Covid-19 contact tracing as a test set (Juneau et al., 2023). Two LLMs of different capability levels assess each study under several prompting conditions of increasing explicitness, using a published 8-criterion rubric (Mulder et al., 2019). Agreement with expert gold labels is compared across prompt conditions and models.

## Study sample
- 14 observational studies, single-arm intervention design
- Study list, 8 expert criterion labels, and overall RoB: [Table - RoB_observational_studies.csv](data/public/Table%20-%20RoB_observational_studies.csv)
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

## Prompt conditions

Each model is run under the following conditions, in order of increasing prompt support. All conditions share the Output schema defined below. Worked examples for condition C are drawn from external RoB assessments (not from the 14 test studies) to preserve the evaluation set. The number of examples increases until agreement plateaus or context-length limits are reached.

### Condition A: Minimal

> Assess risk of bias inthe following observational study. Rate overall risk of bias as:
> - **Low**
> - **Moderate**
> - **Serious**
>
> [Output schema]
>
> Study ID: {{STUDY_ID}}
>
> {{FULL_TEXT}}

### Condition B: A + documentation

> [Condition A, with the following additions:]
>
> **Role.** You are a systematic review methodologist.
>
> **Background.** Risk of bias was assessed using methods similar to a Cochrane review on a related topic. For observational studies, a Cochrane tool was used (Mulder et al., 2019). This tool assesses internal and external validity across eight criteria.
>
> **Criteria.** For each of the 8 criteria below, answer "yes", "no", or "unclear":
> 1. The described study group consisted of >90% of eligible individuals
> 2. The intervention and number of participants was defined
> 3. The outcome was assessed for at least 60% of the study group of interest
> 4. The length of follow-up was mentioned
> 5. The outcome assessors were blinded to the investigated determinant
> 6. The outcome definition was objective and precise
> 7. Important prognostic factors (i.e. age, gender) or follow-up were taken adequately into account
> 8. The method of analysis was described and the effect of the intervention was quantified
>>
> **Scoring rules.**
> - Use `yes` only when the full text explicitly supports the criterion being met.
> - Use `no` only when the full text gives positive evidence the criterion was not met.
> - Use `unclear` when the full text does not provide enough information to judge.

> **Overall rating:**
> Derive an overall risk-of-bias rating:
> - **Low:** all criteria are "yes"
> - **Moderate:** at least one "unclear", no "no"
> - **Serious:** at least one "no"

### Condition C(n): B + worked examples

> [Condition B, with the following addition:]
>
> **Worked examples.** The following are completed risk-of-bias assessments for other studies using this same rubric. Use them as a guide for how to apply the criteria.
>
> {{WORKED_EXAMPLES}}

## Models

| Role | Model ID |
|------|----------|
| Weak | `claude-haiku-4-5-20251001` |
| Strong | `claude-opus-4-6` |

Both models run all prompt conditions. Temperature: 0. Max tokens: 1024.

## Run policy

- One call per study, per model, per prompt condition.
- If the output is invalid JSON or missing any of the 8 criterion fields: retry once with the identical prompt.
- If the second call also fails: record a parse failure for that study; do not impute or manually fix.
- All prompts are frozen before any real-study run. The off-sample smoke test (one study outside the 14) may be used to verify that the pipeline runs end to end, but must not cause any prompt revision.
- No tuning. All 14 studies are scored once per condition and treated as the final test set.

## Inputs

| File | Location | Contents | Privacy |
|------|----------|----------|---------|
| `Table - RoB_observational_studies.csv` | `data/public/` | study ID, year, DOI, 8 expert criterion labels, overall RoB | Public |
| `Table 2 - RoB_criteria.csv` | `data/public/` | rubric criteria definitions | Public |
| `observational/` | `data/private/` | full-text PDFs, one per study | Gitignored |

Gold labels (8 criteria + overall RoB) are in the public CSV. The private directory is listed in `.gitignore`.

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

**Primary outcome:** agreement on overall RoB label (low / moderate / serious) between derived model label and expert gold label, compared across prompt conditions and models.

**Secondary outcome:** criterion-level agreement (8 individual yes/no/unclear judgments vs. expert labels), compared across prompt conditions and models.

**Agreement metrics** (chosen for comparability with prior work; Hasan et al., 2024; Taneri et al., 2025):
- Cohen's kappa (weighted for overall RoB; unweighted per criterion)
- Percent agreement with 95% confidence intervals
- Sensitivity and specificity
- F1 score per criterion
- Accuracy (proportion correct)
- Confusion matrix (3x3 for overall; 3x3 per criterion)
- Majority-class baseline (all 14 studies have "serious" overall RoB)

With n = 14, confidence intervals will be wide. Results are reported descriptively.

## File layout

```
studies/llm-rob/
  data/
    public/
      Table - RoB_observational_studies.csv
      Table 2 - RoB_criteria.csv
    private/              ← gitignored
      observational/      ← full-text PDFs
  prompts/
    examples/             ← external worked examples for condition C
  src/
    schema.py             ← output schema and validation
    run_models.py         ← prompt building, model calls, raw output saving
    score_results.py      ← parsing, RoB derivation, scoring, reporting
  results/                ← raw outputs, parsed results, scored summaries
```

## Build order

1. Prepare `Table - RoB_observational_studies.csv` (public) ✓
2. Collect full-text PDFs (private) ✓
3. Define prompt conditions in protocol (above) ✓
4. Source external worked examples for condition C
5. Write `schema.py` and `score_results.py`; test on mocked data
6. Write `run_models.py` (loops over models x conditions, assembles prompts from protocol definitions)
7. Smoke test on one outside observational study
8. Run all 14 studies x all conditions x weak model; save raw outputs
9. Run all 14 studies x all conditions x strong model; save raw outputs
10. Score all; compare agreement across conditions and models
11. Write memo

# Transparency and reproducibility

Each result row will record: study ID, model name, prompt condition (A/B/C(n)), run timestamp, raw output file reference, 8 parsed criterion values, derived overall RoB, gold overall RoB, correct/incorrect.

Prompt templates are frozen before any real-study run. Each condition is versioned (e.g., `condition_a_v1`).

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

Flemyng E, Noel-Storr A, Macura B, et al. Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025. Campbell Syst Rev. 2025;21(4):e70074. doi:10.1002/cl2.70074

Hasan B, Saadi S, Rajjoub NS, et al. Integrating large language models in systematic reviews: a framework and case study using ROBINS-I for risk of bias assessment. BMJ Evid Based Med. 2024;29(6):394–398. doi:10.1136/bmjebm-2023-112597

Higgins JPT, Thomas J, Chandler J, et al. (eds). Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane, 2024. www.cochrane.org/authors/handbooks-and-manuals/handbook/current

Juneau CE, Briand AS, Collazzo P, Siebert U, Pueyo T. Effective contact tracing for COVID-19: A systematic review. Glob Epidemiol. 2023;5:100103. doi:10.1016/j.gloepi.2023.100103

Lam HY, Lam TS, Wong CH, et al. The epidemiology of COVID-19 cases and the successful containment strategy in Hong Kong-January to May 2020. Int J Infect Dis. 2020;98:51–58. doi:10.1016/j.ijid.2020.06.057

Lieberum J-L, Toews M, Metzendorf M-I, et al. Large language models for conducting systematic reviews: on the rise, but not yet ready for use: a scoping review. J Clin Epidemiol. 2025;181:111746. doi:10.1016/j.jclinepi.2025.111746

Mulder RL, Bresters D, Van den Hof M, et al. Hepatic late adverse effects after antineoplastic treatment for childhood cancer. Cochrane Database Syst Rev. 2019;4:CD008205. doi:10.1002/14651858.CD008205.pub3

Nachega JB, Grimwood A, Mahomed H, et al. From Easing Lockdowns to Scaling-Up Community-Based COVID-19 Screening, Testing, and Contact Tracing in Africa. Clin Infect Dis. 2020;ciaa695. doi:10.1093/cid/ciaa695

Ng Y, Li Z, Chua YX, et al. Evaluation of the Effectiveness of Surveillance and Containment Measures for the First 100 Patients with COVID-19 in Singapore. MMWR Morb Mortal Wkly Rep. 2020;69(11):307–311. doi:10.15585/mmwr.mm6911e1

Taneri PE, Engel C, Engel H, et al. Human Versus Artificial Intelligence: Comparing Cochrane Authors' and ChatGPT's Risk of Bias Assessments. Cochrane Evid Synth Methods. 2025;3(7):e70044. doi:10.1002/cesm.70044

Wilasang C, Sararat C, Jitsuk NC, et al. Reduction in effective reproduction number of COVID-19 is higher in countries employing active case detection with prompt isolation. J Travel Med. 2020;taaa095. doi:10.1093/jtm/taaa095

Wong SYS, Kwok KO, Chan FKL. What can countries learn from Hong Kong's response to the COVID-19 pandemic? CMAJ. 2020;192(19):E511–E515. doi:10.1503/cmaj.200563
