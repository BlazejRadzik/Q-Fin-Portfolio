import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class DataProcessor:
    """Handles ETL and Feature Engineering for Credit Scoring."""
    def __init__(self):
        self.scaler = StandardScaler()

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        # Debt-to-Income Ratio (DTI) - A fundamental Quant metric
        df['DTI'] = df['monthly_debt'] / df['monthly_income'].replace(0, 1)
        
        # Utilization of Credit Lines
        df['Credit_Utilization'] = df['outstanding_balance'] / df['total_credit_limit'].replace(0, 1)
        
        # Log transformation for skewed financial data
        df['Log_Income'] = np.log1p(df['monthly_income'])
        
        return df

    def prepare_datasets(self, df: pd.DataFrame, target: str):
        X = df.drop(columns=[target])
        y = df[target]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )
        
        # Standardizing features for Logistic Regression convergence
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test