## Cel modułu

**Makro i krzywa dochodowości:** spread długo vs krótko (np. 10Y vs 3M), wizualizacja **inwersji**.

## Teoria w skrócie

Spread \(\approx\) długi minus krótki; długa faza ujemna może być (heurystycznie) sygnałem ostrzegawczym dla cyklu — nie reguła automatyczna.

## Zawartość

| Plik | Rola |
|------|------|
| `yield_curve_inversion.py` | `YieldCurveAnalyzer`: Stooq przez **httpx** + **tenacity**, fallback syntetyczny. |

## Uruchomienie

```bash
cd 04_Quantitative_Analysis
pip install pandas numpy matplotlib httpx tenacity
python yield_curve_inversion.py
```

## Powiązania w portfolio

Kontekst dla stóp \(r\) w `01`, `02`, `05`.
