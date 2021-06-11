def test_validate_edge(graph_manager):
    assert graph_manager.validate_edge("A -> B: 10")
    assert not graph_manager.validate_edge("A -> B: nonInt")


def test_validate_routing_query(graph_manager):
    assert graph_manager.validate_routing_query("route A -> B")
    assert not graph_manager.validate_routing_query("route A ->B")
    assert not graph_manager.validate_routing_query("rout A -> B")

    assert graph_manager.validate_routing_query("nearby A, 130")
    assert not graph_manager.validate_routing_query("nearby A, B")
    assert not graph_manager.validate_routing_query("near A, 130")


def test_create_graph(graph_manager_extended):

    # connection from None A to all other node
    connections = graph_manager_extended.graph.connections_from(0)
    assert [(connection[0].name, connection[1]) for connection in connections] == [
        ("B", 240),
        ("C", 70),
        ("D", 120),
    ]

    # connection from None E to all other node
    connections = graph_manager_extended.graph.connections_from(4)
    assert [(connection[0].name, connection[1]) for connection in
            connections] == [
               ("A", 300),
           ]


def test_process_routing_query(graph_manager_extended):
    route = graph_manager_extended.process_routing_query("route A -> B")
    assert route == "A -> C -> B: 130"

    nearby = graph_manager_extended.process_routing_query("nearby A, 130")
    assert nearby == "C: 70, D: 120, B: 130"


def test_process_routing_query_error(minimal_graph_manager):

    route = minimal_graph_manager.process_routing_query("route A -> E")
    # String `\x1b[91m` and `\x1b[0m` represent red color on the console.
    assert route.strip("\x1b[91m").strip("\x1b[0m") == "Error: No route from A to E"

    route = minimal_graph_manager.process_routing_query("route Nowhere -> Norway")
    assert route.strip("\x1b[91m").strip("\x1b[0m") == "Error: No route from Nowhere to Norway"

    nearby = minimal_graph_manager.process_routing_query("nearby A, 55")
    assert nearby.strip("\x1b[91m").strip("\x1b[0m") == "Error: No nearby stations from A with the travel time of 55"
