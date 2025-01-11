a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter an operation (+, -, *, /): ")
if c == "+":
    print(f"The sum is {a + b}")
elif c == "-":
    print(f"The difference is {a - b}")
elif c == "*":
    print(f"The product is {a * b}")
elif c == "/":
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The division result is {a / b}")
else:
    print("Invalid operator. Please enter one of +, -, *, /.")