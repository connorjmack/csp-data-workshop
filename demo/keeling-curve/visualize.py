"""
visualize.py — Publication-quality visualizations of Keeling Curve analysis.

Creates professional figures showing:
1. Full time series with trend decomposition
2. Seasonal decomposition (4-panel)
3. Growth rate and acceleration over time
4. Historical context (800k years)
5. Decade comparison
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Professional styling
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = '#f8f9fa'
plt.rcParams['axes.edgecolor'] = '#dee2e6'
plt.rcParams['grid.color'] = '#dee2e6'
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10


def plot_overview(df: pd.DataFrame, decomp_df: pd.DataFrame) -> None:
    """
    Create main overview figure with observations, trend, and deseasonalized data.
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    # Plot observed data (thin, semi-transparent)
    ax.plot(df["date"], df["co2"],
            color="#1f77b4", linewidth=0.8, alpha=0.4,
            label="Monthly observations", zorder=1)

    # Plot trend (bold)
    ax.plot(decomp_df["date"], decomp_df["trend"],
            color="#d62728", linewidth=2.5,
            label="Trend component", zorder=3)

    # Plot deseasonalized (seasonal removed)
    ax.plot(decomp_df["date"], decomp_df["deseasonalized"],
            color="#2ca02c", linewidth=1.2, alpha=0.7,
            label="Deseasonalized", zorder=2)

    ax.set_xlabel("Year", fontsize=12, fontweight='bold')
    ax.set_ylabel("CO₂ Concentration (ppm)", fontsize=12, fontweight='bold')
    ax.set_title("Atmospheric CO₂ at Mauna Loa Observatory\nObserved, Trend, and Deseasonalized",
                 fontsize=14, fontweight='bold', pad=20)

    ax.legend(loc="upper left", framealpha=0.95, fontsize=10)
    ax.grid(True, alpha=0.3, linewidth=0.8)

    # Format x-axis
    ax.xaxis.set_major_locator(mdates.YearLocator(10))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.tight_layout()
    plt.savefig("fig1_overview.png", dpi=300, bbox_inches='tight')
    print("✓ Saved: fig1_overview.png")
    plt.close()


