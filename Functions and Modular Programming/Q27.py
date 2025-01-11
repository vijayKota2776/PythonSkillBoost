def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) / gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
