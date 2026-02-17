---
name: model-card-generator
description: Create a standardized model card documenting a health AI system's capabilities, limitations, and evidence
category: clinical-ai
raigh_tier: tier-1
difficulty: intermediate
estimated_time: "3 hours"
prerequisites: [run-tripod-ai-checklist, evidence-chain-assessment]
tags: [model-card, documentation, transparency, fairness, deployment]
evidence_basis: "https://doi.org/10.1145/3287560.3287596"
version: "1.0"
---

# Model Card Generator

## Purpose

Model cards are the "nutrition labels" of AI. They document what a model does, how it was trained, what it's good at, what it's not, and who should (and shouldn't) use it. This skill teaches you to create a health AI model card following the standard template, enriched with clinical context, evidence chain status, and fairness considerations.

## Learning Objectives

1. Explain why model cards matter for health AI transparency and safety
2. Complete all sections of a health AI model card template
3. Document performance across demographic subgroups (fairness)
4. Communicate limitations honestly and specifically
5. Create a model card that a clinician, regulator, and patient advocate could all understand

## Context

The FDA now expects model documentation for AI/ML medical devices. The EU AI Act mandates transparency documentation for high-risk AI. Model cards are becoming a regulatory requirement, not just a best practice. But most health AI model cards are boilerplate garbage. This skill teaches you to write one that's actually useful.

## Steps

### Step 1: Select a Model

Choose a health AI model to document. Options:
- A model from the `awesome-health-ai-evaluation` model registry
- An open-source health AI model (e.g., CheXpert, MONAI)
- A model developed at your institution

### Step 2: Complete the Model Card Template

Use this template (adapted from Mitchell et al. 2019 for health AI):

```yaml
model_card:
  # Section 1: Model Details
  model_name: ""
  version: ""
  type: "classification | regression | segmentation | generation"
  developers: ""
  date: ""
  license: ""
  contact: ""

  # Section 2: Intended Use
  primary_use: ""
  primary_users: ""
  out_of_scope_uses: ""
  clinical_context: ""

  # Section 3: Training Data
  dataset_name: ""
  dataset_size: ""
  data_source: ""
  demographics:
    age_range: ""
    sex_distribution: ""
    race_ethnicity: ""
    geographic_origin: ""
  collection_period: ""
  inclusion_criteria: ""
  exclusion_criteria: ""
  known_biases: ""

  # Section 4: Evaluation Data
  validation_type: "internal | external | temporal | geographic"
  evaluation_dataset: ""
  evaluation_size: ""
  evaluation_demographics: ""

  # Section 5: Performance Metrics
  primary_metric: ""
  primary_metric_value: ""
  secondary_metrics: []
  calibration: ""
  clinical_utility: ""  # DCA result if available

  # Section 6: Subgroup Performance
  performance_by_age: {}
  performance_by_sex: {}
  performance_by_ethnicity: {}
  performance_by_site: {}
  worst_subgroup: ""

  # Section 7: Evidence Chain Status
  phase_1_technical: "complete | partial | missing"
  phase_2_clinical: "complete | partial | missing"
  phase_3_utility: "complete | partial | missing"
  phase_4_implementation: "complete | partial | missing"
  phase_5_monitoring: "complete | partial | missing"

  # Section 8: Limitations
  known_limitations: []
  failure_modes: []
  populations_not_tested: []

  # Section 9: Ethical Considerations
  fairness_assessment: ""
  privacy_considerations: ""
  human_oversight_requirement: ""

  # Section 10: Recommendations
  deployment_recommendation: ""
  monitoring_plan: ""
  update_schedule: ""
```

### Step 3: Fill In Each Section

For each section, use these sources:
- **Model Details**: The paper, repo, or product documentation
- **Training Data**: Methods section of the paper + supplementary materials
- **Performance**: Results section + supplementary tables
- **Subgroup Performance**: Often buried in supplementary materials or absent (document as "Not reported")
- **Evidence Chain**: Your evidence chain assessment (from that skill)
- **Limitations**: Discussion section + your critical analysis

### Step 4: Quality Check

Verify your model card against these questions:
- [ ] Could a clinician in Monrovia understand this model card?
- [ ] Are limitations stated specifically (not just "more research needed")?
- [ ] Are populations NOT tested explicitly listed?
- [ ] Is subgroup performance reported, or is the absence documented?
- [ ] Is the evidence chain phase clearly stated?
- [ ] Would you feel comfortable deploying this model based on this card?

## Artifacts

1. **Completed Model Card** — YAML-formatted model card for one health AI model
2. **Narrative Summary** — 1-page human-readable version of the model card
3. **Fairness Flag Report** — Subgroups where performance differs significantly or hasn't been tested

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Completeness | All 10 sections filled (or explicitly marked "Not available") | Sections left blank |
| Accuracy | Information matches source publications/documentation | Errors or unsupported claims |
| Honesty | Limitations stated specifically and prominently | Limitations minimized or generic |
| Accessibility | A non-ML clinician could understand the card | Overly technical jargon |
| Fairness | Subgroup gaps documented or absence flagged | Fairness section ignored |

## Common Mistakes

- Copying performance claims from abstracts without checking methods
- Writing generic limitations ("needs more validation") instead of specific ones ("not tested on patients over 80 or on African populations")
- Treating model cards as marketing documents instead of transparency documents
- Forgetting to document what the model should NOT be used for (out-of-scope uses)

## Related Skills

- `evidence-chain-assessment` — Feeds Section 7 of the model card
- `run-tripod-ai-checklist` — Reporting quality informs model card completeness
- `evaluate-model-calibration` — Feeds Section 5 calibration field
- `fairness-audit` — Feeds Section 6 subgroup performance

## References

- Mitchell et al. (2019). Model Cards for Model Reporting: https://doi.org/10.1145/3287560.3287596
- FDA AI/ML Action Plan: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-software-medical-device
- Google Model Cards Toolkit: https://modelcards.withgoogle.com/
