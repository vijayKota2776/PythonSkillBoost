def count_occurrences(lst, x):
    count = 0
    for element in lst:
        if element == x:
            count += 1
    return count
numbers = [1, 2, 3, 4, 2, 5, 2, 6]
element_to_count = int(input("Enter the element to count: "))
result = count_occurrences(numbers, element_to_count)
print(f"The element {element_to_count} appears {result} times in the list.")
