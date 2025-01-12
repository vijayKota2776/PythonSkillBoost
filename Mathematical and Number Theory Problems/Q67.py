def prime_factors(number):
    factors = []
    divisor = 2 
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor 
        divisor += 1 
    return factors
num = int(input("Enter an integer to find its prime factors: "))

if num < 2:
    print("Please enter an integer greater than 1.")
else:
    result = prime_factors(num)
    print(f"The prime factors of {num} are: {result}")
