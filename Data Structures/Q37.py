list1 = list(map(int, input("Enter the first list of integers (separated by spaces): ").split()))
list2 = list(map(int, input("Enter the second list of integers (separated by spaces): ").split()))
concatenated = list1 + list2
print(f"First list: {list1}")
print(f"Second list: {list2}")
print(f"Concatenated list: {concatenated}")