"""
clean_data.py — Load, clean, and prepare the Keeling Curve data.
"""

import pandas as pd

INPUT_FILE = "co2_monthly.csv"
OUTPUT_FILE = "co2_clean.csv"


def load_and_clean(input_path: str) -> pd.DataFrame:
    """
    Load the raw Scripps CSV and return a clean DataFrame.

    The raw file has:
    - Comment lines starting with "
    - Missing values coded as -99.99
    - Columns: Yr, Mn, Date_Excel, Date, CO2, seasonally_adjusted, fit, ...
    """
    # Read the CSV, skipping comment lines
    df = pd.read_csv(
        input_path,
        comment='"',
        header=0,
        skipinitialspace=True,
        na_values=["-99.99", -99.99],
    )

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Keep only the columns we need
    # The exact column names may vary — let's inspect and adapt
    print(f"Raw columns: {list(df.columns)}")
    print(f"Raw shape: {df.shape}")

    # Rename columns to something consistent
    # Typical columns: Yr, Mn, Date Excel, Date, CO2, seasonally adjusted, fit, ...
    col_map = {}
    for col in df.columns:
        col_lower = col.lower().strip()
        if col_lower in ("yr", "year"):
            col_map[col] = "year"
        elif col_lower in ("mn", "month"):
            col_map[col] = "month"
        elif col_lower == "co2":
            col_map[col] = "co2"
        elif "seasonally" in col_lower:
            col_map[col] = "co2_adjusted"
        elif col_lower == "fit":
            col_map[col] = "co2_fit"

    df = df.rename(columns=col_map)

    # Keep only the columns we mapped
    keep_cols = [c for c in ["year", "month", "co2", "co2_adjusted", "co2_fit"] if c in df.columns]
    df = df[keep_cols].copy()

    # Convert types
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["month"] = pd.to_numeric(df["month"], errors="coerce")
    df["co2"] = pd.to_numeric(df["co2"], errors="coerce")

    # Drop rows where year or co2 is missing
    df = df.dropna(subset=["year", "co2"])

    # Create a proper date column
    df["date"] = pd.to_datetime(
        df["year"].astype(int).astype(str) + "-" + df["month"].astype(int).astype(str) + "-01"
    )

    # Sort by date
    df = df.sort_values("date").reset_index(drop=True)

    print(f"Clean shape: {df.shape}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"CO₂ range: {df['co2'].min():.2f} to {df['co2'].max():.2f} ppm")

    return df


if __name__ == "__main__":
    df = load_and_clean(INPUT_FILE)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved clean data to {OUTPUT_FILE}")
    print(df.head(10))
