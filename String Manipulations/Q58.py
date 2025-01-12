def capitalize_every_word(input_string):
    return input_string.title()
user_string = input("Enter a string: ")
result = capitalize_every_word(user_string)
print(f"\nThe capitalized string is:\n{result}")
