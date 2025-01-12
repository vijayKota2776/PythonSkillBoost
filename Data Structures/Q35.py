numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
positive_count = 0
negative_count = 0
zero_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")