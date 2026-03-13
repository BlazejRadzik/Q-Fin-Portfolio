# 🛡️ Market Risk Management

This module provides tools for assessing market risk using historical simulation and parametric methods. It integrates with a SQL database to manage financial time series.

## 🛠️ Components
* `fx_data_loader.py`: Automated ETL process fetching FX rates from NBP API.
* `var_calculator.py`: Engine for calculating **Value at Risk (VaR)**.

### Usage Example
```python
from var_calculator import VaRCalculator

# Initialize calculator and fetch data from SQL
calc = VaRCalculator()

# Calculate 95% Confidence VaR for EUR/PLN with 1M PLN exposure
calc.calculate_parametric_var(currency_pair='EUR/PLN', confidence_level=0.95, exposure=1000000)

## 🧮 Methodology
The parametric VaR is calculated using the variance-covariance approach:
$$VaR_{\alpha} = V \cdot Z_{\alpha} \cdot \sigma \cdot \sqrt{\Delta t}$$
Where:
* $V$: Portfolio value (Exposure).
* $Z_{\alpha}$: Critical value from the standard normal distribution.
* $\sigma$: Asset volatility (Standard deviation of returns).
