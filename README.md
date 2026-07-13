# Astronomy Parameter Optimizer

This project provides a flexible and efficient tool for optimizing parameters in astronomy data, allowing users to fine-tune their models with various search algorithms and strategies. Built from the ground up in pure Python, this library is designed to be easy to use and integrate into existing workflows. With comprehensive testing and documentation, it's ready to help astronomers refine their understanding of celestial phenomena.

## What makes it unique

Combines star catalogs and light curves with a search-based tuner (grid, random, and annealing strategies) — a niche where few ready-made tools exist.

## Features

- **`astronomy_optimizer/core.py`** — main domain logic and public entry points
- **`astronomy_optimizer/models.py`** — data classes for the domain objects
- **`astronomy_optimizer/io_utils.py`** — reading and writing data files
- **`astronomy_optimizer/analysis.py`** — computation and analysis helpers
- **`astronomy_optimizer/validation.py`** — input validation and error types
- **`astronomy_optimizer/formatting.py`** — human-readable output formatting
- **`astronomy_optimizer/config.py`** — configuration loading with defaults
- **`astronomy_optimizer/cli.py`** — argparse-based command-line interface

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (8/8 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/astronomy-optimizer.git
cd astronomy-optimizer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
astronomy-optimizer/
├── astronomy_optimizer/
│   ├── core.py
│   ├── models.py
│   ├── io_utils.py
│   ├── analysis.py
│   ├── validation.py
│   ├── formatting.py
│   ├── config.py
│   ├── cli.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **astronomy** · Archetype: **optimizer** ·
Built autonomously by JARVIS on 2026-07-12. MIT licensed.
