---
name: regulatory-landscape-analysis
description: Map the AI health regulatory landscape for a specific country or region
category: regulatory
raigh_tier: tier-2
difficulty: intermediate
estimated_time: "6 hours"
prerequisites: [run-tripod-ai-checklist]
tags: [regulation, fda, eu-ai-act, africa, compliance, landscape]
evidence_basis: "https://doi.org/10.1038/s41591-023-02603-3"
version: "1.0"
---

# Regulatory Landscape Analysis

## Purpose

Before deploying a health AI tool in any country, you need to understand the regulatory landscape: what's required, what's missing, and what pathways exist. This skill teaches you to conduct a structured regulatory landscape analysis for any country, with special attention to African nations where frameworks are rapidly evolving.

## Learning Objectives

1. Identify the 4 pillars of health AI regulation (device classification, data protection, clinical evidence, post-market surveillance)
2. Map a specific country's regulatory framework across all 4 pillars
3. Compare the country to reference frameworks (FDA, EU AI Act, AU model law)
4. Identify regulatory gaps and risks for AI deployment
5. Create a compliance roadmap for a specific health AI product

## Context

Only 15 of 54 African countries have any form of medical device regulation that could apply to health AI. The regulatory landscape is a patchwork — some countries have comprehensive frameworks, others have nothing. This skill helps you navigate this landscape and plan accordingly.

## Steps

### Step 1: Framework Mapping

For your target country, research and document:

| Pillar | Key Questions | Source |
|---|---|---|
| **Medical Device Regulation** | Is AI software classified as a medical device? What classification tier? Who is the regulatory authority? | National medicines authority, WHO Global Atlas |
| **Data Protection** | Is there a data protection law? Does it cover health data specifically? Cross-border transfer rules? | National data protection authority |
| **Clinical Evidence Requirements** | What clinical evidence is required for market access? Local clinical trials needed? | Regulatory authority guidelines |
| **Post-Market Surveillance** | Is there a vigilance system? Adverse event reporting requirements? | Regulatory authority + WHO |

### Step 2: Create the Country Profile

```yaml
country_profile:
  country: "Liberia"
  iso_code: "LR"
  regulatory_authority: "Liberia Medicines and Health Products Regulatory Authority (LMHRA)"

  medical_device_regulation:
    status: "emerging | established | comprehensive | none"
    ai_specific_provisions: true | false
    classification_system: "GHTF | EU MDR | national | none"
    details: ""

  data_protection:
    law_name: ""
    year_enacted: null
    health_data_specific: true | false
    cross_border_provisions: true | false
    enforcement_body: ""
    details: ""

  clinical_evidence:
    local_trial_required: true | false
    international_evidence_accepted: true | false
    fast_track_provisions: true | false
    details: ""

  post_market_surveillance:
    vigilance_system: true | false
    adverse_event_reporting: "mandatory | voluntary | none"
    details: ""

  key_gaps: []
  opportunities: []
  risk_level: "low | medium | high"
```

### Step 3: Reference Framework Comparison

Compare your country to these reference frameworks:

| Framework | What It Covers | Relevance |
|---|---|---|
| **US FDA** | AI/ML SaMD classification, predetermined change control plan, real-world performance | Gold standard for medical device AI regulation |
| **EU AI Act** | Risk classification (high-risk for medical AI), conformity assessment, post-market monitoring | Most comprehensive AI-specific regulation |
| **AU Model Law** | African Union model law for medical devices | Continental harmonization reference |
| **WHO AI Guidance** | 6 guiding principles for AI in health | International soft law benchmark |

### Step 4: Gap Analysis

For each pillar, rate the gap:
- **No gap**: Country framework covers this adequately
- **Partial gap**: Framework exists but is incomplete or outdated
- **Critical gap**: No framework exists — deployment risk is high

### Step 5: Compliance Roadmap

For a specific health AI product, create a step-by-step compliance plan:
1. Classification determination (what regulatory category?)
2. Evidence package (what studies/documentation needed?)
3. Registration/notification (what to file, with whom, timeline)
4. Data protection compliance (DPIAs, consent mechanisms)
5. Post-market plan (monitoring, reporting, updates)
6. Timeline and cost estimate

## Artifacts

1. **Country Regulatory Profile** — Complete YAML profile for one country
2. **Comparison Matrix** — Side-by-side comparison with FDA, EU AI Act, and AU model law
3. **Gap Analysis** — 4-pillar gap assessment with risk ratings
4. **Compliance Roadmap** — Step-by-step plan for one health AI product in this country

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Country profile completeness | All 4 pillars researched with sources cited | Pillars missing or unsourced |
| Accuracy | Information verified against primary sources | Reliance on secondary sources only |
| Gap analysis | Specific gaps identified with risk implications | Generic "needs improvement" statements |
| Compliance roadmap | Actionable steps with timeline | Vague or unrealistic plan |

## Common Mistakes

- Assuming absence of regulation means "no compliance needed" (the opposite — absence means higher risk)
- Using US FDA requirements as the global standard (each country has its own framework or lack thereof)
- Ignoring data protection (often the most developed pillar even in countries with weak device regulation)
- Not checking whether the regulatory authority actually enforces its regulations (law on paper vs practice)

## Related Skills

- `run-tripod-ai-checklist` — Evidence quality assessment for regulatory submissions
- `evidence-chain-assessment` — Regulatory submissions require evidence across multiple phases
- `model-card-generator` — Model cards support regulatory transparency requirements

## References

- WHO Global Atlas of Medical Devices: https://www.who.int/publications/i/item/9789241564465
- awesome-health-ai-regulations: See structured country data at https://github.com/EvidenceOS/awesome-health-ai-regulations
- African Union Model Law on Medical Devices: https://au.int/en/documents/20220210/au-model-law-medical-devices
- EU AI Act: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
