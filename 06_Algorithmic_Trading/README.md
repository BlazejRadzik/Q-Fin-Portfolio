# 📈 Algorithmic Trading Backtester

An event-simulating backtester for crossover strategies. This module allows users to test the historical performance of Exponential Moving Averages (EMA) across various asset classes (Crypto, Stocks, FX).

## 🚀 Strategy: Dual EMA Crossover
The strategy generates a **BUY** signal when the Fast EMA crosses above the Slow EMA and a **SELL** (or Cash) signal when it crosses below.

## 💻 Quick Start
To launch the interactive backtester:
```bash
streamlit run app.py