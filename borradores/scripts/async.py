"""A basic testing showing sync/async diferences in pyodide."""
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import asyncio
from pathlib import Path

import viztracer


async def bar():
    """Test function."""
    asyncio.sleep(0.05)

async def foo():
    """Test function."""
    await bar()
    await bar()

### viztracer example ###

output_dir = Path("results")
output_dir.mkdir(parents=True, exist_ok=True)

with viztracer.VizTracer(
    enable_asyncio=True,
    output_file=str(output_dir/"async_profile.json"),
) as tracer:
    asyncio.run(foo())

# or no flamegraph and output_type="html" for more
# or output_file="viztracer_profile.json" and `vizviewer viztracer.json`
# or use chrome's chrome://tracing
