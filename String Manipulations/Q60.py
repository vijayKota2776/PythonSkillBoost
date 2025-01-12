def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
user_string = input("Enter a string: ")
char_freq = character_frequency(user_string)
print("\nCharacter Frequencies:")
for char, count in char_freq.items():
    print(f"'{char}': {count}")
