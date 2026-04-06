# Can LLMs assess risk of bias in medical research? A pilot study protocol
Juneau CE*, Siegel NY
*Corresponding author: carl-etienne.juneau@umontreal.ca

# Abstract

Risk-of-bias assessment is central to reviews of medical research, but time-intensive. In this pilot study, we ask how well two LLMs, a weaker model and a stronger model, natively reproduce expert risk-of-bias judgments. We also examine whether agreement improves with guidance, as prompts cumulatively add criteria definitions, training material, and a worked example. Agreement with expert labels is compared across conditions using mean paired differences in criterion-level agreement.

# Introduction

In medical research, we assess risk of bias (RoB) to judge how much confidence to place in a study's findings. We do this because flaws in study design, conduct, analysis, and reporting can systematically overestimate or underestimate effects (Higgins et al., 2024). To make these judgments, reviewers use structured tools that cover domains such as participant selection, outcome measurement, missing data, and confounding.

This work is important, but it is also time-intensive. Large language models (LLMs) could help reduce this burden. Recent reviews suggest that LLMs are being tested across many parts of evidence synthesis, especially search, screening, and data extraction, but validated applications remain limited and fully autonomous use is not yet supported (Lieberum et al., 2025). Risk-of-bias assessment is a particularly open question. Early studies have reported mixed results, with performance varying by tool, domain, and study type. Related appraisal work suggests that more explicit instructions may improve agreement (Hasan et al., 2024).

Indeed, prior work on automated risk-of-bias assessment is limited. In arapid review, Adam et al. (2024) found seven comparative studies of automation tools for risk-of-bias assessment, with weighted kappa values ranging from 0.11 to 0.48, suggesting modest agreement overall. Much of the pre-LLM literature focused on RobotReviewer. Marshall et al. (2016) trained RobotReviewer on 12,808 trial PDFs and reported 71.0% overall accuracy, compared with 78.3% for published review labels. Gates et al. (2018) found moderate reliability for random sequence generation, allocation concealment, and blinding of participants or personnel, but only fair agreement for overall risk of bias and slight agreement in several other domains. Hirt et al. (2021) reported a similar pattern in nursing-related Cochrane reviews, with moderate agreement for randomization and allocation concealment but only slight agreement for blinding of outcome assessors. Tian et al. (2024) later confirmed substantial domain-to-domain variation in a comparison spanning 1,955 randomized trials, with kappa values ranging from 0.25 to 0.59. Importantly, Arno et al. (2022) found that RobotReviewer-assisted reviewers were noninferior to unaided reviewers in overall risk-of-bias accuracy, suggesting that assisted assessment may be a more realistic near-term role than full automation.

Results in the LLM era have also been mixed and appear sensitive to protocol design. Šuster et al. (2024) tested zero- and few-shot prompting and found that four LLMs seldom beat trivial baselines, with F1 scores of 0.1 to 0.2 for direct prediction. In contrast, Lai et al. (2024) used a structured prompt and a three-expert criterion standard for 30 randomized trials and reported mean correct assessment rates of 84.5% and 89.5% for two LLMs. Hasan et al. (2024) applied GPT-4 to ROBINS-I for non-randomized studies and found 61% raw agreement for overall risk of bias, with only moderate agreement in selected domains. Huang et al. (2025) likewise reported that structured prompting could yield 65% to 70% overall accuracy relative to reviewer or Cochrane judgments, and that deriving judgments from signaling-question answers improved performance. Taken together, these studies suggest that LLM performance is not fixed; it depends on how the task is framed, how much methodological guidance is provided, and more.

