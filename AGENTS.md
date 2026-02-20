# AGENTS.md

## Cloud-specific instructions

### Overview

Python-only repo of ESPN OpenAPI specs and auto-generated API clients. No local services, databases, or Docker required. All tests hit live ESPN APIs over the network.

### Dependencies

- **Package manager:** `uv` (installed at `~/.local/bin/uv`; ensure `$HOME/.local/bin` is on `PATH`)
- **Python:** ≥3.9 (system Python 3.12 works)
- **Install deps:** `uv sync --all-extras` (installs both runtime and dev dependencies from `uv.lock`)
- **Extra pytest plugins:** `pytest-xdist` and `pytest-retry` are required by `pytest.ini` but not listed in `pyproject.toml`. Install them with: `uv pip install pytest-xdist pytest-retry`

### Running tests

Tests call live ESPN APIs and require network access. See `pytest.ini` for config.

- **All tests:** `uv run pytest`
- **Single file:** `uv run pytest tests/test_scoreboard.py -v`
- **Via Makefile:** `make run-test TEST_FILE=tests/test_scoreboard.py`

Tests run in parallel (`-n auto` via pytest-xdist) with retries (`--retries 2`).

### Linting

- `uv run ruff check .`
- `uv run black --check .`
- `uv run isort --check .`

### Code generation

Regenerate Python clients from OpenAPI specs: `make openapi` (requires `openapi-python-client` which is included in dev deps).
