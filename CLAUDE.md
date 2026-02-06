# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flask web application using Python 3.12, managed with uv.

## Commands

- **Install dependencies:** `uv sync`
- **Run dev server:** `uv run flask --app claude_test.app:create_app run --debug`
- **Run all tests:** `uv run pytest`
- **Run a single test:** `uv run pytest tests/test_app.py::test_index`
- **Lint:** `uv run ruff check .`
- **Lint with auto-fix:** `uv run ruff check . --fix`
- **Format:** `uv run ruff format .`

## Architecture

- `src/claude_test/app.py` — Application factory (`create_app()`) and entry point
- `src/claude_test/routes.py` — Route definitions, registered via `register_routes(app)`
- `tests/` — Pytest tests using Flask's test client

Routes are registered in `routes.py` and wired into the app via `register_routes()` in the factory. New route modules should follow this pattern.

## Security Note

The `cctest` file contains a plaintext API key and is gitignored. Never commit credentials to the repository.