More recent studies continue to suggest useful but incomplete performance. Kuitunen et al. (2025) found overall kappa of 0.43 in neonatal trials and concluded that ChatGPT-4o did not achieve sufficient agreement for routine use. Rose et al. (2025), using methods text from 75 randomized trials and a prompt developed on 25 review-trial pairs, reported 50.7% human-ChatGPT agreement for overall risk of bias, although agreement for the randomization process was higher at 78.7%. Taneri (2025) found moderate overall agreement between ChatGPT-4o and Cochrane RoB 2 judgments, with weighted kappa of 0.51, but sensitivity for identifying high-risk studies was only 53%, despite specificity of 99% for low-risk studies. Outside randomized trials, Leucuța et al. (2025) evaluated four LLMs on QUADAS-2 and found a mean signaling-question accuracy of 72.95%, again concluding that expert oversight remained necessary. Overall, the literature does not support fully autonomous risk-of-bias assessment, but it does support a narrower conclusion: current systems may be able to assist reviewers, and their measured performance appears to depend strongly on the prompting and assessment protocol. That is the gap our study is designed to examine.

In this pilot study, we first ask how well two LLMs, a weaker model and a stronger model, natively reproduce expert risk-of-bias labels from our prior review (Juneau et al., 2023). We then examine whether agreement improves with guidance, as prompts cumulatively add criteria definitions, training material, and a worked example. Rather than asking whether LLMs can replace expert reviewers, we ask how much performance depends on the evaluation protocol itself. Current guidance supports studying AI in this assistive role, with human oversight and transparent reporting (Flemyng et al., 2025).

# Methods

This pilot uses risk-of-bias assessments of 14 observational studies from our systematic review of COVID-19 contact tracing as a test set (Juneau et al., 2023). Two LLMs of different capability levels assess each study under four cumulative prompting conditions, using the 8-criterion observational risk-of-bias rubric reported in Juneau et al. (2023). Agreement with expert gold labels is compared across prompt conditions and models. Reporting follows the TRIPOD-LLM guideline for studies using large language models (Collins et al., 2025).

## Sample

The 14 observational studies (single-arm intervention design), 8 expert criterion labels, and overall RoB can be found in [Table - RoB_observational_studies.csv](data/public/Table%20-%20RoB_observational_studies.csv). 


## Research questions

1. Baseline agreement: How well do weak and strong LLMs reproduce expert RoB judgments natively?

2. In-context learning: How much does agreement improve with additional guidance, as prompts add criteria definitions, training material, and a worked example?

## Rubric

>
**Rubric provenance.** For observational studies, this pilot evaluates the 8-criterion rubric as reported in Juneau et al. (2023). That rubric was adapted from Mulder et al. (2019), a Cochrane review in which they were initially developped for childhood cancer. In Juneau et al. (2023), some criteria were generalized so the rubric could be applied to observational studies more broadly, including studies of COVID-19 contact tracing. For example, Mulder defined a "well-defined outcome" in liver-specific terms (whether upper limits of normal for liver function tests were described). We used the broader criterion that the outcome definition was "objective and precise". Appendix A maps each Juneau criterion to its Mulder antecedent and summarizes all wording changes.

### Criteria

See [Table 2 - RoB_criteria.csv](data/public/Table%202%20-%20RoB_criteria.csv). Allowed outputs per criterion: `yes` | `no` | `unclear`.

### Missingness rule

- Use `yes` only when the full text explicitly supports the criterion being met.
- Use `no` only when the full text gives positive evidence the criterion was not met.
- Use `unclear` when the full text does not provide enough information to judge.

### Overall RoB derivation rule

```
all yes              → low
any unclear, no no   → moderate
any no               → serious
```

This rule is given to the model in Conditions B, C, and D (not in A). Python also applies this rule independently to the criterion-level outputs in Conditions B, C, and D to produce a derived overall label for comparison.

## Prompt conditions

### Common elements across conditions

All prompt conditions use the same full-text of the original study (PDF), the same model settings, and the same scoring procedure. In all conditions, the model is instructed to base judgments only on the provided study text and not on outside knowledge or assumptions. All conditions ask the model to report an overall risk-of-bias label (low, moderate, or serious). Conditions B, C, and D additionally return per-criterion judgments with supporting quotes; in those conditions, Python independently derives an overall label from the criterion-level outputs for comparison with the model-reported overall.

