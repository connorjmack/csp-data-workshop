# Capstone Project Workflow

A structured workflow for managing a masters capstone project using Claude Code. Designed for students bringing an existing, partly-finished project into a reproducible, well-documented system. This document serves two purposes: it is your reference throughout the project, and it provides context to Claude Code so the agent can work effectively within your project.

---

## Deliverable Archetypes

Your capstone falls into one of these categories. Each shapes which parts of this workflow you need. Read the one that matches your project; skim the others.

### A. Research Paper or Thesis Chapter

You are producing a formal written document with methodology, results, and figures. This is the most structured archetype.

**You need:** The full document system (plan, todo, architecture, audit), the figure pipeline, the LaTeX workflow (or equivalent for your format), and run management if you are training models.

**Your source of truth** is your methods document (`methods.tex`, `methods.md`, or equivalent). Everything else — the formatted submission, the figures, the code — must be consistent with it.

### B. Software Tool or Application

You are building something — a package, a dashboard, an API, a pipeline tool. There is a written component (report, thesis chapter, or documentation), but the primary artifact is the software itself.

**You need:** The full document system, the figure pipeline (for any figures in your written component), and strong emphasis on `architecture.md` to document your codebase. Run management only if your tool involves model training.

**Your source of truth** is the code. The written component describes and justifies the software.

### C. Data Analysis or Modeling Study

You are analyzing data, building models, and reporting findings. Similar to the paper archetype but the emphasis is on the analytical pipeline and results rather than methodological novelty.

**You need:** The full document system, the figure pipeline (you will have many figures), and run management for any model training. The audit trail matters here — you need to trace every number in your report back to the code that produced it.

**Your source of truth** is your methods document, with the analytical pipeline as the implementation.

---

## Directory Structure

Adopt this structure regardless of archetype. Not every directory will be heavily used in every project — that is fine. The structure exists so that everything has an obvious home.

```
project/
  CLAUDE.md              # Agent instructions (you maintain this)
  environment.yml        # or requirements.txt — pinned dependencies

  docs/
    plan.md              # Design decisions, phased milestones, status
    todo.md              # Living task checklist
    architecture.md      # Codebase map + technical design + figure registry
    audit.md             # Inconsistency tracker

  src/                   # Your source code (packages, modules)
    __init__.py
    ...

  scripts/
    figures/             # One script per publication/report figure
    analysis/            # Exploratory and diagnostic scripts
    preprocessing/       # Data pipeline scripts

  data/
    raw/                 # Unprocessed source data (never modified)
    processed/           # Cleaned, feature-engineered datasets
    lookups/             # Mapping tables, metadata files

  figures/
    main/                # Figures for the main document
      figure1/           # One directory per figure
      figure2/
    appendix/            # Supplementary figures

  paper/                 # Or report/, thesis/, docs/deliverable/ — name it for what it is
    methods.tex          # Working methodology draft (source of truth)
    main.tex             # Formatted submission document
    appendix.tex         # Supplementary material
    refs.bib             # Shared bibliography

  runs/                  # Self-contained model/experiment runs (if applicable)
    {method}/
      {YYYYMMDD_HHMMSS}_{description}/

  notebooks/             # Jupyter/Colab notebooks (exploration only, not deliverables)

  tests/                 # Test suite (especially for archetype B)
```

**If your deliverable is not LaTeX,** replace the `paper/` directory with whatever fits:
- `report/` with `.md` or `.docx` files
- `thesis/` with your university's template
- `docs/` with user-facing documentation (for software tools)

The key principle is that your writing lives in its own directory, separate from code.

### Migrating Your Existing Project

Map your inventory onto this structure. For each existing asset:

1. **Code:** Move into `src/` (library code) or `scripts/` (standalone scripts). If you have Jupyter notebooks with important code embedded in them, extract the reusable logic into `src/` and keep the notebook in `notebooks/` as exploration.
2. **Data:** Place in `data/raw/`. Never modify raw data — processing scripts read from `raw/` and write to `processed/`.
3. **Trained models / results:** Place in `runs/` with a descriptive directory name. Include whatever config or metadata you have, even if incomplete.
4. **Written drafts:** Place in `paper/` (or equivalent). If you have a single messy draft, that becomes the starting point for `methods.tex`.
5. **Figures:** If you have existing figures, place them in `figures/` with the directory-per-figure convention. Create a generating script for each one, even if the original was made ad-hoc.

Do not try to reorganize everything in one sitting. Migrate in phases: code first, then data, then writing. Get each phase working before moving to the next.

