# 96. Write a Python program to find the number of islands in a binary matrix.

def num_islands(matrix):
    """
    Find the number of islands in a binary matrix.

    Parameters:
    matrix (list of list of int): The binary matrix where 1 represents land and 0 represents water.

    Returns:
    int: The number of islands.
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    num_islands = 0

    def dfs(r, c):
        """ Perform depth-first search to mark all cells in the current island. """
        if (r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] == 0):
            return
        # Mark the cell as visited by setting it to 0
        matrix[r][c] = 0
        # Visit all 4 adjacent cells
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                # Found an island, perform DFS
                dfs(r, c)
                num_islands += 1
    
    return num_islands


matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

num = num_islands(matrix)
print(f"Number of islands: {num}")
