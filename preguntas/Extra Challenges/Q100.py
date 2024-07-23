# 100. Write a Python program to implement the A* search algorithm.

import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def astar_search(start, end, grid):
    """
    Perform A* search algorithm to find the shortest path in a grid.

    Parameters:
    start (tuple): The starting position (row, col).
    end (tuple): The goal position (row, col).
    grid (list of list of int): The grid where 0 represents open cells and 1 represents obstacles.

    Returns:
    list: The path from start to end as a list of tuples, or an empty list if no path is found.
    """
    def heuristic(a, b):
        """ Calculate the Manhattan distance heuristic. """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    closed_set = set()
    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        for move in neighbors:
            neighbor_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if (0 <= neighbor_pos[0] < len(grid) and 0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0):
                
                if neighbor_pos in closed_set:
                    continue

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_pos, end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if any(neighbor_node.position == node.position and neighbor_node.g > node.g for node in open_set):
                    continue

                heapq.heappush(open_set, neighbor_node)

    return []


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar_search(start, end, grid)
if path:
    print("Path found:")
    print(path)
else:
    print("No path found")
