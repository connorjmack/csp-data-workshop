# Your First Repository

A **repository** (or "repo") is a folder that Git tracks. It stores your code, its history, and metadata. Let's create your first one.

---

## Create a Repo on GitHub

### 1. Click the **+** icon in the top-right corner of GitHub

Select **New repository**.

### 2. Fill in the details

| Field | Value |
|-------|-------|
| **Repository name** | `data-engineering-workshop` |
| **Description** | "My work from the Data Engineering Workshop" |
| **Visibility** | Public (or Private — your choice) |
| **Initialize** | :white_check_mark: Add a README file |
| **`.gitignore`** | Select **Python** |
| **License** | MIT (or None) |

### 3. Click **Create repository**

You now have a repo at `github.com/your-username/data-engineering-workshop`.

---

## Clone It to Your Computer

**Cloning** downloads a copy of the repo to your local machine so you can work on it.

### 1. Copy the repo URL

On your repo page, click the green **Code** button and copy the **HTTPS** URL:

```
https://github.com/your-username/data-engineering-workshop.git
```

### 2. Open your terminal

=== "macOS"

    Open **Terminal** (search for it in Spotlight with `Cmd + Space`).

=== "Windows"

    Open **Git Bash** (search for it in the Start menu).

=== "Linux"

    Open your terminal emulator (`Ctrl + Alt + T` on Ubuntu).

### 3. Navigate to where you want the repo

```bash
# Go to your home directory
cd ~

# Create a projects folder (optional, but keeps things organized)
mkdir -p projects
cd projects
```

### 4. Clone the repo

```bash
git clone https://github.com/your-username/data-engineering-workshop.git
```

You should see output like:

```
Cloning into 'data-engineering-workshop'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
Receiving objects: 100% (4/4), done.
```

### 5. Enter the repo

```bash
cd data-engineering-workshop
```

### 6. Verify everything

```bash
# Check you're in a git repo
git status

# See the files
ls -la
```

You should see your `README.md` and `.gitignore` files.

---

## Make Your First Commit

Let's make a small change to practice the Git workflow.

### 1. Edit the README

Open `README.md` in any text editor and add a line:

```markdown
# Data Engineering Workshop

My work from the Data Engineering Workshop.

## Setup
- [x] Created GitHub account
- [x] Cloned this repository
- [ ] Installed Gemini CLI
- [ ] Completed Keeling Curve demo
```

### 2. Stage, commit, and push

```bash
# See what changed
git status

# Stage the file
git add README.md

# Commit with a message
git commit -m "Update README with workshop progress checklist"

# Push to GitHub
git push
```

!!! success "Check GitHub"
    Refresh your repo page on GitHub — you should see your updated README rendered beautifully.

---

## Key Git Concepts

| Concept | What it means |
|---------|---------------|
| **Repository** | A folder tracked by Git |
| **Clone** | Download a repo to your machine |
| **Stage** (`git add`) | Mark files to include in the next commit |
| **Commit** (`git commit`) | Save a snapshot of staged changes |
| **Push** (`git push`) | Upload commits to GitHub |
| **Pull** (`git pull`) | Download the latest changes from GitHub |

---

**Next:** [Terminal Basics →](02-terminal-basics.md)
