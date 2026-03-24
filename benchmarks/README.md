# Benchmarks: Python vs `qfin_cpp`

Skrypt [`bs_mc_benchmark.py`](bs_mc_benchmark.py) mierzy czas **Black–Scholes** i **Monte Carlo** (NumPy/SciPy vs moduł C++), oraz różnice wartości.

## Zależności

```bash
pip install -r requirements-benchmarks.txt
```

## Rozszerzenie C++

```bash
pip install pybind11
pip install -e 08_CPP_Pricing_Core/qfin_cpp_ext
```

## Uruchomienie (z korzenia repo)

```bash
python benchmarks/bs_mc_benchmark.py --paths 500000 --repeats 7
```
