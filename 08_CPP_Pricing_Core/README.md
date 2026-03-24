# C++ pricing core & Python bindings

> **Black–Scholes call** i **Monte Carlo** europejskiego calla w C++17; ten sam kod pod **CMake** (`bs_demo`) oraz moduł **`qfin_cpp`** (pybind11).

## Struktura

```
08_CPP_Pricing_Core/
  cpp/
    CMakeLists.txt
    include/qfin/black_scholes.hpp
    src/black_scholes.cpp
    tools/bs_demo.cpp
  qfin_cpp_ext/
    bindings.cpp
    setup.py
    pyproject.toml
```

## CMake (natywny demo)

```bash
cd 08_CPP_Pricing_Core/cpp
cmake -S . -B build
cmake --build build --config Release
./build/bs_demo
```

Na Windows: `build\Release\bs_demo.exe`.

## Moduł Python `qfin_cpp`

```bash
pip install pybind11
pip install -e 08_CPP_Pricing_Core/qfin_cpp_ext
```

API: `black_scholes_call(...)`, `monte_carlo_call(...)`. Benchmark: [`benchmarks/bs_mc_benchmark.py`](../benchmarks/bs_mc_benchmark.py).

## Powiązania

- Python: [`02_Options_Pricing`](../02_Options_Pricing) (`HybridPricingEngine`)
- UI: [`05_Derivatives_Dashboard/Derivatives_Pricing_App/src/analytical.py`](../05_Derivatives_Dashboard/Derivatives_Pricing_App/src/analytical.py)
