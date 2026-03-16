import pandas as pd
import numpy as np

def apply_exponential_averages(df: pd.DataFrame, fast_period: int, slow_period: int):
    """Calculates Exponential Moving Averages (EMA) and crossover signals."""
    df['EMA_Fast'] = df['Close'].ewm(span=fast_period, adjust=False).mean()
    df['EMA_Slow'] = df['Close'].ewm(span=slow_period, adjust=False).mean()
    
    df['Signal'] = 0.0
    df['Signal'] = np.where(df['EMA_Fast'] > df['EMA_Slow'], 1.0, 0.0)
    
    df['Trade_Action'] = df['Signal'].diff()
    return df
