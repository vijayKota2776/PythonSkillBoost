def write_to_file():
    user_input = input("Enter a string to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("The string has been written to 'output.txt'.")
write_to_file()
