def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 2 
        binary_str = str(remainder) + binary_str 
        decimal_num //= 2

    return binary_str
decimal_input = int(input("Enter a decimal integer: "))
binary_result = decimal_to_binary(decimal_input)
print(f"The binary equivalent of decimal '{decimal_input}' is: {binary_result}")
