def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index  
    return -1  
lst = [4, 2, 7, 1, 9, 5, 8]
target = int(input("Enter the number to search: "))
result = linear_search(lst, target)
if result != -1:
    print(f"The target {target} is found at index {result}.")
else:
    print(f"The target {target} is not found in the list.")
