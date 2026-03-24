## Wspólne benchmarki Python ↔ C++

Skrypt `bs_mc_benchmark.py` mierzy czas:

- **Black–Scholes** (NumPy + `scipy.stats.norm` vs moduł `qfin_cpp` z pybind11),
- **Monte Carlo** europejskiego calla (wektoryzowany NumPy vs to samo API w C++).

Porównuje też **wartości liczbowe** (różnica bezwzględna BS i MC), żeby zweryfikować spójność implementacji.

### Instalacja zależności benchmarków

```bash
pip install -r requirements-benchmarks.txt
```

### Rozszerzenie C++

```bash
pip install pybind11
pip install -e 08_Numerical_Kernels/qfin_cpp_ext
```

### Uruchomienie

Z korzenia repozytorium:

```bash
python benchmarks/bs_mc_benchmark.py --paths 500000 --repeats 7
```

Parametry `--paths` i `--repeats` są opcjonalne.
