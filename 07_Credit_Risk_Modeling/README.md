## Cel modułu

**Ryzyko kredytowe:** estymacja **PD** (logit / logistyczna regresja) oraz prosty dashboard Streamlit do scorecardu.

## Teoria w skrócie

- Logit: \(\ln\frac{p}{1-p} = \beta_0 + \sum_i \beta_i x_i\), \(p = \frac{1}{1+e^{-z}}\).
- **Dyskryminacja:** AUC, **Gini** \(= 2\cdot\mathrm{AUC} - 1\).

## Zawartość

| Plik | Rola |
|------|------|
| `app.py` | Interfejs z suwakami (FICO, DTI) i ilustracyjnym PD. |
| `src/model_engine.py` | `ProbabilityOfDefaultModel` (`sklearn`, zapis `joblib`). |

## Uruchomienie

```bash
cd 07_Credit_Risk_Modeling
pip install streamlit numpy scikit-learn joblib
streamlit run app.py
```

Trening: `fit(X, y)` na macierzy cech w osobnym pipeline.

## Powiązania w portfolio

PD × ekspozycja vs **VaR rynkowy** (`03`) w szerszym obrazie ALM (EAD/LGD poza tym repo).
