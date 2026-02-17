---
name: student-record-migration
description: Protocol for migrating medical student academic records from paper to structured digital systems
category: institutional-intelligence
raigh_tier: tier-2
difficulty: intermediate
estimated_time: "6 hours"
prerequisites: [digitalize-paper-records, medical-school-audit]
tags: [migration, student-records, academic, database, digitalization]
evidence_basis: "https://doi.org/10.1016/j.ijmedinf.2019.104012"
version: "1.0"
---

# Student Record Migration

## Purpose

Medical student academic records — grades, clinical rotation evaluations, exam scores, attendance — are the lifeblood of institutional intelligence. When these exist only on paper, the institution is flying blind: no analytics, no early warning for struggling students, no accreditation dashboards. This skill teaches you to design and execute a structured migration of student academic records from paper to a digital system.

## Learning Objectives

1. Design a normalized data schema for medical student academic records
2. Plan a phased migration starting with the most valuable data
3. Implement quality assurance protocols for data entry
4. Validate migrated data against source records
5. Create a basic analytics dashboard from the migrated data

## Context

At the University of Liberia Medical School, ~600 students across 6 levels have academic records spanning multiple years. Some may be partially digitalized (in spreadsheets or a basic system), but the full picture likely requires consolidation from multiple sources. This skill focuses on the academic records specifically — not clinical patient records.

## Steps

### Step 1: Design the Data Schema

A minimal schema for medical student records:

```sql
-- Students
CREATE TABLE students (
    student_id TEXT PRIMARY KEY,  -- e.g., "UL-MED-2026-0042"
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth DATE,
    gender TEXT,
    enrollment_year INTEGER NOT NULL,
    current_level INTEGER CHECK (current_level BETWEEN 1 AND 6),
    status TEXT DEFAULT 'active'  -- active, leave, graduated, withdrawn
);

-- Courses
CREATE TABLE courses (
    course_id TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    level INTEGER NOT NULL,
    credit_hours INTEGER,
    department TEXT
);

-- Grades
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id TEXT REFERENCES students(student_id),
    course_id TEXT REFERENCES courses(course_id),
    academic_year TEXT,  -- e.g., "2025-2026"
    semester INTEGER CHECK (semester IN (1, 2)),
    grade TEXT,  -- letter or percentage
    score NUMERIC,
    status TEXT DEFAULT 'final'  -- final, provisional, incomplete
);

-- Clinical Rotations
CREATE TABLE rotations (
    id SERIAL PRIMARY KEY,
    student_id TEXT REFERENCES students(student_id),
    rotation_name TEXT NOT NULL,
    site TEXT,
    start_date DATE,
    end_date DATE,
    supervisor TEXT,
    evaluation_score NUMERIC,
    comments TEXT
);
```

### Step 2: Plan the Migration Phases

| Phase | What to Migrate | Source | Priority | Effort |
|---|---|---|---|---|
| 1 | Current student roster (active students only) | Registrar records | Highest | 1-2 days |
| 2 | Course catalog (all courses by level) | Academic handbook | High | 1 day |
| 3 | Current semester grades | Faculty grade sheets | High | 3-5 days |
| 4 | Historical grades (past 2-3 years) | Registrar archives | Medium | 1-2 weeks |
| 5 | Clinical rotation records | Department files | Medium | 1-2 weeks |
| 6 | Full historical archive (all years) | Archives | Low | Ongoing |

Start with Phase 1 + 2 + 3. This gives you a working system with current data in under 2 weeks.

### Step 3: Data Entry Protocol

Follow the double-entry protocol from `digitalize-paper-records`:
1. Train 2-4 data entry staff on the schema and forms
2. Person A enters data from paper source
3. Person B independently enters same record
4. System flags discrepancies
5. Supervisor resolves by checking original
6. Target: <2% error rate

For efficiency, create data entry forms (Google Forms, Supabase Forms, or a simple web app) that enforce:
- Required fields
- Value constraints (e.g., grade must be A-F or 0-100)
- Reference integrity (student must exist before entering grades)

### Step 4: Validate Migration

After each phase:
1. Count check: number of digital records = number of paper records
2. Random sample validation: 10% spot-check against paper source
3. Completeness check: no required fields blank
4. Referential integrity: every grade links to a valid student and course
5. Error rate report: track and trend error rates across phases

### Step 5: Build a Basic Dashboard

With migrated data, create a simple analytics dashboard:

- **Student count by level** (bar chart)
- **Average GPA by level** (line chart)
- **Rotation completion rate** (percentage)
- **At-risk students** (GPA below threshold or incomplete rotations)
- **Course pass rates** (which courses have highest failure rates?)

This dashboard is the first "institutional intelligence" deliverable — it immediately demonstrates the value of digitalized records to leadership.

## Artifacts

1. **Data Schema** — SQL schema (or equivalent) for student academic records
2. **Migration Plan** — Phased plan with timeline, effort estimates, and responsible parties
3. **Quality Report** — Error rates from validation of first migration phase
4. **Dashboard Mockup** — Screenshot or live dashboard with at least 3 visualizations from migrated data

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Schema design | Normalized, with proper constraints and references | Flat structure or missing constraints |
| Migration plan | Phased, with effort estimates and clear priorities | All-at-once plan or no prioritization |
| Data quality | <2% error rate, validation documented | No validation or high error rate |
| Dashboard | At least 3 meaningful visualizations | Non-functional or irrelevant charts |

## Common Mistakes

- Trying to migrate everything at once instead of phasing (start with current students, not the full archive)
- Not involving the registrar from day 1 (they own the data and will maintain it)
- Designing the schema in isolation (work with faculty to understand what they need to query)
- Forgetting that data entry is labor — budget for data entry staff time and training
- Not planning for ongoing data entry after migration (migration is useless if new records go back to paper)

## Related Skills

- `digitalize-paper-records` — General protocol for paper-to-digital conversion
- `medical-school-audit` — Broader institutional assessment that identifies records as a priority
- `fhir-resource-basics` — For future integration with health data systems

## References

- Higher Education Data Management Best Practices: https://www.educause.edu/
- Supabase Documentation: https://supabase.com/docs
- WHO Health Workforce Data Standards: https://www.who.int/data/gho/data/themes/topics/health-workforce
