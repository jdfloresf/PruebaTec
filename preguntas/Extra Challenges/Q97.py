# 97. Write a Python program to solve the N-queens problem.

def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all possible solutions.

    Parameters:
    n (int): The number of queens and the size of the board (n x n).

    Returns:
    list of list of str: List of solutions where each solution is represented as a list of strings.
    """
    def is_safe(board, row, col):
        """ Check if it's safe to place a queen at board[row][col]. """
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col):
        """ Use backtracking to solve the N-Queens problem. """
        if col >= n:
            result.append([''.join(row) for row in board])
            return
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve(board, col + 1)
                board[i][col] = '.'  # Backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return result


n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()
