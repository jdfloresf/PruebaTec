# 94. Write a Python program to find the shortest path in a matrix from the 
# top-left corner to the bottom-right corner.


from collections import deque

def shortest_path_in_matrix(matrix):
    """
    Find the shortest path from the top-left corner to the bottom-right corner in a matrix.
    Assumes that movement is allowed in four directions: up, down, left, right.

    Parameters:
    matrix (list of list of int): The matrix where 0 represents open cells and 1 represents obstacles.

    Returns:
    list of tuple: The shortest path from the top-left corner to the bottom-right corner.
    """
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Direction vectors for moving in 4 directions (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS initialization
    queue = deque([(0, 0)])  # Start with the top-left corner
    visited = set()
    visited.add((0, 0))
    predecessor = { (0, 0): None }
    
    while queue:
        r, c = queue.popleft()
        
        # Check if we have reached the bottom-right corner
        if (r, c) == (rows - 1, cols - 1):
            path = []
            while (r, c) is not None:
                path.append((r, c))
                (r, c) = predecessor.get((r, c), (None, None))
            return path[::-1]  # Reverse the path to get the correct order
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                matrix[nr][nc] == 0 and 
                (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append((nr, nc))
                predecessor[(nr, nc)] = (r, c)
    
    return []  # Return empty if there's no path

# Ejemplo de uso
if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    
    path = shortest_path_in_matrix(matrix)
    print("Shortest path from top-left to bottom-right corner:")
    print(path)
