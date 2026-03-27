# Can LLMs assess risk of bias in medical research? A pilot study protocol
Juneau CE*, Siegel N
*Corresponding author: carl-etienne.juneau@umontreal.ca

# Research questions

1. **Prompt quality:** How does RoB agreement change as prompt support increases from a minimal instruction (A), to reviewer documentation (B), to documentation plus worked examples (C)?

Both models (weak and strong) run all conditions, yielding a secondary comparison of model capability across prompt conditions. In a pre-specified secondary analysis, Condition C is repeated with cumulative sets of 1 through 10 worked examples to examine how agreement scales with shot count.

## Future work (scalable oversight)

- Does a strong model's RoB agreement improve when it first receives the weak model's assessments?
- Do strong models benefit more from weak labels with rationales than labels alone?
- Sources of worked examples: Mulder et al. 2019 (different domain, lower contamination) vs. a COVID-19 Cochrane review (closer domain, higher contamination risk)
- **Pending: Weak baseline design? (Pavel Izmailov):** Should we use a single human investigator as the weak baseline instead of a weak LLM? Izmailov: "I think it would be even more interesting if you could generate more realistic weak labels, as in not use weak models, but instead use some biased human signal as labels. To clarify, in weak-to-strong generalization we are interested in whether strong models can generalize biased and imperfect signal coming from supervisors (humans). We don't know if using weak models is a meaningful model of the type of errors and biases that would be coming from humans. If you have more realistic weak labels, that would be better."

---

# Abstract

Risk-of-bias assessment is central to systematic review but time-intensive. We test whether two LLMs of different capability levels can reproduce expert risk-of-bias judgments for 14 observational studies using a published 8-criterion rubric. Each model runs under three prompting conditions: minimal instruction (A), full reviewer rubric (B), and rubric plus worked examples (C). Agreement with expert gold labels is compared across conditions using Cohen's kappa, percent agreement, and F1. A secondary analysis varies the number of worked examples from 1 to 10. This protocol was registered before any model was run on the test set.

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

This rule must appear verbatim in Conditions B and C.

### Overall RoB derivation rule

Overall RoB is derived in Python from the 8 criterion values. The model does not choose the overall label.

```
all yes              → low
any unclear, no no   → moderate
any no               → serious
```

## Prompt conditions

### Common elements across conditions

All prompt conditions use the same normalized full-text input, the same model settings, the same JSON output schema, and the same scoring procedure. In all conditions, the model is instructed to base judgments only on the provided study text and not on outside knowledge or assumptions. The model returns criterion-level judgments only; the final overall risk-of-bias label is derived in Python from the criterion-level outputs.

### Condition A: minimal instruction

The model receives the study text, the task instruction, the names of the 8 risk-of-bias criteria, the allowed outputs (yes, no, unclear), and the JSON output schema. It does not receive detailed criterion definitions, the explicit missingness rule, or worked examples.

### Condition B: rubric-guided instruction

In addition to the materials provided in Condition A, the model receives the operational reviewer rubric used in this study, including the 8 criterion definitions and the missingness rule used to distinguish yes, no, and unclear. The model is instructed to judge each criterion independently.

### Condition C: rubric-guided instruction with worked examples

In addition to the materials provided in Condition B, the model receives a fixed set of external worked examples showing how the rubric was applied and how the structured output should be produced. Each worked example includes both the input study text and the expected structured output. Examples were drawn from Mulder et al. (2019) and selected to maximize diversity in overall derived RoB (low, moderate, serious) and in the spread of yes, no, and unclear judgments across the 8 criteria. In a secondary analysis, Condition C is repeated with pre-specified cumulative sets of 1 through 10 worked examples.

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
4. Source external worked examples for condition C (input text + expected structured output pairs)
5. Write `schema.py` and `score_results.py`; test on mocked data
6. Write `run_models.py` (loops over models x conditions, assembles prompts from protocol definitions)
7. Smoke test on one outside observational study
8. Run all 14 studies x all conditions x weak model; save raw outputs
9. Run all 14 studies x all conditions x strong model; save raw outputs
10. Score all; compare agreement across conditions and models
11. Write memo

## Transparency and reproducibility

Each result row will record: study ID, model name, prompt condition (A/B/C), shot count (for the secondary analysis), run timestamp, raw output file reference, 8 parsed criterion values, derived overall RoB, gold overall RoB, correct/incorrect.

Prompt templates are frozen before any real-study run. Each condition is versioned (e.g., `condition_a_v1`).

# Discussion

