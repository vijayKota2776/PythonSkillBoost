def common(list1, list2):
    common = [element for element in list1 if element in list2]
    return common
list1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))
common_elements_list = common(list1, list2)
print(f"Common elements: {common_elements_list}")