### Condition A: baseline agreement

The model receives the study text and a minimal task instruction: "Assess risk of bias in the following study as low, moderate, or serious." No other instructions. This tests whether the model can reproduce expert judgments natively, without additional guidance.

### Condition B: criteria definitions

In addition to the instructions provided in Condition A, the model receives the 8 criterion definitions, the allowed outputs per criterion (yes, no, unclear), the missingness rule, the overall RoB derivation rule, and the JSON output schema. It does not receive training material or worked examples.

### Condition C: training material

In addition to the instructions provided in Condition B, the model receives the full text of Mulder et al. (2019) as training material. This review developped the RoB tool adapted in Juneau et al. (2023).

### Condition D: worked example

In addition to the instructions provided in Condition C, the model receives one external worked example showing how the rubric was applied and how the structured output should be produced. The worked example includes both the input study text and the expected structured output. The example was drawn from Green et al. (2019), one of the studies assessed in Mulder et al. (2019). Green et al. (2019) is open-access and has a mix of output values represented across the 8 criteria.

Although criterion-level labels for Green et al. (2019) already appear in Mulder et al. (2019) (given in C), Condition D provides additional guidance by pairing the full study text with the expected JSON output. This gives the model an explicit worked example of how the rubric is operationalized study by study.

Exact prompts are shown in the Supplements (`condition_a.txt`, `condition_b.txt`, `condition_c.txt`, `condition_d.txt`).

## Models

The weak model is Google Gemini 3 Flash (`gemini-3-flash`). The strong model is Google Gemini 3.1 Pro at High thinking level (`gemini-3.1-pro-preview`, `thinking_level: high`). Both models run all prompt conditions. Temperature is fixed at 0 and max tokens at 1024. Temperature 0 was chosen to reflect an intended real-world deployment setting in which reviewers seek stable, low-randomness outputs for structured review tasks. Following Miller (2024), a fuller evaluation would estimate expected performance under a decoding policy through repeated sampling or, where feasible, token-probability-based scoring. In this pilot, however, each study × model × prompt-condition combination yields one realized output under a fixed low-randomness setting.

Because each study × model × prompt-condition combination is sampled only once, the observed score reflects the realized output under the specified decoding policy rather than an estimate averaged over repeated samples.

## Run policy

- One call per study, per model, per prompt condition.
- If the output is invalid JSON or missing any of the 8 criterion fields: retry once with the identical prompt.
- If the second call also fails: record a parse failure for that study; do not impute or manually fix.
- All prompts are frozen before any real-study run. The off-sample smoke test (one study outside the 14) may be used to verify that the pipeline runs end to end, but must not cause any prompt revision.
- No tuning. All 14 studies are scored once per condition and treated as the final test set.

## Output schema

### Condition A

```json
{
  "study_id": "string",
  "overall_rob": "low|moderate|serious"
}
```

### Conditions B, C, and D

```json
{
  "study_id": "string",
  "criteria": {
    "study_group_representative": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "intervention_and_participants_defined": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "outcome_assessed_for_60pct": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "follow_up_length_reported": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "outcome_assessors_blinded": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "outcome_definition_objective_precise": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "important_prognostic_factors_accounted_for": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    },
    "analysis_described_and_effect_quantified": {
      "judgment": "yes|no|unclear",
      "quote": "string"
    }
  },
  "overall_rob": "low|moderate|serious"
}
```

Each `quote` field contains the verbatim text from the study that supports the judgment. Quotes are not scored but are recorded for transparency.

## Statistical analysis

The main analysis will focus on criterion-level agreement in Conditions B–D. For each study, model, and prompt condition, we will calculate the proportion of the 8 criterion judgments that match the expert labels. The primary endpoint will be the mean per-study criterion-level agreement across the 14 studies. Because each study contributes the same 8 criteria, this summary is equivalent to overall criterion-level exact agreement while treating the study, rather than the individual criterion judgment, as the unit of analysis.

