def tuple_to_list_and_back():
    my_tuple = tuple(input("Enter comma-separated values for the tuple: ").split(","))
    print(f"Original Tuple: {my_tuple}")
    my_list = list(my_tuple)
    print(f"Converted List: {my_list}")
    modification = input("Do you want to modify the list? (yes/no): ").lower()
    if modification == 'yes':
        action = input("What would you like to do? (add/remove/change): ").lower()
        
        if action == 'add':
            item = input("Enter the item to add: ")
            my_list.append(item)
            print(f"List after adding: {my_list}")
        
        elif action == 'remove':
            item = input("Enter the item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"List after removing: {my_list}")
            else:
                print("Item not found in the list.")
        
        elif action == 'change':
            index = int(input(f"Enter the index (0 to {len(my_list) - 1}) to change: "))
            if 0 <= index < len(my_list):
                new_value = input("Enter the new value: ")
                my_list[index] = new_value
                print(f"List after changing: {my_list}")
            else:
                print("Invalid index.")
        else:
            print("Invalid action.")
    modified_tuple = tuple(my_list)
    print(f"Modified Tuple: {modified_tuple}")
tuple_to_list_and_back()