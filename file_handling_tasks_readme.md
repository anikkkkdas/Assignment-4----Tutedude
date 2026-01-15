# Python File Handling Tasks

This repository contains two simple Python programs that demonstrate basic file handling operations with proper error handling. These tasks focus on reading, writing, appending, and safely managing files using `try-except` blocks.

---

## Task 1: Read a File and Handle Errors

### Description
This program reads data from a text file named `sample.txt` and prints its contents. It also handles the scenario where the file does not exist.

### Features
- Opens and reads a text file
- Reads data line by line
- Gracefully handles `FileNotFoundError`

### What the Code Does
1. Attempts to open `sample.txt` in read mode
2. Reads the first two lines from the file
3. Prints each line with a label
4. Displays a clear error message if the file is missing

### File
- `task1.py`

---

## Task 2: Write and Append Data to a File

### Description
This program interacts with the user to write and append data to a file named `output.txt`, then reads and displays the final content of the file.

### Features
- Takes user input and writes it to a file
- Appends additional user input to the same file
- Reads and displays the final file content
- Handles unexpected errors safely

### What the Code Does
1. Prompts the user for input and writes it to `output.txt`
2. Prompts for additional input and appends it to the file
3. Opens the file in read mode and displays its contents
4. Catches and prints any runtime errors

### File
- `task2.py`
