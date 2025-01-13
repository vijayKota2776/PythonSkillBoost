def file_statistics(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        total_lines = len(lines)
        total_words = 0
        total_characters = 0
        for line in lines:
            words = line.split()
            total_words += len(words)
            total_characters += len(line)
        print(f"File Statistics for '{file_name}':")
        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {total_words}")
        print(f"Total Characters (including spaces and newlines): {total_characters}")
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = "sample.txt"
file_statistics(file_name)