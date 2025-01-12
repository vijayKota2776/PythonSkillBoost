def find_longest_line(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        longest_line = max(lines, key=len)
        return longest_line.strip(), len(longest_line.strip())
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist. Please provide a valid file.")
        return None, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, 0
file_name = input("Enter the file name (including extension): ")
longest_line, line_length = find_longest_line(file_name)
if longest_line:
    print(f"The longest line in the file is:\n{longest_line}")
    print(f"Length of the longest line: {line_length} characters.")
