"""Demo for Astronomy Parameter Optimizer."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import astronomy_optimizer

print("Astronomy Parameter Optimizer", "v" + astronomy_optimizer.__version__)
print("modules:", [m for m in dir(astronomy_optimizer) if not m.startswith('_')])
