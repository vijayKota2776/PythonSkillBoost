def longest_word_in_sentence(sentence):
    words = sentence.split() 
    if not words:
        return None
    longest_word = max(words, key=len) 
    return longest_word
sentence = input("Enter a sentence: ")
longest_word = longest_word_in_sentence(sentence)
if longest_word:
    print(f"The longest word in the sentence is: '{longest_word}'")
else:
    print("The sentence is empty. Please provide a valid sentence.")
