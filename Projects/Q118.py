import re

class EmailSlicer:
    """Analyzes and slices email addresses into components."""
    
    def __init__(self):
        # Regular expression for validating email addresses
        self.email_pattern = re.compile(r"""
            ^[a-zA-Z0-9._%+-]+       # username
            @                        # @ symbol
            [a-zA-Z0-9.-]+          # domain name
            \.[a-zA-Z]{2,}$         # domain suffix
        """, re.VERBOSE)
    
    def validate_email(self, email):
        """
        Validate email address format.
        Returns: (is_valid, message)
        """
        if not email:
            return False, "Email cannot be empty"
        
        if not self.email_pattern.match(email):
            return False, "Invalid email format"
        
        return True, "Valid email address"
    
    def slice_email(self, email):
        """
        Slice email into its components.
        Returns: (username, domain, analysis)
        """
        is_valid, message = self.validate_email(email)
        if not is_valid:
            return None, None, message
        
        # Split email into username and domain
        username, domain = email.split('@')
        
        # Analyze the email
        analysis = self.analyze_email(username, domain)
        
        return username, domain, analysis
    
    def analyze_email(self, username, domain):
        """Analyze email components in detail."""
        analysis = []
        
        # Analyze username
        analysis.append("\nUsername Analysis:")
        analysis.append(f"Length: {len(username)} characters")
        
        if '.' in username:
            analysis.append("Contains dots (possibly a name format)")
        if '_' in username:
            analysis.append("Contains underscores")
        if any(c.isdigit() for c in username):
            analysis.append("Contains numbers")
        
        # Common username patterns
        if username.replace('.', '').isalpha():
            analysis.append("Appears to be name-based")
        elif username.isalnum():
            analysis.append("Alphanumeric format")
        
        # Analyze domain
        analysis.append("\nDomain Analysis:")
        domain_parts = domain.split('.')
        
        if len(domain_parts) > 2:
            analysis.append("Subdomain structure:")
            for i, part in enumerate(domain_parts[:-1], 1):
                analysis.append(f"  Level {i}: {part}")
        
        analysis.append(f"Top-level domain: .{domain_parts[-1]}")
        
        # Common domain types
        tld = domain_parts[-1].lower()
        if tld in ['com', 'net', 'org']:
            analysis.append("Generic top-level domain")
        elif len(tld) == 2:
            analysis.append("Country code top-level domain")
        elif len(tld) > 3:
            analysis.append("Special purpose domain")
        
        return "\n".join(analysis)
    
    def format_email(self, username, domain):
        """Format email components for display."""
        if not username or not domain:
            return ""
        
        output = []
        
        # Username section
        output.append("┌─ Email Address ─┐")
        output.append(f"  {username}@{domain}")
        output.append("└─────────────────┘")
        
        # Components section
        output.append("\n┌─ Components ─┐")
        output.append(f"  Username: {username}")
        output.append(f"  Domain: {domain}")
        output.append("└─────────────┘")
        
        return "\n".join(output)

def print_menu():
    """Print main menu options."""
    print("\nEmail Slicer Menu:")
    print("1. Slice Email")
    print("2. Validate Email")
    print("3. Exit")

def get_email_input():
    """Get email address from user."""
    return input("\nEnter an email address: ").strip()

def main():
    """Email slicer main program."""
    print("Welcome to Email Slicer!")
    slicer = EmailSlicer()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Slice email
            email = get_email_input()
            username, domain, analysis = slicer.slice_email(email)
            
            if username and domain:
                print("\nEmail successfully sliced!")
                print(slicer.format_email(username, domain))
                print(analysis)
            else:
                print(f"\nError: {analysis}")
        
        elif choice == '2':
            # Validate email
            email = get_email_input()
            is_valid, message = slicer.validate_email(email)
            
            print(f"\nValidation result: {message}")
            if is_valid:
                print("✓ Email format is correct")
            else:
                print("✗ Email format is incorrect")
        
        elif choice == '3':
            # Exit
            print("\nThank you for using Email Slicer!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
