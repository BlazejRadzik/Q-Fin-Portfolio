## Cel modułu

**Ryzyko rynkowe:** ETL kursów FX (NBP) do SQL oraz **parametryczny dzienny VaR** z log-zwrotów.

## Teoria w skrócie

- \(r_t = \ln(P_t/P_{t-1})\), \(\hat{\sigma}\) z próby.
- **VaR parametryczny (1 dzień):** \(\mathrm{VaR}_\alpha \approx z_\alpha \hat{\sigma} \cdot V\) przy normalności zwrotów, \(z_\alpha = \Phi^{-1}(\alpha)\).

## Zawartość

| Plik | Rola |
|------|------|
| `fx_data_loader.py` | Pobranie JSON z NBP przez **httpx** + ponowienia **tenacity**, zapis do MySQL. |
| `var_calculator.py` | Odczyt szeregu z bazy, obliczenie VaR. |
| `config.example.py` | Wzorzec `DB_CONFIG` przez **pydantic-settings** (`QFIN_DB_*` / `.env`). |

## Konfiguracja

Skopiuj `config.example.py` → `config.py` albo utrzymuj własny `config.py` ze słownikiem `DB_CONFIG`. Plik z hasłem nie jest commitowany (`.gitignore`).

## Uruchomienie

```bash
cd 03_Risk_Management
pip install pandas numpy scipy sqlalchemy mysql-connector-python httpx tenacity pydantic pydantic-settings
python fx_data_loader.py
python var_calculator.py
```

## Powiązania w portfolio

Historyczny VaR portfela akcji: `01_Stochastic_Models`. Scenariusze \(\sigma\) i \(r\): moduły `02` i `05`.
