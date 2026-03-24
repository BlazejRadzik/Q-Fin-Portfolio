# Derivatives dashboard (Streamlit)

> Interaktywna wycena opcji europejskiej: **Black–Scholes** vs **Monte Carlo**, czułość parametrów, wykres zbieżności MC.

| Ścieżka | Rola |
|---------|------|
| [`Derivatives_Pricing_App/`](Derivatives_Pricing_App/) | Aplikacja Streamlit + moduły `src/` |
| [`Derivatives_Pricing_App/.devcontainer/`](Derivatives_Pricing_App/.devcontainer/) | Dev Container (Docker) — powtarzalne środowisko |

## Uruchomienie

```bash
cd 05_Derivatives_Dashboard/Derivatives_Pricing_App
pip install streamlit numpy scipy pandas plotly pytest
streamlit run app.py
```

W VS Code / Codespaces: *Reopen in Container*, następnie `streamlit run app.py`.

## Powiązania

- Silnik batchowy: [`02_Options_Pricing`](../02_Options_Pricing)
- Jądro C++: [`08_CPP_Pricing_Core`](../08_CPP_Pricing_Core)
