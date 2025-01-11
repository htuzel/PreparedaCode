# PreparedaCode

A simple script to read file paths, collect content, and save it to an output file.

## Setup

1. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

2. Install dependencies (if any) – currently, there are no additional requirements.

## Usage

1. Create a file named `source_files.txt`.
2. Add file paths (one per line) to `source_files.txt`.
3. Run the script:

    ```bash
    python main.py
    ```

4. The output will be saved in a file named `output.txt` in the same directory.

## Notes

- Ensure the file paths in `source_files.txt` point to valid, existing files.
- Lines in `source_files.txt` that are empty or point to non-existent files will be skipped.
