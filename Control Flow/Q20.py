number = int(input("Enter a positive integer: "))
original_number = number
reversed_number = 0
while number > 0:
    last_digit = number % 10 
    reversed_number = reversed_number * 10 + last_digit  
    number = number // 10 
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")