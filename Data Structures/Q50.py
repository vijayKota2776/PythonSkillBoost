def set_membership_test():
    names_set = {"Alice", "Bob", "Charlie", "David", "Eve"}
    name_to_check = input("Enter a name to check: ")
    if name_to_check in names_set:
        print(f"{name_to_check} is in the set!")
    else:
        print(f"{name_to_check} is not in the set.")
set_membership_test()