class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team_size = team_size
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")
employee = Employee("John Doe", "E123", 50000)
print("Employee Info:")
employee.display_info()
print()
manager = Manager("Alice Smith", "M456", 75000, "Sales", 10)
print("Manager Info:")
manager.display_info()