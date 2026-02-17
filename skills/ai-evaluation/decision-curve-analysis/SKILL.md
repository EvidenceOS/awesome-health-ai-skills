---
name: decision-curve-analysis
description: Perform Decision Curve Analysis to determine if a health AI model improves clinical decisions
category: ai-evaluation
raigh_tier: tier-1
difficulty: intermediate
estimated_time: "3 hours"
prerequisites: [evaluate-model-calibration]
tags: [dca, net-benefit, clinical-utility, threshold, decision-making]
evidence_basis: "https://doi.org/10.1177/0272989X06295361"
version: "1.0"
---

# Decision Curve Analysis (DCA)

## Purpose

AUROC tells you the model can discriminate. Calibration tells you the probabilities are trustworthy. But neither answers the most important question: **does using this model lead to better clinical decisions?** Decision Curve Analysis (DCA) answers this by comparing the net benefit of model-guided decisions versus treating all patients or treating none.

## Learning Objectives

1. Explain net benefit and threshold probability in clinical terms
2. Perform DCA using R or Python
3. Interpret a decision curve (when does the model add value?)
4. Identify the clinically relevant threshold range
5. Compare multiple models and strategies on the same decision curve

## Context

A TBI screening model predicts probability of intracranial hemorrhage. Should we scan everyone (treat-all)? No one without the model (treat-none)? Or use the model to decide? DCA plots net benefit across threshold probabilities, showing exactly where the model adds value. This is the missing step in most health AI evaluations.

## Steps

### Step 1: Understand Net Benefit

Net Benefit at threshold pt:

```
NB = (True Positives / N) - (False Positives / N) × (pt / (1 - pt))
```

Where `pt / (1 - pt)` is the odds at the threshold — representing the relative harm of a false positive compared to missing a true positive.

At pt = 10%: treating a false positive is considered 1/9 as harmful as missing a true positive.
At pt = 50%: equal harm from false positive and false negative.

### Step 2: Run DCA in Python

```python
# pip install dcurves
from dcurves import dca, plot_graphs
import pandas as pd

# Load your data with true outcomes and model predictions
df = pd.DataFrame({
    'outcome': y_true,          # binary outcome
    'model_pred': y_pred,       # predicted probability
    'age_only': age_pred        # simpler comparison model
})

# Run DCA
results = dca(
    data=df,
    outcome='outcome',
    modelnames=['model_pred', 'age_only'],
    thresholds=np.arange(0, 0.5, 0.01)
)

# Plot
plot_graphs(
    plot_df=results,
    graph_type='net_benefit',
    y_limits=[-0.05, 0.3]
)
```

### Step 3: Interpret the Curve

Look for:
1. **Where does the model line sit above "Treat All" and "Treat None"?** → Model adds value in this threshold range
2. **Where does the model line dip below "Treat All"?** → Model is worse than just treating everyone
3. **Where do two models cross?** → One model is better below the crossing, the other above
4. **What's the clinically relevant threshold range?** → This depends on the clinical context

### Step 4: Clinical Threshold Mapping

For your specific clinical question, define:

| Parameter | Your Value |
|---|---|
| What is the "treatment"? | e.g., Order a CT scan |
| What's the harm of unnecessary treatment? | e.g., Radiation exposure, cost, time |
| What's the harm of missing the condition? | e.g., Missed intracranial hemorrhage |
| Reasonable threshold range | e.g., 2-20% (most clinicians would scan above 2% risk of hemorrhage) |

### Step 5: Write Clinical Recommendation

Based on DCA, recommend:
- At what threshold range should the model be used?
- Is the model better than simpler alternatives (age-only, treat-all)?
- What patient populations benefit most from model-guided decisions?

## Artifacts

1. **Decision Curve Plot** — DCA for one health AI model with treat-all and treat-none reference lines
2. **Threshold Analysis** — Table defining clinically relevant thresholds with justification
3. **Clinical Recommendation** — 1-page memo recommending whether and how to use the model for clinical decisions

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| DCA correctly computed | Net benefit formula correct, curves plotted | Incorrect formula or missing reference lines |
| Threshold range justified | Clinical reasoning for threshold selection | Arbitrary threshold selection |
| Interpretation | Identifies where model adds/subtracts value | Treats DCA as just another metric |
| Recommendation | Actionable clinical guidance | Generic or absent recommendation |

## Common Mistakes

- Choosing a threshold range without clinical justification (always ask: "at what risk would you act?")
- Forgetting to include both "Treat All" and "Treat None" reference lines
- Interpreting a small net benefit as clinically meaningful without considering the clinical context
- Running DCA on training data instead of validation data

## Related Skills

- `evaluate-model-calibration` — Calibration directly affects DCA results
- `run-tripod-ai-checklist` — Item 16 addresses clinical utility (DCA is the standard method)
- `evidence-chain-assessment` — DCA is Phase 3 (clinical validation) evidence

## References

- Vickers & Elkin (2006). Decision Curve Analysis: https://doi.org/10.1177/0272989X06295361
- Vickers et al. (2016). Net benefit approaches: https://doi.org/10.1136/bmj.i6
- dcurves Python package: https://github.com/ddsjoberg/dca-python
