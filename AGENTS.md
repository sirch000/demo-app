# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

Minimal Python project using `pyproject.toml` for configuration. Single package (`hello`) with a CLI entry point.

### Development environment

- **Python**: 3.12 (system), virtual environment at `.venv/`
- **Package manager**: pip with `pyproject.toml`
- **Linter/formatter**: ruff (configured in `pyproject.toml`)
- **Test framework**: pytest (configured in `pyproject.toml`)

### Common commands

| Task | Command |
|------|---------|
| Activate venv | `. .venv/bin/activate` |
| Install deps | `pip install -e . && pip install ruff pytest` |
| Lint | `ruff check .` |
| Format check | `ruff format --check .` |
| Run tests | `pytest -v` |
| Run app | `hello` or `python -m hello.main` |

### Notes

- The `python3.12-venv` system package must be installed for venv creation (`sudo apt-get install -y python3.12-venv`).
- Always activate the venv before running any project commands.
