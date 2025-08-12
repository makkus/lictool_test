[![PyPI status](https://img.shields.io/pypi/status/lictool_test.svg)](https://pypi.python.org/pypi/lictool_test/)
[![PyPI version](https://img.shields.io/pypi/v/lictool_test.svg)](https://pypi.python.org/pypi/lictool_test/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/lictool_test.svg)](https://pypi.python.org/pypi/lictool_test/)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fmakkus%2Fkiara%2Fbadge%3Fref%3Ddevelop&style=flat)](https://actions-badge.atrox.dev/makkus/lictool_test/goto?ref=develop)
[![Coverage Status](https://coveralls.io/repos/github/makkus/lictool_test/badge.svg?branch=develop)](https://coveralls.io/github/makkus/lictool_test?branch=develop)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# [**kiara**](https://dharpa.org/kiara.documentation) plugin: (lictool_test)

Python project to test pre-commit issues with ruff and lictool

 - Documentation: [https://makkus.github.io/lictool_test](https://makkus.github.io/lictool_test)
 - Code: [https://github.com/makkus/lictool_test](https://github.com/makkus/lictool_test)
 - `kiara`: [https://docs.dharpa.org](https://docs.dharpa.org)

## Description

TODO

## Development

### Requirements

- uv ( https://docs.astral.sh/uv/ )
- git
- make (on Linux / Mac OS X -- optional)
- just (optional)

### Check out the source code & enter the project directory

```
git clone https://github.com/makkus/lictool_test
cd lictool_test
```

### Prepare development environment

The recommended way to setup a development environment is to use [uv](https://docs.astral.sh/uv/). Check out [their install instructions](https://docs.astral.sh/uv/getting-started/installation/).

Once you have `uv` installed, you can either run `kiara` using the `uv run` command:

```
uv run kiara module list
```

or, activate the virtual environment and run `kiara` directly:

```
uv sync  # to make sure the virtualenv exists (and is up to date)
source .venv/bin/activate
kiara module list
```

### Running pre-defined development-related tasks (using `just`)

The included `Makefile` file includes some useful tasks that help with development. This requires `uv` and the `make` tool to be
installed, which should be the case for Linux & Mac OS X systems.

- `just tests`: runs all unit tests
- `just test <pattern>`: runs all unit tests whose name matches the given pattern
- `just typecheck`: run type-checker
- `just lint`: run the `ruff` linter on the source code
- `just format`: run the `ruff` formatter on the source code (similar to `black`)

Alternatively, if you don't have the `just` command available, you can use `uv` directly to run those tasks:

- `uv run pytest tests`
- `uv run mypy src/`
- `uv run ruff check --fix src/`
- `uv run ruff format src/`

## Copyright & license

This project is published under the Apache-2.0 license, for the license text please check the [LICENSE](/LICENSE) file in this repository.
