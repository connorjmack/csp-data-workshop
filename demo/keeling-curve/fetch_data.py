"""
fetch_data.py — Download Keeling Curve and historical CO2 datasets.
"""

import requests
import os

# Modern Mauna Loa monthly measurements (1958-present)
MONTHLY_URL = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv"
MONTHLY_FILE = "co2_monthly.csv"

# Merged ice core and modern data (800,000 years to present)
# This gives us the long-term context
HISTORICAL_URL = "https://scrippsco2.ucsd.edu/assets/data/atmospheric/merged_ice_core_mlo_spo/merged_ice_core_yearly.csv"
HISTORICAL_FILE = "co2_historical.csv"


def download_data(url: str, output_path: str) -> None:
    """Download a CSV file from a URL."""
    print(f"Downloading from {url}...")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(output_path, "w") as f:
            f.write(response.text)

        print(f"✓ Saved to {output_path} ({len(response.text):,} bytes)")
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to download {url}: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("DOWNLOADING KEELING CURVE DATA")
    print("=" * 60)
    print()

    # Download modern monthly data
    download_data(MONTHLY_URL, MONTHLY_FILE)
    print()

    # Download historical data
    download_data(HISTORICAL_URL, HISTORICAL_FILE)
    print()
    print("All downloads complete!")
