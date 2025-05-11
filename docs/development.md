# Development Guide

This document outlines the development setup and process for working on the Wagtail WordPress Import package.

## Setting up a development environment

### Prerequisites

- Python 3.9 or higher
- pip or [uv](https://docs.astral.sh/uv/) (recommended)
  - uv is a modern Python package installer and resolver that's significantly faster than pip
  - Install uv with: `pip install uv`

### Installation

Clone the repository:

```bash
    git clone https://github.com/torchbox/wagtail-wordpress-import.git
    cd wagtail-wordpress-import
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

Install the package in development mode with development dependencies:

```bash
# Using uv (recommended)
uv pip install -e ".[dev,testing]"

# Using pip
pip install -e ".[dev,testing]"
```

## Development Tools

The project uses several development tools that are installed as part of the development dependencies:

- **black**: Code formatter (enforces consistent code style)
- **flake8**: Linter (finds code quality issues)
- **isort**: Import sorter (organizes imports alphabetically and by type)
- **pre-commit**: Runs checks before committing code

### Setting up pre-commit

Pre-commit hooks help ensure code quality by running checks before each commit:

```bash
pre-commit install
```

After installation, pre-commit will automatically run the configured hooks on any files you attempt to commit.

## Running Tests

To run tests:

```bash
# Run all tests
python testmanage.py test

# Run tests with coverage
coverage run testmanage.py test
coverage report
```

## Project Structure

- **src/wagtail_wordpress_import/**: Core package code
  - **importers/**: Import functionality
  - **management/commands/**: Management commands for the package
  - **migrations/**: Database migrations
  - **prefilters/**: Content pre-processing filters
  - **static/**: Static files
  - **templates/**: HTML templates
  - **test/**: Test configuration
- **docs/**: Documentation files
- **tests/**: Test files

## Configuration Files

- **pyproject.toml**: Main project configuration (dependencies, build settings, tools)
- **tox.ini**: Configuration for running tests in multiple environments
- **uv.lock**: Dependency lock file (when using uv)

## Build System

This project uses [hatchling](https://hatch.pypa.io/) as the build backend. The package configuration is defined in `pyproject.toml`.

## Publishing

To build the package for distribution:

```bash
# Install build dependencies
pip install build

# Build the package
python -m build
```

To publish to PyPI:

```bash
# Install twine
pip install twine

# Upload to PyPI
python -m twine upload dist/*
```

## References

- [uv Documentation](https://docs.astral.sh/uv/)
- [hatchling Documentation](https://hatch.pypa.io/)
- [Wagtail Documentation](https://docs.wagtail.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Packaging User Guide](https://packaging.python.org/)
