---
name: fhir-resource-basics
description: Read, interpret, and create basic FHIR resources for health data exchange
category: digital-health-foundations
raigh_tier: MOOC
difficulty: beginner
estimated_time: "3 hours"
prerequisites: []
tags: [fhir, interoperability, hl7, health-data, standards]
evidence_basis: "https://www.hl7.org/fhir/"
version: "1.0"
---

# FHIR Resource Basics

## Purpose

FHIR (Fast Healthcare Interoperability Resources) is the global standard for health data exchange. Every health AI system consumes or produces FHIR data. This skill teaches you to read, interpret, and create basic FHIR resources — the atoms of modern health data.

## Learning Objectives

After completing this skill, you will be able to:
1. Identify the 5 most common FHIR resource types (Patient, Observation, Condition, Encounter, DiagnosticReport)
2. Read a FHIR JSON resource and extract clinical meaning
3. Create a valid Patient resource from a paper record
4. Understand FHIR references (how resources link to each other)
5. Explain why FHIR matters for AI training data quality

## Context

This skill is foundational for anyone working with health data systems. Whether you're building AI models, integrating hospital systems, or analyzing health data dashboards, FHIR is the language everything speaks. In African health systems transitioning from paper to digital, understanding FHIR is the bridge.

## Steps

### Step 1: Understand Resource Types

Open the FHIR specification at https://www.hl7.org/fhir/resourcelist.html and familiarize yourself with these 5 resource types:

| Resource | What It Represents | Example |
|---|---|---|
| Patient | A person receiving care | Name, DOB, gender, identifier |
| Observation | A measurement or finding | Blood pressure, lab result, vital sign |
| Condition | A diagnosis or problem | "Traumatic brain injury, mild" |
| Encounter | A clinical interaction | ER visit, outpatient appointment |
| DiagnosticReport | A collection of findings | Radiology report, lab panel |

### Step 2: Read a FHIR Resource

Given this Patient resource, extract the clinical information:

```json
{
  "resourceType": "Patient",
  "id": "example-liberia-001",
  "identifier": [{
    "system": "http://hospital.liberia.gov/patients",
    "value": "UL-MED-2026-0042"
  }],
  "name": [{"family": "Johnson", "given": ["Emmanuel"]}],
  "gender": "male",
  "birthDate": "1998-03-15",
  "address": [{"city": "Monrovia", "country": "LR"}]
}
```

Questions to answer:
- What is the patient's full name?
- What identifier system is used?
- How old is this patient?

### Step 3: Create a Patient Resource

Take a sample paper patient record (from your institution or use the template in `assets/paper-record-template.pdf`) and convert it to a valid FHIR Patient JSON resource. Include at minimum: name, gender, birthDate, identifier, and address.

### Step 4: Understand References

Create an Observation resource for a Glasgow Coma Scale (GCS) score that references the Patient from Step 3:

```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [{"system": "http://loinc.org", "code": "9269-2", "display": "Glasgow coma score total"}]
  },
  "subject": {"reference": "Patient/example-liberia-001"},
  "valueQuantity": {"value": 14, "unit": "score"}
}
```

Note how `subject.reference` links this observation to a specific patient.

### Step 5: Validate Your Resources

Use the FHIR validator at https://validator.fhir.org/ to check that your Patient and Observation resources are valid FHIR.

## Artifacts

1. **Annotated FHIR Resource** — The Patient resource from Step 2 with clinical annotations explaining each field
2. **Created Patient Resource** — A valid FHIR Patient JSON created from a paper record
3. **Linked Observation** — A valid FHIR Observation referencing your Patient
4. **Validation Report** — Screenshot or output from FHIR validator showing valid resources

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Patient resource valid | Passes FHIR validator | Contains structural errors |
| All required fields present | name, gender, birthDate, identifier | Missing required fields |
| Observation correctly references Patient | Valid reference format | Broken or missing reference |
| Clinical interpretation correct | All questions answered accurately | Errors in interpretation |

## Common Mistakes

- Confusing `name.family` (surname) with `name.given` (first names) — `given` is an array
- Forgetting that `birthDate` uses ISO 8601 format (YYYY-MM-DD)
- Using free text instead of coded values (FHIR prefers LOINC, SNOMED, ICD codes)
- Creating resources without proper `resourceType` field

## Related Skills

- `dhis2-data-entry` — How DHIS2 aggregates FHIR-compatible data
- `digitalize-paper-records` — Systematic approach to paper-to-digital conversion
- `consent-form-design` — Data governance before you start collecting FHIR data

## References

- HL7 FHIR R4 Specification: https://www.hl7.org/fhir/
- FHIR for Africa: https://wiki.hl7.org/FHIR_Africa
- OpenHIE FHIR Guide: https://guides.ohie.org/arch-spec/
