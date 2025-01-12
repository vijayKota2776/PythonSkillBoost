def append_to_file(file_name, text):
    try:
        with open(file_name, "a") as file:
            file.write(text + "\n")
        print(f"Text successfully appended to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = "output.txt"
text_to_append = input("Enter the text to append to the file: ")
append_to_file(file_name, text_to_append)
