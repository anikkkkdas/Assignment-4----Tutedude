'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''

try:
    with open("output.txt", "w") as fh:
        user_input = input("Enter text to write to the file: ")
        fh.write(user_input + "\n")
        print("Data Successfully written to output.txt")
    with open("output.txt", "a") as fh:
        user_add = input("Enter additional text to append: ")
        fh.write(user_add + "\n")
        print("Data Successfully appended")
    with open("output.txt", "r") as fh:
        content = fh.read()
        print("Final content of output.txt:")
        print(content)
except Exception as error:
    print(f"An error occurred: {error}")
