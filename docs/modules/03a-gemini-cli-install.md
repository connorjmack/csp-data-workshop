# Installing Gemini CLI

Gemini CLI is an open-source AI agent from Google that brings Gemini directly into your terminal. Think of it as having a coding partner that can read your files, write code, run commands, and explain things — all from the command line.

---

## Prerequisites

You need **Node.js version 20 or higher**. Check if you have it:

```bash
node --version
```

If you see `v20.x.x` or higher, skip ahead to [Install Gemini CLI](#install-gemini-cli). Otherwise, install Node.js first:

=== "macOS"

    ```bash
    # Using Homebrew (recommended)
    brew install node

    # Or download from nodejs.org
    ```

=== "Windows"

    Download the installer from [nodejs.org](https://nodejs.org/) (LTS version). Run it and accept all defaults.

=== "Linux (Ubuntu/Debian)"

    ```bash
    # Using NodeSource
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

=== "Conda"

    ```bash
    conda create -y -n gemini_env -c conda-forge nodejs
    conda activate gemini_env
    ```

Verify after installation:

```bash
node --version   # Should be v20.x.x or higher
npm --version    # Should be 10.x.x or higher
```

---

## Install Gemini CLI

### Option 1: Global install (Recommended)

```bash
npm install -g @google/gemini-cli
```

Verify it installed:

```bash
gemini --version
```

### Option 2: Run without installing

If you don't want to install it globally, you can run it directly with `npx`:

```bash
npx @google/gemini-cli
```

!!! tip "Which option?"
    Use Option 1 if you plan to use Gemini CLI regularly (recommended for this workshop). Use Option 2 for a quick try without committing to the install.

---

## Authenticate with Google

The first time you run Gemini CLI, it will ask you to log in.

### 1. Start Gemini CLI

```bash
gemini
```

### 2. Choose authentication method

When prompted **"How would you like to authenticate for this project?"**, select:

```
1. Login with Google
```

### 3. Sign in with your student account

A browser window will open. Sign in with the **same university Google account** you used for Gemini Pro in [Module 1](01a-gemini-login.md).

### 4. Grant permissions

Click **Allow** to let Gemini CLI access your account.

### 5. Return to the terminal

After authentication succeeds, you'll see a welcome message in your terminal and the Gemini CLI prompt will appear.

!!! info "Rate limits"
    With your Google account, you get up to **60 requests per minute** and **1,000 requests per day** — more than enough for this workshop.

---

## Verify It's Working

In the Gemini CLI prompt, type:

```
What version of Python do I have installed?
```

Gemini should detect your Python installation and tell you the version. If it asks for permission to run a command, type `y` to allow it.

To exit Gemini CLI:

```
/quit
```

Or press `Ctrl + C`.

---

## Troubleshooting

??? question "`gemini: command not found`"
    Your npm global bin directory might not be in your PATH. Try:
    ```bash
    # Find where npm installed it
    npm list -g --depth=0

    # Add npm global bin to your PATH
    export PATH="$PATH:$(npm config get prefix)/bin"

    # Make it permanent (add to your shell config)
    echo 'export PATH="$PATH:$(npm config get prefix)/bin"' >> ~/.bashrc
    source ~/.bashrc
    ```

??? question "Authentication fails or no browser opens"
    Try setting your default browser, or look for a URL printed in the terminal — you can manually copy and paste it into your browser.

??? question "Getting errors about Node.js version"
    Make sure you have Node.js 20+:
    ```bash
    node --version
    ```
    If it's older, update Node.js using the instructions above.

---

**Next:** [Using Gemini CLI →](03b-gemini-cli-usage.md)
