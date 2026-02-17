---
name: dhis2-data-entry
description: Navigate DHIS2 for health data entry, reporting, and dashboard interpretation
category: digital-health-foundations
raigh_tier: MOOC
difficulty: beginner
estimated_time: "2 hours"
prerequisites: []
tags: [dhis2, hmis, data-entry, dashboards, surveillance]
evidence_basis: "https://dhis2.org/"
version: "1.0"
---

# DHIS2 Data Entry & Dashboard Interpretation

## Purpose

DHIS2 is the world's largest health management information system platform, used by 100+ countries — including 40+ in Africa — to collect, analyze, and visualize health data. This skill teaches you to enter data, navigate dashboards, and understand how facility-level data feeds national health intelligence. For AI practitioners, DHIS2 data is often the training signal for population health models.

## Learning Objectives

1. Navigate the DHIS2 web interface and understand its data model (Organisation Units, Data Elements, Periods)
2. Enter health facility data using data entry forms
3. Interpret a DHIS2 dashboard with maps, charts, and pivot tables
4. Export data in standard formats (CSV, JSON, ADX)
5. Understand data quality indicators and how missing data affects AI models

## Context

In most African health systems, DHIS2 is where routine health data lives. Malaria cases, vaccination coverage, maternal mortality — all flow through DHIS2. If you're building AI for African health, you need to understand this system. If you're a medical student, you'll encounter DHIS2 throughout your career.

## Steps

### Step 1: Access the DHIS2 Demo Instance

Go to https://play.dhis2.org/ and log into the demo instance. Explore:
- **Data Entry** app: Where facility-level data is entered
- **Dashboard** app: Where visualizations live
- **Data Visualizer**: Build your own charts
- **Maps**: Geographic visualization of health data

### Step 2: Understand the Data Model

| Concept | What It Means | Example |
|---|---|---|
| Organisation Unit | A location in the health system hierarchy | Country → Region → District → Facility |
| Data Element | A specific thing being measured | "Malaria cases confirmed", "BCG doses given" |
| Period | When the data was collected | Monthly, quarterly, yearly |
| Data Set | A collection of data elements for a form | "Monthly Disease Surveillance Report" |
| Indicator | A calculated value from data elements | "Malaria positivity rate = confirmed / tested" |

### Step 3: Enter Data

In the Data Entry app:
1. Select an Organisation Unit (pick a health facility)
2. Select a Data Set (e.g., "Disease Surveillance")
3. Select a Period (e.g., January 2026)
4. Enter values for 5+ data elements
5. Click "Complete" to submit

### Step 4: Interpret a Dashboard

Open the "Disease Surveillance" dashboard. For each visualization, answer:
- What data elements are displayed?
- What time period is shown?
- What geographic level (national, regional, facility)?
- What trends do you see?
- Where is data missing, and why does that matter for AI?

### Step 5: Export Data

Use the Data Visualizer to create a chart, then export as:
1. CSV (for spreadsheet analysis)
2. JSON (for programmatic use / AI pipelines)

Note the structure of the exported data — this is what AI models consume.

## Artifacts

1. **Data Entry Screenshot** — Evidence of completed data entry for one facility/period
2. **Dashboard Analysis** — 1-page write-up interpreting 3 dashboard visualizations (what the data shows, what's missing, implications)
3. **Exported Dataset** — CSV or JSON export with brief description of contents and quality assessment

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Data entry completed | All required fields filled, form submitted | Incomplete or not submitted |
| Dashboard interpretation | Identifies trends, gaps, and implications | Surface-level description only |
| Data quality awareness | Notes missing data and discusses impact on AI | Ignores data quality issues |
| Export format correct | Valid CSV/JSON with metadata | Corrupted or incomplete export |

## Common Mistakes

- Entering data for the wrong period (check the period selector carefully)
- Confusing data elements with indicators (elements are raw, indicators are calculated)
- Ignoring "0" vs blank — zero means "none observed", blank means "not reported" — critical difference for AI
- Assuming dashboard data is complete — always check reporting rates

## Related Skills

- `fhir-resource-basics` — How DHIS2 data maps to FHIR resources
- `digitalize-paper-records` — What happens before data reaches DHIS2
- `ai-readiness-scorecard` — DHIS2 usage is a key dimension of institutional AI readiness

## References

- DHIS2 Documentation: https://docs.dhis2.org/
- DHIS2 Academy: https://www.dhis2.org/academy
- HISP Centre: https://www.mn.uio.no/ifi/english/research/networks/hisp/
