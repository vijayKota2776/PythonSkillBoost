import json
import re
from pathlib import Path

class Contact:
    """Represents a contact with name, phone number, and email."""
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def to_dict(self):
        """Convert contact to dictionary."""
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create contact from dictionary."""
        return cls(data['name'], data['phone'], data['email'])
    
    def __str__(self):
        """String representation of contact."""
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class ContactBook:
    """Manages a collection of contacts with file storage."""
    
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from file."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(c) for c in data]
                print(f"Loaded {len(self.contacts)} contacts")
            else:
                print("No existing contacts file found")
        except Exception as e:
            print(f"Error loading contacts: {e}")
    
    def save_contacts(self):
        """Save contacts to file."""
        try:
            data = [c.to_dict() for c in self.contacts]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            print("Contacts saved successfully")
        except Exception as e:
            print(f"Error saving contacts: {e}")
    
    def add_contact(self, name, phone, email):
        """
        Add a new contact.
        Returns: (success, message)
        """
        # Validate input
        if not name or not phone or not email:
            return False, "All fields are required"
        
        # Validate phone number (simple validation)
        phone = re.sub(r'\D', '', phone)  # Remove non-digits
        if not 7 <= len(phone) <= 15:
            return False, "Invalid phone number length"
        
        # Validate email (simple validation)
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return False, "Invalid email format"
        
        # Check for duplicates
        if any(c.phone == phone for c in self.contacts):
            return False, "Phone number already exists"
        if any(c.email == email for c in self.contacts):
            return False, "Email already exists"
        
        # Add contact
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()
        return True, "Contact added successfully"
    
    def search_contacts(self, query):
        """
        Search contacts by name, phone, or email.
        Returns: list of matching contacts
        """
        query = query.lower()
        matches = []
        
        for contact in self.contacts:
            if (query in contact.name.lower() or
                query in contact.phone or
                query in contact.email.lower()):
                matches.append(contact)
        
        return matches
    
    def delete_contact(self, index):
        """
        Delete contact by index.
        Returns: (success, message)
        """
        if 0 <= index < len(self.contacts):
            contact = self.contacts.pop(index)
            self.save_contacts()
            return True, f"Deleted contact: {contact.name}"
        return False, "Invalid contact index"
    
    def edit_contact(self, index, name=None, phone=None, email=None):
        """
        Edit contact by index.
        Returns: (success, message)
        """
        if not (0 <= index < len(self.contacts)):
            return False, "Invalid contact index"
        
        contact = self.contacts[index]
        
        if name:
            contact.name = name
        if phone:
            # Validate phone
            phone = re.sub(r'\D', '', phone)
            if not 7 <= len(phone) <= 15:
                return False, "Invalid phone number length"
            if any(c.phone == phone and c != contact for c in self.contacts):
                return False, "Phone number already exists"
            contact.phone = phone
        if email:
            # Validate email
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                return False, "Invalid email format"
            if any(c.email == email and c != contact for c in self.contacts):
                return False, "Email already exists"
            contact.email = email
        
        self.save_contacts()
        return True, "Contact updated successfully"

def print_menu():
    """Print main menu options."""
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contacts")
    print("3. List All Contacts")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_contact_details():
    """Get contact details from user."""
    print("\nEnter contact details:")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    return name, phone, email

def print_contacts(contacts, header="Contacts:"):
    """Print list of contacts."""
    if not contacts:
        print("No contacts found")
        return
    
    print(f"\n{header}")
    for i, contact in enumerate(contacts):
        print(f"\n[{i+1}]")
        print(contact)

def main():
    """Contact book main program."""
    print("Welcome to Contact Book!")
    book = ContactBook()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # Add contact
            name, phone, email = get_contact_details()
            success, message = book.add_contact(name, phone, email)
            print(f"\n{message}")
        
        elif choice == '2':
            # Search contacts
            query = input("\nEnter search term: ").strip()
            matches = book.search_contacts(query)
            print_contacts(matches, f"Search results for '{query}':")
        
        elif choice == '3':
            # List all contacts
            print_contacts(book.contacts)
        
        elif choice == '4':
            # Edit contact
            print_contacts(book.contacts)
            try:
                index = int(input("\nEnter contact number to edit: ")) - 1
                name, phone, email = get_contact_details()
                success, message = book.edit_contact(index, name, phone, email)
                print(f"\n{message}")
            except ValueError:
                print("\nInvalid input")
        
        elif choice == '5':
            # Delete contact
            print_contacts(book.contacts)
            try:
                index = int(input("\nEnter contact number to delete: ")) - 1
                success, message = book.delete_contact(index)
                print(f"\n{message}")
            except ValueError:
                print("\nInvalid input")
        
        elif choice == '6':
            # Exit
            print("\nThank you for using Contact Book!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
