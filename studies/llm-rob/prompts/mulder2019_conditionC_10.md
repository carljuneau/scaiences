# Mulder 2019 Condition C worked examples

Important caveats:

1. The Mulder 2019 Cochrane review does not provide all 8 judgments for all 33 included studies. Criteria 7 and 8 were assessed only for the 18 studies that reported risk-factor analyses. In the all-33 extraction file, the remaining 15 studies are coded as `review_not_assessed` for those two fields.
2. All 10 selected worked examples below are from that 18-study subset, so every criterion value in the expected JSON is review-confirmed.
3. I could not lawfully or technically package full article text here. Each example therefore includes a short source excerpt plus a direct source link. The `full_text_status` field shows whether I actually fetched full text in this environment.
4. Under the protocol derivation rule (`all yes -> low; any unclear and no no -> moderate; any no -> serious`), all 10 selected examples derive to `serious` because every selected study has at least one `no` criterion.

## Selected studies

| Study | PMID | DOI | PMCID | Full-text status | Derived overall |
|---|---:|---|---|---|---|
| Ballauff 1999 | 10407809 | 10.1055/s-2008-1043763 |  | abstract_only_fetched_from_PubMed; full text not fetched in this environment | serious |
| Chotsampancharoen 2009 | 18518909 | 10.1111/j.1399-3046.2008.00983.x |  | abstract_only_fetched_from_PubMed; full text not fetched in this environment | serious |
| El-Rashedy 2017 | 28512555 | 10.4084/MJHID.2017.026 | PMC5419197 | full_text_fetched_from_PMC | serious |
| Green 2019 | 30016547 | 10.1002/hep.30176 | PMC6324960 | full_text_fetched_from_PMC | serious |
| Gunn 2016 | 26812459 | 10.1089/jayao.2015.0036 |  | abstract_only_fetched_from_PubMed; publisher page identified but not fetched in this environment | serious |
| Hudson 2013 | 23757085 | 10.1001/jama.2013.6296 | PMC3771083 | full_text_fetched_from_PMC | serious |
| Hyodo 2012 | 22248714 | 10.1016/j.bbmt.2012.01.004 |  | publisher_open_archive_page_fetched; full methods/results not retrieved in this environment | serious |
| Mulder 2013 | 22901831 | 10.1016/j.ejca.2012.07.009 |  | PubMed abstract fetched; publisher full-text endpoint returned 403 in this environment | serious |
| Schempp 2016 | 26422286 | 10.1097/MPH.0000000000000444 |  | abstract_only_fetched_from_PubMed; full text not fetched in this environment | serious |
| Tomita 2011 | 20562924 | 10.1038/bmt.2010.144 |  | publisher preview and PubMed abstract fetched; full text not retrieved in this environment | serious |

## Worked examples

### Ballauff 1999

- Citation: Ballauff A, Krähe J, Jansen B, Ross RS, Roggendorf H, Havers W. [Chronic liver disease after treatment of malignancies in children]. Klin Padiatr. 1999;211(2):49-52.
- PMID: 10407809
- DOI: 10.1055/s-2008-1043763
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/10407809/
- Full-text status: abstract_only_fetched_from_PubMed; full text not fetched in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 87

Input excerpt:

> Chemotherapy, which has greatly improved the prognosis of children with malignant diseases, is potentially hepatotoxic. Furthermore, there is a risk for viral hepatitis acquired by blood products. In this study we looked for hepatotoxicity and for chronic viral hepatitis during and after chemotherapy in 50 unselected children with malignant diseases. All patients had been treated before 1991 and had received blood products not screened for hepatitis C-antibodies. At follow up 16 children (32%) had pathological liver function tests; 13 of these 16 patients had chronic hepatitis C.

Expected JSON:

