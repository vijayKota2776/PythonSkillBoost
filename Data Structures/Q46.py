def print_keys_values():
    student_info = {
        "Alice": 25,
        "Bob": 22,
        "Charlie": 23,
        "David": 24
    }
    print("Keys (Student Names):")
    for key in student_info.keys():
        print(key)
    print("\nValues (Ages):")
    for value in student_info.values():
        print(value)
print_keys_values()