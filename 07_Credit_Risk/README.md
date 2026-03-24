# Credit risk & PD (logit)

> **Prawdopodobieństwo defaultu (PD)** w ramce logistycznej; silnik `sklearn` w `src/model_engine.py` oraz prosty dashboard Streamlit.

| Plik | Rola |
|------|------|
| [`app.py`](app.py) | Suwaki (FICO, DTI), ilustracyjne PD |
| [`src/model_engine.py`](src/model_engine.py) | `ProbabilityOfDefaultModel`, zapis `joblib` |

## Teoria

Logit:

$$
\ln\frac{p}{1-p} = \beta_0 + \sum_i \beta_i x_i, \qquad
p = \frac{1}{1 + e^{-z}}
$$

**Dyskryminacja:** AUC, **Gini** $= 2\cdot\mathrm{AUC} - 1$.

## Uruchomienie

```bash
cd 07_Credit_Risk
pip install streamlit numpy scikit-learn joblib
streamlit run app.py
```

Trening: `fit(X, y)` w osobnym pipeline po przygotowaniu macierzy cech.

## Powiązania

VaR rynkowy: [`03_FX_And_Market_Risk`](../03_FX_And_Market_Risk) — szerszy obraz ALM (EAD/LGD poza tym repozytorium).
