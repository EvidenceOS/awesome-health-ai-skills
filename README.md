# Awesome Health AI Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Skills](https://img.shields.io/badge/skills-17-blue)](data/skills_index.json)
[![Bundles](https://img.shields.io/badge/bundles-7-green)](data/bundles.json)
[![Workflows](https://img.shields.io/badge/workflows-3-orange)](data/workflows.json)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

**Executable health AI skills for practitioners, students, and institutions.** Each skill is a structured, assessable unit with clear learning objectives, step-by-step instructions, and artifact-based assessment. Complete skills → produce artifacts → earn credentials.

> **This is not a link collection.** Our [sister repositories](#sister-repositories) curate references. This repo contains executable skills — the lab manual to their textbook.

## The Stack

```
Layer 1: Awesome-Lists (reference, CC0, community)
  ↓ feeds
Layer 2: Awesome-Skills (executable, CC BY 4.0, practitioner)  ← YOU ARE HERE
  ↓ assessed by
Layer 3: Certification Platform (credentialed, co-certified with university)
  ↓ placed by
Layer 4: Employment Network (RAIGH Academy guarantee)
```

## How It Works

1. **Browse** skills by category or bundle
2. **Execute** the skill following the structured steps
3. **Produce** the required artifacts (evidence of learning)
4. **Submit** artifacts for peer + expert review
5. **Earn** PAATHI-certified credentials

---

## Skill Categories

### Elements of Health AI (Pre-MOOC)

The on-ramp for everyone — digital literacy, Gen AI awareness, and health data ethics. Inspired by the University of Helsinki's [Elements of AI](https://www.elementsofai.com/) (2M+ enrollments, 26 languages). No prerequisites. Smartphone-accessible.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [Digital Literacy](skills/pre-mooc/digital-literacy/SKILL.md) | 2h | Beginner | File management, cloud storage, internet safety, professional communication |
| [Gen AI Basics for Health](skills/pre-mooc/gen-ai-basics-for-health/SKILL.md) | 3h | Beginner | Use Gen AI safely, detect hallucinations, VERIFY framework, privacy rules |
| [Health Data Awareness](skills/pre-mooc/health-data-awareness/SKILL.md) | 2h | Beginner | Health data types, patient rights, consent design, data protection |

### Digital Health Foundations (MOOC)

Core digital health literacy for every health professional.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [FHIR Resource Basics](skills/digital-health-foundations/fhir-resource-basics/SKILL.md) | 3h | Beginner | Read, interpret, and create FHIR resources |
| [DHIS2 Data Entry](skills/digital-health-foundations/dhis2-data-entry/SKILL.md) | 2h | Beginner | Navigate DHIS2 for data entry and dashboard interpretation |
| [Digitalize Paper Records](skills/digital-health-foundations/digitalize-paper-records/SKILL.md) | 4h | Beginner | Convert paper health records to structured digital formats |

### AI Evaluation (Tier 1)

Critical appraisal of health AI evidence — the skill most missing from medical education.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [TRIPOD+AI Checklist](skills/ai-evaluation/run-tripod-ai-checklist/SKILL.md) | 3h | Intermediate | Evaluate published health AI studies using the gold standard |
| [Model Calibration](skills/ai-evaluation/evaluate-model-calibration/SKILL.md) | 4h | Intermediate | Assess if predicted probabilities match observed outcomes |
| [Decision Curve Analysis](skills/ai-evaluation/decision-curve-analysis/SKILL.md) | 3h | Intermediate | Determine if a model improves clinical decisions |

### Clinical AI (Tier 1-2)

From evidence assessment to clinical deployment.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [Evidence Chain Assessment](skills/clinical-ai/evidence-chain-assessment/SKILL.md) | 4h | Intermediate | Map an AI tool through the 5-phase evidence chain |
| [BRIDGE-TBI Protocol](skills/clinical-ai/bridge-tbi-protocol/SKILL.md) | 5h | Advanced | Biomarker-guided CT decisions for traumatic brain injury |
| [Model Card Generator](skills/clinical-ai/model-card-generator/SKILL.md) | 3h | Intermediate | Create standardized AI model documentation |

### DPI Architecture (Tier 2)

Digital public infrastructure for national health data exchange.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [X-Road Setup](skills/dpi-architecture/xroad-setup/SKILL.md) | 8h | Advanced | Install and configure X-Road Security Server |

### Regulatory (Tier 2)

Navigate health AI regulation across jurisdictions.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [Regulatory Landscape Analysis](skills/regulatory/regulatory-landscape-analysis/SKILL.md) | 6h | Intermediate | Map AI health regulation for any country |

### Institutional Intelligence (Tier 1-2)

Digitalize and transform health education institutions.

| Skill | Time | Difficulty | Description |
|---|---|---|---|
| [AI Readiness Scorecard](skills/institutional-intelligence/ai-readiness-scorecard/SKILL.md) | 2h | Beginner | Score an institution on 10 AI readiness dimensions |
| [Medical School Audit](skills/institutional-intelligence/medical-school-audit/SKILL.md) | 8h | Intermediate | Comprehensive digital maturity audit |
| [Student Record Migration](skills/institutional-intelligence/student-record-migration/SKILL.md) | 6h | Intermediate | Migrate paper academic records to digital systems |

---

## Bundles

Bundles are role-based skill collections mapped to RAIGH Academy certification tiers.

| Bundle | Tier | Skills | Total Time | Certification |
|---|---|---|---|---|
| **Elements of Health AI** | Pre-MOOC | 3 | 7h | Certificate of Completion |
| **Digital Health Foundations** | MOOC | 3 | 9h | Certificate of Completion |
| **AI Evaluation Practitioner** | Tier 1 | 3 | 10h | PAATHI Certified AI Health Practitioner |
| **Clinical AI Deployer** | Tier 2 | 3 | 12h | PAATHI Certified Clinical AI Specialist |
| **DPI Architect** | Tier 2 | 1 (+3 planned) | 8h | PAATHI Certified DPI Architect |
| **Regulatory Navigator** | Tier 2 | 1 (+3 planned) | 6h | PAATHI Certified Regulatory Navigator |
| **Institutional Intelligence** | Tier 2 | 3 | 16h | PAATHI Certified II Specialist |

See [bundles.json](data/bundles.json) for the machine-readable bundle definitions.

## Workflows

Workflows chain skills into end-to-end professional objectives.

### 1. From Zero to Health AI Practitioner
**Time:** ~26 hours over 12-16 weeks
**Outcome:** Digitally literate, AI-aware, FHIR-competent, ready for Tier 1 certification

`digital-literacy` → `gen-ai-basics-for-health` → `health-data-awareness` → `fhir-resource-basics` → `dhis2-data-entry` → `run-tripod-ai-checklist` → `evaluate-model-calibration` → `decision-curve-analysis`

### 2. Medical School Digital Transformation Pilot
**Time:** ~40 hours over 8-12 weeks
**Outcome:** Institution assessed, records migrated, first dashboard live

`ai-readiness-scorecard` → `medical-school-audit` → `digitalize-paper-records` → `student-record-migration` → `fhir-resource-basics` → `dhis2-data-entry`

### 3. Become a Health AI Evidence Evaluator
**Time:** ~20 hours over 8 weeks
**Outcome:** Portfolio of evidence assessments, ready for Tier 1 certification

`fhir-resource-basics` → `run-tripod-ai-checklist` → `evaluate-model-calibration` → `decision-curve-analysis` → `evidence-chain-assessment` → `model-card-generator`

See [workflows.json](data/workflows.json) for the machine-readable workflow definitions.

---

## Skill Anatomy

Every SKILL.md follows this structure:

```
---
name: skill-name
description: One-line description
category: category-name
raigh_tier: MOOC | tier-1 | tier-2 | tier-3
difficulty: beginner | intermediate | advanced
estimated_time: "X hours"
prerequisites: [list-of-prerequisite-skills]
tags: [searchable, tags]
evidence_basis: "DOI or URL"
version: "1.0"
---

# Skill Name

## Purpose          — Why this skill matters
## Learning Objectives — What you'll be able to do
## Context          — When and where this skill is used
## Steps            — Detailed, executable instructions
## Artifacts        — What you produce as evidence
## Assessment Criteria — How artifacts are evaluated
## Common Mistakes  — What to watch out for
## Related Skills   — Prerequisite and follow-on skills
## References       — Evidence base and further reading
```

## Structured Data

All data is machine-readable for AI agent consumption:

| File | Description |
|---|---|
| [`data/skills_index.json`](data/skills_index.json) | Complete index of all skills with metadata |
| [`data/bundles.json`](data/bundles.json) | RAIGH tier bundle definitions |
| [`data/workflows.json`](data/workflows.json) | End-to-end workflow definitions |

## Validation

```bash
python scripts/validate_skills.py
```

Validates frontmatter fields, required sections, category-directory consistency, and prerequisite references.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines. Summary:

1. Fork this repo
2. Create a skill folder: `skills/<category>/<your-skill>/SKILL.md`
3. Follow the SKILL.md template above
4. Run `python scripts/validate_skills.py`
5. Submit a PR

### PAAHI OG Contributors

PAAHI (Pan-African AI Health Initiative) Original Generation members receive priority review queue and co-authorship on the methodology paper. See CONTRIBUTING.md for details.

### CEAIH Review

Skills with clinical or regulatory content undergo additional review by CEAIH (Center for Evidence and AI in Health) for evidence-basis validation.

---

## Sister Repositories

This repo is part of the EvidenceOS Awesome-List Ecosystem:

| Repository | Focus | Relationship |
|---|---|---|
| [awesome-african-digital-health](https://github.com/EvidenceOS/awesome-african-digital-health) | African digital health landscape | Reference layer for Digital Health Foundations skills |
| [awesome-health-ai-evaluation](https://github.com/EvidenceOS/awesome-health-ai-evaluation) | Health AI evidence assessment | Reference layer for AI Evaluation + Clinical AI skills |
| [awesome-ai-evaluation-metrics](https://github.com/EvidenceOS/awesome-ai-evaluation-metrics) | AI evaluation metrics catalog | Reference layer for calibration, DCA, fairness skills |
| [awesome-dpi-infrastructure](https://github.com/EvidenceOS/awesome-dpi-infrastructure) | Digital public infrastructure | Reference layer for DPI Architecture skills |
| [awesome-health-ai-regulations](https://github.com/EvidenceOS/awesome-health-ai-regulations) | Health AI regulatory landscape | Reference layer for Regulatory skills |

**The awesome-lists are the textbook. This repo is the lab manual.**

---

## Certification

Skills are assessed through artifact submission and peer + expert review. Certifications are co-issued by PAATHI (Pan-African Alliance for Technology & Health Innovation) and partner universities.

**Pilot:** University of Liberia Medical School (~600 students, 6 levels)

Credentials are:
- **Digital** — Open Badges 3.0 compliant
- **Verifiable** — Unique credential ID with QR verification
- **Portable** — One-click LinkedIn integration
- **Co-branded** — PAATHI + partner university logos

---

## License

Content is licensed under [Creative Commons Attribution 4.0 International](LICENSE). Skills have more IP value than link collections — CC BY 4.0 (not CC0) ensures attribution while allowing free use, adaptation, and redistribution.

---

*Maintained by [EvidenceOS](https://github.com/EvidenceOS) · PAATHI — Pan-African Alliance for Technology & Health Innovation · RAIGH Academy — Workforce Development Pillar*
