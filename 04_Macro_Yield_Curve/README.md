# Macro: spread krzywej & inwersja

> Porównanie długiego i krótkiego oprocentowania (np. 10Y vs 3M), wykrycie **inwersji krzywej**; dane ze **Stooq** (**httpx** + **tenacity**) lub tryb demonstracyjny.

| Plik | Rola |
|------|------|
| [`yield_curve_inversion.py`](yield_curve_inversion.py) | Klasa `YieldCurveAnalyzer`: spread, flaga inwersji, wykres |

## Teoria

Spread można zapisać jako różnicę stóp / yieldów:

$$
s_t = y^{\mathrm{long}}_t - y^{\mathrm{short}}_t
$$

Długa faza $s_t < 0$ bywa interpretowana heurystycznie jako sygnał ostrzegawczy dla cyklu (nie reguła automatyczna).

## Uruchomienie

```bash
cd 04_Macro_Yield_Curve
pip install pandas numpy matplotlib httpx tenacity
python yield_curve_inversion.py
```

## Powiązania

Kontekst dla stopy bezryzyka $r$ w [`01_Portfolio_Optimization`](../01_Portfolio_Optimization) oraz wycenie w [`02_Options_Pricing`](../02_Options_Pricing).
