def string_case_conversion(input_string):
    upper_case = input_string.upper()
    lower_case = input_string.lower()
    title_case = input_string.title()
    
    return {
        "Upper Case": upper_case,
        "Lower Case": lower_case,
        "Title Case": title_case,
    }
user_string = input("Enter a string: ")
converted_cases = string_case_conversion(user_string)
print("\nCase Conversions:")
for case, result in converted_cases.items():
    print(f"{case}: {result}")
