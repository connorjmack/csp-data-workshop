# Using Gemini CLI

Now that Gemini CLI is installed, let's learn how to use it effectively. This page covers the core commands and patterns you'll need for the demo project.

---

## Starting a Session

Navigate to your project directory first, then start Gemini:

```bash
cd ~/projects/data-engineering-workshop
gemini
```

!!! tip "Always start in your project folder"
    Gemini CLI is context-aware — it can see and work with files in your current directory. Starting it inside your project gives it the context it needs.

---

## Core Interaction Patterns

### Asking questions

Just type naturally. Gemini understands context:

```
What files are in this directory?
```

```
Explain what a CSV file is
```

### Asking it to write code

Be specific about what you want:

```
Create a Python script called hello.py that prints "Hello, Data Engineering!"
```

```
Write a function that reads a CSV file and returns the number of rows
```

### Asking it to explain code

Paste or reference code and ask for explanations:

```
Explain what this line does: df.groupby('year')['co2'].mean()
```

### Asking it to fix errors

Copy an error message and ask for help:

```
I'm getting this error: ModuleNotFoundError: No module named 'pandas'
How do I fix it?
```

---

## Useful Slash Commands

Gemini CLI has built-in commands that start with `/`:

| Command | What it does |
|---------|-------------|
| `/help` | Show available commands |
| `/quit` | Exit Gemini CLI |
| `/chat` | Start a new conversation (clears context) |
| `/stats` | Show usage statistics for the session |

---

## Managing Context

One of the most important skills when working with AI assistants is knowing when to **keep building** on your conversation versus when to **start fresh**. Think of it like tabs in your browser — sometimes you want to keep working in the same tab, sometimes you need to open a new one.

### When to Keep Building in the Same Session

**Continue the conversation when:**

- **Iterating on the same file** — You're refining a script, adding features incrementally, or fixing bugs
  ```
  You: Create a script to load co2_data.csv
  [Gemini creates basic_load.py]

  You: Now add a function to calculate monthly averages
  [Gemini adds to the same file, knowing what's already there]

  You: Add error handling for missing files
  [Gemini builds on the previous additions]
  ```

- **Working within the same project context** — Multiple files that relate to each other
  ```
  You: Create fetch_data.py to download from this API
  You: Now create process_data.py that uses the output from fetch_data.py
  You: Create a README explaining how to run both scripts in order
  ```

- **The AI needs memory of earlier decisions** — You want it to remember choices you made
  ```
  You: Use matplotlib for plotting, not seaborn
  [Later in same session]
  You: Create another visualization
  [Gemini remembers to use matplotlib]
  ```

**The benefit:** Gemini maintains context about variable names, function signatures, file paths, and your preferences. It can reference earlier work without you having to re-explain.

### When to Start Fresh with `/chat`

**Use `/chat` to clear context when:**

- **Switching topics entirely** — Moving from one project to a completely different one
  ```
  You've been working on a CO₂ analysis script for 20 minutes
  Now you want help with something totally unrelated

  → Type /chat before switching to the new topic
  ```

- **The conversation gets cluttered** — Too many tangents, failed attempts, or abandoned ideas
  ```
  You tried 3 different approaches to parse dates
  Each attempt is still in the conversation history
  Gemini keeps referencing the old failed attempts

  → Type /chat to clear the clutter and start with the working solution
  ```

- **You hit an error loop** — The AI keeps suggesting the same broken fix
  ```
  You: This import isn't working
  Gemini: Try pip install X
  You: Still doesn't work
  Gemini: Try pip install X again
  You: [frustrated] Still failing!

  → Type /chat, then rephrase: "I have pandas installed but getting
     ImportError: cannot import name 'DataFrame'. Here's my full error..."
  ```

- **You want a second opinion** — Start fresh to see if Gemini suggests a different approach
  ```
  Current session suggested using regex for parsing
  You're not sure if that's the best way

  → Type /chat and ask: "What are different ways to extract
     year-month from strings like '2024-Jan'?"
  ```

**The benefit:** A clean slate prevents confusion and lets you reframe the problem more clearly.

