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
