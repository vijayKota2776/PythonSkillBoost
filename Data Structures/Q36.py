numbers = list(map(int, input("Enter integers separated by spaces (with duplicates): ").split()))
unique_numbers = list(set(numbers))
print(f"Original list: {numbers}")
print(f"List with duplicates removed: {unique_numbers}")