```json
{
  "study_id": "Ballauff 1999",
  "criteria": {
    "study_group_representative": "yes",
    "intervention_and_participants_defined": "no",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "yes",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: described study group consisted of more than 90% of the original cohort; intervention_and_participants_defined: type of chemotherapy was not mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: Chi² was calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### Chotsampancharoen 2009

- Citation: Chotsampancharoen T, Gan K, Kasow KA, Barfield RC, Hale GA, Leung W. Iron overload in survivors of childhood leukemia after allogeneic hematopoietic stem cell transplantation. Pediatr Transplant. 2009;13(3):348-352.
- PMID: 18518909
- DOI: 10.1111/j.1399-3046.2008.00983.x
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/18518909/
- Full-text status: abstract_only_fetched_from_PubMed; full text not fetched in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 89

Input excerpt:

> Iron overload has not been studied extensively and prospectively in pediatric survivors of allogeneic hematopoietic stem cell transplantation (HSCT); therefore, we conducted a prospective long-term study of 133 survivors of childhood leukemia to assess the incidence of and risk factors for iron overload and to investigate its association with organ dysfunction. One year after HSCT, the mean serum ferritin level was 1158 ng/mL, and 124 patients (93.2%) had serum ferritin above the upper limit of normal. Serum ferritin correlated positively with total bilirubin and glutamate pyruvate transaminase.

Expected JSON:

```json
{
  "study_id": "Chotsampancharoen 2009",
  "criteria": {
    "study_group_representative": "no",
    "intervention_and_participants_defined": "no",
    "outcome_assessed_for_60pct": "unclear",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: described study group consisted of less than 90% of the original cohort and was no random sample with respect to cancer treatment; intervention_and_participants_defined: number of participants with hepatitis virus infection was not mentioned; outcome_assessed_for_60pct: it was unclear whether outcome was assessed for more than 60% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was not objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: Chi² was calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### El-Rashedy 2017

- Citation: El-Rashedy FH, El-Hawy MA, El Hefnawy SM, Mohammed MM. Assessment of Obesity and Hepatic Late Adverse Effects in the Egyptian Survivors of Pediatric Acute Lymphoblastic Leukemia: a Single Center Study. Mediterr J Hematol Infect Dis. 2017;9(1):e2017026.
- PMID: 28512555
- DOI: 10.4084/MJHID.2017.026
- PMCID: PMC5419197
- Source link: https://pmc.ncbi.nlm.nih.gov/articles/PMC5419197/
- Full-text status: full_text_fetched_from_PMC
- Input text type: PMC_abstract_excerpt
- Input excerpt word count: 90

Input excerpt:

> Background: Childhood acute lymphoblastic leukemia (ALL) with current cure rates reaching 80% emphasizes the necessity to determine treatment-related long-term effects. Methods: In this case-control study, height, weight, and body mass index were assessed for 35 pediatric ALL survivors and 35 healthy children. Laboratory investigations included iron profile, liver enzymes, total and direct bilirubin, serum urea and creatinine, and hepatitis C virus antibodies by ELISA. Results: ALT, total and direct bilirubin, serum ferritin, and transferrin saturation were higher in survivors than controls, and 10 survivors (28.6%) had hepatitis C antibodies.

Expected JSON:

```json
{
  "study_id": "El-Rashedy 2017",
  "criteria": {
    "study_group_representative": "unclear",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "no",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: it was unclear whether the described study group consisted of more than 90% of the original cohort or was a random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: exact follow-up duration of the study group was not mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was not objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: Mann-Whitney test was performed."
}
```

Derived overall RoB under protocol rule: **serious**

### Green 2019

- Citation: Green DM, Wang M, Krasin MJ, et al. Serum Alanine Aminotransferase Elevations in Survivors of Childhood Cancer: A Report From the St. Jude Lifetime Cohort Study. Hepatology. 2019;69(1):94-106.
- PMID: 30016547
- DOI: 10.1002/hep.30176
- PMCID: PMC6324960
- Source link: https://pmc.ncbi.nlm.nih.gov/articles/PMC6324960/
- Full-text status: full_text_fetched_from_PMC
- Input text type: PMC_methods_results_excerpt
- Input excerpt word count: 108

Input excerpt:

> Eligibility for SJLIFE included diagnosis of childhood malignancy treated at St. Jude, survival ≥10 years from diagnosis, and current age ≥18 years. Participants underwent anthropometric measurements and markers of liver function and injury. Descriptive statistics summarized demographic and treatment variables. Elastic Net was used for model selection, and modified Poisson regression models with robust error variance identified risk factors; results were presented as relative risks with 95% confidence intervals. Among 4421 eligible individuals, 2751 participants (62.3%) had evaluable ALT. Median age at diagnosis was 7.4 years, median age at evaluation was 31.4 years, and median elapsed time from diagnosis to evaluation was 23.2 years.

Expected JSON:

```json
{
  "study_id": "Green 2019",
  "criteria": {
    "study_group_representative": "no",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "yes",
    "important_prognostic_factors_accounted_for": "yes",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: described study group consisted of less than 90% of the original cohort and was no random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was objective and precise; important_prognostic_factors_accounted_for: important prognostic factors and follow-up were taken into account; analysis_described_and_effect_quantified: relative risks were calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### Gunn 2016

- Citation: Gunn HM, Emilsson H, Gabriel M, Maguire AM, Steinbeck KS. Metabolic Health in Childhood Cancer Survivors: A Longitudinal Study in a Long-Term Follow-Up Clinic. J Adolesc Young Adult Oncol. 2016;5(1):24-30.
- PMID: 26812459
- DOI: 10.1089/jayao.2015.0036
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/26812459/
- Full-text status: abstract_only_fetched_from_PubMed; publisher page identified but not fetched in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 77

Input excerpt:

> Purpose: Childhood cancer survivors are at increased risk of metabolic dysfunction as a late effect of cancer treatment. Methods: This single-center, retrospective observational longitudinal study evaluated the metabolic health of all childhood cancer survivors attending an oncology long-term follow-up clinic at a university hospital in Sydney, Australia. Participants were 276 survivors, at least 5 years disease free, with a broad spectrum of oncological diagnoses. Primary metabolic health risk factors included raised body mass index, hypertension, and hypertransaminasemia.

Expected JSON:

```json
{
  "study_id": "Gunn 2016",
  "criteria": {
    "study_group_representative": "unclear",
    "intervention_and_participants_defined": "no",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "no",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: it was unclear whether the described study group consisted of more than 90% of the original cohort or was a random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were not mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: exact follow-up duration of the study group was not mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was not objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: Chi-square test and t-tests were performed."
}
```

Derived overall RoB under protocol rule: **serious**

### Hudson 2013

- Citation: Hudson MM, Ness KK, Gurney JG, et al. Clinical ascertainment of health outcomes among adults treated for childhood cancer. JAMA. 2013;309(22):2371-2381.
- PMID: 23757085
- DOI: 10.1001/jama.2013.6296
- PMCID: PMC3771083
- Source link: https://pmc.ncbi.nlm.nih.gov/articles/PMC3771083/
- Full-text status: full_text_fetched_from_PMC
- Input text type: PMC_methods_results_excerpt
- Input excerpt word count: 99

Input excerpt:

> Presence of health outcomes was ascertained among 1713 adult survivors of childhood cancer enrolled in the St Jude Lifetime Cohort Study and followed through October 31, 2012. Age-specific cumulative prevalence of adverse outcomes by organ system and sex-adjusted attributable fraction percentages with 95% confidence intervals were calculated. Using clinical criteria, hepatic abnormalities affected 13.0% of survivors. Hepatic screening used alanine aminotransferase, aspartate aminotransferase, and bilirubin. For hepatic outcomes, 1713 survivors were screened overall; among those exposed to mercaptopurine, thioguanine, or liver radiation, 119 of 920 (13.0%) had hepatopathy, versus 86 of 793 (10.9%) among unexposed survivors.

Expected JSON:

```json
{
  "study_id": "Hudson 2013",
  "criteria": {
    "study_group_representative": "no",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "yes",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: described study group consisted of less than 90% of the original cohort and was no random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy, radiotherapy location, and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: attributable fraction was calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### Hyodo 2012

- Citation: Hyodo H, Ishiguro H, Tomita Y, et al. Decreased serum testosterone levels in long-term adult survivors with fatty liver after childhood stem cell transplantation. Biol Blood Marrow Transplant. 2012;18(7):1119-1127.
- PMID: 22248714
- DOI: 10.1016/j.bbmt.2012.01.004
- PMCID: none found
- Source link: https://www.sciencedirect.com/science/article/pii/S1083879112000304
- Full-text status: publisher_open_archive_page_fetched; full methods/results not retrieved in this environment
- Input text type: publisher_abstract_excerpt
- Input excerpt word count: 91

Input excerpt:

> Fatty liver and male gonadal dysfunction are potential late effects of therapy in adult survivors treated with stem cell transplantation in childhood. We reviewed the clinical records of 34 male patients who received allogeneic SCT in childhood or adolescence. Median follow-up after SCT was 15.9 years. Fatty liver was diagnosed by ultrasound in 15 patients at 4 to 20 years after SCT. Patients who received cranial radiation therapy before SCT were more likely to develop fatty liver and insulin resistance. Fatty liver was also associated with decreased serum testosterone levels.

Expected JSON:

```json
{
  "study_id": "Hyodo 2012",
  "criteria": {
    "study_group_representative": "unclear",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: it was unclear whether the described study group consisted of more than 90% of the original cohort or was a random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy, radiotherapy location, and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was not objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: mean difference was calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### Mulder 2013

- Citation: Mulder RL, Kremer LCM, Koot BGP, et al. Surveillance of hepatic late adverse effects in a large cohort of long-term survivors of childhood cancer: prevalence and risk factors. Eur J Cancer. 2013;49(1):185-193.
- PMID: 22901831
- DOI: 10.1016/j.ejca.2012.07.009
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/22901831/
- Full-text status: PubMed abstract fetched; publisher full-text endpoint returned 403 in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 91

Input excerpt:

> Background: Childhood cancer survivors are a growing group of young individuals with a high risk of morbidity and mortality. Methods: The cohort consisted of all five-year childhood cancer survivors treated in the EKZ/AMC between 1966 and 2003, without hepatitis virus infection and history of veno-occlusive disease. Liver enzyme tests included serum alanine aminotransferase and gamma-glutamyltransferase. Multivariable linear and logistic regression analyses were performed. Results: The study population consisted of 1404 of 1795 eligible survivors, of whom 1362 performed liver enzyme tests at a median follow-up of 12 years after diagnosis.

Expected JSON:

```json
{
  "study_id": "Mulder 2013",
  "criteria": {
    "study_group_representative": "no",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "yes",
    "important_prognostic_factors_accounted_for": "yes",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: described study group consisted of less than 90% of the original cohort and was no random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: outcome definition was objective and precise; important_prognostic_factors_accounted_for: important prognostic factors and follow-up were taken into account; analysis_described_and_effect_quantified: odds ratios were calculated."
}
```

Derived overall RoB under protocol rule: **serious**

### Schempp 2016

- Citation: Schempp A, Lee J, Kearney S, Mulrooney DA, Smith AR. Iron Overload in Survivors of Childhood Cancer. J Pediatr Hematol Oncol. 2016;38(1):27-31.
- PMID: 26422286
- DOI: 10.1097/MPH.0000000000000444
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/26422286/
- Full-text status: abstract_only_fetched_from_PubMed; full text not fetched in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 92

Input excerpt:

> Iron overload is a significant cause of morbidity and mortality for patients who require frequent transfusions. We completed a prospective, cross-sectional study to evaluate the prevalence of iron overload in previously transfused childhood cancer survivors. Survivors were stratified into oncology patients not treated with HSCT, patients treated with allogeneic HSCT, and patients treated with autologous HSCT. Serum ferritin was collected and hepatic magnetic resonance imaging was obtained for those with iron overload. The prevalence of iron overload was 25.9% after allogeneic HSCT, 3.7% without HSCT, and 0% after autologous HSCT.

Expected JSON:

```json
{
  "study_id": "Schempp 2016",
  "criteria": {
    "study_group_representative": "unclear",
    "intervention_and_participants_defined": "no",
    "outcome_assessed_for_60pct": "unclear",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "yes",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "no"
  },
  "rationale": "study_group_representative: it was unclear whether the described study group consisted of more than 90% of the original cohort or was a random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were not mentioned; outcome_assessed_for_60pct: it was unclear whether the outcome was assessed for more than 60% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear, but the biochemical outcome measurement was not likely to be influenced by lack of blinding; outcome_definition_objective_precise: upper limits of normal for liver function measures were not described; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: no risk estimation was reported."
}
```

Derived overall RoB under protocol rule: **serious**

### Tomita 2011

- Citation: Tomita Y, Ishiguro H, Yasuda Y, et al. High incidence of fatty liver and insulin resistance in long-term adult survivors of childhood SCT. Bone Marrow Transplant. 2011;46(3):416-425.
- PMID: 20562924
- DOI: 10.1038/bmt.2010.144
- PMCID: none found
- Source link: https://pubmed.ncbi.nlm.nih.gov/20562924/
- Full-text status: publisher preview and PubMed abstract fetched; full text not retrieved in this environment
- Input text type: abstract_excerpt
- Input excerpt word count: 98

Input excerpt:

> Overweight and obesity among adult survivors of childhood SCT have been considered predictive of metabolic abnormalities, but the real incidence of fatty liver in adult survivors of SCT has not been fully elucidated. We determined whether adult survivors are at risk for overweight or obesity, metabolic abnormalities, and fatty liver, and whether these risks are associated with cranial radiotherapy before SCT. Among 51 patients, fatty liver was diagnosed in 11 male and 10 female patients during follow-up, and patients who received cranial radiotherapy before SCT developed fatty liver with insulin resistance more often than those who did not.

Expected JSON:

```json
{
  "study_id": "Tomita 2011",
  "criteria": {
    "study_group_representative": "unclear",
    "intervention_and_participants_defined": "yes",
    "outcome_assessed_for_60pct": "yes",
    "follow_up_length_reported": "yes",
    "outcome_assessors_blinded": "unclear",
    "outcome_definition_objective_precise": "no",
    "important_prognostic_factors_accounted_for": "no",
    "analysis_described_and_effect_quantified": "yes"
  },
  "rationale": "study_group_representative: it was unclear whether the described study group consisted of more than 90% of the original cohort or was a random sample with respect to cancer treatment; intervention_and_participants_defined: type of chemotherapy and number of participants with hepatitis virus infection were mentioned; outcome_assessed_for_60pct: outcome was assessed for more than 90% of the study group of interest; follow_up_length_reported: length of follow-up was mentioned; outcome_assessors_blinded: blinding was unclear; although biochemical measurements were unlikely to be influenced by lack of blinding, it was unclear whether biopsy assessors were blinded; outcome_definition_objective_precise: outcome definition was not objective and precise; important_prognostic_factors_accounted_for: important prognostic factors or follow-up were not taken into account; analysis_described_and_effect_quantified: mean difference was calculated."
}
```

Derived overall RoB under protocol rule: **serious**

## Files

- `mulder2019_rob_extraction_33.csv`: all 33 review extractions with `review_not_assessed` where Mulder 2019 did not score criteria 7 and 8.
- `mulder2019_conditionC_examples_10.json`: machine-readable structured list of the 10 worked examples.
- `mulder2019_conditionC_examples_10.md`: human-readable report.