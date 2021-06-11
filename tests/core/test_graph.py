def test_dijkstra_shortest_path_from_source(graph):
    # Index 0 is Node A
    shortest_path = graph.dijkstra(0)
    paths = []
    for path in shortest_path:
        nodes = [node.name for node in path[1]]
        paths.append([path[0], nodes])

    assert paths == [
        [0, ["A"]],
        [130, ["A", "C", "B"]],
        [70, ["A", "C"]],
        [120, ["A", "D"]],
        [310, ["A", "C", "E"]],
    ]
