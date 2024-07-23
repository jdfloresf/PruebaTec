# 77. Write a Python function to implement depth-first search (DFS) in a graph.

def dfs(graph, start, visited=None):
    """
    Perform depth-first search (DFS) on a graph.

    Parameters:
    graph (dict): The graph represented as an adjacency list.
    start: The starting node for the DFS.
    visited (set): Set to keep track of visited nodes (used for recursion).

    Returns:
    list: A list of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()
        
    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
print(f"DFS starting from node '{start_node}':")
visited_nodes = dfs(graph, start_node)
print(visited_nodes)
