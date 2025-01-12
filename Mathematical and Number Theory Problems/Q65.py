def binary_to_decimal(binary_str):
    decimal_value = 0
    power = 0
    for digit in reversed(binary_str):
        decimal_value += int(digit) * (2 ** power)
        power += 1
    return decimal_value
binary_input = input("Enter a binary string: ")
if all(char in '01' for char in binary_input):
    decimal_result = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of binary '{binary_input}' is: {decimal_result}")
else:
    print("Invalid input! Please enter a valid binary string containing only 0s and 1s.")
