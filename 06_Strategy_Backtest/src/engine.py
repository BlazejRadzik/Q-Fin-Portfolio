from __future__ import annotations

import numpy as np
import pandas as pd


class BacktestEngine:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def equity_curve(
        self, close: pd.Series, signal: pd.Series, initial: float = 100_000.0
    ) -> pd.Series:
        aligned = pd.DataFrame({"close": close, "signal": signal}).dropna()
        position = aligned["signal"].shift(1).fillna(0.0)
        ret = aligned["close"].pct_change().fillna(0.0)
        strat = position * ret
        growth = (1.0 + strat).cumprod()
        return initial * growth

    def metrics(
        self, equity: pd.Series, risk_free_annual: float = 0.02
    ) -> dict[str, float]:
        er = equity.pct_change().dropna()
        if len(er) < 2 or float(er.std()) == 0.0:
            return {
                "total_return": 0.0,
                "cagr": 0.0,
                "sharpe": 0.0,
                "max_drawdown": 0.0,
            }
        total_return = float(equity.iloc[-1] / equity.iloc[0] - 1.0)
        n = len(equity)
        years = n / 252.0 if n > 0 else 1.0
        cagr = (
            float(
                (equity.iloc[-1] / equity.iloc[0]) ** (1.0 / max(years, 1e-9)) - 1.0
            )
            if equity.iloc[0] > 0
            else 0.0
        )
        rf_daily = risk_free_annual / 252.0
        excess = er - rf_daily
        sharpe = float(np.sqrt(252.0) * excess.mean() / excess.std())
        cum = (1.0 + er).cumprod()
        peak = cum.cummax()
        mdd = float((cum / peak - 1.0).min())
        return {
            "total_return": total_return,
            "cagr": cagr,
            "sharpe": sharpe,
            "max_drawdown": mdd,
        }