def plot_decomposition(decomp_df: pd.DataFrame) -> None:
    """
    Create 4-panel seasonal decomposition figure.
    """
    fig = plt.figure(figsize=(14, 10))
    gs = GridSpec(4, 1, hspace=0.3)

    # Panel 1: Observed
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(decomp_df["date"], decomp_df["observed"], color="#1f77b4", linewidth=1)
    ax1.set_ylabel("Observed\n(ppm)", fontsize=10, fontweight='bold')
    ax1.set_title("Seasonal Decomposition of Keeling Curve", fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(labelbottom=False)

    # Panel 2: Trend
    ax2 = fig.add_subplot(gs[1])
    ax2.plot(decomp_df["date"], decomp_df["trend"], color="#d62728", linewidth=1.5)
    ax2.set_ylabel("Trend\n(ppm)", fontsize=10, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelbottom=False)

    # Panel 3: Seasonal
    ax3 = fig.add_subplot(gs[2])
    ax3.plot(decomp_df["date"], decomp_df["seasonal"], color="#2ca02c", linewidth=1)
    ax3.set_ylabel("Seasonal\n(ppm)", fontsize=10, fontweight='bold')
    ax3.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(labelbottom=False)

    # Panel 4: Residual
    ax4 = fig.add_subplot(gs[3])
    ax4.plot(decomp_df["date"], decomp_df["residual"], color="#ff7f0e", linewidth=0.8, alpha=0.7)
    ax4.set_ylabel("Residual\n(ppm)", fontsize=10, fontweight='bold')
    ax4.set_xlabel("Year", fontsize=12, fontweight='bold')
    ax4.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax4.grid(True, alpha=0.3)

    # Format x-axis for bottom panel
    ax4.xaxis.set_major_locator(mdates.YearLocator(10))
    ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    plt.savefig("fig2_decomposition.png", dpi=300, bbox_inches='tight')
    print("✓ Saved: fig2_decomposition.png")
    plt.close()


def plot_growth_and_acceleration(growth_df: pd.DataFrame) -> None:
    """
    Create dual-panel figure showing growth rate and acceleration.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

    # Panel 1: Growth rate
    ax1.plot(growth_df["year"], growth_df["growth_rate"],
             color="#1f77b4", linewidth=0.8, alpha=0.3, label="Annual")
    ax1.plot(growth_df["year"], growth_df["growth_rate_smooth"],
             color="#d62728", linewidth=2.5, label="5-year average")
    ax1.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax1.set_ylabel("Growth Rate\n(ppm/year)", fontsize=11, fontweight='bold')
    ax1.set_title("CO₂ Growth Rate and Acceleration Over Time", fontsize=14, fontweight='bold', pad=15)
    ax1.legend(loc="upper left", framealpha=0.95)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Acceleration
    ax2.plot(growth_df["year"], growth_df["acceleration"],
             color="#2ca02c", linewidth=0.8, alpha=0.3, label="Annual")
    ax2.plot(growth_df["year"], growth_df["acceleration_smooth"],
             color="#ff7f0e", linewidth=2.5, label="5-year average")
    ax2.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
    ax2.set_xlabel("Year", fontsize=12, fontweight='bold')
    ax2.set_ylabel("Acceleration\n(ppm/year²)", fontsize=11, fontweight='bold')
    ax2.legend(loc="upper left", framealpha=0.95)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("fig3_growth_acceleration.png", dpi=300, bbox_inches='tight')
    print("✓ Saved: fig3_growth_acceleration.png")
    plt.close()


def plot_historical_context() -> None:
    """
    Plot 800,000 years of CO₂ from ice cores + modern measurements.
    """
    try:
        # Load historical data
        hist = pd.read_csv("co2_historical.csv", comment='"', skipinitialspace=True)
        hist.columns = hist.columns.str.strip()

        # Find the CO2 column (might be named differently)
        co2_col = None
        for col in hist.columns:
            if 'co2' in col.lower() and 'age' not in col.lower():
                co2_col = col
                break

        if co2_col is None:
            print("⚠ Could not find CO2 column in historical data, skipping historical plot")
            return

        # Find year/age column - could be sample_date, year, age, etc.
        year_col = None
        for col in hist.columns:
            if any(x in col.lower() for x in ['year', 'age', 'yr', 'date', 'sample']):
                year_col = col
                break

        if year_col is None:
            print("⚠ Could not find year column in historical data, skipping historical plot")
            return

        hist = hist.rename(columns={year_col: 'year', co2_col: 'co2'})
        hist = hist[['year', 'co2']].dropna()

        # Convert to numeric
        hist['year'] = pd.to_numeric(hist['year'], errors='coerce')
        hist['co2'] = pd.to_numeric(hist['co2'], errors='coerce')
        hist = hist.dropna()

        # Create figure
        fig, ax = plt.subplots(figsize=(16, 6))

        # Split into ice core (historical) and modern
        ice_core = hist[hist['year'] < 1958].copy()
        modern = hist[hist['year'] >= 1958].copy()

        # Plot ice core data
        ax.plot(ice_core['year'], ice_core['co2'],
                color="#3498db", linewidth=1.5, alpha=0.8, label="Ice core data")

        # Plot modern data
        ax.plot(modern['year'], modern['co2'],
                color="#e74c3c", linewidth=2, label="Direct measurements (Mauna Loa)")

        # Highlight pre-industrial level
        ax.axhline(y=280, color='green', linewidth=1.5, linestyle='--',
                   alpha=0.7, label="Pre-industrial level (~280 ppm)")

        # Highlight current level
        if len(modern) > 0:
            current = modern['co2'].iloc[-1]
            ax.axhline(y=current, color='red', linewidth=1.5, linestyle='--',
                       alpha=0.7, label=f"Current level (~{current:.0f} ppm)")

        ax.set_xlabel("Year", fontsize=12, fontweight='bold')
        ax.set_ylabel("CO₂ Concentration (ppm)", fontsize=12, fontweight='bold')
        # Determine title based on data range
        year_span = modern['year'].max() - ice_core['year'].min()
        if year_span > 10000:
            title = f"{int(year_span):,} Years of Atmospheric CO₂\nIce Core Records + Modern Measurements"
        else:
            title = f"{int(year_span):,} Years of Atmospheric CO₂\nIce Core Records + Modern Measurements"

        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.legend(loc="upper left", framealpha=0.95, fontsize=10)
        ax.grid(True, alpha=0.3)

        # Set x-axis limits to show full range
        ax.set_xlim(ice_core['year'].min(), modern['year'].max())

        plt.tight_layout()
        plt.savefig("fig4_historical_context.png", dpi=300, bbox_inches='tight')
        print("✓ Saved: fig4_historical_context.png")
        plt.close()

    except FileNotFoundError:
        print("⚠ Historical data file not found, skipping historical context plot")
    except Exception as e:
        print(f"⚠ Error creating historical context plot: {e}")


def plot_seasonal_cycle(df: pd.DataFrame) -> None:
    """
    Create detailed seasonal cycle analysis.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: Average seasonal cycle
    monthly_avg = df.groupby("month")["co2"].mean()
    monthly_std = df.groupby("month")["co2"].std()

    months = range(1, 13)
    month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    ax1.bar(months, monthly_avg.values, color="#2ecc71", alpha=0.7,
            edgecolor='white', linewidth=1.5, yerr=monthly_std.values, capsize=4)
    ax1.set_xticks(months)
    ax1.set_xticklabels(month_labels, fontsize=10)
    ax1.set_xlabel("Month", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Average CO₂ (ppm)", fontsize=12, fontweight='bold')
    ax1.set_title("Average Seasonal Cycle\n(±1 std dev)", fontsize=12, fontweight='bold')
    ax1.grid(True, axis='y', alpha=0.3)

    # Panel 2: Seasonal cycle by decade
    colors = plt.cm.viridis_r
    decades = sorted(df["year"].apply(lambda y: int(y) // 10 * 10).unique())

    for i, decade in enumerate(decades):
        mask = (df["year"] >= decade) & (df["year"] < decade + 10)
        subset = df[mask]
        if len(subset) > 12:  # Only plot if we have enough data
            monthly = subset.groupby("month")["co2"].mean()
            color = colors(i / len(decades))
            # Only label first and last decade
            if decade == decades[0] or decade == decades[-1]:
                ax2.plot(monthly.index, monthly.values,
                        color=color, linewidth=2, label=f"{decade}s", alpha=0.9)
            else:
                ax2.plot(monthly.index, monthly.values,
                        color=color, linewidth=1, alpha=0.3)

    ax2.set_xticks(months)
    ax2.set_xticklabels(month_labels, fontsize=10)
    ax2.set_xlabel("Month", fontsize=12, fontweight='bold')
    ax2.set_ylabel("CO₂ (ppm)", fontsize=12, fontweight='bold')
    ax2.set_title("Seasonal Cycle by Decade", fontsize=12, fontweight='bold')
    ax2.legend(loc="upper left", framealpha=0.95)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("fig5_seasonal_analysis.png", dpi=300, bbox_inches='tight')
    print("✓ Saved: fig5_seasonal_analysis.png")
    plt.close()


def main():
    """Generate all publication-quality figures."""
    print("=" * 70)
    print("GENERATING PUBLICATION-QUALITY FIGURES")
    print("=" * 70)
    print()

    # Load data
    df = pd.read_csv("co2_clean.csv", parse_dates=["date"])
    decomp_df = pd.read_csv("analysis_decomposition.csv", parse_dates=["date"])
    growth_df = pd.read_csv("analysis_growth_rate.csv")

    # Generate figures
    plot_overview(df, decomp_df)
    plot_decomposition(decomp_df)
    plot_growth_and_acceleration(growth_df)
    plot_historical_context()
    plot_seasonal_cycle(df)

    print()
    print("=" * 70)
    print("All figures generated!")
    print("=" * 70)


if __name__ == "__main__":
    main()
