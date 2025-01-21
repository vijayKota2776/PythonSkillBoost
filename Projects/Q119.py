import json
import re
from pathlib import Path

class DictionaryApp:
    """A simple dictionary application with word definitions."""
    
    def __init__(self, filename='dictionary.json'):
        self.filename = filename
        self.dictionary = {}
        self.search_history = []
        self.load_dictionary()
    
    def load_dictionary(self):
        """Load dictionary from file."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r') as f:
                    self.dictionary = json.load(f)
                print(f"Loaded {len(self.dictionary)} words")
            else:
                print("No existing dictionary file found")
                self.create_sample_dictionary()
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            self.create_sample_dictionary()
    
    def create_sample_dictionary(self):
        """Create a sample dictionary with some basic words."""
        self.dictionary = {
            "python": {
                "noun": ["A large heavy-bodied nonvenomous constrictor snake",
                        "A high-level programming language"],
                "etymology": "From Greek 'pythōn'",
                "examples": ["The python coiled around the branch",
                           "She wrote the program in Python"]
            },
            "algorithm": {
                "noun": ["A step-by-step procedure for solving a problem or accomplishing a task"],
                "etymology": "From Latin 'algorithmus'",
                "examples": ["The sorting algorithm efficiently organized the data"]
            },
            "computer": {
                "noun": ["An electronic device for storing and processing data"],
                "etymology": "From Latin 'computare' meaning 'to calculate'",
                "examples": ["She bought a new computer",
                           "The computer processed the data quickly"]
            }
        }
        self.save_dictionary()
    
    def save_dictionary(self):
        """Save dictionary to file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.dictionary, f, indent=2)
            print("Dictionary saved successfully")
        except Exception as e:
            print(f"Error saving dictionary: {e}")
    
    def add_word(self, word, definitions, etymology="", examples=None):
        """
        Add a new word to the dictionary.
        Returns: (success, message)
        """
        word = word.lower().strip()
        if not word or not definitions:
            return False, "Word and at least one definition are required"
        
        if not isinstance(definitions, list):
            definitions = [definitions]
        
        if word in self.dictionary:
            return False, "Word already exists"
        
        self.dictionary[word] = {
            "noun": definitions,
            "etymology": etymology,
            "examples": examples or []
        }
        
        self.save_dictionary()
        return True, "Word added successfully"
    
    def search_word(self, word):
        """
        Search for a word in the dictionary.
        Returns: (word_data, similar_words)
        """
        word = word.lower().strip()
        self.search_history.append(word)
        
        # Exact match
        if word in self.dictionary:
            return self.dictionary[word], []
        
        # Find similar words
        similar = []
        for dict_word in self.dictionary:
            # Check for words containing the search term
            if word in dict_word:
                similar.append(dict_word)
            # Check for words with similar spelling (simple implementation)
            elif len(word) > 3 and (
                word[:-1] in dict_word or
                word[1:] in dict_word or
                word[1:-1] in dict_word
            ):
                similar.append(dict_word)
        
        return None, similar
    
    def get_word_of_the_day(self):
        """Get a random word with its definition."""
        import random
        if not self.dictionary:
            return None
        
        word = random.choice(list(self.dictionary.keys()))
        return word, self.dictionary[word]
    
    def get_search_statistics(self):
        """Get statistics about searches."""
        if not self.search_history:
            return "No searches yet"
        
        stats = ["\nSearch Statistics:"]
        
        # Total searches
        stats.append(f"Total searches: {len(self.search_history)}")
        
        # Most searched words
        from collections import Counter
        common = Counter(self.search_history).most_common(3)
        if common:
            stats.append("\nMost searched words:")
            for word, count in common:
                stats.append(f"  {word}: {count} times")
        
        # Success rate
        found = sum(1 for word in self.search_history if word in self.dictionary)
        success_rate = (found / len(self.search_history)) * 100
        stats.append(f"\nSearch success rate: {success_rate:.1f}%")
        
        return "\n".join(stats)

def format_word_data(word, data):
    """Format word data for display."""
    output = [f"\n=== {word.upper()} ==="]
    
    # Definitions
    output.append("\nDefinitions:")
    for i, definition in enumerate(data['noun'], 1):
        output.append(f"{i}. {definition}")
    
    # Etymology
    if data['etymology']:
        output.append(f"\nEtymology: {data['etymology']}")
    
    # Examples
    if data['examples']:
        output.append("\nExamples:")
        for example in data['examples']:
            output.append(f"• {example}")
    
    return "\n".join(output)

def print_menu():
    """Print main menu options."""
    print("\nDictionary Menu:")
    print("1. Search Word")
    print("2. Add Word")
    print("3. Word of the Day")
    print("4. View Statistics")
    print("5. Exit")

def get_word_details():
    """Get word details from user."""
    word = input("\nEnter word: ").strip()
    
    definitions = []
    print("\nEnter definitions (one per line, empty line to finish):")
    while True:
        definition = input().strip()
        if not definition:
            break
        definitions.append(definition)
    
    etymology = input("\nEnter etymology (optional): ").strip()
    
    examples = []
    print("\nEnter example sentences (one per line, empty line to finish):")
    while True:
        example = input().strip()
        if not example:
            break
        examples.append(example)
    
    return word, definitions, etymology, examples

def main():
    """Dictionary app main program."""
    print("Welcome to Dictionary App!")
    app = DictionaryApp()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Search word
            word = input("\nEnter word to search: ").strip()
            data, similar = app.search_word(word)
            
            if data:
                print(format_word_data(word, data))
            else:
                print(f"\nWord '{word}' not found")
                if similar:
                    print("\nSimilar words:")
                    for w in similar:
                        print(f"- {w}")
        
        elif choice == '2':
            # Add word
            details = get_word_details()
            success, message = app.add_word(*details)
            print(f"\n{message}")
        
        elif choice == '3':
            # Word of the day
            result = app.get_word_of_the_day()
            if result:
                word, data = result
                print("\nWORD OF THE DAY")
                print(format_word_data(word, data))
            else:
                print("\nNo words in dictionary")
        
        elif choice == '4':
            # View statistics
            print(app.get_search_statistics())
        
        elif choice == '5':
            # Exit
            print("\nThank you for using Dictionary App!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
