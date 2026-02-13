#!/usr/bin/env python3
"""
run_pipeline.py — Run the complete Keeling Curve data pipeline.
"""

from fetch_data import download_data
from clean_data import load_and_clean
from analyze import analyze
from visualize import plot_full_curve, plot_seasonal_cycle, plot_decade_comparison
import pandas as pd

DATA_URL = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv"
RAW_FILE = "co2_monthly.csv"
CLEAN_FILE = "co2_clean.csv"


def main():
    print("=" * 50)
    print("KEELING CURVE DATA PIPELINE")
    print("=" * 50)

    # Step 1: Fetch
    print("\n[1/4] Fetching data...")
    download_data(DATA_URL, RAW_FILE)

    # Step 2: Clean
    print("\n[2/4] Cleaning data...")
    df = load_and_clean(RAW_FILE)
    df.to_csv(CLEAN_FILE, index=False)

    # Step 3: Analyze
    print("\n[3/4] Analyzing data...")
    analyze(CLEAN_FILE)

    # Step 4: Visualize
    print("\n[4/4] Creating visualizations...")
    df = pd.read_csv(CLEAN_FILE, parse_dates=["date"])
    plot_full_curve(df)
    plot_seasonal_cycle(df)
    plot_decade_comparison(df)

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()
