# VS Code Installation

Visual Studio Code (VS Code) is a free, lightweight code editor that has become the standard tool for data engineers and developers. It runs on macOS, Windows, and Linux.

---

## Why VS Code?

- **Free and open-source** — no license needed
- **Built-in terminal** — run commands without leaving the editor
- **Git integration** — see changes, make commits, and push directly from the editor
- **Extensions** — add support for Python, Jupyter notebooks, AI assistants, and more
- **Lightweight** — starts fast, uses less than 500 MB on disk

---

## Install VS Code

=== "macOS"

    1. Go to [code.visualstudio.com/download](https://code.visualstudio.com/download)
    2. Click **Download for Mac** (it auto-detects Intel vs Apple Silicon)
    3. Open the downloaded `.zip` file
    4. Drag **Visual Studio Code.app** to your **Applications** folder
    5. Open VS Code from Applications

    **Add the `code` command to your terminal:**

    1. Open VS Code
    2. Press `Cmd + Shift + P` to open the Command Palette
    3. Type `shell command` and select **Shell Command: Install 'code' command in PATH**

    Now you can open any folder from the terminal:

    ```bash
    code ~/projects/data-engineering-workshop
    ```

=== "Windows"

    1. Go to [code.visualstudio.com/download](https://code.visualstudio.com/download)
    2. Click **Download for Windows**
    3. Run the installer (`VSCodeUserSetup-x64-*.exe`)
    4. During installation:
        - Accept the license agreement
        - **Check** "Add to PATH" (so you can type `code` in the terminal)
        - **Check** "Add 'Open with Code' action to file context menu" (optional but handy)
    5. Click Install and Launch

    After installation, restart your terminal and verify:

    ```bash
    code --version
    ```

=== "Linux (Ubuntu/Debian)"

    ```bash
    # Download and install the .deb package
    sudo apt update
    sudo apt install -y wget gpg
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
    sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
    sudo apt update
    sudo apt install -y code
    ```

    Or use Snap:

    ```bash
    sudo snap install code --classic
    ```

---

## Recommended Extensions

After installing VS Code, add these extensions for the workshop. Open VS Code and click the **Extensions** icon in the left sidebar (or press `Ctrl/Cmd + Shift + X`), then search for each one:

### Essential

| Extension | What it does |
|-----------|-------------|
| **Python** (by Microsoft) | Python language support, IntelliSense, debugging |
| **Jupyter** (by Microsoft) | Run Jupyter notebooks inside VS Code |
| **GitLens** | Enhanced Git integration — see who changed what and when |

### Recommended

| Extension | What it does |
|-----------|-------------|
| **Pylance** | Fast, feature-rich Python language server |
| **autoDocstring** | Generate Python docstrings with a shortcut |
| **Rainbow CSV** | Color-codes CSV columns so they're easier to read |
| **Material Icon Theme** | Better file icons in the sidebar |

To install from the terminal:

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension eamodio.gitlens
```

---

## Quick Tour

### Open a project folder

```bash
# From the terminal
code ~/projects/data-engineering-workshop
```

Or in VS Code: **File → Open Folder**

### The integrated terminal

Press `` Ctrl + ` `` (backtick) to toggle the built-in terminal. This is where you'll run Python scripts, Git commands, and more — without leaving the editor.

### Key shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + Shift + P` | Command Palette (search for any action) |
| `` Ctrl + ` `` | Toggle terminal |
| `Ctrl/Cmd + P` | Quick Open (search for files) |
| `Ctrl/Cmd + B` | Toggle sidebar |
| `Ctrl/Cmd + S` | Save file |
| `Ctrl/Cmd + /` | Toggle comment on selected lines |
| `F5` | Start debugging |

### Select your Python interpreter

When you open a Python file, VS Code may ask you to select an interpreter:

1. Press `Ctrl/Cmd + Shift + P`
2. Type `Python: Select Interpreter`
3. Choose the one from your `workshop` Conda environment (e.g., `~/miniforge3/envs/workshop/bin/python`)

---

## Verify Your Setup

1. Open VS Code
2. Open the integrated terminal (`` Ctrl + ` ``)
3. Activate your Conda environment:

    ```bash
    conda activate workshop
    ```

4. Create a test file:

    ```bash
    echo 'print("VS Code is ready!")' > test.py
    python test.py
    ```

5. You should see `VS Code is ready!` in the terminal

!!! success "If you see the output, your editor is set up and ready!"

---

**Next:** [GitHub Account Setup →](01b-github-setup.md)
