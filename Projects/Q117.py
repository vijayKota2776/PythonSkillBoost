import random
import time

class RockPaperScissors:
    """Manages a game of Rock Paper Scissors."""
    
    MOVES = ['rock', 'paper', 'scissors']
    
    # Rules: key beats value
    RULES = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    # ASCII art for moves
    ART = {
        'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        'paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
        'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    }
    
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.player_moves = []
        self.computer_moves = []
    
    def get_computer_move(self):
        """Get computer's move based on strategy."""
        # Simple strategy: If player has made moves, try to counter their most common move
        if self.player_moves:
            most_common = max(set(self.player_moves), key=self.player_moves.count)
            counter_move = self.RULES.keys()[self.RULES.values().index(most_common)]
            if random.random() < 0.7:  # 70% chance to use strategy
                return counter_move
        
        return random.choice(self.MOVES)
    
    def play_round(self, player_move):
        """
        Play one round of the game.
        Returns: (result, message)
        """
        player_move = player_move.lower()
        if player_move not in self.MOVES:
            return None, "Invalid move! Choose rock, paper, or scissors."
        
        computer_move = self.get_computer_move()
        self.rounds_played += 1
        self.player_moves.append(player_move)
        self.computer_moves.append(computer_move)
        
        # Display moves with animation
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoot!\n")
        
        print("Your move:")
        print(self.ART[player_move])
        print("\nComputer's move:")
        print(self.ART[computer_move])
        
        # Determine winner
        if player_move == computer_move:
            return 'tie', "It's a tie!"
        
        if self.RULES[player_move] == computer_move:
            self.player_score += 1
            return 'win', f"{player_move.capitalize()} beats {computer_move}. You win!"
        
        self.computer_score += 1
        return 'lose', f"{computer_move.capitalize()} beats {player_move}. Computer wins!"
    
    def get_stats(self):
        """Get current game statistics."""
        stats = [
            f"\nGame Statistics:",
            f"Rounds played: {self.rounds_played}",
            f"Your score: {self.player_score}",
            f"Computer score: {self.computer_score}"
        ]
        
        if self.rounds_played > 0:
            win_rate = (self.player_score / self.rounds_played) * 100
            stats.append(f"Your win rate: {win_rate:.1f}%")
            
            # Most used moves
            if self.player_moves:
                player_favorite = max(set(self.player_moves), 
                                   key=self.player_moves.count)
                stats.append(f"Your most used move: {player_favorite}")
            
            if self.computer_moves:
                computer_favorite = max(set(self.computer_moves), 
                                     key=self.computer_moves.count)
                stats.append(f"Computer's most used move: {computer_favorite}")
        
        return "\n".join(stats)
    
    def analyze_game(self):
        """Analyze the game and provide tips."""
        if self.rounds_played < 3:
            return "Play more rounds to get game analysis!"
        
        analysis = ["\nGame Analysis:"]
        
        # Check for patterns in player moves
        pairs = list(zip(self.player_moves[:-1], self.player_moves[1:]))
        if len(pairs) >= 2:
            for move in self.MOVES:
                count = sum(1 for a, b in pairs if a == move)
                if count >= 2:
                    analysis.append(
                        f"Tip: You often use {move} consecutively. "
                        "Try mixing up your moves more!")
        
        # Check win/loss patterns
        if self.player_score < self.computer_score:
            analysis.append(
                "Tip: Try to predict the computer's moves based on your previous moves!")
        elif self.player_score > self.computer_score:
            analysis.append("Great job! You're beating the computer!")
        
        return "\n".join(analysis)

def print_rules():
    """Print game rules."""
    print("\nRock Paper Scissors Rules:")
    print("1. Rock crushes Scissors")
    print("2. Scissors cuts Paper")
    print("3. Paper covers Rock")
    print("\nFirst to win the chosen number of rounds wins the game!")

def print_menu():
    """Print main menu options."""
    print("\nRock Paper Scissors Menu:")
    print("1. Play Game")
    print("2. View Rules")
    print("3. View Statistics")
    print("4. Exit")

def play_game():
    """Play a full game of Rock Paper Scissors."""
    game = RockPaperScissors()
    
    try:
        target_score = int(input("\nHow many wins to end the game? "))
        if target_score <= 0:
            print("Please enter a positive number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return
    
    print("\nGame started! Enter your move (rock/paper/scissors)")
    print("Enter 'quit' to end the game early")
    
    while (game.player_score < target_score and 
           game.computer_score < target_score):
        move = input("\nYour move: ").strip().lower()
        
        if move == 'quit':
            break
        
        result, message = game.play_round(move)
        if result is None:
            print(message)
            continue
        
        print(message)
        print(f"\nScore - You: {game.player_score} Computer: {game.computer_score}")
    
    # Game over
    print("\nGame Over!")
    if game.player_score > game.computer_score:
        print("Congratulations! You won the game!")
    elif game.player_score < game.computer_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")
    
    print(game.get_stats())
    print(game.analyze_game())

def main():
    """Rock Paper Scissors main program."""
    print("Welcome to Rock Paper Scissors!")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Play game
            play_game()
        
        elif choice == '2':
            # View rules
            print_rules()
        
        elif choice == '3':
            # View statistics
            game = RockPaperScissors()
            print(game.get_stats())
        
        elif choice == '4':
            # Exit
            print("\nThanks for playing Rock Paper Scissors!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
