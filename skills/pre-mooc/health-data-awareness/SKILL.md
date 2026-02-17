---
name: health-data-awareness
description: Understand health data types, patient rights, informed consent, and data protection principles for health professionals
category: pre-mooc
raigh_tier: MOOC
difficulty: beginner
estimated_time: "2 hours"
prerequisites: [digital-literacy]
tags: [health-data, consent, privacy, data-protection, gdpr, patient-rights, ethics]
evidence_basis: "WHO Global Strategy on Digital Health 2020-2025; AU Convention on Cyber Security and Personal Data Protection (Malabo Convention)"
version: "1.0"
---

# Health Data Awareness

## Purpose

Health data is among the most sensitive data that exists. A leaked diagnosis can cost someone their job, their marriage, or their safety. Yet most health professionals receive minimal training on data rights, consent, and protection — especially in contexts where paper records are transitioning to digital systems. This skill builds the ethical and legal foundation for handling health data responsibly, whether on paper or screen.

## Learning Objectives

After completing this skill, you will be able to:

1. Classify health data into categories (identifiable, de-identified, anonymized, aggregate)
2. Explain patient data rights under at least one legal framework (GDPR, Malabo Convention, or national DPA)
3. Design an informed consent form for a simple health data collection
4. Identify 5 common data protection violations in health settings
5. Explain the difference between data collection for care vs research vs reporting

## Context

As African health systems digitalize — from paper registers to DHIS2, from WhatsApp consultations to telemedicine platforms — the volume of digital health data is exploding. But legal frameworks are catching up slowly: only 33 of 55 AU member states have data protection laws (as of 2024). This skill is relevant whether you work in a fully digital hospital in Nairobi or a paper-based clinic in rural Liberia.

This is part of the Pre-MOOC track and requires only basic digital literacy.

## Steps

### Step 1: Types of Health Data (20 minutes)

1. **Study the health data spectrum:**

   | Type | Definition | Example | Risk Level |
   |------|-----------|---------|------------|
   | **Identifiable** | Can be linked to a specific person | "John Kamara, DOB 15/03/1990, HIV positive" | Highest |
   | **Pseudonymized** | Identifying info replaced with codes | "Patient #4472, HIV positive" | High (can be re-identified) |
   | **De-identified** | All identifiers removed | "45-year-old male, HIV positive, Freetown" | Medium (small populations risk re-identification) |
   | **Anonymized** | Impossible to re-identify | "Urban male, 40-49, HIV positive" | Low |
   | **Aggregate** | Group-level statistics | "HIV prevalence in Freetown: 2.1%" | Lowest |

2. **Exercise:** Classify these 5 examples into the correct type:
   - "Mrs. Aminata Koroma tested positive for malaria on 12 February"
   - "Patient MK-2024-0847 tested positive for malaria"
   - "A 35-year-old woman in Western Area tested positive for malaria"
   - "Malaria positivity rate among women aged 30-39: 12%"
   - "35-year-old woman, only female teacher at [school name], tested positive"

3. **Key insight:** The last example shows that de-identification can fail in small populations. Context matters.

### Step 2: Patient Rights (30 minutes)

1. **Study the core patient data rights** (common across GDPR, Malabo Convention, and most national laws):

   | Right | What It Means | Health Example |
   |-------|--------------|----------------|
   | **Right to be informed** | Know what data is collected and why | Patient told their blood test results will be entered into DHIS2 |
   | **Right of access** | See your own data | Patient requests their full medical record |
   | **Right to rectification** | Correct inaccurate data | Patient's blood type was entered incorrectly |
   | **Right to erasure** | Request deletion (with limitations) | Patient wants STI test result removed from system |
   | **Right to restrict processing** | Limit how data is used | Patient consents to care but not research use |
   | **Right to data portability** | Move data between providers | Patient transferring from one hospital to another |
   | **Right to object** | Refuse certain data uses | Patient refuses data to be used for AI training |

