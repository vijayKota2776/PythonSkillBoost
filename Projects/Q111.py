import random
import string

class PasswordGenerator:
    """Password generator with customizable options."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length, use_upper=True, use_digits=True, 
                         use_special=True, min_of_each=1):
        """
        Generate a random password with specified requirements.
        
        Args:
            length: Length of password
            use_upper: Include uppercase letters
            use_digits: Include digits
            use_special: Include special characters
            min_of_each: Minimum count of each selected character type
        """
        if length < 1:
            return None, "Length must be positive"
        
        # Calculate minimum required length
        min_length = min_of_each  # Always include lowercase
        if use_upper:
            min_length += min_of_each
        if use_digits:
            min_length += min_of_each
        if use_special:
            min_length += min_of_each
        
        if length < min_length:
            return None, f"Length must be at least {min_length} for given requirements"
        
        # Build character pool and ensure minimum requirements
        password = []
        char_types = [(self.lowercase, min_of_each)]  # Always include lowercase
        
        if use_upper:
            char_types.append((self.uppercase, min_of_each))
        if use_digits:
            char_types.append((self.digits, min_of_each))
        if use_special:
            char_types.append((self.special, min_of_each))
        
        # Add minimum required characters of each type
        for char_set, min_count in char_types:
            password.extend(random.choice(char_set) for _ in range(min_count))
        
        # Build pool for remaining characters
        pool = self.lowercase
        if use_upper:
            pool += self.uppercase
        if use_digits:
            pool += self.digits
        if use_special:
            pool += self.special
        
        # Fill remaining length with random characters
        remaining = length - len(password)
        password.extend(random.choice(pool) for _ in range(remaining))
        
        # Shuffle the password
        random.shuffle(password)
        
        return ''.join(password), None
    
    def analyze_password_strength(self, password):
        """Analyze the strength of a password."""
        if not password:
            return "No password to analyze"
        
        strength = 0
        analysis = []
        
        # Length check
        if len(password) >= 12:
            strength += 3
            analysis.append("✓ Excellent length (12+ characters)")
        elif len(password) >= 8:
            strength += 2
            analysis.append("✓ Good length (8+ characters)")
        else:
            analysis.append("✗ Password is too short (< 8 characters)")
        
        # Character type checks
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.special for c in password)
        
        if has_lower:
            strength += 1
            analysis.append("✓ Contains lowercase letters")
        else:
            analysis.append("✗ Missing lowercase letters")
        
        if has_upper:
            strength += 1
            analysis.append("✓ Contains uppercase letters")
        else:
            analysis.append("✗ Missing uppercase letters")
        
        if has_digit:
            strength += 1
            analysis.append("✓ Contains numbers")
        else:
            analysis.append("✗ Missing numbers")
        
        if has_special:
            strength += 1
            analysis.append("✓ Contains special characters")
        else:
            analysis.append("✗ Missing special characters")
        
        # Overall strength rating
        if strength >= 6:
            rating = "Strong"
        elif strength >= 4:
            rating = "Moderate"
        else:
            rating = "Weak"
        
        return f"Strength: {rating}\n" + "\n".join(analysis)

def print_password_requirements():
    """Print password generation options and requirements."""
    print("\nPassword Generation Options:")
    print("1. Length: Minimum recommended length is 12 characters")
    print("2. Character Types:")
    print("   - Lowercase letters (a-z) [always included]")
    print("   - Uppercase letters (A-Z)")
    print("   - Numbers (0-9)")
    print("   - Special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)")
    print("3. Minimum Requirements:")
    print("   - At least one character of each selected type")

def get_user_preferences():
    """Get password generation preferences from user."""
    try:
        print_password_requirements()
        
        length = int(input("\nEnter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        return length, use_upper, use_digits, use_special
    
    except ValueError:
        print("Please enter a valid number for length!")
        return None, None, None, None

def main():
    """Password generator main program."""
    print("Welcome to Password Generator!")
    generator = PasswordGenerator()
    
    while True:
        # Get user preferences
        prefs = get_user_preferences()
        if prefs[0] is None:
            continue
        
        length, use_upper, use_digits, use_special = prefs
        
        # Generate password
        password, error = generator.generate_password(
            length, use_upper, use_digits, use_special)
        
        if error:
            print(f"\nError: {error}")
            continue
        
        # Display results
        print("\nGenerated Password:", password)
        print("\nPassword Analysis:")
        print(generator.analyze_password_strength(password))
        
        # Ask to generate another
        if input("\nGenerate another password? (y/n): ").lower() != 'y':
            break
    
    print("\nThank you for using Password Generator!")

if __name__ == "__main__":
    main()
