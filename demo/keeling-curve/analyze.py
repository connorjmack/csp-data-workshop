"""
analyze.py — Compute summary statistics and trends from the Keeling Curve data.
"""

import pandas as pd

INPUT_FILE = "co2_clean.csv"


def analyze(input_path: str) -> None:
    """Print key insights from the Keeling Curve data."""
    df = pd.read_csv(input_path, parse_dates=["date"])

    # --- Annual averages ---
    annual = df.groupby("year")["co2"].mean()

    print("=" * 50)
    print("KEELING CURVE ANALYSIS")
    print("=" * 50)

    # Overall statistics
    print(f"\nDate range: {df['date'].min().year} – {df['date'].max().year}")
    print(f"Total measurements: {len(df)}")
    print(f"CO₂ start: {annual.iloc[0]:.2f} ppm ({int(annual.index[0])})")
    print(f"CO₂ latest: {annual.iloc[-1]:.2f} ppm ({int(annual.index[-1])})")
    print(f"Total increase: {annual.iloc[-1] - annual.iloc[0]:.2f} ppm")

    # --- Growth rate by decade ---
    print("\n--- Average Annual Growth Rate by Decade ---")
    df_annual = annual.reset_index()
    df_annual.columns = ["year", "co2"]
    df_annual["decade"] = (df_annual["year"] // 10) * 10
    df_annual["co2_diff"] = df_annual["co2"].diff()

    decade_growth = df_annual.groupby("decade")["co2_diff"].mean()
    for decade, rate in decade_growth.items():
        if pd.notna(rate):
            print(f"  {int(decade)}s: +{rate:.2f} ppm/year")

    # --- Seasonal amplitude ---
    print("\n--- Seasonal Cycle ---")
    monthly_avg = df.groupby("month")["co2"].mean()
    amplitude = monthly_avg.max() - monthly_avg.min()
    peak_month = monthly_avg.idxmax()
    trough_month = monthly_avg.idxmin()

    month_names = [
        "", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    print(f"  Seasonal amplitude: {amplitude:.2f} ppm")
    print(f"  Peak month: {month_names[int(peak_month)]} ({monthly_avg.max():.2f} ppm)")
    print(f"  Trough month: {month_names[int(trough_month)]} ({monthly_avg.min():.2f} ppm)")


if __name__ == "__main__":
    analyze(INPUT_FILE)
