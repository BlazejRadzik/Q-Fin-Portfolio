import sys

import pandas as pd


def print_simulation_table(
    file_path: str, scenario_name: str, top_n: int = 5
) -> None:
    try:
        df = pd.read_csv(file_path, sep=";")
        scenario_data = df[df["Scenario"] == scenario_name].head(top_n)

        if scenario_data.empty:
            print(f"Warning: No data found for scenario '{scenario_name}'.")
            return

        _render_table(scenario_name, scenario_data, top_n)

    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'.")
        print("Please run 'hybrid_pricing_engine.py' first to generate the data.")
        sys.exit(1)


def _render_table(
    scenario_name: str, scenario_data: pd.DataFrame, top_n: int
) -> None:
    try:
        from rich.console import Console
        from rich.table import Table

        console = Console()
        title = f"Monte Carlo — scenario: {scenario_name}"
        table = Table(title=title, show_header=True, header_style="bold")
        table.add_column("Sim ID", justify="right")
        table.add_column("Random Z", justify="right")
        table.add_column("Spot (S_T)", justify="right")
        table.add_column("Payoff (PV)", justify="right")
        table.add_column("Hybrid Val", justify="right")

        for _, row in scenario_data.iterrows():
            table.add_row(
                str(int(row["Sim_ID"])),
                f"{row['Random_Z']:.4f}",
                f"{row['Simulated_Spot']:.2f}",
                f"{row['MC_Payoff_PV']:.4f}",
                f"{row['Hybrid_Value']:.4f}",
            )

        console.print(table)
        console.print(f"[dim]First {top_n} rows.[/dim]\n")
    except ImportError:
        print(f"\n Table 3 (Scenario: {scenario_name})")
        print("-" * 80)
        print(
            f"{'Sim ID':<8} | {'Random Z':<12} | {'Spot (S_T)':<12} | "
            f"{'Payoff (PV)':<12} | {'Hybrid Val':<12}"
        )
        print("-" * 80)
        for _, row in scenario_data.iterrows():
            print(
                f"{int(row['Sim_ID']):<8} | "
                f"{row['Random_Z']:<12.4f} | "
                f"{row['Simulated_Spot']:<12.2f} | "
                f"{row['MC_Payoff_PV']:<12.4f} | "
                f"{row['Hybrid_Value']:.4f}"
            )
        print("-" * 80)
        print(f"Showing top {top_n} rows for report extraction.\n")


if __name__ == "__main__":
    print_simulation_table("simulation_details.csv", "PKO_BP_Shock", top_n=5)
