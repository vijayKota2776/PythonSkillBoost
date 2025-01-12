def remove_blank_lines(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
        non_blank_lines = [line for line in lines if line.strip() != ""]
        
        with open(output_file, "w") as file:
            file.writelines(non_blank_lines)
        print(f"Blank lines removed. Content written to '{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
input_file_name = "input.txt"
output_file_name = "output_no_blank_lines.txt"
remove_blank_lines(input_file_name, output_file_name)
