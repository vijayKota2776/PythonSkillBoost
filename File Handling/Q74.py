def count_lines_in_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return len(lines)
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist. Please provide a valid file.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
file_name = input("Enter the file name (including extension): ")
line_count = count_lines_in_file(file_name)
if line_count > 0:
    print(f"The file '{file_name}' contains {line_count} lines.")
