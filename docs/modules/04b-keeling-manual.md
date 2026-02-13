# Part 1: Manual Python Approach

In this part, you'll write the complete Keeling Curve pipeline by hand. This teaches you the fundamentals — what the data looks like, how to clean it, and how to work with pandas and matplotlib.

---

## Step 1: Download the Data

Create a file called `fetch_data.py`:

```python
"""
fetch_data.py — Download the Keeling Curve dataset from Scripps CO2 Program.
"""

import requests
import os

DATA_URL = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv"
OUTPUT_FILE = "co2_monthly.csv"


def download_data(url: str, output_path: str) -> None:
    """Download the raw CSV data from Scripps."""
    print(f"Downloading data from {url}...")
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(output_path, "w") as f:
        f.write(response.text)

    print(f"Saved to {output_path} ({len(response.text):,} bytes)")


if __name__ == "__main__":
    download_data(DATA_URL, OUTPUT_FILE)
```

Run it:

```bash
python3 fetch_data.py
```

!!! info "About the data source"
    This data comes from the Scripps CO₂ Program at UC San Diego. The CSV has header comments (lines starting with `"`) and some missing values marked as `-99.99`.

---

## Step 2: Clean and Parse the Data

Create `clean_data.py`:

```python
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
```

Run it:

```bash
python3 clean_data.py
```

You should see output like:

```
Raw columns: ['Yr', 'Mn', 'Date Excel', 'Date', 'CO2', ...]
Raw shape: (800+, 7)
Clean shape: (790+, 5)
Date range: 1958-03-01 to 2025-XX-01
CO₂ range: 312.XX to 42X.XX ppm
```

---

## Step 3: Analyze the Data

Create `analyze.py`:

```python
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
```

Run it:

```bash
python3 analyze.py
```

---

## Step 4: Visualize the Data

Create `visualize.py`:

```python
"""
visualize.py — Create plots of the Keeling Curve data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


INPUT_FILE = "co2_clean.csv"


def plot_full_curve(df: pd.DataFrame) -> None:
    """Plot the complete Keeling Curve."""
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df["date"], df["co2"], color="#2196F3", linewidth=0.8, alpha=0.8, label="Monthly average")

    # Add a trend line using the adjusted/fit values if available
    if "co2_fit" in df.columns:
        ax.plot(df["date"], df["co2_fit"], color="#F44336", linewidth=1.5, label="Trend (fit)")

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("CO₂ Concentration (ppm)", fontsize=12)
    ax.set_title("The Keeling Curve — Atmospheric CO₂ at Mauna Loa", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    # Format x-axis
    ax.xaxis.set_major_locator(mdates.YearLocator(10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.tight_layout()
    plt.savefig("keeling_curve_full.png", dpi=150)
    print("Saved: keeling_curve_full.png")
    plt.close()


def plot_seasonal_cycle(df: pd.DataFrame) -> None:
    """Plot the average seasonal CO₂ cycle."""
    monthly_avg = df.groupby("month")["co2"].mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    months = range(1, 13)
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    ax.bar(months, monthly_avg.values, color="#4CAF50", alpha=0.7, edgecolor="white")
    ax.set_xticks(months)
    ax.set_xticklabels(month_labels)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Average CO₂ (ppm)", fontsize=12)
    ax.set_title("Average Seasonal CO₂ Cycle", fontsize=14, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig("keeling_curve_seasonal.png", dpi=150)
    print("Saved: keeling_curve_seasonal.png")
    plt.close()


def plot_decade_comparison(df: pd.DataFrame) -> None:
    """Plot CO₂ trend for each decade."""
    fig, ax = plt.subplots(figsize=(12, 6))

    colors = plt.cm.viridis_r  # Color map: darker = more recent
    decades = sorted(df["year"].apply(lambda y: int(y) // 10 * 10).unique())

    for i, decade in enumerate(decades):
        mask = (df["year"] >= decade) & (df["year"] < decade + 10)
        subset = df[mask]
        if len(subset) > 0:
            color = colors(i / len(decades))
            ax.plot(subset["month"], subset["co2"], alpha=0.3, color=color)

    # Plot the mean for first and last decades
    for decade, style, label in [(decades[0], "--", f"{decades[0]}s avg"),
                                  (decades[-1], "-", f"{decades[-1]}s avg")]:
        mask = (df["year"] >= decade) & (df["year"] < decade + 10)
        subset = df[mask]
        if len(subset) > 0:
            monthly = subset.groupby("month")["co2"].mean()
            ax.plot(monthly.index, monthly.values, style, linewidth=2.5, label=label)

    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("CO₂ (ppm)", fontsize=12)
    ax.set_title("CO₂ Seasonal Cycle by Decade", fontsize=14, fontweight="bold")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("keeling_curve_decades.png", dpi=150)
    print("Saved: keeling_curve_decades.png")
    plt.close()


if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE, parse_dates=["date"])
    plot_full_curve(df)
    plot_seasonal_cycle(df)
    plot_decade_comparison(df)
    print("\nAll plots saved!")
```

Run it:

```bash
python3 visualize.py
```

You should now have three PNG files in your directory:

- `keeling_curve_full.png` — The complete CO₂ record since 1958
- `keeling_curve_seasonal.png` — The average seasonal cycle
- `keeling_curve_decades.png` — How the seasonal pattern has shifted over decades

---

## Step 5: Commit Your Work

```bash
# Stage all new files
git add fetch_data.py clean_data.py analyze.py visualize.py requirements.txt

# Don't commit data files or virtual environments
echo "venv/
*.csv
*.png
__pycache__/" > .gitignore
git add .gitignore

# Commit
git commit -m "Add Keeling Curve data pipeline (fetch, clean, analyze, visualize)"

# Push
git push
```

---

## What You've Built

Your project now has a complete data pipeline:

```
keeling-curve/
├── fetch_data.py          ← Downloads raw data
├── clean_data.py          ← Parses and cleans the CSV
├── analyze.py             ← Computes statistics and trends
├── visualize.py           ← Generates plots
├── requirements.txt       ← Python dependencies
├── .gitignore             ← Keeps repo clean
├── co2_monthly.csv        ← Raw data (not committed)
├── co2_clean.csv          ← Clean data (not committed)
├── keeling_curve_full.png         ← (not committed)
├── keeling_curve_seasonal.png     ← (not committed)
└── keeling_curve_decades.png      ← (not committed)
```

---

**Next:** [Part 2: AI-Assisted with Gemini CLI →](04c-keeling-gemini.md)
