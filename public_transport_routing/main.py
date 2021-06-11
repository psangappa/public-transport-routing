"""
Once you start, the application is ready to read the user inputs.

There are 3 types of input that the user need to provide.

1. Number of edges.
    ```prompt
    Enter the number of edges in the graph:
    ```
2. The edges.
    ```prompt
    Enter the edges in the form <source> -> <destination>: <travel time>
    ```
3. A routing query
    ```prompt
    Type route <source> -> <destination> to find out the shortest route between two stations.
    Type nearby <source>, <maximum travel time> to find out all the stations that can be reached from a given station within a given time.
    Type exit to terminate the program.
    ```

Note that you will be asked to enter the edges or the query again in case you entered a wrong command.
"""

import sys

from public_transport_routing.utils.utils import QUERY_PROMPT
from public_transport_routing.utils.utils import EDGES_PROMPT
from public_transport_routing.core.graph_manager import GraphManager


def start_app() -> None:
    number_of_edges = int(input("Enter the number of edges in the graph: "))

    graph_manager = GraphManager()

    print(EDGES_PROMPT)
    for i in range(number_of_edges):
        while not graph_manager.validate_edge(edge := input()):
            print("\033[91mWrong form.\x1b[0m ")
        graph_manager.add_edge(edge)

    graph_manager.create_graph()

    while (query := input(QUERY_PROMPT)) != "exit":
        while not graph_manager.validate_routing_query(query):
            query = input("\033[91mEntered query is wrong.\x1b[0m ")
            if query == "exit":
                sys.exit()
        print(graph_manager.process_routing_query(query))
