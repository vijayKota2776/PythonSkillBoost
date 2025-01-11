a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(f"{a} and {b} are the values before swapping")
a = a + b
b = a - b
a = a - b
print(f"{a} and {b} are the values after swapping")