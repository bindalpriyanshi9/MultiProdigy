## 👥 Contributing to MultiProdigy

Thank you for considering contributing to MultiProdigy! We welcome community involvement to improve and expand the framework. Please follow these guidelines to ensure a smooth workflow.

---

### 🧱 Project Setup

To get started:

1. **Clone the repo**

   ```bash
   git clone https://github.com/Abhay-Cerberus/MultiProdigy.git
   cd MultiProdigy
   ```

2. **Install dependencies**

   ```bash
   poetry install
   ```

3. **Set your PYTHONPATH** (for Windows PowerShell):

   ```powershell
   $env:PYTHONPATH = ".\MultiProdigy"
   ```

---

### 🌱 Branching Strategy

| Branch      | Purpose                      |
| ----------- | ---------------------------- |
| `main`      | Stable production-ready code |
| `develop`   | Integration of all features  |
| `feature/*` | Feature development branches |
| `fix/*`     | Bugfix branches              |
| `docs/*`    | Documentation updates        |

---

### 🔁 Pull Requests

* **Branch from**: `develop`
* **PR Title**: use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)

  * `feat: add streaming support to MessageBus`
  * `fix: resolve race condition in AgentScheduler`
* **Checklist Before Submitting:**

  * ✅ All tests pass (`pytest tests/`)
  * ✅ Code is formatted with `black .` and `isort .`
  * ✅ Includes related issue number (`Closes #123`)
  * ✅ Relevant documentation updated

---

### 📐 Coding Style

* Follow **PEP8**
* Use `black` for consistent formatting:

  ```bash
  black .
  ```
* Use `isort` for clean imports:

  ```bash
  isort .
  ```

---

### 🧪 Testing

Tests live under the `tests/` directory. To run them:

```bash
pytest tests/
```

Write tests for:

* All new functionality
* Bugfixes (include a regression test)

---

### 🧾 Writing Issues

Before submitting an issue:

* Check [existing issues](https://github.com/Abhay-Cerberus/MultiProdigy/issues)
* Use the templates:

  * **Bug report**: provide minimal reproduction steps
  * **Feature request**: explain the motivation and use case

---

### 📎 Documentation

All user-facing changes must include relevant doc updates in `docs/`.

Pages include:

* `getting_started.md`
* `architecture.md`
* `modules_reference.md`

To preview docs locally:

```bash
mkdocs serve
```

---

### 💡 Good First Issues

If you're new, look for [good first issues](https://github.com/Abhay-Cerberus/MultiProdigy/labels/good%20first%20issue) — these are beginner-friendly and well-scoped.

---

### 💬 Communication

For discussions, ideas, or questions:

* Use GitHub Discussions or Issues
* Respect the [Code of Conduct](https://github.com/Abhay-Cerberus/MultiProdigy/blob/main/CODE_OF_CONDUCT.md)

---

### 🙏 Thank You!

Your contributions make MultiProdigy better — we appreciate your time and ideas!