---

## Document System

Six documents form the backbone of project management. Each has a distinct role. The key principle is **separation of concerns** — design rationale, task tracking, methodology prose, figure provenance, and known issues each live in their own place so they can evolve independently.

### CLAUDE.md (repo root)

Agent instructions for Claude Code. This file is read automatically at the start of every conversation. It keeps the agent grounded in your project's reality.

**What belongs here:**
- One-line project summary (what are you building and why)
- Your deliverable archetype (A, B, or C from above)
- Pointers to source-of-truth documents
- Code layout summary (key directories, entry points)
- Critical invariants the agent must never violate
- Environment setup commands
- Platform-specific notes (paths, OS, remote servers)
- Figure and plotting conventions

**What does not belong here:** Task lists, design rationale, methodology prose. Those have their own docs.

**Template to start from:**

```markdown
# CLAUDE.md

## Project
{One sentence: what this project does and what the deliverable is.}

Archetype: {A: Paper | B: Software | C: Analysis}

## Key Docs
- Source of truth: `paper/methods.tex` (or equivalent)
- Plan & status: `docs/plan.md`
- Tasks: `docs/todo.md`
- Architecture & figure registry: `docs/architecture.md`
- Issue tracker: `docs/audit.md`

## Setup
{Environment activation, install commands, test commands.}

## Code Layout
{Brief directory descriptions — 1 line per key directory.}

## Conventions
- Save all plotting scripts (no throwaway plots)
- When you make a new figure, open it as a PNG
- {Add your own rules as the project evolves}
```

Update CLAUDE.md as your project evolves. If you find yourself repeatedly correcting the agent about the same thing, add a rule here.

### docs/plan.md — Design, Strategy, and Milestones

The strategic document. Contains the *why* behind your approach, phased implementation milestones, and current status.

**Structure:**
- Problem statement and motivation
- Approach / methodology overview
- Phased milestones with **absolute dates** tied to your academic calendar
- Status markers: `COMPLETE`, `CURRENT`, `TODO`, `BLOCKED`
- Known constraints and open questions
- Success criteria / definition of done

**Example milestone section:**

```markdown
## Milestones

### Phase 1: Data pipeline (COMPLETE — 2026-02-15)
Ingest raw data, clean, feature-engineer, produce analysis-ready dataset.

### Phase 2: Model development (CURRENT — target 2026-03-30)
Train and evaluate models. Produce comparison figures.

### Phase 3: Writing (TODO — target 2026-04-20)
Draft methods and results sections. Finalize figures.

### Phase 4: Defense prep (TODO — defense 2026-05-10)
Polish document, prepare slides, rehearse.
```

**Relationship to `todo.md`:** `plan.md` is the parent — it defines phases, `todo.md` tracks individual tasks within them. When scope changes, update `plan.md` first, then sync `todo.md`.

### docs/todo.md — Living Checklist

The tactical document. Checkbox-style task tracking seeded from `plan.md` phases.

**Rules:**
- Each task is a concrete, completable action (not a vague goal)
- Mark tasks done as they are completed — do not batch
- Group by phase or milestone, matching `plan.md` structure
- Include notes on blockers or open questions inline
- Distinguish between what you will do vs. what the agent should do

**What this is not:** A design document. If you need to explain *why* you are doing something, that goes in `plan.md`.

### docs/architecture.md — Codebase Map + Technical Design + Figure Registry

The comprehensive reference for the project. Anyone (human or agent) should be able to open this file and understand what exists, where it lives, and how the pieces connect.

**Section 1: Codebase map.** A structured inventory of the repository — not just source code but everything: data directories, config files, scripts, checkpoints, documents. Organized by directory with brief descriptions.

**Section 2: Technical design.** Implementation details beyond what `plan.md` covers: data shapes, module relationships, pipeline stages, key algorithms. The engineering companion to your methods document.

**Section 3: Figure registry.** Maps every deliverable figure to its generating code:

| Field | Purpose |
|---|---|
| Label | Figure reference in your document (`fig:...` or Figure 1, etc.) |
| Script | Path to the generating script |
| Output dir | Where timestamped outputs go |
| Data deps | Input data files or directories |
| Run deps | Model run directories the figure reads from (if any) |
| CLI command | Exact command to reproduce the figure |
| Notes | Options, variants, known quirks |

You will build this registry incrementally as figures are created. Start it empty — populate it as you go.

### docs/audit.md — Issue Tracker