### How Much Context is "Too Much"?

**Signs you might have too much context:**

1. **Gemini references old, irrelevant code** — It keeps mentioning files or variables you've moved past
2. **Responses get slower** — Processing a large conversation history takes time
3. **You can't remember what you asked 10 turns ago** — If you're lost, Gemini might be too
4. **You've been in the same session for 30+ minutes across multiple different tasks**

**Rule of thumb:**

- **Short focused tasks (5-10 turns)** → Keep building
- **Complex multi-step tasks within one project (15-25 turns)** → Keep building, it's worth the context
- **Multiple unrelated tasks or errors piling up (25+ turns)** → Consider starting fresh
- **Switching projects** → Always use `/chat`

**Pro tip:** If you're unsure, you can always save your work (Gemini creates the files for you), use `/chat` to start fresh, and then say "I have a file called analyze.py [paste code]. How can I add feature X?"

### Practical Example: Context Decisions

```
Session 1: Building CO₂ analysis script
───────────────────────────────────────
Turn 1: "Create script to load co2_data.csv"
Turn 2: "Add a line plot of CO₂ over time"
Turn 3: "Fix the date parsing error"
Turn 4: "Add axis labels and title"
Turn 5: "Save as co2_plot.png"

✅ Good to keep building! Same project, each step builds on the last.

Turn 6: "Actually, can you help me with my Python homework? I need to
         write a function that checks if a number is prime"

❌ Stop! Use /chat first — this is a completely different topic.
```

**After using `/chat`:**

```
Session 2: Prime number homework
──────────────────────────────────
Turn 1: "Write a function to check if a number is prime"
Turn 2: "Add error handling for negative numbers"
Turn 3: "Write unit tests for this function"

✅ Keep building — all related to the same homework problem.

[Homework done, you want to get back to the CO₂ project]

Turn 4: "Back to my CO₂ project. Can you modify the plotting script
         to show a trend line?"

🤔 This might work, but Gemini has no context about the CO₂ project
   anymore. Better option:

→ /chat
→ "I have a Python script analyze_co2.py [paste code]. Can you add
   a polynomial trend line to this plot?"
```

!!! tip "When in doubt, err on the side of keeping context"
    For students working through the Keeling Curve demo, you'll likely work in **one continuous session** for the entire project. That's perfect! The context helps Gemini understand your data, your file names, and your goals.

---

## Working with Files

One of Gemini CLI's strengths is working with your actual project files.

### Reading files

```
Read the file data.csv and summarize its contents
```

```
What does the script analyze.py do?
```

### Creating files

```
Create a Python script called fetch_data.py that downloads CSV data from a URL
```

Gemini will show you the code and ask permission before creating the file.

### Modifying files

```
Add error handling to the fetch_data.py script
```

```
Refactor analyze.py to use functions instead of top-level code
```

---

## Permission Model

Gemini CLI will ask permission before:

- Running shell commands
- Creating or modifying files
- Installing packages

You'll see a prompt like:

```
Gemini wants to run: pip install pandas
Allow? (y/n)
```

!!! warning "Review before approving"
    Always read what Gemini wants to do before typing `y`. This is a good habit — understand the code before running it.

---

## Tips for Effective Prompting

**Be specific:** Instead of "make a script," say "create a Python script that reads `co2_data.csv`, calculates the annual average CO₂ concentration, and saves a line chart as `co2_trend.png`."

**Give context:** "I'm working on a data pipeline for climate data. The input is a CSV with columns: year, month, co2_ppm."

**Iterate:** Start simple, then ask for improvements:

1. "Write a basic script to load the CSV"
2. "Now add a plot of CO₂ over time"
3. "Add proper axis labels and a title"
4. "Save the plot as a PNG file"

**Ask it to explain:** If you don't understand what it produced, ask! "Why did you use `pd.to_datetime()` here?"

---

## Data Engineering with Gemini CLI

Since this is a data engineering workshop, let's look at specific patterns for working with data. These examples show how to use Gemini CLI for the most common data tasks you'll encounter.

### Reading and Exploring CSV Files

