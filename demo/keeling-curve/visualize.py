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
