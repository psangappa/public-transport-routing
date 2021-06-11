"""
A Node object hold data.
List of node objects in the  `Graph` class whose indices correspond to their
row (column) number in the adjacency matrix.
"""

from __future__ import annotations

from typing import List
from typing import Tuple
from typing import Union


class Node:
    def __init__(self, name: str, index: int = None) -> None:
        self.name = name
        self.index = index

    def __repr__(self) -> str:
        return self.name


class Graph:
    def __init__(self) -> None:
        self.adjacency_matrix: List[List[int]] = []
        self.nodes: List[Node] = []

    @classmethod
    def create_from_nodes(cls, nodes: List[Node]) -> Graph:
        """
        A utility method to generate the graph from the node list.
        """
        graph = cls()
        for node in nodes:
            graph.add_node(node)
        return graph

    def connect(self, source_node: Node, destination_node: Node, travel_time: int) -> None:
        """
        Connect both the node.
        """
        self.adjacency_matrix[source_node.index][destination_node.index] = travel_time

    def connections_from(
        self, source_name: Union[Node, int]
    ) -> List[Tuple[Node, int]]:
        """
        Get all other nodes and their distances from `source_name`.
        """
        source_name = self.get_index_from_node(source_name)
        return [
            (self.nodes[col_num], self.adjacency_matrix[source_name][col_num])
            for col_num in range(len(self.adjacency_matrix[source_name]))
            if self.adjacency_matrix[source_name][col_num] != 0
        ]

    def add_node(self, node: Node) -> None:
        """
        Add the node to the graph and adjust the matrix.
        """
        self.nodes.append(node)
        node.index = len(self.nodes) - 1
        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0] * (len(self.adjacency_matrix) + 1))

    @staticmethod
    def get_index_from_node(node: Union[Node, int]):
        """
        Allows either node OR node indices to be passed into.
        """
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(
        self, source_node: Union[Node, int], destination_node: Union[Node, int] = None
    ) -> List[List[Union[int, List]]]:
        """
        Set `provisional_time` of all nodes from the source node to infinity.

        Define an empty set of `seen_nodes`. This set will ensure we don't
        re-evaluate a node which already has the shortest path set, and that
        we don’t evaluate paths through a node which has a shorter path to the
        source than the current path.

        Set `provisional_time` of the source node to equal 0, and the array
        representing the hops taken to just include the source node itself.
        (This will be useful later as we track which path through the graph
        we take to get the calculated minimum distance).

        `ITERATIVE PROCEDURE`

        While we have not seen all nodes or, in the case of source to single
        destination node evaluation, while we have not seen the destination node.

        Set current_node to the node with the smallest `provisional_time` in the
        entire graph. Note that for the first iteration, this will be the
        `source_node` because we set its `provisional_time` to 0.

        Add `current_node` to the seen_nodes set.

        Update the `provisional_time` of each of `current_node's` neighbors to
        be the time from `current_node` to `source_node` plus the edge length
        from `current_node` to that neighbor IF that value is less than the
        neighbor’s current provisional_time.
        If this neighbor has never had a provisional distance set, remember
        that it is initialized to infinity and thus must be larger than this
        sum. If we update `provisional_time`, also update the hops we took to
        get this distance by concatenating `current_node's` hops to the source
        node with current_node itself.
        """
        source_node_index = self.get_index_from_node(source_node)

        provisional_time: List = [None] * len(self.nodes)
        for i in range(len(provisional_time)):
            provisional_time[i] = [float("inf"), [self.nodes[source_node_index]]]

        provisional_time[source_node_index][0] = 0

        queue = [i for i in range(len(self.nodes))]
        seen_nodes = set()
        while len(queue) > 0:
            min_time = float("inf")
            current_node = None
            for n in queue:
                if provisional_time[n][0] < min_time and n not in seen_nodes:
                    min_time = provisional_time[n][0]
                    current_node = n
            if (
                destination_node and destination_node.index == current_node
            ) or current_node is None:
                break

            queue.remove(current_node)
            seen_nodes.add(current_node)

            connections = self.connections_from(current_node)

            for (node, travel_time) in connections:
                total_time = travel_time + min_time
                if total_time < provisional_time[node.index][0]:
                    provisional_time[node.index][0] = total_time
                    provisional_time[node.index][1] = list(
                        provisional_time[current_node][1]
                    )
                    provisional_time[node.index][1].append(node)
        return provisional_time
