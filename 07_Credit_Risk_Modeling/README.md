# 🏦 Credit Risk Modeling (PD Scorecard)

This module implements a professional **Credit Scoring Pipeline** to estimate the **Probability of Default (PD)** using a modular Logistic Regression framework.

## 🧮 Theoretical Background

### The Logistic Regression Framework
The model estimates the log-odds of a binary default event based on applicant attributes:
$$\ln\left(\frac{P(Default)}{1 - P(Default)}\right) = \beta_0 + \sum \beta_i X_i$$

The final **PD** is calculated using the Sigmoid function:
$$PD = \frac{1}{1 + e^{-z}}$$

### Performance Metric: Gini Coefficient
We measure the model's discriminatory power using the **Gini Coefficient**, derived from the Area Under the Curve (AUC):
$$Gini = 2 \times AUC - 1$$

## 📂 Modular Structure
* `src/data_processor.py`: Feature engineering (DTI, Utilization).
* `src/model_engine.py`: Logistic engine for logit estimation.
* `src/risk_metrics.py`: Statistical validation tools.
* `app.py`: Interactive **Risk Underwriting Dashboard**.