def word_count():
    input_string = input("Enter a string: ")
    words = input_string.lower().split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print("Word count dictionary:", word_dict)
word_count()