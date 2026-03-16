import pandas as pd
import requests
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
from datetime import datetime, timedelta
import sys

try:
    from config import DB_CONFIG
except ImportError:
    print("Error: 'config.py' missing. Please create it with DB credentials.")
    sys.exit(1)

class MarketDataLoader:
    """
    Handles fetching FX market data from external APIs (e.g., NBP)
    and loading it into a relational database.
    """
    def __init__(self):
        safe_password = quote_plus(DB_CONFIG['password'])
        db_url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{safe_password}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        self.engine = create_engine(db_url)

    def fetch_nbp_rates(self, currency: str = "EUR", days_back: int = 365):
        """Fetches historical FX rates from NBP API for the last 'days_back' days."""
        print(f"Fetching {currency}/PLN data from NBP API...")
        
        end_date = datetime.today()
        start_date = end_date - timedelta(days=days_back)
        
        start_str = start_date.strftime('%Y-%m-%d')
        end_str = end_date.strftime('%Y-%m-%d')
        
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start_str}/{end_str}/?format=json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['rates'])
            df['currency_pair'] = f"{currency}/PLN"
            
            # Format dataframe to match DB schema
            df = df.rename(columns={'effectiveDate': 'date', 'mid': 'rate_mid'})
            df = df[['date', 'currency_pair', 'rate_mid']]
            
            self._save_to_database(df, currency)
        else:
            print(f"NBP API Error: {response.status_code} - {response.text}")

    def _save_to_database(self, df: pd.DataFrame, currency: str):
        """Saves dataframe to the SQL database."""
        try:
            df.to_sql('market_data', self.engine, if_exists='append', index=False)
            print(f"Success! Data for {currency} loaded into the database.\n")
        except Exception as e:
            print(f"Database Error: {e}")

    def clean_table(self):
        """Drops the table to prevent duplicate entries on fresh loads."""
        try:
            with self.engine.connect() as conn:
                conn.execute(text("DROP TABLE IF EXISTS market_data"))
                conn.commit()
            print("Database table 'market_data' cleaned successfully.")
        except Exception as e:
            print(f"Error cleaning table: {e}")

if __name__ == "__main__":
    loader = MarketDataLoader()
    loader.clean_table()
    loader.fetch_nbp_rates("EUR")
    loader.fetch_nbp_rates("USD")
