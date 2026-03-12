"""Dependency graph validators for composed feature execution."""

from __future__ import annotations

from feature_engine.errors import CircularDependency, InvalidAlignment, MissingDependency
from feature_engine.registry import FeatureRegistry


def build_dependency_graph(
    registry: FeatureRegistry,
    requested_features: tuple[str, ...] | list[str] | None = None,
) -> dict[str, tuple[str, ...]]:
    """Build and validate the dependency graph for requested features."""
    requested = tuple(requested_features or registry.names())
    graph: dict[str, tuple[str, ...]] = {}
    visiting: list[str] = []
    visited: set[str] = set()

    def visit(name: str) -> None:
        if name in visited:
            return
        if name in visiting:
            cycle = visiting[visiting.index(name):] + [name]
            raise CircularDependency("Circular dependency detected: " + " -> ".join(cycle))

        feature = registry.get(name)
        visiting.append(name)

        dependencies = feature.spec.depends_on
        for dep_name in dependencies:
            if dep_name not in registry:
                raise MissingDependency(f"Feature {name!r} depends on missing feature {dep_name!r}")

            dep_feature = registry.get(dep_name)
            if dep_feature.spec.timeframe != feature.spec.timeframe:
                raise InvalidAlignment(
                    f"Feature {name!r} depends on {dep_name!r} with mismatched timeframe "
                    f"{dep_feature.spec.timeframe!r} != {feature.spec.timeframe!r}"
                )
            visit(dep_name)

        visiting.pop()
        visited.add(name)
        graph[name] = dependencies

    for feature_name in requested:
        visit(feature_name)

    return graph


def topological_sort(graph: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    """Return a deterministic topological order for a validated dependency graph."""
    visited: set[str] = set()
    order: list[str] = []

    def dfs(name: str) -> None:
        if name in visited:
            return
        visited.add(name)
        for dep_name in graph.get(name, ()):  # already validated
            dfs(dep_name)
        order.append(name)

    for name in sorted(graph):
        dfs(name)

    return tuple(order)


def validate_feature_graph(
    registry: FeatureRegistry,
    requested_features: tuple[str, ...] | list[str] | None = None,
) -> dict[str, tuple[str, ...]]:
    """Validate the requested feature graph and return its adjacency map."""
    return build_dependency_graph(registry, requested_features)