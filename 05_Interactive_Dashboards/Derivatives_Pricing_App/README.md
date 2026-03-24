## Cel

Porównanie **ceny analitycznej Blacka–Scholesa** z estymatą **Monte Carlo** dla opcji europejskiej, z możliwością zmiany \(S, K, T, r, \sigma\) i liczby ścieżek.

## Uruchomienie

```bash
pip install streamlit numpy scipy pandas plotly
streamlit run app.py
```

Z kontenera: w VS Code użyj **Reopen in Container**, następnie to samo polecenie `streamlit run app.py`.

## Testy

```bash
pytest
```

(jeśli w projekcie zdefiniowano scenariusze testowe zbieżności).