**Basic loading:**

```
Load the file weather_data.csv and show me the first few rows
```

Gemini will read the file and display a sample. You can then follow up:

```
What columns does this CSV have?
```

```
Are there any missing values in this dataset?
```

**More specific exploration:**

```
Create a Python script that:
1. Loads climate_data.csv using pandas
2. Prints the shape (rows and columns)
3. Shows data types for each column
4. Displays summary statistics
```

Gemini will generate something like:

```python
import pandas as pd

df = pd.read_csv('climate_data.csv')
print(f"Shape: {df.shape}")
print("\nData types:")
print(df.dtypes)
print("\nSummary statistics:")
print(df.describe())
```

!!! tip "Ask for explanations"
    If you see unfamiliar pandas methods, ask! "What does `df.describe()` do?" or "Why use `pd.read_csv()` instead of just `open()`?"

### Handling Missing Data

**Identifying problems:**

```
I have a CSV file called sensor_readings.csv. Check if there are any missing
values and tell me which columns have them.
```

**Asking for solutions:**

```
The 'temperature' column has missing values. Show me different ways to handle
them: dropping rows, filling with mean, or forward-filling.
```

Gemini will show you multiple approaches:

```python
# Option 1: Drop rows with missing temperature
df_cleaned = df.dropna(subset=['temperature'])

# Option 2: Fill with column mean
df['temperature'].fillna(df['temperature'].mean(), inplace=True)

# Option 3: Forward fill (use previous valid value)
df['temperature'].fillna(method='ffill', inplace=True)
```

**Follow-up questions:**

```
Which approach is best for time-series sensor data?
```

```
What's the difference between inplace=True and creating a new dataframe?
```

### Data Cleaning Operations

**Date parsing:**

```
My CSV has a column called 'date' with values like "2024-Jan-15". Convert this
to proper datetime objects.
```

**Filtering and subsetting:**

```
Create a script that:
1. Loads co2_measurements.csv
2. Filters to only rows where year >= 2000
3. Keeps only the columns: date, co2_ppm, location
4. Saves the result as co2_recent.csv
```

**Renaming and reformatting:**

```
The column names in my CSV have spaces and capital letters like "CO2 Level".
Rename all columns to lowercase with underscores instead of spaces.
```

Gemini will suggest:

```python
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

**Dealing with duplicates:**

```
Check if my dataset has duplicate rows and remove them if it does
```

**Type conversions:**

```
The 'year' column is being read as text but I need it as integers.
How do I convert it?
```

### Creating Visualizations

**Basic plotting:**

```
Create a line plot of CO₂ concentration over time from my co2_data.csv file.
Use the 'year' column for x-axis and 'co2_ppm' for y-axis.
```

**Customizing plots:**

```
Improve this plot with:
- Title: "Atmospheric CO₂ Concentration (1958-2024)"
- X-axis label: "Year"
- Y-axis label: "CO₂ (ppm)"
- Grid lines
- Figure size 12x6 inches
```

**Multiple visualizations:**

```
Create three subplots showing:
1. Line chart of CO₂ over time
2. Histogram of CO₂ values
3. Box plot of CO₂ by decade
Save as co2_analysis.png
```

Gemini will generate matplotlib code with proper subplot layout:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: Time series
axes[0].plot(df['year'], df['co2_ppm'])
axes[0].set_title('CO₂ Over Time')

# Plot 2: Histogram
axes[1].hist(df['co2_ppm'], bins=30)
axes[1].set_title('CO₂ Distribution')

# Plot 3: Box plot by decade
df['decade'] = (df['year'] // 10) * 10
df.boxplot(column='co2_ppm', by='decade', ax=axes[2])

plt.tight_layout()
plt.savefig('co2_analysis.png', dpi=300, bbox_inches='tight')
```

**Styling and aesthetics:**

```
Use a scientific color scheme and make the plot publication-ready
```

```
Add a trend line to show the overall increase
```

### Exporting Results

**Saving processed data:**

```
After cleaning my data, save it as:
1. A new CSV file called 'cleaned_data.csv'
2. An Excel file with the sheet name 'Climate Data'
```

