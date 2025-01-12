def student_grade():
    grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "C",
        "David": "B",
        "vijay": "f"
    }
    student_name = input("Enter the student's name: ")
    if student_name in grades:
        print(f"{student_name}'s grade is: {grades[student_name]}")
    else:
        print(f"Student {student_name} not found in the list.")
student_grade()