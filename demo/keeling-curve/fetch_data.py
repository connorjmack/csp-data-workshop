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
