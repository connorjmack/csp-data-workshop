# Keeling Curve Data Pipeline — Advanced Time Series Analysis

This is a comprehensive, publication-quality implementation of the Keeling Curve data pipeline, demonstrating professional time series analysis techniques for climate science data.

## What is the Keeling Curve?

The Keeling Curve is a graph that shows the continuous measurement of atmospheric CO₂ concentration at Mauna Loa Observatory in Hawaii since 1958. It's named after scientist Charles David Keeling who began the measurements.

## Project Overview

This project demonstrates:

- **Data acquisition** from multiple sources (modern measurements + ice core records)
- **Proper time series decomposition** (trend, seasonal, residual components)
- **Advanced statistical analysis** (detrending, deseasonalization, growth rate, acceleration)
- **Publication-quality visualizations** using matplotlib
- **Best practices** for data engineering in climate science

## Project Structure

```
keeling-curve/
├── fetch_data.py                    # Downloads modern + historical CO₂ data
├── clean_data.py                    # Cleans and parses the CSV data
├── analyze.py                       # Advanced time series analysis
├── visualize.py                     # Publication-quality figures
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to exclude from git
├── README.md                        # This file
│
├── co2_monthly.csv                  # Raw modern data (not committed)
├── co2_historical.csv               # Ice core + modern data (not committed)
├── co2_clean.csv                    # Cleaned data (not committed)
│
├── analysis_decomposition.csv       # Seasonal decomposition results (not committed)
├── analysis_growth_rate.csv         # Growth rate & acceleration (not committed)
├── analysis_by_decade.csv           # Decadal statistics (not committed)
│
├── fig1_overview.png                # Overview with trend & deseasonalized (not committed)
├── fig2_decomposition.png           # 4-panel seasonal decomposition (not committed)
├── fig3_growth_acceleration.png     # Growth rate & acceleration (not committed)
├── fig4_historical_context.png      # 1,869 years of CO₂ history (not committed)
└── fig5_seasonal_analysis.png       # Seasonal cycle analysis (not committed)
```

## Setup

This project uses conda for environment management:

```bash
# Create a conda environment
conda create -n keeling-demo python=3.12 -y

# Activate it
conda activate keeling-demo

# Install dependencies
conda install pandas matplotlib requests scipy statsmodels -y
```

## Running the Pipeline

Run each script in order:

```bash
# 1. Download the data (modern + historical)
python fetch_data.py

# 2. Clean and parse modern measurements
python clean_data.py

# 3. Perform advanced time series analysis
python analyze.py

# 4. Create publication-quality visualizations
python visualize.py
```

## Analysis Outputs

### Time Series Decomposition

The analysis performs **seasonal decomposition** using statsmodels:

```
Observed = Trend + Seasonal + Residual
```

- **Trend**: Long-term upward trajectory (1.66 ppm/year linear trend)
- **Seasonal**: ~5.9 ppm annual cycle (northern hemisphere growing season)
- **Residual**: Random noise (~0.92 ppm std dev)

### Key Findings

Based on data from **1958 to 2025**:

#### Overall Change
- **Total increase**: 111.68 ppm (315.33 → 427.02 ppm)
- **Percent increase**: 35.4%
- **Linear trend**: 1.657 ppm/year (R² = 0.9751)
- **Quadratic acceleration**: 0.027 ppm/year²

#### Growth Rate by Decade
| Decade | Growth Rate (ppm/year) |
|--------|------------------------|
| 1950s  | +0.65 ± 0.00          |
| 1960s  | +0.86 ± 0.38          |
| 1970s  | +1.22 ± 0.52          |
| 1980s  | +1.58 ± 0.36          |
| 1990s  | +1.55 ± 0.65          |
| 2000s  | +1.91 ± 0.39          |
| 2010s  | +2.41 ± 0.47          |
| 2020s  | +2.60 ± 0.53          |

**⚠️ The growth rate has quadrupled** from the 1950s to the 2020s.

#### Seasonal Cycle
- **Amplitude**: 5.89 ppm
- **Peak**: May-June (northern hemisphere spring)
- **Trough**: September-October (after growing season)
- **Cause**: Seasonal uptake/release by terrestrial vegetation

#### Historical Context (1,869 years)
- Pre-industrial level: ~280 ppm (stable for ~1,700 years)
- Industrial era: Rapid rise starting ~1850
- Current level: ~419 ppm (**50% above pre-industrial**)

## Figures

### Figure 1: Overview
Shows observed monthly data, extracted trend component, and deseasonalized data (seasonal removed).

### Figure 2: Seasonal Decomposition
4-panel figure showing:
1. Observed time series
2. Trend component (smooth upward trajectory)
3. Seasonal component (repeating annual cycle)
4. Residual component (unexplained variation)

### Figure 3: Growth Rate & Acceleration
Dual-panel showing:
1. Annual growth rate (ppm/year) over time
2. Acceleration (second derivative, ppm/year²)

Both show clear upward trends, indicating the problem is getting worse faster.

### Figure 4: Historical Context
1,869 years of CO₂ from ice core records merged with modern measurements, showing:
- Long pre-industrial stability (~280 ppm)
- Dramatic modern rise
- Current levels unprecedented in recorded history

### Figure 5: Seasonal Analysis
Dual-panel showing:
1. Average seasonal cycle across all years (with error bars)
2. How the seasonal cycle has shifted upward from 1950s to 2020s

## Data Sources

- **Modern measurements**: Scripps CO₂ Program, Mauna Loa Observatory
  - URL: https://scrippsco2.ucsd.edu
- **Historical data**: Ice core records (Law Dome) merged with modern measurements
  - Citation: Rubino et al. (2019), CSIRO, https://doi.org/10.25919/5bfe29ff807fb

## Methods

This analysis uses standard time series analysis techniques:

1. **Seasonal Decomposition** (statsmodels `seasonal_decompose`)
2. **Trend Analysis** (linear and quadratic regression via scipy)
3. **Growth Rate** (first derivative: year-over-year change)
4. **Acceleration** (second derivative: change in growth rate)
5. **Residual Analysis** (normality tests, variance decomposition)

## About This Demo

This is an **advanced version** of the Keeling Curve demo project for the Data Engineering Workshop. It demonstrates:

- How to go beyond basic plotting to publication-quality analysis
- Proper time series decomposition methods
- How to communicate climate data effectively
- Professional data visualization techniques

Students will:
1. **Part 1 (Manual)**: Build a simpler version by hand to understand fundamentals
2. **Part 2 (AI-Assisted)**: Use Gemini CLI to accelerate development
3. **Part 3 (Advanced, Optional)**: Study this implementation to see professional techniques

This code can serve as a template for analyzing other climate time series (temperature, sea level, Arctic ice extent, etc.).
