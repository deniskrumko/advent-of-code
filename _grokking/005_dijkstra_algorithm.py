from dataclasses import (
    dataclass,
    field,
)

import pytest


@dataclass
class Vertex:
    name: str
    edges: list = field(default_factory=list)

    def add_edge(self, vertex, cost):
        new_edge = Edge(src=self, dest=vertex, cost=cost)
        self.edges.append(new_edge)
        return new_edge

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self):
        return f'<Vertex: {self.name}>'


@dataclass
class Edge:
    src: Vertex
    dest: Vertex
    cost: int


def dijkstra_algorithm(start: Vertex, end: Vertex, vertexes: list[Vertex]) -> int:
    """Dijkstra algorithm with only best cost."""
    # Start element shouldn't be checked
    unchecked = set(vertexes)
    unchecked.remove(start)

    # Build initial cost table
    costs_table = {v: float('+inf') for v in unchecked}
    for edge in start.edges:
        costs_table[edge.dest] = edge.cost

    while unchecked:
        # Find vertex with smallest cost
        smallest_cost_vertex = min(unchecked, key=lambda x: costs_table[x])

        # Mark it as checked
        unchecked.remove(smallest_cost_vertex)

        # Update costs for edges
        for edge in smallest_cost_vertex.edges:
            new_cost = costs_table[smallest_cost_vertex] + edge.cost
            if new_cost < costs_table[edge.dest]:
                costs_table[edge.dest] = new_cost

    return costs_table[end]


def dijkstra_algorithm_with_path(
    start: Vertex,
    end: Vertex,
    vertexes: list[Vertex],
) -> tuple[str, int]:
    """Dijkstra algorithm with both best path and best cost."""
    # Start element shouldn't be checked
    unchecked = set(vertexes)
    unchecked.remove(start)

    # Build initial costs table
    costs_table = {v: float('+inf') for v in unchecked}
    for edge in start.edges:
        costs_table[edge.dest] = edge.cost

    # Parents table
    parents_table = {v: None for v in unchecked}
    for edge in start.edges:
        parents_table[edge.dest] = start

    while unchecked:
        # Find vertex with smallest cost
        smallest_cost_vertex = min(unchecked, key=lambda x: costs_table[x])

        # Mark it as checked
        unchecked.remove(smallest_cost_vertex)

        # Update costs for edges
        for edge in smallest_cost_vertex.edges:
            new_cost = costs_table[smallest_cost_vertex] + edge.cost
            if new_cost < costs_table[edge.dest]:
                costs_table[edge.dest] = new_cost

                # Update parent only in case if cost is smalled!
                parents_table[edge.dest] = smallest_cost_vertex

    # Build full path
    backwards_path = []
    current = end
    while current is not None:  # start has no parent
        backwards_path.append(current)
        current = parents_table.get(current)

    path_str = ' -> '.join(v.name for v in reversed(backwards_path))
    return path_str, costs_table[end]


def bellman_ford_algorithm(
    start: Vertex,
    vertexes: list[Vertex],
    edges: list[Edge],
):
    dist_table = {v: float('+inf') for v in vertexes}
    dist_table[start] = 0

    for _ in range(len(vertexes) - 1):
        for edge in edges:
            u, v = edge.src, edge.dest
            if dist_table[v] > dist_table[u] + edge.cost:
                dist_table[v] = dist_table[u] + edge.cost

    for edge in edges:
        u, v = edge.src, edge.dest
        if dist_table[v] > dist_table[u] + edge.cost:
            raise ValueError('Negative cycle detected')

    return dist_table


# TESTS
# =============================================================================================

def test_dijkstra_algorithm():
    """Test search for best path using Dijkstra Algorithm."""
    # 6 vertexes
    book = Vertex(name='book')
    record = Vertex(name='record')
    poster = Vertex(name='poster')
    drums = Vertex(name='drums')
    bass = Vertex(name='bass')
    piano = Vertex(name='piano')

    # Intentionally unsorted
    vertexes = [piano, bass, drums, poster, book, record]

    # 8 edges
    book.add_edge(record, 5)
    book.add_edge(poster, 0)
    record.add_edge(bass, 15)
    record.add_edge(drums, 20)
    poster.add_edge(bass, 30)
    poster.add_edge(drums, 35)
    drums.add_edge(piano, 10)
    bass.add_edge(piano, 20)

    assert dijkstra_algorithm(start=book, end=piano, vertexes=vertexes) == 35
    assert dijkstra_algorithm_with_path(start=book, end=piano, vertexes=vertexes) == (
        'book -> record -> drums -> piano',
        35,
    )


def test_dijkstra_algorithm_for_negative_cost():
    """Test that Dijkstra Algorithm does not work with negative cost edges."""
    # 4 vertexes
    book = Vertex(name='book')
    record = Vertex(name='record')
    poster = Vertex(name='poster')
    drums = Vertex(name='drums')
    vertexes = [book, record, poster, drums]

    # 4 edges
    book.add_edge(record, 5)
    book.add_edge(poster, 0)
    record.add_edge(poster, -7)  # <-- Negative cost edge!
    poster.add_edge(drums, 35)

    # BEST COST MUST BE 33!
    assert dijkstra_algorithm(start=book, end=drums, vertexes=vertexes) == 35


def test_bellman_ford_algorithm_for_negative_cost():
    # 4 vertexes
    book = Vertex(name='book')
    record = Vertex(name='record')
    poster = Vertex(name='poster')
    drums = Vertex(name='drums')
    vertexes = [book, record, poster, drums]

    # 4 edges
    edges = [
        book.add_edge(record, 5),
        book.add_edge(poster, 0),
        record.add_edge(poster, -7),  # <-- Negative cost edge!
        poster.add_edge(drums, 35),
    ]

    result_table = bellman_ford_algorithm(start=book, vertexes=vertexes, edges=edges)
    assert result_table[drums] == 33


@pytest.mark.parametrize('negative_cycle_cost, expected', (
    (-32, None),
    (-33, None),
    (-34, ValueError),
    (-35, ValueError),
))
def test_bellman_ford_algorithm_with_cycle(negative_cycle_cost, expected):
    # 4 vertexes
    book = Vertex(name='book')
    record = Vertex(name='record')
    poster = Vertex(name='poster')
    drums = Vertex(name='drums')
    vertexes = [book, record, poster, drums]

    # 4 edges
    edges = [
        book.add_edge(record, 5),
        book.add_edge(poster, 0),
        record.add_edge(poster, -7),  # <-- Negative cost edge!
        poster.add_edge(drums, 35),
        drums.add_edge(book, negative_cycle_cost),  # <-- Negative cycle!
    ]

    if expected is ValueError:
        with pytest.raises(ValueError, match=r'.*Negative cycle detected.*'):
            bellman_ford_algorithm(start=book, vertexes=vertexes, edges=edges)
    else:
        assert bellman_ford_algorithm(start=book, vertexes=vertexes, edges=edges)
