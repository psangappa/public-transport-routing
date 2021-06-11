"""
Graph manager that manages creation of graph and validating user inputs.
"""

import re
from typing import List

from public_transport_routing.utils.utils import edge_regex
from public_transport_routing.utils.utils import route_query_regex
from public_transport_routing.utils.utils import nearby_query_regex
from public_transport_routing.core.graph import Node
from public_transport_routing.core.graph import Graph


class GraphManager:
    def __init__(self):
        self.edges: List[str] = []
        self.graph = Graph()
        self.vertices = dict()

    def add_edge(self, edge: str) -> None:
        self.edges.append(edge)

    @staticmethod
    def validate_edge(edge: str) -> bool:
        """
        Validate again `edge` form.
        """
        return bool(re.match(edge_regex, edge))

    @staticmethod
    def validate_routing_query(query: str) -> bool:
        """
        Validate again `route` and `nearby` query forms.
        """
        return bool(re.match(route_query_regex, query)) or bool(
            re.match(nearby_query_regex, query)
        )

    def create_graph(self):
        """
        Create graph from user inputs.
        """
        for edge in self.edges:
            source, destination, travel_time = re.match(edge_regex, edge).groups()
            if source not in self.vertices:
                source_node = Node(source)
                self.vertices.update({source: source_node})
                self.graph.add_node(source_node)
            else:
                source_node = self.vertices[source]
            if destination not in self.vertices:
                destination_node = Node(destination)
                self.vertices.update({destination: destination_node})
                self.graph.add_node(destination_node)
            else:
                destination_node = self.vertices[destination]
            self.graph.connect(source_node, destination_node, int(travel_time))

    def process_routing_query(self, query: str) -> str:
        """
        Decide the query type and act accordingly.
        """
        if query.startswith("route"):
            _, source, destination = re.match(route_query_regex, query).groups()
            try:
                source = self.vertices[source]
                destination = self.vertices[destination]
                return self.find_route(source, destination)
            except KeyError:
                return f"\033[91mError: No route from {source} to {destination}\x1b[0m"
        _, source, maximum_travel_time = re.match(nearby_query_regex, query).groups()
        try:
            source = self.vertices[source]
            return self.find_nearby(source, int(maximum_travel_time))
        except KeyError:
            return f"\033[91mError: No nearby stations from {source} with the travel time of {maximum_travel_time}\x1b[0m"

    def find_route(self, source: Node, destination: Node) -> str:
        """
        Find route and travel time between source and destination.
        """
        distance = self.graph.dijkstra(source, destination)[destination.index]
        route = [node.name for node in distance[1]]
        return (
            f"\033[91mError: No route from {source.name} to {destination.name}\x1b[0m"
            if len(route) == 1
            else f"{' -> '.join(route)}: {distance[0]}"
        )

    def find_nearby(self, source: Node, maximum_travel_time: int) -> str:
        """
        Find nearby stations that are within `maximum_travel_time` away from
        source.
        """
        distances = self.graph.dijkstra(source)
        nearby_route = [
            f"{str(distance[1][-1])}: {distance[0]}"
            for distance in sorted(distances, key=lambda x: x[0])
            if maximum_travel_time >= distance[0] > 0
        ]
        return (
            ", ".join(nearby_route)
            if nearby_route
            else f"\033[91mError: No nearby stations from {source.name} with the travel time of {maximum_travel_time}\x1b[0m"
        )
