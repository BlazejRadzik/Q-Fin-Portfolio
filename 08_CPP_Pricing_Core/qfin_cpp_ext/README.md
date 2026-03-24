# Python module `qfin_cpp`

Wiązanie **pybind11** do `../cpp/src/black_scholes.cpp`.

## Wymagania

Python 3.9+, kompilator **C++17**, `pip install pybind11`.

## Instalacja

```bash
cd 08_CPP_Pricing_Core/qfin_cpp_ext
pip install pybind11
pip install -e .
```

## API

- `qfin_cpp.black_scholes_call(spot, strike, time_years, rate, vol) -> float`
- `qfin_cpp.monte_carlo_call(spot, strike, time_years, rate, vol, paths, seed=42) -> float`

Porównanie z Pythonem: [`../../benchmarks/bs_mc_benchmark.py`](../../benchmarks/bs_mc_benchmark.py).
