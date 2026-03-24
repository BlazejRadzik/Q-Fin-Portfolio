## Cel modułu

**Jądro numeryczne w C++:** szybkie i deterministyczne (poza RNG) funkcje używane w wycenie i kalibracji — **Black–Scholes call** oraz **Monte Carlo** europejskiego calla pod miarą martingalową z dyskontem \(e^{-rT}\).

## Teoria w skrócie

- Analityka: identyczna struktura \(d_1, d_2\) jak w standardowym BS.
- MC: \(S_T = S_0 \exp((r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z)\), estymator ceny \(e^{-rT}\mathbb{E}[(S_T-K)^+]\).

## Struktura

```
08_Numerical_Kernels/cpp/
  CMakeLists.txt
  include/qfin/black_scholes.hpp
  src/black_scholes.cpp
  tools/bs_demo.cpp
08_Numerical_Kernels/qfin_cpp_ext/
  bindings.cpp
  setup.py
  pyproject.toml
```

## Budowanie (CMake)

```bash
cd 08_Numerical_Kernels/cpp
cmake -S . -B build
cmake --build build --config Release
./build/bs_demo
```

Na Windows: `build\Release\bs_demo.exe` (generator Visual Studio).

## Moduł Python (`qfin_cpp`)

```bash
pip install pybind11
pip install -e qfin_cpp_ext
```

Po instalacji: `import qfin_cpp` — funkcje `black_scholes_call` i `monte_carlo_call`. Zobacz też `benchmarks/bs_mc_benchmark.py` w korzeniu repozytorium.

## Powiązania w portfolio

Wynik `black_scholes_call` można porównać z `HybridPricingEngine` w Pythonie (`02_Pricing_Engines`) i z `black_scholes_european` w `05_Interactive_Dashboards/Derivatives_Pricing_App/src/analytical.py`.
