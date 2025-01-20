import json
import random
from pathlib import Path

class Question:
    """Represents a multiple-choice question."""
    
    def __init__(self, question, options, correct_answer, explanation=""):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.explanation = explanation
    
    def to_dict(self):
        """Convert question to dictionary."""
        return {
            'question': self.question,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'explanation': self.explanation
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create question from dictionary."""
        return cls(
            data['question'],
            data['options'],
            data['correct_answer'],
            data.get('explanation', "")
        )
    
    def display(self, number):
        """Display the question with options."""
        print(f"\nQuestion {number}:")
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
    
    def check_answer(self, answer):
        """Check if the answer is correct."""
        try:
            return self.options[int(answer)-1] == self.correct_answer
        except (ValueError, IndexError):
            return False

class QuizGame:
    """Manages a quiz game with questions and scoring."""
    
    def __init__(self, filename='quiz_questions.json'):
        self.filename = filename
        self.questions = []
        self.load_questions()
    
    def load_questions(self):
        """Load questions from file."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.questions = [Question.from_dict(q) for q in data]
                print(f"Loaded {len(self.questions)} questions")
            else:
                print("No existing questions file found")
                self.create_sample_questions()
        except Exception as e:
            print(f"Error loading questions: {e}")
            self.create_sample_questions()
    
    def create_sample_questions(self):
        """Create sample questions if no file exists."""
        sample_questions = [
            Question(
                "What is the capital of France?",
                ["London", "Berlin", "Paris", "Madrid"],
                "Paris",
                "Paris is the capital and largest city of France."
            ),
            Question(
                "Which planet is known as the Red Planet?",
                ["Venus", "Mars", "Jupiter", "Saturn"],
                "Mars",
                "Mars appears red due to iron oxide (rust) on its surface."
            ),
            Question(
                "What is the largest mammal in the world?",
                ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "Blue Whale",
                "The Blue Whale is the largest animal known to have ever existed."
            )
        ]
        self.questions = sample_questions
        self.save_questions()
    
    def save_questions(self):
        """Save questions to file."""
        try:
            data = [q.to_dict() for q in self.questions]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            print("Questions saved successfully")
        except Exception as e:
            print(f"Error saving questions: {e}")
    
    def add_question(self, question, options, correct_answer, explanation=""):
        """Add a new question."""
        if not question or len(options) < 2 or not correct_answer:
            return False, "Question and at least 2 options are required"
        
        if correct_answer not in options:
            return False, "Correct answer must be one of the options"
        
        q = Question(question, options, correct_answer, explanation)
        self.questions.append(q)
        self.save_questions()
        return True, "Question added successfully"
    
    def run_quiz(self, num_questions=None):
        """
        Run the quiz game.
        Returns: (score, total questions)
        """
        if not self.questions:
            print("No questions available!")
            return 0, 0
        
        # Select questions
        if num_questions is None or num_questions > len(self.questions):
            num_questions = len(self.questions)
        
        quiz_questions = random.sample(self.questions, num_questions)
        score = 0
        
        print(f"\nStarting Quiz! ({num_questions} questions)")
        print("=" * 40)
        
        for i, question in enumerate(quiz_questions, 1):
            # Display question
            question.display(i)
            
            # Get answer
            while True:
                answer = input("\nYour answer (1-4): ").strip()
                if answer in ['1', '2', '3', '4']:
                    break
                print("Please enter a number between 1 and 4")
            
            # Check answer
            is_correct = question.check_answer(answer)
            if is_correct:
                print("\n✓ Correct!")
                score += 1
            else:
                print("\n✗ Incorrect!")
                print(f"The correct answer is: {question.correct_answer}")
            
            if question.explanation:
                print(f"Explanation: {question.explanation}")
            
            print("\n" + "=" * 40)
        
        return score, num_questions

def print_menu():
    """Print main menu options."""
    print("\nQuiz Game Menu:")
    print("1. Start Quiz")
    print("2. Add Question")
    print("3. View All Questions")
    print("4. Exit")

def get_question_details():
    """Get question details from user."""
    print("\nEnter question details:")
    question = input("Question: ").strip()
    
    options = []
    print("\nEnter 4 options:")
    for i in range(4):
        option = input(f"Option {i+1}: ").strip()
        options.append(option)
    
    while True:
        try:
            correct = int(input("\nEnter the number of correct option (1-4): "))
            if 1 <= correct <= 4:
                correct_answer = options[correct-1]
                break
            print("Please enter a number between 1 and 4")
        except ValueError:
            print("Please enter a valid number")
    
    explanation = input("\nExplanation (optional): ").strip()
    
    return question, options, correct_answer, explanation

def main():
    """Quiz game main program."""
    print("Welcome to Quiz Game!")
    game = QuizGame()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Start quiz
            try:
                num = input("\nHow many questions? (press Enter for all): ").strip()
                num = int(num) if num else None
                if num is not None and num <= 0:
                    print("Number of questions must be positive")
                    continue
                
                score, total = game.run_quiz(num)
                print(f"\nFinal Score: {score}/{total}")
                percentage = (score / total) * 100 if total > 0 else 0
                print(f"Percentage: {percentage:.1f}%")
                
                # Performance message
                if percentage >= 90:
                    print("Excellent performance! 🌟")
                elif percentage >= 70:
                    print("Good job! 👍")
                elif percentage >= 50:
                    print("Not bad! Keep practicing! 💪")
                else:
                    print("Keep learning! You can do better! 📚")
                
            except ValueError:
                print("\nPlease enter a valid number")
        
        elif choice == '2':
            # Add question
            details = get_question_details()
            success, message = game.add_question(*details)
            print(f"\n{message}")
        
        elif choice == '3':
            # View questions
            print("\nAll Questions:")
            for i, q in enumerate(game.questions, 1):
                q.display(i)
                print(f"Correct Answer: {q.correct_answer}")
                if q.explanation:
                    print(f"Explanation: {q.explanation}")
                print("-" * 40)
        
        elif choice == '4':
            # Exit
            print("\nThank you for playing Quiz Game!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