**Creating summary reports:**

```
Calculate these summary statistics and save them to summary_stats.txt:
- Mean CO₂ by decade
- Year with highest CO₂
- Total increase from 1958 to 2024
- Average annual rate of change
```

**Exporting multiple outputs:**

```
Create a script that:
1. Processes raw_weather.csv
2. Saves cleaned data as processed_weather.csv
3. Generates a visualization as temp_trend.png
4. Writes a summary report as analysis_summary.txt

Put all outputs in a folder called 'results/'
```

Gemini will structure this with proper file organization:

```python
import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output directory
os.makedirs('results', exist_ok=True)

# Load and process data
df = pd.read_csv('raw_weather.csv')
# ... cleaning steps ...

# Save cleaned data
df.to_csv('results/processed_weather.csv', index=False)

# Generate visualization
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature'])
plt.savefig('results/temp_trend.png', dpi=300)

# Write summary
with open('results/analysis_summary.txt', 'w') as f:
    f.write(f"Mean temperature: {df['temperature'].mean():.2f}\n")
    # ... more stats ...
```

### Common Data Workflows

Here are complete prompts for typical data engineering tasks:

**Data pipeline from scratch:**

```
I have a CSV file at https://example.com/climate_data.csv

Create a Python script that:
1. Downloads the CSV
2. Loads it with pandas
3. Removes rows with missing 'temperature' values
4. Converts the 'date' column to datetime
5. Calculates monthly averages
6. Creates a line plot of average temperature by month
7. Saves the plot as 'monthly_temps.png'
8. Exports the monthly averages to 'monthly_summary.csv'

Include error handling for the download step.
```

**Combining multiple files:**

```
I have three CSV files: jan_data.csv, feb_data.csv, mar_data.csv
Each has the same columns: date, temperature, humidity

Create a script that:
1. Loads all three files
2. Combines them into one dataframe
3. Sorts by date
4. Removes any duplicate dates (keep first occurrence)
5. Saves as 'q1_combined.csv'
```

**Data quality checks:**

```
Create a script that validates my sensor_data.csv file:
- Check for missing values in required columns: timestamp, sensor_id, reading
- Verify all timestamps are in the format YYYY-MM-DD HH:MM:SS
- Check that all readings are between 0 and 100
- Flag any sensor_ids that appear fewer than 10 times
- Print a report of any issues found
```

!!! success "Iterative refinement works great for data tasks"
    Start with basic loading and exploration, then gradually add cleaning, analysis, and visualization steps. Each iteration builds on the previous code, and Gemini maintains context about your dataset structure.

### Debugging Data Issues

When things go wrong, Gemini CLI excels at helping you debug:

**Column name errors:**

```
I'm getting KeyError: 'CO2'. Here's my code: [paste code]
What's wrong?
```

Gemini might spot: "Your CSV has a column called 'co2' (lowercase), but you're trying to access 'CO2' (uppercase). Python is case-sensitive."

**Type errors:**

```
TypeError: unsupported operand type(s) for /: 'str' and 'int'

This happens when I try: df['value'] / 100

Why?
```

**Shape mismatches:**

```
I'm trying to create a plot but getting: ValueError: x and y must have same first dimension

Here's my code: [paste code]
```

**Data format issues:**

```
My dates look like "15-Jan-2024" but pd.to_datetime() isn't parsing them correctly.
How do I specify the format?
```

Gemini will explain the format string:

```python
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%Y')
```

---

## Advanced Workflows: Agentic Development

As you get more comfortable with AI coding assistants, you can adopt patterns that treat the AI as a collaborator on larger projects. These workflows help maintain consistency and structure as projects grow.

### The `gemini.md` File

Similar to how you might have a README for humans, a `gemini.md` file provides instructions specifically for Gemini CLI. When Gemini starts in a directory containing `gemini.md`, it reads this file first to understand your project's context and preferences.

**What goes in `gemini.md`:**

- Project overview and purpose
- Coding standards (formatting, naming conventions, error handling)
- File structure explanations
- Dependencies and environment setup
- Things to ask before doing (like adding dependencies or changing schemas)
- Common commands and workflows

