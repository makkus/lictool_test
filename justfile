default:
    @just --list

typecheck:
    uv run ty check --python=.venv/ src/lictool_test

lint:
    uv run ruff check src . --fix

format:
    uv run ruff format src .

tests:
    uv run pytest tests -s

test pattern:
    uv run pytest tests -s -k
