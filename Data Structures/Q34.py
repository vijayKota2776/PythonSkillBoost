numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
total_sum = sum(numbers)
average = total_sum / len(numbers) if numbers else 0
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")