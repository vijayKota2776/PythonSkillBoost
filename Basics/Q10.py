principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time (in years): "))
SI = (principal * rate * time) / 100
print(f"This is the simple interest: {SI}")