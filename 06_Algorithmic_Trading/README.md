## Cel modułu

**Backtest** przecięcia dwóch **EMA** na OHLCV; metryki: zwrot, CAGR, Sharpe, max drawdown.

## Teoria w skrócie

- \(\text{EMA}_t = \alpha P_t + (1-\alpha)\text{EMA}_{t-1}\), \(\alpha = 2/(n+1)\).
- Pozycja \( \in \{0,1\} \), realizacja zwrotu z jednodniowym opóźnieniem sygnału.

## Zawartość

| Plik | Rola |
|------|------|
| `src/data_loader.py` | `yfinance` + cache **cachetools** (TTL). |
| `src/indicators.py` | EMA i sygnał crossover. |
| `src/engine.py` | `BacktestEngine`. |
| `app.py` | Streamlit + Plotly (strategia vs buy-and-hold). |

## Uruchomienie

```bash
cd 06_Algorithmic_Trading
pip install streamlit pandas numpy yfinance plotly cachetools
streamlit run app.py
```

## Powiązania w portfolio

Alternatywa dla alokacji z `01`; \(\sigma\) rynkowa vs `02`.
