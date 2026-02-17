---
name: medical-school-audit
description: Conduct a comprehensive digital maturity and AI readiness audit of a medical school
category: institutional-intelligence
raigh_tier: tier-2
difficulty: intermediate
estimated_time: "8 hours"
prerequisites: [digitalize-paper-records, dhis2-data-entry]
tags: [institutional-intelligence, medical-education, digitalization, audit, ai-readiness]
evidence_basis: "https://doi.org/10.1186/s12909-020-02007-6"
version: "1.0"
---

# Medical School Digitalization Audit

## Purpose

Most medical schools across Africa operate with a mix of paper records, disconnected digital systems, and limited data infrastructure. Before introducing AI health education or building institutional intelligence, you need a clear picture of what exists. This skill teaches you to conduct a structured audit of a medical school's digital maturity across 10 dimensions.

## Learning Objectives

1. Define the 10 dimensions of medical school digital maturity
2. Conduct structured interviews with key stakeholders (dean, registrar, IT, faculty, students)
3. Score each dimension using the AI Readiness Scorecard
4. Identify quick wins (improvements achievable in < 3 months)
5. Produce an actionable digitalization roadmap

## Context

The University of Liberia Medical School is the pilot case. ~600 students across 6 levels, likely significant paper-based processes. This audit template is designed to be replicable — once refined at UL, it can be deployed at any medical school in Africa.

## Steps

### Step 1: Prepare the Audit

Before arriving at the institution:
1. Request organizational chart and faculty list
2. Request any existing IT inventory or system documentation
3. Prepare interview guides for each stakeholder group
4. Set up the scoring spreadsheet (template in assets/)
5. Schedule 1-hour interviews with: Dean/Associate Dean, Registrar, IT Director, 3 faculty members, 3 student representatives

### Step 2: Conduct the 10-Dimension Assessment

| # | Dimension | What to Assess | Who to Ask |
|---|---|---|---|
| 1 | **Student Records** | Paper vs digital, completeness, accessibility, security | Registrar |
| 2 | **Learning Management** | LMS platform, usage rate, course materials online, assessment tools | IT Director, Faculty |
| 3 | **Library & Resources** | E-journal access (HINARI?), offline collections, search tools | Librarian |
| 4 | **Clinical Training** | Rotation documentation, evaluation forms, simulation tools | Clinical faculty |
| 5 | **Communication** | Email, messaging, announcement systems, student-faculty channels | Students, IT |
| 6 | **Connectivity** | Internet reliability, bandwidth, Wi-Fi coverage, device availability | IT Director, Students |
| 7 | **Faculty Digital Skills** | LMS competency, data literacy, willingness to adopt new tools | Faculty |
| 8 | **Data Governance** | Policies on data protection, consent, retention, sharing | Dean, IT |
| 9 | **Interoperability** | Do systems connect? Data flows between departments? | IT Director |
| 10 | **AI Awareness** | Current AI tool usage, attitudes toward AI, perceived needs | Faculty, Students |

### Step 3: Score Each Dimension

Use a 0-4 scale:

| Score | Level | Description |
|---|---|---|
| 0 | **None** | No digital systems for this dimension |
| 1 | **Ad hoc** | Some digital tools used inconsistently by individuals |
| 2 | **Developing** | Institutional tools exist but not universally adopted |
| 3 | **Established** | Digital systems standardized and widely used |
| 4 | **Advanced** | Digital systems integrated, data-driven, continuously improving |

**Total possible: 40 points**

| Range | Digital Maturity Level |
|---|---|
| 0-10 | **Pre-digital** — Major infrastructure investment needed |
| 11-20 | **Early digital** — Foundation exists, significant gaps |
| 21-30 | **Developing digital** — Ready for targeted interventions |
| 31-40 | **Digitally mature** — Ready for advanced AI integration |

### Step 4: Identify Quick Wins

Quick wins meet ALL of these criteria:
- Achievable in < 3 months
- Low cost (< $5,000)
- High impact on at least one dimension
- Don't require institutional policy changes

Common quick wins:
- Set up HINARI access (if not already active) — free e-journal access
- Create a shared Google Drive / OneDrive for course materials
- Digitalize the most critical paper form (e.g., clinical rotation evaluation)
- Establish a student communication channel (WhatsApp group → Telegram/Slack upgrade path)
- Run a faculty digital skills workshop (half-day)

### Step 5: Create the Roadmap

Structure the roadmap as:

**Immediate (0-3 months): Quick Wins**
- List quick wins with responsible person and deadline

**Short-term (3-6 months): Foundation**
- LMS selection/deployment
- Student records digitalization (highest-priority subset)
- Data governance policy draft

**Medium-term (6-12 months): Integration**
- System connectivity (LMS ↔ student records)
- Faculty digital skills certification
- First AI health module (Module 00)

**Long-term (12-24 months): Transformation**
- Full RAIGH curriculum delivery
- Institutional data analytics
- AI-assisted learning tools

## Artifacts

1. **Interview Summaries** — Notes from each stakeholder interview (anonymized)
2. **10-Dimension Scorecard** — Completed scoring matrix with evidence for each score
3. **Quick Wins List** — Prioritized list of ≤5 quick wins with owners and deadlines
4. **Digitalization Roadmap** — 24-month phased roadmap with milestones

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| All 10 dimensions assessed | Evidence from interviews + observation | Dimensions missing or scored without evidence |
| Scores justified | Each score backed by specific observation | Arbitrary scores |
| Quick wins realistic | Achievable, low-cost, high-impact | Ambitious projects masquerading as quick wins |
| Roadmap actionable | Named owners, specific deadlines, clear milestones | Vague timeline without accountability |

## Common Mistakes

- Conducting the audit as a checklist exercise instead of genuine inquiry (ask "show me" not just "do you have")
- Scoring based on what the institution plans to do instead of what currently exists
- Recommending expensive solutions when simple ones would work (e.g., suggesting a $50K LMS when Google Classroom is free)
- Not including students in the assessment — they often have the most accurate picture of what works and what doesn't
- Ignoring power dynamics — IT may overstate capabilities, students may understate access

## Related Skills

- `digitalize-paper-records` — Follow-up skill for the records dimension
- `lms-integration` — Follow-up skill for the LMS dimension
- `ai-readiness-scorecard` — Simplified version focused only on AI readiness
- `student-record-migration` — Technical skill for the records digitalization

## References

- Ellaway et al. (2015). Building Digital Infrastructure in Medical Schools: https://doi.org/10.3402/meo.v20.26160
- WHO-AFRO Digital Health Strategy: https://www.afro.who.int/publications/digital-health-strategy-africa
- WFME Basic Medical Education Standards: https://wfme.org/standards/