A running log of known inconsistencies, stale figures, label mismatches, incorrect numbers, and anything that needs fixing before submission/defense.

**When to update:** Any time you notice something wrong — a figure that does not match its caption, a number in the text from a stale run, a broken reference. Write it down immediately rather than trying to fix everything at once.

**When to resolve:** Before submission or defense, walk through every open issue and close it.

---

## Writing Your Deliverable

### If you are writing a paper, thesis chapter, or formal report

Three documents serve distinct roles. The key principle is that **the methods document is the source of truth** — other documents must be consistent with it, not the other way around.

**`paper/methods.tex` (or `methods.md`)** — Your working methodology draft. Contains the full methodology: math, tables, prose, citations. This is what you iterate on. Keep it standalone (compiles or renders on its own) so you can work on it without journal/university formatting overhead.

**`paper/main.tex` (or your formatted submission document)** — The deliverable in its required format. Uses your university template, journal style, etc. The methods section is derived from `methods.tex`. Figure references use `latest.pdf` symlinks (see Figure Pipeline), so regenerating a figure never requires editing this file.

**`paper/appendix.tex`** — Supplementary material with its own numbering scheme.

**If your deliverable is not LaTeX:** The same principle applies. Have a working draft where you develop content freely, and a separate formatted version in the required submission format. The working draft is the source of truth.

### Source of Truth Hierarchy

1. Your methods document — methodology and formulations
2. `plan.md` — design decisions and approach
3. Code — implementation (must match the methods document)
4. Formatted deliverable — derived from the above

If any two of these disagree, the higher-ranked one wins. Fix the lower-ranked one to match.

---

## Figure Pipeline

Figures are code outputs, not files you edit by hand. Every figure in your deliverable is generated by a script, and your documents reference a stable symlink that points to the current version.

### Why This Matters

When your advisor says "change the colormap on Figure 3" or your committee asks "can you regenerate this with updated data," you run one command. There is no ambiguity about which version of a figure is current, and there is no risk of accidentally including a stale version.

### Timestamped Outputs

Every figure script writes its output with a timestamp:

```
{descriptive_name}_{YYYYMMDD_HHMMSS}.{ext}
```

Never overwrite existing figures. Timestamps create an automatic version history. If a new version looks wrong, the previous version is still there.

### Latest Symlinks

Each figure directory contains a `latest.pdf` (or `latest.png`) symlink pointing to the most recent version:

```
figures/
  main/
    figure1/
      study_area_20260301_120000.pdf
      study_area_20260315_143022.pdf
      latest.pdf -> study_area_20260315_143022.pdf
    figure2/
      ...
  appendix/
    ...
```

Your deliverable document references the symlink:
```latex
\includegraphics[width=\textwidth]{figures/main/figure1/latest.pdf}
```

Or in Markdown:
```markdown
![Study area](figures/main/figure1/latest.png)
```

Regenerating a figure: run the script, update the symlink. The document source does not change.

### Figure Scripts

Each figure has a dedicated generating script in `scripts/figures/`. Rules:

- **Deterministic.** Same inputs produce the same output.
- **CLI-invocable.** `python scripts/figures/make_figure1.py` with documented arguments.
- **Self-contained.** The script reads its own data. It does not depend on notebook state or global variables.
- **Registered.** Every figure in your deliverable has an entry in the figure registry in `architecture.md`.

If you have existing figures that were made ad-hoc (in a notebook, in a REPL, by hand), convert them to scripts. This is non-negotiable for reproducibility.

### Symlink Helper

A convenience pattern for your figure scripts to update the symlink automatically:

```python
from pathlib import Path
from datetime import datetime

def save_figure(fig, output_dir, name, fmt="png", dpi=300):
    """Save a figure with timestamp and update the latest symlink."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.{fmt}"
    filepath = output_dir / filename

    fig.savefig(filepath, dpi=dpi, bbox_inches="tight")
    print(f"Saved: {filepath}")

    symlink = output_dir / f"latest.{fmt}"
    if symlink.is_symlink() or symlink.exists():
        symlink.unlink()
    symlink.symlink_to(filename)
    print(f"Updated: {symlink} -> {filename}")

    return filepath
```

Copy this into your project (e.g., `src/utils/figures.py`) and use it in every figure script.

---

## Run Management

If your project involves training models or running experiments, each run lives in a self-contained directory:

```
runs/{method}/
  {YYYYMMDD_HHMMSS}_{description}/
    config.json          # Full configuration used
    model.pkl            # Trained weights / saved model
    predictions.npz      # Cached predictions
    metrics.json         # Evaluation metrics
    figures/             # Run-specific diagnostic plots
```

