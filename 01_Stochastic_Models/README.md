# Portfolio Optimization and Stochastic Models

This module focuses on Modern Portfolio Theory (MPT) and stochastic processes.

## Portfolio Optimizer
The portfolio_optimizer allows users to:
* Fetch live market data for S&P 500 and GPW assets.
* Calculate the **Efficient Frontier**.
* Optimize weights for **Max Sharpe Ratio**, **Minimum Volatility**, or **Target Return**.

### Usage Example
To launch the interactive dashboard, ensure you have the requirements installed and run:
```bash
streamlit run portfolio_optimizer_app.py
Mathematical CoreThe optimization engine solves the quadratic programming problem:$$\min w^T \Sigma w$$Subject to:$\sum w_i = 1$$w^T \mu = \mu_{target}$
