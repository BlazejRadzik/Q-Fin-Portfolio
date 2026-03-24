from __future__ import annotations

import sys
from datetime import datetime, timedelta
from urllib.parse import quote_plus

import httpx
import pandas as pd
from sqlalchemy import create_engine, text
from tenacity import retry, stop_after_attempt, wait_exponential

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
        safe_password = quote_plus(DB_CONFIG["password"])
        db_url = (
            f"mysql+mysqlconnector://{DB_CONFIG['user']}:{safe_password}"
            f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        self.engine = create_engine(db_url)

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=1, max=20),
        reraise=False,
    )
    def _nbp_json(self, url: str) -> dict | None:
        try:
            with httpx.Client(timeout=30.0, follow_redirects=True) as client:
                r = client.get(url)
            if r.status_code == 200:
                return r.json()
            return None
        except httpx.HTTPError:
            return None

    def fetch_nbp_rates(self, currency: str = "EUR", days_back: int = 365):
        """Fetches historical FX rates from NBP API for the last 'days_back' days."""
        print(f"Fetching {currency}/PLN data from NBP API...")

        end_date = datetime.today()
        start_date = end_date - timedelta(days=days_back)

        start_str = start_date.strftime("%Y-%m-%d")
        end_str = end_date.strftime("%Y-%m-%d")

        url = (
            f"http://api.nbp.pl/api/exchangerates/rates/A/"
            f"{currency}/{start_str}/{end_str}/?format=json"
        )
        data = self._nbp_json(url)

        if data is not None and "rates" in data:
            df = pd.DataFrame(data["rates"])
            df["currency_pair"] = f"{currency}/PLN"
            df = df.rename(columns={"effectiveDate": "date", "mid": "rate_mid"})
            df = df[["date", "currency_pair", "rate_mid"]]
            self._save_to_database(df, currency)
        else:
            print("NBP API: brak danych lub blad po stronie serwera.")

    def _save_to_database(self, df: pd.DataFrame, currency: str):
        """Saves dataframe to the SQL database."""
        try:
            df.to_sql("market_data", self.engine, if_exists="append", index=False)
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
