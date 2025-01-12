def is_palindrome(string, case_sensitive=True):
    if not case_sensitive:
        string = string.lower()
    return string == string[::-1]
user_string = input("Enter a string to check if it's a palindrome: ")
case_option = input("Do you want the check to be case-sensitive? (yes/no): ").strip().lower()
case_sensitive = case_option == "yes"
if is_palindrome(user_string, case_sensitive):
    print(f"The string '{user_string}' is a palindrome.")
else:
    print(f"The string '{user_string}' is not a palindrome.")
