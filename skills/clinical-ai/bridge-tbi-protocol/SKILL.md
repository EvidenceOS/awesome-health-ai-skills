---
name: bridge-tbi-protocol
description: Understand and apply the BRIDGE-TBI biomarker-guided CT decision protocol
category: clinical-ai
raigh_tier: tier-2
difficulty: advanced
estimated_time: "5 hours"
prerequisites: [evidence-chain-assessment, evaluate-model-calibration]
tags: [tbi, biomarkers, gfap, uch-l2, ct-reduction, bridge, clinical-protocol]
evidence_basis: "https://doi.org/10.1016/S0140-6736(23)01554-5"
version: "1.0"
---

# BRIDGE-TBI Protocol

## Purpose

The BRIDGE-TBI study demonstrated that blood biomarkers (GFAP and UCH-L2) can safely reduce unnecessary CT scans in mild traumatic brain injury by 32% (meta-analysis of 28,612 patients). This skill teaches you to understand the protocol, evaluate its evidence chain, and consider adaptation for resource-limited settings where CT access is scarce and biomarker-guided triage could be transformative.

## Learning Objectives

1. Explain the clinical problem: CT overuse in mild TBI and CT scarcity in LMICs
2. Describe the BRIDGE-TBI protocol (biomarker thresholds, decision rules, patient flow)
3. Evaluate the evidence using the evidence chain framework
4. Calculate the clinical impact (NNT, CT reduction rate, sensitivity at threshold)
5. Design an adaptation protocol for a resource-limited setting

## Context

In high-income countries, ~90% of CT scans for mild TBI are negative — massive overuse. In low-income countries, CT scanners may be hours away — massive underuse. A blood biomarker that identifies who truly needs a CT scan solves both problems: reducing unnecessary scans in HICs and prioritizing scarce CT resources in LMICs.

## Steps

### Step 1: Understand the Biomarkers

| Biomarker | Full Name | What It Measures | Key Threshold |
|---|---|---|---|
| **GFAP** | Glial Fibrillary Acidic Protein | Astrocyte damage (brain-specific) | < 30 pg/mL suggests low risk |
| **UCH-L2** | Ubiquitin C-terminal Hydrolase L1 | Neuronal cell body injury | Used in combination with GFAP |

Both are FDA-cleared (Abbott i-STAT TBI Plasma test) when used together with GCS 13-15 within 12 hours of injury.

### Step 2: Map the Decision Protocol

```
Patient presents with mild TBI (GCS 13-15, within 12 hours)
│
├── Draw blood for GFAP + UCH-L2
│
├── IF GFAP < threshold AND UCH-L2 < threshold
│   └── LOW RISK → Observe, no CT needed
│       (Sensitivity ≥ 97% for intracranial lesions)
│
├── IF either biomarker ≥ threshold
│   └── ELEVATED RISK → CT scan indicated
│
└── Clinical judgment always overrides biomarker result
    (e.g., anticoagulant use, deteriorating GCS)
```

### Step 3: Evidence Chain Assessment

Apply the evidence chain framework to BRIDGE-TBI:

**Phase 1 — Technical Validation:**
- Multi-site derivation and validation (Bazarian et al., Lancet 2023)
- 28,612 patients across multiple studies
- GFAP+UCH-L2 AUROC for detecting CT-positive TBI

**Phase 2 — Clinical Validation:**
- Prospective, multi-center studies
- Sensitivity ≥ 97% for traumatic intracranial lesions
- 32% CT reduction (meta-analysis)

**Phase 3 — Clinical Utility:**
- Decision Curve Analysis showing net benefit at relevant thresholds
- NNT calculations (how many patients tested to prevent one unnecessary CT?)
- Comparison to existing rules (Canadian CT Head Rule, New Orleans Criteria)

**Phase 4 — Implementation:**
- FDA clearance (2023) for point-of-care testing
- Emergency department workflow integration studies
- Turnaround time: ~15 minutes (point-of-care)

