---
name: evidence-chain-assessment
description: Map a health AI tool through the 5-phase evidence chain from lab to deployment
category: clinical-ai
raigh_tier: tier-1
difficulty: intermediate
estimated_time: "4 hours"
prerequisites: [run-tripod-ai-checklist]
tags: [evidence, validation, deployment, clinical-ai, lifecycle]
evidence_basis: "https://doi.org/10.1038/s41591-020-01069-z"
version: "1.0"
---

# Evidence Chain Assessment

## Purpose

Getting an AI model from "works in the lab" to "safe for patients" requires a chain of evidence across 5 distinct phases. Most health AI tools stall at Phase 1 (technical accuracy) and never complete Phases 3-5 (clinical validation, deployment, monitoring). This skill teaches you to map any health AI tool's evidence maturity and identify what's missing.

## Learning Objectives

1. Define the 5 phases of health AI evidence maturity
2. Assess where a specific AI tool sits in the evidence chain
3. Identify critical evidence gaps that block deployment
4. Design the study needed to fill the most critical gap
5. Communicate evidence maturity to non-technical stakeholders

## Context

When a vendor says "our AI is 95% accurate," you need to ask: accurate in whose hands, on what population, compared to what, and does accuracy translate to better patient outcomes? The evidence chain framework gives you the vocabulary and structure to ask the right questions.

## Steps

### Step 1: Learn the 5 Phases

| Phase | Name | Key Question | Gold Standard |
|---|---|---|---|
| 1 | **Technical Validation** | Does the model perform well on held-out data? | AUROC, AUPRC on external test set |
| 2 | **Clinical Validation** | Does performance hold in clinical conditions? | Prospective study in clinical setting |
| 3 | **Clinical Utility** | Does using the model improve clinical decisions? | Randomized controlled trial or DCA |
| 4 | **Implementation** | Can the model be deployed safely in real workflows? | Deployment study with workflow integration |
| 5 | **Monitoring** | Does performance hold over time in production? | Continuous monitoring with drift detection |

### Step 2: Select an AI Tool to Assess

Choose a health AI tool from:
- The `awesome-health-ai-evaluation` model registry
- An AI tool used or proposed at your institution
- A commercially available FDA-cleared AI device

### Step 3: Evidence Mapping

For each phase, search for and document the evidence:

```
Phase 1: Technical Validation
├── Published papers: [list with DOIs]
├── Test set description: [internal? external? multi-site?]
├── Key metrics: [AUROC, sensitivity, specificity, calibration]
├── Comparison to baseline: [what was the comparator?]
└── Assessment: [Strong / Adequate / Weak / Missing]

Phase 2: Clinical Validation
├── Prospective studies: [list with DOIs]
├── Population: [who was studied? representative?]
├── Setting: [academic? community? LMIC?]
├── Sample size: [adequate for the prevalence?]
└── Assessment: [Strong / Adequate / Weak / Missing]

Phase 3: Clinical Utility
├── RCTs or comparative studies: [list with DOIs]
├── Outcome measures: [patient outcomes? process measures?]
├── Decision Curve Analysis: [done? results?]
├── Override/adoption rates: [do clinicians actually use it?]
└── Assessment: [Strong / Adequate / Weak / Missing]

Phase 4: Implementation
├── Deployment studies: [list with DOIs]
├── Workflow integration: [how was it embedded?]
├── User experience: [clinician feedback?]
├── Failure modes: [what went wrong?]
└── Assessment: [Strong / Adequate / Weak / Missing]

Phase 5: Monitoring
├── Post-deployment monitoring: [is it being tracked?]
├── Performance drift: [has performance changed over time?]
├── Demographic fairness: [different performance by subgroup?]
├── Feedback loop: [are corrections fed back to model?]
└── Assessment: [Strong / Adequate / Weak / Missing]
```

### Step 4: Evidence Maturity Score

| Score | Meaning |
|---|---|
| **Phase 1 only** | Lab-ready. Not clinically validated. |
| **Phase 1-2** | Clinically validated. Not proven useful. |
| **Phase 1-3** | Clinical utility demonstrated. Ready for deployment planning. |
| **Phase 1-4** | Deployed. Needs monitoring plan. |
| **Phase 1-5** | Full evidence chain. Gold standard. |

Most health AI tools score Phase 1 only. The IDx-DR (diabetic retinopathy screening) is one of the few Phase 1-5 examples.

### Step 5: Gap Analysis and Next Study Design

For the most critical missing phase, design the study that would fill the gap:
- Study type (RCT, prospective cohort, implementation study)
- Population and setting
- Primary outcome
- Sample size estimate
- Timeline and budget estimate

## Artifacts

1. **Evidence Chain Map** — Complete 5-phase assessment for one health AI tool (using the template above)
2. **Evidence Maturity Score** — Phase score with justification
3. **Gap Analysis** — Which phase is the weakest link and why
4. **Next Study Proposal** — 1-page study design to fill the most critical gap

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| All 5 phases assessed | Every phase documented with evidence or "Missing" | Phases skipped |
| Evidence accurately represented | Cited papers match claims | Misrepresentation of study findings |
| Gap identification | Critical gap identified with clinical reasoning | Superficial gap analysis |
| Study proposal | Feasible study design addressing the right gap | Unrealistic or misdirected proposal |

## Common Mistakes

- Treating Phase 1 (technical) evidence as sufficient for deployment
- Ignoring Phase 5 (monitoring) — performance degrades over time, especially in new populations
- Conflating association studies with clinical utility (showing a biomarker correlates with outcome ≠ showing the AI improves decisions)
- Assuming evidence from one population transfers to another (a model validated in US academic centers may fail in African community hospitals)

## Related Skills

- `run-tripod-ai-checklist` — Phase 1-2 reporting quality assessment
- `decision-curve-analysis` — Phase 3 clinical utility quantification
- `model-card-generator` — Document the evidence chain in a model card
- `bridge-tbi-protocol` — Example of Phase 1-3 evidence chain in TBI

## References

- Park & Han (2018). Methodological Guide for Health AI Validation: https://doi.org/10.3348/kjr.2018.19.3.552
- Kelly et al. (2019). Key challenges for delivering clinical impact with AI: https://doi.org/10.1186/s12916-019-1426-2
- WHO Guidance on AI for Health (2021): https://www.who.int/publications/i/item/9789240029200
