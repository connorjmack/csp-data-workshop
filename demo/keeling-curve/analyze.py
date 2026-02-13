"""
analyze.py — Advanced time series analysis of the Keeling Curve.

This script performs a complete time series analysis including:
- Trend decomposition
- Seasonal decomposition
- Detrending
- Growth rate analysis
- Acceleration analysis
"""

import pandas as pd
import numpy as np
from scipy import stats, signal
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings
warnings.filterwarnings('ignore')

INPUT_FILE = "co2_clean.csv"
OUTPUT_PREFIX = "analysis"


def calculate_growth_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate annual growth rate and acceleration."""
    annual = df.groupby("year")["co2"].mean().reset_index()
    annual.columns = ["year", "co2"]

    # First derivative: growth rate (ppm/year)
    annual["growth_rate"] = annual["co2"].diff()

    # Second derivative: acceleration (ppm/year²)
    annual["acceleration"] = annual["growth_rate"].diff()

    # 5-year rolling average for smoothing
    annual["growth_rate_smooth"] = annual["growth_rate"].rolling(5, center=True).mean()
    annual["acceleration_smooth"] = annual["acceleration"].rolling(5, center=True).mean()

    return annual


def perform_seasonal_decomposition(df: pd.DataFrame, period: int = 12):
    """
    Decompose time series into trend, seasonal, and residual components.

    Uses additive decomposition: observed = trend + seasonal + residual
    """
    # Set date as index for decomposition
    ts = df.set_index("date")["co2"]

    # Perform seasonal decomposition
    decomposition = seasonal_decompose(ts, model='additive', period=period, extrapolate_trend='freq')

    # Extract components
    result = pd.DataFrame({
        'date': df['date'],
        'observed': df['co2'],
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    })

    # Detrended = observed - trend
    result['detrended'] = result['observed'] - result['trend']

    # Deseasonalized = observed - seasonal
    result['deseasonalized'] = result['observed'] - result['seasonal']

    return result, decomposition


def calculate_decadal_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate statistics by decade."""
    annual = df.groupby("year")["co2"].mean().reset_index()
    annual["decade"] = (annual["year"] // 10) * 10
    annual["co2_diff"] = annual["co2"].diff()

    decade_stats = annual.groupby("decade").agg({
        "co2": ["mean", "min", "max"],
        "co2_diff": ["mean", "std"]
    }).round(2)

    decade_stats.columns = ["co2_mean", "co2_min", "co2_max", "growth_mean", "growth_std"]
    return decade_stats


def analyze_residuals(decomposition_df: pd.DataFrame):
    """Analyze the residuals from decomposition."""
    residuals = decomposition_df['residual'].dropna()

    # Statistical tests
    mean_resid = residuals.mean()
    std_resid = residuals.std()

    # Normality test
    _, p_value = stats.normaltest(residuals)

    return {
        'mean': mean_resid,
        'std': std_resid,
        'p_value_normality': p_value,
        'is_normal': p_value > 0.05
    }


def main():
    """Run complete time series analysis."""
    print("=" * 70)
    print("KEELING CURVE — ADVANCED TIME SERIES ANALYSIS")
    print("=" * 70)
    print()

    # Load data
    df = pd.read_csv(INPUT_FILE, parse_dates=["date"])

    # === BASIC STATISTICS ===
    print("📊 BASIC STATISTICS")
    print("-" * 70)
    annual = df.groupby("year")["co2"].mean()
    print(f"Date range:        {df['date'].min().year} – {df['date'].max().year}")
    print(f"Total measurements: {len(df)}")
    print(f"CO₂ start:         {annual.iloc[0]:.2f} ppm ({int(annual.index[0])})")
    print(f"CO₂ latest:        {annual.iloc[-1]:.2f} ppm ({int(annual.index[-1])})")
    print(f"Total increase:    {annual.iloc[-1] - annual.iloc[0]:.2f} ppm")
    print(f"Percent increase:  {((annual.iloc[-1] / annual.iloc[0]) - 1) * 100:.1f}%")
    print()

    # === GROWTH RATE ANALYSIS ===
    print("📈 GROWTH RATE & ACCELERATION")
    print("-" * 70)
    growth_df = calculate_growth_rate(df)

    # Recent statistics
    recent_growth = growth_df["growth_rate"].tail(10).mean()
    recent_accel = growth_df["acceleration_smooth"].dropna().tail(10).mean()

    print(f"Recent growth rate (last 10y):     {recent_growth:.2f} ppm/year")
    print(f"Recent acceleration (last 10y):    {recent_accel:.3f} ppm/year²")
    print()

    # By decade
    print("Growth rate by decade:")
    decade_stats = calculate_decadal_statistics(df)
    for decade, row in decade_stats.iterrows():
        if pd.notna(row['growth_mean']):
            print(f"  {int(decade)}s: {row['growth_mean']:+.2f} ± {row['growth_std']:.2f} ppm/year")
    print()

    # === SEASONAL DECOMPOSITION ===
    print("🌊 SEASONAL DECOMPOSITION")
    print("-" * 70)
    decomp_df, decomposition = perform_seasonal_decomposition(df, period=12)

    seasonal_amplitude = decomp_df['seasonal'].max() - decomp_df['seasonal'].min()
    print(f"Seasonal amplitude:     {seasonal_amplitude:.2f} ppm")
    print(f"Trend variance:         {decomp_df['trend'].var():.2f}")
    print(f"Seasonal variance:      {decomp_df['seasonal'].var():.2f}")
    print(f"Residual variance:      {decomp_df['residual'].var():.2f}")
    print()

    # === RESIDUAL ANALYSIS ===
    print("🔍 RESIDUAL ANALYSIS")
    print("-" * 70)
    resid_stats = analyze_residuals(decomp_df)
    print(f"Residual mean:          {resid_stats['mean']:.4f} ppm")
    print(f"Residual std dev:       {resid_stats['std']:.2f} ppm")
    print(f"Normality test p-value: {resid_stats['p_value_normality']:.4f}")
    print(f"Residuals normal:       {'Yes' if resid_stats['is_normal'] else 'No'}")
    print()

    # === TREND FITTING ===
    print("📐 TREND ANALYSIS")
    print("-" * 70)

    # Linear trend
    x = (df['date'] - df['date'].min()).dt.days.values
    y = df['co2'].values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Convert slope from ppm/day to ppm/year
    slope_yearly = slope * 365.25

    print(f"Linear trend:           {slope_yearly:.4f} ppm/year")
    print(f"R² (goodness of fit):   {r_value**2:.4f}")
    print(f"Standard error:         {std_err * 365.25:.4f} ppm/year")
    print()

    # Quadratic trend (to capture acceleration)
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    quadratic_fit = p(x)

    # Calculate curvature (acceleration)
    curvature = 2 * z[0] * 365.25 * 365.25  # Convert to ppm/year²
    print(f"Quadratic acceleration: {curvature:.6f} ppm/year²")
    print()

    # === SAVE RESULTS ===
    print("💾 SAVING RESULTS")
    print("-" * 70)

    # Save decomposition
    decomp_df.to_csv(f"{OUTPUT_PREFIX}_decomposition.csv", index=False)
    print(f"✓ Saved: {OUTPUT_PREFIX}_decomposition.csv")

    # Save growth rate analysis
    growth_df.to_csv(f"{OUTPUT_PREFIX}_growth_rate.csv", index=False)
    print(f"✓ Saved: {OUTPUT_PREFIX}_growth_rate.csv")

    # Save decade statistics
    decade_stats.to_csv(f"{OUTPUT_PREFIX}_by_decade.csv")
    print(f"✓ Saved: {OUTPUT_PREFIX}_by_decade.csv")

    print()
    print("=" * 70)
    print("Analysis complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
