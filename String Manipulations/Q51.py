def reverse_string_with_loop():
    user_string = input("Enter a string to reverse: ")
    reversed_string = ""
    for char in user_string:
        reversed_string = char + reversed_string
    print(f"The reversed string is: {reversed_string}")
reverse_string_with_loop()
