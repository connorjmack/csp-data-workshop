# Claude Code

Claude Code is Anthropic's command-line AI coding agent. Like Gemini CLI, it lives in your terminal — but it's designed for deeper, multi-step work: reading your entire project, editing files, running commands, and iterating until something works.

!!! info "Account required"
    Claude Code requires a Claude Pro, Max, or API account — there is no free tier.

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

- **Node.js 20+** — check with:

    ```bash
    node --version
    ```

    If you completed the Gemini CLI module, you already have this. If not, install Node 20+ from [nodejs.org](https://nodejs.org).

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

=== "Windows (Anaconda Prompt)"

    Open **Anaconda Prompt** (not PowerShell or Command Prompt) and run:

    ```bash
    npm install -g @anthropic-ai/claude-code
    ```

    All subsequent `claude` commands should also be run from Anaconda Prompt.

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

## Slash Commands

Claude Code has built-in slash commands that control your session. Type `/` inside an interactive session to see the full list. Here are the most useful ones to know:

| Command | What it does |
|---------|-------------|
| `/help` | Show all available commands and keyboard shortcuts |
| `/model` | Switch between models (Opus, Sonnet, Haiku) — trade capability for speed |
| `/context` | See and manage what files Claude has loaded into its context |
| `/usage` | Check your token usage and remaining quota |
| `/compact` | Compress the conversation history to free up context window space |
| `/clear` | Wipe the conversation and start fresh (does not undo file changes) |
| `/commit` | Stage and commit your changes with an auto-generated commit message |

!!! exercise "Try this now"
    1. In your Claude Code session, run `/model` and note what models are available to you
    2. Run `/usage` to see your current token consumption
    3. Run `/context` to see what files Claude has loaded from your project

    These are useful for managing long sessions. `/compact` is especially helpful when Claude starts losing track of earlier context, and `/model` lets you drop to a faster model for simple tasks.

---

## Exercise 3 — Build Something with Your Data

This is where your capstone project enters the picture. You should have data, documents, or other materials from your project already on your machine. If you don't have capstone materials handy, any dataset will work — a CSV from a class assignment, a public dataset you've downloaded, anything.

!!! exercise "Try this now"
    1. Navigate to a directory containing data you're working with and start Claude Code
    2. Ask it to **read your data and describe what it contains**:
        ```
        > Read the data files in this project and tell me what's there —
          columns, row counts, data types, and anything that stands out
        ```
    3. Then ask it to **create a visualization**:
        ```
        > Using that data, create a Python script that generates a
          meaningful plot. Pick the most interesting relationship you
          see and save the figure as output.png
        ```
    4. Review the script it produces, approve it, and let it run
    5. If the plot isn't what you want, give feedback and let it iterate:
        ```
        > Change this to a scatter plot instead, and increase the font
          size on the axis labels
        ```

    **Goal:** Experience the full loop — data exploration, code generation, execution, and iteration — using your own project materials. This is the core workflow you'll use going forward.

!!! tip "Bring context, get better results"
    The more you tell Claude Code about what you're trying to do, the better the output. Instead of "make a plot," try "I'm investigating whether temperature affects yield in my experiment data — show me that relationship." Domain context makes a real difference.

---

## A Workflow to Try: Structured Capstone Sessions

One way to get more out of Claude Code on a long-running project is to give it persistent context so you don't re-explain everything each session. This is optional — use what's helpful and skip what isn't.

### CLAUDE.md — persistent project context

Claude Code automatically reads a file called `CLAUDE.md` at the root of your project at the start of every session. Think of it as onboarding instructions for a research assistant who's joining your project.

Create a `CLAUDE.md` in your project root with at minimum:

```markdown
# CLAUDE.md

## Project
One sentence: what this project does and what the deliverable is.

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

### plan.md and todo.md as a session interface

Some students find it useful to maintain two lightweight documents alongside their code:

1. **`docs/plan.md`** — a strategic overview: phases, milestones, approach, current status
2. **`docs/todo.md`** — a checkbox task list seeded from the plan, one concrete action per line

Then at the start of each session:

```
> Read docs/todo.md and tell me what the next unchecked task is
> [Claude summarizes the next task]
> Go ahead and do that
```

This can save you from re-explaining your project each session — the agent picks up where you left off. You can also ask Claude Code to generate these files for you based on your existing project materials.

### Example directory structure

Here's one way to organize a capstone project for this workflow. You don't need all of these — adopt the pieces that make sense for your project:

```
project/
  CLAUDE.md              # Agent instructions
  environment.yml        # Pinned dependencies

  docs/
    plan.md              # Milestones and strategy
    todo.md              # Living task checklist

  src/                   # Library code
  scripts/               # Standalone scripts (analysis, figures)
  data/
    raw/                 # Never modified — read only
    processed/           # Output of your pipeline
  figures/               # Generated outputs
  paper/                 # Your written deliverable
```

### Example prompts for capstone work

```
> Read CLAUDE.md and docs/todo.md, then do the next unchecked task

> My data pipeline in scripts/preprocess.py is slow on large files —
  profile it and suggest optimizations

> Help me write the methods section for this analysis based on what
  you see in the code

> I just finished the feature engineering step — update docs/todo.md
  to check that off and tell me what's next
```

!!! tip "Let the agent update your docs"
    After completing a task, you can ask Claude Code to check off the item in `todo.md` and update any project docs that changed. This keeps your project state current with minimal bookkeeping.

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

    === "Windows (Anaconda Prompt)"
        Make sure you installed from **Anaconda Prompt** and are running `claude` from the same terminal. If it still fails, close and reopen Anaconda Prompt and try again.

    Then verify: `which claude` (macOS/Linux) or `where claude` (Windows)

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

**Back to:** [Home](../index.md) | **Previous:** [Gemini CLI →](03b-gemini-cli-usage.md)
