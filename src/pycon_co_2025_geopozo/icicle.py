"""Helps convert viztracer jsons to a flamegraph."""
from typing import Literal

import plotly.graph_objects as go

BranchValuesOptions = Literal["total", "remainder"]

def from_viztrace(tree, branchvalues="total"):
    """
    Convert a VizTracer-JSON to a Plotly Icicle figure.

    Args:
        tree (dict): Root node of the viztracer json
        branchvalues (str): Change branchvalue setting in go.Icicle

    Returns:
        fig (plotly.graph_objects.Figure): Icicle figure.

    """
    labels = []
    parents = []
    values = []

    def _traverse(node, parent_name):
        labels.append(node["name"])
        parents.append(parent_name)
        values.append(node["value"])
        for child in node.get("children", []):
            _traverse(child, node["name"])

    # Initialize recursion (root's parent should be "")
    _traverse(tree, "")

    return go.Figure(go.Icicle(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues=branchvalues
    ))