Prior work on automated risk-of-bias assessment is limited. In an AHRQ rapid review and evidence map, Adam et al. (2024) found only seven comparative studies of automation tools for risk-of-bias assessment, with weighted kappa values ranging from 0.11 to 0.48, suggesting only modest agreement overall. Much of the pre-LLM literature focused on RobotReviewer. Marshall et al. (2016) trained RobotReviewer on 12,808 trial PDFs and reported 71.0% overall accuracy, compared with 78.3% for published review labels. Gates et al. (2018) found moderate reliability for random sequence generation, allocation concealment, and blinding of participants or personnel, but only fair agreement for overall risk of bias and slight agreement in several other domains. Hirt et al. (2021) reported a similar pattern in nursing-related Cochrane reviews, with moderate agreement for randomization and allocation concealment but only slight agreement for blinding of outcome assessors. Tian et al. (2024) later confirmed substantial domain-to-domain variation in a comparison spanning 1,955 randomized trials, with kappa values ranging from 0.25 to 0.59. Importantly, Arno et al. (2022) found that RobotReviewer-assisted reviewers were noninferior to unaided reviewers in overall risk-of-bias accuracy, suggesting that assisted assessment may be a more realistic near-term role than full automation.

Results in the LLM era have also been mixed and appear sensitive to protocol design. Šuster et al. (2024) tested zero- and few-shot prompting for RoB 2 and found that four LLMs seldom beat trivial baselines, with F1 scores of 0.1 to 0.2 for direct prediction. In contrast, Lai et al. (2024) used a structured prompt and a three-expert criterion standard for 30 randomized trials and reported mean correct assessment rates of 84.5% and 89.5% for two LLMs, although performance was weaker in some domains. Hasan et al. (2024) applied GPT-4 to ROBINS-I for non-randomized studies and found 61% raw agreement for overall risk of bias, with only moderate agreement in selected domains. Huang et al. (2025) likewise reported that structured prompting could yield 65% to 70% overall accuracy relative to reviewer or Cochrane judgments, and that deriving judgments from signaling-question answers improved performance. Taken together, these studies suggest that LLM performance is not fixed; it depends in part on how the task is framed, how much methodological guidance is provided, and whether the assessment is decomposed into signaling questions rather than treated as a single overall classification.

More recent studies continue to suggest useful but incomplete performance. Kuitunen et al. (2025) found overall kappa of 0.43 in neonatal trials and concluded that ChatGPT-4o did not achieve sufficient agreement for routine use. Rose et al. (2025), using methods text from 75 randomized trials and a prompt developed on 25 review-trial pairs, reported 50.7% human-ChatGPT agreement for overall risk of bias, although agreement for the randomization process was higher at 78.7%. Taneri (2025) found moderate overall agreement between ChatGPT-4o and Cochrane RoB 2 judgments, with weighted kappa of 0.51, but sensitivity for identifying high-risk studies was only 53%, despite specificity of 99% for low-risk studies. Outside randomized trials, Leucuța et al. (2025) evaluated four LLMs on QUADAS-2 and found a mean signaling-question accuracy of 72.95%, again concluding that expert oversight remained necessary. Overall, the literature does not support fully autonomous risk-of-bias assessment, but it does support a narrower conclusion: current systems may be able to assist reviewers, and their measured performance appears to depend strongly on the prompting and assessment protocol. That is the gap our study is designed to address.

# References

Adam GP, Davies M, George J, et al. Machine Learning Tools To (Semi-)Automate Evidence Synthesis: A Rapid Review and Evidence Map [Internet]. Rockville, MD: Agency for Healthcare Research and Quality (US); 2024. PMID: 40424432.

Arno A, Thomas J, Wallace B, Marshall IJ, McKenzie JE, Elliott JH. Accuracy and Efficiency of Machine Learning-Assisted Risk-of-Bias Assessments in "Real-World" Systematic Reviews: A Noninferiority Randomized Controlled Trial. Ann Intern Med. 2022;175(7):1001–1009. doi:10.7326/M22-0092

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

Gates A, Vandermeer B, Hartling L. Technology-assisted risk of bias assessment in systematic reviews: a prospective cross-sectional evaluation of the RobotReviewer machine learning tool. J Clin Epidemiol. 2018;96:54–62. doi:10.1016/j.jclinepi.2017.12.015

Hasan B, Saadi S, Rajjoub NS, et al. Integrating large language models in systematic reviews: a framework and case study using ROBINS-I for risk of bias assessment. BMJ Evid Based Med. 2024;29(6):394–398. doi:10.1136/bmjebm-2023-112597

Higgins JPT, Thomas J, Chandler J, et al. (eds). Cochrane Handbook for Systematic Reviews of Interventions version 6.5. Cochrane, 2024. www.cochrane.org/authors/handbooks-and-manuals/handbook/current

