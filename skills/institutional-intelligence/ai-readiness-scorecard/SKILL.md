---
name: ai-readiness-scorecard
description: Score a health institution on 10 dimensions of AI readiness
category: institutional-intelligence
raigh_tier: tier-1
difficulty: beginner
estimated_time: "2 hours"
prerequisites: []
tags: [ai-readiness, assessment, institutional, scorecard, digital-maturity]
evidence_basis: "https://doi.org/10.1038/s41591-021-01614-4"
version: "1.0"
---

# AI Readiness Scorecard

## Purpose

Before any health institution can adopt AI, it needs to know where it stands. The AI Readiness Scorecard is a rapid assessment tool that scores an institution across 10 dimensions in under 2 hours. It produces a single composite score (0-100) with a visual radar chart, making it easy to communicate gaps to leadership.

## Learning Objectives

1. Administer the AI Readiness Scorecard to a health institution
2. Score each of the 10 dimensions objectively
3. Generate a radar chart visualization
4. Identify the top 3 readiness gaps
5. Recommend targeted interventions for each gap

## Context

This is the lightweight version of the full medical school audit. Use it when you need a quick assessment (2 hours vs 8 hours) or when you're screening multiple institutions to identify the best pilot sites. The scorecard can be administered remotely via a structured interview.

## Steps

### Step 1: Administer the Scorecard

For each dimension, ask the structured questions and score 0-10:

| Dimension | Score 0 (Not Ready) | Score 5 (Partially Ready) | Score 10 (Ready) |
|---|---|---|---|
| **1. Data Availability** | No structured digital data | Some digital data but fragmented | Comprehensive, structured, accessible data |
| **2. Data Quality** | No quality processes | Ad hoc cleaning | Systematic quality management |
| **3. Infrastructure** | No servers/cloud, unreliable internet | Basic infrastructure, intermittent connectivity | Reliable infrastructure, adequate compute |
| **4. Technical Talent** | No IT/data staff | Basic IT support | Data engineers, analysts, or ML-capable staff |
| **5. Leadership Buy-in** | Leadership unaware or opposed | Aware but uncommitted | Active champion in leadership |
| **6. Clinical Workflow** | No standardized workflows | Some standardization | Digitized, standardized workflows |
| **7. Governance** | No data governance | Informal policies | Formal governance framework |
| **8. Interoperability** | Siloed systems | Some data sharing | Standards-based data exchange |
| **9. Ethics & Trust** | No ethics framework | Awareness exists | Ethics committee or framework active |
| **10. Change Readiness** | Resistance to change | Mixed attitudes | Culture of innovation and adoption |

### Step 2: Calculate Composite Score

**AI Readiness Score = Sum of all 10 dimensions (max 100)**

| Score Range | Level | Interpretation |
|---|---|---|
| 0-25 | **Foundation** | Significant investment needed before AI adoption |
| 26-50 | **Developing** | Ready for awareness training and pilot planning |
| 51-75 | **Ready** | Can begin AI pilots with targeted support |
| 76-100 | **Advanced** | Ready for production AI deployment |

### Step 3: Create Radar Chart

Plot the 10 dimension scores on a radar (spider) chart:

```python
import matplotlib.pyplot as plt
import numpy as np

dimensions = [
    'Data Availability', 'Data Quality', 'Infrastructure',
    'Technical Talent', 'Leadership', 'Clinical Workflow',
    'Governance', 'Interoperability', 'Ethics & Trust',
    'Change Readiness'
]
scores = [3, 2, 4, 1, 7, 3, 2, 1, 5, 6]  # Example scores

angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
scores_plot = scores + scores[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, scores_plot, alpha=0.25)
ax.plot(angles, scores_plot, linewidth=2)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(dimensions, size=9)
ax.set_ylim(0, 10)
ax.set_title('AI Readiness Scorecard', size=16, pad=20)
plt.savefig('ai_readiness_radar.png', dpi=150, bbox_inches='tight')
```

### Step 4: Identify Top 3 Gaps

Sort dimensions by score (ascending). The bottom 3 are your priority gaps. For each:
- Why is this dimension low? (root cause)
- What's the quick win? (achievable in < 3 months)
- What's the strategic fix? (6-12 month investment)

### Step 5: Write the One-Page Brief

Structure: Score (number) → Radar Chart (visual) → Top 3 Gaps (table) → Recommendations (bullets)

This one-pager is designed for hospital/university leadership — it should be immediately understandable without technical jargon.

## Artifacts

1. **Completed Scorecard** — 10 dimensions scored with brief justification for each
2. **Radar Chart** — Visual representation of readiness profile
3. **One-Page Brief** — Leadership-ready summary with score, chart, gaps, and recommendations

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| All 10 dimensions scored | Each score justified with evidence | Scores without justification |
| Radar chart | Clean, readable, accurately plotted | Missing or inaccurate visualization |
| Gap analysis | Root causes identified for bottom 3 | Gaps listed without analysis |
| One-pager | Readable by non-technical leadership | Overly technical or too long |

## Common Mistakes

- Scoring based on aspirations rather than current state
- Giving high "Leadership Buy-in" scores because one person is enthusiastic (need institutional commitment)
- Conflating data availability with data quality (you can have lots of bad data)
- Presenting the scorecard as a judgment rather than a diagnostic tool

## Related Skills

- `medical-school-audit` — Full 8-hour audit when you need deeper assessment
- `digitalize-paper-records` — Intervention for low Data Availability scores
- `lms-integration` — Intervention for low Clinical Workflow scores

## References

- Rajkomar et al. (2019). Machine Learning in Medicine: https://doi.org/10.1056/NEJMra1814259
- WHO Digital Health Maturity Model: https://www.who.int/publications/i/item/9789240042100
- HIMSS Digital Health Indicator: https://www.himss.org/what-we-do-solutions/digital-health-transformation/maturity-model
