import numpy as np
import pandas as pd


def apply_exponential_averages(
    df: pd.DataFrame, fast_period: int, slow_period: int
) -> pd.DataFrame:
    out = df.copy()
    out["EMA_Fast"] = out["Close"].ewm(span=fast_period, adjust=False).mean()
    out["EMA_Slow"] = out["Close"].ewm(span=slow_period, adjust=False).mean()
    out["Signal"] = np.where(out["EMA_Fast"] > out["EMA_Slow"], 1.0, 0.0)
    out["Trade_Action"] = out["Signal"].diff()
    return out
