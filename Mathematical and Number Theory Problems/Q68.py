def number_to_words(number):
    digit_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    if number == 0:
        return digit_to_word[0]

    words = []
    is_negative = False
    if number < 0:
        is_negative = True
    while number > 0:
        digit = number % 10 
        words.append(digit_to_word[digit])
        number //= 10 

    if is_negative:
        words.append("negative") 
    return " ".join(reversed(words))
user_input = int(input("Enter an integer to convert to words: "))
result = number_to_words(user_input)
print(f"The number in words is: {result}")
