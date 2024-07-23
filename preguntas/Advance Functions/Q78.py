# 78. Write a Python function to implement breadth-first search (BFS) in a graph.

from collections import deque

def bfs(graph, start):
    """
    Perform breadth-first search (BFS) on a graph.

    Parameters:
    graph (dict): The graph represented as an adjacency list.
    start: The starting node for the BFS.

    Returns:
    list: A list of nodes in the order they were visited.
    """
    visited = set()         # Set to keep track of visited nodes
    queue = deque([start])  # Queue to manage the BFS exploration
    result = []             # List to store the order of visited nodes

    while queue:
        node = queue.popleft()   # Get the next node from the queue
        if node not in visited:
            visited.add(node)   # Mark the node as visited
            result.append(node) # Add the node to the result list
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
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
print(f"BFS starting from node '{start_node}':")
visited_nodes = bfs(graph, start_node)
print(visited_nodes)
