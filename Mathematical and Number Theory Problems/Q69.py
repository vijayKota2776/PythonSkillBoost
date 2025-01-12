from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_range(n):
    if n < 1:
        return None
    
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
        
    return result
n = int(input("Enter the upper limit of the range [1..n]: "))
if n > 0:
    lcm_result = lcm_of_range(n)
    print(f"The LCM of numbers from 1 to {n} is: {lcm_result}")
else:
    print("Please enter a positive integer.")
