import random
import json
from pathlib import Path

class HangmanGame:
    """Manages a game of Hangman."""
    
    HANGMAN_STAGES = [
        # Initial empty state
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        # Head
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        # Head and torso
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        # Head, torso, and one arm
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        # Head, torso, and both arms
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ==========""",
        # Head, torso, both arms, and one leg
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ==========""",
        # Full body (game over)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ==========""",
    ]
    
    def __init__(self, words_file='hangman_words.json'):
        self.words_file = words_file
        self.words = self.load_words()
        self.reset_game()
    
    def load_words(self):
        """Load words from file or use defaults."""
        default_words = [
            "python", "programming", "computer", "algorithm", "database",
            "network", "software", "developer", "internet", "keyboard"
        ]
        
        try:
            if Path(self.words_file).exists():
                with open(self.words_file, 'r') as f:
                    return json.load(f)
            else:
                self.save_words(default_words)
                return default_words
        except Exception as e:
            print(f"Error loading words: {e}")
            return default_words
    
    def save_words(self, words):
        """Save words to file."""
        try:
            with open(self.words_file, 'w') as f:
                json.dump(words, f, indent=2)
        except Exception as e:
            print(f"Error saving words: {e}")
    
    def add_word(self, word):
        """Add a new word to the game."""
        word = word.lower().strip()
        if not word.isalpha():
            return False, "Word must contain only letters"
        
        if word in self.words:
            return False, "Word already exists"
        
        self.words.append(word)
        self.save_words(self.words)
        return True, "Word added successfully"
    
    def reset_game(self):
        """Reset the game state."""
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False
    
    def display_game_state(self):
        """Display current game state."""
        # Clear screen (print newlines)
        print("\n" * 5)
        
        # Show hangman
        print(self.HANGMAN_STAGES[self.wrong_guesses])
        
        # Show word progress
        word_display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "
        print("\nWord:", word_display)
        
        # Show guessed letters
        print("\nGuessed letters:", " ".join(sorted(self.guessed_letters)))
        print(f"Wrong guesses: {self.wrong_guesses}/6")
    
    def make_guess(self, letter):
        """Process a letter guess."""
        if self.game_over:
            return "Game is over! Start a new game."
        
        letter = letter.lower()
        if not letter.isalpha() or len(letter) != 1:
            return "Please enter a single letter."
        
        if letter in self.guessed_letters:
            return "You already guessed that letter!"
        
        self.guessed_letters.add(letter)
        
        if letter not in self.word:
            self.wrong_guesses += 1
            if self.wrong_guesses >= len(self.HANGMAN_STAGES) - 1:
                self.game_over = True
                return f"Game Over! The word was: {self.word}"
            return "Wrong guess!"
        
        # Check if word is complete
        if all(letter in self.guessed_letters for letter in self.word):
            self.game_over = True
            self.won = True
            return "Congratulations! You won!"
        
        return "Good guess!"

def print_menu():
    """Print main menu options."""
    print("\nHangman Game Menu:")
    print("1. Play Game")
    print("2. Add Word")
    print("3. View Words")
    print("4. Exit")

def play_game(game):
    """Play one game of hangman."""
    game.reset_game()
    
    print("\nWelcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You can make 6 wrong guesses before the game is over.")
    
    while not game.game_over:
        game.display_game_state()
        
        guess = input("\nEnter a letter: ").strip()
        message = game.make_guess(guess)
        print("\n" + message)
    
    game.display_game_state()
    
    if game.won:
        print("\n🎉 Congratulations! You won! 🎉")
    else:
        print("\n😔 Game Over! Better luck next time!")
        print(f"The word was: {game.word}")
    
    # Show statistics
    total_guesses = len(game.guessed_letters)
    correct_guesses = sum(1 for letter in game.guessed_letters if letter in game.word)
    accuracy = (correct_guesses / total_guesses * 100) if total_guesses > 0 else 0
    
    print("\nGame Statistics:")
    print(f"Total guesses: {total_guesses}")
    print(f"Correct guesses: {correct_guesses}")
    print(f"Wrong guesses: {game.wrong_guesses}")
    print(f"Accuracy: {accuracy:.1f}%")

def main():
    """Hangman game main program."""
    game = HangmanGame()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Play game
            play_game(game)
        
        elif choice == '2':
            # Add word
            word = input("\nEnter a word to add: ").strip()
            success, message = game.add_word(word)
            print(message)
        
        elif choice == '3':
            # View words
            print("\nAvailable words:")
            for i, word in enumerate(sorted(game.words), 1):
                print(f"{i}. {word}")
        
        elif choice == '4':
            # Exit
            print("\nThank you for playing Hangman!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
