def search_word_in_file(file_name, word):
    line_numbers = []
    try:
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, start=1):
                if word.lower() in line.lower():
                    line_numbers.append(line_num)
        return line_numbers
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist. Please provide a valid file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
file_name = input("Enter the file name (including extension): ")
word = input("Enter the word to search for: ")
lines_with_word = search_word_in_file(file_name, word)
if lines_with_word:
    print(f"The word '{word}' appears in the following line(s): {lines_with_word}")
elif lines_with_word == []:
    print(f"The word '{word}' does not appear in the file.")
