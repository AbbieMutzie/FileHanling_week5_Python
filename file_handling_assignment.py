
# Step 1: Create and write to the file
file_name = "my_file.txt"

# Writing a Python script for file handling.
try:
    # Create and open the file in write mode
    with open(file_name, 'w') as file:
        # Writing three lines of text (strings and numbers)
        file.write("This is the first line.\n")
        file.write("Here is a number: 42\n")
        file.write("The third line is here.\n")

    # Step 2: Read and display the contents of the file
    with open(file_name, 'r') as file:
        print("File content after write:")
        print(file.read())

    # Step 3: Open the file in append mode and add more content
    with open(file_name, 'a') as file:
        file.write("This is an appended line.\n")
        file.write("Another number: 100\n")
        file.write("Last line after appending.\n")

    # Read the file again to display the updated content
    with open(file_name, 'r') as file:
        print("File content after append:")
        print(file.read())

# Step 4: Error handling
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except PermissionError:
    print(f"Permission denied to access the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
