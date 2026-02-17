---
name: gen-ai-basics-for-health
description: Understand what generative AI is, use it safely in health contexts, recognize hallucinations, and protect patient privacy
category: pre-mooc
raigh_tier: MOOC
difficulty: beginner
estimated_time: "3 hours"
prerequisites: [digital-literacy]
tags: [generative-ai, chatgpt, claude, health-ai, hallucinations, privacy, responsible-ai]
evidence_basis: "WHO Guidance on Ethics and Governance of AI for Health (2021); Elements of AI (University of Helsinki)"
version: "1.0"
---

# Gen AI Basics for Health

## Purpose

Generative AI (ChatGPT, Claude, Gemini, and others) is transforming how health professionals access information, draft documents, and support clinical reasoning. Yet most health education programs offer zero training on these tools. This creates two risks: (1) professionals who reject AI entirely and fall behind, and (2) professionals who use AI blindly without understanding its limitations. This skill teaches the responsible middle path — using Gen AI as a powerful assistant while understanding exactly where it fails.

## Learning Objectives

After completing this skill, you will be able to:

1. Explain what generative AI is and how large language models work (conceptually)
2. Use a Gen AI tool (ChatGPT, Claude, or Gemini) to complete a health-related task
3. Identify at least 3 types of AI hallucinations in health contexts
4. Apply the VERIFY framework to fact-check AI outputs
5. Explain why patient data must never be entered into public AI tools
6. Articulate the difference between AI as a tool vs AI as a decision-maker

## Context

Inspired by the University of Helsinki's "Elements of AI" (2M+ enrollments, 26 languages), this skill is the "Elements of Health AI" equivalent — the first exposure to AI for health professionals anywhere in the world.

This skill is for anyone in health — doctors, nurses, pharmacists, administrators, community health workers, students. No technical background required. You need only a smartphone or computer with internet access.

## Steps

### Step 1: What Is Generative AI? (30 minutes)

1. **Read** the provided brief (or use the Elements of AI Chapter 1 as reference)
2. **Key concepts to understand:**
   - AI = pattern recognition from data (not thinking or understanding)
   - Large Language Models (LLMs) = predict the next word based on training data
   - "Generative" = creates new text, not retrieves existing text
   - Training data cutoff = the model doesn't know what happened after training
   - Temperature/creativity = models can be more or less creative (and more or less accurate)
3. **Write a 5-sentence summary** of how LLMs work in your own words. Avoid jargon.

### Step 2: Your First Health AI Interaction (30 minutes)

1. **Open** a free Gen AI tool: ChatGPT (chat.openai.com), Claude (claude.ai), or Gemini (gemini.google.com)
2. **Complete 3 tasks** using the AI tool:

   **Task A — Information synthesis:**
   > "Summarize the 5 most common causes of maternal mortality in Sub-Saharan Africa, with approximate percentages, and cite sources."

   **Task B — Clinical reasoning support:**
   > "A 45-year-old male presents with sudden onset headache, neck stiffness, and photophobia. What is the differential diagnosis and what initial investigations should be ordered?"

   **Task C — Document drafting:**
   > "Draft a 200-word patient information leaflet about managing Type 2 diabetes through diet, appropriate for a patient with primary school education in a rural African setting."

3. **For each response**, note:
   - Was it helpful? (1-5)
   - Did anything seem wrong or suspicious?
   - Would you trust this without checking?

### Step 3: The Hallucination Problem (45 minutes)

1. **What is a hallucination?** When AI generates plausible-sounding but factually wrong information. In health, hallucinations can be dangerous.

2. **Find 3 hallucinations.** Ask the AI tool:
   > "What clinical trials have been conducted on [specific drug] for [specific condition] in [specific African country]?"

   Choose a narrow, specific query. The AI will likely generate trial names, dates, and results that do not exist. Try to verify each claim.

3. **Types of health AI hallucinations:**
   - **Citation hallucination** — invents journal articles with realistic DOIs
   - **Dosage hallucination** — generates plausible but incorrect drug dosages
   - **Guideline hallucination** — references guidelines that don't exist or misquotes them
   - **Epidemiology hallucination** — fabricates statistics with false precision
   - **Clinical trial hallucination** — invents trials with specific sample sizes and outcomes

4. **Document your 3 hallucinations** with:
   - The prompt you used
   - The AI's response
   - What was wrong (with evidence)
   - What the correct information is (with source)

### Step 4: The VERIFY Framework (30 minutes)

Apply this framework to EVERY AI output in a health context:

| Step | Action | Question to Ask |
|------|--------|----------------|
| **V** — Validate source | Check if cited papers/guidelines exist | Does this reference actually exist? |
| **E** — Examine specifics | Verify numbers, dosages, percentages | Are these numbers correct and current? |
| **R** — Review reasoning | Check if the logic chain is sound | Does the conclusion follow from the evidence? |
| **I** — Identify bias | Consider training data limitations | Is this answer biased toward high-income country settings? |
| **F** — Find alternatives | Compare with at least one other source | Does UpToDate / WHO / local guidelines agree? |
| **Y** — Your judgment | Apply clinical/professional judgment | Does this match my experience and context? |

**Exercise:** Apply the VERIFY framework to the 3 AI responses from Step 2. Fill in the table for each.

### Step 5: Privacy and Patient Data (30 minutes)

