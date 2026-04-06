# Claude Code

Claude Code is Anthropic's command-line AI coding agent. Like Gemini CLI, it lives in your terminal — but it's designed for deeper, multi-step work: reading your entire project, editing files, running commands, and iterating until something works.

!!! info "Optional module"
    This section is for those who want to explore an alternative (or additional) AI coding assistant. Claude Code requires a Claude Pro, Max, or API account — there is no free tier.

---

## What is Claude Code?

Claude Code is an **agentic coding tool** that runs in your terminal. Unlike a chat interface, it can take actions directly in your project:

- Read and understand your entire codebase
- Write, edit, and refactor code across multiple files
- Run commands and fix errors iteratively
- Work with Git (commits, branches, pull requests)
- Search the web and your local files

The key difference from Gemini CLI: Claude Code can **chain multiple steps together autonomously**. You give it a goal, and it figures out the sequence of actions needed to get there.

!!! tip "How it handles your files"
    Claude Code will ask for your approval before taking actions that modify files or run commands — unless you tell it to proceed automatically. You are always in control.

---

## Prerequisites

- **Node.js 18+** — check with:

    ```bash
    node --version
    ```

    If it says `v18.x.x` or higher, you're good. If not, install it from [nodejs.org](https://nodejs.org).

- **A Claude account** — one of:
    - Claude Pro or Max subscription at [claude.ai](https://claude.ai)
    - Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

!!! note "Cost"
    Claude Pro ($20/mo) or Max ($100/mo) subscriptions give you unlimited Claude Code usage. An API key is pay-as-you-go — typically a few cents per session for light use. For a masters project, a Pro subscription is the most practical option.

---

## Installation

=== "macOS / Linux"

    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

=== "Windows (via WSL)"

    Claude Code is designed for Unix-like environments. On Windows, run it inside WSL:

    ```bash
    wsl --install -d Ubuntu
    ```

    Then, inside the Ubuntu terminal:

    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

### Verify the installation

```bash
claude --version
```

You should see a version number printed. If you get `command not found`, see [Troubleshooting](#troubleshooting) below.

---

## Authentication

Run Claude Code for the first time:

```bash
claude
```

You'll be prompted to choose an authentication method:

```
? How would you like to authenticate?
  ❯ Claude.ai account (Pro or Max subscription)
    Anthropic API key
```

**Option 1 — Claude.ai account (recommended for most students):**
Select this and a browser window will open. Log into your Claude account and authorize the CLI. You'll be redirected back and the terminal will confirm you're authenticated.

**Option 2 — API key:**
Select this and paste your key from [console.anthropic.com](https://console.anthropic.com) when prompted. The key is stored locally and never sent anywhere other than Anthropic's servers.

### Check your setup

After authenticating, run:

```bash
claude doctor
```

This checks your installation and reports any issues. A healthy output looks like:

```
✓ Node.js version: v20.x.x
✓ Claude Code version: x.x.x
✓ Authentication: OK
✓ Network connectivity: OK
```

---

## Your First Session

Navigate to any project directory and start Claude Code:

```bash
cd ~/your-project
claude
```

Claude Code will read the contents of your current directory before doing anything else. You'll see a prompt like:

```
✓ Loaded project context
> 
```

Type a question or task and press Enter. Try starting with something low-stakes:

```
> What files are in this project and what does each one do?
```

Claude Code will read your files and give you a plain-English summary. This is a good way to see how well it understands your project before asking it to make changes.

!!! tip "Start with questions, not edits"
    Before asking Claude Code to change anything, ask it to explain what's there. This builds your confidence in what it understands — and catches any misunderstandings early.

### Giving it a task

When you ask it to modify something, Claude Code will show you what it plans to do and ask for approval:

```
> Add a docstring to the load_data function in data_loader.py

I'll add a docstring to the load_data function. Here's what I plan to do:

  Edit data_loader.py:
  - Add a Google-style docstring describing the function's parameters and return value

Proceed? [y/n]
```

Press `y` to approve, `n` to cancel. You can also type feedback and it will adjust.

### One-shot commands

You can skip the interactive session and give a task directly from the terminal:

```bash
claude "explain what this project does"
claude "what does the train_model function do?"
claude "add a --verbose flag to the CLI in main.py"
```

---

## Exercise 1 — Explore Your Project

!!! exercise "Try this now"
    1. Navigate to any project you have locally (your capstone project, a class assignment, anything with code in it)
    2. Start Claude Code: `claude`
    3. Ask it: **"Read this project and give me a summary of what it does, what the main files are, and what's still incomplete or unclear"**
    4. Follow up with one or two questions based on its response

    **Goal:** Get comfortable with the read-explain-ask loop before you ask it to change anything.

---

## Exercise 2 — Make a Change

!!! exercise "Try this now"
    1. In the same project, ask Claude Code to make a small, low-risk change:
        - Add a docstring to a function that doesn't have one
        - Rename a variable to be more descriptive
        - Add a comment explaining a confusing section of code
    2. Review the proposed edit before approving
    3. After it applies the change, open the file and confirm it looks right

    **Goal:** Experience the propose-review-approve workflow. Notice that Claude Code shows you the diff before touching your files.

---

## Exercise 3 — Ask It to Fix Something

!!! exercise "Try this now"
    1. Find something in your project that's broken, incomplete, or could be improved
    2. Describe the problem clearly: **"The load_data function crashes when the CSV has missing values — add handling for that"**
    3. Let Claude Code propose a fix, review it, and approve
    4. Ask it to run the relevant code to verify the fix works (if applicable)

    **Goal:** Practice giving Claude Code a problem description rather than a solution. The more context you provide, the better the result.

---

## Applying Claude Code to Your Capstone

The real power of Claude Code is in sustained, structured collaboration on a long-running project. Here's a lightweight workflow designed for masters capstone projects.

### Set up a CLAUDE.md file

Claude Code automatically reads a file called `CLAUDE.md` at the root of your project at the start of every session. This is how you give the agent permanent context about your project — without re-explaining it every time.

Create a `CLAUDE.md` in your project root with at minimum:

```markdown
# CLAUDE.md

## Project
One sentence: what this project does and what the deliverable is.

## Key Files
- Source of truth: paper/methods.md (or your main document)
- Plan & status: docs/plan.md
- Tasks: docs/todo.md

## Setup
conda activate my-env  # or pip install -r requirements.txt

## Code Layout
src/          # core library code
scripts/      # standalone analysis and figure scripts
data/raw/     # raw input data (never modified)
data/processed/  # cleaned datasets

## Ask Before
- Deleting files
- Adding new dependencies
- Changing directory structure
- Modifying data files
```

The more specific and current this file is, the more useful Claude Code will be. Update it as your project evolves.

### Use plan.md and todo.md as the interface

The most effective workflow is:

1. **`docs/plan.md`** — your strategic document: phases, milestones, approach, status markers
2. **`docs/todo.md`** — a checkbox task list seeded from your plan, one concrete action per line

Then in each Claude Code session:

```
> Read docs/todo.md and tell me what the next unchecked task is
> [Claude summarizes the next task]
> Go ahead and do that
```

This is more effective than explaining your project from scratch each session. The agent picks up exactly where you left off.

### Recommended directory structure

```
project/
  CLAUDE.md              # Agent instructions
  environment.yml        # Pinned dependencies

  docs/
    plan.md              # Milestones and strategy
    todo.md              # Living task checklist
    architecture.md      # Codebase map and technical design

  src/                   # Library code
  scripts/               # Standalone scripts (analysis, figures)
  data/
    raw/                 # Never modified — read only
    processed/           # Output of your pipeline
  figures/               # Generated outputs
  paper/                 # Your written deliverable
```

You don't need all of these at once — migrate your existing project incrementally.

### What to ask Claude Code to help with

Once your project is set up:

```
> Read CLAUDE.md and docs/todo.md, then do the next unchecked task

> My data pipeline in scripts/preprocess.py is slow on large files — profile it and suggest optimizations

> I added three new functions to src/model.py — update docs/architecture.md to reflect that

> Help me write the methods section for this analysis based on what you see in the code
```

!!! tip "Let the agent update your docs"
    After completing a task, ask Claude Code to check off the item in `todo.md` and update `architecture.md` if any files changed. This keeps your project state current with no manual bookkeeping.

---

## Claude Code vs. Gemini CLI

Both are AI coding assistants in the terminal, but they have different strengths:

| Feature | Gemini CLI | Claude Code |
|---------|-----------|-------------|
| **Provider** | Google (Gemini) | Anthropic (Claude) |
| **Free tier** | Yes (1,000 req/day) | No (Pro/Max or API credits) |
| **Autonomy** | Asks before each action | Can chain multiple actions together |
| **File editing** | Creates/edits files with permission | Deep multi-file editing and refactoring |
| **Git integration** | Basic | Full (commits, PRs, branches) |
| **Persistent context** | No | Yes — reads CLAUDE.md automatically |
| **Best for** | Quick questions, single-file tasks | Multi-file projects, sustained iteration |

!!! tip "Use both"
    Many developers use both depending on the task — Gemini CLI for quick free queries, Claude Code for complex multi-step work on a project they return to regularly.

---

## Troubleshooting

??? question "`claude: command not found` after installation"
    The npm global bin directory may not be on your PATH. Add it:

    === "macOS / Linux (bash)"
        ```bash
        echo 'export PATH="$(npm bin -g):$PATH"' >> ~/.bashrc
        source ~/.bashrc
        ```

    === "macOS (zsh)"
        ```bash
        echo 'export PATH="$(npm bin -g):$PATH"' >> ~/.zshrc
        source ~/.zshrc
        ```

    Then verify: `which claude`

??? question "Authentication fails or browser doesn't open"
    Run `claude doctor` to diagnose. Common fixes:

    - Make sure you're logged into [claude.ai](https://claude.ai) in your browser before authenticating
    - Try the API key option instead of the browser OAuth flow
    - Check that your account type is Pro, Max, or has API credits

??? question "Claude Code modifies files without asking"
    By default, Claude Code asks before editing files. If it's not asking, check your session settings with `/settings` inside an interactive session. You can also add explicit instructions to your `CLAUDE.md`:

    ```markdown
    Always ask for approval before editing any file.
    ```

??? question "Can I use Claude Code for free?"
    There is no free tier. You need either a Claude Pro ($20/mo) or Max ($100/mo) subscription, or an Anthropic API key with credits. API usage for light sessions typically costs a few cents per session — check [anthropic.com/pricing](https://anthropic.com/pricing) for current rates.

??? question "It keeps misunderstanding my project"
    This usually means your `CLAUDE.md` needs more context. Add:

    - A clearer one-sentence project description
    - The entry points (which file to run, which function does X)
    - Any conventions or constraints the agent should follow

    Think of `CLAUDE.md` as onboarding instructions for a new research assistant.

---

**Back to:** [Home](../index.md)
