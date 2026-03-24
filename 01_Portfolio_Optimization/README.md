# Portfolio optimization & historical VaR

> Streamlit + **PyPortfolioOpt**: front efektywny Markowitza, optymalne wagi (Sharpe / min. wariancja / target return) oraz **historyczny VaR** portfela na szeregach cen z `yfinance`.

| Plik | Rola |
|------|------|
| [`portfolio_optimizer_app.py`](portfolio_optimizer_app.py) | `EfficientFrontier`, wizualizacja wag, VaR z empirycznego rozkładu zwrotów |

## Teoria

**Markowitz (mean–variance):** przy macierzy kowariancji $\Sigma$ i wektorze oczekiwanych zwrotów $\boldsymbol{\mu}$ minimalizuje się wariancję portfela

$$
\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \mathbf{w}
$$

przy typowych ograniczeniach $\sum_i w_i = 1$ oraz (w zależności od trybu) $\mathbf{w}^\top \boldsymbol{\mu}$ lub maksymalizacji Sharpe’a.

**VaR historyczny:** dla poziomu $\alpha$ (np. $5\%$) jest to kwantyl rozkładu zwrotów portfela $r_p = \sum_i w_i r_i$:

$$
\mathrm{VaR}^{\mathrm{hist}}_\alpha = Q_\alpha(r_p)
$$

## Uruchomienie

```bash
cd 01_Portfolio_Optimization
pip install streamlit yfinance pandas plotly PyPortfolioOpt numpy
streamlit run portfolio_optimizer_app.py
```

## Powiązania

- Parametryczny VaR FX: [`03_FX_And_Market_Risk`](../03_FX_And_Market_Risk)
- Backtest strategii (EMA): [`06_Strategy_Backtest`](../06_Strategy_Backtest)
