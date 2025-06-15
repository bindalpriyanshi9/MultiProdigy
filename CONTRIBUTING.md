<!-- CONTRIBUTING.md -->
# Contributing to Prodigal AI Agents Framework

Thank you for your interest in contributing! This document covers:

1. [Branching Strategy](#branching-strategy)  
2. [Pull Request Etiquette](#pull-request-etiquette)  
3. [Coding Style](#coding-style)  
4. [Running Tests Locally](#running-tests-locally)  
5. [Issues vs. Pull Requests](#issues-vs-pull-requests)

---

## Branching Strategy

- **`main`** — always contains stable, released code (v0.1.0, v0.2.0, …).  
- **`develop`** — integration branch for features completed and reviewed.  
- **`feature/<short-description>`** — new work; merge into `develop` when ready.  
- **`hotfix/<short-description>`** — urgent fixes; merge into both `main` and `develop`.

---

## Pull Request Etiquette

1. Base branch → `develop` (unless it’s a hotfix).  
2. Title: `feat: <short summary>` or `fix: <short summary>`.  
3. In description, include:  
   - What changed and why.  
   - Issue number being closed (e.g. `Closes #42`).  
   - Screenshots or logs if relevant.  
4. Assign at least one reviewer and request review when ready.  
5. Don’t merge your own PR; wait for approval.

---

## Coding Style

- **Format** with [Black](https://black.readthedocs.io/) (run `black .`).  
- **Import sorting** with [isort](https://pycqa.github.io/isort/) (run `isort .`).  
- **Lint** with `flake8` (max line length = 88).  
- **Type hints** encouraged for all public functions and classes.

---

## Running Tests Locally

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run all tests
pytest --maxfail=1 --disable-warnings -q
