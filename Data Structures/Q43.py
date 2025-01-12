def check_element_in_tuple():
    my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
    element = input("Enter an element to check if it exists in the tuple: ")
    if element in my_tuple:
        print(f"The element '{element}' exists in the tuple.")
    else:
        print(f"The element '{element}' does not exist in the tuple.")
check_element_in_tuple()