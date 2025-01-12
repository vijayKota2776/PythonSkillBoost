def access_tuple_element():
    my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    index = int(input(f"Enter an index (0 to {len(my_tuple) - 1}): "))
    if 0 <= index < len(my_tuple):
        print(f"The element at index {index} is: {my_tuple[index]}")
    else:
        print("Invalid index! Please enter a valid index within the range.")
access_tuple_element()