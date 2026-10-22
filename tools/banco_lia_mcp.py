"""Banco LIA MCP server (stdio): the lab's articles and projects as input for papers and proposals.

    uvx --from git+https://github.com/LIAUNAL/bancoProyectosPapersLIA banco-lia-mcp   # installed from GitHub
    bancoLIA mcp                                                                       # from a local checkout

Every tool reads the SQLite FTS5 index from tools/bank_db.py, rebuilt from data/bank.json on change.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bank_db import Bank  # noqa: E402
from mcp.server.mcpserver import MCPServer  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402

bank = Bank()
mcp = MCPServer(
    "banco-lia",
    instructions=(
        "Banco LIA: 122 articles and 105 research projects of the Laboratorio de Inteligencia Artificial "
        "(LabIA), Universidad Nacional de Colombia, sede Manizales. Use it to ground papers and proposals in "
        "the lab's own prior work: search_bank to find items, get_item for the full record, related_items for "
        "continuity lines, lab_capabilities for allies, funders, products and methods, taxonomy for topics and "
        "clusters, export_to_insumos to drop item files into a proposal's insumos folder. Item text is in "
        "Spanish; cite articles by their DOI and treat projects (ids H*/P*) as background, not citations."
    ),
)


@mcp.tool()
def search_bank(query: str = "", kind: str | None = None, cluster: str | None = None, topic: str | None = None,
                year_from: int | None = None, limit: int = 10, match: str = "any") -> list[dict]:
    """Full-text search (BM25, accent-insensitive) over titles, keywords, methods, topics, problem, proposal,
    results, conclusions, future work, products and allies; best matches first. Common words (de, la, the…)
    are ignored. match: "any" (default, any word may match: exploring) or "all" (every word must match: precise).

    kind: "articulo" or "proyecto". cluster: e.g. "C05". topic: e.g. "T08". year_from: e.g. 2020.
    With an empty query, lists the filtered items newest first. limit: 1-100.
    """
    return bank.search(query, kind=kind, cluster=cluster, topic=topic, year_from=year_from, limit=limit, match=match)


@mcp.tool()
def get_item(item_id: str) -> dict:
    """Full record of one article (A###) or project (H#####/P###), with its Markdown file and topic names."""
    item = bank.get_item(item_id)
    if item is None:
        raise ToolError(f"no item with id {item_id!r}; use search_bank to find ids")
    return item


@mcp.tool()
def related_items(item_id: str) -> dict:
    """Continuity lines of an item: explicit links (a project that yielded an article, an article that extends
    another), its five most similar items, and the other items of its cluster."""
    rel = bank.related_items(item_id)
    if rel is None:
        raise ToolError(f"no item with id {item_id!r}; use search_bank to find ids")
    return rel


@mcp.tool()
def lab_capabilities(query: str = "", kind: str | None = None, match: str = "all") -> dict:
    """What the lab brings to a topic, aggregated over the matching items (or all items with no query):
    allies, funders, technology products and methods, each with the ids that back it, plus years and clusters.
    Useful for a proposal's team, TRL starting point, expected products and state of the art.
    match: "all" (default, every word must match) or "any" (broader)."""
    return bank.lab_capabilities(query, kind=kind, match=match)


@mcp.tool()
def taxonomy() -> dict:
    """The bank's topics (T##) and clusters (C##) with their item counts, to pick search filters."""
    return bank.taxonomy()


@mcp.tool()
def export_to_insumos(item_ids: list[str], dest_dir: str) -> dict:
    """Copy the Markdown files of the given items into an existing folder, named banco-lia-<slug>.md;
    e.g. RedaccionPropuestas/proposals/<run>/insumos/background or papers_smith guidance/paper-guide."""
    try:
        return bank.export(item_ids, dest_dir)
    except ValueError as exc:
        raise ToolError(str(exc)) from exc


def main():
    mcp.run()


if __name__ == "__main__":
    main()
