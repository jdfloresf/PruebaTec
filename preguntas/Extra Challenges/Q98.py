# 98. Write a Python program to solve the Sudoku puzzle.

def is_valid(board, row, col, num):
    """
    Check if it's valid to place `num` in `board[row][col]`.

    Parameters:
    board (list of list of int): The Sudoku board.
    row (int): The row index.
    col (int): The column index.
    num (int): The number to place.

    Returns:
    bool: True if it's valid to place the number, False otherwise.
    """
    # Check if the number is not repeated in the row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check if the number is not repeated in the column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check if the number is not repeated in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.

    Parameters:
    board (list of list of int): The Sudoku board where 0 represents empty cells.

    Returns:
    bool: True if the puzzle is solved, False otherwise.
    """
    empty = find_empty_location(board)
    if not empty:
        return True  # No empty cell found, puzzle is solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack

    return False

def find_empty_location(board):
    """
    Find an empty cell in the Sudoku board.

    Parameters:
    board (list of list of int): The Sudoku board.

    Returns:
    tuple: The row and column of an empty cell, or None if no empty cell is found.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def print_board(board):
    """
    Print the Sudoku board.

    Parameters:
    board (list of list of int): The Sudoku board.
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if solve_sudoku(sudoku_board):
    print("Sudoku puzzle solved:")
    print_board(sudoku_board)
else:
    print("No solution exists")