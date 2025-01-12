def sum_of_digits(number):
    number = abs(number)
    
    digit_sum = 0
    
    while number > 0:
        digit_sum += number % 10
        number //= 10 
    
    return digit_sum
user_number = int(input("Enter an integer: "))
result = sum_of_digits(user_number)
print(f"The sum of the digits of {user_number} is: {result}")
