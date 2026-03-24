## Cel modułu

Aplikacje **Streamlit** do wyceny i eksperymentów numerycznych (BS vs MC, czułość parametrów).

## Stack

- Streamlit, NumPy/SciPy, Plotly
- Opcjonalnie Docker: **Dev Containers** w `Derivatives_Pricing_App/.devcontainer/`

## Zawartość

| Ścieżka | Rola |
|---------|------|
| `Derivatives_Pricing_App/` | Dashboard opcji europejskich, zbieżność MC. |
| `Derivatives_Pricing_App/.devcontainer/` | Powtarzalne środowisko (VS Code: *Reopen in Container*). |

## Uruchomienie

```bash
cd 05_Interactive_Dashboards/Derivatives_Pricing_App
pip install streamlit numpy scipy pandas plotly pytest
streamlit run app.py
```

## Powiązania w portfolio

Spójność z `02_Pricing_Engines` i jądrem C++ `08_Numerical_Kernels`.
