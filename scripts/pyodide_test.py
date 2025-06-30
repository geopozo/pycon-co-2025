"""A basic testing showing sync/async diferences in pyodide."""
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import time
from pathlib import Path

import pyinstrument
import viztracer

output_dir = Path("results")
output_dir.mkdir(parents=True, exist_ok=True)

def bar():
    """Test function."""
    time.sleep(0.05)

def foo():
    """Test function."""
    bar()
    bar()

### pyinstrument example ###

with pyinstrument.Profiler(use_timing_thread=True) as profiler:
    foo()

with (output_dir/"pyinstrument_profile.html").open("w") as f:
    f.write(profiler.output_html())

### viztracer example ###

with viztracer.VizTracer(
    output_file=str(output_dir/"viztracer_profile.html"),
) as tracer:
    foo()

# or no flamegraph and output_type="html" for more
# or output_file="viztracer_profile.json" and `vizviewer viztracer.json`
# or use chrome's chrome://tracing
