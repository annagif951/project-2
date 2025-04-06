# This script reads a file named 'input.txt', modifies its content, and writes the result to 'output.txt'.
try:
    # Read the original file
    with open('input.txt', 'r') as input_file:
        content = input_file.read()

    # Modify content (convert to uppercase, as an example)
    modified_content = content.upper()

    # Write to a new file
    with open('output.txt', 'w') as output_file:
        output_file.write(modified_content)

    print("File processed and modified successfully!")

except FileNotFoundError:
    print("Error: 'input.txt' not found.")
except IOError:
    print("Error: An error occurred while reading/writing the file.")


    # Error Handling Lab
filename = input("Enter the filename: ")

try:
    # Attempt to open and read the file
    with open(filename, 'r') as file:
        print("File content:\n")
        print(file.read())

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




