from __future__ import annotations

import time
from typing import Optional

import numpy as np
import typer
from rich.console import Console
from rich.table import Table
from scipy.stats import norm

console = Console()


def black_scholes_numpy(
    spot: float,
    strike: float,
    time_years: float,
    rate: float,
    vol: float,
) -> float:
    if time_years <= 0.0 or vol <= 0.0:
        return max(spot - strike, 0.0)
    sqrt_t = np.sqrt(time_years)
    d1 = (np.log(spot / strike) + (rate + 0.5 * vol * vol) * time_years) / (vol * sqrt_t)
    d2 = d1 - vol * sqrt_t
    return float(
        spot * norm.cdf(d1) - strike * np.exp(-rate * time_years) * norm.cdf(d2)
    )


def monte_carlo_numpy(
    spot: float,
    strike: float,
    time_years: float,
    rate: float,
    vol: float,
    paths: int,
    seed: int,
) -> float:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(paths)
    drift = (rate - 0.5 * vol * vol) * time_years
    diffusion = vol * np.sqrt(time_years) * z
    st = spot * np.exp(drift + diffusion)
    payoff = np.maximum(st - strike, 0.0)
    df = np.exp(-rate * time_years)
    return float(df * np.mean(payoff))


def _timeit(fn, repeats: int) -> tuple[float, float]:
    best = float("inf")
    last = 0.0
    for _ in range(repeats):
        t0 = time.perf_counter()
        last = fn()
        dt = time.perf_counter() - t0
        best = min(best, dt)
    return best, last


def try_import_qfin_cpp():
    try:
        import qfin_cpp  # type: ignore

        return qfin_cpp
    except ImportError:
        return None


def main(
    paths: int = typer.Option(500_000, help="Monte Carlo path count"),
    repeats: int = typer.Option(7, help="Timing repeats (reports minimum of runs)"),
) -> None:
    spot = 100.0
    strike = 100.0
    time_years = 1.0
    rate = 0.05
    vol = 0.2
    seed = 42

    qfin_cpp = try_import_qfin_cpp()

    t_np_bs, v_np_bs = _timeit(
        lambda: black_scholes_numpy(spot, strike, time_years, rate, vol), repeats
    )
    t_np_mc, v_np_mc = _timeit(
        lambda: monte_carlo_numpy(spot, strike, time_years, rate, vol, paths, seed),
        repeats,
    )

    t_cpp_bs: Optional[float] = None
    v_cpp_bs: Optional[float] = None
    t_cpp_mc: Optional[float] = None
    v_cpp_mc: Optional[float] = None

    if qfin_cpp is not None:
        t_cpp_bs, v_cpp_bs = _timeit(
            lambda: float(
                qfin_cpp.black_scholes_call(spot, strike, time_years, rate, vol)
            ),
            repeats,
        )
        t_cpp_mc, v_cpp_mc = _timeit(
            lambda: float(
                qfin_cpp.monte_carlo_call(
                    spot, strike, time_years, rate, vol, paths, seed
                )
            ),
            repeats,
        )

    table = Table(title="Benchmark BS / MC (Q-Fin)")
    table.add_column("Implementacja", style="cyan", no_wrap=True)
    table.add_column("BS [ms]", justify="right")
    table.add_column("MC [ms]", justify="right")
    table.add_column("|BS_py - BS_cpp|", justify="right")
    table.add_column("|MC_py - MC_cpp|", justify="right")

    diff_bs = "-"
    diff_mc = "-"
    if v_cpp_bs is not None and v_cpp_mc is not None:
        diff_bs = f"{abs(v_np_bs - v_cpp_bs):.2e}"
        diff_mc = f"{abs(v_np_mc - v_cpp_mc):.2e}"

    row_cpp_bs = f"{t_cpp_bs * 1000:.3f}" if t_cpp_bs is not None else "n/a"
    row_cpp_mc = f"{t_cpp_mc * 1000:.3f}" if t_cpp_mc is not None else "n/a"

    table.add_row(
        "NumPy / SciPy",
        f"{t_np_bs * 1000:.3f}",
        f"{t_np_mc * 1000:.3f}",
        "0",
        "0",
    )
    table.add_row(
        "qfin_cpp (C++)",
        row_cpp_bs,
        row_cpp_mc,
        diff_bs,
        diff_mc,
    )

    console.print(table)
    console.print(
        "[dim]Install: pip install -e 08_Numerical_Kernels/qfin_cpp_ext "
        "(needs C++17 toolchain).[/dim]"
    )


if __name__ == "__main__":
    typer.run(main)
