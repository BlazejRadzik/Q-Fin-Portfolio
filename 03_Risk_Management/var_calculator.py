import pandas as pd
import numpy as np
from scipy.stats import norm
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from config import DB_CONFIG

class VaRCalculator:
    """
    Calculates Parametric Value at Risk (VaR) based on historical SQL data.
    """
    def __init__(self):
        safe_password = quote_plus(DB_CONFIG['password'])
        db_url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{safe_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        self.engine = create_engine(db_url)

    def calculate_parametric_var(self, currency_pair: str = 'EUR/PLN', confidence_level: float = 0.95, exposure: float = 1_000_000):
        """
        Calculates daily VaR using the Variance-Covariance (Parametric) method.
        """
        print(f"--- Risk Analysis for {currency_pair} ---")
        
        query = f"SELECT date, rate_mid FROM market_data WHERE currency_pair = '{currency_pair}' ORDER BY date"
        df = pd.read_sql(query, self.engine)
        
        if df.empty:
            print(f"No data found for {currency_pair}! Please run 'fx_data_loader.py' first.\n")
            return

        df['returns'] = np.log(df['rate_mid'] / df['rate_mid'].shift(1))
        df = df.dropna()
        
        volatility = df['returns'].std()
        
        z_score = norm.ppf(confidence_level) 
        
        var_pct = z_score * volatility
        var_value = exposure * var_pct
        
        print(f"Analyzed trading sessions : {len(df)}")
        print(f"Daily VaR ({confidence_level:.0%})      : {var_pct:.4%}")
        print(f"Potential Loss Exposure   : {var_value:,.2f} PLN (on {exposure:,.0f} PLN portfolio)\n")

if __name__ == "__main__":
    calculator = VaRCalculator()
    calculator.calculate_parametric_var('EUR/PLN', confidence_level=0.95, exposure=1_000_000)
    calculator.calculate_parametric_var('USD/PLN', confidence_level=0.99, exposure=1_000_000)