To compare models and prompt conditions, we will follow Miller (2024) by using paired differences on the same items: for each prespecified contrast, we will compute the per-study difference in criterion-level agreement and report the mean paired difference with a 95% confidence interval. For comparability with prior risk-of-bias studies, unweighted Cohen’s kappa will be reported as a secondary descriptive measure at the criterion level. Confusion matrices by criterion and a majority-class baseline will also be reported.

Overall-label analyses will be secondary and descriptive. For each condition, we will report percent agreement between the model-reported overall risk-of-bias label and the expert overall label, together with weighted Cohen’s kappa for the ordinal overall categories (low, moderate, serious). For Conditions B–D, we will also compare the Python-derived overall label with the expert overall label.

Because all 14 expert overall labels in this pilot are serious, overall-label metrics may be inflated by class imbalance and will not be treated as the primary endpoint. Condition A returns only an overall label and will therefore be treated as a descriptive baseline rather than included in the primary criterion-level comparison.

The main prompt comparisons of interest are C vs B and D vs C within each model. Secondary exploratory analyses will compare the weak and strong models within each prompt condition using the same paired-difference framework. Because each study × model × prompt-condition combination is sampled only once, the reported scores reflect realized performance under the specified decoding policy, not expected performance under repeated sampling. Accordingly, the reported confidence intervals capture variation across studies in this benchmark, but not within-prompt sampling variability from repeated model calls. Following Miller (2024), repeated sampling would provide a better estimate of expected performance under the same decoding policy, but that was outside the scope of this pilot. Sensitivity, specificity, and F1 will not be used as main outcomes in this pilot, because the small sample and the single-class overall outcome make them difficult to interpret. No multiplicity adjustment is planned; this is a pilot study, and secondary analyses will be treated as exploratory.

## Scope and limitations

### Limitations

This pilot study has several limitations. First, each study × model × prompt-condition combination was sampled only once, at temperature 0. This reflects a plausible real-world deployment setting for structured review assistance, where users often seek stable low-randomness outputs, but it does not estimate expected performance under repeated sampling. As Miller (2024) notes, a fuller evaluation would resample outputs under fixed settings or use token-probability-based scoring where feasible. Accordingly, our confidence intervals reflect variation across studies in this benchmark, but not residual sampling variability within the same prompt and model configuration. Future work should assess whether the present findings are robust to repeated sampling under the same decoding policy.

Second, overall-label analyses are constrained by the fact that all 14 expert overall labels in this pilot are serious, which limits the interpretability of overall-label agreement measures. For that reason, the primary endpoint in this study focuses on criterion-level agreement in Conditions B–D rather than on overall-label agreement alone.

Third, our sample size was limited to 14 studies, which constrains both the precision of the estimates and the generalizability of the findings to study designs other than single-arm observational studies.

### Future directions

#### Scalable oversight
- Does a strong model's RoB agreement improve when it first receives the weak model's assessments?
- Do strong models benefit more from weak labels with rationales than labels alone?
- Consider additional worked examples for the observational rubric: studies from Mulder et al. (2019), which reflect the earlier childhood-cancer version from which the Juneau rubric was adapted and may reduce topical contamination, versus examples from a closer COVID-19 review, which may offer a closer application domain but a higher risk of task contamination.

#### Weak baseline design

Should we use a single human investigator as the weak baseline instead of a weak LLM? Pavel Izmailov (personal communication, 2026) has suggested that using weak models may not be a meaningful model of the errors and biases that would come from humans, and that more realistic (human) weak labels would be better. More realistic weak labels could be generated from a single human investigator (instead of two) working with or without access to the training material or with limited time per study.

### Ethical approval

This study is a secondary analysis of published, publicly available data. No new data were collected from human participants. No patients or members of the public were involved in the design, conduct, or reporting of this study. No ethical approval was required.

