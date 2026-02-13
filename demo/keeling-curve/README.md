# Keeling Curve Data Pipeline

This is a complete example implementation of the Keeling Curve data pipeline from the Data Engineering Workshop.

## What is the Keeling Curve?

The Keeling Curve is a graph that shows the continuous measurement of atmospheric CO₂ concentration at Mauna Loa Observatory in Hawaii since 1958. It's named after scientist Charles David Keeling who began the measurements.

## Project Structure

```
keeling-curve/
├── fetch_data.py              # Downloads raw CO₂ data from Scripps
├── clean_data.py              # Cleans and parses the CSV data
├── analyze.py                 # Computes statistics and trends
├── visualize.py               # Generates plots
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files to exclude from git
├── co2_monthly.csv            # Raw data (not committed)
├── co2_clean.csv              # Cleaned data (not committed)
├── keeling_curve_full.png     # Full time series plot (not committed)
├── keeling_curve_seasonal.png # Seasonal cycle plot (not committed)
└── keeling_curve_decades.png  # Decade comparison plot (not committed)
```

## Setup

This example uses conda for environment management:

```bash
# Create a conda environment
conda create -n keeling-demo python=3.12 -y

# Activate it
conda activate keeling-demo

# Install dependencies
conda install pandas matplotlib requests -y
```

## Running the Pipeline

Run each script in order:

```bash
# 1. Download the data
python fetch_data.py

# 2. Clean and parse it
python clean_data.py

# 3. Analyze the trends
python analyze.py

# 4. Create visualizations
python visualize.py
```

## Key Findings

Based on the analysis of data from 1958 to 2025:

- **Total CO₂ increase:** ~112 ppm (from ~315 ppm to ~427 ppm)
- **Growth rate is accelerating:**
  - 1950s: +0.65 ppm/year
  - 1980s: +1.58 ppm/year
  - 2020s: +2.60 ppm/year
- **Seasonal cycle:** ~6 ppm amplitude
  - Peak: May-June (northern hemisphere spring/summer)
  - Trough: September-October (after northern hemisphere growing season)

## Data Source

Data comes from the Scripps CO₂ Program at UC San Diego:
https://scrippsco2.ucsd.edu/data/atmospheric_co2/

## About This Demo

This is the manual implementation from **Part 1** of the Keeling Curve module. Students will write this code themselves to understand:

1. How to download data from a public API
2. How to clean messy real-world data
3. How to compute meaningful statistics
4. How to create clear visualizations

The workshop also includes **Part 2**, where students rebuild this same pipeline using AI assistance (Gemini CLI) to compare the two approaches.
