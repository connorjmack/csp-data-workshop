# Conda & Python Installation

Before we start coding, you need **Python** and a way to manage packages and environments. We'll use **Conda** — the standard tool for this in data science and engineering.

---

## What is Conda?

Conda is a **package manager** and **environment manager** rolled into one. Think of it this way:

- A **package manager** installs software for you (like `pip install pandas`, but broader — Conda can install Python itself, R, C libraries, and more)
- An **environment manager** creates isolated "sandboxes" so that different projects can use different versions of packages without conflicting

### Why does this matter?

Imagine you have two projects:

- **Project A** needs `pandas 1.5` and `Python 3.9`
- **Project B** needs `pandas 2.1` and `Python 3.12`

Without environments, installing one would break the other. Conda solves this by creating separate environments for each project:

```
┌─────────────────────┐    ┌─────────────────────┐
│ Environment: proj_a  │    │ Environment: proj_b  │
│ Python 3.9           │    │ Python 3.12          │
│ pandas 1.5           │    │ pandas 2.1           │
│ numpy 1.24           │    │ numpy 1.26           │
└─────────────────────┘    └─────────────────────┘
```

Each environment is completely independent. You switch between them with a single command.

### Conda vs. pip

| Feature | Conda | pip |
|---------|-------|-----|
| Installs Python itself | Yes | No |
| Manages non-Python packages (C libs, R, etc.) | Yes | No |
| Environment management built in | Yes | No (needs `venv` separately) |
| Resolves dependency conflicts | Yes (thorough) | Partially |
| Package source | Anaconda / conda-forge channels | PyPI |
| Speed | Slower (more thorough) | Faster |

!!! tip "You'll use both"
    In practice, data engineers use Conda to manage environments and install core packages, then use `pip` inside a Conda environment for Python-only packages that aren't on conda-forge.

---

## Miniforge vs. Anaconda vs. Miniconda

There are several Conda distributions. Here's the difference:

| Distribution | What it includes | Best for |
|-------------|-----------------|----------|
| **Miniforge** | Conda + conda-forge defaults | Recommended — lightweight, open-source |
| **Miniconda** | Conda + Anaconda defaults | Lightweight, uses Anaconda channel |
| **Anaconda** | Conda + 250+ pre-installed packages | Beginners who want everything pre-installed |

**We recommend Miniforge** — it's lightweight, uses the community-maintained `conda-forge` channel by default, and is fully open-source.

---

## Install Miniforge

=== "macOS"

    ```bash
    # Download and run the installer
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

    Follow the prompts:

    - Press **Enter** to review the license, then type `yes`
    - Accept the default install location (`~/miniforge3`)
    - Type `yes` when asked to initialize Miniforge (this adds it to your shell)

    Then restart your terminal, or run:

    ```bash
    source ~/.bashrc   # or ~/.zshrc on macOS
    ```

=== "Windows"

    1. Download the installer from [github.com/conda-forge/miniforge/releases](https://github.com/conda-forge/miniforge/releases/latest)
        - Choose `Miniforge3-Windows-x86_64.exe`
    2. Run the installer
        - Check **"Add Miniforge3 to my PATH environment variable"**
        - Check **"Register Miniforge3 as my default Python"**
    3. Open a new **Command Prompt** or **PowerShell** window

=== "Linux"

    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

    Follow the same prompts as macOS. Restart your terminal or run:

    ```bash
    source ~/.bashrc
    ```

### Verify the installation

```bash
conda --version
```

You should see something like `conda 24.x.x`. Also verify Python:

```bash
python --version
```

---

## Essential Conda Commands

### Create an environment

```bash
# Create an environment called "workshop" with Python 3.12
conda create -n workshop python=3.12
```

### Activate / deactivate

```bash
# Activate the environment
conda activate workshop

# Your prompt changes to show the active environment:
# (workshop) username@computer:~$

# Deactivate (go back to base)
conda deactivate
```

### Install packages

```bash
# Install packages with conda
conda install pandas matplotlib requests

# Install from pip (inside a conda environment)
pip install some-package-not-on-conda
```

### List environments and packages

```bash
# See all your environments
conda env list

# See packages in the current environment
conda list

# Search for a package
conda search numpy
```

### Remove an environment

```bash
conda env remove -n old-project
```

---

## Set Up the Workshop Environment

Let's create the environment we'll use for the rest of the workshop:

```bash
# Create the environment
conda create -n workshop python=3.12 pandas matplotlib requests -y

# Activate it
conda activate workshop

# Verify
python --version
pip list
```

!!! success "You should see"
    ```
    Python 3.12.x
    ```
    And `pandas`, `matplotlib`, and `requests` in your package list.

From now on, always activate this environment before working on workshop code:

```bash
conda activate workshop
```

---

## Troubleshooting

??? question "`conda: command not found`"
    The installer didn't add Conda to your PATH. Run:
    ```bash
    # macOS/Linux
    ~/miniforge3/bin/conda init
    source ~/.bashrc  # or ~/.zshrc
    ```
    On Windows, make sure you checked "Add to PATH" during installation. If you didn't, reinstall.

??? question "Conda is very slow to resolve environments"
    Miniforge uses `mamba` as the default solver, which is much faster than classic Conda. If you installed Miniconda or Anaconda instead, you can switch:
    ```bash
    conda install -n base conda-libmamba-solver
    conda config --set solver libmamba
    ```

??? question "Should I use `pip` or `conda` to install packages?"
    Prefer `conda install` when the package is available on conda-forge. Use `pip install` as a fallback for packages that are only on PyPI. Avoid mixing them heavily in the same environment.

---

**Next:** [VS Code Installation →](00b-vscode.md)
