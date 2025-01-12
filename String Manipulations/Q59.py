def count_special_characters(input_string):
    special_characters = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~`"
    count = 0

    for char in input_string:
        if char in special_characters:
            count += 1

    return count
user_string = input("Enter a string: ")
special_char_count = count_special_characters(user_string)
print(f"\nThe number of special characters in the string is: {special_char_count}")
