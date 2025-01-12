def element_wise_sum(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]
list1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))
if len(list1) == len(list2):
    result = element_wise_sum(list1, list2)
    print(f"Element-wise sum: {result}")
else:
    print("The lists are not of equal length.")