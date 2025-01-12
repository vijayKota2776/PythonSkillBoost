def is_perfect_number(number):
    if number <= 0:
        return False
    divisor_sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number
user_number = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(user_number):
    print(f"{user_number} is a Perfect Number.")
else:
    print(f"{user_number} is not a Perfect Number.")
