---
name: run-tripod-ai-checklist
description: Apply the TRIPOD+AI checklist to evaluate a published health AI study
category: ai-evaluation
raigh_tier: tier-1
difficulty: intermediate
estimated_time: "3 hours"
prerequisites: [fhir-resource-basics]
tags: [tripod, reporting-standards, critical-appraisal, evidence, methodology]
evidence_basis: "https://doi.org/10.1136/bmj-2023-078378"
version: "1.0"
---

# Run TRIPOD+AI Checklist

## Purpose

TRIPOD+AI is the gold standard checklist for reporting prediction model studies that use AI/ML. Most published health AI studies fail basic reporting standards. This skill teaches you to systematically evaluate any health AI study using the full TRIPOD+AI checklist — the same tool peer reviewers and regulators use.

## Learning Objectives

1. Explain why reporting standards matter for health AI evidence
2. Navigate the TRIPOD+AI checklist (27 items across 7 sections)
3. Apply the checklist to a published health AI study
4. Identify critical gaps that undermine a study's validity
5. Write a structured evidence assessment report

## Context

When someone publishes a paper claiming "our AI achieves 95% accuracy for detecting disease X," you need to know: What accuracy metric? On what population? With what validation method? Was it compared to clinician performance? TRIPOD+AI gives you the systematic framework to evaluate these claims.

## Steps

### Step 1: Obtain the Checklist

Download the TRIPOD+AI checklist from: https://www.tripod-statement.org/

The checklist has 27 items across these sections:
1. Title and Abstract
2. Introduction
3. Methods (Participants, Predictors/Model, Outcome, Sample Size, Missing Data, Analysis)
4. Results
5. Discussion
6. Other Information (Funding, Data/Code Sharing)

### Step 2: Select a Study to Evaluate

Choose a published health AI study. Good candidates:
- Any study from the `awesome-health-ai-evaluation` model registry
- A recent paper from your clinical domain
- The original IDx-DR FDA clearance study (good example of strong reporting)

### Step 3: Systematic Evaluation

For each of the 27 TRIPOD+AI items, score the study:

| Score | Meaning |
|---|---|
| **Complete** | Item fully reported with sufficient detail |
| **Partial** | Item mentioned but lacks detail |
| **Not reported** | Item not addressed |
| **N/A** | Item not applicable to this study type |

Work through each section methodically. Key items that most studies fail:

- **Item 4a** — Data sources (where did training data come from?)
- **Item 6a** — Model architecture and hyperparameters (reproducibility)
- **Item 8** — Sample size justification (was the study powered?)
- **Item 9** — Missing data handling (critical for real-world deployment)
- **Item 13a** — Calibration assessment (not just discrimination)
- **Item 15** — Model availability (can others validate?)

### Step 4: Calculate Reporting Completeness

Count:
- Total applicable items
- Complete items
- Partial items
- Not reported items

Reporting Completeness = (Complete + 0.5 * Partial) / Total Applicable × 100%

Research shows the median completeness for health AI studies is ~50%. Studies below 60% should be interpreted with significant caution.

### Step 5: Write Assessment Report

Structure your report as:

1. **Study summary** (1 paragraph: what was studied, main finding, study design)
2. **TRIPOD+AI completeness** (overall score + breakdown by section)
3. **Critical gaps** (which missing items most undermine confidence?)
4. **Strengths** (what did the study do well?)
5. **Recommendation** (is this evidence strong enough to inform clinical practice?)

## Artifacts

1. **Completed TRIPOD+AI Checklist** — All 27 items scored for one published study
2. **Evidence Assessment Report** — 2-3 page structured report following the template above
3. **Gap Summary Table** — Table of all "Not reported" and "Partial" items with impact assessment

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Checklist completeness | All 27 items evaluated | Items skipped or grouped |
| Scoring accuracy | Scores match actual paper content | Scores don't reflect paper |
| Critical analysis | Identifies which gaps matter most and why | Lists gaps without impact analysis |
| Report quality | Clear, structured, actionable conclusion | Vague or unfocused |

## Common Mistakes

- Confusing TRIPOD+AI with TRIPOD (classic) — the +AI extension adds items specific to ML/AI
- Scoring "Complete" when the study mentions something briefly (that's "Partial")
- Focusing only on performance metrics and ignoring methods items (8, 9, 13a)
- Treating the checklist as a scorecard rather than a guide — some items matter more than others depending on context

## Related Skills

- `evaluate-model-calibration` — Deep dive into TRIPOD+AI Item 13a
- `decision-curve-analysis` — TRIPOD+AI Item 16 (clinical utility)
- `evidence-chain-assessment` — Place the study in the broader evidence chain
- `model-card-generator` — Create structured model documentation from TRIPOD+AI assessment

## References

- TRIPOD+AI Statement: https://doi.org/10.1136/bmj-2023-078378
- TRIPOD+AI Explanation & Elaboration: https://doi.org/10.1136/bmj-2023-078259
- Collins GS et al. Protocol for TRIPOD+AI: https://doi.org/10.1136/bmjopen-2020-038916
