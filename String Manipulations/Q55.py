def remove_spaces(string):
    return string.replace(" ", "")
user_string = input("Enter a string: ")
result = remove_spaces(user_string)
print(f"The string without spaces is: '{result}'")
