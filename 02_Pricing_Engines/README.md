# Hybrid Options Pricing Engine

This module provides a robust, object-oriented pricing engine that combines the analytical Black-Scholes-Merton framework with Monte Carlo simulations. It implements variance reduction using the Control Variates method.

## Quick Start (Usage Example)

You can import and use the `HybridPricingEngine` in your own scripts or notebooks.

```python
from hybrid_pricing_engine import HybridPricingEngine

# 1. Initialize the pricing engine for a specific asset and period
engine = HybridPricingEngine(
    ticker="PKO.WA", 
    start_date="2022-01-01", 
    end_date="2022-12-31", 
    risk_free_rate=0.045,
    iterations=100_000
)

# 2. Run the full Monte Carlo analysis
summary, detailed_df = engine.run_full_analysis(scenario_name="PKO_Shock_Scenario")

# 3. View the analytical vs numerical results
print(summary)
# Expected Output:
# {'Company': 'PKO.WA', 'Period': 'PKO_Shock_Scenario', 'BS_Price': 2.45, 'MC_Mean': 2.44, 'Hybrid_Mean': 2.45}

Generate Results
To extract a formatted ASCII table for research papers or reports, use the built-in formatter:
from report_formatter import print_simulation_table

# Print top 5 simulations for a specific scenario
print_simulation_table('simulation_details.csv', 'PKO_Shock_Scenario', top_n=5)
