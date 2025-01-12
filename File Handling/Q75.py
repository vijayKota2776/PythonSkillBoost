def count_words_in_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            words = content.split()
        return len(words)
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist. Please provide a valid file.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
file_name = input("Enter the file name (including extension): ")
word_count = count_words_in_file(file_name)
if word_count > 0:
    print(f"The file '{file_name}' contains {word_count} words.")
