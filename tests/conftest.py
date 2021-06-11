import pytest

from public_transport_routing.core.graph_manager import GraphManager
from public_transport_routing.core.graph import Graph, Node


@pytest.fixture
def graph_manager():
    return GraphManager()


@pytest.fixture
def graph_manager_extended(graph_manager):
    graph_manager.add_edge("A -> B: 240")
    graph_manager.add_edge("A -> C: 70")
    graph_manager.add_edge("A -> D: 120")
    graph_manager.add_edge("C -> B: 60")
    graph_manager.add_edge("D -> E: 480")
    graph_manager.add_edge("C -> E: 240")
    graph_manager.add_edge("B -> E: 210")
    graph_manager.add_edge("E -> A: 300")

    graph_manager.create_graph()
    return graph_manager


@pytest.fixture
def minimal_graph_manager(graph_manager):
    graph_manager.add_edge("A -> B: 240")
    graph_manager.add_edge("A -> C: 70")
    graph_manager.add_edge("D -> E: 480")

    graph_manager.create_graph()
    return graph_manager


@pytest.fixture
def graph():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    graph = Graph.create_from_nodes([a, b, c, d, e])
    graph.connect(a, b, 240)
    graph.connect(a, c, 70)
    graph.connect(a, d, 120)
    graph.connect(c, b, 60)
    graph.connect(d, e, 480)
    graph.connect(c, e, 240)
    graph.connect(b, e, 210)
    graph.connect(e, a, 300)

    return graph
