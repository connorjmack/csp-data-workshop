# Essential Terminal Commands

A reference of the commands you'll use most often as a data engineer. Bookmark this page.

---

## File & Directory Operations

| Command | What it does | Example |
|---------|-------------|---------|
| `mkdir` | Create a directory | `mkdir my-project` |
| `mkdir -p` | Create nested directories | `mkdir -p src/data/raw` |
| `touch` | Create an empty file | `touch script.py` |
| `cp` | Copy a file | `cp data.csv backup.csv` |
| `cp -r` | Copy a directory | `cp -r src/ src-backup/` |
| `mv` | Move or rename | `mv old.txt new.txt` |
| `rm` | Delete a file | `rm unwanted.txt` |
| `rm -r` | Delete a directory | `rm -r old-project/` |

!!! danger "Be careful with `rm`"
    There is no trash can in the terminal. `rm` deletes permanently. Always double-check before running `rm -r` on a directory.

---

## Viewing File Contents

```bash
# Print the entire file
cat data.csv

# View with scrolling (press q to quit)
less data.csv

# See the first 10 lines
head data.csv

# See the first 20 lines
head -n 20 data.csv

# See the last 10 lines
tail data.csv

# Watch a file update in real time (great for logs)
tail -f app.log
```

---

## Searching & Filtering

```bash
# Find text in a file
grep "CO2" data.csv

# Find text, case-insensitive
grep -i "carbon" README.md

# Find files by name
find . -name "*.py"

# Count lines in a file
wc -l data.csv
```

---

## Pipes and Redirection

Pipes (`|`) connect the output of one command to the input of another. This is one of the most powerful ideas in the terminal.

```bash
# Count how many Python files you have
find . -name "*.py" | wc -l

# Find lines with "error" in a log, show just the first 5
grep "error" app.log | head -n 5

# Sort a CSV and save to a new file
sort data.csv > sorted_data.csv

# Append output to a file (instead of overwriting)
echo "new line" >> notes.txt
```

---

## Environment & System

```bash
# See environment variables
env

# Print a specific variable
echo $HOME
echo $PATH

# See running processes
ps aux

# Check disk space
df -h

# Check folder size
du -sh my-project/
```

---

## Python-Specific Commands

Since we'll be using Python with Conda in the demo project:

```bash
# Check Python version
python --version

# Create a conda environment
conda create -n myproject python=3.12 -y

# Activate it
conda activate myproject

# Install packages
conda install pandas matplotlib -y

# Or use pip inside the conda environment
pip install some-package

# Run a script
python my_script.py

# Deactivate the conda environment
conda deactivate
```

---

## Keyboard Shortcuts

These work in most terminals and will save you a lot of time:

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete file/folder names |
| `Ctrl + C` | Cancel the current command |
| `Ctrl + L` | Clear the screen |
| `Ctrl + A` | Jump to the beginning of the line |
| `Ctrl + E` | Jump to the end of the line |
| `Up Arrow` | Previous command |
| `Ctrl + R` | Search command history |

---

## Quick Reference Card

??? abstract "Cheat sheet — click to expand"

    ```
    NAVIGATE           FILES              VIEW
    pwd                mkdir dir          cat file
    ls / ls -la        touch file         less file
    cd dir             cp src dst         head file
    cd ..              mv src dst         tail file
    cd ~               rm file            grep pat file

    PIPES              CONDA/PYTHON       SHORTCUTS
    cmd1 | cmd2        conda create -n x  Tab    = autocomplete
    cmd > file         conda activate x   Ctrl+C = cancel
    cmd >> file        conda install pkg  Ctrl+L = clear
    cmd 2>&1           python script.py   Ctrl+R = search history
    ```

---

**Next:** [Gemini Pro Student Login →](01a-gemini-login.md)
