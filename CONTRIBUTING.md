# Contributing

Thank you for your interest in contributing to this project.

## Development Environment

**Prerequisites:**

- Python 3.10 or later
- pip (bundled with Python)

**Setup:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

> **Note:** This package is ROS-independent but includes `package.xml` and a
> `resource/` marker for colcon workspace compatibility. You do not need a ROS
> installation to develop or test.

## Running Tests

Tests use the `unittest` framework and are executed via `pytest`:

```bash
python -m pytest tests/
```

For verbose output with JUnit XML (mirrors CI):

```bash
python -m pytest --junitxml=test-results/results.xml tests/
```

## Linting

The CI pipeline runs `flake8` for style checks:

```bash
flake8 .
```

Fix any reported issues before opening a pull request.

## Branching Convention

- Create a feature branch from `main` with a descriptive name, e.g.
  `feat/add-logging` or `fix/ascii-art-encoding`.
- Keep commits atomic - each commit should represent a single logical change.
- Write clear commit messages following the conventional commits style
  (`feat:`, `fix:`, `docs:`, `build:`, etc.).

## Pull Request Requirements

1. All CI checks must pass (tests across Python 3.10/3.11/3.12 and flake8).
2. At least one approving review from a code owner.
3. PR description should explain **what** changed and **why**.
4. Reference any related issues (e.g. `Closes #42`).
