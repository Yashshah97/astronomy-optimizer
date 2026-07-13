# Architecture Plan

- `astronomy_optimizer/core.py` — main domain logic and public entry points
- `astronomy_optimizer/models.py` — data classes for the domain objects
- `astronomy_optimizer/io_utils.py` — reading and writing data files
- `astronomy_optimizer/analysis.py` — computation and analysis helpers
- `astronomy_optimizer/validation.py` — input validation and error types
- `astronomy_optimizer/formatting.py` — human-readable output formatting
- `astronomy_optimizer/config.py` — configuration loading with defaults
- `astronomy_optimizer/cli.py` — argparse-based command-line interface
