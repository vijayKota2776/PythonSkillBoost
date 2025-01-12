def reverse_list(lst):
    lst.reverse()
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
reverse_list(numbers)
print(f"Reversed list: {numbers}")