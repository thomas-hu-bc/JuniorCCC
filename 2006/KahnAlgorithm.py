"""
Created by Thomas Hu on 2025-09-09 at 4:49 p.m.
"""
import logging
from pathlib import Path

# We mainly take input graph as a set of edges. This function is
# mainly a utility function to convert the edges to an adjacency
# list
def construct_edges(V, edges):
    graph = {i:[] for i in range(1,V+1)}
    edge_count = {i:0 for i in range(1,V+1)}
    for u, v in edges:
        graph[u].append(v)
        edge_count[v]+=1
    return graph, edge_count


# Function to return list containing vertices in Topological order
def topologicalSort(V, edges):
    graph, edge_count = construct_edges(V, edges)
    print(f"graph: {graph} edge_count:{edge_count}")

    free_nodes = sorted([i for i in range(1,V+1) if edge_count[i] == 0], reverse=True)

    result = []
    while free_nodes:
        node = free_nodes.pop()
        result.append(node)

        for connected_node in graph[node]:
            edge_count[connected_node] -= 1
            if edge_count[connected_node] == 0:
                free_nodes.append(connected_node)
        free_nodes = sorted(free_nodes, reverse=True)
        print(f"Remove:{node}, dependent nodes: {graph[node]}, remove dependency, free q is {free_nodes} ")

    # Check for cycle
    print(f"The result is {result}")
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result


def main():
    Total = 7
    edges = [[1, 7],[1, 4], [2, 1], [3, 4], [3, 5],[6,2],[5,4]]
    result = topologicalSort(Total, edges)
    if result:
        print("Topological Order:", result)

if __name__ == "__main__":
    log_dir = Path("C:/Logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "WeChat_New_Client.txt"

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),  # log to file
            logging.StreamHandler()  # log to console
        ],
        force=True,
    )
    logging.info("Started")
    main()
    logging.info("Finished Successfully")
