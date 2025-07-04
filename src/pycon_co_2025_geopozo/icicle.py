"""Helps convert viztracer jsons to a flamegraph."""
import json
import subprocess
from pathlib import Path
from typing import Literal

BranchValuesOptions = Literal["total", "remainder"]

def sort_and_strip_json(path: Path | str):
    try:
        path = str(path)
        jq_filter = (
            '.traceEvents'
            ' | [ .[]'
            '     | select(.ph == "X" and .cat == "FEE")'
            '     | {tid, ts, dur, name}'
            '   ]'
            ' | sort_by(.tid)'
            ' | group_by(.tid)'
            ' | map({ (.[0].tid|tostring): (sort_by(.ts)) })'
            ' | add'
        )
        # run jq, capture its stdout
        proc = subprocess.run(
            ["jq", jq_filter, path],
            capture_output=True,
            text=True,
            check=True
        )
        # parse the JSON output back into Python
        return json.loads(proc.stdout)
    except Exception as e:
        raise RuntimeError("This requires jq to be installed.") from e

def from_threads(thread_events_dict):
    """
    Given a dict mapping thread IDs to a SORTED list of events
    (each event a dict with keys 'ts', 'dur', 'name', 'tid']),
    produce Plotly Icicle-format flat lists: labels, parents, values.
    """
    labels = []
    parents = []
    values = []

    # Iterate each thread
    counter = {}
    for tid, events in thread_events_dict.items():
        # Thread root
        thread_label = f"Thread {tid}"
        labels.append(thread_label)
        parents.append("")       # no parent
        values.append(0)         # will accumulate top-level durations

        root_idx = len(labels) - 1
        stack = []  # holds (end_ts, label)

        # Events list assumed sorted by 'ts'
        for ev in events:
            start = ev["ts"]
            dur   = ev["dur"]
            name  = ev["name"]
            end   = start + dur

            # Pop completed spans
            while stack and start >= stack[-1][0]:
                stack.pop()

            # Parent is top of stack or thread root
            parent_label = stack[-1][1] if stack else thread_label

            # Ensure each label is unique: incorporate tid and serial index
            i = counter.setdefault(name, 0)
            counter[name] += 1

            node_label = f"{name.split(" ")[0]}#{i!s}"

            labels.append(node_label)
            parents.append(parent_label)
            values.append(dur)

            # Track this span
            stack.append((end, node_label))

            # If it's not nested, accumulate at thread root
            if len(stack) == 1:
                values[root_idx] += dur

    return labels, parents, values
