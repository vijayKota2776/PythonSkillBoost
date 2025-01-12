def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_strong_number(number):
    sum_of_factorials = 0
    temp = number
    while temp > 0:
        digit = temp % 10 
        sum_of_factorials += factorial(digit) 
        temp //= 10
    return sum_of_factorials == number
user_number = int(input("Enter a number to check if it's a strong number: "))
if is_strong_number(user_number):
    print(f"{user_number} is a Strong Number.")
else:
    print(f"{user_number} is not a Strong Number.")
