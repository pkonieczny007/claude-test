# claude-test

A Flask web application with SQLite persistence, managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

## Running

```bash
uv run flask --app claude_test.app:create_app run --debug
```

The app will be available at `http://127.0.0.1:5000`.

## Pages

- **/** — Homepage
- **/dashboard** — Dashboard with user count
- **/settings** — Save username and theme preferences
- **/health** — JSON health check

## Development

```bash
# Run tests
uv run pytest

# Lint
uv run ruff check .

# Format
uv run ruff format .
```

## Project Structure

```
src/claude_test/
  app.py        — Application factory
  models.py     — SQLAlchemy models (User)
  routes.py     — Route definitions
  templates/    — Jinja2 templates
tests/
  conftest.py   — Test fixtures (in-memory SQLite)
  test_app.py   — Tests
```
