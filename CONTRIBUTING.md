# Contributing to Awesome Health AI Skills

Thank you for contributing to the health AI skills ecosystem. Every skill you contribute helps train the next generation of AI health practitioners across Africa and globally.

## How to Contribute a Skill

### 1. Choose a Category

| Category | Description |
|---|---|
| `digital-health-foundations` | Core digital health literacy (FHIR, DHIS2, EHR navigation) |
| `ai-evaluation` | Model evaluation, reporting standards, evidence assessment |
| `clinical-ai` | Clinical decision support, biomarker-guided AI, clinician-AI interaction |
| `dpi-architecture` | Digital public infrastructure setup and integration |
| `regulatory` | Regulatory compliance, submission preparation, landscape analysis |
| `institutional-intelligence` | Medical school digitalization, LMS integration, AI readiness |

### 2. Create a Skill Folder

```
skills/<category>/<your-skill-name>/
├── SKILL.md          # Required: The skill definition
├── assets/           # Optional: Templates, data files, images
└── tests/            # Optional: Validation tests
```

### 3. Write Your SKILL.md

Every SKILL.md follows this structure:

```markdown
---
name: your-skill-name
description: One-line description
category: digital-health-foundations | ai-evaluation | clinical-ai | dpi-architecture | regulatory | institutional-intelligence
raigh_tier: MOOC | tier-1 | tier-2 | tier-3
difficulty: beginner | intermediate | advanced
estimated_time: e.g., "2 hours"
prerequisites: []
tags: []
evidence_basis: "DOI or URL to supporting evidence"
version: "1.0"
---

# Skill Name

## Purpose
What this skill teaches and why it matters.

## Learning Objectives
What the practitioner will be able to do after completing this skill.

## Context
When and where this skill is applied in health AI practice.

## Steps
Detailed, executable steps to practice this skill.

## Artifacts
What the practitioner produces as evidence of skill completion.

## Assessment Criteria
How artifacts are evaluated (rubric or checklist).

## Common Mistakes
What to watch out for.

## Related Skills
Links to prerequisite and follow-on skills.

## References
Evidence base and further reading.
```

### 4. Submit a Pull Request

1. Fork this repository
2. Create a branch: `skill/<your-skill-name>`
3. Add your skill folder with SKILL.md
4. Run validation: `python scripts/validate_skills.py`
5. Submit PR with description of what the skill teaches

### Quality Standards

- **Evidence-based**: Every skill should reference published evidence, guidelines, or standards
- **Executable**: Skills must produce measurable artifacts, not just knowledge transfer
- **Inclusive**: Write for practitioners in low-resource settings (consider bandwidth, device access)
- **Reviewed**: All skills are reviewed by domain experts before merging

### PAAHI OG Contributors

PAAHI Original Generation community members receive:
- Priority review queue for submitted skills
- Co-authorship recognition in the methodology paper
- Early access to new skill bundles and workflows
- Invitation to the RAIGH Academy Skill Authors cohort

### CEAIH Review

Skills tagged with clinical or regulatory content undergo additional review by CEAIH (Center for Evidence and AI in Health) to ensure accuracy and evidence-basis.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be respectful, constructive, and inclusive.

## License

Contributions are licensed under CC BY 4.0. By submitting a PR, you agree to this license.
