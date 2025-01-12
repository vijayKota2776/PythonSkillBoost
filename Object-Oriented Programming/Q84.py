class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0
name = input("Enter student's name: ")
student_id = input("Enter student's ID: ")
grades_input = input("Enter student's grades (comma separated): ")
grades = list(map(int, grades_input.split(',')))
student = Student(name, student_id, grades)
avg_grade = student.average_grade()
print(f"Student Name: {student.name}")
print(f"Student ID: {student.student_id}")
print(f"Average Grade: {avg_grade:.2f}")