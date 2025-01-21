class Room:
    """Represents a room in the adventure game."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}  # direction: room
        self.items = []
    
    def add_connection(self, direction, room):
        """Add a connection to another room."""
        self.connections[direction] = room
    
    def get_connections(self):
        """Get available directions and connected rooms."""
        return self.connections
    
    def add_item(self, item):
        """Add an item to the room."""
        self.items.append(item)
    
    def remove_item(self, item):
        """Remove an item from the room."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

class Player:
    """Represents the player in the game."""
    
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.current_room = None
    
    def move(self, direction):
        """
        Move to a connected room.
        Returns: (success, message)
        """
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            return True, f"You move {direction}."
        return False, "You can't go that way!"
    
    def take_item(self, item):
        """
        Take an item from current room.
        Returns: (success, message)
        """
        if item in self.current_room.items:
            self.current_room.remove_item(item)
            self.inventory.append(item)
            return True, f"You take the {item}."
        return False, f"There is no {item} here!"
    
    def drop_item(self, item):
        """
        Drop an item in current room.
        Returns: (success, message)
        """
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
            return True, f"You drop the {item}."
        return False, f"You don't have a {item}!"
    
    def show_inventory(self):
        """Show player's inventory."""
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory: " + ", ".join(self.inventory)

class AdventureGame:
    """Manages the text adventure game."""
    
    def __init__(self):
        self.rooms = {}
        self.player = None
        self.game_over = False
        self.setup_game()
    
    def setup_game(self):
        """Set up the game world."""
        # Create rooms
        self.rooms = {
            'start': Room('Forest Clearing', 
                         'You are in a peaceful forest clearing. Sunlight filters through the leaves above.'),
            'cave': Room('Dark Cave', 
                        'You are in a dark cave. Water drips from the ceiling.'),
            'bridge': Room('Wooden Bridge', 
                          'You are on an old wooden bridge crossing a deep ravine.'),
            'tower': Room('Ancient Tower', 
                         'You are in an ancient stone tower. Dust covers everything.'),
            'garden': Room('Overgrown Garden', 
                          'You are in an overgrown garden. Colorful flowers bloom among the weeds.')
        }
        
        # Add connections
        self.rooms['start'].add_connection('north', self.rooms['cave'])
        self.rooms['start'].add_connection('east', self.rooms['bridge'])
        self.rooms['cave'].add_connection('south', self.rooms['start'])
        self.rooms['cave'].add_connection('east', self.rooms['tower'])
        self.rooms['bridge'].add_connection('west', self.rooms['start'])
        self.rooms['bridge'].add_connection('north', self.rooms['tower'])
        self.rooms['tower'].add_connection('west', self.rooms['cave'])
        self.rooms['tower'].add_connection('south', self.rooms['bridge'])
        self.rooms['tower'].add_connection('east', self.rooms['garden'])
        self.rooms['garden'].add_connection('west', self.rooms['tower'])
        
        # Add items
        self.rooms['start'].add_item('map')
        self.rooms['cave'].add_item('torch')
        self.rooms['bridge'].add_item('rope')
        self.rooms['tower'].add_item('key')
        self.rooms['garden'].add_item('flower')
    
    def start_game(self):
        """Start a new game."""
        print("\nWelcome to the Text Adventure!")
        name = input("What is your name, adventurer? ").strip()
        
        self.player = Player(name)
        self.player.current_room = self.rooms['start']
        self.game_over = False
        
        print(f"\nWelcome, {name}! Your adventure begins...")
        self.show_current_location()
    
    def show_current_location(self):
        """Show current room description and available actions."""
        room = self.player.current_room
        print(f"\n=== {room.name} ===")
        print(room.description)
        
        # Show items in room
        if room.items:
            print("You see:", ", ".join(room.items))
        
        # Show available directions
        directions = list(room.get_connections().keys())
        print("You can go:", ", ".join(directions))
    
    def handle_command(self, command):
        """
        Handle player command.
        Returns: (success, message)
        """
        words = command.lower().split()
        if not words:
            return False, "Please enter a command."
        
        action = words[0]
        
        if action == "go":
            if len(words) < 2:
                return False, "Go where?"
            return self.player.move(words[1])
        
        elif action == "take":
            if len(words) < 2:
                return False, "Take what?"
            return self.player.take_item(words[1])
        
        elif action == "drop":
            if len(words) < 2:
                return False, "Drop what?"
            return self.player.drop_item(words[1])
        
        elif action == "inventory":
            return True, self.player.show_inventory()
        
        elif action == "look":
            self.show_current_location()
            return True, ""
        
        elif action == "help":
            return True, self.get_help()
        
        elif action == "quit":
            self.game_over = True
            return True, "Thanks for playing!"
        
        return False, "I don't understand that command."
    
    def get_help(self):
        """Get list of available commands."""
        return """
Available commands:
- go [direction]: Move in a direction (north, south, east, west)
- take [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- inventory: Show your inventory
- look: Look around the current room
- help: Show this help message
- quit: Exit the game
"""

def main():
    """Text adventure game main program."""
    game = AdventureGame()
    game.start_game()
    
    while not game.game_over:
        command = input("\nWhat would you like to do? ").strip()
        success, message = game.handle_command(command)
        
        if message:
            print(message)

if __name__ == "__main__":
    main()
