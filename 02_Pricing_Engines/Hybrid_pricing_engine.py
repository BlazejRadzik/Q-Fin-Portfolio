import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

class HybridPricingEngine:
    """
    A hybrid options pricing engine combining Black-Scholes analytical
    pricing with Monte Carlo simulations. Utilizes the Control Variate
    method for variance reduction.
    """
    def __init__(self, ticker: str, start_date: str, end_date: str, risk_free_rate: float, iterations: int = 100000):
        self.ticker = ticker
        self.risk_free_rate = risk_free_rate
        self.time_to_maturity = 0.25
        self.iterations = iterations

        data = yf.download(ticker, start=start_date, end=end_date)
        close_data = data['Close']
        
        if isinstance(close_data, pd.DataFrame):
            close_data = close_data.iloc[:, 0]

        self.spot_price = float(close_data.iloc[-1])
        self.strike_price = self.spot_price 
        
        log_returns = np.log(close_data / close_data.shift(1)).dropna()
        self.volatility = float(log_returns.std()) * np.sqrt(252)

    def run_full_analysis(self, scenario_name: str) -> tuple:
        """
        Executes the Black-Scholes pricing and Monte Carlo simulation.
        Returns a summary dictionary and a detailed DataFrame.
        """
        d1 = (np.log(self.spot_price / self.strike_price) + (self.risk_free_rate + 0.5 * self.volatility**2) * self.time_to_maturity) / (self.volatility * np.sqrt(self.time_to_maturity))
        d2 = d1 - self.volatility * np.sqrt(self.time_to_maturity)
        bs_price = self.spot_price * norm.cdf(d1) - self.strike_price * np.exp(-self.risk_free_rate * self.time_to_maturity) * norm.cdf(d2)

        np.random.seed(42)
        z = np.random.standard_normal(self.iterations)
        
        simulated_spot = self.spot_price * np.exp((self.risk_free_rate - 0.5 * self.volatility**2) * self.time_to_maturity + self.volatility * np.sqrt(self.time_to_maturity) * z)
        payoffs = np.maximum(simulated_spot - self.strike_price, 0)
        pv_payoffs = np.exp(-self.risk_free_rate * self.time_to_maturity) * payoffs
        
        hybrid_contributions = pv_payoffs + 1.0 * (bs_price - pv_payoffs)

        detailed_df = pd.DataFrame({
            'Scenario': scenario_name,
            'Sim_ID': np.arange(1, self.iterations + 1),
            'Start_Spot': self.spot_price,
            'Volatility': round(self.volatility, 4),
            'Risk_Free_Rate': self.risk_free_rate,
            'Random_Z': z,
            'Simulated_Spot': simulated_spot,
            'MC_Payoff_PV': pv_payoffs,
            'BS_Constant': bs_price,
            'Hybrid_Value': hybrid_contributions
        })

        summary = {
            "Company": self.ticker,
            "Period": scenario_name,
            "BS_Price": bs_price,
            "MC_Mean": np.mean(pv_payoffs),
            "Hybrid_Mean": np.mean(hybrid_contributions)
        }

        return summary, detailed_df

# ==========================================
# Execution Block
# ==========================================
if __name__ == "__main__":
    companies = {
        "KGHM": "KGH.WA", 
        "PKO_BP": "PKO.WA", 
        "ORLEN": "PKN.WA", 
        "ALLEGRO": "ALE.WA"
    }
    
    time_periods = [
        ("Stable", "2021-10-01", "2022-01-31", 0.025),
        ("Shock", "2022-02-01", "2022-04-30", 0.045)
    ]

    all_summaries = []
    all_details = []

    print("Starting analysis")

    for company_name, ticker in companies.items():
        for period_name, start_date, end_date, rate in time_periods:
            full_name = f"{company_name}_{period_name}"
            
            engine = HybridPricingEngine(ticker, start_date, end_date, rate)
            summary_data, details_data = engine.run_full_analysis(full_name)
            
            all_summaries.append(summary_data)
            all_details.append(details_data)
            
            print(f"Completed {full_name}")

    pd.DataFrame(all_summaries).to_csv("summary_results.csv", index=False, sep=';')
    pd.concat(all_details).to_csv("simulation_details.csv", index=False, sep=';')

    print("\nProcess finished successfully")
    print("Exported summary_results.csv")
    print("Exported simulation_details.csv")
