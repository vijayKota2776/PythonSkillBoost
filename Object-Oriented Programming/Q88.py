class MyClass:
    class_variable = "I am a class variable"
    
    def __init__(self, name):
        self.name = name
    def instance_method(self):
        print(f"Hello, {self.name}! I can access the instance variable and class variable.")
        print(f"Class Variable: {self.class_variable}")
    @classmethod
    def class_method(cls):
        print(f"Hello! I am a class method. I can access the class variable: {cls.class_variable}")
    @staticmethod
    def static_method():
        print("Hello! I am a static method. I cannot access instance or class variables.")
obj = MyClass("Alice")
obj.instance_method()
obj.class_method()
obj.static_method()
MyClass.class_method()
MyClass.static_method()