### Conflict of interest

Carl-Etienne Juneau is founder of Dr. Muscle AI, which provided financial support for this research (https://dr-muscle.com). Noah Y. Siegel is Senior Research Engineer at Google DeepMind.

### Generative AI disclosure

Large language models (Claude Sonnet, Google Gemini) were used to assist in drafting and editing this protocol. All substantive content, judgments, and interpretations were made by the authors. GenAI tools did not contribute to the study design, analytical decisions, or conclusions. No study data or participant information was entered into GenAI tools. The LLMs evaluated in this study are distinct from those used in manuscript preparation.

## References

Adam GP, Davies M, George J, et al. Machine Learning Tools To (Semi-)Automate Evidence Synthesis: A Rapid Review and Evidence Map [Internet]. Rockville, MD: Agency for Healthcare Research and Quality (US); 2024. PMID: 40424432.

Arno A, Thomas J, Wallace B, Marshall IJ, McKenzie JE, Elliott JH. Accuracy and Efficiency of Machine Learning-Assisted Risk-of-Bias Assessments in "Real-World" Systematic Reviews: A Noninferiority Randomized Controlled Trial. Ann Intern Med. 2022;175(7):1001–1009. doi:10.7326/M22-0092

Bernard Stoecklin S, Rolland P, Silue Y, et al. First cases of coronavirus disease 2019 (COVID-19) in France: surveillance, investigations and control measures, January 2020. Euro Surveill. 2020;25(6):2000094. doi:10.2807/1560-7917.ES.2020.25.6.2000094

Bi Q, Wu Y, Mei S, et al. Epidemiology and transmission of COVID-19 in 391 cases and 1286 of their close contacts in Shenzhen, China: a retrospective cohort study. Lancet Infect Dis. 2020;S1473-3099(20)30287-5. doi:10.1016/S1473-3099(20)30287-5

Burke RM, Midgley CM, Dratch A, et al. Active Monitoring of Persons Exposed to Patients with Confirmed COVID-19 — United States, January–February 2020. MMWR Morb Mortal Wkly Rep. 2020;69:245–246. doi:10.15585/mmwr.mm6909e1

Chen CM, Jyan HW, Chien SC, et al. Containing COVID-19 Among 627,386 Persons in Contact With the Diamond Princess Cruise Ship Passengers Who Disembarked in Taiwan. J Med Internet Res. 2020;22(5):e19540. doi:10.2196/19540

Collins GS, Dhiman P, Andaur Navarro CL, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):49–60. doi:10.1038/s41591-024-03425-5

Choi H, Cho W, Kim MH, Hur JY. Public Health Emergency and Crisis Management: Case Study of SARS-CoV-2 Outbreak. Int J Environ Res Public Health. 2020;17:3984. doi:10.3390/ijerph17113984

Choi JY. COVID-19 in South Korea. Postgrad Med J. 2020;96:399–402. doi:10.1136/postgradmedj-2020-137738

Cowling BJ, Ali ST, Ng TWY, et al. Impact assessment of non-pharmaceutical interventions against coronavirus disease 2019 and influenza in Hong Kong: an observational study. Lancet Public Health. 2020;5(5):e279–e288. doi:10.1016/S2468-2667(20)30090-6

Davalgi S, Malatesh U, Rachana A, et al. Comparison of measures adopted to combat COVID-19 pandemic by different countries in WHO regions. Indian J Comm Health. 2020;32(2). doi:10.47203/IJCH.2020.v32i02SUPP.023

Dinh L, Dinh P, Nguyen PDM, Nguyen DHN, Hoang T. Vietnam's response to COVID-19: prompt and proactive actions. J Travel Med. 2020;27(3):taaa047. doi:10.1093/jtm/taaa047

