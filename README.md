# PreparedaCode

A simple script to read file paths, collect their content, and format it into a single output file—perfectly prepared to feed into a language model (LLM).

## Setup

1. Create a virtual environment and activate it:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

2. Install dependencies (if any) – currently, there are no additional requirements.

## Usage

1. Open the provided `source_files.txt` file.
2. Update it with your file or directory paths (one per line) as needed.
3. Run the script:

    ```bash
    python main.py
    ```

4. The output will be saved in a file named `output.txt` in the same directory.

## Notes

- Ensure the file paths in `source_files.txt` point to valid, existing files or directories.
- If a directory path is provided, all files within that directory (including subdirectories) will be recursively processed.
- Lines in `source_files.txt` that are empty or point to non-existent files/directories will be skipped.

This script makes it easy to consolidate multiple files into a single, LLM-friendly format. 🚀
