# Claude Code Installation

Claude Code is Anthropic's command-line AI coding agent. Like Gemini CLI, it lives in your terminal — but it's powered by Claude and has deep integration with your local files and tools.

!!! info "Optional module"
    This section is for those who want to explore an alternative (or additional) AI coding assistant. Claude Code requires a Claude Pro, Max, or API account.

---

## What is Claude Code?

Claude Code is an **agentic coding tool** that runs in your terminal. It can:

- Read and understand your entire project
- Write, edit, and refactor code across multiple files
- Run commands and fix errors iteratively
- Work with Git (commits, PRs, branches)
- Search the web and your codebase
- Execute multi-step tasks autonomously

Think of it as a more autonomous version of a chat-based AI — it doesn't just suggest code, it can take actions on your project directly.

---

## Prerequisites

- **Node.js 18+** (you may already have this from the Gemini CLI setup)
- A **Claude account** — one of the following:
    - Claude Pro or Max subscription ([claude.ai](https://claude.ai))
    - Anthropic API key ([console.anthropic.com](https://console.anthropic.com))

Check Node.js:

```bash
node --version   # Should be 18.x.x or higher
```

---

## Installation

### Option 1: Native installer (Recommended)

=== "macOS / Linux"

    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    This downloads and installs the latest stable release with no extra dependencies.

=== "Windows (via WSL)"

    Claude Code is designed for Unix-like environments. On Windows, use WSL:

    ```bash
    # If you don't have WSL yet
    wsl --install -d Ubuntu

    # Inside the Ubuntu terminal
    curl -fsSL https://claude.ai/install.sh | bash
    ```

### Option 2: npm install

If you prefer npm:

```bash
npm install -g @anthropic-ai/claude-code
```

### Verify installation

```bash
claude --version
```

---

## Authentication

The first time you run Claude Code, it will walk you through authentication:

```bash
claude
```

You'll be given options:

1. **Claude Pro/Max subscription** — Opens a browser to authenticate via OAuth (no API key needed)
2. **Anthropic API** — Enter your API key from [console.anthropic.com](https://console.anthropic.com)

After authenticating, verify everything is working:

```bash
claude doctor
```

This checks your setup and reports any issues.

---

## Quick Usage

### Start an interactive session

```bash
# Navigate to your project first
cd ~/projects/data-engineering-workshop

# Start Claude Code
claude
```

### One-shot commands

You can also give Claude Code a task directly:

```bash
claude "explain what this project does"
```

```bash
claude "add error handling to fetch_data.py"
```

### Example session for the Keeling Curve project

```
> Read the keeling-curve directory and explain what each script does

> The visualize.py script has a bug — the decade comparison plot
  doesn't show a legend for all decades. Fix it.

> Add a new script that calculates the rate of CO₂ acceleration
  over time and creates a plot showing it.

> Commit everything with a descriptive message
```

---

## Claude Code vs. Gemini CLI

Both are AI coding assistants in the terminal, but they have different strengths:

| Feature | Gemini CLI | Claude Code |
|---------|-----------|-------------|
| **Provider** | Google (Gemini) | Anthropic (Claude) |
| **Free tier** | Yes (1,000 req/day with Google account) | No (requires Pro/Max or API credits) |
| **Autonomy** | Asks before each action | Can chain multiple actions together |
| **File editing** | Creates/edits files with permission | Deep multi-file editing and refactoring |
| **Git integration** | Basic | Full (commits, PRs, branches) |
| **Best for** | Quick questions, single-file tasks | Multi-file projects, complex refactoring |

!!! tip "Use both!"
    There's no rule against using multiple AI tools. Many developers use both depending on the task — Gemini CLI for quick free queries, Claude Code for complex multi-step work.

---

## Troubleshooting

??? question "`claude: command not found`"
    Add the install directory to your PATH:
    ```bash
    # macOS/Linux
    export PATH="$HOME/.local/bin:$PATH"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

??? question "Authentication keeps failing"
    Run `claude doctor` to diagnose the issue. Make sure you're using a supported account type (Pro, Max, or API key).

??? question "Can I use Claude Code for free?"
    Claude Code requires either a Claude Pro/Max subscription or Anthropic API credits. There's no free tier, but API usage is pay-as-you-go.

---

**Back to:** [Home](../index.md)
