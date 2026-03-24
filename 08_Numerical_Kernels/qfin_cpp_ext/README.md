## Moduł Python `qfin_cpp`

Natywna warstwa wiążąca implementację z `../cpp/src/black_scholes.cpp` z interpreterem Python (**pybind11**). Po instalacji importujesz `qfin_cpp` i porównujesz czasy oraz wartości z NumPy / SciPy (patrz `benchmarks/` w korzeniu repozytorium).

### Wymagania

- Python 3.9+
- Kompilator C++17 (MSVC, Clang, GCC)
- `pip install pybind11`

### Instalacja (edytowalna)

```bash
cd 08_Numerical_Kernels/qfin_cpp_ext
pip install pybind11
pip install -e .
```

### API

- `qfin_cpp.black_scholes_call(spot, strike, time_years, rate, vol) -> float`
- `qfin_cpp.monte_carlo_call(spot, strike, time_years, rate, vol, paths, seed=42) -> float`
