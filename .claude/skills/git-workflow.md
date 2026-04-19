# Skill: Git Workflow

Follow these steps every time a logical unit of work is complete.

## 1. Check what changed
```bash
git status
git diff
```
Review every changed file before staging anything.

## 2. Run quality checks
```bash
cd backend && ruff check . && ruff format --check .
cd backend && mypy app
cd backend && pytest
```
Do not proceed if any check fails. Fix the issue first.

## 3. Create a branch (if not already on one)
```bash
git checkout -b <type>/<short-description>
```
Never commit directly to main.

## 4. Stage and commit
```bash
git add <specific files>   # never use git add .
git commit -m "<type>(<scope>): <short description>"
```
Follow the commit format in .claude/rules/git.md.
Stage specific files deliberately — do not blindly add everything.

## 5. Before pushing
- Confirm you are not on main: `git branch`
- Confirm no .env or secret files are staged: `git diff --cached`
- Confirm the commit message follows the convention

## 6. Push
```bash
git push -u origin <branch-name>
```

## When to commit
- After each working layer (data service, API endpoints, models, etc.)
- After adding or updating tests
- After any migration file is created
- Never in the middle of a broken state — the repo should always
  be in a working condition after every commit
