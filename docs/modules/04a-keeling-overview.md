# Demo Project: The Keeling Curve

## What You'll Build

In this module, you'll build a complete data pipeline that downloads, cleans, analyzes, and visualizes one of the most important datasets in climate science — the **Keeling Curve**.

You'll do it **twice**:

1. **Part 1 — Manual:** Write the Python code yourself, step by step
2. **Part 2 — AI-Assisted:** Rebuild it using Gemini CLI to see how AI accelerates the workflow

---

## What is the Keeling Curve?

In 1958, scientist Charles David Keeling began measuring atmospheric CO₂ concentration at the Mauna Loa Observatory in Hawaii. His continuous measurements revealed a clear, relentless upward trend in CO₂ — now known as the **Keeling Curve**.

The dataset shows two key patterns:

- A **seasonal cycle** — CO₂ dips each northern hemisphere summer as plants absorb it, then rises in winter
- A **long-term upward trend** — atmospheric CO₂ has risen from ~315 ppm in 1958 to over 425 ppm today

This dataset is publicly available from the Scripps Institution of Oceanography.

---

## Project Pipeline

Here's what your code will do:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Download   │───▶│    Clean     │───▶│   Analyze    │───▶│  Visualize   │
│  raw CSV     │    │  & parse     │    │  trends      │    │  & save      │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

| Stage | What happens |
|-------|-------------|
| **Download** | Fetch the raw CSV from Scripps/NOAA |
| **Clean** | Handle missing values, parse dates, set data types |
| **Analyze** | Calculate annual averages, growth rate, seasonal amplitude |
| **Visualize** | Plot the full curve, seasonal cycle, and trend |

---

## Project Setup

Before starting either part, set up your project:

```bash
# Navigate to your workshop repo
cd ~/projects/data-engineering-workshop

# Create a directory for the demo
mkdir -p keeling-curve
cd keeling-curve

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

# Install dependencies
pip install pandas matplotlib requests
```

Create a `requirements.txt` file:

```bash
echo "pandas
matplotlib
requests" > requirements.txt
```

Your project structure should look like:

```
keeling-curve/
├── venv/
├── requirements.txt
└── (your scripts will go here)
```

---

## Ready?

Choose your path:

- [**Part 1: Manual Python Approach →**](04b-keeling-manual.md) — Write the code yourself
- [**Part 2: AI-Assisted with Gemini CLI →**](04c-keeling-gemini.md) — Let AI help you build it

!!! tip "Recommended order"
    Do Part 1 first to understand the data and the code, then do Part 2 to see how Gemini CLI can speed things up. The contrast is the whole point!
