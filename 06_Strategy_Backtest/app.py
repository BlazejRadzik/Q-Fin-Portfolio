import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data_loader import load_ohlcv
from src.engine import BacktestEngine
from src.indicators import apply_exponential_averages

st.set_page_config(page_title="EMA Crossover Backtest", layout="wide")
st.title("Backtest strategii EMA")

symbol = st.sidebar.text_input("Ticker", value="SPY")
start = st.sidebar.date_input("Początek", value=pd.Timestamp("2018-01-01"))
fast_p = st.sidebar.slider("Okres EMA szybkiej", 5, 50, 12)
slow_p = st.sidebar.slider("Okres EMA wolnej", 10, 200, 26)
rf = st.sidebar.slider("Roczna stopa wolna od ryzyka (%)", 0.0, 8.0, 2.0) / 100.0

if slow_p <= fast_p:
    st.sidebar.warning("Wolna EMA musi być większa od szybkiej.")

run = st.sidebar.button("Uruchom backtest", use_container_width=True)

if run and slow_p > fast_p:
    df = load_ohlcv(symbol, start=str(start.date()))
    if df.empty or "Close" not in df.columns:
        st.error("Brak danych OHLCV dla podanego tickera i zakresu.")
    else:
        sig = apply_exponential_averages(df, fast_p, slow_p)
        eng = BacktestEngine(sig)
        eq = eng.equity_curve(sig["Close"], sig["Signal"])
        m = eng.metrics(eq, risk_free_annual=rf)
        bench = (df["Close"] / df["Close"].iloc[0]) * 100_000.0

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Zwrot całkowity", f"{m['total_return']:.2%}")
        c2.metric("CAGR", f"{m['cagr']:.2%}")
        c3.metric("Sharpe (roczny)", f"{m['sharpe']:.2f}")
        c4.metric("Max drawdown", f"{m['max_drawdown']:.2%}")

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=eq.index, y=eq.values, name="Strategia", line=dict(width=2))
        )
        fig.add_trace(
            go.Scatter(
                x=bench.index,
                y=bench.values,
                name="Buy & hold",
                line=dict(width=1, dash="dot"),
            )
        )
        fig.update_layout(
            height=480,
            legend=dict(orientation="h"),
            yaxis_title="Wartość (jednostki początkowe)",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Ostatnie sygnały")
        tail = sig[
            ["Close", "EMA_Fast", "EMA_Slow", "Signal", "Trade_Action"]
        ].tail(25)
        st.dataframe(
            tail.style.format(
                {
                    "Close": "{:.2f}",
                    "EMA_Fast": "{:.2f}",
                    "EMA_Slow": "{:.2f}",
                    "Signal": "{:.0f}",
                    "Trade_Action": "{:.0f}",
                }
            )
        )
