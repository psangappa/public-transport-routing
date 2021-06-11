edge_regex = r"([a-zA-Z0-9]{1,})\s->\s([a-zA-Z0-9]{1,}):\s([0-9]{1,})"
route_query_regex = r"(route)\s([a-zA-Z0-9]{1,})\s->\s([a-zA-Z0-9]{1,})"
nearby_query_regex = r"(nearby)\s([a-zA-Z0-9]{1,}),\s([0-9]{1,})"

EDGES_PROMPT = "Enter the edges in the form \033[92m<source> -> <destination>: <travel time>\x1b[0m"

QUERY_PROMPT = """
Type \033[92mroute <source> -> <destination>\x1b[0m to find out the shortest route between two stations.
Type \033[92mnearby <source>, <maximum travel time>\x1b[0m to find out all the stations that can be reached from a given station within a given time.
Type \033[92mexit\x1b[0m to terminate the program.
"""