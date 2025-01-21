import json
import datetime
from pathlib import Path

class Task:
    """Represents a task in the to-do list."""
    
    def __init__(self, title, description="", due_date=None, priority="medium",
                 completed=False, created_at=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.created_at = created_at or datetime.datetime.now().isoformat()
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary."""
        return cls(
            data['title'],
            data.get('description', ""),
            data.get('due_date'),
            data.get('priority', "medium"),
            data.get('completed', False),
            data.get('created_at')
        )
    
    def __str__(self):
        """String representation of task."""
        status = "✓" if self.completed else "☐"
        priority_symbols = {"high": "❗", "medium": "•", "low": "◦"}
        
        output = [f"{status} {priority_symbols[self.priority]} {self.title}"]
        
        if self.description:
            output.append(f"   {self.description}")
        if self.due_date:
            output.append(f"   Due: {self.due_date}")
        
        return "\n".join(output)

class TodoList:
    """Manages a list of tasks."""
    
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file."""
        try:
            if Path(self.filename).exists():
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data]
                print(f"Loaded {len(self.tasks)} tasks")
            else:
                print("No existing tasks file found")
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    def save_tasks(self):
        """Save tasks to file."""
        try:
            data = [t.to_dict() for t in self.tasks]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            print("Tasks saved successfully")
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        """
        Add a new task.
        Returns: (success, message)
        """
        if not title:
            return False, "Task title is required"
        
        # Validate priority
        if priority not in ["high", "medium", "low"]:
            return False, "Invalid priority level"
        
        # Validate due date format if provided
        if due_date:
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                return False, "Invalid date format. Use YYYY-MM-DD"
        
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()
        return True, "Task added successfully"
    
    def complete_task(self, index):
        """
        Mark a task as completed.
        Returns: (success, message)
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            self.save_tasks()
            return True, f"Marked '{task.title}' as completed"
        return False, "Invalid task index"
    
    def delete_task(self, index):
        """
        Delete a task.
        Returns: (success, message)
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.save_tasks()
            return True, f"Deleted task: {task.title}"
        return False, "Invalid task index"
    
    def get_tasks(self, include_completed=True, sort_by="created"):
        """Get list of tasks with optional filtering and sorting."""
        tasks = self.tasks
        if not include_completed:
            tasks = [t for t in tasks if not t.completed]
        
        if sort_by == "priority":
            priority_order = {"high": 0, "medium": 1, "low": 2}
            return sorted(tasks, key=lambda t: (priority_order[t.priority], t.title))
        elif sort_by == "due_date":
            return sorted(tasks, 
                        key=lambda t: (t.due_date or "9999-99-99", t.title))
        else:  # sort by created_at
            return sorted(tasks, key=lambda t: t.created_at)
    
    def get_statistics(self):
        """Get task statistics."""
        if not self.tasks:
            return "No tasks yet"
        
        stats = ["\nTask Statistics:"]
        
        # Count by status
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.completed)
        pending = total - completed
        
        stats.append(f"Total tasks: {total}")
        stats.append(f"Completed: {completed}")
        stats.append(f"Pending: {pending}")
        
        # Count by priority
        priorities = {"high": 0, "medium": 0, "low": 0}
        for task in self.tasks:
            priorities[task.priority] += 1
        
        stats.append("\nPriority breakdown:")
        for priority, count in priorities.items():
            stats.append(f"  {priority.capitalize()}: {count}")
        
        # Overdue tasks
        today = datetime.date.today()
        overdue = sum(1 for t in self.tasks 
                     if not t.completed and t.due_date and 
                     datetime.datetime.strptime(t.due_date, "%Y-%m-%d").date() < today)
        
        stats.append(f"\nOverdue tasks: {overdue}")
        
        return "\n".join(stats)

def print_menu():
    """Print main menu options."""
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. View Statistics")
    print("6. Exit")

def get_task_details():
    """Get task details from user."""
    print("\nEnter task details:")
    title = input("Title: ").strip()
    description = input("Description (optional): ").strip()
    
    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
    if not due_date:
        due_date = None
    
    print("\nPriority levels:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    while True:
        try:
            priority = int(input("Choose priority (1-3): "))
            if 1 <= priority <= 3:
                priority = ["high", "medium", "low"][priority-1]
                break
        except ValueError:
            pass
        print("Please enter 1, 2, or 3")
    
    return title, description, due_date, priority

def main():
    """To-do list main program."""
    print("Welcome to To-Do List Manager!")
    todo = TodoList()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # View tasks
            print("\nView options:")
            print("1. All tasks")
            print("2. Pending tasks only")
            view_choice = input("Choose option (1-2): ").strip()
            
            print("\nSort by:")
            print("1. Creation date")
            print("2. Priority")
            print("3. Due date")
            sort_choice = input("Choose option (1-3): ").strip()
            
            include_completed = view_choice != '2'
            sort_by = {
                '1': "created",
                '2': "priority",
                '3': "due_date"
            }.get(sort_choice, "created")
            
            tasks = todo.get_tasks(include_completed, sort_by)
            
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks):
                    print(f"\n[{i+1}]")
                    print(task)
            else:
                print("\nNo tasks found")
        
        elif choice == '2':
            # Add task
            details = get_task_details()
            success, message = todo.add_task(*details)
            print(f"\n{message}")
        
        elif choice == '3':
            # Complete task
            tasks = todo.get_tasks(include_completed=False)
            if not tasks:
                print("\nNo pending tasks")
                continue
            
            print("\nPending Tasks:")
            for i, task in enumerate(tasks):
                print(f"\n[{i+1}]")
                print(task)
            
            try:
                index = int(input("\nEnter task number to complete: ")) - 1
                success, message = todo.complete_task(index)
                print(f"\n{message}")
            except ValueError:
                print("\nInvalid input")
        
        elif choice == '4':
            # Delete task
            tasks = todo.get_tasks()
            if not tasks:
                print("\nNo tasks to delete")
                continue
            
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"\n[{i+1}]")
                print(task)
            
            try:
                index = int(input("\nEnter task number to delete: ")) - 1
                success, message = todo.delete_task(index)
                print(f"\n{message}")
            except ValueError:
                print("\nInvalid input")
        
        elif choice == '5':
            # View statistics
            print(todo.get_statistics())
        
        elif choice == '6':
            # Exit
            print("\nThank you for using To-Do List Manager!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
