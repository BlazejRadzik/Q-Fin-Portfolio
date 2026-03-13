import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
import numpy as np
import matplotlib.dates as mdates

class YieldCurveAnalyzer:
    """
    Analyzes and visualizes the yield curve inversion between long-term bonds 
    and short-term interest rates (e.g., 10Y Polish Bonds vs WIBOR 3M).
    """
    def __init__(self, short_term_ticker: str = 'PLOPLN3M', long_term_ticker: str = '10PLY.B'):
        self.short_term_ticker = short_term_ticker
        self.long_term_ticker = long_term_ticker
        self.data_source = "Unknown"

    def _fetch_stooq_data(self, ticker: str) -> pd.Series:
        """Fetches historical financial data from Stooq API."""
        url = f"https://stooq.com/q/d/l/?s={ticker}&i=d"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200 and len(r.text) > 100:
                df = pd.read_csv(io.StringIO(r.text), index_col=0, parse_dates=True)
                return df.iloc[:, -1] # Assuming the last column is 'Close'
        except Exception as e:
            print(f"Warning: Could not fetch data for {ticker}. Error: {e}")
        
        return pd.Series(dtype=float)

    def generate_spread_data(self) -> pd.DataFrame:
        """Calculates the spread. Generates synthetic data if API fails."""
        print("Fetching yield curve data...")
        short_term_rate = self._fetch_stooq_data(self.short_term_ticker)
        long_term_bonds = self._fetch_stooq_data(self.long_term_ticker)

        if short_term_rate.empty or long_term_bonds.empty:
            print("Stooq API unavailable. Falling back to Synthetic Demo Data.")
            self.data_source = "Synthetic Demo Data"
            
            # Generate random walk for demo purposes
            dates = pd.date_range(end=pd.Timestamp.now(), periods=1000, freq='D')
            spread_values = np.cumsum(np.random.normal(0, 0.06, 1000)) + 1.0
            spread_values[400:700] = spread_values[400:700] - 3.0  # Force an inversion period
            
            df = pd.DataFrame({'Spread': spread_values}, index=dates)
        else:
            self.data_source = "Stooq Data (Live)"
            df = pd.DataFrame({'Short_Term': short_term_rate, 'Long_Term': long_term_bonds}).dropna()
            df['Spread'] = df['Long_Term'] - df['Short_Term']

        df['Inversion'] = df['Spread'] < 0
        return df

    def plot_inversion(self, df: pd.DataFrame, output_filename: str = 'wibor_plot_pro.png'):
        """Plots the spread with a professional dark theme."""
        print("Plotting yield curve inversion...")
        
        # Apply dark theme locally for this plot
        with plt.style.context('dark_background'):
            fig, ax = plt.subplots(figsize=(12, 7))
            
            # Background and grid styling
            fig.patch.set_facecolor('#212121')
            ax.set_facecolor('#2b2b2b')
            ax.grid(True, linestyle=':', linewidth=0.7, color='#444444')

            # Plot main spread line
            ax.plot(df.index, df['Spread'], label='Spread (10Y - 3M)', color='#00BFFF', linewidth=2)
            ax.axhline(0, color='#FF3333', linestyle='--', linewidth=1.5, alpha=0.8)
            
            # Highlight Inversion Area
            ax.fill_between(df.index, df['Spread'], 0, where=df['Inversion'], 
                            color='#FF0000', alpha=0.4, label='Inversion Area')

            # Annotate Maximum Inversion
            min_date = df['Spread'].idxmin()
            min_value = df['Spread'].min()
            
            if min_value < 0:
                ax.annotate(f'Max Inversion: {min_value:.2f} p.p.',
                            xy=(min_date, min_value),
                            xytext=(min_date, min_value - 0.8),
                            arrowprops=dict(facecolor='#FF3333', shrink=0.05, width=2, headwidth=8),
                            color='white', fontweight='bold', ha='center',
                            bbox=dict(boxstyle="round,pad=0.3", fc="#FF3333", ec="none", alpha=0.3))

            # Labels and title
            ax.set_title('Yield Curve Inversion Analysis (Poland)', fontsize=16, fontweight='bold', pad=20, color='#d4d4d4')
            ax.set_ylabel('Spread (Percentage Points)', fontsize=12, color='#d4d4d4')
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
            fig.autofmt_xdate()

            # Legend and Source
            legend = ax.legend(loc='upper right', facecolor='#333333', edgecolor='#555555')
            plt.setp(legend.get_texts(), color='#d4d4d4')
            plt.figtext(0.95, 0.02, f'Source: {self.data_source} | Quant Portfolio Analytics', 
                        ha='right', fontsize=9, color='#888888')

            plt.tight_layout()
            plt.savefig(output_filename, dpi=150, bbox_inches='tight')
            print(f"Plot successfully saved as '{output_filename}'")

if __name__ == "__main__":
    analyzer = YieldCurveAnalyzer()
    spread_df = analyzer.generate_spread_data()
    analyzer.plot_inversion(spread_df)