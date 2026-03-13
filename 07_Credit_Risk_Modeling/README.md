```markdown
# 🏦 Institutional Credit Risk Intelligence (PD Model)

This module implements a professional **Credit Scoring Engine** designed to estimate the **Probability of Default (PD)** for banking portfolios. The system utilizes a modular architecture to separate data preprocessing, statistical modeling, and risk validation.

## 🧮 Theoretical Framework

### The Logistic PD Model
The model estimates the log-odds of default using a **Logistic Regression** framework. The relationship between input risk factors and the binary outcome is modeled as:

$$\ln\left(\frac{P(Default)}{1 - P(Default)}\right) = \beta_0 + \sum_{i=1}^{n} \beta_i X_i$$

The final **PD** is obtained by applying the Sigmoid function to the logit $z$:
$$PD = \frac{1}{1 + e^{-z}}$$

### Model Discrimination: The Gini Coefficient
To validate the model's ability to rank-order risk, we calculate the **Gini Coefficient** derived from the Area Under the Curve (AUC):
$$Gini = 2 \times AUC - 1$$

## 📂 Architecture
* `src/data_processor.py`: Handles Feature Engineering (DTI, Credit Utilization).
* `src/model_engine.py`: Logistic engine for logit estimation.
* `src/risk_metrics.py`: Validation suite for Gini scores.
* `app.py`: Streamlit-based **Risk Underwriting Terminal**.