# FX data & parametric market VaR

> **NBP → SQL:** pobieranie kursów walut, zapis do MySQL; **VaR parametryczny** (wariancja–kowariancja) z dziennych log-zwrotów.

| Plik | Rola |
|------|------|
| [`fx_data_loader.py`](fx_data_loader.py) | HTTP (**httpx** + **tenacity**), ETL do bazy |
| [`var_calculator.py`](var_calculator.py) | Odczyt szeregu, VaR 1-dniowy |
| [`config.example.py`](config.example.py) | Szablon `DB_CONFIG` (**pydantic-settings**, prefiks `QFIN_DB_`) |

## Teoria

Niech $P_t$ będzie kursem (np. EUR/PLN). Log-zwroty:

$$
r_t = \ln\frac{P_t}{P_{t-1}}
$$

**VaR parametryczny (1 dzień),** przy normalności $r_t$ i ekspozycji $V$:

$$
\mathrm{VaR}_\alpha \approx V \cdot z_\alpha \cdot \hat{\sigma}
$$

gdzie $z_\alpha = \Phi^{-1}(\alpha)$, a $\hat{\sigma}$ to odchylenie standardowe z próby.

## Konfiguracja

Skopiuj `config.example.py` → `config.py` lub utrzymuj własny `config.py` ze słownikiem `DB_CONFIG`. Hasła nie commituj (`.gitignore`).

## Uruchomienie

```bash
cd 03_FX_And_Market_Risk
pip install pandas numpy scipy sqlalchemy mysql-connector-python httpx tenacity pydantic pydantic-settings
python fx_data_loader.py
python var_calculator.py
```

## Powiązania

- VaR historyczny portfela akcji: [`01_Portfolio_Optimization`](../01_Portfolio_Optimization)
- Scenariusze $\sigma$, $r$: [`02_Options_Pricing`](../02_Options_Pricing), [`05_Derivatives_Dashboard`](../05_Derivatives_Dashboard)
