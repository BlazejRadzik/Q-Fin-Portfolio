## Cel modułu

Silnik wyceny łączący **Blacka–Scholesa**, **Monte Carlo** oraz hybrydę typu **control variate**.

## Teoria w skrócie

- **BS (call europejski):** \(d_1, d_2\) i \(\Phi(\cdot)\).
- **MC:** dyskretyzacja \(S_T\) pod \(Q\), dyskont payoffu.
- **Control variate:** redukcja wariancji estymatora średniej MC przy znanej wartości analitycznej.

## Zawartość

| Plik | Rola |
|------|------|
| `Hybrid_pricing_engine.py` | `HybridPricingEngine`: \(\sigma\) z log-zwrotów, BS, MC, hybryda, eksport CSV. |
| `report_formatter.py` | Podgląd symulacji z CSV; **Rich** (opcjonalnie) lub tryb tekstowy. |

## Uruchomienie

```bash
cd 02_Pricing_Engines
pip install numpy pandas yfinance scipy rich
python Hybrid_pricing_engine.py
```

Import:

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

## Powiązania w portfolio

Identyczna struktura BS jest w C++ (`08_Numerical_Kernels`) i w dashboardzie opcji (`05_Interactive_Dashboards`). Benchmarki: `benchmarks/bs_mc_benchmark.py`.
