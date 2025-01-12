def copy_file(source_file, destination_file):
    try:
        with open(source_file, "r") as src:
            content = src.read()
        with open(destination_file, "w") as dest:
            dest.write(content)
        
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    
    except FileNotFoundError:
        print(f"The source file '{source_file}' does not exist. Please provide a valid file.")
    except Exception as e:
        print(f"An error occurred: {e}")
source = input("Enter the source file name (including extension): ")
destination = input("Enter the destination file name (including extension): ")
copy_file(source, destination)
