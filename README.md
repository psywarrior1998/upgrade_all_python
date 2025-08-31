# Ultimate Python Upgrader (`py-upgrade`)

[![PyPI version](https://badge.fury.io/py/ultimate-python-upgrader.svg)](https://badge.fury.io/py/ultimate-python-upgrader)
[![CI](https://github.com/psywarrior1998/upgrade_all_python/actions/workflows/ci.yml/badge.svg)](https://github.com/psywarrior1998/upgrade_all_python/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, feature-rich CLI tool to manage and upgrade Python packages with a clean, modern interface and a powerful dependency safety-net.

## Key Features

  - **🛡️ Atomic Upgrades with Rollback**: If an upgrade fails for any reason (e.g., compilation error, network issue), the tool automatically reverts the package to its previous stable version. This ensures your environment is never left in a broken state.
  - **🔎 Intelligent Dependency Analysis**: Performs a pre-flight check using `pip` to detect and warn you about potential dependency conflicts *before* you upgrade.
  - **⚡ Concurrent & Fast**: Upgrades packages in parallel using a configurable number of workers, dramatically reducing the time you spend waiting.
  - **📊 Rich & Interactive UI**: Uses `rich` to display outdated packages in a clean, readable table with clear progress bars and status updates.
  - **🎯 Selective Upgrades**: Upgrade all packages at once, or specify exactly which packages to include or exclude from an upgrade operation.
  - **⛑️ Safety First**: Includes a `--dry-run` mode to see what would be upgraded without making any changes to your environment.
  - **🤖 Automation Friendly**: A `--yes` flag allows for non-interactive use in automated scripts and CI/CD pipelines.

## Installation

The tool is available on PyPI. Install it with pip:

```bash
pip install ultimate-python-upgrader
```

## Usage

Once installed, the `py-upgrade` command will be available.

**1. Check for outdated packages and upgrade all interactively**

```bash
py-upgrade
```

**2. Upgrade specific packages**

```bash
py-upgrade requests numpy
```

**3. Upgrade all packages except a few**

```bash
py-upgrade --exclude black ruff
```

**4. Perform a dry run to see what needs upgrading**

```bash
py-upgrade --dry-run
```

**5. Run non-interactively for automation**

```bash
py-upgrade --yes
```

**6. Increase concurrency for faster upgrades**

```bash
py-upgrade --workers 20
```

## Contributing

Contributions are welcome\! This project uses `black` for formatting and `ruff` for linting.

To get started with development:

1.  Clone the repository.
2.  Create a virtual environment: `python -m venv .venv`
3.  Activate it: `source .venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4.  Install the project in editable mode with all development dependencies:
    ```bash
    pip install -e ".[test,dev]"
    ```
5.  Run tests with `pytest`.

Please feel free to submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
