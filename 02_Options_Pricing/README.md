# Options pricing: Black–Scholes, Monte Carlo, hybryda

> Silnik wyceny calla europejskiego: **analityka BS**, symulacja **Monte Carlo** oraz korekta typu **control variate** łącząca oba estymatory.

| Plik | Rola |
|------|------|
| [`Hybrid_pricing_engine.py`](Hybrid_pricing_engine.py) | Estymacja $\sigma$ z log-zwrotów, BS, MC, hybryda, eksport CSV |
| [`report_formatter.py`](report_formatter.py) | Podgląd symulacji (opcjonalnie **Rich** w terminalu) |

## Teoria

**Black–Scholes (call):** standardowe $d_1$, $d_2$ i wartość zamknięta pod miarą martyngałową.

**Monte Carlo:** dyskretyzacja $S_T$ pod $Q$, dyskont $e^{-rT}$, średnia z payoffu $(S_T - K)^+$.

**Control variate:** redukcja wariancji estymatora MC przy wykorzystaniu znanej wartości analitycznej.

## Uruchomienie

```bash
cd 02_Options_Pricing
pip install numpy pandas yfinance scipy rich
python Hybrid_pricing_engine.py
```

**Import:**

```python
from Hybrid_pricing_engine import HybridPricingEngine

engine = HybridPricingEngine(
    ticker="PKO.WA",
    start_date="2022-01-01",
    end_date="2022-12-31",
    risk_free_rate=0.045,
    iterations=100_000,
)
summary, detailed_df = engine.run_full_analysis(scenario_name="PKO_Shock_Scenario")
```

```python
from report_formatter import print_simulation_table

print_simulation_table("simulation_details.csv", "PKO_Shock_Scenario", top_n=5)
```

## Powiązania

- Jądro C++: [`08_CPP_Pricing_Core`](../08_CPP_Pricing_Core)
- Dashboard: [`05_Derivatives_Dashboard`](../05_Derivatives_Dashboard)
- Benchmarki: [`benchmarks/`](../benchmarks)