Hirt J, Meichlinger J, Schumacher P, et al. Agreement in Risk of Bias Assessment Between RobotReviewer and Human Reviewers: An Evaluation Study on Randomised Controlled Trials in Nursing-Related Cochrane Reviews. J Nurs Scholarsh. 2021;53(2):246–254. doi:10.1111/jnu.12628

Huang J, Pan B, Liu J, et al. Large Language Model–Assisted Risk-of-Bias Assessment in Randomized Controlled Trials Using the Revised Risk-of-Bias Tool: Evaluation Study. J Med Internet Res. 2025;27:e70450. doi:10.2196/70450

Juneau CE, Briand AS, Collazzo P, Siebert U, Pueyo T. Effective contact tracing for COVID-19: A systematic review. Glob Epidemiol. 2023;5:100103. doi:10.1016/j.gloepi.2023.100103

Kuitunen I, Nyrhi L, De Luca D. ChatGPT-4o in Risk-of-Bias Assessments in Neonatology: A Validity Analysis. Neonatology. 2025;1–6. doi:10.1159/000544857

Lai H, Ge L, Sun M, et al. Assessing the Risk of Bias in Randomized Clinical Trials With Large Language Models. JAMA Netw Open. 2024;7(5):e2412687. doi:10.1001/jamanetworkopen.2024.12687

Lam HY, Lam TS, Wong CH, et al. The epidemiology of COVID-19 cases and the successful containment strategy in Hong Kong-January to May 2020. Int J Infect Dis. 2020;98:51–58. doi:10.1016/j.ijid.2020.06.057

Leucuța D-C, Urda-Cîmpean AE, Istrate D, Drugan T. Risk of Bias Assessment of Diagnostic Accuracy Studies Using QUADAS 2 by Large Language Models. Diagnostics. 2025;15(12):1451. doi:10.3390/diagnostics15121451

Lieberum J-L, Toews M, Metzendorf M-I, et al. Large language models for conducting systematic reviews: on the rise, but not yet ready for use: a scoping review. J Clin Epidemiol. 2025;181:111746. doi:10.1016/j.jclinepi.2025.111746

Marshall IJ, Kuiper J, Wallace BC. RobotReviewer: evaluation of a system for automatically assessing bias in clinical trials. J Am Med Inform Assoc. 2016;23(1):193–201. doi:10.1093/jamia/ocv044

Mulder RL, Bresters D, Van den Hof M, et al. Hepatic late adverse effects after antineoplastic treatment for childhood cancer. Cochrane Database Syst Rev. 2019;4:CD008205. doi:10.1002/14651858.CD008205.pub3

Nachega JB, Grimwood A, Mahomed H, et al. From Easing Lockdowns to Scaling-Up Community-Based COVID-19 Screening, Testing, and Contact Tracing in Africa. Clin Infect Dis. 2020;ciaa695. doi:10.1093/cid/ciaa695

Ng Y, Li Z, Chua YX, et al. Evaluation of the Effectiveness of Surveillance and Containment Measures for the First 100 Patients with COVID-19 in Singapore. MMWR Morb Mortal Wkly Rep. 2020;69(11):307–311. doi:10.15585/mmwr.mm6911e1

Rose CJ, Bidonde J, Ringsten M, et al. Using a Large Language Model (ChatGPT-4o) to Assess the Risk of Bias in Randomized Controlled Trials of Medical Interventions: Interrater Agreement With Human Reviewers. Cochrane Evid Synth Methods. 2025;3(5):e70048. doi:10.1002/cesm.70048

Šuster S, Baldwin T, Verspoor K. Zero- and few-shot prompting of generative large language models provides weak assessment of risk of bias in clinical trials. Res Synth Methods. 2024;15(6):988–1000. doi:10.1002/jrsm.1749

Taneri PE, Engel C, Engel H, et al. Human Versus Artificial Intelligence: Comparing Cochrane Authors' and ChatGPT's Risk of Bias Assessments. Cochrane Evid Synth Methods. 2025;3(7):e70044. doi:10.1002/cesm.70044

Tian Y, Yang X, Doi SAR, et al. Towards the automatic risk of bias assessment on randomized controlled trials: A comparison of RobotReviewer and humans. Res Synth Methods. 2024;15(6):1111–1119. doi:10.1002/jrsm.1761

Wilasang C, Sararat C, Jitsuk NC, et al. Reduction in effective reproduction number of COVID-19 is higher in countries employing active case detection with prompt isolation. J Travel Med. 2020;taaa095. doi:10.1093/jtm/taaa095

Wong SYS, Kwok KO, Chan FKL. What can countries learn from Hong Kong's response to the COVID-19 pandemic? CMAJ. 2020;192(19):E511–E515. doi:10.1503/cmaj.200563
