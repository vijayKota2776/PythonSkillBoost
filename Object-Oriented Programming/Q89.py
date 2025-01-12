class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age 
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value 
        else:
            print("Age cannot be negative.")
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
person = Person("Alice", 30)
person.display()
print(f"Current age: {person.age}")
person.age = 35
person.display()
person.age = -5 
person.display()