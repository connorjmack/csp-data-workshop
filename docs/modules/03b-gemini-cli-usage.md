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
