from __future__ import annotations

import pandas as pd
import yfinance as yf
from cachetools import TTLCache, cached
from cachetools.keys import hashkey

_CACHE = TTLCache(maxsize=256, ttl=900)


def _ohlcv_cache_key(
    fn, symbol: str, start: str, end: str | None = None, **kwargs
):
    return hashkey(symbol, start, end or "")


@cached(cache=_CACHE, key=_ohlcv_cache_key)
def _download_ohlcv(
    symbol: str, start: str, end: str | None = None
) -> pd.DataFrame:
    return yf.download(
        symbol,
        start=start,
        end=end,
        progress=False,
        auto_adjust=True,
    )


def load_ohlcv(symbol: str, start: str, end: str | None = None) -> pd.DataFrame:
    raw = _download_ohlcv(symbol, start, end)
    if raw.empty:
        return pd.DataFrame()
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = [c[0] if isinstance(c, tuple) else c for c in raw.columns]
    cols = [c for c in ("Open", "High", "Low", "Close", "Volume") if c in raw.columns]
    return raw[cols].copy()
