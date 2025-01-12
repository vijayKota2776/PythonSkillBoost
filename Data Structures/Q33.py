numbers = list(map(int, input("Enter unique integers separated by spaces: ").split()))
if len(numbers) < 2:
    print("The list must have at least two unique integers.")
else:
    numbers.sort(reverse=True)
    second = numbers[1]
    print(f"The second largest element is: {second}")