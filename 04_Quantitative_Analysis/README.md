# 📉 Macro-Quantitative Analysis

This module focuses on macroeconomic indicators and yield curve dynamics. It primarily tracks the spread between long-term government bonds and short-term interbank rates.

## 🔍 Featured: Yield Curve Inversion Tracker
The `yield_curve_inversion.py` script visualizes the spread between the Polish 10Y Bond Yield and the WIBOR 3M rate. 

### Key Insights:
* **Recession Signaling:** Historically, a negative spread (inversion) often precedes economic downturns.
* **Automated Data Fetching:** Utilizes the Stooq API for live market data with a synthetic fallback for offline testing.

### How to run:
```bash
python yield_curve_inversion.py