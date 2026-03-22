---
title: "Large language models (LLMs) and LLM-based agents (hereafter, LLMs/agents) in life sciences research: an overview of systematic reviews. Protocol."
version: "v0.2"
date: "2026-02-11"
status: "DRAFT (V0.2)"
authors:
  - name: "Wait for name"
    affiliation: "Scaiences"
    contact: "email"
contributors:
  - "Name (role)"
links:
  repo: "https://github.com/carljuneau/scaiences"
  osf_registration: "<osf url (once registered)>"
---

# Protocol version and date
Version 0.2. February 11, 2026.

# Background and rationale
Large language models (LLMs) and LLM-based agents are being explored across many steps of the life sciences research lifecycle, including reading and synthesizing literature, extracting structured facts from papers, supporting analysis workflows, and generating research outputs. As systematic reviews on these applications accumulate, an overview of systematic reviews can help map what has been studied, how it has been studied, what works reliably, and where evidence is thin. Overviews treat systematic reviews as the unit of inclusion and synthesis, and require explicit methods as well as careful handling of overlap among reviews (Cochrane Handbook, Chapter V: Overviews of Reviews, accessed 2026-02-11 [Link](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-v)).

## Guidance and reporting standards
This protocol is written to align with established best practices for protocol transparency and overview conduct. We will use PRISMA-P items as a protocol structure guide where applicable (Moher et al., 2015 [Link](https://pubmed.ncbi.nlm.nih.gov/25554246/); Shamseer et al., 2015 [Link](https://www.bmj.com/content/349/bmj.g7647)). We will report the completed overview using PRIOR as the primary reporting guideline for overviews of reviews, adapting items as needed to fit a methods-focused topic rather than healthcare interventions (Gates et al., 2022 [Link](https://www.bmj.com/content/378/bmj-2022-070849)). We will report literature searches in line with PRISMA-S (Rethlefsen et al., 2021 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/)) and we will use PRISMA 2020 flow reporting conventions for transparency in study selection where compatible with PRIOR (Page et al., 2021 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC8008539/)).

# Objective
To provide an overview of systematic reviews on LLMs/agents use in life sciences research.

## Review questions
1. What life sciences research tasks and use cases for LLMs/agents have been covered by systematic reviews, and how are these uses characterized (for example, the research stage, workflow role, and tool type)?
2. How do systematic reviews evaluate LLM/agent performance, impact, and limitations (for example, study designs, benchmarks, comparators, error analysis, and human oversight)?
3. What recurrent gaps, risks, and methodological weaknesses are reported across systematic reviews, and what implications follow for future research and evidence synthesis practice?

## Operational definitions
We will use the term **LLMs/agents** to mean large language models and LLM-based agents. For inclusion decisions, we will accept authors’ own definitions when they explicitly study “large language models,” specific named LLMs (for example, GPT-family, PaLM-family, Llama-family, Claude-family), or agentic systems built around LLMs. We will define a **“systematic review”** as a review that reports an explicit, reproducible search strategy; prespecified eligibility criteria; and a documented selection process (for example, a PRISMA-style flow or equivalent). We will treat “systematic literature reviews” that meet these criteria as systematic reviews, even if not in biomedical journals, provided the topic is life sciences research.

# Eligibility criteria
We will include systematic reviews (with or without meta-analysis) that focus on the use, evaluation, or implementation of LLMs/agents in life sciences research. **Life sciences research** will be interpreted broadly and may include biomedical research, healthcare research, public health research, biology, bioinformatics, omics-related research workflows, and other adjacent domains where the primary intent is generating, analyzing, synthesizing, or applying life science knowledge.

We will **exclude**:
- Non-systematic narrative reviews, editorials, opinion pieces, tutorials, and single primary studies.
- Umbrella reviews and overviews of reviews (to avoid creating an additional review layer), but we will scan their reference lists to identify eligible systematic reviews.
- Systematic reviews focused solely on non-life-science domains (for example, business, law, or general education) unless they include a clearly separable life sciences research component.

We will include peer-reviewed articles and, if encountered, preprints that meet the systematic review definition; however, we will tag preprints as not peer-reviewed and consider them separately in synthesis to avoid mixing evidentiary status.

# Methods

## Information sources
We will search bibliographic databases that index both life sciences and computational research. At minimum we will search **MEDLINE via PubMed**. We will additionally search at least one broad multidisciplinary index (for example, **Scopus** or **Web of Science**), and one computer-science–leaning source (for example, **IEEE Xplore**) if access is available. Given the rapid pace of AI methods dissemination, we will also screen preprint sources where feasible (for example, **arXiv**) for systematic reviews that meet inclusion criteria, and we will use forward and backward citation searching on included reviews.

## Search strategy
The search strategy will combine terms for LLMs/agents with systematic review filters. We will use both controlled vocabulary (when available) and free-text keywords. We will not rely on a narrow list of model names alone, because naming conventions change quickly; instead, we will include general terms such as “large language model,” “LLM,” “generative AI,” and “agent,” plus a limited set of high-signal model identifiers (for example, “ChatGPT,” “GPT-4,” “Claude”) to improve recall. We will include systematic review terms such as “systematic review,” “systematic literature review,” and relevant publication types/filters when supported by the database.

We will peer review the main database strategy using the PRESS 2015 guideline (McGowan et al., 2016 [Link](https://pubmed.ncbi.nlm.nih.gov/27005575/)) and we will report the final strategies using PRISMA-S (Rethlefsen et al., 2021 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/)). The full search strategies (including exact strings, run dates, and any limits) will be publicly posted in the project repository at the time of manuscript submission.

## Study records and selection process
All retrieved records will be exported to a reference manager and deduplicated using a documented procedure. Screening will proceed in two stages: title/abstract screening and full-text screening. Two reviewers will independently screen records at both stages after a short calibration exercise on a pilot sample to align interpretations of eligibility criteria. Disagreements will be resolved by discussion, and if needed, a third reviewer will arbitrate.

We will document the selection process with a flow diagram and reasons for exclusion at full-text stage, consistent with PRIOR and PRISMA conventions (Gates et al., 2022 [Link](https://www.bmj.com/content/378/bmj-2022-070849); Page et al., 2021 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC8008539/)).

## Data extraction and data items
We will design a standardized extraction form and pilot it on a small subset of included reviews, refining as needed before full extraction. Two reviewers will extract data independently for a subset of reviews to ensure consistency, then proceed with single extraction plus verification depending on workload and observed agreement.

We will extract:
- **Bibliographic and scope data**: publication year, venue, review type, search end date, included study types, and domain.
- **Definitions**: how LLMs/agents are defined and which systems are studied.
- **Tasks**: the life sciences research tasks addressed (for example, literature discovery, screening, data extraction, synthesis, hypothesis generation, experiment planning, analysis support, reporting/writing) and the claimed role of the system (assistive tool, semi-automated pipeline, agentic workflow).
- **Evaluation**: how the systematic review evaluated evidence (for example, included benchmarks, performance metrics, human evaluation, comparators, error analysis, reproducibility, and any real-world deployment evidence).
- **Limitations**: reported limitations, risks, and research gaps.

## Risk of bias and methodological quality assessment of included systematic reviews
Because the unit of analysis is the systematic review, we will assess the trustworthiness of included reviews. We will use **ROBIS** to assess risk of bias in systematic reviews (Whiting et al., 2016 [Link](https://pubmed.ncbi.nlm.nih.gov/26092286/)). If we encounter systematic reviews for which ROBIS domains are not interpretable due to the nature of included primary studies (for example, highly heterogeneous computational benchmarks), we will document this and apply ROBIS as far as possible rather than silently omitting appraisal. We will report appraisal results transparently and will not exclude reviews solely on the basis of quality; instead, we will use appraisal to structure interpretation.

As a secondary lens, we may also capture **AMSTAR 2** items that are directly applicable to transparency and rigor (Shea et al., 2017 [Link](https://www.bmj.com/content/358/bmj.j4008/)), but ROBIS will be treated as the primary risk-of-bias framework.

## Management of overlap across systematic reviews
Overlaps in included primary studies across systematic reviews can bias summary impressions and can lead to double-counting when synthesizing claims. We will quantify overlap by constructing a citation matrix where feasible and computing the corrected covered area (CCA) (Pieper et al., 2014 [Link](https://pubmed.ncbi.nlm.nih.gov/24581293/)). We will also describe overlap narratively.

When multiple systematic reviews cover highly similar questions and substantially overlap, we will apply a transparent decision rule to avoid redundancy. We will use an established decision tool for selecting among overlapping systematic reviews (Pollock et al., 2019 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6341524/)) and we will justify any exclusions or prioritizations.

## Data synthesis plan
Given expected heterogeneity in LLM/agent systems, tasks, and evaluation designs, we anticipate primarily narrative and structured synthesis rather than meta-analysis. We will produce a descriptive map of where systematic review evidence exists across life sciences research tasks, the kinds of evaluation used, and the degree to which conclusions are supported by rigorous comparative designs.

We will synthesize findings at the level of systematic reviews, and we will avoid re-analyzing primary-study outcomes unless a very specific, well-justified need emerges and doing so would not effectively become a new systematic review. We will emphasize datedness by reporting each review’s search end date and discussing the implications for fast-moving LLM capability changes.

# Administrative information

## LLM assistance in conduct of this overview and transparency safeguards
This will be an LLM-assisted overview in the sense that LLM tools may be used to support parts of the workflow such as drafting and editing text, assisting with consistent coding, and checking extraction completeness. Any LLM assistance will be treated as a tool and not as an author. Human reviewers will remain accountable for all inclusion decisions, extracted data, analyses, and interpretations.

We will document any LLM use with the tool name, version, provider, dates of use, and a description of what it was used for, consistent with major editorial guidance that emphasizes transparency and accountability (ICMJE, 2024 [Link](https://www.icmje.org/news-and-editorials/updated_recommendations_jan2024.html); Flanagin et al., 2024 [Link](https://jamanetwork.com/journals/jama/fullarticle/2816213); Leung et al., 2023 [Link](https://www.jmir.org/2023/1/e51584)). Where feasible, we will archive prompts and outputs that materially shaped the work, while respecting copyright and data confidentiality. We will not input non-public full-text articles into third-party LLM tools unless licensing and terms permit it. We will treat LLM outputs as non-authoritative suggestions that require verification against source documents.

As a concrete precedent that LLM-assisted evidence synthesis workflows are being reported in the literature, we will cite and learn from published examples that document LLM-assisted review steps and their limitations (Scherbakov et al., 2024/2025 [Link](https://arxiv.org/abs/2409.04600)).

## Protocol registration, amendments, and deviations
We will publicly register this protocol before full screening begins. Because PROSPERO has eligibility constraints (for example, it does not accept many methods-focused reviews that lack direct health outcomes), we plan to register on OSF Registries using an available systematic review registration template and link the registration from the project repository (Page et al., 2018 [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC5819709/); OSF registration template [Link](https://osf.io/by27q/)). Any protocol amendments will be dated, described, and justified in the repository and in the final manuscript.

## Ethics and dissemination
This study synthesizes published literature and does not involve human participants, patient data, or interventions, so formal ethics review is not anticipated. We will disseminate results via a peer-reviewed publication and a public repository that includes search strategies, extraction templates, and derived datasets where licensing permits.

## Living overview option
This protocol defines a standard (non-living) overview as the initial publication. After publication, we may transition to a living overview if (a) new systematic reviews appear at a rate that would meaningfully change conclusions, and (b) maintaining updates remains feasible. Living is best treated as a production mode that can be applied after Version 1, as long as the update plan and versioning are explicit (Nussbaumer-Streit et al., 2025 [Link](https://pubmed.ncbi.nlm.nih.gov/40914296/)). If we transition to living mode, we will (i) define an update frequency, (ii) define triggers for interim updates, (iii) report changes between versions, and (iv) follow PRISMA-LSR reporting expectations for living evidence synthesis updates (Akl et al., 2024 [Link](https://www.bmj.com/content/387/bmj-2024-079183)).

## Data and code availability
We will make the protocol, search strategies, screening decisions (to the extent allowed), extraction forms, and analysis code publicly available in a version-controlled repository. We will provide a clear data dictionary for all extracted fields and document any manual judgment calls that affect coding.