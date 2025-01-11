import os

def get_file_content(file_path):
    """
    Reads and returns the content of the given file path.
    
    Parameters:
        file_path (str): The path to the file.
    
    Returns:
        str or None: The content of the file, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
        return None

def read_file_paths(filepath="source_files.txt"):
    """
    Reads file paths from a specified text file. Each line should contain one file path.
    
    Parameters:
        filepath (str): The path to the file containing file paths.
    
    Returns:
        list: A list of valid file paths.
    """
    if not os.path.isfile(filepath):
        print(f"The file '{filepath}' does not exist.")
        return []
    
    file_paths = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            path = line.strip()
            if not path:
                print(f"Line {line_number} in '{filepath}' is empty. Skipping.")
                continue
            if not os.path.isfile(path):
                print(f"Line {line_number}: The path '{path}' does not point to a valid file. Skipping.")
                continue
            file_paths.append(path)
    
    return file_paths

def create_output_file(file_paths, output_filename="output.txt"):
    """
    Creates the output file with the specified format.
    
    Parameters:
        file_paths (list): A list of file paths to include in the output.
        output_filename (str): The name of the output file.
    """
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write("this is my code:\n")
            for path in file_paths:
                content = get_file_content(path)
                if content is not None:
                    outfile.write(f"{path}:\n{content}\n\n")  # Added extra newline for readability
            
            # Add the instructions at the end
            outfile.write("\nI want you to do these:\n")
            outfile.write("\n1:\n")
            outfile.write("\n2:\n")
            outfile.write(
                "\nInstructions: Provide fully complete code for files that have changes. If a file remains unchanged, simply list its name and state 'no change'. "
                "Do not include unchanged code in your response—only specify the filenames. For any file that has been modified, include the entire updated code for that file.\n"
            )
        print(f"Output successfully written to '{output_filename}'.")
    except Exception as e:
        print(f"Failed to write to '{output_filename}': {e}")

def main():
    print("=== Code Collector from 'source_files.txt' ===")
    input_filepath = "source_files.txt"
    file_paths = read_file_paths(input_filepath)
    if file_paths:
        create_output_file(file_paths)
    else:
        print("No valid file paths were provided. Exiting.")

if __name__ == "__main__":
    main()
