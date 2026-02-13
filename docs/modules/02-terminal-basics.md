# Navigating the Terminal

The terminal (also called the command line, shell, or console) is how you talk to your computer using text instead of clicking. Every data engineer uses it daily.

!!! note ":beginner: Beginners"
    If you've never used a terminal before, read this whole page. If you're comfortable with `cd`, `ls`, and `pwd`, skip to [Essential Commands](02b-essential-commands.md).

---

## Opening the Terminal

=== "macOS"

    **Option 1:** Press `Cmd + Space`, type `Terminal`, press Enter.

    **Option 2:** Go to Applications → Utilities → Terminal.

    **Recommended:** Install [iTerm2](https://iterm2.com/) for a better experience.

=== "Windows"

    **Option 1:** Open **Git Bash** (installed with Git).

    **Option 2:** Open **Windows Terminal** from the Start menu.

    **Recommended:** Install [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) for a full Linux environment:
    ```powershell
    wsl --install
    ```

=== "Linux"

    Press `Ctrl + Alt + T` on most distributions, or search for "Terminal" in your app launcher.

---

## The Prompt

When you open the terminal, you'll see something like this:

```
username@computer:~$
```

This is your **prompt** — it tells you who you are, what computer you're on, and where you are in the file system. The `~` means you're in your **home directory**.

The `$` (or `%` on some systems) means the terminal is ready for your input.

---

## Your First Commands

### Where am I?

```bash
pwd
```

**P**rint **W**orking **D**irectory — shows your current location in the file system.

```
/home/username
```

### What's in this folder?

```bash
ls
```

**L**i**s**t — shows the files and folders in your current directory.

```bash
# Show hidden files too (files starting with a dot)
ls -a

# Show details (permissions, size, date)
ls -l

# Combine both
ls -la
```

### How do I move around?

```bash
# Go into a folder
cd projects

# Go up one level
cd ..

# Go to your home directory
cd ~

# Go to an absolute path
cd /home/username/projects
```

!!! tip "Tab completion"
    Start typing a folder name and press **Tab** — the terminal will auto-complete it for you. This saves time and prevents typos.

---

## Understanding the File System

Your computer's files are organized in a tree structure:

```
/                        ← Root (the very top)
├── home/
│   └── username/        ← Your home directory (~)
│       ├── Desktop/
│       ├── Documents/
│       ├── Downloads/
│       └── projects/    ← Where we'll work
│           └── data-engineering-workshop/
├── usr/
│   └── bin/             ← System programs live here
└── tmp/                 ← Temporary files
```

**Key concepts:**

- **Absolute path:** Starts from root `/` — e.g., `/home/username/projects`
- **Relative path:** Starts from where you are — e.g., `projects` (if you're in `~`)
- `..` means "parent directory" (one level up)
- `.` means "current directory"
- `~` means "home directory"

---

## Practice Exercise

Try this sequence of commands:

```bash
# 1. Check where you are
pwd

# 2. Go home
cd ~

# 3. List everything
ls -la

# 4. Create a test folder
mkdir terminal-practice

# 5. Enter it
cd terminal-practice

# 6. Verify
pwd

# 7. Create a file
touch hello.txt

# 8. Verify the file exists
ls

# 9. Go back up
cd ..

# 10. Clean up
rm -r terminal-practice
```

!!! success "If you completed all 10 steps, you're ready to move on!"

---

**Next:** [Essential Commands →](02b-essential-commands.md)
