"""Run from the repository root: python scripts/run_ordinal.py [optional data path]."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1] / 'overleaf/ordinal_regression/code/run_ordinal.py'), run_name='__main__')
