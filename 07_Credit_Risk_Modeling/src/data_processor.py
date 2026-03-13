import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    """Handles Feature Engineering and Scaling for Credit Risk data."""
    def __init__(self):
        self.scaler = StandardScaler()

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        # DTI - Debt to Income Ratio
        df['DTI'] = df['monthly_debt'] / df['monthly_income'].replace(0, 1)
        
        # Credit Utilization Ratio
        df['Utilization'] = df['outstanding_balance'] / df['credit_limit'].replace(0, 1)
        
        return df