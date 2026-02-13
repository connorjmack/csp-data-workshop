# GitHub Account Setup

GitHub is where developers store, share, and collaborate on code. You'll use it throughout this workshop and in your career.

---

## Create Your Account

### 1. Go to GitHub

```
https://github.com/signup
```

### 2. Enter your details

- **Email:** Use your university email (`.edu`) — this qualifies you for free GitHub Pro later
- **Password:** Choose a strong, unique password
- **Username:** Pick something professional (e.g., `jsmith-data`, `jane-doe-23`). This will be visible publicly.

!!! tip "Username advice"
    Your GitHub username becomes part of your public profile URL (`github.com/your-username`). Employers and collaborators will see this — keep it professional.

### 3. Complete verification

- Solve the CAPTCHA puzzle
- Enter the verification code sent to your email
- Choose the **Free** plan (you can upgrade later)

### 4. Skip the personalization (or fill it in)

GitHub will ask about your experience level and interests. You can skip this or fill it out — it just customizes your dashboard.

---

## Configure Your Profile

Once your account is created:

1. Click your **profile icon** → **Settings**
2. Add a **profile picture** (optional but recommended)
3. Add your **name** and a short **bio** (e.g., "MS Data Engineering student @ University")
4. Set your email visibility preferences under **Emails**

---

## Apply for GitHub Education (Optional but Recommended)

GitHub offers free Pro features for students:

1. Visit [education.github.com/benefits](https://education.github.com/benefits)
2. Click **Get student benefits**
3. Verify with your `.edu` email and/or student ID
4. Benefits include: unlimited private repos, GitHub Copilot access, and more

!!! info "Approval can take a few days"
    Don't wait for this — continue with the workshop. The free plan has everything you need for now.

---

## Install Git (if not already installed)

Git is the version control tool that powers GitHub. Check if it's already installed:

```bash
git --version
```

If you see a version number (e.g., `git version 2.43.0`), you're good. If not:

=== "macOS"

    ```bash
    # Install via Homebrew (recommended)
    brew install git

    # Or install Xcode Command Line Tools (includes git)
    xcode-select --install
    ```

=== "Windows"

    Download and install from [git-scm.com/downloads](https://git-scm.com/downloads).

    During installation, accept the defaults. Make sure **"Git Bash"** is selected.

=== "Linux (Ubuntu/Debian)"

    ```bash
    sudo apt update && sudo apt install git -y
    ```

### Configure Git with your identity

After installing, tell Git who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@university.edu"
```

Verify your config:

```bash
git config --list
```

---

## Troubleshooting

??? question "I already have a personal GitHub account"
    That's fine! You can use your existing account. Just make sure to add your `.edu` email under **Settings → Emails** so you can apply for student benefits.

??? question "`git` command not found on macOS"
    Run `xcode-select --install` and follow the prompts. This installs Apple's developer command line tools, which include Git.

??? question "I'm on Windows and the terminal looks different"
    Use **Git Bash** (installed with Git) for a Unix-like terminal experience. You can also use **Windows Terminal** with WSL for a full Linux environment.

---

**Next:** [Your First Repository →](01c-first-repo.md)
