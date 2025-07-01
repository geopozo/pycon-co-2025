"""dag helps create graphs from function dictionaries."""
from typing import TypeAlias, cast

from graphviz import Digraph  # type: ignore[import-untyped]
from graphviz.backend.execute import ExecutableNotFound  # type: ignore[import-untyped]

Node: TypeAlias = ( # noqa: UP040 mypy disagrees
    str
        | list[str]
        | tuple[str, ...]
        | dict[str, "Node"]
)

def _dict_to_edges_and_labels( # noqa: C901
        tree: Node
) -> tuple[list[tuple[str, str]], dict[str, str]]:

    edges: list[tuple[str, str]]= []
    labels: dict[str, str] = {}
    counts: dict[str, int] = {}

    def make_id(label: str) -> str:
        counts[label] = counts.get(label, 0) + 1
        node_id = f"{label}_{counts[label]}"
        labels[node_id] = label
        return node_id

    def walk(subtree: Node, parent_id: str | None=None) -> None: # noqa: C901
        # If we're at the top-level dict, seed the roots
        if parent_id is None:
            if isinstance(subtree, dict):
                for root_label, child in subtree.items():
                    root_id = make_id(root_label)
                    walk(child, root_id)
            elif isinstance(subtree, (list, tuple)):
                for root_label in subtree:
                    root_id = make_id(root_label)
            elif isinstance(subtree, str):
                root_id = make_id(subtree)
            return

        # Otherwise, traverse children
        if isinstance(subtree, dict):
            for child_label, child_sub in subtree.items():
                child_id = make_id(child_label)
                edges.append((parent_id, child_id))
                walk(child_sub, child_id)
        elif isinstance(subtree, (list, tuple)):
            for child_label in subtree:
                child_id = make_id(child_label)
                edges.append((parent_id, child_id))
        else:
            # leaf that's not list/dict
            leaf_id = make_id(str(subtree))
            edges.append((parent_id, leaf_id))

    walk(tree)
    return edges, labels

def _render_dag(tree: Node) -> str:
    """Render html string of svg."""
    edges, labels = _dict_to_edges_and_labels(tree)
    dot = Digraph(format="svg")
    dot.graph_attr["bgcolor"] = "transparent"
    dot.graph_attr["rankdir"] = "LR"
    dot.attr("graph", bgcolor="transparent", fontname="sans-serif", fontsize="14")
    dot.attr("edge", fontname="sans-serif", fontsize="12")
    dot.attr("node",
        style="filled",
        fillcolor="transparent",
        fontname="sans-serif",
        fontsize="16",
        penwidth="1"  # ← important to avoid thick outlines
)

    # Add all nodes (with display labels)
    for node_id, label in labels.items():
        dot.node(node_id, label=label)

    # Add all edges
    for parent_id, child_id in edges:
        dot.edge(parent_id, child_id)

    return cast(str, dot.pipe().decode("utf-8"))   # raw <svg>…</svg> string

# Example usage:
def from_function_tree(tree: Node) -> str:
    """Render html string of style + svg."""
    try:
        svg = _render_dag(tree)
    except ExecutableNotFound as e:
        raise RuntimeError(
            "You must install graphviz to use this function. "
            "https://graphviz.org/download/"
        ) from e

    return """
    <style>
      /* Set default text + line color via currentColor */
      svg * {
        stroke: currentColor;
      }
      svg text {
          fill: currentColor;
          font-weight: 100;
          letter-spacing: .1em;
      }

      /* Light mode default */
      :root {
        color: black;
      }

      /* Dark mode override */
      @media (prefers-color-scheme: dark) {
        :root {
          color: white;
        }
      }
    </style>"""+f'<div style="text-align:center">{svg}</div>'
