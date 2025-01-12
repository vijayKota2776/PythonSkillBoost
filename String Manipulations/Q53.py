def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
user_string = input("Enter a string to count the vowels: ")
vowel_count = count_vowels(user_string)
print(f"The number of vowels in the string is: {vowel_count}")