Flemyng E, Noel-Storr A, Macura B, et al. Position Statement on Artificial Intelligence (AI) Use in Evidence Synthesis Across Cochrane, the Campbell Collaboration, JBI, and the Collaboration for Environmental Evidence 2025. Campbell Syst Rev. 2025;21(4):e70074. doi:10.1002/cl2.70074

Gates A, Vandermeer B, Hartling L. Technology-assisted risk of bias assessment in systematic reviews: a prospective cross-sectional evaluation of the RobotReviewer machine learning tool. J Clin Epidemiol. 2018;96:54–62. doi:10.1016/j.jclinepi.2017.12.015

Green DM, Bhatt NS, Bhakta N, et al. Serum Alanine Aminotransferase Elevations in Survivors of Childhood Cancer: A Report From the St. Jude Lifetime Cohort Study. Hepatology. 2019;69(1):94–106. doi:10.1002/hep.30176

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

Miller E. Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations. arXiv:2411.00640. 2024.

Mulder RL, Bresters D, Van den Hof M, et al. Hepatic late adverse effects after antineoplastic treatment for childhood cancer. Cochrane Database Syst Rev. 2019;4:CD008205. doi:10.1002/14651858.CD008205.pub3

Nachega JB, Grimwood A, Mahomed H, et al. From Easing Lockdowns to Scaling-Up Community-Based COVID-19 Screening, Testing, and Contact Tracing in Africa. Clin Infect Dis. 2020;ciaa695. doi:10.1093/cid/ciaa695

Ng Y, Li Z, Chua YX, et al. Evaluation of the Effectiveness of Surveillance and Containment Measures for the First 100 Patients with COVID-19 in Singapore. MMWR Morb Mortal Wkly Rep. 2020;69(11):307–311. doi:10.15585/mmwr.mm6911e1

Rose CJ, Bidonde J, Ringsten M, et al. Using a Large Language Model (ChatGPT-4o) to Assess the Risk of Bias in Randomized Controlled Trials of Medical Interventions: Interrater Agreement With Human Reviewers. Cochrane Evid Synth Methods. 2025;3(5):e70048. doi:10.1002/cesm.70048

Šuster S, Baldwin T, Verspoor K. Zero- and few-shot prompting of generative large language models provides weak assessment of risk of bias in clinical trials. Res Synth Methods. 2024;15(6):988–1000. doi:10.1002/jrsm.1749

Taneri PE, Engel C, Engel H, et al. Human Versus Artificial Intelligence: Comparing Cochrane Authors' and ChatGPT's Risk of Bias Assessments. Cochrane Evid Synth Methods. 2025;3(7):e70044. doi:10.1002/cesm.70044

Tian Y, Yang X, Doi SAR, et al. Towards the automatic risk of bias assessment on randomized controlled trials: A comparison of RobotReviewer and humans. Res Synth Methods. 2024;15(6):1111–1119. doi:10.1002/jrsm.1761

Wilasang C, Sararat C, Jitsuk NC, et al. Reduction in effective reproduction number of COVID-19 is higher in countries employing active case detection with prompt isolation. J Travel Med. 2020;taaa095. doi:10.1093/jtm/taaa095

Wong SYS, Kwok KO, Chan FKL. What can countries learn from Hong Kong's response to the COVID-19 pandemic? CMAJ. 2020;192(19):E511–E515. doi:10.1503/cmaj.200563

## Appendices

## Appendix A

### Mapping of the observational risk-of-bias criteria in Juneau et al. (2023) to the earlier criteria in Mulder et al. (2019)

For observational studies, this pilot uses the 8-criterion risk-of-bias rubric as reported in Juneau et al. (2023). That rubric was adapted from Mulder et al. (2019), where similar criteria were applied in a childhood-cancer review. In Juneau et al. (2023), some criteria were generalized so the rubric could be applied to observational studies more broadly, including studies of COVID-19 contact tracing. Table 3 documents those wording changes for transparency.

See [Table 3 - RoB_criteria_mapping.csv](data/public/Table%203%20-%20RoB_criteria_mapping.csv)