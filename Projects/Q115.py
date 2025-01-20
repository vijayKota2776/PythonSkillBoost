class TicTacToe:
    """Manages a game of Tic-Tac-Toe."""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves = 0
    
    def make_move(self, row, col):
        """
        Make a move on the board.
        Returns: (success, message)
        """
        if self.game_over:
            return False, "Game is already over!"
        
        if not (0 <= row < 3 and 0 <= col < 3):
            return False, "Invalid position!"
        
        if self.board[row][col] != ' ':
            return False, "Position already taken!"
        
        # Make the move
        self.board[row][col] = self.current_player
        self.moves += 1
        
        # Check for win or draw
        if self.check_winner(row, col):
            self.game_over = True
            self.winner = self.current_player
            return True, f"Player {self.current_player} wins!"
        
        if self.moves == 9:
            self.game_over = True
            return True, "It's a draw!"
        
        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True, f"Player {self.current_player}'s turn"
    
    def check_winner(self, row, col):
        """Check if the last move created a winning condition."""
        player = self.board[row][col]
        
        # Check row
        if all(self.board[row][j] == player for j in range(3)):
            return True
        
        # Check column
        if all(self.board[i][col] == player for i in range(3)):
            return True
        
        # Check diagonals
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def display_board(self):
        """Display the current board state."""
        print("\n")
        print("     0   1   2")
        print("   +---+---+---+")
        for i in range(3):
            print(f" {i} | {' | '.join(self.board[i])} |")
            print("   +---+---+---+")
    
    def get_board_state(self):
        """Get a string representation of the board state."""
        lines = []
        for row in self.board:
            lines.append('|'.join(row))
        return '\n-+-+-\n'.join(lines)
    
    def analyze_game(self):
        """Analyze the current game state."""
        if not self.game_over:
            return "Game is still in progress"
        
        analysis = []
        
        if self.winner:
            analysis.append(f"Winner: Player {self.winner}")
        else:
            analysis.append("Result: Draw")
        
        analysis.append(f"Total moves: {self.moves}")
        
        # Count moves by each player
        x_moves = sum(row.count('X') for row in self.board)
        o_moves = sum(row.count('O') for row in self.board)
        analysis.append(f"Player X moves: {x_moves}")
        analysis.append(f"Player O moves: {o_moves}")
        
        return "\n".join(analysis)

def print_instructions():
    """Print game instructions."""
    print("\nTic-Tac-Toe Instructions:")
    print("1. The game is played on a 3x3 grid")
    print("2. Players take turns placing X's and O's")
    print("3. First player to get 3 in a row wins")
    print("4. Enter moves as row and column numbers (0-2)")
    print("   For example: '1 2' for row 1, column 2")
    print("\nBoard positions:")
    print("     0   1   2")
    print("   +---+---+---+")
    print(" 0 |   |   |   |")
    print("   +---+---+---+")
    print(" 1 |   |   |   |")
    print("   +---+---+---+")
    print(" 2 |   |   |   |")
    print("   +---+---+---+")

def get_move():
    """Get move from user."""
    while True:
        try:
            move = input(f"\nEnter move (row col): ").strip()
            if move.lower() == 'q':
                return None
            
            row, col = map(int, move.split())
            return row, col
        
        except (ValueError, IndexError):
            print("Invalid input! Use format: row col (0-2)")

def print_menu():
    """Print main menu options."""
    print("\nTic-Tac-Toe Menu:")
    print("1. New Game")
    print("2. View Instructions")
    print("3. Exit")

def play_game():
    """Play one game of Tic-Tac-Toe."""
    game = TicTacToe()
    print("\nStarting new game!")
    print("Enter 'q' to quit the game")
    
    while not game.game_over:
        game.display_board()
        print(f"\nPlayer {game.current_player}'s turn")
        
        move = get_move()
        if move is None:
            print("\nGame aborted!")
            return
        
        success, message = game.make_move(*move)
        print(message)
    
    # Show final board and analysis
    game.display_board()
    print("\nGame Over!")
    print(game.analyze_game())

def main():
    """Tic-Tac-Toe main program."""
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # New game
            play_game()
        
        elif choice == '2':
            # View instructions
            print_instructions()
        
        elif choice == '3':
            # Exit
            print("\nThank you for playing Tic-Tac-Toe!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
