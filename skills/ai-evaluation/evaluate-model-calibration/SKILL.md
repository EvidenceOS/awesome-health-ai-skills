---
name: evaluate-model-calibration
description: Assess whether a health AI model's predicted probabilities match observed outcomes
category: ai-evaluation
raigh_tier: tier-1
difficulty: intermediate
estimated_time: "4 hours"
prerequisites: [run-tripod-ai-checklist]
tags: [calibration, ece, brier-score, reliability-diagram, clinical-trust]
evidence_basis: "https://doi.org/10.1145/1102351.1102430"
version: "1.0"
---

# Evaluate Model Calibration

## Purpose

A model that says "80% chance of disease" should be correct about 80% of the time. That's calibration. Most health AI papers report discrimination (AUROC) but ignore calibration — yet calibration determines whether clinicians can trust the model's probability estimates for decision-making. This skill teaches you to assess and visualize calibration, a critical gap in health AI evaluation.

## Learning Objectives

1. Explain the difference between discrimination and calibration
2. Create a reliability diagram (calibration plot) from model predictions
3. Calculate Expected Calibration Error (ECE) and Brier Score
4. Interpret calibration in clinical context (when does miscalibration cause harm?)
5. Recommend recalibration strategies when needed

## Context

Imagine an ER triage AI that predicts "90% probability of severe TBI." If the model is poorly calibrated, that 90% might really mean 50%. The clinician who trusts that 90% may order unnecessary interventions — or worse, a model that says "10%" when the true risk is 40% may lead to missed diagnoses. Calibration is the bridge between model output and clinical trust.

## Steps

### Step 1: Understand the Concepts

| Concept | Question It Answers |
|---|---|
| **Discrimination** (AUROC) | Can the model rank patients by risk? (higher risk patients get higher scores) |
| **Calibration** | Are the predicted probabilities accurate? (80% prediction = 80% observed rate) |
| **Clinical Utility** (DCA) | Does using the model lead to better decisions than alternatives? |

A model can have perfect discrimination (AUROC=1.0) but terrible calibration (all predictions are 0.99 or 0.01). And vice versa.

### Step 2: Create a Reliability Diagram

Using provided predictions and outcomes (or your own dataset):

```python
import numpy as np
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

# Sample: model predictions and true outcomes
y_true = [...]   # 0 or 1
y_pred = [...]   # predicted probabilities (0.0 to 1.0)

# Create calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_pred, n_bins=10)

# Plot
plt.plot(prob_pred, prob_true, marker='o', label='Model')
plt.plot([0, 1], [0, 1], linestyle='--', label='Perfect calibration')
plt.xlabel('Mean predicted probability')
plt.ylabel('Observed frequency')
plt.title('Reliability Diagram')
plt.legend()
plt.savefig('calibration_plot.png')
```

### Step 3: Calculate ECE and Brier Score

```python
from sklearn.metrics import brier_score_loss

# Brier Score (lower is better, 0 is perfect)
brier = brier_score_loss(y_true, y_pred)

# Expected Calibration Error (lower is better)
def expected_calibration_error(y_true, y_pred, n_bins=10):
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0
    for i in range(n_bins):
        mask = (y_pred >= bins[i]) & (y_pred < bins[i+1])
        if mask.sum() > 0:
            bin_acc = y_true[mask].mean()
            bin_conf = y_pred[mask].mean()
            ece += mask.sum() / len(y_true) * abs(bin_acc - bin_conf)
    return ece

ece = expected_calibration_error(np.array(y_true), np.array(y_pred))
```

### Step 4: Interpret Clinically

For your model, answer:
- **Where is the model over-confident?** (predicts high but observed frequency is lower)
- **Where is the model under-confident?** (predicts low but observed frequency is higher)
- **At what probability thresholds does this matter clinically?** (e.g., the 15% threshold for CT scanning in TBI)
- **What's the clinical harm of miscalibration at this threshold?** (missed scans vs unnecessary scans)

### Step 5: Recalibration Options

If calibration is poor, common fixes:
1. **Platt Scaling** — Fit a logistic regression on model outputs
2. **Isotonic Regression** — Non-parametric calibration mapping
3. **Temperature Scaling** — Single parameter adjustment (common for neural networks)

Recalibrate on a held-out calibration set, never on the test set.

## Artifacts

1. **Reliability Diagram** — Calibration plot for one health AI model (from data or literature)
2. **ECE and Brier Score Calculation** — Code + results with interpretation
3. **Clinical Interpretation** — 1-page memo explaining what the calibration means for clinical decision-making at specific thresholds
4. **Recalibration Recommendation** — If needed, which method and why

## Assessment Criteria

| Criterion | Meets Standard | Below Standard |
|---|---|---|
| Reliability diagram | Correctly plotted with reference line | Missing reference line or incorrect binning |
| ECE calculation | Correct implementation, reasonable bin count | Wrong formula or interpretation |
| Clinical interpretation | Links calibration to specific clinical decisions | Generic interpretation without clinical context |
| Recalibration | Appropriate method recommended with justification | No recalibration plan for poorly calibrated model |

## Common Mistakes

- Using too few bins (< 5) or too many bins (> 20) for the reliability diagram
- Confusing calibration with discrimination — a well-calibrated model can still have mediocre AUROC
- Recalibrating on the test set (data leakage — always use a separate calibration set)
- Ignoring calibration because "the AUROC is high" — a common and dangerous practice in health AI

## Related Skills

- `run-tripod-ai-checklist` — Item 13a specifically addresses calibration reporting
- `decision-curve-analysis` — Clinical utility assessment that accounts for calibration
- `fairness-audit` — Calibration may differ across demographic subgroups
- `model-card-generator` — Include calibration metrics in model documentation

## References

- Niculescu-Mizil & Caruana (2005). Predicting Good Probabilities: https://doi.org/10.1145/1102351.1102430
- Van Calster et al. (2019). Calibration: the Achilles heel of predictive analytics: https://doi.org/10.1186/s12916-019-1466-7
- sklearn Calibration Guide: https://scikit-learn.org/stable/modules/calibration.html