1. **The cardinal rule:** NEVER enter patient-identifiable data into public AI tools (ChatGPT, Claude, Gemini). This includes:
   - Names, dates of birth, ID numbers
   - Specific clinical histories that could identify someone
   - Hospital record numbers
   - Photos of patients (even with consent)

2. **Why?** Public AI tools may:
   - Store your inputs for training (opt-out varies by tool)
   - Be accessed by the AI company's employees
   - Leak data through future model outputs
   - Violate GDPR, local data protection acts, and HIPAA

3. **Safe alternatives:**
   - De-identify before querying: "A 45-year-old male..." not "Mr. Ngum from Kumba..."
   - Use approved institutional AI tools when available
   - Use local/on-premise models for sensitive data
   - Ask about general patterns, not specific patients

4. **Write a 1-page privacy policy** for AI use in your institution or practice. Include:
   - What data can be entered into AI tools
   - What data must never be entered
   - How to de-identify clinical scenarios
   - Who to contact if a data breach occurs

### Step 6: AI as Tool vs Decision-Maker (15 minutes)

1. **The spectrum:**
   ```
   AI as search engine ──── AI as assistant ──── AI as advisor ──── AI as decision-maker
   (acceptable)              (acceptable)         (with caution)     (NOT acceptable in health)
   ```

2. **Write a reflection (300 words):** "How could AI help in my work, and where should it never replace human judgment?" Include at least:
   - One task where AI would save you time
   - One task where AI could be dangerous
   - Your personal rule for when to trust AI output

## Artifacts

You must produce **all 5 artifacts** to complete this skill:

1. **LLM Summary** — 5-sentence explanation of how large language models work, in your own words, jargon-free
2. **3 AI Interaction Logs** — Screenshots or transcripts of your 3 health AI tasks (information synthesis, clinical reasoning, document drafting) with helpfulness ratings and suspicion notes
3. **Hallucination Hunt Report** — 3 documented hallucinations with: prompt used, AI response, what was wrong, correct answer with source
4. **VERIFY Analysis** — Completed VERIFY framework table applied to your 3 AI responses from Step 2
5. **AI Privacy Policy + Reflection** — 1-page institutional AI privacy policy draft PLUS 300-word reflection on AI as tool vs decision-maker

## Assessment Criteria

| Criterion | Excellent (3) | Adequate (2) | Needs Improvement (1) |
|-----------|--------------|-------------|----------------------|
| **LLM Understanding** | Accurate, jargon-free, captures key concepts (prediction, not understanding) | Mostly accurate, some confusion | Fundamental misconceptions |
| **AI Interaction** | All 3 tasks completed with thoughtful ratings and specific observations | Tasks completed but observations shallow | Missing tasks or no critical observation |
| **Hallucination Detection** | 3 hallucinations documented with specific evidence of incorrectness and correct answers | 2 hallucinations found, some evidence | Fewer than 2, or evidence missing |
| **VERIFY Application** | All 6 steps applied to all 3 responses with specific findings | Framework applied but some steps skipped | Incomplete or superficial application |
| **Privacy + Reflection** | Comprehensive policy with specific rules; reflection shows nuanced thinking about AI limits | Basic policy; reflection present | Policy missing key elements; reflection superficial |

**Passing score:** 10/15 (at least "Adequate" on all criteria)

## Common Mistakes

1. **Assuming AI "knows" things** — LLMs predict probable text, they don't have knowledge. A confident-sounding answer is not necessarily correct.
2. **Trusting citations without checking** — AI frequently invents realistic-looking journal references. Always verify DOIs.
3. **Entering patient data** — Even "just to ask a question." Once data is submitted, you cannot retrieve it.
4. **Dismissing AI entirely** — The solution is not to avoid AI but to use it critically. The tool is powerful when used correctly.
5. **Using AI for diagnosis** — In its current form, Gen AI is not approved as a diagnostic tool. Use it for education, synthesis, and drafting — not for making clinical decisions.
6. **Forgetting context bias** — Most AI training data comes from high-income countries. Drug availability, clinical guidelines, and disease patterns may not match your setting.

## Related Skills

- **Prerequisite:** [Digital Literacy](../digital-literacy/SKILL.md) — Basic digital skills needed to access AI tools
- **Next:** [Health Data Awareness](../health-data-awareness/SKILL.md) — Deeper dive into health data rights and responsibilities
- **Leads to:** [TRIPOD+AI Checklist](../../ai-evaluation/run-tripod-ai-checklist/SKILL.md) — Evaluate health AI studies using the gold standard
- **Leads to:** [Model Calibration](../../ai-evaluation/evaluate-model-calibration/SKILL.md) — Assess AI model reliability

## References

1. WHO (2021). Ethics and Governance of Artificial Intelligence for Health. World Health Organization.
2. University of Helsinki & MinnaLearn (2018). Elements of AI. https://www.elementsofai.com/
3. Ji, Z. et al. (2023). Survey of Hallucination in Natural Language Generation. *ACM Computing Surveys*, 55(12), 1-38.
4. Thirunavukarasu, A.J. et al. (2023). Large language models in medicine. *Nature Medicine*, 29, 1930-1940.
5. Meskó, B. & Topol, E.J. (2023). The imperative for regulatory oversight of large language models in healthcare. *npj Digital Medicine*, 6, 120.
6. Omiye, J.A. et al. (2024). Large language models propagate race-based medicine. *npj Digital Medicine*, 7, 44.