**Phase 5 — Monitoring:**
- Post-market surveillance ongoing
- Population-specific calibration questions (do thresholds hold in African populations?)

### Step 4: Calculate Clinical Impact

Using the meta-analysis data:
- 28,612 patients with mild TBI
- CT reduction: 32% (patients safely diverted from CT)
- Sensitivity: ≥ 97% for intracranial lesions requiring intervention
- Missed lesion rate: < 0.5% (and none requiring neurosurgical intervention in major studies)

Calculate for your setting:
- How many mild TBI patients does your facility see per year?
- At 32% reduction, how many CTs would be avoided?
- What is the cost saving? (CT cost × avoided scans)
- What is the time saving for patients? (CT wait time × avoided scans)

### Step 5: LMIC Adaptation Design

For a resource-limited setting (e.g., Liberia, Cameroon), design an adaptation:

| Consideration | HIC Protocol | LMIC Adaptation |
|---|---|---|
| CT availability | On-site, immediate | May be 2+ hours away by ambulance |
| Biomarker platform | Abbott i-STAT (lab) | Point-of-care lateral flow (future) |
| Decision threshold | Standard cut-offs | May need recalibration for local population |
| Clinical expertise | EM-trained physicians | May include clinical officers, nurses |
| Triage value proposition | Reduce unnecessary CTs | Identify who MUST get a CT (prioritize scarce resource) |

Key adaptation questions:
1. Is the biomarker threshold valid in this population? (need local validation study)
2. Can clinical officers use the protocol safely? (task-shifting study needed)
3. What's the referral pathway when CT is indicated but not on-site?
4. What's the cost-effectiveness in this resource context?

## Artifacts

1. **Protocol Flowchart** — Visual decision flowchart for BRIDGE-TBI adapted to your setting
2. **Evidence Chain Map** — Complete 5-phase evidence assessment for BRIDGE-TBI
3. **Impact Calculator** — Spreadsheet showing CT reduction, cost savings, and time savings for a specific facility
4. **LMIC Adaptation Proposal** — 2-page protocol adaptation for a named resource-limited setting

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Protocol understanding | Correctly describes biomarkers, thresholds, and decision rules | Errors in clinical protocol |
| Evidence assessment | All 5 phases evaluated with citations | Phases skipped or evidence misrepresented |
| Impact calculation | Reasonable estimates with stated assumptions | Implausible numbers or missing assumptions |
| LMIC adaptation | Addresses key differences with evidence-based reasoning | Copy-paste of HIC protocol without adaptation |

## Common Mistakes

- Confusing the CT reduction rate (32% from meta-analysis) with sensitivity (≥ 97%)
- Assuming HIC biomarker thresholds automatically apply in LMIC populations (they may not — genetic, nutritional, and injury pattern differences)
- Ignoring the "clinical override" component — biomarkers assist but don't replace clinical judgment
- Treating BRIDGE-TBI as "solved" — Phase 5 monitoring and population-specific validation are ongoing

## Related Skills

- `evidence-chain-assessment` — Apply the framework to other clinical AI tools
- `evaluate-model-calibration` — Calibration of biomarker thresholds
- `regulatory-landscape-analysis` — Regulatory pathway for biomarker tests in Africa
- `model-card-generator` — Document the BRIDGE-TBI evidence in a standardized card

## References

- Bazarian et al. (2023). Serum GFAP and UCH-L1 for prediction of absence of intracranial injuries on head CT (ALERT-TBI): Lancet. https://doi.org/10.1016/S0140-6736(23)01554-5
- FDA Clearance: Abbott i-STAT TBI Plasma test (2023)
- Korley et al. (2022). Performance of GFAP in TBI: https://doi.org/10.1016/S1474-4422(21)00083-5
- EvidenceOS BRIDGE-TBI Module: See `awesome-health-ai-evaluation` for full model registry entry
