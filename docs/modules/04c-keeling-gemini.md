# Part 2: AI-Assisted with Gemini CLI

Now let's rebuild the same pipeline — but this time, you'll use Gemini CLI as your coding partner. The goal is to see how AI-assisted coding changes the workflow, not to skip learning.

!!! tip "Do Part 1 first"
    If you haven't completed [Part 1](04b-keeling-manual.md) yet, do that first. Understanding the data and code manually makes you a much better AI collaborator.

---

## Setup

Start fresh so we can compare the two approaches:

```bash
# Create a separate directory
cd ~/projects/data-engineering-workshop
mkdir keeling-curve-ai
cd keeling-curve-ai

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Start Gemini CLI
gemini
```

---

## Prompt 1: Scaffold the Project

Start with a high-level description of what you want:

```
I'm building a data pipeline to analyze the Keeling Curve CO₂ dataset.
The data is available at:
https://scrippsco2.ucsd.edu/assets/data/atmospheric/stations/in_situ_co2/monthly/monthly_in_situ_co2_mlo.csv

Create a project structure with these scripts:
1. fetch_data.py - download the raw CSV
2. clean_data.py - parse and clean it (handle comment lines starting with ", missing values as -99.99)
3. analyze.py - compute annual averages, growth rate by decade, and seasonal amplitude
4. visualize.py - plot the full curve, seasonal cycle, and decade comparison
5. requirements.txt - list dependencies

Also create a run_pipeline.py that executes all steps in order.
```

!!! note "What to watch for"
    Observe how Gemini structures the code. Compare it to your manual approach:

    - Does it handle edge cases you didn't think of?
    - Does it organize the code differently?
    - Is the code more or less readable?

---

## Prompt 2: Review and Improve

After Gemini creates the files, ask it to improve them:

```
Review the code you just created. Are there any:
1. Missing error handling?
2. Edge cases that could cause failures?
3. Best practices we're not following?

Fix any issues you find.
```

---

## Prompt 3: Run the Pipeline

Ask Gemini to run everything:

```
Run the complete pipeline: fetch the data, clean it, analyze it, and create all the visualizations.
Show me the analysis output.
```

When Gemini asks permission to run commands, review them and approve.

---

## Prompt 4: Add Something New

Now push beyond what you did manually. Ask for something extra:

```
Add a new analysis: calculate the rate of acceleration.
Is CO₂ increasing faster now than it was in the 1960s?
Create a plot that shows the annual growth rate over time with a trend line.
```

This is where AI assistance really shines — you can rapidly iterate on ideas without writing boilerplate.

---

## Prompt 5: Documentation

Ask Gemini to document the project:

```
Create a README.md for this project that explains:
- What the Keeling Curve is
- How to set up and run the pipeline
- What each script does
- Sample output/findings
```

---

## Prompt 6: Git Workflow

Finally, commit everything:

```
Create a .gitignore for this Python data project, then stage and commit everything
with a descriptive commit message.
```

---

## Comparing the Two Approaches

After completing both parts, take a moment to reflect:

| Aspect | Manual (Part 1) | AI-Assisted (Part 2) |
|--------|-----------------|---------------------|
| **Time** | ~45 minutes | ~15 minutes |
| **Understanding** | Deep — you wrote every line | Moderate — you reviewed, not wrote |
| **Error handling** | Only what you thought of | Often more comprehensive |
| **Code quality** | Depends on your experience | Generally follows best practices |
| **Creativity** | Limited by what you know | Can suggest approaches you haven't seen |
| **Debugging** | You own the mental model | Need to read and understand generated code |

!!! abstract "Key takeaway"
    AI coding assistants are **most powerful when you understand the fundamentals**. Part 1 gave you that understanding. Part 2 showed how to leverage AI to move faster — while still being the one making decisions.

---

## Bonus Challenges

If you have extra time, try these prompts in Gemini CLI:

??? example "Challenge 1: Anomaly detection"
    ```
    Analyze the Keeling Curve data for anomalies.
    Are there any months where CO₂ deviated significantly from the expected trend?
    What might have caused those deviations?
    Create a plot highlighting the anomalies.
    ```

??? example "Challenge 2: Future projection"
    ```
    Based on the historical Keeling Curve data, fit a model to project
    CO₂ levels to 2050. Use both a linear and a polynomial fit.
    Plot the historical data and both projections.
    Add a horizontal line at 450 ppm (a commonly discussed threshold).
    ```

??? example "Challenge 3: Interactive dashboard"
    ```
    Create an interactive HTML dashboard using Plotly that shows:
    1. The full Keeling Curve with hover data
    2. A dropdown to filter by decade
    3. A seasonal decomposition chart
    Save it as dashboard.html
    ```

---

**Next:** [Wrap-Up & Next Steps →](04d-wrapup.md)
