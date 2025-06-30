"""A basic testing showing sync/async diferences in pyodide."""
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import sys
import time
from pathlib import Path

import viztracer


def bar():
    """Test function."""
    time.sleep(0.05)

def foo():
    """Test function."""
    bar()
    bar()

### viztracer example ###


if sys._is_gil_enabled(): # noqa: SLF001
    print("The GIL is currently enabled.")
else:
    print("The GIL is currently disabled.")

output_dir = Path("results")
output_dir.mkdir(parents=True, exist_ok=True)

with viztracer.VizTracer(
    output_file=str(output_dir/"viztracer_profile.json"),
) as tracer:
    foo()