2. **Research your country's data protection law:**
   - Does your country have a data protection act? (Check: [UNCTAD tracker](https://unctad.org/page/data-protection-and-privacy-legislation-worldwide))
   - If yes: What is it called? When was it enacted? Which body enforces it?
   - If no: What international framework applies? (Malabo Convention, GDPR for EU partners)

3. **Write a 1-paragraph summary** of the data protection landscape in your country.

### Step 3: Informed Consent Design (30 minutes)

1. **Study the 7 elements of valid informed consent for health data:**
   - **Purpose:** Why is data being collected?
   - **Data types:** What specific data will be collected?
   - **Duration:** How long will data be stored?
   - **Access:** Who will see the data?
   - **Use:** Will data be used for care only, or also research/reporting?
   - **Rights:** How can the patient access, correct, or delete their data?
   - **Voluntary:** Patient can refuse without affecting their care

2. **Design a consent form** for this scenario:
   > A medical school is conducting a pilot project to digitalize student health records. Students will have their immunization history, blood type, and chronic conditions entered into a new electronic system. The data will be used for student health services and may be used in anonymized form for a research paper on medical student health patterns.

3. Your consent form must:
   - Be written at a reading level accessible to all students
   - Include all 7 elements above
   - Include a clear opt-in/opt-out mechanism
   - Be no longer than 1 page

### Step 4: Spot the Violations (20 minutes)

1. **Read these 5 scenarios and identify the data protection violation in each:**

   **Scenario A:** A nurse takes a photo of a patient's wound on her personal phone to show a dermatologist colleague on WhatsApp.

   **Scenario B:** A hospital IT department migrates patient records to a new system. The old hard drives are thrown in the general waste bin.

   **Scenario C:** A research team publishes a paper about a rare disease case at a specific rural hospital. The paper says "a 23-year-old female patient" but the hospital only had one female patient with that condition that year.

   **Scenario D:** A community health worker enters patient data into a Google Sheet shared with the entire project team, including administrative staff.

   **Scenario E:** A medical school uses student patient encounter logs (with patient names) as training data for an AI model, citing the institution's general research consent.

2. **For each scenario, document:**
   - What right or principle was violated
   - What should have been done instead
   - What the potential harm could be

### Step 5: Care vs Research vs Reporting (20 minutes)

1. **Understand the three purposes** of health data collection:

   | Purpose | Legal Basis | Consent Needed | Example |
   |---------|------------|----------------|---------|
   | **Clinical care** | Necessity for treatment | Implied (emergency) or explicit | Recording vitals in patient chart |
   | **Research** | Informed consent or ethics board approval | Explicit, specific, documented | Using patient data in a clinical trial |
   | **Public health reporting** | Legal mandate | Not always required (statutory reporting) | Reporting cholera cases to district health office |

2. **The gray areas:**
   - Quality improvement: Is it care or research? (Usually care, but check your institution)
   - Secondary use: Data collected for care, now wanted for AI training (needs new consent)
   - Aggregate analytics: Usually acceptable if truly anonymized, but "anonymized" is harder than you think

3. **Write a 200-word reflection:** Think of a situation in your clinical experience or education where health data was collected. Was the purpose clear? Was consent obtained? What would you do differently now?

## Artifacts

You must produce **all 4 artifacts** to complete this skill:

1. **Data Classification Exercise** — Correct classification of all 5 examples from Step 1 with explanation of why the last example is problematic
2. **Country Data Protection Summary** — 1-paragraph summary of your country's data protection landscape (law name, year, enforcing body, or absence of law and applicable frameworks)
3. **Informed Consent Form** — 1-page consent form for the medical school digitalization scenario, including all 7 required elements
4. **Violation Analysis + Reflection** — All 5 scenarios analyzed (violation identified, correct approach, potential harm) PLUS 200-word reflection on data use in your own experience

## Assessment Criteria

| Criterion | Excellent (3) | Adequate (2) | Needs Improvement (1) |
|-----------|--------------|-------------|----------------------|
| **Data Classification** | All 5 correct with nuanced explanation of re-identification risk | 4/5 correct | 3 or fewer correct |
| **Country Research** | Specific law cited, year, enforcing body, strengths/gaps noted | Law identified but details sparse | No research or incorrect information |
| **Consent Form** | All 7 elements present, accessible language, clear opt-in/opt-out | Most elements present, some unclear | Missing multiple elements or inaccessible language |
| **Violation Analysis** | All 5 violations correctly identified with specific remedies and realistic harms | 4/5 identified, some remedies vague | 3 or fewer identified |

**Passing score:** 8/12 (at least "Adequate" on all criteria)

## Common Mistakes

1. **Confusing de-identified with anonymized** — In small populations (rural clinics, rare diseases), "de-identified" data can still identify someone. True anonymization is harder than removing names.
2. **WhatsApp as clinical tool** — Widely used, rarely compliant. If your institution uses WhatsApp for clinical communication, that's a policy discussion worth having.
3. **Assuming consent is one-time** — Consent for clinical care does not automatically extend to research, AI training, or publication.
4. **Ignoring paper records** — Data protection applies to paper too. An unlocked filing cabinet is a data breach waiting to happen.
5. **"We've always done it this way"** — Historical practice is not legal justification. Many common health data practices violate data protection principles.

## Related Skills

- **Prerequisite:** [Digital Literacy](../digital-literacy/SKILL.md) — Basic digital skills foundation
- **Parallel:** [Gen AI Basics for Health](../gen-ai-basics-for-health/SKILL.md) — Understanding AI privacy implications
- **Leads to:** [FHIR Resource Basics](../../digital-health-foundations/fhir-resource-basics/SKILL.md) — Structured health data standards
- **Leads to:** [Digitalize Paper Records](../../digital-health-foundations/digitalize-paper-records/SKILL.md) — Apply data protection when digitizing records
- **Leads to:** [Regulatory Landscape Analysis](../../regulatory/regulatory-landscape-analysis/SKILL.md) — Map the full regulatory environment

## References

1. WHO (2021). Global Strategy on Digital Health 2020-2025. World Health Organization.
2. African Union (2014). Convention on Cyber Security and Personal Data Protection (Malabo Convention).
3. UNCTAD (2024). Data Protection and Privacy Legislation Worldwide. https://unctad.org/page/data-protection-and-privacy-legislation-worldwide
4. Vayena, E. et al. (2018). Machine learning in medicine: Addressing ethical challenges. *PLoS Medicine*, 15(11), e1002689.
5. Abouelmehdi, K. et al. (2018). Big healthcare data: preserving security and privacy. *Journal of Big Data*, 5(1), 1-18.
6. El Emam, K. et al. (2011). A systematic review of re-identification attacks on health data. *PLoS ONE*, 6(12), e28071.