**Example `gemini.md`:**

```markdown
# Weather Data Pipeline Project

## Overview
This project fetches and analyzes historical weather data from NOAA.

## Code Standards
- Use pandas for data processing
- All dates should be in ISO 8601 format (YYYY-MM-DD)
- Save plots to `outputs/` directory
- Match existing file style over PEP 8

## Ask Before
- Adding new dependencies to requirements.txt
- Changing the data directory structure
- Modifying any file in `config/`

## Project Structure
- `fetch/` — scripts to download data
- `process/` — data cleaning and transformation
- `analyze/` — statistical analysis and visualization
- `outputs/` — generated charts and reports
```

!!! tip "Why this matters"
    Without `gemini.md`, you'd have to re-explain your project structure and preferences in every session. With it, Gemini automatically knows your conventions and can make better decisions.

### The `plan.md` / `todo.md` Workflow

For larger projects, many developers use a two-file system for planning and execution:

**`plan.md` — The Design Document**

This is your Product Requirements Document (PRD). It contains:

- **What** you're building and **why**
- High-level architecture and design decisions
- Key features and requirements
- Technical constraints
- Initial task breakdown

Think of it as the blueprint. It changes rarely — usually only when requirements shift.

**`todo.md` — The Living Checklist**

This is derived from `plan.md` but updates constantly as you work:

- Concrete, actionable tasks (often seeded from the plan)
- Current status: pending, in progress, completed
- Blockers and dependencies
- Notes and decisions made during development

**Example workflow:**

1. **Start with planning:**
   ```
   I'm building a CO₂ data pipeline. Help me create a plan.md with:
   - Overview of the project
   - Required features (fetch data, clean it, visualize trends, export results)
   - Tech stack (Python, pandas, matplotlib)
   - Task breakdown
   ```

2. **Generate the todo list:**
   ```
   Based on plan.md, create todo.md with specific tasks
   ```

3. **Work through tasks:**
   ```
   Let's tackle the first pending task in todo.md
   ```

4. **Update as you go:**
   ```
   Mark task #3 as completed and add a new task: "Add error handling for missing data"
   ```

**Sample `todo.md` structure:**

```markdown
# TODO: Weather Data Pipeline

## Setup
- [x] Create project structure
- [x] Set up conda environment
- [x] Install pandas, matplotlib, requests
- [ ] Create gemini.md with project conventions

## Data Fetching
- [x] Write fetch_noaa.py to download CSV from API
- [ ] Add retry logic for failed downloads
- [ ] Add validation: check if CSV has expected columns

## Processing
- [ ] Parse dates into datetime objects
- [ ] Handle missing values (interpolate or drop?)
- [ ] Calculate monthly averages

## Visualization
- [ ] Line chart: temperature over time
- [ ] Save to outputs/temp_trend.png

## Documentation
- [ ] Add docstrings to all functions
- [ ] Update README with usage instructions
```

!!! success "The power of this workflow"
    The AI can now work **autonomously** through your checklist. You say "work on the next pending task" and it knows exactly what to do, staying aligned with your original plan.

### Combining It All

Here's how these pieces work together:

1. **`gemini.md`** — "This is how we work on this project"
2. **`plan.md`** — "This is what we're building and why"
3. **`todo.md`** — "This is what's left to do"

With this structure in place, you can have conversations like:

```
Review plan.md and todo.md. What should we work on next?
```

```
According to our gemini.md conventions, refactor the data processing
module to match our error handling standards
```

The AI becomes a more effective collaborator because it has **persistent context** about your project.

---

## Practice Exercise

Try this sequence in Gemini CLI:

```
1. Create a Python script called practice.py that generates 100 random
   numbers and saves them to a file called random_numbers.txt

2. Now modify practice.py to also calculate and print the mean,
   median, and standard deviation

3. Add a histogram plot saved as histogram.png
```

!!! success "If you got through all three prompts, you're ready for the demo project!"

---

**Next:** [Keeling Curve Demo — Overview →](04a-keeling-overview.md)
