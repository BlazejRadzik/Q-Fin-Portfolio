# Strategy backtest (EMA crossover)

> Backtest reguły **dwóch EMA** na OHLCV: krzywa kapitału, Sharpe, CAGR, max drawdown; dane z `yfinance` z cache (**cachetools**).

| Plik | Rola |
|------|------|
| [`src/data_loader.py`](src/data_loader.py) | Pobranie OHLCV + TTL cache |
| [`src/indicators.py`](src/indicators.py) | EMA, sygnał crossover |
| [`src/engine.py`](src/engine.py) | `BacktestEngine` |
| [`app.py`](app.py) | Streamlit + Plotly (strategia vs buy-and-hold) |

## Teoria

EMA z okresem $n$: $\alpha = 2/(n+1)$,

$$
\mathrm{EMA}_t = \alpha P_t + (1-\alpha)\,\mathrm{EMA}_{t-1}
$$

Pozycja długa gdy EMA szybka $>$ EMA wolna; realizacja z jednodniowym opóźnieniem sygnału.

## Uruchomienie

```bash
cd 06_Strategy_Backtest
pip install streamlit pandas numpy yfinance plotly cachetools
streamlit run app.py
```

## Powiązania

- Alokacja mean–variance: [`01_Portfolio_Optimization`](../01_Portfolio_Optimization)
- Zmienność rynkowa vs wycena: [`02_Options_Pricing`](../02_Options_Pricing)
