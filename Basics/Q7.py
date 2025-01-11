letter = input("Enter a single letter: ")
if len(letter) == 1 and letter.isalpha():
    if letter in "aeiou":  
        print(f"'{letter}' is a vowel.")
    else:
        print(f"'{letter}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic letter.")