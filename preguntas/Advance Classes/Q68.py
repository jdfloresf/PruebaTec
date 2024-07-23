# 68. Write a Python class to represent a tic-tac-toe game and 
# implement methods to play the game.

class TicTacToe:
    def __init__(self):
        """Initialize the Tic-Tac-Toe board."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        """Print the current state of the board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_valid_move(self, row, col):
        """Check if a move is valid (i.e., the cell is empty and within bounds)."""
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col):
        """Make a move for the current player at the specified position."""
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                print(f"Player {self.current_player} wins!")
                return True
            elif self.check_draw():
                print("The game is a draw!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
        return False

    def check_winner(self, row, col):
        """Check if the current player has won the game."""
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Check diagonals
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        """Check if the game is a draw (i.e., no empty cells left)."""
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))


game = TicTacToe()
game.print_board()
while True:
    row = int(input(f"Player {game.current_player}, enter row (0-2): "))
    col = int(input(f"Player {game.current_player}, enter col (0-2): "))
    if game.make_move(row, col):
        game.print_board()
        break
    game.print_board()