**Why self-contained?** When a figure script references a run, it gets model, predictions, and metadata in one place. No hunting across directories.

Figure scripts take run directories as arguments:
```bash
python scripts/figures/make_figure3.py --run runs/random_forest/20260402_final
```

If your project does not involve model training, skip this section.

---

## Working With Claude Code

Claude Code reads your CLAUDE.md at the start of every conversation. The quality of that file directly determines how useful the agent is. A few principles:

### Keep CLAUDE.md current

If the agent keeps making the same mistake, add a rule. If a rule no longer applies, remove it. CLAUDE.md is a living document.

### Use plan.md and todo.md as the interface

When you want Claude Code to do work:
1. Make sure `plan.md` reflects your current strategy
2. Make sure `todo.md` has concrete, actionable tasks
3. Point the agent at the next unchecked task

This is more effective than explaining your project from scratch each conversation.

### Let the agent update docs

After the agent completes work, have it update:
- `todo.md` — check off completed tasks
- `architecture.md` — if files were added or changed
- `audit.md` — if inconsistencies were found

### What the agent should not do without asking

Include a section like this in your CLAUDE.md:

```markdown
## Ask Before
- Deleting files or directories
- Adding new dependencies
- Changing directory structure
- Modifying data files
- Creating new modules or packages
```

---

## Getting Started Checklist

Do these in order. Each phase should be working before you start the next.

### Week 1: Inventory and Migration
- [ ] Complete the project inventory (tables above)
- [ ] Create the repo with the directory structure
- [ ] Migrate existing code into `src/` and `scripts/`
- [ ] Move data to `data/raw/`
- [ ] Move any existing writing to `paper/` (or equivalent)
- [ ] Place existing models/results in `runs/`
- [ ] Write your initial `CLAUDE.md`

### Week 2: Document System
- [ ] Write `plan.md` with milestones tied to your academic calendar
- [ ] Seed `todo.md` from `plan.md` phases
- [ ] Start `architecture.md` with a codebase map (section 1 only — section 2 and 3 come later)
- [ ] Create `audit.md` (can be empty to start)
- [ ] Set up your environment (`environment.yml` or `requirements.txt` with pinned versions)
- [ ] Verify everything runs: code executes, tests pass (if you have tests)

### Week 3+: Build
- [ ] Work through `todo.md`, checking off tasks as you go
- [ ] As figures are created, add generating scripts to `scripts/figures/` and register them in `architecture.md`
- [ ] Keep `plan.md` status markers current
- [ ] Log inconsistencies in `audit.md` as you find them

### Before Defense / Submission
- [ ] Resolve all open issues in `audit.md`
- [ ] Verify every figure can be regenerated from its script
- [ ] Verify the source of truth hierarchy is consistent (methods doc matches code matches formatted deliverable)
- [ ] Verify `architecture.md` figure registry is complete and all CLI commands work

---

## Conventions Summary

### Naming
- **Figures:** `{descriptive_name}_{YYYYMMDD_HHMMSS}.{ext}` — never overwrite
- **Runs:** `{YYYYMMDD_HHMMSS}_{description}/` — timestamps prevent collisions
- **Symlinks:** `latest.pdf` or `latest.png` in each figure directory

### Working Rules
- Do not speculate when you can verify — read the file, run the query, check the data
- Do not fabricate data or results for figures, ever
- Do not make ad-hoc plots that appear in your deliverable — every figure has a script
- Update `audit.md` when inconsistencies are found
- Update `architecture.md` when figures are added or changed
- Raw data in `data/raw/` is read-only — never modify it

### Information Flow

```
CLAUDE.md
  Read automatically by the agent.
  Sets conventions and invariants.

plan.md ──seeds──> todo.md
  Design decisions flow into task tracking.
  Scope changes go to plan.md first, then todo.md syncs.

methods doc ──syncs to──> formatted deliverable + appendix
  Methodology is written in the working draft.
  The submission document consumes it.

scripts/ ──generate──> figures/{section}/{name}/latest.{ext}
  Figure scripts produce timestamped outputs with latest symlinks.

deliverable documents ──consume──> latest symlinks
  Never reference timestamped filenames directly.

architecture.md
  Maps every figure to its script, data, runs, and CLI command.
  The glue between code and deliverable.

audit.md
  Tracks inconsistencies across everything above.
  Resolved before submission.
```
