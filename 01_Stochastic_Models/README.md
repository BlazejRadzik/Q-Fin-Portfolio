## Cel modułu

Warstwa **alokacji aktywów** (Modern Portfolio Theory) i prostych narzędzi opartych na szeregach cen: front efektywny Markowitza oraz **historyczny VaR** portfela w jednej aplikacji Streamlit.

## Teoria w skrócie

- **Model Markowitza:** minimalizacja \(\mathbf{w}^\top \Sigma \mathbf{w}\) przy ograniczeniach na \(\sum w_i\) i \(\mathbf{w}^\top \boldsymbol{\mu}\), albo maksymalizacja Sharpe’a.
- **Osiągalny front:** kombinacje ryzyko–zwrot przy ograniczeniach na długie pozycje.
- **VaR historyczny:** kwantyl empiryczny rozkładu zwrotów portfela (np. \(\alpha = 5\%\)).

## Zawartość

| Plik | Rola |
|------|------|
| `portfolio_optimizer_app.py` | Streamlit: `yfinance`, `EfficientFrontier` (PyPortfolioOpt), wykresy wag, VaR. |

## Uruchomienie

```bash
cd 01_Stochastic_Models
pip install streamlit yfinance pandas plotly PyPortfolioOpt numpy
streamlit run portfolio_optimizer_app.py
```

## Powiązania w portfolio

Wagi można zestawiać z **parametrycznym VaR FX** (`03_Risk_Management`) i z **backtestem** reguł technicznych (`06_Algorithmic_Trading`).
