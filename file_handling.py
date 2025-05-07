def modify_file_content(content):
    """Modify the file content — here, we convert it to uppercase."""
    return content.upper()

def read_and_write_file():
    
    input_filename = input("Enter the name of the file to read: ")

    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.read()

        
        modified_content = modify_file_content(content)

        
        output_filename = "modified_" + input_filename

        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")


read_and_write_file()
